package com.lietu.rtf.parserTests;

import java.util.Map.Entry;

import com.lietu.rtf.IRtfColor;
import com.lietu.rtf.IRtfDocument;
import com.lietu.rtf.IRtfDocumentProperty;
import com.lietu.rtf.IRtfElement;
import com.lietu.rtf.IRtfFont;
import com.lietu.rtf.IRtfGroup;
import com.lietu.rtf.IRtfTag;
import com.lietu.rtf.IRtfText;
import com.lietu.rtf.RtfElementKind;
import com.lietu.rtf.interpreter.RtfInterpreterListenerFileLogger;
import com.lietu.rtf.parser.RtfParser;
import com.lietu.rtf.parser.RtfParserListenerStructureBuilder;
import com.lietu.rtf.parser.RtfSource;
import com.lietu.rtf.support.RtfInterpreterTool;

public class RtfParserDump {
	public static void main(String[] args) throws Exception {
		RtfSympleParser();
		RtfSympleInterpreter();
		System.in.read();
	} // Main

	// ----------------------------------------------------------------------
	static void RtfSympleParser() throws Exception {
		RtfParser parser = new RtfParser();
		RtfParserListenerStructureBuilder structureBuilder = new RtfParserListenerStructureBuilder();
		parser.AddParserListener(structureBuilder);
		parser.Parse(new RtfSource("{\\rtf1foobar}"));
		RtfDumpElement(structureBuilder.getStructureRoot());
	} // RtfSympleParser

	// ----------------------------------------------------------------------
	static void RtfDumpElement(IRtfElement rtfElement) {
		RtfElementKind getKind = rtfElement.getKind();
		if (getKind == RtfElementKind.Group) {
			// System.out.println( "Group: " +
			// ((IRtfGroup)rtfElement).getDestination() );
			for (IRtfElement rtfChildElement : ((IRtfGroup) rtfElement)
					.getContents()) {
				RtfDumpElement(rtfChildElement);
			}
		} else if (getKind == RtfElementKind.Tag) {
			 System.out.println( "Tag: " + ((IRtfTag)rtfElement).getFullName() );
		} else if (getKind == RtfElementKind.Text) {
			System.out.println( "Text: " + ((IRtfText)rtfElement).getText());
		}

	} // RtfDumpElement

	// ----------------------------------------------------------------------
	static void RtfSympleInterpreter() throws Exception {
		RtfInterpreterListenerFileLogger logger = new RtfInterpreterListenerFileLogger(
				"c:\\temp\\RtfInterpreter.log");
		RtfInterpreterListenerFileLogger[] log = new RtfInterpreterListenerFileLogger[1];
		log[0] = logger;
		IRtfDocument document = RtfInterpreterTool.BuildDoc("{\rtf1foobar}",
				log);
		RtfWriteDocument(document);
	} // RtfSympleInterpreter

	// ----------------------------------------------------------------------
	static void RtfWriteDocument(IRtfDocument document) {
		// System.out.println( "RTF Version: " + document.getRtfVersion());

		// document info
		// System.out.println( "Title: " + document.getDocumentInfo().getTitle()
		// );
		// System.out.println( "Subject: " +
		// document.getDocumentInfo().getSubject() );
		// System.out.println( "Author: " +
		// document.getDocumentInfo().getAuthor() );
		// ...

		// fonts
		for (Entry<String, IRtfFont> font : document.getFontTable().entrySet()) {
			System.out.println("Font: " + font.getKey());
		}

		// colors
		for (IRtfColor color : document.getColorTable()) {
			System.out
					.println("Color: " + color.getAsDrawingColor().toString());
		}

		// user properties
		for (IRtfDocumentProperty documentProperty : document
				.getUserProperties()) {
			System.out.println("User property: " + documentProperty.getName());
		}

		// visuals
		/*
		 * for ( IRtfVisual visual : document.getVisualContent() ) {
		 * RtfVisualKind getKind=visual.getKind();
		 * if(getKind==RtfVisualKind.Text){ System.out.println( "Text: " + (
		 * (IRtfVisualText)visual ).getText()); }else
		 * if(getKind==RtfVisualKind.Break){ System.out.println( "Tag: " + (
		 * (IRtfVisualBreak)visual ).getBreakKind().toString() ); }else
		 * if(getKind==RtfVisualKind.Special){ System.out.println( "Text: " + (
		 * (IRtfVisualSpecialChar)visual ).getCharKind().toString() ); }else
		 * if(getKind==RtfVisualKind.Image){ IRtfVisualImage image =
		 * (IRtfVisualImage)visual; System.out.println( "Text: " +
		 * image.getFormat().toString() + " " + image.getWidth() + "x" +
		 * image.getHeight() ); } }
		 */
	} // RtfWriteElement

} // class RtfParser

