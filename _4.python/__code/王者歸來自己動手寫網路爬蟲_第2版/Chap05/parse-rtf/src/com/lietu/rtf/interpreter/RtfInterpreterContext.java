package com.lietu.rtf.interpreter;

import java.util.ArrayList;
import java.util.Stack;

import java.util.Hashtable;

import com.lietu.rtf.IRtfColor;
import com.lietu.rtf.IRtfDocumentInfo;
import com.lietu.rtf.IRtfDocumentProperty;
import com.lietu.rtf.IRtfFont;
import com.lietu.rtf.IRtfInterpreterContext;
import com.lietu.rtf.IRtfTextFormat;
import com.lietu.rtf.RtfInterpreterState;
import com.lietu.rtf.RtfSpec;
import com.lietu.rtf.model.RtfDocumentInfo;
import com.lietu.rtf.model.RtfTextFormat;


public final class RtfInterpreterContext implements IRtfInterpreterContext
{
	// ----------------------------------------------------------------------
	public RtfInterpreterContext()
	{
	} // RtfInterpreterContext

	// ----------------------------------------------------------------------
	public RtfInterpreterState getState()
	{
		 return this.state; 
		
	} // State

	public void setState(RtfInterpreterState state)
	{
		
		 this.state = state; 
	} 
	// ----------------------------------------------------------------------
	public int getRtfVersion()
	{
		 return this.rtfVersion; 
		
	} // RtfVersion

	public void setRtfVersion(int rtfVersion)
	{
		this.rtfVersion = rtfVersion;
	}
	// ----------------------------------------------------------------------
	public String getDefaultFontId()
	{
		 return this.defaultFontId;
	
	} // DefaultFontIndex

	public void setDefaultFontId(String defaultFontId)
	{
		this.defaultFontId=defaultFontId;
	}
	
	// ----------------------------------------------------------------------
	public IRtfFont getDefaultFont() throws Exception
	{
			IRtfFont defaultFont = this.fontTable.get( this.defaultFontId );
			if ( defaultFont != null )
			{
				return defaultFont;
			}
			throw new Exception( "invalid default font id '" + this.defaultFontId +
				"', only the following fonts are available (yet): " + this.fontTable );
		
	} // DefaultFont

	@Override
	public Hashtable<String,IRtfFont> getFontTable()
	{
		return this.fontTable; 
	} // FontTable

	// ----------------------------------------------------------------------
	public Hashtable<String,IRtfFont> getWritableFontTable()
	{
		return this.fontTable; 
	} // WritableFontTable

	@Override
	public ArrayList<IRtfColor> getColorTable()
	{
		 return this.colorTable; 
	} // ColorTable

	// ----------------------------------------------------------------------
	public ArrayList<IRtfColor> getWritableColorTable()
	{
		 return this.colorTable; 
	} // WritableColorTable

	// ----------------------------------------------------------------------
	public String getGenerator()
	{
		 return this.generator; 
		
	} // Generator

	public void setGenerator(String generator)
	{
		 this.generator=generator; 
		
	}
	// ----------------------------------------------------------------------
	public ArrayList<IRtfTextFormat> getUniqueTextFormats()
	{
		 return this.uniqueTextFormats; 
	} // UniqueTextFormats

	// ----------------------------------------------------------------------
	public IRtfTextFormat getCurrentTextFormat()
	{
		return this.currentTextFormat; 
	} // CurrentTextFormat

	// ----------------------------------------------------------------------
	public IRtfTextFormat getGetSafeCurrentTextFormat() throws Exception
	{
		return this.currentTextFormat != null ? this.currentTextFormat : getWritableCurrentTextFormat();
	} // GetSafeCurrentTextFormat

	// ----------------------------------------------------------------------
	public RtfTextFormat getWritableCurrentTextFormat() throws Exception
	{
		
			if ( this.currentTextFormat == null )
			{
				// set via property to ensure it will get added to the unique map
				setWritableCurrentTextFormat(new RtfTextFormat( getDefaultFont(), RtfSpec.DefaultFontSize )); 
			}
			return this.currentTextFormat;			
		
	} // WritableCurrentTextFormat

	public void setWritableCurrentTextFormat(RtfTextFormat value) throws Exception
	{
		
			if ( value == null )
			{
				throw new Exception( "value" );
			}
			int existingEquivalentPos = this.uniqueTextFormats.indexOf( value );
			if ( existingEquivalentPos >= 0 )
			{
				// we already know an equivalent format -> reference that one for future use
				this.currentTextFormat = (RtfTextFormat)uniqueTextFormats.get(existingEquivalentPos );
			}
			else
			{
				// this is a yet unknown format -> add it to the known formats and use it
				this.uniqueTextFormats.add( value );
				this.currentTextFormat = value;
			}
	}
	// ----------------------------------------------------------------------
	public IRtfDocumentInfo getDocumentInfo()
	{
		return this.documentInfo;
	} // DocumentInfo

	// ----------------------------------------------------------------------
	public RtfDocumentInfo getWritableDocumentInfo()
	{
		 return this.documentInfo; 
	} // WritableDocumentInfo

	// ----------------------------------------------------------------------
	public ArrayList<IRtfDocumentProperty> getUserProperties()
	{
		 return this.userProperties; 
	} // UserProperties

	// ----------------------------------------------------------------------
	public ArrayList<IRtfDocumentProperty> getWritableUserProperties()
	{
		 return this.userProperties; 
	} // WritableUserProperties

	// ----------------------------------------------------------------------
	public void PushCurrentTextFormat() throws Exception
	{
		this.textFormatStack.push( getWritableCurrentTextFormat() );
	} // PushCurrentTextFormat

	// ----------------------------------------------------------------------
	public void PopCurrentTextFormat() throws Exception
	{
		if ( this.textFormatStack.size() == 0 )
		{
			throw new Exception( "illegal state: cannot pop text format from empty stack" );
		}
		currentTextFormat = (RtfTextFormat)this.textFormatStack.pop();
	} // PopCurrentTextFormat

	// ----------------------------------------------------------------------
	public void Reset()
	{
		this.state = RtfInterpreterState.Init;
		this.rtfVersion = RtfSpec.RtfVersion1;
		this.defaultFontId = "f0";
		this.fontTable.clear();
		this.colorTable.clear();
		this.generator = null;
		this.uniqueTextFormats.clear();
		this.textFormatStack.clear();
		this.currentTextFormat = null;
		this.documentInfo.Reset();
		this.userProperties.clear();
	} // Reset

	// ----------------------------------------------------------------------
	// members
	private RtfInterpreterState state;
	private int rtfVersion;
	private String defaultFontId;
	private  Hashtable<String,IRtfFont> fontTable = new Hashtable<String,IRtfFont>();
	private  ArrayList<IRtfColor> colorTable = new ArrayList<IRtfColor>();
	private String generator;
	private  ArrayList<IRtfTextFormat> uniqueTextFormats = new ArrayList<IRtfTextFormat>();
	private  Stack<IRtfTextFormat> textFormatStack = new Stack<IRtfTextFormat>();
	private RtfTextFormat currentTextFormat;
	private  RtfDocumentInfo documentInfo = new RtfDocumentInfo();
	private  ArrayList<IRtfDocumentProperty> userProperties = new ArrayList<IRtfDocumentProperty>();
} // class RtfInterpreterContext
