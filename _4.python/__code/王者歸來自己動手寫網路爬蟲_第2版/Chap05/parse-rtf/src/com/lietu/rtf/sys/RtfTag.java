package com.lietu.rtf.sys;

import com.lietu.rtf.IRtfElementVisitor;
import com.lietu.rtf.IRtfTag;
import com.lietu.rtf.RtfElementKind;
import com.lietu.rtf.model.RtfElement;

public final class RtfTag extends RtfElement implements IRtfTag
{

	// ----------------------------------------------------------------------
	public RtfTag( String name ) throws Exception
	{
		super( RtfElementKind.Tag );
		if ( name == null )
		{
			throw new Exception( "name" );
		}
		this.fullName = name;
		this.name = name;
		this.valueAsText = null;
		this.valueAsNumber = -1;
	} // RtfTag

	// ----------------------------------------------------------------------
	public RtfTag( String name, String value ) throws Exception
	{
		 super( RtfElementKind.Tag );
		if ( name == null )
		{
			throw new Exception( "name" );
		}
		if ( value == null )
		{
			throw new Exception( "value" );
		}
		this.fullName = name + value;
		this.name = name;
		this.valueAsText = value;
		int numericalValue;
		
		try{
		numericalValue = Integer.parseInt(value);
		this.valueAsNumber = numericalValue;
		}catch(Exception e){
			this.valueAsNumber = -1;
		}
		
	} // RtfTag

	// ----------------------------------------------------------------------
	public String getFullName()
	{
		return this.fullName; 
	} // FullName

	// ----------------------------------------------------------------------
	public String getName()
	{
		return this.name;
	} // Name

	// ----------------------------------------------------------------------
	public boolean getHasValue()
	{
		return this.valueAsText != null;
	} // HasValue

	// ----------------------------------------------------------------------
	public String getValueAsText()
	{
		 return this.valueAsText; 
	} // ValueAsText

	// ----------------------------------------------------------------------
	public int getValueAsNumber()
	{
		 return this.valueAsNumber;
	} // ValueAsNumber

	// ----------------------------------------------------------------------
	public String toString()
	{
		return "\\" + this.fullName;
	} // ToString

	// ----------------------------------------------------------------------
	protected  void DoVisit( IRtfElementVisitor visitor ) throws Exception
	{
		visitor.VisitTag( this );
	} // DoVisit

	// ----------------------------------------------------------------------
	protected  boolean isEqual(Object obj )
	{
		RtfTag compare = (RtfTag)obj  ; // guaranteed to be non-null
		return super.isEqual( obj ) &&
			this.fullName.equals( compare.fullName );
	} // IsEqual

	// ----------------------------------------------------------------------
	public  int hashCode()
	{
		int hash = super.ComputeHashCode();
		hash = HashTool.AddHashCode( hash, this.fullName );
		return hash;
	} // ComputeHashCode

	// ----------------------------------------------------------------------
	// members
	private  String fullName;
	private  String name;
	private  String valueAsText;
	private  int valueAsNumber;
} // class RtfTag
