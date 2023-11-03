package com.lietu.rtf.parser;

	public class RtfParserLoggerSettings
	{

		// ----------------------------------------------------------------------
		public RtfParserLoggerSettings()
		{
			 this( true );
		} // RtfParserLoggerSettings

		// ----------------------------------------------------------------------
		public RtfParserLoggerSettings( boolean enabled )
		{
			this.enabled = enabled;
		} // RtfParserLoggerSettings

		// ----------------------------------------------------------------------
		public boolean getEnabled()
		{
			return this.enabled; 
			
		} // Enabled

		public void setEnabled(boolean value)
		{
			this.enabled = value;
		}
		// ----------------------------------------------------------------------
		public String getParseBeginText()
		{
			return this.parseBeginText; 
		
		} // ParseBeginText

		public void setParseBeginText(String value)
		{
			this.parseBeginText = value; 
		}
		// ----------------------------------------------------------------------
		public String getParseEndText()
		{
			 return this.parseEndText; 
			
		} // ParseEndText

		public void setParseEndText(String value)
		{
			 this.parseEndText = value; 
		}
		// ----------------------------------------------------------------------
		public String getParseGroupBeginText()
		{
			  return this.parseGroupBeginText;
			
		} // ParseGroupBeginText

		public void setParseGroupBeginText(String value)
		{
			 this.parseGroupBeginText = value; 
		}
		// ----------------------------------------------------------------------
		public String getParseGroupEndText()
		{
			return this.parseGroupEndText;
			 
		} // ParseGroupEndText

		public void setParseGroupEndText(String value)
		{
			 this.parseGroupEndText = value;
		}
		// ----------------------------------------------------------------------
		public String getParseTagText()
		{
			 return this.parseTagText;
			
		} // ParseTagText

		public void setParseTagText(String value)
		{
			 this.parseTagText = value; 
		}
		// ----------------------------------------------------------------------
		public String getTextOverflowText()
		{
			 { return this.textOverflowText; }
			
		} // TextOverflowText

		public void setTextOverflowText(String value)
		{
			this.textOverflowText = value; 
		}
		// ----------------------------------------------------------------------
		public String getParseTextText()
		{
			 return this.parseTextText; 
			
		} // ParseTextText

		public void setParseTextText(String value)
		{
			 this.parseTextText = value; 
		}
		// ----------------------------------------------------------------------
		public String getParseSuccessText()
		{
			 return this.parseSuccessText; 
			
		} // ParseSuccessText

		public void setParseSuccessText(String value)
		{
			 this.parseSuccessText = value; 
		}
		// ----------------------------------------------------------------------
		public String getParseFailKnownReasonText()
		{
			return this.parseFailKnownReasonText; 
			
		} // ParseFailKnownReasonText

		public void setParseFailKnownReasonText(String value)
		{
			this.parseFailKnownReasonText = value; 
		}
		// ----------------------------------------------------------------------
		public String getParseFailUnknownReasonText()
		{
			 return this.parseFailUnknownReasonText;
		
		} // ParseFailUnknownReasonText

		public void setParseFailUnknownReasonText(String value)
		{
			this.parseFailUnknownReasonText = value;
		}
		// ----------------------------------------------------------------------
		public int getTextMaxLength()
		{
			 return this.textMaxLength; 
		
		} // TextMaxLength

		public void setTextMaxLength(int value)
		{
			 this.textMaxLength = value;
		}
		// ----------------------------------------------------------------------
		// members
		private boolean enabled;
		private String parseBeginText = "ParseBegin";
		private String parseEndText = "ParseEnd";
		private String parseGroupBeginText = "GroupBegin";
		private String parseGroupEndText = "GroupEnd";
		private String parseTagText = "Tag: {0}";
		private String parseTextText = "Text: {0}";
		private String textOverflowText = "...";
		private String parseSuccessText = "ParseSuccess";
		private String parseFailKnownReasonText = "ParseFail: {0}";
		private String parseFailUnknownReasonText = "ParseFail: unknown reason";

		private int textMaxLength = 80;

	} // class RtfParserLoggerSettings

