package com.lietu.rtf.converter.text;

import com.lietu.rtf.IRtfInterpreterContext;
import com.lietu.rtf.RtfVisualBreakKind;
import com.lietu.rtf.RtfVisualImageFormat;
import com.lietu.rtf.RtfVisualSpecialCharKind;
import com.lietu.rtf.interpreter.RtfInterpreterListenerBase;

public class RtfTextConverter extends RtfInterpreterListenerBase
{

	// ----------------------------------------------------------------------
	public final static String DefaultTextFileExtension = ".txt";

	// ----------------------------------------------------------------------
	public RtfTextConverter() throws Exception
	{
		this( new RtfTextConvertSettings() );
	} // RtfTextConverter

	// ----------------------------------------------------------------------
	public RtfTextConverter( RtfTextConvertSettings settings ) throws Exception
	{
		if ( settings == null )
		{
			throw new Exception( "settings" );
		}

		this.settings = settings;
	} // RtfTextConverter

	// ----------------------------------------------------------------------
	public String getPlainText()
	{
		 return this.plainText.toString();
	} // PlainText

	// ----------------------------------------------------------------------
	public RtfTextConvertSettings getSettings()
	{
		 return this.settings; 
	} // Settings

	// ----------------------------------------------------------------------
	public void Clear()
	{
		plainText.delete( 0, this.plainText.length());
	} // Clear

	// ----------------------------------------------------------------------
	protected  void DoBeginDocument( IRtfInterpreterContext context )
	{
		Clear();
	} // DoBeginDocument

	@ Override
	protected  void DoInsertText( IRtfInterpreterContext context, String text )
	{
		//System.out.println("DoInsertText:"+text);
		this.plainText.append( text );
	} // DoInsertText

	// ----------------------------------------------------------------------
	protected  void DoInsertSpecialChar( IRtfInterpreterContext context, RtfVisualSpecialCharKind kind )
	{
		if(kind==RtfVisualSpecialCharKind.Tabulator){
			this.plainText.append( this.settings.getTabulatorText() );
		}else if(kind== RtfVisualSpecialCharKind.NonBreakingSpace){
			this.plainText.append( this.settings.getNonBreakingSpaceText() );
		}else if(kind== RtfVisualSpecialCharKind.EmSpace){
			this.plainText.append( this.settings.getEmSpaceText() );
		}else if(kind== RtfVisualSpecialCharKind.EnSpace){
			this.plainText.append( this.settings.getEnSpaceText() );
		}else if(kind==RtfVisualSpecialCharKind.QmSpace){
			this.plainText.append( this.settings.getQmSpaceText() );
		}else if(kind==RtfVisualSpecialCharKind.EmDash){
			this.plainText.append( this.settings.getEmDashText() );
		}else if(kind==RtfVisualSpecialCharKind.EnDash){
			this.plainText.append( this.settings.getEnDashText() );
		}else if(kind==RtfVisualSpecialCharKind.OptionalHyphen){
			this.plainText.append( this.settings.getOptionalHyphenText() );
		}else if(kind==RtfVisualSpecialCharKind.NonBreakingHyphen){
			this.plainText.append( this.settings.getNonBreakingHyphenText() );
		}else if(kind==RtfVisualSpecialCharKind.Bullet){
			this.plainText.append( this.settings.getBulletText() );
		}else if(kind==RtfVisualSpecialCharKind.LeftSingleQuote){
			this.plainText.append( this.settings.getLeftSingleQuoteText() );
		}else if(kind==RtfVisualSpecialCharKind.RightSingleQuote){
			this.plainText.append( this.settings.getRightSingleQuoteText() );
		}else if(kind==RtfVisualSpecialCharKind.LeftDoubleQuote){
			this.plainText.append( this.settings.getLeftDoubleQuoteText() );
		}else if(kind==RtfVisualSpecialCharKind.RightDoubleQuote){
			this.plainText.append( this.settings.getRightDoubleQuoteText() );
		}else {
			this.plainText.append( this.settings.getUnknownSpecialCharText() );
		}
	} // DoInsertSpecialChar

	// ----------------------------------------------------------------------
	protected  void DoInsertBreak( IRtfInterpreterContext context, RtfVisualBreakKind kind )
	{
		if(kind==RtfVisualBreakKind.Line){
			this.plainText.append( this.settings.getLineBreakText() );
		}else if(kind==RtfVisualBreakKind.Page){
			this.plainText.append( this.settings.getPageBreakText() );
		}else if(kind==RtfVisualBreakKind.Paragraph){
			this.plainText.append( this.settings.getParagraphBreakText() );
		}else if(kind==RtfVisualBreakKind.Section){
			this.plainText.append( this.settings.getSectionBreakText() );
		}else {
			this.plainText.append( this.settings.getUnknownBreakText() );
		}
	} // DoInsertBreak

	// ----------------------------------------------------------------------
	protected  void DoInsertImage( IRtfInterpreterContext context,
		RtfVisualImageFormat format,
		int width, int height, int desiredWidth, int desiredHeight,
		int scaleWidthPercent, int scaleHeightPercent,
		String imageDataHex
	)
	{
		return;
		/*String imageFormatText = this.settings.getImageFormatText();
		if ( imageFormatText !=null && ""!= imageFormatText)
		{
			return;
		}

		String imageText = String.format(
			
			imageFormatText,
			format,
			width,
			height,
			desiredWidth,
			desiredHeight,
			scaleWidthPercent,
			scaleHeightPercent,
			imageDataHex );

		this.plainText.append( imageText );*/
	} // DoInsertImage

	// ----------------------------------------------------------------------
	// members
	private  StringBuilder plainText = new StringBuilder();
	private  RtfTextConvertSettings settings;
} // class RtfTextConverter
