package com.lietu.rtf.interpreter;

	public class RtfInterpreterLoggerSettings
	{

		// ----------------------------------------------------------------------
		public RtfInterpreterLoggerSettings()
			
		{
			this( true );
		} // RtfInterpreterLoggerSettings

		// ----------------------------------------------------------------------
		public RtfInterpreterLoggerSettings( boolean enabled )
		{
			this.enabled = enabled;
		} // RtfInterpreterLoggerSettings

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
		public String getBeginDocumentText()
		{
			 return this.beginDocumentText; 
			
		} // BeginDocumentText

		public void setBeginDocumentText(String value)
		{
			this.beginDocumentText = value;
		}
		// ----------------------------------------------------------------------
		public String getEndDocumentText()
		{
			 return this.endDocumentText; 
			
		} // EndDocumentText

		public void setEndDocumentText(String value)
		{
			this.endDocumentText = value;
		}
		// ----------------------------------------------------------------------
		public String getTextFormatText()
		{
			return this.textFormatText; 
			
		} // TextFormatText

		public void setTextFormatText(String value){
			this.textFormatText = value;
		}
		// ----------------------------------------------------------------------
		public String getTextOverflowText()
		{
		 return this.textOverflowText; 
		
		} // TextOverflowText

		public void setTextOverflowTest(String value){
			this.textOverflowText = value;
		}
		// ----------------------------------------------------------------------
		public String getSpecialCharFormatText()
		{
			return this.specialCharFormatText; 
			
		} // SpecialCharFormatText

		public void setSpecialCharFormatText(String value){
			this.specialCharFormatText = value;
		}
		// ----------------------------------------------------------------------
		public String getBreakFormatText()
		{
			 return this.breakFormatText; 
			
		} // BreakFormatText

		public void setBreakFormatText(String value){
			this.breakFormatText = value; 
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
		public int getTextMaxLength()
		{
			 return this.textMaxLength; 
			
		} // TextMaxLength

		public void setTextMaxLength(int value){
			this.textMaxLength = value;
		}
		// ----------------------------------------------------------------------
		// members
		private boolean enabled;
		private String beginDocumentText = "BeginDocument";
		private String endDocumentText = "EndDocument";
		private String textFormatText = "InsertText: \'{0}\' with format [{1}]";
		private String textOverflowText = "...";
		private String specialCharFormatText = "InsertChar: {0}";
		private String breakFormatText = "InsertBreak: {0}";
		private String imageFormatText = 
			"InsertImage: {0}: {1} x {2}" +
			", desired: {3} x {4}" +
			", scaled: {5}% x {6}%" +
			", {8} bytes";

		private int textMaxLength = 80;

	} // class RtfInterpreterLoggerSettings

