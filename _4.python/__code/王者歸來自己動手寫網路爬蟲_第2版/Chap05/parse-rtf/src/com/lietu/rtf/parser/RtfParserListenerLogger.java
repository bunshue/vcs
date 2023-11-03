package com.lietu.rtf.parser;

import java.util.logging.Logger;

import com.lietu.rtf.IRtfTag;
import com.lietu.rtf.IRtfText;
import com.lietu.rtf.RtfException;


public class RtfParserListenerLogger extends RtfParserListenerBase
	{

		// ----------------------------------------------------------------------
		public RtfParserListenerLogger() throws Exception
		{
			this( new RtfParserLoggerSettings(), systemLogger );
		} // RtfParserListenerLogger

		// ----------------------------------------------------------------------
		public RtfParserListenerLogger( RtfParserLoggerSettings settings ) throws Exception
		{
			this( settings, systemLogger );
		} // RtfParserListenerLogger

		// ----------------------------------------------------------------------
		public RtfParserListenerLogger( Logger logger ) throws Exception
		{
			 this( new RtfParserLoggerSettings(), logger );
		} // RtfParserListenerLogger

		// ----------------------------------------------------------------------
		public RtfParserListenerLogger( RtfParserLoggerSettings settings, Logger logger ) throws Exception
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
		} // RtfParserListenerLogger

		// ----------------------------------------------------------------------
		public RtfParserLoggerSettings getSettings()
		{
			return this.settings; 
		} // Settings

		// ----------------------------------------------------------------------
		public Logger getLogger()
		{
			 return this.logger; 
		} // Logger

		// ----------------------------------------------------------------------
		protected  void DoParseBegin()
		{
			if ( this.settings.getEnabled() &&  this.settings.getParseBeginText()!=null && ""!=this.settings.getParseBeginText()) 
			{
				Log( this.settings.getParseBeginText() );
			}
		} // DoParseBegin

		// ----------------------------------------------------------------------
		protected  void DoGroupBegin()
		{
			if ( this.settings.getEnabled() && ( this.settings.getParseGroupBeginText()!=null && ""!=this.settings.getParseGroupBeginText() ) )
			{
				Log( this.settings.getParseGroupBeginText() );
			}
		} // DoGroupBegin

		// ----------------------------------------------------------------------
		protected  void DoTagFound( IRtfTag tag )
		{
			if ( this.settings.getEnabled() && ( this.settings.getParseTagText()!=null && ""!=this.settings.getParseTagText() ) )
			{
				Log( String.format(
					this.settings.getParseTagText(),
					tag.toString() ) );
			}
		} // DoTagFound

		// ----------------------------------------------------------------------
		protected  void DoTextFound( IRtfText text )
		{
			if ( this.settings.getEnabled() && !( this.settings.getParseTextText()!=null && ""!=this.settings.getParseTextText() ) )
			{
				String msg = text.getText();
				if ( msg.length() > this.settings.getTextMaxLength() && !( this.settings.getTextOverflowText()!=null && ""!=this.settings.getTextOverflowText() ) )
				{
					msg = msg.substring( 0, msg.length() - this.settings.getTextOverflowText().length() ) + this.settings.getTextOverflowText();
				}
				Log( String.format(
					this.settings.getParseTextText(),
					msg ) );
			}
		} // DoTextFound

		// ----------------------------------------------------------------------
		protected  void DoGroupEnd()
		{
			if ( this.settings.getEnabled() && ( this.settings.getParseGroupEndText()!=null && ""!=this.settings.getParseGroupEndText() ) )
			{
				Log( this.settings.getParseGroupEndText() );
			}
		} // DoGroupEnd

		// ----------------------------------------------------------------------
		protected  void DoParseSuccess()
		{
			if ( this.settings.getEnabled() && !( this.settings.getParseSuccessText()!=null && ""!=this.settings.getParseSuccessText() ) )
			{
				Log( this.settings.getParseSuccessText() );
			}
		} // DoParseSuccess

		// ----------------------------------------------------------------------
		protected  void DoParseFail( RtfException reason )
		{
			if ( this.settings.getEnabled() )
			{
				if ( reason != null )
				{
					if (  this.settings.getParseFailKnownReasonText()!=null && ""!=this.settings.getParseFailKnownReasonText() )
					{
						Log( String.format(
							this.settings.getParseFailKnownReasonText(),
							reason.getMessage()) );
					}
				}
				else
				{
					if ( this.settings.getParseFailUnknownReasonText()!=null && ""!=this.settings.getParseFailUnknownReasonText())
					{
						Log( this.settings.getParseFailUnknownReasonText() );
					}
				}
			}
		} // DoParseFail

		// ----------------------------------------------------------------------
		protected  void DoParseEnd()
		{
			if ( this.settings.getEnabled() && !( this.settings.getParseEndText()!=null && ""!=this.settings.getParseEndText() ) )
			{
				Log( this.settings.getParseEndText() );
			}
		} // DoParseEnd

		// ----------------------------------------------------------------------
		private void Log( String... msg )
		{
			String logText = Indent( msg );

			systemLogger.info( logText );

			if ( this.logger != null )
			{
				this.logger.info( logText );
			}
		} // Log

		// ----------------------------------------------------------------------
		private String Indent( String... msg )
		{
			StringBuilder buf = new StringBuilder();
			if ( msg != null )
			{
				for ( int i = 0; i < level; i++ )
				{
					buf.append( " " );
				}
				for ( String m : msg )
				{
					buf.append( m );
				}
			}
			return buf.toString();
		} // Indent

		// ----------------------------------------------------------------------
		// members
		private  RtfParserLoggerSettings settings;
		private  Logger logger;

		private static final Logger systemLogger = Logger.getLogger( RtfParserListenerLogger.class.getName() );

	} // class RtfParserListenerLogger

