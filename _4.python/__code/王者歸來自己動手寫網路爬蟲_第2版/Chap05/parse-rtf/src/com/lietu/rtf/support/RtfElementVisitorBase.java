package com.lietu.rtf.support;

import com.lietu.rtf.IRtfElement;
import com.lietu.rtf.IRtfElementVisitor;
import com.lietu.rtf.IRtfGroup;
import com.lietu.rtf.IRtfTag;
import com.lietu.rtf.IRtfText;
import com.lietu.rtf.RtfElementVisitorOrder;

	public class RtfElementVisitorBase implements IRtfElementVisitor
	{

		// ----------------------------------------------------------------------
		public RtfElementVisitorBase( RtfElementVisitorOrder order )
		{
			this.order = order;
		} // RtfElementVisitorBase

		// ----------------------------------------------------------------------
		public void VisitTag( IRtfTag tag )
		{
			if ( tag != null )
			{
				DoVisitTag( tag );
			}
		} // VisitTag

		// ----------------------------------------------------------------------
		protected  void DoVisitTag( IRtfTag tag )
		{
		} // DoVisitTag

		// ----------------------------------------------------------------------
		public void VisitGroup( IRtfGroup group ) throws Exception
		{
			if ( group != null )
			{
				if ( this.order == RtfElementVisitorOrder.DepthFirst )
				{
					VisitGroupChildren( group );
				}
				DoVisitGroup( group );
				if ( this.order == RtfElementVisitorOrder.BreadthFirst )
				{
					VisitGroupChildren( group );
				}
			}
		} // VisitGroup

		// ----------------------------------------------------------------------
		protected  void DoVisitGroup( IRtfGroup group ) throws Exception
		{
		} // DoVisitGroup

		// ----------------------------------------------------------------------
		protected void VisitGroupChildren( IRtfGroup group ) throws Exception
		{
			for ( IRtfElement child : group.getContents() )
			{
				child.Visit( this );
			}
		} // VisitGroupChildren

		// ----------------------------------------------------------------------
		public void VisitText( IRtfText text ) throws Exception
		{
			if ( text != null )
			{
				DoVisitText( text );
			}
		} // VisitText

		// ----------------------------------------------------------------------
		protected  void DoVisitText( IRtfText text ) throws Exception
		{
		} // DoVisitText

		// ----------------------------------------------------------------------
		// members
		private  RtfElementVisitorOrder order;

	} // class RtfElementVisitorBase

