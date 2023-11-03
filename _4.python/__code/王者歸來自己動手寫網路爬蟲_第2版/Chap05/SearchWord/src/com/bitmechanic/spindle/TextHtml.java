/*
 * Created on 2004-5-11
 *
 */
package com.bitmechanic.spindle;

/**	TextHtml
 * 
 * 	23.10.2001  MAP  Initial release
 * 	24.01.2002  MAP  Method "text2html()".
 * 					Check for the ordinal value of char before addressing
 * 					"symbolicCode" array. Non ISO8859-1 char.
 *  14.06.2005	Luogang add unicode converter from html.
 */
import java.util.Arrays;

/**
 * This class convert a text in an HTML text format with symbolic code (&xxxx;),
 * it also convert a given HTML text format which contain symbolic code to text.
 * @version 1.1
 * @author Philippe Martin
 */
public class TextHtml {
	/**
	 * Method text2html: Convert a text to an HTML format.
	 *
	 * @param text:     The original text string
	 * @return          The converted HTML text including symbolic codes string
	 */

	public static void main(String argv[]) throws Exception {
		
		//VisitedTaskList vt = new VisitedTaskList();
		//System.out.println(TextHtml.html2text("<code>&quot;Hello from ActivePerl!&quot;</code> &#x900D;&#x9065; &#32; &#25;"));
		System.out.println(TextHtml.text2html("&"));
		//System.out.println(TextHtml.html2text("&#32593;&#31449;&#23548;&#33322;"));
		//char a = ':';
		//System.out.println(TextHtml.print(new String("将红帽认证培训计划引入中国".getBytes("GBK"), "iso8859_1")));
	}

	public static String text2html(String text) {
		if (text == null)
			return text;
		StringBuffer t = new StringBuffer(text.length() + 10); // 10 is just a test value, could be anything, should affect performance
		for (int i = 0; i < text.length(); i++) {
			char c = text.charAt(i);
			// Check for non ISO8859-1 characters
			if ((int)c < symbolicCode.length) { // Maybe slower than  "(int)c & 0xFF != 0" but more evolutive

				//System.out.println("hi");
				String sc = symbolicCode[(int)c];
				if ("".equals(sc)) {
					t = t.append(c);
				}
				else {
					t = t.append(sc);
				}
			}
			else {
				t.append("&#x");
				t.append(Integer.toHexString(c));
				System.out.println("char:"+Integer.toHexString(c));
				t.append(";");
			}
		}
		return t.toString();
	}

	public static String print(String text) {
		if (text == null)
			return text;
		StringBuffer t = new StringBuffer(text.length() + 10); // 10 is just a test value, could be anything, should affect performance
		for (int i = 0; i < text.length(); i++) {
			char c = text.charAt(i);
			// Check for non ISO8859-1 characters
			//{
				t.append("&#x");
				t.append(Integer.toHexString(c));
				System.out.println("char:"+Integer.toHexString(c));
				t.append(";");
			//}
		}
		return t.toString();
	}

	/**
	 * Method html2text: Convert an HTML text format to a normal text format.
	 *
	 * @param text:     The original HTML text string
	 * @return          The converted text without symbolic codes string
	 */
	public static String html2text(String text) {
		if (text == null)
			return text;
		StringBuffer t = new StringBuffer(text.length());
		
		boolean number=false;
		char tempchar;
		
		for (int i = 0; i < text.length(); i++) {
			char c = text.charAt(i);
			if (c == '&') {
				String code = String.valueOf(c);
				number=false;
				do {
					if (++i >= text.length())
						break;
					tempchar = text.charAt(i);
					if (tempchar == '&') {
						i--;
						break;
					}
					else if (tempchar == '#')
						number=true;
					code += tempchar;
				} while (text.charAt(i) != ';');
				if (!code.equals("&nbsp;"))
				{
					if (number)
					{
						try
						{
							//System.out.println("will decode:"+"0"+code.substring(2,code.length() -1));
							long tempL;
							if(code.length()<4)
							{
								t.append(code);
								continue;
							}
							if (code.substring(2,code.length() -1).startsWith("x"))
								tempL= (Long.decode("0"+code.substring(2,code.length() -1))).longValue();
							else
								tempL= (Long.decode(code.substring(2,code.length() -1))).longValue();
							//System.out.println("long value:"+tempL);
							byte[] b;
							String charset;
							//{
								//System.out.println("into utf");
								b= new byte[2];
								b[1]=(byte)tempL;
								//System.out.println(b[1]);
								b[0]=(byte)(tempL>>>8);
								//System.out.println(b[0]);
								charset = "UTF-16BE";//"UTF-16LE";//
							//}
							try{
								//System.out.println(new String(b, charset ));
								t.append(new String(b, charset ));
							}catch(Exception e)
							{}
						}
						catch(NumberFormatException e)
						{
							t.append(code);
						}
					}
					else
					{
						int index = Arrays.binarySearch(sortedSymbolicCode,
													  new NumericSymbolicCode(code, 0));
						// Does the extracting code correspond to something ?
						if (index >= 0) {
							t = t.append((char)sortedSymbolicCode[index].getNumericCode());
						}
						else {
							t = t.append(code);
						}
					}
				}
			}
			else {
				t = t.append(c);
				//modify here
				//if(c == '<') intag = true;
				//if(! intag) t = t.append(c);
				//if(c == '>')intag = false;
				//end modify				
			}
		}
		return t.toString();
	}

	/**
	 * Array of symbolic code order by numeric code ! <br>
	 * The symbolic codes and their position correspond to the ISO 8859-1 set
	 * of char. The empty definitions mean that there is no symbolic codes for
	 * that character or this symbolic code is not used.
	 */
	private static final String[] symbolicCode = {
		// 0
		"", "", "", "", "", "", "", "", "", "",
		// 10
		"", "", "", "", "", "", "", "", "", "",
		// 20
		"", "", "", "", "",
		"&#25;",       // yen sign
		"", "", "", "",
		// 30
		"", "", "&#32;", "",
		"&quot;",      // quotation mark
		"", "", "", "&amp;", "", // unfortunately &apos; is not supported in HTML 4, only XHTML 1.0
		// 40
		"", "", "", "", "", "", "", "", "", "",
		// 50
		"", "", "", "", "", "", "", "", "", "",
		// 60
		//change here
		"&lt;", "", "&gt;", "",
		//end change luogang
		"&#64;",       // commercial at
		"", "", "", "", "",
		// 70
		"", "", "", "", "", "", "", "", "", "",
		// 80
		"", "", "", "", "", "", "", "", "", "",
		// 90
		"", "", "", "", "", "",
		"&#96;",       // grave accent
		"", "", "",
		// 100
		"", "", "", "", "", "", "", "", "", "",
		// 110-130
		"", "", "", "", "", "", "", "", "", "",
		"", "", "", "", "", "", "", "", "", "",
		"", "", "", "", "", "", "", "", "", "",
		// 140
		"", "", "", "", "", "",
		"&#146;",      // other apostrophe
		"", "", "",
		// 150
		"", "", "", "", "", "", "", "", "", "",
		// 160
		"",          // non breaking space (should be &nbsp;)
		"&iexcl;",     // invertedexclamation sign
		"&cent;",      // cent sign
		"&pound;",     // pound sterling sign
		"&curren;",    // general currency sign
		"&yen;",       // yen sign
		"&brvbar;",    // broken vertical bar
		"&sect;",      // section sign (legal)
		"&uml;",       // umlaut (dieresis)
		"&copy;",      // copyright
		// 170
		"&ordf;",      // feminine ordinal
		"&laquo;",     // guillemot left
		"&not;",       // not sign
		"&shy;",       // soft hyphen
		"&reg;",       // registered trademark
		"&macr;",      // macron accent
		"&deg;",       // degree sign
		"&plusmn;",    // plus or minus
		"&sup2;",      // raised to square(superscript two)
		"&sup3;",      // superscript three
		// 180
		"&acute;",     // acute accent
		"&micro;",     // micron sign
		"&para",       // paragraph sign, Pi
		"&middot;",    // middle dot
		"&cedil;",     // cedilla mark
		"&supl;",      // raised to one(superscript one)
		"&ordm;",      // masculine ordinal
		"&raquo;",     // guillemot right
		"&frac14;",    // one-forth fraction
		"&frac12;",    // half fraction
		// 190
		"&frac34;",    // three-forths fraction
		"&iquest;",    // inverted question mark
		"&Agrave;",    // A with grave accent
		"&Aacute;",    // A with acute accent
		"&Acirc;",     // A with circumflex accent
		"&Atilde;",    // A with tilde accent
		"&Auml;",     // A with angstrom
		"&Aring;",      // A with umlaut mark
		"&AElig;",     // AE dipthong (ligature)
		"&Ccedil;",    // C with cedilla mark
		// 200
		"&Egrave;",    // E with grave accent
		"&Eacute;",    // E with acute accent
		"&Ecirc;",     // E with circumflex accent
		"&Euml;",      // E with umlaut mark
		"&Igrave;",    // I with grave accent
		"&Iacute;",    // I with acute accent
		"&Icirc;",     // I with circumflex accent
		"&Iuml;",      // I with umlaut mark
		"&ETH;",       // Icelandic Capital Eth
		"&Ntilde;",    // N with tilde accent
		// 210
		"&Ograve;",    // O with grave accent
		"&Oacute;",    // O with acute accent
		"&Ocirc;",     // O with circumflex accent
		"&Otilde;",    // O with tilde accent
		"&Ouml;",      // O with umlaut mark
		"&times;",     // multiply sign
		"&Oslash;",    // O slash
		"&Ugrave;",    // U with grave accent
		"&Uacute;",    // U with acute accent
		"&Ucirc;",     // U with circumflex accent
		// 220
		"&Uuml;",      // U with umlaut mark
		"&Yacute;",    // Y with acute accent
		"&THORN;",     // Icelandic Capital Thorn
		"&szlig;",     // small sharp s(sz ligature)
		"&agrave;",    // a with grave accent
		"&aacute;",    // a with acute accent
		"&acirc;",     // a with circumflex accent
		"&atilde;",    // a with tilde accent
		"&auml;",     // a with angstrom
		"&aring;",      // a with umlaut mark
		// 230
		"&aelig;",     // ae dipthong (ligature)
		"&ccedil;",    // c with cedilla mark
		"&egrave;",    // e with grave accent
		"&eacute;",    // e with acute accent
		"&ecirc;",     // e with circumflex accent
		"&euml;",      // e with umlaut mark
		"&igrave;",    // i with grave accent
		"&iacute;",    // i with acute accent
		"&icirc;",     // i with circumflex accent
		"&iuml;",      // i with umlaut mark
		// 240
		"&eth;",       // Icelandic small eth
		"&ntilde;",    // n with tilde accent
		"&ograve",     // o with grave accent
		"&oacute;",    // o with acute accent
		"&ocirc;",     // o with circumflex accent
		"&otilde",     // o with tilde accent
		"&ouml;",      // o with umlaut mark
		"&divide;",    // divide sign
		"&oslash;",    // o slash
		"&ugrave;",    // u with grave accent
		// 250
		"&uacute;",    // u with acute accent
		"&ucirc;",     // u with circumflex accent
		"&uuml;",      // u with umlaut mark
		"&yacute;",    // y with acute accent
		"&thorn;",     // Icelandic small thorn
		"&yuml;",      // y with umlaut mark
	};

	/**
	 * Array of symbolic code order symbolic code !<br>
	 * This array is the reciprocal from the 'symbolicCode' array.
	 */
	private static NumericSymbolicCode[] sortedSymbolicCode =
									new NumericSymbolicCode[symbolicCode.length];

	/**
	 * This class is the structure used for the 'sortedSymbolicCode' array.
	 * Each symbolic code string (sorted by alphabetical order) have its numerical
	 * corresponding code.<br>
	 * This class also implements the 'Comparable' interface to ease the sorting
	 * process in the initialisation bloc.
	*/
	final private static class NumericSymbolicCode implements Comparable {

		public NumericSymbolicCode(String symbolicCode, int numericCode) {
			this.symbolicCode = symbolicCode;
			this.numericCode = numericCode;
		}

		public String getSymbolicCode() {
			return symbolicCode;
		}

		public int getNumericCode() {
			return numericCode;
		}

		public int compareTo(Object object) {
			NumericSymbolicCode nsc = (NumericSymbolicCode)object;
			return symbolicCode.compareTo(nsc.symbolicCode);
		}

		private String symbolicCode;
		private int numericCode;
	}

	/**
	* Initialization and sorting of the 'sortedSymbolicCode'
	*/
	static {
		for (int i = 0; i < symbolicCode.length; i++) {
			  sortedSymbolicCode[i] = new NumericSymbolicCode(symbolicCode[i], i);
		}
		Arrays.sort(sortedSymbolicCode);
	}
}