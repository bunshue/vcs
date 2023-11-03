package com.lietu.rtf.interpreter;

import com.lietu.rtf.IRtfText;
import com.lietu.rtf.RtfElementVisitorOrder;
import com.lietu.rtf.support.RtfElementVisitorBase;

// -- FILE ------------------------------------------------------------------
// name       : RtfTextBuilder.cs
// project    : RTF Framelet
// created    : Leon Poyyayil - 2008.05.23
// language   : c#
// environment: .NET 2.0
// copyright  : (c) 2004-2008 by Itenso GmbH, Switzerland
// --------------------------------------------------------------------------

// ------------------------------------------------------------------------
public class RtfTextBuilder extends RtfElementVisitorBase
{

	// ----------------------------------------------------------------------
	public RtfTextBuilder()
	{
		super( RtfElementVisitorOrder.DepthFirst );
		Reset();
	} // RtfTextBuilder

	// ----------------------------------------------------------------------
	public String getCombinedText()
	{ return this.buffer.toString(); }
	// CombinedText

	// ----------------------------------------------------------------------
	public void Reset()
	{
		this.buffer.setLength(0);
	} // Reset

	// ----------------------------------------------------------------------
	protected void DoVisitText( IRtfText text )
	{
		//System.out.println(":"+text.getText());
		this.buffer.append( text.getText() );
	} // DoVisitText

	// ----------------------------------------------------------------------
	// members
	private final StringBuilder buffer = new StringBuilder();

} // class RtfTextBuilder
