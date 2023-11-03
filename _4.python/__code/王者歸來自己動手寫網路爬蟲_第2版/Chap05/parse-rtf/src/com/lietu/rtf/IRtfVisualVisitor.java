package com.lietu.rtf;

public interface IRtfVisualVisitor
	{

		// ----------------------------------------------------------------------
		void VisitText( IRtfVisualText visualText );

		// ----------------------------------------------------------------------
		void VisitBreak( IRtfVisualBreak visualBreak );

		// ----------------------------------------------------------------------
		void VisitSpecial( IRtfVisualSpecialChar visualSpecialChar );

		// ----------------------------------------------------------------------
		void VisitImage( IRtfVisualImage visualImage );

	} // interface IRtfVisualVisitor

