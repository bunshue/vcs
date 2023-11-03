package com.lietu.rtf;

public interface IRtfVisual
{

	// ----------------------------------------------------------------------
	RtfVisualKind getKind ();

	// ----------------------------------------------------------------------
	void Visit( IRtfVisualVisitor visitor ) throws Exception;

} // interface IRtfVisual

