package com.lietu.rtf;

import java.util.ArrayList;
import java.util.Hashtable;

// ------------------------------------------------------------------------
public interface IRtfDocument
{
	// ----------------------------------------------------------------------
	int getRtfVersion() ;

	// ----------------------------------------------------------------------
	IRtfFont getDefaultFont() ;

	// ----------------------------------------------------------------------
	IRtfTextFormat getDefaultTextFormat() ;

	// ----------------------------------------------------------------------
	Hashtable<String,IRtfFont>  getFontTable() ;

	// ----------------------------------------------------------------------
	ArrayList<IRtfColor> getColorTable() ;

	// ----------------------------------------------------------------------
	String getGenerator() ;

	// ----------------------------------------------------------------------
	ArrayList<IRtfTextFormat> getUniqueTextFormats() ;

	// ----------------------------------------------------------------------
	IRtfDocumentInfo getDocumentInfo() ;

	// ----------------------------------------------------------------------
	ArrayList<IRtfDocumentProperty> getUserProperties() ;

	// ----------------------------------------------------------------------
	ArrayList<IRtfVisual> getVisualContent() ;

} // interface IRtfDocument
