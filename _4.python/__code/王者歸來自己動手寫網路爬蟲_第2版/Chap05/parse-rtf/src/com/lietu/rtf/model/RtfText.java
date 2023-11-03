package com.lietu.rtf.model;

import com.lietu.rtf.IRtfElementVisitor;
import com.lietu.rtf.IRtfText;
import com.lietu.rtf.RtfElementKind;
import com.lietu.rtf.sys.HashTool;


public final class RtfText extends RtfElement implements IRtfText
{

	// ----------------------------------------------------------------------
	public RtfText( String text ) throws Exception
		
	{
		super( RtfElementKind.Text );
		if ( text == null )
		{
			throw new Exception( "text" );
		}
		this.text = text;
	} // RtfText

	// ----------------------------------------------------------------------
	public String getText()
	{
		 return this.text; 
	} // Text

	// ----------------------------------------------------------------------
	public  String toString()
	{
		return this.text;
	} // ToString

	// ----------------------------------------------------------------------
	protected  void DoVisit( IRtfElementVisitor visitor ) throws Exception
	{
		visitor.VisitText( this );
	} // DoVisit

	// ----------------------------------------------------------------------
	protected  boolean isEqual( Object obj )
	{
		RtfText compare = (RtfText)obj  ; // guaranteed to be non-null
		return super.isEqual( obj ) &&
			this.text.equals( compare.text );
	} // IsEqual

	// ----------------------------------------------------------------------
	public  int hashCode()
	{
		return HashTool.AddHashCode( super.ComputeHashCode(), this.text );
	} // ComputeHashCode

	// ----------------------------------------------------------------------
	// members
	private  String text;

} // class RtfText
