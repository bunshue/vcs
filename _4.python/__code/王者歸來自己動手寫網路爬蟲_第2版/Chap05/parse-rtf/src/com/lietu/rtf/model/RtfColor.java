package com.lietu.rtf.model;

import java.awt.Color;

import com.lietu.rtf.IRtfColor;
import com.lietu.rtf.sys.HashTool;



	// ------------------------------------------------------------------------
	public final class RtfColor implements IRtfColor
	{

		// ----------------------------------------------------------------------
		public static final IRtfColor Black = new RtfColor( 0, 0, 0 );
		public static final IRtfColor White = new RtfColor( 255, 255, 255 );

		// ----------------------------------------------------------------------
		public RtfColor( int red, int green, int blue )
		{			
			try {
				if ( red < 0 || red > 255 )
				{
					throw new Exception(
						"invalid color component, must be in the range [0..255], but is " + red );
				}
				if ( green < 0 || green > 255 )
				{
					throw new Exception(
						"invalid color component, must be in the range [0..255], but is " + green);
				}
				if ( blue < 0 || blue > 255 )
				{
					throw new Exception(
						"invalid color component, must be in the range [0..255], but is " + blue );
				}
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			this.red = red;
			this.green = green;
			this.blue = blue;
			this.drawingColor = Color.getHSBColor( red, green, blue );
		} // RtfColor

		// ----------------------------------------------------------------------
		public int getRed()
		{
			 return this.red; 
		} // Red

		// ----------------------------------------------------------------------
		public int getGreen()
		{
			return this.green;
		} // Green

		// ----------------------------------------------------------------------
		public int getBlue()
		{
			return this.blue;
		} // Blue

		// ----------------------------------------------------------------------
		public Color getAsDrawingColor()
		{
			 return this.drawingColor;
		} // AsDrawingColor

		// ----------------------------------------------------------------------
		public  boolean equals( Object obj )
		{
			if ( obj == this )
			{
				return true;
			}
			else if ( obj == null)
			{
				return false;
			}
			return IsEqual( obj );
		} // Equals

		// ----------------------------------------------------------------------
		public int GetHashCode()
		{
			return HashTool.AddHashCode( this.hashCode(), ComputeHashCode() );
		} // GetHashCode

		// ----------------------------------------------------------------------
		public String toString()
		{
			return "Color{" + this.red + "," + this.green + "," + this.blue + "}";
		} // ToString

		// ----------------------------------------------------------------------
		
		private boolean IsEqual( Object obj )
		{
			RtfColor compare =(RtfColor)obj; // guaranteed to be non-null
			return this.red == compare.red &&
				this.green == compare.green &&
				this.blue == compare.blue;
		} // I

		// ----------------------------------------------------------------------
		private int ComputeHashCode()
		{
			int hash = this.red;
			hash = HashTool.AddHashCode( hash, this.green );
			hash = HashTool.AddHashCode( hash, this.blue );
			return hash;
		} // ComputeHashCode

		// ----------------------------------------------------------------------
		// members
		private final int red;
		private final int green;
		private final int blue;
		private final Color drawingColor;

	} // class RtfColor

