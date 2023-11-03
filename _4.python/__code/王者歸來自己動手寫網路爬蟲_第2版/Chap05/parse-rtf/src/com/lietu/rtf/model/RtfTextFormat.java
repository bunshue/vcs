package com.lietu.rtf.model;

import com.lietu.rtf.IRtfColor;
import com.lietu.rtf.IRtfFont;
import com.lietu.rtf.IRtfTextFormat;
import com.lietu.rtf.RtfSpec;
import com.lietu.rtf.RtfTextAlignment;
import com.lietu.rtf.sys.HashTool;


	public  class RtfTextFormat implements IRtfTextFormat
	{

		// ----------------------------------------------------------------------
		public RtfTextFormat( IRtfFont font, int fontSize ) throws Exception
		{
			if ( font == null )
			{
				throw new Exception( "font" );
			}
			if ( fontSize <= 0 || fontSize > 0xFFFF )
			{
				throw new Exception(
					"invalid font size, must be in the range [1..0xFFFF], but is " + fontSize);
			}
			this.font = font;
			this.fontSize = fontSize;
		} // RtfTextFormat

		// ----------------------------------------------------------------------
		public RtfTextFormat( IRtfTextFormat copy ) throws Exception
		{
			if ( copy == null )
			{
				throw new Exception( "copy" );
			}
			this.font = copy.getFont(); // enough because immutable
			this.fontSize = copy.getFontSize();
			this.superScript = copy.getSuperScript();
			this.bold = copy.getIsBold();
			this.italic = copy.getIsItalic();
			this.underline = copy.getIsUnderline();
			this.strikeThrough = copy.getIsStrikeThrough();
			this.backgroundColor = copy.getBackgroundColor(); // enough because immutable
			this.foregroundColor = copy.getBackgroundColor(); // enough because immutable
			this.alignment = copy.getAlignment();
		} // RtfTextFormat

		// ----------------------------------------------------------------------
		public RtfTextFormat( RtfTextFormat copy ) throws Exception
		{
			if ( copy == null )
			{
				throw new Exception( "copy" );
			}
			this.font = copy.font; // enough because immutable
			this.fontSize = copy.fontSize;
			this.superScript = copy.superScript;
			this.bold = copy.bold;
			this.italic = copy.italic;
			this.underline = copy.underline;
			this.strikeThrough = copy.strikeThrough;
			this.backgroundColor = copy.backgroundColor; // enough because immutable
			this.foregroundColor = copy.foregroundColor; // enough because immutable
			this.alignment = copy.alignment;
		} // RtfTextFormat

		// ----------------------------------------------------------------------
		public String getFontDescriptionDebug()
		{
				StringBuilder buf = new StringBuilder( this.font.getName() );
				buf.append( ", " );
				buf.append( this.fontSize );
				buf.append( this.superScript >= 0 ? "+" : "" );
				buf.append( this.superScript );
				buf.append( ", " );
				if ( this.bold || this.italic || this.underline || this.strikeThrough )
				{
					boolean combined = false;
					if ( this.bold )
					{
						buf.append( "bold" );
						combined = true;
					}
					if ( this.italic )
					{
						buf.append( combined ? "+italic" : "italic" );
						combined = true;
					}
					if ( this.underline )
					{
						buf.append( combined ? "+underline" : "underline" );
						combined = true;
					}
					if ( this.strikeThrough )
					{
						buf.append( combined ? "+strikethrough" : "strikethrough" );
					}
				}
				else
				{
					buf.append( "plain" );
				}
				return buf.toString();
		
		} // FontDescriptionDebug

		// ----------------------------------------------------------------------
		public IRtfFont getFont()
		{
			 return this.font; 
		} // Font

		// ----------------------------------------------------------------------
		public RtfTextFormat DeriveWithFont( IRtfFont font ) throws Exception
		{
			if ( font == null )
			{
				throw new Exception( "font" );
			}
			if ( this.font.equals( font ) )
			{
				return this;
			}
			else
			{
				RtfTextFormat copy = new RtfTextFormat( this );
				copy.font = font;
				return copy;
			}
		} // DeriveWithFont

		// ----------------------------------------------------------------------
		public int getFontSize()
		{
			return this.fontSize; 
		} // FontSize

		// ----------------------------------------------------------------------
		public RtfTextFormat DeriveWithFontSize( int fontSize ) throws Exception
		{
			if ( fontSize <= 0 || fontSize > 0xFFFF )
			{
				throw new Exception(
					"invalid font size, must be in the range [1..0xFFFF], but is " + fontSize);
			}
			if ( this.fontSize == fontSize )
			{
				return this;
			}
			else
			{
				RtfTextFormat copy = new RtfTextFormat( this );
				copy.fontSize = fontSize;
				return copy;
			}
		} // DeriveWithFontSize

		// ----------------------------------------------------------------------
		public int getSuperScript()
		{
			return this.superScript; 
		} // SuperScript

		// ----------------------------------------------------------------------
		public RtfTextFormat DeriveWithSuperScript( int deviation ) throws Exception
		{
			if ( this.superScript == deviation )
			{
				return this;
			}
			else
			{
				RtfTextFormat copy = new RtfTextFormat( this );
				copy.superScript = deviation;
				return copy;
			}
		} // DeriveWithSuperScript

		// ----------------------------------------------------------------------
		public boolean getIsNormal()
		{
			
				return
					!this.bold && !this.italic && !this.underline && !this.strikeThrough &&
					this.fontSize == RtfSpec.DefaultFontSize &&
					this.superScript == 0 &&
					RtfColor.Black.equals( this.foregroundColor ) &&
					RtfColor.White.equals( this.backgroundColor );
			
		} // IsNormal

		// ----------------------------------------------------------------------
		public RtfTextFormat DeriveNormal() throws Exception
		{
			if ( getIsNormal() )
			{
				return this;
			}
			else
			{
				RtfTextFormat copy = new RtfTextFormat( this.font, RtfSpec.DefaultFontSize );
				copy.alignment = this.alignment; // this is a paragraph property, keep it
				return copy;
			}
		} // DeriveNormal

		// ----------------------------------------------------------------------
		public boolean getIsBold()
		{
			 return this.bold;
		} // IsBold

		// ----------------------------------------------------------------------
		public RtfTextFormat DeriveWithBold( boolean bold ) throws Exception
		{
			if ( this.bold == bold )
			{
				return this;
			}
			else
			{
				RtfTextFormat copy = new RtfTextFormat( this );
				copy.bold = bold;
				return copy;
			}
		} // DeriveWithBold

		// ----------------------------------------------------------------------
		public boolean getIsItalic()
		{
			 return this.italic; 
		} // IsItalic

		// ----------------------------------------------------------------------
		public RtfTextFormat DeriveWithItalic( boolean italic ) throws Exception
		{
			if ( this.italic == italic )
			{
				return this;
			}
			else
			{
				RtfTextFormat copy = new RtfTextFormat( this );
				copy.italic = italic;
				return copy;
			}
		} // DeriveWithItalic

		// ----------------------------------------------------------------------
		public boolean getIsUnderline()
		{
			return this.underline; 
		} // IsUnderline

		// ----------------------------------------------------------------------
		public RtfTextFormat DeriveWithUnderline( boolean underline ) throws Exception
		{
			if ( this.underline == underline )
			{
				return this;
			}
			else
			{
				RtfTextFormat copy = new RtfTextFormat( this );
				copy.underline = underline;
				return copy;
			}
		} // DeriveWithUnderline

		// ----------------------------------------------------------------------
		public boolean getIsStrikeThrough()
		{
			 return this.strikeThrough;
		} // IsStrikeThrough

		// ----------------------------------------------------------------------
		public RtfTextFormat DeriveWithStrikeThrough( boolean strikeThrough ) throws Exception
		{
			if ( this.strikeThrough == strikeThrough )
			{
				return this;
			}
			else
			{
				RtfTextFormat copy = new RtfTextFormat( this );
				copy.strikeThrough = strikeThrough;
				return copy;
			}
		} // DeriveWithStrikeThrough

		// ----------------------------------------------------------------------
		public IRtfColor getBackgroundColor()
		{
			 return this.backgroundColor; 
		} // BackgroundColor

		// ----------------------------------------------------------------------
		public RtfTextFormat DeriveWithBackgroundColor( IRtfColor backgroundColor ) throws Exception 
		{
			if ( backgroundColor == null )
			{
				throw new Exception( "backgroundColor" );
			}
			if ( this.backgroundColor.equals( backgroundColor ) )
			{
				return this;
			}
			else
			{
				RtfTextFormat copy = new RtfTextFormat( this );
				copy.backgroundColor = backgroundColor;
				return copy;
			}
		} // DeriveWithBackgroundColor

		// ----------------------------------------------------------------------
		public IRtfColor getForegroundColor()
		{
			return this.foregroundColor;
		} // ForegroundColor

		// ----------------------------------------------------------------------
		public RtfTextFormat DeriveWithForegroundColor( IRtfColor foregroundColor ) throws Exception
		{
			if ( foregroundColor == null )
			{
				throw new Exception( "foregroundColor" );
			}
			if ( this.foregroundColor.equals( foregroundColor ) )
			{
				return this;
			}
			else
			{
				RtfTextFormat copy = new RtfTextFormat( this );
				copy.foregroundColor = foregroundColor;
				return copy;
			}
		} // DeriveWithForegroundColor

		// ----------------------------------------------------------------------
		public RtfTextAlignment getAlignment()
		{
			 return this.alignment; 
		} // Alignment

		// ----------------------------------------------------------------------
		public RtfTextFormat DeriveWithAlignment( RtfTextAlignment alignment ) throws Exception
		{
			if ( this.alignment == alignment )
			{
				return this;
			}
			else
			{
				RtfTextFormat copy = new RtfTextFormat( this );
				copy.alignment = alignment;
				return copy;
			}
		} // DeriveWithForegroundColor

		// ----------------------------------------------------------------------
//		IRtfTextFormat IRtfTextFormat.getDuplicate()
//		{
//			return new RtfTextFormat( this );
//		} // IRtfTextFormat.Duplicate

		// ----------------------------------------------------------------------
		public RtfTextFormat getDuplicate() throws Exception
		{
			return new RtfTextFormat( this );
		} // Duplicate

		// ----------------------------------------------------------------------
		public boolean equals( Object obj )
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
		public  int hashCode()
		{
			return HashTool.AddHashCode( this.hashCode(), ComputeHashCode() );
		} // GetHashCode

		// ----------------------------------------------------------------------
		private boolean IsEqual( Object obj )
		{
			RtfTextFormat compare = (RtfTextFormat)obj ; // guaranteed to be non-null
			return
				this.font.equals( compare.font ) &&
				this.fontSize == compare.fontSize &&
				this.superScript == compare.superScript &&
				this.bold == compare.bold &&
				this.italic == compare.italic &&
				this.underline == compare.underline &&
				this.strikeThrough == compare.strikeThrough &&
				this.backgroundColor.equals( compare.backgroundColor ) &&
				this.foregroundColor.equals( compare.foregroundColor ) &&
				this.alignment == compare.alignment;
		} // IsEqual

		// ----------------------------------------------------------------------
		private int ComputeHashCode()
		{
			int hash = this.font.hashCode();
			hash = HashTool.AddHashCode( hash, this.fontSize );
			hash = HashTool.AddHashCode( hash, this.superScript );
			hash = HashTool.AddHashCode( hash, this.bold );
			hash = HashTool.AddHashCode( hash, this.italic );
			hash = HashTool.AddHashCode( hash, this.underline );
			hash = HashTool.AddHashCode( hash, this.strikeThrough );
			hash = HashTool.AddHashCode( hash, this.backgroundColor );
			hash = HashTool.AddHashCode( hash, this.foregroundColor );
			hash = HashTool.AddHashCode( hash, this.alignment );
			return hash;
		} // ComputeHashCode

		// ----------------------------------------------------------------------
		public  String toString()
		{
			StringBuilder buf = new StringBuilder( "Font " );
			buf.append( getFontDescriptionDebug() );
			buf.append( ", " );
			buf.append( this.alignment );
			buf.append( ", " );
			buf.append( this.foregroundColor.toString() );
			buf.append( " on " );
			buf.append( this.backgroundColor.toString() );
			return buf.toString();
		} // ToString

		// ----------------------------------------------------------------------
		// members
		private IRtfFont font;
		private int fontSize;
		private int superScript;
		private boolean bold = false;
		private boolean italic = false;
		private boolean underline = false;
		private boolean strikeThrough = false;
		private IRtfColor backgroundColor = RtfColor.White;
		private IRtfColor foregroundColor = RtfColor.Black;
		private RtfTextAlignment alignment = RtfTextAlignment.Left;
		
		

	} // class RtfTextFormat

