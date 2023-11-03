package com.lietu.rtf.support;

import com.lietu.rtf.IRtfGroup;
import com.lietu.rtf.IRtfParserListener;
import com.lietu.rtf.IRtfSource;
import com.lietu.rtf.parser.RtfParser;
import com.lietu.rtf.parser.RtfParserListenerStructureBuilder;
import com.lietu.rtf.parser.RtfSource;
import com.lietu.rtf.parser.TextReader;

public final class RtfParserTool
{

	// ----------------------------------------------------------------------
	private RtfParserTool()
	{
	} // RtfParserTool

	// ----------------------------------------------------------------------
	public static IRtfGroup Parse( String rtfText,  IRtfParserListener... listeners ) throws Exception
	{
		return Parse( new RtfSource( rtfText ), listeners );
	} // Parse

	// ----------------------------------------------------------------------
	public static IRtfGroup Parse( TextReader rtfTextSource,  IRtfParserListener... listeners ) throws Exception
	{
		return Parse( new RtfSource( rtfTextSource ), listeners );
	} // Parse

	// ----------------------------------------------------------------------
//		public static IRtfGroup Parse( StringReader rtfTextSource,  IRtfParserListener[] listeners )
//		{
//			return Parse( new RtfSource( rtfTextSource ), listeners );
//		} // Parse

	// ----------------------------------------------------------------------
	public static IRtfGroup Parse( IRtfSource rtfTextSource,  IRtfParserListener... listeners ) throws Exception
	{
		RtfParserListenerStructureBuilder structureBuilder = new RtfParserListenerStructureBuilder();
		RtfParserListenerStructureBuilder[] log = new RtfParserListenerStructureBuilder[1];
		log[0] = structureBuilder;
		RtfParser parser = new RtfParser(log );
		if ( listeners != null )
		{
			for ( IRtfParserListener listener : listeners )
			{
				if ( listener != null )
				{
					parser.AddParserListener( listener );
				}
			}
		}
		//TODO: add here
		parser.setIgnoreContentAfterRootGroup(true);
		//end add
		parser.Parse( rtfTextSource );
		return structureBuilder.getStructureRoot();
	} // Parse

} // class RtfParserTool

