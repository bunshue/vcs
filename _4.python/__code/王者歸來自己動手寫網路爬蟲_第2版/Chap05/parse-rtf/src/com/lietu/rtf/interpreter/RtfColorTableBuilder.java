package com.lietu.rtf.interpreter;

import java.util.ArrayList;

import com.lietu.rtf.IRtfColor;
import com.lietu.rtf.IRtfGroup;
import com.lietu.rtf.IRtfTag;
import com.lietu.rtf.IRtfText;
import com.lietu.rtf.RtfElementVisitorOrder;
import com.lietu.rtf.RtfSpec;
import com.lietu.rtf.model.RtfColor;
import com.lietu.rtf.support.RtfElementVisitorBase;


	public final class RtfColorTableBuilder extends RtfElementVisitorBase
	{

		// ----------------------------------------------------------------------
		public RtfColorTableBuilder( ArrayList<IRtfColor> colorTable ) throws Exception 
		{
			super( RtfElementVisitorOrder.NonRecursive );
			// we iterate over our children ourselves -> hence non-recursive
			if ( colorTable == null )
			{
				throw new Exception( "colorTable" );
			}
			this.colorTable = colorTable;
		} // RtfColorTableBuilder

		// ----------------------------------------------------------------------
		public void Reset()
		{
			this.colorTable.clear();
			this.curRed = 0;
			this.curGreen = 0;
			this.curBlue = 0;
		} // Reset

		// ----------------------------------------------------------------------
		protected  void DoVisitGroup( IRtfGroup group ) throws Exception
		{
			if ( RtfSpec.TagColorTable.equals( group.getDestination() ) )
			{
				VisitGroupChildren( group );
			}
		} // DoVisitGroup

		// ----------------------------------------------------------------------
		protected  void DoVisitTag( IRtfTag tag )
		{
			if ( tag.getName().equals(RtfSpec.TagColorRed) )
			{
					this.curRed = tag.getValueAsNumber();
			}
			else if(tag.getName().equals(RtfSpec.TagColorGreen))
			{
					this.curGreen = tag.getValueAsNumber();
			}
			else if( tag.getName().equals( RtfSpec.TagColorBlue) )
			{
				this.curBlue = tag.getValueAsNumber();
			}
		} // DoVisitTag

		// ----------------------------------------------------------------------
		protected void DoVisitText( IRtfText text ) throws Exception
		{
			if ( RtfSpec.TagDelimiter.equals( text.getText() ) )
			{
				this.colorTable.add( new RtfColor( curRed, curGreen, curBlue ) );
				this.curRed = 0;
				this.curGreen = 0;
				this.curBlue = 0;
			}
			else
			{
				throw new Exception( "unsupported text in color table: '" + text.getText() + "'" );
			}
		} // DoVisitText

		// ----------------------------------------------------------------------
		// members
		private  ArrayList<IRtfColor> colorTable;

		private int curRed;
		private int curGreen;
		private int curBlue;

	} // class RtfColorBuilder
