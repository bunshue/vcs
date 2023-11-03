package com.lietu.rtf;

import java.nio.charset.Charset;

public  class RtfSpec
{

	// --- rtf general ----
	public static final String TagRtf = "rtf";
	public static final  int RtfVersion1 = 1;

	public static final String TagGenerator = "generator";

	// --- encoding ----
	public static final String TagEncodingAnsi = "ansi";
	public static final String TagEncodingMac = "mac";
	public static final String TagEncodingPc = "pc";
	public static final String TagEncodingPca = "pca";
	public static final String TagEncodingAnsiCodePage = "ansicpg";
	public static final int AnsiCodePage = 1252;
	public static final int SymbolFakeCodePage = 42; // a windows legacy hack ...
	public static final Charset AnsiEncoding = Charset.forName("GBK");

	public static final String TagUnicodeSkipCount = "uc";
	public static final String TagUnicodeCode = "u";
	public static final String TagUnicodeAlternativeChoices = "upr";
	public static final String TagUnicodeAlternativeUnicode = "ud";

	// --- font ----
	public static final String TagFontTable = "fonttbl";
	public static final String TagDefaultFont = "deff";
	public static final String TagFont = "f";
	public static final String TagFontKindNil = "fnil";
	public static final String TagFontKindRoman = "froman";
	public static final String TagFontKindSwiss = "fswiss";
	public static final String TagFontKindModern = "fmodern";
	public static final String TagFontKindScript = "fscript";
	public static final String TagFontKindDecor = "fdecor";
	public static final String TagFontKindTech = "ftech";
	public static final String TagFontKindBidi = "fbidi";
	public static final String TagFontCharset = "fcharset";
	public static final String TagFontPitch = "fprq";
	public static final String TagFontSize = "fs";
	public static final String TagFontSubscript = "dn";
	public static final String TagFontSuperscript = "up";

	public static final int DefaultFontSize = 24;

	public static final String TagCodePage = "cpg";

	// --- color ----
	public static final String TagColorTable = "colortbl";
	public static final String TagColorRed = "red";
	public static final String TagColorGreen = "green";
	public static final String TagColorBlue = "blue";
	public static final String TagColorForeground = "cf";
	public static final String TagColorBackground = "cb";
	public static final String TagColorBackgroundWord = "chcbpat";

	// --- header/footer ----
	public static final String TagHeader = "header";
	public static final String TagHeaderFirst = "headerf";
	public static final String TagHeaderLeft = "headerl";
	public static final String TagHeaderRight = "headerr";
	public static final String TagFooter = "footer";
	public static final String TagFooterFirst = "footerf";
	public static final String TagFooterLeft = "footerl";
	public static final String TagFooterRight = "footerr";
	public static final String TagFootnote = "footnote";

	// --- character ----
	public static final String TagDelimiter = ";";
	public static final String TagExtensionDestination = "*";
	public static final String TagTilde = "~";
	public static final String TagHyphen = "-";
	public static final String TagUnderscore = "_";

	// --- special character ----
	public static final String TagPage = "page";
	public static final String TagSection = "sect";
	public static final String TagParagraph = "par";
	public static final String TagLine = "line";
	public static final String TagTabulator = "tab";
	public static final String TagEmDash = "emdash";
	public static final String TagEnDash = "endash";
	public static final String TagEmSpace = "emspace";
	public static final String TagEnSpace = "enspace";
	public static final String TagQmSpace = "qmspace";
	public static final String TagBulltet = "bullet";
	public static final String TagLeftSingleQuote = "lquote";
	public static final String TagRightSingleQuote = "rquote";
	public static final String TagLeftDoubleQuote = "ldblquote";
	public static final String TagRightDoubleQuote = "rdblquote";

	// --- format ----
	public static final String TagPlain = "plain";
	public static final String TagParagraphDefaults = "pard";
	public static final String TagSectionDefaults = "sectd";

	public static final String TagBold = "b";
	public static final String TagItalic = "i";
	public static final String TagUnderLine = "ul";
	public static final String TagUnderLineNone = "ulnone";
	public static final String TagStrikeThrough = "strike";
	public static final String TagAlignLeft = "ql";
	public static final String TagAlignCenter = "qc";
	public static final String TagAlignRight = "qr";
	public static final String TagAlignJustify = "qj";

	// --- info ----
	public static final String TagInfo = "info";
	public static final String TagInfoVersion = "version";
	public static final String TagInfoRevision = "vern";
	public static final String TagInfoNumberOfPages = "nofpages";
	public static final String TagInfoNumberOfWords = "nofwords";
	public static final String TagInfoNumberOfChars = "nofchars";
	public static final String TagInfoId = "id";
	public static final String TagInfoTitle = "title";
	public static final String TagInfoSubject = "subject";
	public static final String TagInfoAuthor = "author";
	public static final String TagInfoManager = "manager";
	public static final String TagInfoCompany = "company";
	public static final String TagInfoOperator = "operator";
	public static final String TagInfoCategory = "category";
	public static final String TagInfoKeywords = "keywords";
	public static final String TagInfoComment = "comment";
	public static final String TagInfoDocumentComment = "doccomm";
	public static final String TagInfoHyperLinkBase = "hlinkbase";
	public static final String TagInfoCreationTime = "creatim";
	public static final String TagInfoRevisionTime = "revtim";
	public static final String TagInfoPrintTime = "printim";
	public static final String TagInfoBackupTime = "buptim";
	public static final String TagInfoYear = "yr";
	public static final String TagInfoMonth = "mo";
	public static final String TagInfoDay = "dy";
	public static final String TagInfoHour = "hr";
	public static final String TagInfoMinute = "min";
	public static final String TagInfoSecond = "sec";
	public static final String TagInfoEditingTimeMinutes = "edmins";

	// --- user properties ----
	public static final String TagUserProperties = "userprops";
	public static final String TagUserPropertyType = "proptype";
	public static final String TagUserPropertyName = "propname";
	public static final String TagUserPropertyValue = "static finalval";
	public static final String TagUserPropertyLink = "linkval";

	// this table is from the RTF specification 1.9.1, page 40
	public static final int PropertyTypeInteger = 3;
	public static final int PropertyTypeRealNumber = 5;
	public static final int PropertyTypeDate = 64;
	public static final int PropertyTypeBoolean = 11;
	public static final int PropertyTypeText = 30;

	// --- picture ----
	public static final String TagPicture = "pict";
	public static final String TagPictureFormatEmf = "emfblip";
	public static final String TagPictureFormatPng = "pngblip";
	public static final String TagPictureFormatJpg = "jpegblip";
	public static final String TagPictureFormatPict = "macpict";
	public static final String TagPictureFormatOs2Metafile = "pmmetafile";
	public static final String TagPictureFormatWmf = "wmetafile";
	public static final String TagPictureFormatWinDib = "dibitmap";
	public static final String TagPictureFormatWinBmp = "wbitmap";
	public static final String TagPictureWidth = "picw";
	public static final String TagPictureHeight = "pich";
	public static final String TagPictureWidthGoal = "picwgoal";
	public static final String TagPictureHeightGoal = "pichgoal";
	public static final String TagPictureWidthScale = "picscalex";
	public static  final String TagPictureHeightScale = "picscaley";

	// --- bulltes/numbering ----
	public static  final String TagParagraphNumberText = "pntext";
	public static  final String TagListNumberText = "listtext";

	// ----------------------------------------------------------------------
	private RtfSpec()
	{
	} // RtfSpec

	// ----------------------------------------------------------------------
	public static  int GetCodePage( int charSet )
	{
		switch ( charSet )
		{
			case 0:
				return 1252; // ANSI
			case 1:
				return 0; // Default
			case 2:
				return 42; // Symbol
			case 77:
				return 10000; // Mac Roman
			case 78:
				return 10001; // Mac Shift Jis
			case 79:
				return 10003; // Mac Hangul
			case 80:
				return 10008; // Mac GB2312
			case 81:
				return 10002; // Mac Big5
			case 82:
				return 0; // Mac Johab (old)
			case 83:
				return 10005; // Mac Hebrew
			case 84:
				return 10004; // Mac Arabic
			case 85:
				return 10006; // Mac Greek
			case 86:
				return 10081; // Mac Turkish
			case 87:
				return 10021; // Mac Thai
			case 88:
				return 10029; // Mac East Europe
			case 89:
				return 10007; // Mac Russian
			case 128:
				return 932; // Shift JIS
			case 129:
				return 949; // Hangul
			case 130:
				return 1361; // Johab
			case 134:
				return 936; // GB2312
			case 136:
				return 950; // Big5
			case 161:
				return 1253; // Greek
			case 162:
				return 1254; // Turkish
			case 163:
				return 1258; // Vietnamese
			case 177:
				return 1255; // Hebrew
			case 178:
				return 1256; // Arabic
			case 179:
				return 0; // Arabic Traditional (old)
			case 180:
				return 0; // Arabic user (old)
			case 181:
				return 0; // Hebrew user (old)
			case 186:
				return 1257; // Baltic
			case 204:
				return 1251; // Russian
			case 222:
				return 874; // Thai
			case 238:
				return 1250; // Eastern European
			case 254:
				return 437; // PC 437
			case 255:
				return 850; // OEM
		}

		return 0;
	} // GetCodePage

} // class RtfSpec

