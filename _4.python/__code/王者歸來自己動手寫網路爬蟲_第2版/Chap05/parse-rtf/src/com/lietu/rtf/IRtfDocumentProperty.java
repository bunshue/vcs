package com.lietu.rtf;

	public interface IRtfDocumentProperty
	{

		// ----------------------------------------------------------------------
		int getPropertyKindCode ();

		// ----------------------------------------------------------------------
		RtfPropertyKind getPropertyKind ();

		// ----------------------------------------------------------------------
		String getName ();

		// ----------------------------------------------------------------------
		String getStaticValue ();

		// ----------------------------------------------------------------------
		String getLinkValue ();

	} // interface IRtfDocumentProperty
