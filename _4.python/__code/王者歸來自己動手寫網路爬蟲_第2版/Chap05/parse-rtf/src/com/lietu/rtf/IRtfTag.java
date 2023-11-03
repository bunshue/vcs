package com.lietu.rtf;

public interface IRtfTag extends IRtfElement
{
	// ----------------------------------------------------------------------
	/// <summary>
	/// Returns the name together with the concatenated value as it stands in the rtf.
	/// </summary>
	String getFullName ();

	// ----------------------------------------------------------------------
	 String getName ();

	// ----------------------------------------------------------------------
	boolean getHasValue ();

	// ----------------------------------------------------------------------
	String getValueAsText();

	// ----------------------------------------------------------------------
	int getValueAsNumber ();

} // interface IRtfTag

