package com.lietu.rtf.model;

import com.lietu.rtf.IRtfDocumentProperty;
import com.lietu.rtf.RtfPropertyKind;
import com.lietu.rtf.RtfSpec;
import com.lietu.rtf.sys.CompareTool;
import com.lietu.rtf.sys.HashTool;


	public final class RtfDocumentProperty implements IRtfDocumentProperty
	{

		// ----------------------------------------------------------------------
		public RtfDocumentProperty( int propertyKindCode, String name, String staticValue ) 
			
		{
			this( propertyKindCode, name, staticValue, null );
		} // RtfDocumentProperty

		// ----------------------------------------------------------------------
		public RtfDocumentProperty( int propertyKindCode, String name, String staticValue, String linkValue )
		{
			try {
				if ( name == null )
				{
					throw new Exception( "name" );
				}
				if ( staticValue == null )
				{
					throw new Exception( "staticValue" );
				}
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			this.propertyKindCode = propertyKindCode;
			switch ( propertyKindCode )
			{
				case RtfSpec.PropertyTypeInteger:
					this.propertyKind = RtfPropertyKind.IntegerNumber;
					break;
				case RtfSpec.PropertyTypeRealNumber:
					this.propertyKind = RtfPropertyKind.RealNumber;
					break;
				case RtfSpec.PropertyTypeDate:
					this.propertyKind = RtfPropertyKind.Date;
					break;
				case RtfSpec.PropertyTypeBoolean:
					this.propertyKind = RtfPropertyKind.Boolean;
					break;
				case RtfSpec.PropertyTypeText:
					this.propertyKind = RtfPropertyKind.Text;
					break;
				default:
					this.propertyKind = RtfPropertyKind.Unknown;
					break;
			}
			this.name = name;
			this.staticValue = staticValue;
			this.linkValue = linkValue;
		} // RtfDocumentProperty

		// ----------------------------------------------------------------------
		public int getPropertyKindCode()
		{
			 return this.propertyKindCode;
		} // PropertyKindCode

		// ----------------------------------------------------------------------
		public RtfPropertyKind getPropertyKind()
		{
			return this.propertyKind; 
		} // PropertyKind

		// ----------------------------------------------------------------------
		public String getName()
		{
			 return this.name; 
		} // Name

		// ----------------------------------------------------------------------
		public String getStaticValue()
		{
			 return this.staticValue; 
		} // StaticValue

		// ----------------------------------------------------------------------
		public String getLinkValue()
		{
			 return this.linkValue;
		} // LinkValue

		// ----------------------------------------------------------------------
		public  boolean equals( Object obj )
		{
			if ( obj == this )
			{
				return true;
			}
			else if ( obj == null || this.getClass() != obj.getClass() )
			{
				return false;
			}
			return isEqual( obj );
		} // Equals

		// ----------------------------------------------------------------------
		private boolean isEqual( Object obj )
		{
			RtfDocumentProperty compare = (RtfDocumentProperty)obj ; // guaranteed to be non-null
			return
				this.propertyKindCode == compare.propertyKindCode &&
				this.propertyKind == compare.propertyKind &&
				this.name.equals( compare.name ) &&
				CompareTool.AreEqual( this.staticValue, compare.staticValue ) &&
				CompareTool.AreEqual( this.linkValue, compare.linkValue );
		} // IsEqual

		// ----------------------------------------------------------------------
		public  int hashCode()
		{
			return HashTool.AddHashCode( this.hashCode(), ComputeHashCode() );
		} // GetHashCode

		// ----------------------------------------------------------------------
		private int ComputeHashCode()
		{
			int hash = this.propertyKindCode;
			hash = HashTool.AddHashCode( hash, this.propertyKind );
			hash = HashTool.AddHashCode( hash, this.name );
			hash = HashTool.AddHashCode( hash, this.staticValue );
			hash = HashTool.AddHashCode( hash, this.linkValue );
			return hash;
		} // ComputeHashCode

		// ----------------------------------------------------------------------
		public  String toString()
		{
			StringBuilder buf = new StringBuilder( this.name );
			if ( staticValue != null )
			{
				buf.append( "=" );
				buf.append( this.staticValue );
			}
			if ( linkValue != null )
			{
				buf.append( "@" );
				buf.append( this.linkValue );
			}
			return buf.toString();
		} // ToString

		// ----------------------------------------------------------------------
		// members
		private  int propertyKindCode;
		private  RtfPropertyKind propertyKind;
		private  String name;
		private  String staticValue;
		private  String linkValue;

	} // class RtfDocumentProperty

