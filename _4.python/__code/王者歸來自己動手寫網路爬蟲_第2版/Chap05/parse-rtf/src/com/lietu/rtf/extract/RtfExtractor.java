package com.lietu.rtf.extract;

import java.io.InputStream;

import com.lietu.rtf.IRtfGroup;
import com.lietu.rtf.converter.text.RtfTextConverter;
import com.lietu.rtf.interpreter.RtfInterpreterListenerFileLogger;
import com.lietu.rtf.parser.RtfParser;
import com.lietu.rtf.parser.RtfParserListenerStructureBuilder;
import com.lietu.rtf.parser.RtfSource;
import com.lietu.rtf.support.RtfInterpreterTool;

public class RtfExtractor {
	private IRtfGroup rtfStructure;
	
	public RtfExtractor(InputStream is) throws Exception
	{
		// parse the rtf structure
		//System.out.println(stream);
		RtfParserListenerStructureBuilder structureBuilder = new RtfParserListenerStructureBuilder();
		RtfParser parser = new RtfParser( structureBuilder );
		//parser.IgnoreContentAfterRootGroup = true; // support WordPad documents
		parser.setIgnoreContentAfterRootGroup(true);
		
		parser.Parse( new RtfSource( is ) );
		rtfStructure = structureBuilder.getStructureRoot();
	}

	public RtfExtractor(String is) throws Exception
	{
		// parse the rtf structure
		//System.out.println(stream);
		RtfParserListenerStructureBuilder structureBuilder = new RtfParserListenerStructureBuilder();
		RtfParser parser = new RtfParser( structureBuilder );
		//parser.IgnoreContentAfterRootGroup = true; // support WordPad documents
		parser.setIgnoreContentAfterRootGroup(true);
		
		parser.Parse( new RtfSource( is ) );
		rtfStructure = structureBuilder.getStructureRoot();
	}
	
	public String getText() throws Exception
	{
		RtfInterpreterListenerFileLogger interpreterLogger = null;
		
		// text converter
		RtfTextConverter textConverter = new RtfTextConverter();
	
		// rtf parser
		// interpret the rtf structure using the extractors
		RtfInterpreterTool.Interpret( rtfStructure, interpreterLogger, textConverter );

		// get the resulting text
		return  textConverter.getPlainText();
	}
}
