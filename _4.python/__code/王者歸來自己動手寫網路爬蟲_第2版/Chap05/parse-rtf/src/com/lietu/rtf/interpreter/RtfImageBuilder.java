package com.lietu.rtf.interpreter;

import com.lietu.rtf.IRtfGroup;
import com.lietu.rtf.IRtfTag;
import com.lietu.rtf.IRtfText;
import com.lietu.rtf.RtfElementVisitorOrder;
import com.lietu.rtf.RtfSpec;
import com.lietu.rtf.RtfVisualImageFormat;
import com.lietu.rtf.support.RtfElementVisitorBase;


	public final class RtfImageBuilder extends RtfElementVisitorBase
	{

		// ----------------------------------------------------------------------
		public RtfImageBuilder()
			
		{
			 super( RtfElementVisitorOrder.DepthFirst );
			Reset();
		} // RtfImageBuilder

		// ----------------------------------------------------------------------
		public void Reset()
		{
			this.format = RtfVisualImageFormat.Bmp;
			this.width = 0;
			this.height = 0;
			this.desiredWidth = 0;
			this.desiredHeight = 0;
			this.scaleWidthPercent = 100;
			this.scaleHeightPercent = 100;
			this.imageDataHex = null;
		} // Reset

		// ----------------------------------------------------------------------
		public RtfVisualImageFormat getFormat()
		{
			return this.format; 
		} // Format

		// ----------------------------------------------------------------------
		public int getWidth()
		{
			 return this.width; 
		} // Width

		// ----------------------------------------------------------------------
		public int getHeight()
		{
			 return this.height;
		} // Height

		// ----------------------------------------------------------------------
		public int getDesiredWidth()
		{
			return this.desiredWidth; 
		} // DesiredWidth

		// ----------------------------------------------------------------------
		public int getDesiredHeight()
		{
			 return this.desiredHeight;
		} // DesiredHeight

		// ----------------------------------------------------------------------
		public int getScaleWidthPercent()
		{
			return this.scaleWidthPercent;
		} // ScaleWidthPercent

		// ----------------------------------------------------------------------
		public int getScaleHeightPercent()
		{
			 return this.scaleHeightPercent;
		} // ScaleHeightPercent

		// ----------------------------------------------------------------------
		public String getImageDataHex()
		{
			 return this.imageDataHex;
		} // ImageDataHex

		// ----------------------------------------------------------------------
		protected  void DoVisitGroup( IRtfGroup group ) throws Exception
		{
			String groupDestination=group.getDestination() ;
			if(groupDestination.equals(RtfSpec.TagPicture)){
				Reset();
				VisitGroupChildren( group );
			}
			
		} // DoVisitGroup

		// ----------------------------------------------------------------------
		protected  void DoVisitTag( IRtfTag tag )
		{
			String tagName=tag.getName() ;
			if(tagName.equals(RtfSpec.TagPictureFormatWinDib)){
				;
			}else if(tagName.equals(RtfSpec.TagPictureFormatWinBmp)){
				this.format = RtfVisualImageFormat.Bmp;
			}else if(tagName.equals(RtfSpec.TagPictureFormatEmf)){
				this.format = RtfVisualImageFormat.Emf;
			}else if(tagName.equals(RtfSpec.TagPictureFormatJpg)){
				this.format = RtfVisualImageFormat.Jpg;
			}else if(tagName.equals(RtfSpec.TagPictureFormatPng)){
				this.format = RtfVisualImageFormat.Png;
			}else if(tagName.equals(RtfSpec.TagPictureFormatWmf)){
				this.format = RtfVisualImageFormat.Wmf;
			}else if(tagName.equals(RtfSpec.TagPictureWidth)){
				this.width = tag.getValueAsNumber();
				this.desiredWidth = width;
			}else if(tagName.equals(RtfSpec.TagPictureHeight)){
				this.height = tag.getValueAsNumber();
				this.desiredHeight = height;
			}else if(tagName.equals(RtfSpec.TagPictureWidthGoal)){
				this.desiredWidth = tag.getValueAsNumber();
				if ( this.width == 0 )
				{
					// hack to prevent WordPad documents which lack the \picw and \pich tags
					// from resulting in an exception due to undefined width/height
					this.width = this.desiredWidth;
				}
			}else if(tagName.equals(RtfSpec.TagPictureHeightGoal)){
				this.desiredHeight = tag.getValueAsNumber();
				if ( this.height == 0 )
				{
					// hack to prevent WordPad documents which lack the \picw and \pich tags
					// from resulting in an exception due to undefined width/height
					this.height = this.desiredHeight;
				}
			}else if(tagName.equals(RtfSpec.TagPictureWidthScale)){
				this.scaleWidthPercent = tag.getValueAsNumber();
			}else if(tagName.equals(RtfSpec.TagPictureHeightScale)){
				this.scaleHeightPercent = tag.getValueAsNumber();
			}
			
			
		} // DoVisitTag

		// ----------------------------------------------------------------------
		protected  void DoVisitText( IRtfText text )
		{
			this.imageDataHex = text.getText();
		} // DoVisitText

		// ----------------------------------------------------------------------
		// members
		private RtfVisualImageFormat format;
		private int width;
		private int height;
		private int desiredWidth;
		private int desiredHeight;
		private int scaleWidthPercent;
		private int scaleHeightPercent;
		private String imageDataHex;

	} // class RtfImageBuilder

