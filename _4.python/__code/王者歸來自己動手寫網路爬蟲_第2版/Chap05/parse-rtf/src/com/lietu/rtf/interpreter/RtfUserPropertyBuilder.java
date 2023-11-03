package com.lietu.rtf.interpreter;

import java.util.ArrayList;

import com.lietu.rtf.IRtfDocumentProperty;
import com.lietu.rtf.IRtfGroup;
import com.lietu.rtf.IRtfTag;
import com.lietu.rtf.RtfElementVisitorOrder;
import com.lietu.rtf.RtfSpec;
import com.lietu.rtf.model.RtfDocumentProperty;
import com.lietu.rtf.support.RtfElementVisitorBase;


public final class RtfUserPropertyBuilder extends RtfElementVisitorBase
{

	// ----------------------------------------------------------------------
	public RtfUserPropertyBuilder( ArrayList<IRtfDocumentProperty> collectedProperties ) throws Exception 
	{
		super( RtfElementVisitorOrder.NonRecursive );
		// we iterate over our children ourselves -> hence non-recursive
		if ( collectedProperties == null )
		{
			throw new Exception( "collectedProperties" );
		}
		this.collectedProperties = collectedProperties;
	} // RtfUserPropertyBuilder

	// ----------------------------------------------------------------------
	public IRtfDocumentProperty CreateProperty()
	{
		return new RtfDocumentProperty( this.propertyTypeCode, this.propertyName, this.staticValue, this.linkValue );
	} // CreateProperty

	// ----------------------------------------------------------------------
	public void Reset()
	{
		this.propertyTypeCode = 0;
		this.propertyName = null;
		this.staticValue = null;
		this.linkValue = null;
	} // Reset

	// ----------------------------------------------------------------------
	protected  void DoVisitGroup( IRtfGroup group ) throws Exception
	{
		String qroupDestination=group.getDestination();
		if(qroupDestination.equals(RtfSpec.TagUserProperties)){
			VisitGroupChildren( group );
		}else if(qroupDestination==null){
			Reset();
			VisitGroupChildren( group );
			this.collectedProperties.add( CreateProperty() );
		}else if(qroupDestination.equals(RtfSpec.TagUserPropertyName)){
			this.textBuilder.Reset();
			this.textBuilder.VisitGroup( group );
			this.propertyName = textBuilder.getCombinedText();
		}else if(qroupDestination.equals(RtfSpec.TagUserPropertyValue)){
			this.textBuilder.Reset();
			this.textBuilder.VisitGroup( group );
			this.staticValue = textBuilder.getCombinedText();
		}else if(qroupDestination.equals(RtfSpec.TagUserPropertyLink)){
			this.textBuilder.Reset();
			this.textBuilder.VisitGroup( group );
			this.linkValue = textBuilder.getCombinedText();
		}
		
		
	} // DoVisitGroup

	// ----------------------------------------------------------------------
	protected  void DoVisitTag( IRtfTag tag )
	{
		String tagName=tag.getName();
		if(tagName==RtfSpec.TagUserPropertyType){
			this.propertyTypeCode = tag.getValueAsNumber();
		}
		
	} // DoVisitTag

	// ----------------------------------------------------------------------
	// members
	private ArrayList<IRtfDocumentProperty> collectedProperties;
	private  RtfTextBuilder textBuilder = new RtfTextBuilder();
	private int propertyTypeCode;
	private String propertyName;
	private String staticValue;
	private String linkValue;

} // class RtfUserPropertyBuilder

