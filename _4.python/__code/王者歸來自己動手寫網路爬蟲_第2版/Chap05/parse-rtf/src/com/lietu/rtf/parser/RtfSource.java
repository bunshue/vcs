package com.lietu.rtf.parser;

import java.io.InputStream;
import java.io.StringReader;

import com.lietu.rtf.IRtfSource;

public final class RtfSource implements IRtfSource
{

	// ----------------------------------------------------------------------
	public RtfSource( String rtf ) throws Exception
	{
		if ( rtf == null )
		{
			throw new Exception( "rtf" );
		}
		this.reader = new TextReader( new StringReader( rtf) );
	} // RtfSource

	// ----------------------------------------------------------------------
	public RtfSource( TextReader rtf ) throws Exception
	{
		if ( rtf == null )
		{
			throw new Exception( "rtf" );
		}
		this.reader = rtf;
	} // RtfSource

	// ----------------------------------------------------------------------
	public RtfSource( InputStream rtf ) throws Exception
	{
		if ( rtf == null )
		{
			throw new Exception( "rtf" );
		}
		this.reader = new TextReader( rtf );
		//new StreamReader( rtf, RtfSpec.AnsiEncoding );
	} // RtfSource
	
	// ----------------------------------------------------------------------
	public TextReader getReader()
	{
		 return this.reader;
	} // Reader

	// ----------------------------------------------------------------------
	// members
	private  TextReader reader;

} // class RtfSource

