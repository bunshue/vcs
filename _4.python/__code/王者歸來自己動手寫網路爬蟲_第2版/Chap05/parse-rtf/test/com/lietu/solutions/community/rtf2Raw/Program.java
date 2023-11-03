package com.lietu.solutions.community.rtf2Raw;

import com.lietu.rtf.IRtfGroup;
import com.lietu.rtf.converter.text.RtfTextConverter;
import com.lietu.rtf.interpreter.RtfInterpreterListenerFileLogger;
import com.lietu.rtf.interpreterTests.RtfInterpreterTest;
import com.lietu.rtf.parser.RtfParser;
import com.lietu.rtf.parser.RtfParserListenerFileLogger;
import com.lietu.rtf.parser.RtfParserListenerStructureBuilder;
import com.lietu.rtf.parser.RtfSource;
import com.lietu.rtf.support.RtfInterpreterTool;

public class Program
{

	// ----------------------------------------------------------------------
	public static  void main(String[] argv) throws Exception
	{
		//System.out.println((int)';');
		// parse rtf
		String file = //"D:/lg/work/cnlist/minimal.rtf";
			//"D:/lg/work/cnlist/test/ANBOUND-每日金融-第2564期.rtf";
			//"D:/lg/work/cnlist/test/20061101153687.rtf";
			//"D:/lg/work/cnlist/test.rtf";
			//"D:/lg/work/cnlist/n.rtf";
			//"D:/lg/work/cnlist/4.rtf";  // error
			//"D:/lg/work/cnlist/c.rtf";  // error
			//"D:/lg/work/cnlist/z.rtf";
			//"D:/lg/work/cnlist/2.rtf";
			//"D:/lg/work/cnlist/7.rtf";
			//"D:/lg/work/cnlist/t.rtf";
			//"D:/lg/work/cnlist/6.rtf";
			"RtfInterpreterTest_10.rtf";
		IRtfGroup rtfStructure = ParseRtf(file);
		
		// interpret rtf
		String text = InterpretRtf( rtfStructure );

		// display raw text
		DisplayRawText( text );

		//System.out.println( "successfully converted RTF to Raw data " );
		
	} // Execute

	// ----------------------------------------------------------------------
	private static IRtfGroup ParseRtf(String sourceFile) throws Exception
	{
		IRtfGroup rtfStructure = null;
		RtfParserListenerFileLogger parserLogger = null;
		
		// rtf parser
		// open readonly - in case of dominant locks...
		String stream=RtfInterpreterTest.GetTestResource(sourceFile);
	
		// parse the rtf structure
		//System.out.println(stream);
		RtfParserListenerStructureBuilder structureBuilder = new RtfParserListenerStructureBuilder();
		RtfParser parser = new RtfParser( structureBuilder );
		//parser.IgnoreContentAfterRootGroup = true; // support WordPad documents
		parser.setIgnoreContentAfterRootGroup(true);
		if ( parserLogger != null )
		{
			parser.AddParserListener( parserLogger );
		}
		//System.out.println(stream);
		parser.Parse( new RtfSource( stream ) );
		rtfStructure = structureBuilder.getStructureRoot();
	
		return rtfStructure;
	} // ParseRtf
	
	// ----------------------------------------------------------------------
	private static String InterpretRtf( IRtfGroup rtfStructure ) throws Exception
	{
		RtfInterpreterListenerFileLogger interpreterLogger = null;
	
		// text converter
		RtfTextConverter textConverter = new RtfTextConverter();
	
		// rtf parser
		// interpret the rtf structure using the extractors
		RtfInterpreterTool.Interpret( rtfStructure, interpreterLogger, textConverter );

		// get the resulting text
		String text = textConverter.getPlainText();
		//System.out.println("text:"+text);

		return text;
	} // InterpretRtf

	// ----------------------------------------------------------------------
	private static void DisplayRawText( String text )
	{
		System.out.println();
		System.out.println( text );
	} // DisplayRawText

} // class Program
