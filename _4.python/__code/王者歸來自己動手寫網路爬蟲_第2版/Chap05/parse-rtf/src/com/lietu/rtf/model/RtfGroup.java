package com.lietu.rtf.model;

import java.util.ArrayList;

import com.lietu.rtf.IRtfElement;
import com.lietu.rtf.IRtfElementVisitor;
import com.lietu.rtf.IRtfGroup;
import com.lietu.rtf.IRtfTag;
import com.lietu.rtf.RtfElementKind;
import com.lietu.rtf.RtfSpec;
import com.lietu.rtf.sys.HashTool;

public final class RtfGroup extends RtfElement implements IRtfGroup
{
	// ----------------------------------------------------------------------
	public RtfGroup()
	{
		super( RtfElementKind.Group );
	} // RtfGroup

	@ Override
	public ArrayList<IRtfElement> getContents()
	{
		 return this.contents; 
	} // Contents

	// ----------------------------------------------------------------------
	public ArrayList<IRtfElement> getWritableContents()
	{
		 return this.contents; 
	} // WritableContents

	@ Override
	public String getDestination()
	{
			if ( this.contents.size() > 0 )
			{
				IRtfElement firstChild = (IRtfElement) this.contents.get(0);
				if ( firstChild.getKind() == RtfElementKind.Tag )
				{
					IRtfTag firstTag = (IRtfTag)firstChild;
					if ( RtfSpec.TagExtensionDestination.equals( firstTag.getName() ) )
					{
						if ( this.contents.size()> 1 )
						{
							IRtfElement secondChild = (IRtfElement) this.contents.get(1);
							if ( secondChild.getKind ()== RtfElementKind.Tag )
							{
								IRtfTag secondTag = (IRtfTag)secondChild;
								return secondTag.getName();
							}
						}
					}
					return firstTag.getName();
				}
			}
			return null;
		
	} // Destination

	// ----------------------------------------------------------------------
	public boolean getIsExtensionDestination()
	{
		
			if ( this.contents.size() > 0 )
			{
				IRtfElement firstChild = (IRtfElement) this.contents.get( 0 );
				if ( firstChild.getKind() == RtfElementKind.Tag )
				{
					IRtfTag firstTag = (IRtfTag)firstChild;
					if ( RtfSpec.TagExtensionDestination.equals( firstTag.getName() ) )
					{
						return true;
					}
				}
			}
			return false;
		
	} // IsExtensionDestination

	// ----------------------------------------------------------------------
	public IRtfGroup SelectChildGroupWithDestination( String destination ) throws Exception
	{
		if ( destination == null )
		{
			throw new Exception( "destination" );
		}
		for( IRtfElement child : this.contents )
		{
			if ( child.getKind() == RtfElementKind.Group )
			{
				IRtfGroup group = (IRtfGroup)child;
				if ( destination.equals( group.getDestination() ) )
				{
					return group;
				}
			}
		}
		return null;
	} // SelectChildGroupWithDestination

	// ----------------------------------------------------------------------
	public  String toString()
	{
		return "{" + this.contents.size() + " items}";
	} // ToString

	// ----------------------------------------------------------------------
	protected  void DoVisit( IRtfElementVisitor visitor ) throws Exception
	{
		visitor.VisitGroup( this );
	} // DoVisit

	// ----------------------------------------------------------------------
	protected  boolean isEqual( Object obj )
	{
		RtfGroup compare = (RtfGroup)obj  ; // guaranteed to be non-null
		return super.isEqual( obj ) &&
			this.contents.equals( compare.contents );
	} // IsEqual

	// ----------------------------------------------------------------------
	public  int hashCode()
	{
		return HashTool.AddHashCode( super.ComputeHashCode(), this.contents );
	} // ComputeHashCode

	// ----------------------------------------------------------------------
	// members
	private  ArrayList<IRtfElement> contents = new ArrayList<IRtfElement>();

} // class RtfGroup

