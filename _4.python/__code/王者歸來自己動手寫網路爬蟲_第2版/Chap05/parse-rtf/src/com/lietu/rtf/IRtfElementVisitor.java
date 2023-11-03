package com.lietu.rtf;

	public interface IRtfElementVisitor
	{

		// ----------------------------------------------------------------------
		public void VisitTag( IRtfTag tag ) throws Exception;

		// ----------------------------------------------------------------------
		public void VisitGroup( IRtfGroup group ) throws Exception;

		// ----------------------------------------------------------------------
		public void VisitText( IRtfText text )  throws Exception;

	} // interface IRtfElementVisitor

