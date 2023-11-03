package com.lietu.rtf;

import java.util.ArrayList;
import java.util.Hashtable;

public interface IRtfInterpreterContext
{
	// ----------------------------------------------------------------------
	RtfInterpreterState getState ();

	// ----------------------------------------------------------------------
	int getRtfVersion ();

	// ----------------------------------------------------------------------
	String getDefaultFontId ();

	// ----------------------------------------------------------------------
	IRtfFont getDefaultFont () throws Exception;

	// ----------------------------------------------------------------------
	Hashtable<String,IRtfFont> getFontTable ();

	// ----------------------------------------------------------------------
	ArrayList<IRtfColor> getColorTable ();

	// ----------------------------------------------------------------------
	String getGenerator ();

	// ----------------------------------------------------------------------
	ArrayList<IRtfTextFormat> getUniqueTextFormats ();

	// ----------------------------------------------------------------------
	IRtfTextFormat getCurrentTextFormat ();

	// ----------------------------------------------------------------------
	IRtfTextFormat getGetSafeCurrentTextFormat() throws Exception;

	// ----------------------------------------------------------------------
	IRtfDocumentInfo getDocumentInfo ();

	// ----------------------------------------------------------------------
	ArrayList<IRtfDocumentProperty> getUserProperties ();

} // interface IRtfInterpreterContext

