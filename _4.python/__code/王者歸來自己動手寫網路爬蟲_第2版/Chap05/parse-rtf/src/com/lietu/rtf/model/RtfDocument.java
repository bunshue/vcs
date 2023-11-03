package com.lietu.rtf.model;

import java.util.ArrayList;
import java.util.Hashtable;

import com.lietu.rtf.IRtfColor;
import com.lietu.rtf.IRtfDocument;
import com.lietu.rtf.IRtfDocumentInfo;
import com.lietu.rtf.IRtfDocumentProperty;
import com.lietu.rtf.IRtfFont;
import com.lietu.rtf.IRtfInterpreterContext;
import com.lietu.rtf.IRtfTextFormat;
import com.lietu.rtf.IRtfVisual;
import com.lietu.rtf.RtfSpec;


public  class RtfDocument implements IRtfDocument
{

	// ----------------------------------------------------------------------
	public RtfDocument( IRtfInterpreterContext context, ArrayList<IRtfVisual> visualContent ) throws Exception 
	{
		this( context.getRtfVersion(),
				context.getDefaultFont(),
				context.getFontTable(),
				context.getColorTable(),
				context.getGenerator(),
				context.getUniqueTextFormats(),
				context.getDocumentInfo(),
				context.getUserProperties(),
				visualContent
			);
	} // RtfDocument

	// ----------------------------------------------------------------------
	public RtfDocument(
		int rtfVersion,
		IRtfFont defaultFont,
		Hashtable<String,IRtfFont> fontTable,
		ArrayList<IRtfColor> colorTable,
		String generator,
		ArrayList<IRtfTextFormat> uniqueTextFormats,
		IRtfDocumentInfo documentInfo,
		ArrayList<IRtfDocumentProperty> userProperties,
		ArrayList<IRtfVisual> visualContent
	) throws Exception
	{
		if ( rtfVersion != RtfSpec.RtfVersion1 )
		{
			throw new Exception( "unsupported RTF version: " + rtfVersion );
		}
		if ( defaultFont == null )
		{
			throw new Exception( "defaultFont" );
		}
		if ( fontTable == null )
		{
			throw new Exception( "fontTable" );
		}
		if ( colorTable == null )
		{
			throw new Exception( "colorTable" );
		}
		if ( uniqueTextFormats == null )
		{
			throw new Exception( "uniqueTextFormats" );
		}
		if ( documentInfo == null )
		{
			throw new Exception( "documentInfo" );
		}
		if ( userProperties == null )
		{
			throw new Exception( "userProperties" );
		}
		if ( visualContent == null )
		{
			throw new Exception( "visualContent" );
		}
		this.rtfVersion = rtfVersion;
		this.defaultFont = defaultFont;
		this.defaultTextFormat = new RtfTextFormat( defaultFont, RtfSpec.DefaultFontSize );
		this.fontTable = fontTable;
		this.colorTable = colorTable;
		this.generator = generator;
		this.uniqueTextFormats = uniqueTextFormats;
		this.documentInfo = documentInfo;
		this.userProperties = userProperties;
		this.visualContent = visualContent;
	} // RtfDocument

	// ----------------------------------------------------------------------
	public int getRtfVersion()
	{
		 return this.rtfVersion; 
	} // RtfVersion

	// ----------------------------------------------------------------------
	public IRtfFont getDefaultFont()
	{
		 return this.defaultFont; 
	} // DefaultFont

	// ----------------------------------------------------------------------
	public IRtfTextFormat getDefaultTextFormat()
	{
		 return this.defaultTextFormat; 
	} // DefaultTextFormat

	// ----------------------------------------------------------------------
	public Hashtable<String,IRtfFont> getFontTable()
	{
		 return this.fontTable; 
	} // FontTable

	// ----------------------------------------------------------------------
	public ArrayList<IRtfColor> getColorTable()
	{
		return this.colorTable; 
	} // ColorTable

	// ----------------------------------------------------------------------
	public String getGenerator()
	{
		 return this.generator; 
	} // Generator

	@Override
	public ArrayList<IRtfTextFormat> getUniqueTextFormats()
	{
		return this.uniqueTextFormats; 
	} // UniqueTextFormats

	// ----------------------------------------------------------------------
	public IRtfDocumentInfo getDocumentInfo()
	{
		 return this.documentInfo; 
	} // DocumentInfo

	// ----------------------------------------------------------------------
	public ArrayList<IRtfDocumentProperty> getUserProperties()
	{
		return this.userProperties;
	} // UserProperties

	// ----------------------------------------------------------------------
	public ArrayList<IRtfVisual> getVisualContent()
	{
		return this.visualContent;
	} // VisualContent

	// ----------------------------------------------------------------------
	public  String toString()
	{
		return "RTFv" + this.rtfVersion;
	} // ToString

	// ----------------------------------------------------------------------
	// members
	private  int rtfVersion;
	private  IRtfFont defaultFont;
	private  IRtfTextFormat defaultTextFormat;
	private  Hashtable<String,IRtfFont> fontTable;
	private  ArrayList<IRtfColor> colorTable;
	private  String generator;
	private  ArrayList<IRtfTextFormat> uniqueTextFormats;
	private  IRtfDocumentInfo documentInfo;
	private  ArrayList<IRtfDocumentProperty> userProperties;
	private  ArrayList<IRtfVisual> visualContent;
} // class RtfDocument

