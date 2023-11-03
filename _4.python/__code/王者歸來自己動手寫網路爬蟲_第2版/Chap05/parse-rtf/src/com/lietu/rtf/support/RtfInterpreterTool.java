package com.lietu.rtf.support;

import com.lietu.rtf.IRtfDocument;
import com.lietu.rtf.IRtfGroup;
import com.lietu.rtf.IRtfInterpreterListener;
import com.lietu.rtf.IRtfSource;
import com.lietu.rtf.interpreter.RtfInterpreter;
import com.lietu.rtf.interpreter.RtfInterpreterListenerDocumentBuilder;
import com.lietu.rtf.parser.TextReader;

public final class RtfInterpreterTool
{

	// ----------------------------------------------------------------------
	private RtfInterpreterTool()
	{
	} // RtfInterpreterTool

	// ----------------------------------------------------------------------
	public static IRtfDocument BuildDoc( String rtfText,  IRtfInterpreterListener... listeners ) throws Exception
	{
		return BuildDoc( RtfParserTool.Parse( rtfText ), listeners );
	} // BuildDoc

	// ----------------------------------------------------------------------
	public static IRtfDocument BuildDoc( TextReader rtfTextSource,  IRtfInterpreterListener... listeners ) throws Exception
	{
		return BuildDoc( RtfParserTool.Parse( rtfTextSource), listeners );
	} // BuildDoc

	// ----------------------------------------------------------------------
	public static IRtfDocument BuildDoc( IRtfSource rtfTextSource,  IRtfInterpreterListener... listeners ) throws Exception
	{
		return BuildDoc( RtfParserTool.Parse( rtfTextSource), listeners );
	} // BuildDoc

	// ----------------------------------------------------------------------
	public static IRtfDocument BuildDoc( IRtfGroup rtfDocument,  IRtfInterpreterListener... listeners ) throws Exception
	{
		RtfInterpreterListenerDocumentBuilder docBuilder = new RtfInterpreterListenerDocumentBuilder();
		IRtfInterpreterListener[] allListeners;
		if ( listeners == null )
		{
			allListeners = new IRtfInterpreterListener[] { docBuilder };
		}
		else
		{
			allListeners = new IRtfInterpreterListener[ listeners.length + 1 ];
			allListeners[ 0 ] = docBuilder;
			System.arraycopy(listeners, 0, allListeners, 1, listeners.length);
			//listeners.CopyTo( allListeners, 1 );
		}
		Interpret( rtfDocument, allListeners );
		return docBuilder.getDocument();
	} // BuildDoc

	// ----------------------------------------------------------------------
	public static void Interpret( String rtfText,  IRtfInterpreterListener... listeners ) throws Exception
	{
		Interpret( RtfParserTool.Parse( rtfText), listeners );
	} // Interpret

	// ----------------------------------------------------------------------
	public static void Interpret( TextReader rtfTextSource,  IRtfInterpreterListener... listeners ) throws Exception
	{
		Interpret( RtfParserTool.Parse( rtfTextSource), listeners );
	} // Interpret

	// ----------------------------------------------------------------------
	public static void Interpret( IRtfSource rtfTextSource,  IRtfInterpreterListener... listeners ) throws Exception
	{
		Interpret( RtfParserTool.Parse( rtfTextSource), listeners );
	} // Interpret

	// ----------------------------------------------------------------------
	public static void Interpret( IRtfGroup rtfDocument,  IRtfInterpreterListener... listeners ) throws Exception
	{
		RtfInterpreter parser = new RtfInterpreter();
		if ( listeners != null )
		{
			for( IRtfInterpreterListener listener : listeners )
			{
				if ( listener != null )
				{
					parser.AddInterpreterListener( listener );
				}
			}
		}
		parser.Interpret( rtfDocument );
	} // Interpret
}
	