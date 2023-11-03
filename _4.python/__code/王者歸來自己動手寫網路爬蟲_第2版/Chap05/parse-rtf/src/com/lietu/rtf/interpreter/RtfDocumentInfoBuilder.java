package com.lietu.rtf.interpreter;

import java.util.Date;

import com.lietu.rtf.IRtfGroup;
import com.lietu.rtf.IRtfTag;
import com.lietu.rtf.RtfElementVisitorOrder;
import com.lietu.rtf.RtfSpec;
import com.lietu.rtf.model.RtfDocumentInfo;
import com.lietu.rtf.support.RtfElementVisitorBase;



	public class RtfDocumentInfoBuilder extends RtfElementVisitorBase
	{

		// ----------------------------------------------------------------------
		public RtfDocumentInfoBuilder( RtfDocumentInfo info ) throws Exception 
		{
			super( RtfElementVisitorOrder.NonRecursive );
			// we iterate over our children ourselves -> hence non-recursive
			if ( info == null )
			{
				throw new Exception( "info" );
			}
			this.info = info;
		} // RtfDocumentInfoBuilder

		// ----------------------------------------------------------------------
		public void Reset()
		{
			this.info.Reset();
		} // Reset

		// ----------------------------------------------------------------------
		protected void DoVisitGroup( IRtfGroup group ) throws Exception
		{
			if ( group.getDestination().equals(RtfSpec.TagInfo) )
			{
					VisitGroupChildren( group );
			}
			else if( group.getDestination().equals( RtfSpec.TagInfoTitle))
			{
					this.info.setTitle(ExtractGroupText( group ));
			}
			else if( group.getDestination().equals( RtfSpec.TagInfoSubject))
			{
					this.info.setSubject ( ExtractGroupText( group ));
			}
			else if( group.getDestination().equals( RtfSpec.TagInfoAuthor))
			{
				    this.info.setAuthor ( ExtractGroupText( group ));
			}	
			else if( group.getDestination().equals( RtfSpec.TagInfoManager))
			{
				this.info.setManager ( ExtractGroupText( group ));
			}
			
			else if( group.getDestination().equals( RtfSpec.TagInfoCompany))
			{
				this.info.setCompany (ExtractGroupText( group ));
			}	
			else if( group.getDestination().equals( RtfSpec.TagInfoOperator))
			{
				this.info.setOperator ( ExtractGroupText( group ));
			}		
			else if( group.getDestination().equals( RtfSpec.TagInfoCategory))
			{
				this.info.setCategory ( ExtractGroupText( group ));
			}		
			else if( group.getDestination().equals( RtfSpec.TagInfoKeywords))
			{
				this.info.setKeywords ( ExtractGroupText( group ));
			}	
			else if( group.getDestination().equals( RtfSpec.TagInfoComment))
			{
				this.info.setComment (ExtractGroupText( group ));
			}		
			else if( group.getDestination().equals( RtfSpec.TagInfoDocumentComment))
			{
				this.info.setDocumentComment ( ExtractGroupText( group ));
			}	
			else if( group.getDestination().equals( RtfSpec.TagInfoHyperLinkBase))
			{
				this.info.setHyperLinkbase (ExtractGroupText( group ));
			}	
			else if( group.getDestination().equals( RtfSpec.TagInfoCreationTime))
			{
				this.info.setCreationTime (ExtractTimestamp( group ));
			}	
			else if( group.getDestination().equals( RtfSpec.TagInfoRevisionTime))
			{
				this.info.setRevisionTime(ExtractTimestamp( group));
			}	
			else if( group.getDestination().equals( RtfSpec.TagInfoPrintTime))
			{
				this.info.setPrintTime(ExtractTimestamp( group ));
			}	
			else if( group.getDestination().equals( RtfSpec.TagInfoBackupTime))
			{
				this.info.setBackupTime(ExtractTimestamp( group ));
			}	
			}
		// DoVisitGroup

		// ----------------------------------------------------------------------
		protected  void DoVisitTag( IRtfTag tag )
		{
			String tagName=tag.getName();
			if(tagName.equals(RtfSpec.TagInfoVersion)){
				this.info.setVersion(tag.getValueAsNumber());
			}else if(tagName.equals(RtfSpec.TagInfoRevision)){
				this.info.setRevision(tag.getValueAsNumber());
			}else if(tagName.equals(RtfSpec.TagInfoNumberOfPages)){
				this.info.setNumberOfPages(tag.getValueAsNumber());
			}else if(tagName.equals(RtfSpec.TagInfoNumberOfWords)){
				this.info.setNumberOfWords(tag.getValueAsNumber());	
			}else if(tagName.equals(RtfSpec.TagInfoNumberOfChars)){
				this.info.setNumberOfCharacters(tag.getValueAsNumber());
			}else if(tagName.equals(RtfSpec.TagInfoId)){
				this.info.setId(tag.getValueAsNumber());
			}else if(tagName.equals(RtfSpec.TagInfoEditingTimeMinutes)){
				this.info.setEditingTimeInMinutes(tag.getValueAsNumber());
			}
			
		} // DoVisitTag

		// ----------------------------------------------------------------------
		private String ExtractGroupText( IRtfGroup group ) throws Exception
		{
			this.textBuilder.Reset();
			this.textBuilder.VisitGroup( group );
			return this.textBuilder.getCombinedText();
		} // ExtractGroupText

		// ----------------------------------------------------------------------
		private Date ExtractTimestamp( IRtfGroup group ) throws Exception
		{
			this.timestampBuilder.Reset();
			this.timestampBuilder.VisitGroup( group );
			return this.timestampBuilder.CreateTimestamp();
		} // ExtractTimestamp

		// ----------------------------------------------------------------------
		// members
		private final RtfDocumentInfo info;
		private final RtfTextBuilder textBuilder = new RtfTextBuilder();
		private final RtfTimestampBuilder timestampBuilder = new RtfTimestampBuilder();

	} // class RtfDocumentInfoBuilder
