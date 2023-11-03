package com.lietu.rtf.model;

import com.lietu.rtf.IRtfElement;
import com.lietu.rtf.IRtfElementVisitor;
import com.lietu.rtf.RtfElementKind;
import com.lietu.rtf.sys.HashTool;

public abstract class RtfElement implements IRtfElement
{
	// ----------------------------------------------------------------------
	protected RtfElement( RtfElementKind kind )
	{
		this.kind = kind;
	} // RtfElement

	@Override
	public RtfElementKind getKind()
	{
		 return this.kind; 
	} // Kind

	@Override
	public void Visit( IRtfElementVisitor visitor ) throws Exception
	{
		try {
			if ( visitor == null )
			{
				throw new Exception( "visitor" );
			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		DoVisit( visitor );
	} // Visit

	// ----------------------------------------------------------------------
	public   boolean equals( Object obj )
	{
		if ( obj == this )
		{
			return true;
		}
		else if ( obj == null || this.getClass() != obj.getClass() )
		{
			return false;
		}
		return isEqual( obj );
	} // Equals

	// ----------------------------------------------------------------------
	public   int hashCode()
	{
		return HashTool.AddHashCode( this.hashCode(), ComputeHashCode() );
	} // GetHashCode

	// ----------------------------------------------------------------------
	protected abstract void DoVisit( IRtfElementVisitor visitor ) throws Exception;

	// ----------------------------------------------------------------------
	protected boolean isEqual( Object obj )
	{
		//RtfElement compare = (RtfElement)obj  ; // guaranteed to be non-null
		return true;
	} // IsEqual

	// ----------------------------------------------------------------------
	protected  int ComputeHashCode()
	{
		return 0x0f00ba11;
	} // ComputeHashCode

	// ----------------------------------------------------------------------
	// members
	private  RtfElementKind kind;

} // class RtfElement
