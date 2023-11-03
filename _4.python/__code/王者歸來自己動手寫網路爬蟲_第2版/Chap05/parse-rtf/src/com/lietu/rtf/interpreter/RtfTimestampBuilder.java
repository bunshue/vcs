package com.lietu.rtf.interpreter;

import java.util.Date;

import com.lietu.rtf.IRtfTag;
import com.lietu.rtf.RtfElementVisitorOrder;
import com.lietu.rtf.RtfSpec;
import com.lietu.rtf.support.RtfElementVisitorBase;

// ------------------------------------------------------------------------
public class RtfTimestampBuilder extends RtfElementVisitorBase
{

	// ----------------------------------------------------------------------
	public RtfTimestampBuilder()
	{
		super( RtfElementVisitorOrder.BreadthFirst );
		Reset();
	} // RtfTimestampBuilder

	// ----------------------------------------------------------------------
	public void Reset()
	{
		this.year = 1970;
		this.month = 1;
		this.day = 1;
		this.hour = 0;
		this.minutes = 0;
		this.seconds = 0;
	} // Reset

	// ----------------------------------------------------------------------
	public Date CreateTimestamp()
	{
		return new Date( this.year, this.month, this.day, this.hour, this.minutes, this.seconds );
	} // CreateTimestamp

	// ----------------------------------------------------------------------
	protected void DoVisitTag( IRtfTag tag )
	{
		if ( tag.getName().equals (RtfSpec.TagInfoYear))
		{
			this.year = tag.getValueAsNumber();
		}	
		else if ( tag.getName().equals (RtfSpec.TagInfoMonth))
		{
			this.month = tag.getValueAsNumber();
		}		
		if ( tag.getName().equals (RtfSpec.TagInfoDay))
		{
			this.day = tag.getValueAsNumber();
		}		
		if ( tag.getName().equals (RtfSpec.TagInfoHour))
		{
			this.hour = tag.getValueAsNumber();
		}	
		if ( tag.getName().equals (RtfSpec.TagInfoMinute))
		{
			this.minutes = tag.getValueAsNumber();
		}		
	    if ( tag.getName().equals (RtfSpec.TagInfoSecond))
			{
			this.seconds = tag.getValueAsNumber();
			}		
		}
	 // DoVisitTag

	// ----------------------------------------------------------------------
	// members
	private int year;
	private int month;
	private int day;
	private int hour;
	private int minutes;
	private int seconds;

} // class RtfTimestampBuilder
