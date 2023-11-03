package com.lietu.rtf.model;

import com.lietu.rtf.IRtfVisualImage;
import com.lietu.rtf.IRtfVisualVisitor;
import com.lietu.rtf.RtfTextAlignment;
import com.lietu.rtf.RtfVisualImageFormat;
import com.lietu.rtf.RtfVisualKind;
import com.lietu.rtf.sys.HashTool;


	public final class RtfVisualImage extends RtfVisual implements IRtfVisualImage
	{

		// ----------------------------------------------------------------------
		public RtfVisualImage(
			RtfVisualImageFormat format,
			RtfTextAlignment alignment,
			int width,
			int height,
			int desiredWidth,
			int desiredHeight,
			int scaleWidthPercent,
			int scaleHeightPercent,
			String imageDataHex
		) throws Exception 
			
		{
			super( RtfVisualKind.Image );
			if ( width <= 0 )
			{
				throw new Exception( "width must be > 0 but is " + width+ " width" );
			}
			if ( height <= 0 )
			{
				throw new Exception( "height must be > 0 but is " + height+ " height" );
			}
			if ( desiredWidth <= 0 )
			{
				throw new Exception( "desiredWidth must be > 0 but is " + desiredWidth+ " desiredWidth" );
			}
			if ( desiredHeight <= 0 )
			{
				throw new Exception( "desiredHeight must be > 0 but is " + desiredHeight+ " desiredHeight" );
			}
			if ( scaleWidthPercent <= 0 )
			{
				throw new Exception( "scaleWidthPercent must be > 0 but is " + scaleWidthPercent+ " scaleWidthPercent" );
			}
			if ( scaleHeightPercent <= 0 )
			{
				throw new Exception( "scaleHeightPercent must be > 0 but is " + scaleHeightPercent+" scaleHeightPercent" );
			}
			if ( imageDataHex == null )
			{
				throw new Exception( "imageDataHex" );
			}
			this.format = format;
			this.alignment = alignment;
			this.width = width;
			this.height = height;
			this.desiredWidth = desiredWidth;
			this.desiredHeight = desiredHeight;
			this.scaleWidthPercent = scaleWidthPercent;
			this.scaleHeightPercent = scaleHeightPercent;
			this.imageDataHex = imageDataHex;
		} // RtfVisualImage

		// ----------------------------------------------------------------------
		protected  void DoVisit( IRtfVisualVisitor visitor )
		{
			visitor.VisitImage( this );
		} // DoVisit

		// ----------------------------------------------------------------------
		public RtfVisualImageFormat getFormat()
		{
			 return this.format;
		} // Format

		// ----------------------------------------------------------------------
		public RtfTextAlignment getAlignment()
		{
			 return this.alignment; 
		} // Alignment

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
		public byte[] getImageDataBinary() throws Exception
		{
	
			
				if ( this.imageDataBinary == null )
				{
					this.imageDataBinary = ToBinary( this.imageDataHex );
				}
				return imageDataBinary;
			
		} // ImageDataBinary

		// ----------------------------------------------------------------------
		public java.awt.Image getImageForDrawing() throws Exception
		{
			
			RtfVisualImageFormat fm=format;
			if(fm==RtfVisualImageFormat.Bmp){
				;
			}if(fm==RtfVisualImageFormat.Jpg){
				;
			}if(fm==RtfVisualImageFormat.Png){
				;
			}if(fm==RtfVisualImageFormat.Emf){
				;
			}if(fm==RtfVisualImageFormat.Wmf){
				//byte[] data = getImageDataBinary();
				//return System.Drawing.Image.FromStream( new MemoryStream( data, 0, data.length ) );
			}
				
				return null;
			
		} // ImageForDrawing

		// ----------------------------------------------------------------------
		public static byte[] ToBinary( String imageDataHex ) throws Exception
		{
			if ( imageDataHex == null )
			{
				throw new Exception ("imageDataHex" );
			}

			int hexDigits = imageDataHex.length();
			int dataSize = hexDigits / 2;
			byte[] imageDataBinary = new byte[ dataSize ];

			//StringBuilder hex = new StringBuilder( 2 );

			/*int dataPos = 0;
			for ( int i = 0; i < hexDigits; i++ )
			{
				hex.append( imageDataHex[ i ] );
				if ( hex.Length == 2 )
				{
					imageDataBinary[ dataPos ] = byte.Parse( hex.ToString(), NumberStyles.HexNumber );
					dataPos++;
					hex.Remove( 0, 2 );
				}
			}*/

			return imageDataBinary;
		} // ToBinary

		// ----------------------------------------------------------------------
		protected  boolean isEqual( Object obj )
		{
			RtfVisualImage compare = (RtfVisualImage)obj  ; // guaranteed to be non-null
			return super.isEqual( compare ) &&
				this.format == compare.format &&
				this.alignment == compare.alignment &&
				this.width == compare.width &&
				this.height == compare.height &&
				this.desiredWidth == compare.desiredWidth &&
				this.desiredHeight == compare.desiredHeight &&
				this.scaleWidthPercent == compare.scaleWidthPercent &&
				this.scaleHeightPercent == compare.scaleHeightPercent &&
				this.imageDataHex.equals( compare.imageDataHex );
			//imageDataBinary.Equals( compare.imageDataBinary ); // cached info only
		} // IsEqual

		// ----------------------------------------------------------------------
		public  int hashCode()
		{
			int hash = super.hashCode();
			hash = HashTool.AddHashCode( hash, this.format );
			hash = HashTool.AddHashCode( hash, this.alignment );
			hash = HashTool.AddHashCode( hash, this.width );
			hash = HashTool.AddHashCode( hash, this.height );
			hash = HashTool.AddHashCode( hash, this.desiredWidth );
			hash = HashTool.AddHashCode( hash, this.desiredHeight );
			hash = HashTool.AddHashCode( hash, this.scaleWidthPercent );
			hash = HashTool.AddHashCode( hash, this.scaleHeightPercent );
			hash = HashTool.AddHashCode( hash, this.imageDataHex );
			//hash = HashTool.AddHashCode( hash, this.imageDataBinary ); // cached info only
			return hash;
		} // ComputeHashCode

		// ----------------------------------------------------------------------
		public  String toString()
		{
			return "[" + this.format + ": " + this.alignment + ", " +
				this.width + " x " + this.height + " " +
				"(" + this.desiredWidth + " x " + this.desiredHeight + ") " +
				"{" + this.scaleWidthPercent + "% x " + this.scaleHeightPercent + "%} " +
				":" + (this.imageDataHex.length() / 2) + " bytes]";
		} // ToString

		// ----------------------------------------------------------------------
		// members
		private  RtfVisualImageFormat format;
		private  RtfTextAlignment alignment;
		private  int width;
		private  int height;
		private  int desiredWidth;
		private  int desiredHeight;
		private  int scaleWidthPercent;
		private  int scaleHeightPercent;
		private  String imageDataHex;
		private byte[] imageDataBinary; // cached info only
	

	} // class RtfVisualImage
