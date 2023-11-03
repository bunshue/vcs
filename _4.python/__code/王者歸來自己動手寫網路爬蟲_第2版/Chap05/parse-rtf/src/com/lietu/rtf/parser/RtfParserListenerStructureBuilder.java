package com.lietu.rtf.parser;

import java.util.Stack;

import com.lietu.rtf.IRtfGroup;
import com.lietu.rtf.IRtfTag;
import com.lietu.rtf.IRtfText;
import com.lietu.rtf.model.RtfGroup;

public final class RtfParserListenerStructureBuilder extends RtfParserListenerBase
{

	// ----------------------------------------------------------------------
	public RtfParserListenerStructureBuilder()
	{
	} // RtfParserListenerStructureBuilder

	// ----------------------------------------------------------------------
	public IRtfGroup getStructureRoot()
	{
		 return this.structureRoot; 
	} // StructureRoot

	// ----------------------------------------------------------------------
	protected  void DoParseBegin()
	{
		this.openGroupStack.clear();
		this.curGroup = null;
		this.structureRoot = null;
	} // DoParseBegin

	// ----------------------------------------------------------------------
	protected  void DoGroupBegin()
	{
		RtfGroup newGroup = new RtfGroup();
		if ( this.curGroup != null )
		{
			this.openGroupStack.push( this.curGroup );
			this.curGroup.getWritableContents().add( newGroup );
		}
		this.curGroup = newGroup;
	} // DoGroupBegin

	// ----------------------------------------------------------------------
	protected  void DoTagFound( IRtfTag tag ) throws Exception
	{
		if ( this.curGroup == null )
		{
			throw new Exception( "invalid state: no group available yet for adding a tag" );
		}
		this.curGroup.getWritableContents().add( tag );
		//System.out.println("TagFound:"+tag);
	} // DoTagFound

	// ----------------------------------------------------------------------
	protected  void DoTextFound( IRtfText text ) throws Exception
	{
		if ( this.curGroup == null )
		{
			throw new Exception( "invalid state: no group available yet for adding a text" );
		}
		//System.out.println( text .getText());
		this.curGroup.getWritableContents().add( text );
	} // DoTextFound

	// ----------------------------------------------------------------------
	protected  void DoGroupEnd() throws Exception
	{
		if ( this.openGroupStack.size() > 0 )
		{
			this.curGroup = this.openGroupStack.pop();
		}
		else
		{
			if ( structureRoot != null )
			{
				throw new Exception( "invalid state: multiple root level groups" );
			}
			this.structureRoot = this.curGroup;
			this.curGroup = null;
		}
		//System.out.println("openGroupStack.size:"+this.openGroupStack.size());
	} // DoGroupEnd

	// ----------------------------------------------------------------------
	protected  void DoParseEnd() throws Exception
	{
		if ( openGroupStack.size() > 0 )
		{
			throw new Exception( "invalid state: unclosed groups" );
		}
		//System.out.println("root size:"+structureRoot.getContents().size());
		//for(IRtfElement e:structureRoot.getContents())
		//{
		//	System.out.println("e:"+e);
		//}
	} // DoParseEnd

	// ----------------------------------------------------------------------
	// members
	private  Stack<RtfGroup> openGroupStack = new Stack<RtfGroup>();
	private RtfGroup curGroup;
	private RtfGroup structureRoot;

} // class RtfParserListenerStructureBuilder

