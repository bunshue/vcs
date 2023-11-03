package com.lietu.rtf;

public interface IRtfElement
{

	// ----------------------------------------------------------------------
	RtfElementKind getKind();

	// ----------------------------------------------------------------------
	void Visit( IRtfElementVisitor visitor ) throws Exception;

} // interface IRtfElement
