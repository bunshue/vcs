package com.lietu.rtf.converter.text;

public class RtfTextConvertSettings
{
	// ----------------------------------------------------------------------
	public final static String SeparatorCr = "\r";
	public final static String SeparatorLf = "\n";
	public final static String SeparatorCrLf = "\r\n";
	public final static String SeparatorLfCr = "\n\r";

	// ----------------------------------------------------------------------
	public RtfTextConvertSettings() throws Exception
	{
		 this( SeparatorCrLf );
	} // RtfTextConvertSettings

	// ----------------------------------------------------------------------
	public RtfTextConvertSettings( String breakText ) throws Exception
	{
		SetBreakText( breakText );
	} // RtfTextConvertSettings

	// ----------------------------------------------------------------------
	public String getTabulatorText()
	{
		 return this.tabulatorText;
		
	} // TabulatorText

	public void setTabulatorText(String value)
	{
		this.tabulatorText = value;
	}
	// ----------------------------------------------------------------------
	public String getNonBreakingSpaceText()
	{
		 return this.nonBreakingSpaceText; 
		
	} // NonBreakingSpaceText

	public void setNonBreakingSpaceText(String value)
	{
		this.nonBreakingSpaceText = value;
	}
	// ----------------------------------------------------------------------
	public String getEmSpaceText()
	{
		return this.emSpaceText;
	} // EmSpaceText

	public void setEmSpaceText(String value)
	{
		this.emSpaceText = value;
	}
	// ----------------------------------------------------------------------
	public String getEnSpaceText()
	{
		 return this.enSpaceText; 
		
	} // EnSpaceText

	public void setEnSpaceText(String value)
	{
		this.enSpaceText = value;
	}
	// ----------------------------------------------------------------------
	public String getQmSpaceText()
	{
		 return this.qmSpaceText;
		
	} // QmSpaceText

	public void setQmSpaceText(String value)
	{
		this.qmSpaceText = value;
	}
	// ----------------------------------------------------------------------
	public String getEmDashText()
	{
		 return this.emDashText; 
		
	} // EmDashText

	public void setEmDashText(String value)
	{
		this.emDashText = value;
	}
	// ----------------------------------------------------------------------
	public String getEnDashText()
	{
		return this.enDashText; 
		
	} // EnDashText

	public void setEnDashText(String value)
	{
		this.enDashText = value;
	}
	// ----------------------------------------------------------------------
	public String getOptionalHyphenText()
	{
		 return this.optionalHyphenText; 
		
	} // OptionalHyphenText

	public void setOptionalHyphenText(String value)
	{
		 this.optionalHyphenText = value;
	}
	// ----------------------------------------------------------------------
	public String getNonBreakingHyphenText()
	{
		 return this.nonBreakingHyphenText;
		
	} // NonBreakingHyphenText

	public void setNonBreakingHyphenText(String value)
	{
		this.nonBreakingHyphenText = value;
	}
	// ----------------------------------------------------------------------
	public String getBulletText()
	{
		return this.bulletText; 
		
	} // BulletText

	public void setBulletText(String value)
	{
		this.bulletText = value; 
	}
	// ----------------------------------------------------------------------
	public String getLeftSingleQuoteText()
	{
		return this.leftSingleQuoteText; 
		
	} // LeftSingleQuoteText

	public void setLeftSingleQuoteText(String value)
	{
		this.leftSingleQuoteText = value;
	}
	// ----------------------------------------------------------------------
	public String getRightSingleQuoteText()
	{
		return this.rightSingleQuoteText; 
		
	} // RightSingleQuoteText

	public void setRightSingleQuoteText(String value)
	{
		this.rightSingleQuoteText = value;
	}
	// ----------------------------------------------------------------------
	public String getLeftDoubleQuoteText()
	{
		 return this.leftDoubleQuoteText; 
		
	} // LeftDoubleQuoteText

	public void setLeftDoubleQuoteText(String value)
	{
		 this.leftDoubleQuoteText = value;
	}
	// ----------------------------------------------------------------------
	public String getRightDoubleQuoteText()
	{
		 return this.rightDoubleQuoteText; 
		
	} // RightDoubleQuoteText

	public void setRightDoubleQuoteText(String value)
	{
		 this.rightDoubleQuoteText = value;
	}
	// ----------------------------------------------------------------------
	public String getUnknownSpecialCharText()
	{
		return this.unknownSpecialCharText; 
		
	} // UnknownSpecialCharText

	public void setUnknownSpecialCharText(String value)
	{
		 this.unknownSpecialCharText = value; 
	}
	// ----------------------------------------------------------------------
	public String getLineBreakText()
	{
		return this.lineBreakText; 
		
	} // LineBreakText

	public void setLineBreakText(String value)
	{
		 this.lineBreakText = value;
	}
	// ----------------------------------------------------------------------
	public String getPageBreakText()
	{
		 return this.pageBreakText; 
		
	} // PageBreakText

	public void setPageBreakText(String value)
	{
		this.pageBreakText = value; 
	}
	// ----------------------------------------------------------------------
	public String getParagraphBreakText()
	{
		 return this.paragraphBreakText; 
		
	} // ParagraphBreakText

	public void setParagraphBreakText(String value)
	{
		this.paragraphBreakText = value;
	}
	// ----------------------------------------------------------------------
	public String getSectionBreakText()
	{
		 return this.sectionBreakText; 
		
	} // SectionBreakText

	public void setSectionBreakText(String value)
	{
		this.sectionBreakText = value;
	}
	// ----------------------------------------------------------------------
	public String getUnknownBreakText()
	{
		return this.unknownBreakText; 
		
	} // UnknownBreakText

	public void setUnknownBreakText(String value)
	{
		this.unknownBreakText = value;
	}
	// ----------------------------------------------------------------------
	public String getImageFormatText()
	{
		 return this.imageFormatText;
		
	} // ImageFormatText

	public void setImageFormatText(String value)
	{
		this.imageFormatText = value;
	}
	// ----------------------------------------------------------------------
	public void SetBreakText( String breakText ) throws Exception
	{
		if ( breakText == null )
		{
			throw new Exception( "breakText" );
		}

		this.lineBreakText = breakText;
		this.pageBreakText = breakText + breakText;
		this.paragraphBreakText = breakText;
		this.sectionBreakText = breakText + breakText;
		this.unknownBreakText = breakText;
	} // SetBreakText

	// ----------------------------------------------------------------------
	// members: special chars
	private String tabulatorText = "\t";
	private String nonBreakingSpaceText = " ";
	private String emSpaceText = " ";
	private String enSpaceText = " ";
	private String qmSpaceText = " ";
	private String emDashText = "-";
	private String enDashText = "-";
	private String optionalHyphenText = "-";
	private String nonBreakingHyphenText = "-";
	private String bulletText = "¢X";
	private String leftSingleQuoteText = "`";
	private String rightSingleQuoteText = "¡¬";
	private String leftDoubleQuoteText = "``";
	private String rightDoubleQuoteText = "¡¬¡¬";
	private String unknownSpecialCharText = "";

	// members: breaks
	private String lineBreakText;
	private String pageBreakText;
	private String paragraphBreakText;
	private String sectionBreakText;
	private String unknownBreakText;

	// members: image
	private String imageFormatText = "[{0}:{1} x {2}]";

} // class RtfTextConvertSettings
