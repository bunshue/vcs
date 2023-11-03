package com.lietu.rtf;

public interface IRtfTextFormat
	{

		// ----------------------------------------------------------------------
		IRtfFont getFont ();

		// ----------------------------------------------------------------------
		int getFontSize ();

		// ----------------------------------------------------------------------
		/// <summary>
		/// Combines the setting for sub/super script: negative values are considered
		/// equivalent to subscript, positive values correspond to superscript.<br/>
		/// Same unit as font size.
		/// </summary>
		int getSuperScript ();

		// ----------------------------------------------------------------------
		boolean getIsBold ();

		// ----------------------------------------------------------------------
		boolean getIsItalic ();

		// ----------------------------------------------------------------------
		boolean getIsUnderline ();

		// ----------------------------------------------------------------------
		boolean getIsStrikeThrough ();

		// ----------------------------------------------------------------------
		String getFontDescriptionDebug ();

		// ----------------------------------------------------------------------
		IRtfColor getBackgroundColor ();

		// ----------------------------------------------------------------------
		IRtfColor getForegroundColor ();

		// ----------------------------------------------------------------------
		RtfTextAlignment getAlignment ();

		// ----------------------------------------------------------------------
		IRtfTextFormat getDuplicate() throws Exception;

	} // interface IRtfTextFormat

