package com.lietu.rtf.interpreter;

import java.util.ArrayList;

import com.lietu.rtf.IRtfDocument;
import com.lietu.rtf.IRtfInterpreterContext;
import com.lietu.rtf.IRtfTextFormat;
import com.lietu.rtf.IRtfVisual;
import com.lietu.rtf.RtfVisualBreakKind;
import com.lietu.rtf.RtfVisualImageFormat;
import com.lietu.rtf.RtfVisualSpecialCharKind;
import com.lietu.rtf.model.RtfDocument;
import com.lietu.rtf.model.RtfVisualBreak;
import com.lietu.rtf.model.RtfVisualImage;
import com.lietu.rtf.model.RtfVisualSpecialChar;
import com.lietu.rtf.model.RtfVisualText;


public final class RtfInterpreterListenerDocumentBuilder extends RtfInterpreterListenerBase
{

	// ----------------------------------------------------------------------
	public RtfInterpreterListenerDocumentBuilder()
	{
	} // RtfInterpreterListenerDocumentBuilder

	// ----------------------------------------------------------------------
	public boolean getCombineTextWithSameFormat()
	{
		 return this.combineTextWithSameFormat; 
		
	} // CombineTextWithSameFormat

	public void setCombineTextWithSameFormat(boolean value)
	{
		this.combineTextWithSameFormat = value;
	}
	// ----------------------------------------------------------------------
	public IRtfDocument getDocument()
	{
		 return this.document; 
	} // Document

	// ----------------------------------------------------------------------
	protected  void DoBeginDocument( IRtfInterpreterContext context )
	{
		this.document = null;
		this.visualContent = new ArrayList<IRtfVisual>();
	} // DoBeginDocument

	// ----------------------------------------------------------------------
	protected  void DoInsertText( IRtfInterpreterContext context, String text ) throws Exception
	{
		if ( this.combineTextWithSameFormat )
		{
			IRtfTextFormat newFormat = context.getGetSafeCurrentTextFormat();
			if ( !newFormat.equals( this.pendingTextFormat ) )
			{
				FlushPendingText();
			}
			this.pendingTextFormat = newFormat;
			this.pendingText.append( text );
		}
		else
		{
			this.visualContent.add( new RtfVisualText( text, context.getGetSafeCurrentTextFormat() ) );
		}
	} // DoInsertText

	// ----------------------------------------------------------------------
	protected  void DoInsertSpecialChar( IRtfInterpreterContext context, RtfVisualSpecialCharKind kind ) throws Exception
	{
		FlushPendingText();
		this.visualContent.add( new RtfVisualSpecialChar( kind ) );
	} // DoInsertSpecialChar

	// ----------------------------------------------------------------------
	protected  void DoInsertBreak( IRtfInterpreterContext context, RtfVisualBreakKind kind ) throws Exception
	{
		FlushPendingText();
		this.visualContent.add( new RtfVisualBreak( kind ) );
	} // DoInsertBreak

	// ----------------------------------------------------------------------
	protected  void DoInsertImage( IRtfInterpreterContext context,
		RtfVisualImageFormat format,
		int width, int height, int desiredWidth, int desiredHeight,
		int scaleWidthPercent, int scaleHeightPercent,
		String imageDataHex
	) throws Exception
	{
		FlushPendingText();
		this.visualContent.add( new RtfVisualImage( format,
			context.getGetSafeCurrentTextFormat().getAlignment(),
			width, height, desiredWidth, desiredHeight,
			scaleWidthPercent, scaleHeightPercent, imageDataHex ) );
	} // DoInsertImage

	// ----------------------------------------------------------------------
	protected  void DoEndDocument( IRtfInterpreterContext context ) throws Exception
	{
		FlushPendingText();
		this.document = new RtfDocument( context, this.visualContent );
		this.visualContent = null;
	} // DoEndDocument

	// ----------------------------------------------------------------------
	private void FlushPendingText() throws Exception
	{
		if ( this.pendingTextFormat != null )
		{
			this.visualContent.add( new RtfVisualText( this.pendingText.toString(), this.pendingTextFormat ) );
			this.pendingTextFormat = null;
			this.pendingText.delete( 0, this.pendingText.length() );
		}
	} // FlushPendingText

	// ----------------------------------------------------------------------
	// members
	private boolean combineTextWithSameFormat = true;

	private RtfDocument document;
	private ArrayList<IRtfVisual> visualContent;

	private IRtfTextFormat pendingTextFormat;
	private  StringBuilder pendingText = new StringBuilder();

} // class RtfInterpreterListenerDocumentBuilder

