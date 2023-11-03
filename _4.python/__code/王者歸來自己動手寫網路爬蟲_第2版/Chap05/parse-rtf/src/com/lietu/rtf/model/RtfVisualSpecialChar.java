package com.lietu.rtf.model;

import com.lietu.rtf.IRtfVisualSpecialChar;
import com.lietu.rtf.IRtfVisualVisitor;
import com.lietu.rtf.RtfVisualKind;
import com.lietu.rtf.RtfVisualSpecialCharKind;
import com.lietu.rtf.sys.HashTool;


	public final class RtfVisualSpecialChar extends RtfVisual implements IRtfVisualSpecialChar
	{

		// ----------------------------------------------------------------------
		public RtfVisualSpecialChar( RtfVisualSpecialCharKind charKind ) 
			
		{
			super( RtfVisualKind.Special );
			this.charKind = charKind;
		} // RtfVisualSpecialChar

		// ----------------------------------------------------------------------
		protected  void DoVisit( IRtfVisualVisitor visitor )
		{
			visitor.VisitSpecial( this );
		} // DoVisit

		// ----------------------------------------------------------------------
		public RtfVisualSpecialCharKind getCharKind()
		{
			 return this.charKind; 
		} // CharKind

		// ----------------------------------------------------------------------
		protected  boolean isEqual( Object obj )
		{
			RtfVisualSpecialChar compare = (RtfVisualSpecialChar)obj; // guaranteed to be non-null
			return super.isEqual( compare ) &&
				this.charKind == compare.charKind;
		} // IsEqual

		// ----------------------------------------------------------------------
		protected  int ComputeHashCode()
		{
			return HashTool.AddHashCode( super.hashCode(), this.charKind );
		} // ComputeHashCode

		// ----------------------------------------------------------------------
		public  String toString()
		{
			return this.charKind.toString();
		} // ToString

		// ----------------------------------------------------------------------
		// members
		private  RtfVisualSpecialCharKind charKind;

	} // class RtfVisualSpecialChar
