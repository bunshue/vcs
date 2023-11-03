package com.lietu.rtf.support;

import com.lietu.rtf.IRtfVisualBreak;
import com.lietu.rtf.IRtfVisualImage;
import com.lietu.rtf.IRtfVisualSpecialChar;
import com.lietu.rtf.IRtfVisualText;
import com.lietu.rtf.IRtfVisualVisitor;

	public class RtfVisualVisitorBase implements IRtfVisualVisitor
	{

		// ----------------------------------------------------------------------
		public RtfVisualVisitorBase()
		{
		} // RtfVisualVisitorBase

		// ----------------------------------------------------------------------
		public void VisitText( IRtfVisualText visualText )
		{
			if ( visualText != null )
			{
				DoVisitText( visualText );
			}
		} // VisitText

		// ----------------------------------------------------------------------
		protected  void DoVisitText( IRtfVisualText visualText )
		{
		} // DoVisitText

		// ----------------------------------------------------------------------
		public void VisitBreak( IRtfVisualBreak visualBreak )
		{
			if ( visualBreak != null )
			{
				DoVisitBreak( visualBreak );
			}
		} // VisitBreak

		// ----------------------------------------------------------------------
		protected  void DoVisitBreak( IRtfVisualBreak visualBreak )
		{
		} // DoVisitBreak

		// ----------------------------------------------------------------------
		public void VisitSpecial( IRtfVisualSpecialChar visualSpecialChar )
		{
			if ( visualSpecialChar != null )
			{
				DoVisitSpecial( visualSpecialChar );
			}
		} // VisitSpecial

		// ----------------------------------------------------------------------
		protected  void DoVisitSpecial( IRtfVisualSpecialChar visualSpecialChar )
		{
		} // DoVisitSpecial

		// ----------------------------------------------------------------------
		public void VisitImage( IRtfVisualImage visualImage )
		{
			if ( visualImage != null )
			{
				DoVisitImage( visualImage );
			}
		} // VisitImage

		// ----------------------------------------------------------------------
		protected  void DoVisitImage( IRtfVisualImage visualImage )
		{
		} // DoVisitImage

	} // class RtfVisualVisitorBase
