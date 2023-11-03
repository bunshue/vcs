package com.lietu.rtf.model;

import com.lietu.rtf.IRtfTextFormat;
import com.lietu.rtf.IRtfVisualText;
import com.lietu.rtf.IRtfVisualVisitor;
import com.lietu.rtf.RtfVisualKind;
import com.lietu.rtf.sys.HashTool;


	public final class RtfVisualText extends RtfVisual implements IRtfVisualText
	{

		// ----------------------------------------------------------------------
		public RtfVisualText( String text, IRtfTextFormat format ) throws Exception 
			
		{
			super (RtfVisualKind.Text );
			if ( text == null )
			{
				throw new Exception( "text" );
			}
			if ( format == null )
			{
				throw new Exception( "format" );
			}
			this.text = text;
			this.format = format;
		} // RtfVisualText

		// ----------------------------------------------------------------------
		protected  void DoVisit( IRtfVisualVisitor visitor )
		{
			visitor.VisitText( this );
		} // DoVisit

		// ----------------------------------------------------------------------
		public String getText()
		{
			 return this.text;
		} // Text

		// ----------------------------------------------------------------------
		public IRtfTextFormat getFormat()
		{
			 return this.format; 
		} // Format

		// ----------------------------------------------------------------------
		protected  boolean isEqual( Object obj )
		{
			RtfVisualText compare = (RtfVisualText)obj  ; // guaranteed to be non-null
			return super.isEqual( compare ) &&
				this.text.equals( compare.text ) &&
				this.format.equals( compare.format );
		} // IsEqual

		// ----------------------------------------------------------------------
		public  int hashCode()
		{
			int hash = super.hashCode();
			hash = HashTool.AddHashCode( hash, this.text );
			hash = HashTool.AddHashCode( hash, this.format );
			return hash;
		} // ComputeHashCode

		// ----------------------------------------------------------------------
		public  String toString()
		{
			return "'" + this.text + "'";
		} // toString

		// ----------------------------------------------------------------------
		// members
		private  String text;
		private  IRtfTextFormat format;

	} // class RtfVisualText

