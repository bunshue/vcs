package com.lietu.rtf.model;

import com.lietu.rtf.IRtfVisual;
import com.lietu.rtf.IRtfVisualVisitor;
import com.lietu.rtf.RtfVisualKind;
import com.lietu.rtf.sys.HashTool;


public abstract class RtfVisual implements IRtfVisual
{

	// ----------------------------------------------------------------------
	protected RtfVisual( RtfVisualKind kind )
	{
		this.kind = kind;
	} // RtfVisual

	// ----------------------------------------------------------------------
	public RtfVisualKind getKind()
	{
		 return this.kind; 
	} // Kind

	// ----------------------------------------------------------------------
	public void Visit( IRtfVisualVisitor visitor ) throws Exception
	{
		if ( visitor == null )
		{
			throw new Exception( "visitor" );
		}
		DoVisit( visitor );
	} // Visit

	// ----------------------------------------------------------------------
	public   boolean Equals( Object obj )
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
		return HashTool.AddHashCode(this.hashCode(), ComputeHashCode() );
	} // GetHashCode

	// ----------------------------------------------------------------------
	protected abstract void DoVisit( IRtfVisualVisitor visitor );

	// ----------------------------------------------------------------------
	protected  boolean isEqual( Object obj )
	{
		//RtfVisual compare = (RtfVisual)obj ; // guaranteed to be non-null
		return true;
	} // IsEqual

	// ----------------------------------------------------------------------
	protected  int ComputeHashCode()
	{
		return 0x0f00ba11;
	} // ComputeHashCode

	// ----------------------------------------------------------------------
	// members
	private  RtfVisualKind kind;

} // class RtfVisual

