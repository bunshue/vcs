package com.lietu.rtf.interpreter;


import java.util.logging.Logger;

import com.lietu.rtf.IRtfInterpreterContext;
import com.lietu.rtf.RtfVisualBreakKind;
import com.lietu.rtf.RtfVisualImageFormat;
import com.lietu.rtf.RtfVisualSpecialCharKind;

	public class RtfInterpreterListenerLogger extends RtfInterpreterListenerBase
	{

		// ----------------------------------------------------------------------
		public RtfInterpreterListenerLogger() throws Exception
		
		{
			this( new RtfInterpreterLoggerSettings(), systemLogger  );
		} // RtfInterpreterListenerLogger

		// ----------------------------------------------------------------------
		public RtfInterpreterListenerLogger( RtfInterpreterLoggerSettings settings ) throws Exception
			
		{
			this( settings, systemLogger );
		} // RtfInterpreterListenerLogger

		// ----------------------------------------------------------------------
		public RtfInterpreterListenerLogger( Logger logger ) throws Exception
			 
		{
			this( new RtfInterpreterLoggerSettings(), logger );
		} // RtfInterpreterListenerLogger

		// ----------------------------------------------------------------------
		public RtfInterpreterListenerLogger( RtfInterpreterLoggerSettings settings, Logger logger ) throws Exception
		{
			if ( settings == null )
			{
				throw new Exception( "settings" );
			}
			if ( logger == null )
			{
				throw new Exception( "logger" );
			}

			this.settings = settings;
			this.logger = logger;
		} // RtfInterpreterListenerLogger

		// ----------------------------------------------------------------------
		public RtfInterpreterLoggerSettings getSettings()
		{
			  return this.settings; 
		} // Settings

		// ----------------------------------------------------------------------
		public Logger getLogger()
		{
			return this.logger; 
		} // Logger

		// ----------------------------------------------------------------------
		protected  void DoBeginDocument( IRtfInterpreterContext context )
		{
			if ( this.settings.getEnabled() && this.settings.getBeginDocumentText()!=null &&""!=this.settings.getBeginDocumentText() )
			{
				Log( this.settings.getBeginDocumentText() );
			}
		} // DoBeginDocument

		// ----------------------------------------------------------------------
		protected  void DoInsertText( IRtfInterpreterContext context, String text ) throws Exception
		{
			if ( this.settings.getEnabled() && this.settings.getTextFormatText()!=null && ""!=this.settings.getTextFormatText() )
			{
				String msg = text;
				if ( msg.length() > this.settings.getTextMaxLength() && this.settings.getTextOverflowText()!=null && ""!=this.settings.getTextOverflowText() )
				{
					msg = msg.substring( 0, msg.length() - this.settings.getTextOverflowText().length() ) + this.settings.getTextOverflowText();
				}
				Log( String.format(
					
					this.settings.getTextFormatText(),
					msg,
					context.getGetSafeCurrentTextFormat() ) );
			}
		} // DoInsertText

		// ----------------------------------------------------------------------
		protected  void DoInsertSpecialChar( IRtfInterpreterContext context, RtfVisualSpecialCharKind kind )
		{
			if ( this.settings.getEnabled() && this.settings.getSpecialCharFormatText()!=null && ""!=this.settings.getSpecialCharFormatText() )
			{
				Log( String.format(
					
					this.settings.getSpecialCharFormatText(),
					kind ) );
			}
		} // DoInsertSpecialChar

		// ----------------------------------------------------------------------
		protected  void DoInsertBreak( IRtfInterpreterContext context, RtfVisualBreakKind kind )
		{
			if ( this.settings.getEnabled() && this.settings.getBreakFormatText()!=null && ""!=this.settings.getBreakFormatText() )
			{
				Log( String.format(
					
					this.settings.getBreakFormatText(),
					kind ) );
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
			if ( this.settings.getEnabled() && this.settings.getImageFormatText()!=null && ""!=this.settings.getImageFormatText() )
			{
				Log( String.format(
				
					this.settings.getImageFormatText(),
					format,
					width,
					height,
					desiredWidth,
					desiredHeight,
					scaleWidthPercent,
					scaleHeightPercent,
					imageDataHex,
					(imageDataHex.length() / 2) ) );
			}
		} // DoInsertImage

		// ----------------------------------------------------------------------
		protected  void DoEndDocument( IRtfInterpreterContext context )
		{
			if ( this.settings.getEnabled() && this.settings.getEndDocumentText()!=null && ""!=this.settings.getEndDocumentText() )
			{
				Log( this.settings.getEndDocumentText() );
			}
		} // DoEndDocument

		// ----------------------------------------------------------------------
		private void Log( String message )
		{
			systemLogger.info( message );
			if ( this.logger != null )
			{
				this.logger.info( message );
			}
		} // Log

		// ----------------------------------------------------------------------
		// members
		private final RtfInterpreterLoggerSettings settings;
		private final Logger logger;

		private static final Logger systemLogger = Logger.getLogger(RtfInterpreterListenerLogger.class.getName());

			//Itenso.Sys.Logging.Logger.GetLogger( typeof( RtfInterpreterListenerLogger ) );

	} // class RtfInterpreterListenerLogger

