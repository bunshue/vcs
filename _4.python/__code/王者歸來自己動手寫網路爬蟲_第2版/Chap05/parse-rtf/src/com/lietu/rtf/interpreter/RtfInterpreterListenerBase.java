package com.lietu.rtf.interpreter;

import java.io.IOException;

import com.lietu.rtf.IRtfInterpreterContext;
import com.lietu.rtf.IRtfInterpreterListener;
import com.lietu.rtf.RtfVisualBreakKind;
import com.lietu.rtf.RtfVisualImageFormat;
import com.lietu.rtf.RtfVisualSpecialCharKind;


	public class RtfInterpreterListenerBase implements IRtfInterpreterListener
	{

		// ----------------------------------------------------------------------
		public RtfInterpreterListenerBase()
		{
		} // RtfInterpreterListenerBase

		// ----------------------------------------------------------------------
		public void BeginDocument( IRtfInterpreterContext context ) throws IOException
		{
			if ( context != null )
			{
				DoBeginDocument( context );
			}
		} // BeginDocument

		@ Override
		public void InsertText( IRtfInterpreterContext context, String text ) throws Exception
		{
			//System.out.println("insert text");
			if ( context != null )
			{
				DoInsertText( context, text );
			}
		} // InsertText

		// ----------------------------------------------------------------------
		public void InsertSpecialChar( IRtfInterpreterContext context, RtfVisualSpecialCharKind kind ) throws Exception
		{
			if ( context != null )
			{
				DoInsertSpecialChar( context, kind );
			}
		} // InsertSpecialChar

		// ----------------------------------------------------------------------
		public void InsertBreak( IRtfInterpreterContext context, RtfVisualBreakKind kind ) throws Exception
		{
			if ( context != null )
			{
				DoInsertBreak( context, kind );
			}
		} // InsertBreak

		// ----------------------------------------------------------------------
		public void InsertImage( IRtfInterpreterContext context, RtfVisualImageFormat format,
			int width, int height, int desiredWidth, int desiredHeight,
			int scaleWidthPercent, int scaleHeightPercent, String imageDataHex
		) throws Exception
		{
			if ( context != null )
			{
				DoInsertImage( context, format,
					width, height, desiredWidth, desiredHeight,
					scaleWidthPercent, scaleHeightPercent, imageDataHex );
			}
		} // InsertImage

		// ----------------------------------------------------------------------
		public void EndDocument( IRtfInterpreterContext context ) throws Exception
		{
			if ( context != null )
			{
				DoEndDocument( context );
			}
		} // EndDocument

		// ----------------------------------------------------------------------
		protected  void DoBeginDocument( IRtfInterpreterContext context ) throws IOException
		{
		} // DoBeginDocument

		protected  void DoInsertText( IRtfInterpreterContext context, String text ) throws Exception
		{
		} // DoInsertText

		// ----------------------------------------------------------------------
		protected  void DoInsertSpecialChar( IRtfInterpreterContext context, RtfVisualSpecialCharKind kind )throws Exception {
		}
		{
		} // DoInsertSpecialChar

		// ----------------------------------------------------------------------
		protected  void DoInsertBreak( IRtfInterpreterContext context, RtfVisualBreakKind kind ) throws Exception
		{
		} // DoInsertBreak

		// ----------------------------------------------------------------------
		protected  void DoInsertImage( IRtfInterpreterContext context,
			RtfVisualImageFormat format,
			int width, int height, int desiredWidth, int desiredHeight,
			int scaleWidthPercent, int scaleHeightPercent,
			String imageDataHex
		) throws Exception
		{
		} // DoInsertImage

		// ----------------------------------------------------------------------
		protected  void DoEndDocument( IRtfInterpreterContext context ) throws Exception
		{
		} // DoEndDocument

	} // class RtfInterpreterListenerBase

