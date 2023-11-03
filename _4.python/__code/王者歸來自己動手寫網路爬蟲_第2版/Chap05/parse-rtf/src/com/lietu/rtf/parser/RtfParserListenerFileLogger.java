package com.lietu.rtf.parser;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

import com.lietu.rtf.IRtfTag;
import com.lietu.rtf.IRtfText;
import com.lietu.rtf.RtfException;


public class RtfParserListenerFileLogger extends RtfParserListenerBase {

	// ----------------------------------------------------------------------
	public final String DefaultLogFileExtension = ".parser.log";

	// ----------------------------------------------------------------------
	public RtfParserListenerFileLogger( String fileName ) throws Exception
	{
		this( fileName, new RtfParserLoggerSettings() );
	} // RtfParserListenerFileLogger

	// ----------------------------------------------------------------------
	public RtfParserListenerFileLogger( String fileName, RtfParserLoggerSettings settings ) throws Exception
	{
		if ( fileName == null )
		{
			throw new Exception( "fileName" );
		}
		if ( settings == null )
		{
			throw new Exception( "settings" );
		}

		this.fileName = fileName;
		this.settings = settings;
	} // RtfParserListenerFileLogger

	// ----------------------------------------------------------------------
	public String getFileName()
	{
		return this.fileName;
	} // FileName

	// ----------------------------------------------------------------------
	public RtfParserLoggerSettings getSettings()
	{
		return this.settings;
	} // Settings

	// ----------------------------------------------------------------------
	public void Dispose() throws IOException
	{
		CloseStream();
	} // Dispose

	// ----------------------------------------------------------------------
	protected void DoParseBegin() throws IOException
	{
		EnsureDirectory();
		OpenStream();

		if ( this.settings.getEnabled() && this.settings.getParseBeginText()!=null )
		{
			//System.out.println( this.settings.getParseBeginText() );
		}
	} // DoParseBegin

	// ----------------------------------------------------------------------
	protected void DoGroupBegin()
	{
		if ( this.settings.getEnabled() && this.settings.getParseGroupBeginText()!=null && !"".equals(this.settings.getParseGroupBeginText())  )
		{
			//System.out.println( this.settings.getParseGroupBeginText() );
		}
	} // DoGroupBegin

	// ----------------------------------------------------------------------
	protected void DoTagFound( IRtfTag tag )
	{
		if ( this.settings.getEnabled() && this.settings.getParseTagText()!=null && !"".equals(this.settings.getParseTagText()) )
		{
			//System.out.println( String.format(
			//	this.settings.getParseTagText(),
			//	tag.toString() ) );
		}
	} // DoTagFound

	// ----------------------------------------------------------------------
	protected void DoTextFound( IRtfText text )
	{
		//System.out.println("found text");
		if ( this.settings.getEnabled() && this.settings.getParseTextText()!=null )
		{
			String msg = text.getText();
			//System.out.println("found text2"+msg);
			if ( msg.length() > this.settings.getTextMaxLength() &&  this.settings.getTextOverflowText()!=null  )
			{
				msg = msg.substring( 0, msg.length() - this.settings.getTextOverflowText().length() ) + this.settings.getTextOverflowText();
			}
			//System.out.println( String.format(
			//	this.settings.getParseTextText(),
			//	msg ) );
		}
	} // DoTextFound

	// ----------------------------------------------------------------------
	protected void DoGroupEnd() throws IOException
	{
		if ( this.settings.getEnabled() && this.settings.getParseGroupEndText()!=null )
		{
			WriteLine( this.settings.getParseGroupEndText() );
		}
	} // DoGroupEnd

	// ----------------------------------------------------------------------
	protected void DoParseSuccess() throws IOException
	{
		if ( this.settings.getEnabled() && ( this.settings.getParseSuccessText()!=null ) )
		{
			WriteLine( this.settings.getParseSuccessText() );
		}
	} // DoParseSuccess

	// ----------------------------------------------------------------------
	protected void DoParseFail( RtfException reason ) throws IOException
	{
		if ( this.settings.getEnabled() )
		{
			if ( reason != null )
			{
				if ( this.settings.getParseFailKnownReasonText()!=null )
				{
					WriteLine( String.format(
						this.settings.getParseFailKnownReasonText(),
						reason.getMessage() ) );
				}
			}
			else
			{
				if ( this.settings.getParseFailUnknownReasonText()!=null )
				{
					WriteLine( this.settings.getParseFailUnknownReasonText() );
				}
			}
		}
	} // DoParseFail

	// ----------------------------------------------------------------------
	protected void DoParseEnd() throws IOException
	{
		if ( this.settings.getEnabled() && this.settings.getParseEndText()!=null )
		{
			WriteLine( this.settings.getParseEndText() );
		}

		CloseStream();
	} // DoParseEnd

	// ----------------------------------------------------------------------
	private void WriteLine( String... msg ) throws IOException
	{
		if ( this.streamWriter == null )
		{
			return;
		}
		String logText = Indent( msg );
		this.streamWriter.write( logText +"\r\n" );
		this.streamWriter.flush();
	} // WriteLine

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
	private void EnsureDirectory()
	{
		File fi = new File( this.fileName );
		if ( ! new File( fi.getAbsolutePath() ).exists() )
		{
			fi.mkdir();
			//Directory.CreateDirectory( fi.DirectoryName );
		}
	} // EnsureDirectory

	// ----------------------------------------------------------------------
	private void OpenStream() throws IOException
	{
		if ( this.streamWriter != null )
		{
			return;
		}
		this.streamWriter = new BufferedWriter( new FileWriter( this.fileName ) );
	} // OpenStream

	// ----------------------------------------------------------------------
	private void CloseStream() throws IOException
	{
		if ( this.streamWriter == null )
		{
			return;
		}
		this.streamWriter.close();
		this.streamWriter = null;
	} // OpenStream

	// ----------------------------------------------------------------------
	// members
	private final String fileName;
	private final RtfParserLoggerSettings settings;
	private BufferedWriter streamWriter;
}
