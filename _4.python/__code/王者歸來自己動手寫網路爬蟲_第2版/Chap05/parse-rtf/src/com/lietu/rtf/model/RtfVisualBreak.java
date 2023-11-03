package com.lietu.rtf.model;

import com.lietu.rtf.IRtfVisualBreak;
import com.lietu.rtf.IRtfVisualVisitor;
import com.lietu.rtf.RtfVisualBreakKind;
import com.lietu.rtf.RtfVisualKind;
import com.lietu.rtf.sys.HashTool;


	public final class RtfVisualBreak extends RtfVisual implements IRtfVisualBreak
	{

		// ----------------------------------------------------------------------
		public RtfVisualBreak( RtfVisualBreakKind breakKind ) 
		{
			super( RtfVisualKind.Break );
			this.breakKind = breakKind;
		} // RtfVisualBreak

		// ----------------------------------------------------------------------
		public RtfVisualBreakKind getBreakKind()
		{
			 return this.breakKind; 
		} // BreakKind

		// ----------------------------------------------------------------------
		public  String toString()
		{
			return this.breakKind.toString();
		} // ToString

		// ----------------------------------------------------------------------
		protected  void DoVisit( IRtfVisualVisitor visitor )
		{
			visitor.VisitBreak( this );
		} // DoVisit

		// ----------------------------------------------------------------------
		protected  boolean isEqual( Object obj )
		{
			RtfVisualBreak compare = (RtfVisualBreak)obj  ; // guaranteed to be non-null
			return super.isEqual( compare ) &&
				this.breakKind == compare.breakKind;
		} // IsEqual

		// ----------------------------------------------------------------------
		public  int hashCode()
		{
			return HashTool.AddHashCode( super.ComputeHashCode(), this.breakKind );
		} // ComputeHashCode

		// ----------------------------------------------------------------------
		// members
		private  RtfVisualBreakKind breakKind;

	} // class RtfVisualBreak

