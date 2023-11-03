package com.lietu.rtf.interpreterTests;

import com.lietu.rtf.IRtfColor;
import com.lietu.rtf.IRtfDocument;
import com.lietu.rtf.IRtfDocumentProperty;
import com.lietu.rtf.IRtfVisual;
import com.lietu.rtf.IRtfVisualBreak;
import com.lietu.rtf.IRtfVisualImage;
import com.lietu.rtf.IRtfVisualSpecialChar;
import com.lietu.rtf.IRtfVisualText;
import com.lietu.rtf.interpreter.RtfInterpreterListenerFileLogger;
import com.lietu.rtf.support.RtfInterpreterTool;
import com.lietu.rtf.RtfVisualKind;

public class WriteDocumentModel {

	/**
	 * @param args
	 * @throws Exception 
	 */
	public static void main(String[] args) throws Exception {
		String file = "RtfInterpreterTest_10.rtf";
		String stream=RtfInterpreterTest.GetTestResource(file);
		RtfWriteDocumentModel(stream);
	}

// ----------------------------------------------------------------------
public static void RtfWriteDocumentModel(String rtfStream) throws Exception {
	RtfInterpreterListenerFileLogger logger = null;
	IRtfDocument document = RtfInterpreterTool.BuildDoc(rtfStream, logger);
	RtfWriteDocument(document);
} // RtfWriteDocumentModel

// ----------------------------------------------------------------------
public static void RtfWriteDocument(IRtfDocument document) {
	System.out.println("RTF Version: " + document.getRtfVersion());

	// document info
	System.out.println("Title: " + document.getDocumentInfo().getTitle());
	System.out.println("Subject: "
			+ document.getDocumentInfo().getSubject());
	System.out.println("Author: " + document.getDocumentInfo().getAuthor());
	// ...

	// fonts
	for (String fontName : document.getFontTable().keySet()) {
		System.out.println("Font: " + fontName);
	}

	// colors
	for (IRtfColor color : document.getColorTable()) {
		System.out.println("Color: " + color.getAsDrawingColor());
	}

	// user properties
	for (IRtfDocumentProperty documentProperty : document
			.getUserProperties()) {
		System.out.println("User property: " + documentProperty.getName());
	}

	// visuals (preferably handled through an according visitor)
	for (IRtfVisual visual : document.getVisualContent()) {
		RtfVisualKind visualKind = visual.getKind();
		if (visualKind == RtfVisualKind.Text) {
			System.out.println("Text: "
					+ ((IRtfVisualText) visual).getText());
		} else if (visualKind == RtfVisualKind.Break) {
			System.out.println("Tag: "
					+ ((IRtfVisualBreak) visual).getBreakKind().toString());
		} else if (visualKind == RtfVisualKind.Special) {
			System.out.println("Text: "
					+ ((IRtfVisualSpecialChar) visual).getCharKind()
							.toString());
		} else if (visualKind == RtfVisualKind.Image) {
			IRtfVisualImage image = (IRtfVisualImage) visual;
			System.out.println("Image: " + image.getFormat().toString()
					+ " " + image.getWidth() + "x" + image.getHeight());

		}
	}
} // RtfWriteDocument
}
