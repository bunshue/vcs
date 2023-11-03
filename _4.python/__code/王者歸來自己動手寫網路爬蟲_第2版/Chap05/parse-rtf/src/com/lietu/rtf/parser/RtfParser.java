package com.lietu.rtf.parser;

import java.nio.ByteBuffer;
import java.nio.CharBuffer;
import java.nio.charset.CharacterCodingException;
import java.nio.charset.Charset;
import java.nio.charset.CharsetDecoder;
import java.util.Hashtable;
import java.util.Stack;

import com.lietu.rtf.IRtfParserListener;
import com.lietu.rtf.IRtfSource;
import com.lietu.rtf.IRtfTag;
import com.lietu.rtf.RtfSpec;
import com.lietu.rtf.model.RtfText;
import com.lietu.rtf.sys.RtfTag;

public final class RtfParser extends RtfParserBase {
	// ----------------------------------------------------------------------
	public RtfParser() {
	} // RtfParser

	// ----------------------------------------------------------------------
	public RtfParser(IRtfParserListener... listeners) throws Exception {
		super(listeners);
	} // RtfParser

	// ----------------------------------------------------------------------
	protected void DoParse(IRtfSource rtfTextSource) throws Exception {
		NotifyParseBegin();
		try {
			ParseRtf(rtfTextSource.getReader());
			NotifyParseSuccess();
		} finally {
			try {
				NotifyParseEnd();
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	} // DoParse

	// ----------------------------------------------------------------------
	private void ParseRtf(TextReader reader) throws Exception {
		this.curText = new StringBuilder();

		this.unicodeSkipCountStack.clear();
		this.unicodeSkipCount = 1;
		this.level = 0;
		this.tagCountAtLastGroupStart = 0;
		this.tagCount = 0;
		this.fontTableStartLevel = -1;
		this.targetFont = null;
		this.fontToCodePageMapping.clear();
		this.hexDecodingBuffer.SetLength(0);
		UpdateEncoding(RtfSpec.AnsiCodePage);
		int groupCount = 0;
		int eof = -1;
		int nextChar = PeekNextChar(reader, false);
		boolean backslashAlreadyConsumed = false;
		while (nextChar != eof) {
			// System.out.println("enter while nextchar:"+nextChar);
			int peekChar = 0;
			boolean peekCharValid = false;
			switch (nextChar) {
			case '\\':
				if (!backslashAlreadyConsumed) {
					reader.read(); // must still consume the 'peek'ed char
				}
				int secondChar = PeekNextChar(reader, true);
				switch (secondChar) {
				case '\\':
				case '{':
				case '}':
					this.curText.append(ReadOneChar(reader)); // must still
																// consume the
																// 'peek'ed char
					break;

				case '\n':
				case '\r':
					reader.read(); // must still consume the 'peek'ed char
					// must be treated as a 'par' tag if preceded by a backslash
					// (see RTF spec page 144)
					HandleTag(reader, new RtfTag(RtfSpec.TagParagraph));
					break;

				case '\'':
					reader.read(); // must still consume the 'peek'ed char
					char hex1 = (char) ReadOneByte(reader);
					char hex2 = (char) ReadOneByte(reader);
					if (!IsHexDigit(hex1)) {
						throw new Exception(
								"invalid first hex digit after \\' : " + hex1);
					} else if (!IsHexDigit(hex2)) {
						throw new Exception(
								"invalid second hex digit after \\' : " + hex2);
					}
					int decodedByte = Integer.parseInt("" + hex1 + hex2, 16); // Int32
																				// .
																				// Parse
																				// (
																				// ,
																				// NumberStyles
																				// .
																				// HexNumber
																				// )
																				// ;
					// System.out.println(decodedByte);
					this.hexDecodingBuffer.WriteByte((byte) decodedByte);
					peekChar = PeekNextChar(reader, false);
					peekCharValid = true;
					boolean mustFlushHexContent = true;
					if (peekChar == '\\') {
						reader.read();
						backslashAlreadyConsumed = true;
						int continuationChar = PeekNextChar(reader, false);
						if (continuationChar == '\'') {
							mustFlushHexContent = false;
						}
					}
					if (mustFlushHexContent) {
						// we may _NOT_ handle hex content in a
						// character-by-character way as
						// this results in invalid text for japanese/chinese
						// content ...
						// -> we wait until the following content is non-hex and
						// then flush the
						// pending data. ugly but necessary with our decoding
						// model.
						DecodeCurrentHexBuffer();
					}
					break;

				case '|':
				case '~':
				case '-':
				case '_':
				case ':':
				case '*':
					HandleTag(reader, new RtfTag("" + ReadOneChar(reader))); // must
																				// still
																				// consume
																				// the
																				// 'peek'ed
																				// char
					break;

				default:
					ParseTag(reader);
					break;
				}
				break;

			case '\n':
			case '\r':
				reader.read(); // must still consume the 'peek'ed char
				break;

			case '\t':
				reader.read(); // must still consume the 'peek'ed char
				// should be treated as a 'tab' tag (see RTF spec page 144)
				HandleTag(reader, new RtfTag(RtfSpec.TagTabulator));
				break;

			case '{':
				reader.read(); // must still consume the 'peek'ed char
				FlushText();
				NotifyGroupBegin();
				this.tagCountAtLastGroupStart = this.tagCount;
				this.unicodeSkipCountStack.push(this.unicodeSkipCount);
				this.level++;
				break;

			case '}':
				reader.read(); // must still consume the 'peek'ed char
				FlushText();
				if (this.level > 0) {
					this.unicodeSkipCount = (int) this.unicodeSkipCountStack
							.pop();
					if (this.fontTableStartLevel == this.level) {
						this.fontTableStartLevel = -1;
						this.targetFont = null;
					}
					this.level--;
					NotifyGroupEnd();
					groupCount++;
				} else {
					throw new Exception(
							"improper nesting of braces: too many }");
				}
				break;

			default:
				this.curText.append(ReadOneChar(reader)); // must still consume
															// the 'peek'ed char
				break;
			}
			if (this.level == 0 && getIgnoreContentAfterRootGroup()) {
				break;
			}
			if (peekCharValid) {
				nextChar = peekChar;
			} else {
				nextChar = PeekNextChar(reader, false);
				backslashAlreadyConsumed = false;
			}
		}
		FlushText();
		reader.close();

		if (this.level > 0) {
			throw new Exception("improper nesting of braces: too few }");
		}
		if (groupCount == 0) {
			throw new Exception("no rtf content");
		}
		this.curText = null;
	} // ParseRtf

	// ----------------------------------------------------------------------
	private void ParseTag(TextReader reader) throws Exception {
		// System.out.println("parse tag");
		StringBuilder tagName = new StringBuilder();
		StringBuilder tagValue = null;
		boolean readingName = true;
		boolean delimReached = false;

		int nextChar = PeekNextChar(reader, true);
		while (!delimReached) {
			if (readingName && IsASCIILetter(nextChar)) {
				// System.out.println("IsASCIILetter");
				tagName.append(ReadOneChar(reader)); // must still consume the
														// 'peek'ed char
			} else if (IsDigit(nextChar)
					|| (nextChar == '-' && tagValue == null)) {
				// System.out.println("IsDigit");
				readingName = false;
				if (tagValue == null) {
					tagValue = new StringBuilder();
				}
				tagValue.append(ReadOneChar(reader)); // must still consume the
														// 'peek'ed char
			} else {
				delimReached = true;
				IRtfTag newTag;
				if (tagValue != null && tagValue.length() > 0) {
					newTag = new RtfTag(tagName.toString(), tagValue.toString());
				} else {
					newTag = new RtfTag(tagName.toString());
				}
				HandleTag(reader, newTag);
				if (nextChar == ' ') {
					reader.read(); // must still consume the 'peek'ed char
				}
			}
			if (!delimReached) {
				nextChar = PeekNextChar(reader, true);
			}
		}
	} // ParseTag

	// ----------------------------------------------------------------------
	private void HandleTag(TextReader reader, IRtfTag tag) throws Exception {
		if (this.level == 0) {
			throw new Exception(
					"a tag cannot appear on root level, must be child of a group: "
							+ tag.toString());
		}

		if (this.tagCount < 4) {
			// this only handles the initial encoding tag in the header section
			UpdateEncoding(tag);
		}

		String tagName = tag.getName();
		if (this.tagCountAtLastGroupStart == this.tagCount) {
			// first tag in a group:
			if (tagName.equals(RtfSpec.TagFont)) {
				if (this.fontTableStartLevel > 0) {
					// in the font-table definition:
					// -> remember the target font for charset mapping
					this.targetFont = tag.getFullName();
				}
			} else if (tagName.equals(RtfSpec.TagFontTable)) {
				this.fontTableStartLevel = this.level;
			}
		}
		if (this.targetFont != null) {
			// within a font-tables font definition: perform charset mapping
			if (RtfSpec.TagFontCharset.equals(tagName)) {
				int charSet = tag.getValueAsNumber();
				int codePage = RtfSpec.GetCodePage(charSet);
				this.fontToCodePageMapping.put(this.targetFont, codePage);
				UpdateEncoding(codePage);
			}
		}
		if (this.fontToCodePageMapping.size() > 0
				&& RtfSpec.TagFont.equals(tagName)) {
			Integer codePage = this.fontToCodePageMapping
					.get(tag.getFullName());
			if (codePage != null) {
				UpdateEncoding(codePage);
			}
		}

		if (tagName.equals(RtfSpec.TagUnicodeCode)) {
			// System.out.println("TagUnicodeCode");
			int unicodeValue = tag.getValueAsNumber();
			char unicodeChar = (char) unicodeValue;
			this.curText.append(unicodeChar);
			for (int i = 0; i < this.unicodeSkipCount; i++) {
				// skip over the indicated number of
				// 'alternative representation' text
				char skip1 = (char) reader.read();
				if (skip1 == ' ') {
					char skip2 = (char) PeekNextChar(reader, false);
					if (skip2 == '\\') {
						reader.read();
						char skip3 = (char) PeekNextChar(reader, false);
						while (skip3 != '\\' && skip3 != '}' && skip3 != '{') {
							reader.read();
							skip3 = (char) PeekNextChar(reader, false);
						}
					}
				} else if (skip1 == '\\') {
					reader.read();
					char skip3 = (char) PeekNextChar(reader, false);
					while (skip3 != '\\' && skip3 != '}' && skip3 != '{') {
						reader.read();
						skip3 = (char) PeekNextChar(reader, false);
					}
				} else if (skip1 == '\r') {
					reader.read();
					char skip2 = (char) PeekNextChar(reader, false);

					if (skip2 == '\\') {
						reader.read();
						char skip3 = (char) PeekNextChar(reader, false);
						while (skip3 != '\\' && skip3 != '}' && skip3 != '{') {
							reader.read();
							// System.Console.Write((char)reader.Read());
							skip3 = (char) PeekNextChar(reader, false);
						}
					}
				}
			}
		} else if (tagName.equals(RtfSpec.TagUnicodeSkipCount)) {
			// System.out.println("TagUnicodeSkipCount");
			int newSkipCount = tag.getValueAsNumber();
			if (newSkipCount < 0 || newSkipCount > 10) {
				throw new Exception("invalid unicode skip count: " + tag);
			}
			this.unicodeSkipCount = newSkipCount;
		} else {
			FlushText();
			NotifyTagFound(tag);
		}

		this.tagCount++;
	} // HandleTag

	// ----------------------------------------------------------------------
	private void UpdateEncoding(IRtfTag tag) {
		String tagNa = tag.getName();
		// System.out.println("tagNa:"+tagNa);
		if (tagNa.equals(RtfSpec.TagEncodingAnsi)) {
			UpdateEncoding(RtfSpec.AnsiCodePage);
		} else if (tagNa.equals(RtfSpec.TagEncodingMac)) {
			UpdateEncoding(10000);
		} else if (tagNa.equals(RtfSpec.TagEncodingPc)) {
			UpdateEncoding(437);
		} else if (tagNa.equals(RtfSpec.TagEncodingPca)) {
			UpdateEncoding(850);
		} else if (tagNa.equals(RtfSpec.TagEncodingAnsiCodePage)) {
			// System.out.println("tag.getValueAsText()"+tag.getValueAsText());
			UpdateEncoding(tag.getValueAsNumber());
		}
	} // UpdateEncoding

	// ----------------------------------------------------------------------
	private void UpdateEncoding(int codePage) {
		// System.out.println(codePage);
		if (this.encoding == null
				|| codePage2Locale.getLocale(codePage) != this.encoding.name()) {
			if (codePage == RtfSpec.AnsiCodePage
					|| codePage == RtfSpec.SymbolFakeCodePage) {
				this.encoding = RtfSpec.AnsiEncoding;
			} else {
				this.encoding = Charset.forName(codePage2Locale
						.getLocale(codePage));
			}
			this.byteToCharDecoder = null;
		}
		if (this.byteToCharDecoder == null) {
			this.byteToCharDecoder = this.encoding.newDecoder();
			// System.out.println(byteToCharDecoder.charset().displayName());
		}
	} // UpdateEncoding

	// ----------------------------------------------------------------------
	private boolean IsASCIILetter(int character) {
		return (character >= 'a' && character <= 'z')
				|| (character >= 'A' && character <= 'Z');
	} // IsASCIILetter

	// ----------------------------------------------------------------------
	private boolean IsHexDigit(int character) {
		return (character >= '0' && character <= '9')
				|| (character >= 'a' && character <= 'f')
				|| (character >= 'A' && character <= 'F');
	} // IsHexDigit

	// ----------------------------------------------------------------------
	private boolean IsDigit(int character) {
		return character >= '0' && character <= '9';
	} // IsDigit

	// ----------------------------------------------------------------------
	private int ReadOneByte(TextReader reader) throws Exception {
		int byteValue = reader.read();
		if (byteValue == -1) {
			throw new Exception(
					"unexpected end of file: requiring at least one more character");
		}
		// System.out.print((char)byteValue);
		return byteValue;
	} // ReadOneByte

	// ----------------------------------------------------------------------
	private char ReadOneChar(TextReader reader) throws Exception {
		char c = (char) ReadOneByte(reader);
		// System.out.print(c);
		return c;
	} // ReadOneChar

	// ----------------------------------------------------------------------
	private void DecodeCurrentHexBuffer() {
		int pendingByteCount = this.hexDecodingBuffer.Length();
		if (pendingByteCount > 0) {
			byte[] pendingBytes = this.hexDecodingBuffer.ToArray();
			// char[] convertedChars = new char[ pendingByteCount ]; // should
			// be enough

			int startIndex = 0;
			boolean completed = false;
			while (!completed && startIndex < pendingBytes.length) {
				// convertedChars=new String(pendingBytes).toCharArray();

				ByteBuffer buf1 = ByteBuffer.wrap(pendingBytes);
				try {
					CharBuffer cb = this.byteToCharDecoder.decode(buf1);

					//System.out.println(byteToCharDecoder.charset().displayName
					// ());
					// System.out.println("convertedChars:"+cb.toString());

					this.curText.append(cb.toString());
					startIndex += cb.length();
				} catch (CharacterCodingException e) {
					// TODO Auto-generated catch block
					// e.printStackTrace();
					//System.err.println(byteToCharDecoder.charset().displayName
					// ());
				}

				completed = true;
				// System.out.println("startIndex:"+startIndex +
				// " pendingBytes.Length:" + pendingBytes.length
				// +" convertedChars:"+new String(pendingBytes));
			}

			this.hexDecodingBuffer.SetLength(0);
		}
	} // DecodeCurrentHexBuffer

	// ----------------------------------------------------------------------
	private int PeekNextChar(TextReader reader, boolean mandatory)
			throws Exception {
		int character = reader.peek();
		if (mandatory && character == -1) {
			throw new Exception(
					"unexpected end of file while examining next character");
		}
		return character;
	} // PeekNextChar

	// ----------------------------------------------------------------------
	private void FlushText() throws Exception {
		if (this.curText.length() > 0) {
			if (this.level == 0) {
				throw new Exception(
						"a text cannot appear on root level, must be child of a group: '"
								+ this.curText.toString() + "'");
			}
			// System.out.println(this.curText.toString());
			NotifyTextFound(new RtfText(this.curText.toString()));
			this.curText.delete(0, this.curText.length());
		}
	} // FlushText

	// ----------------------------------------------------------------------
	// members
	private StringBuilder curText;
	private final Stack<Integer> unicodeSkipCountStack = new Stack<Integer>();
	private int unicodeSkipCount;
	private int level;
	private int tagCountAtLastGroupStart;
	private int tagCount;
	private int fontTableStartLevel;
	private String targetFont;
	private final Hashtable<String, Integer> fontToCodePageMapping = new Hashtable<String, Integer>();
	private Charset encoding;
	private CharsetDecoder byteToCharDecoder;
	private final MemoryStream hexDecodingBuffer = new MemoryStream(3);
	private static CodePage2Locale codePage2Locale = new CodePage2Locale();
} // class RtfParser

