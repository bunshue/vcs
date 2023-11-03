package com.bitmechanic.spindle;

public class XmlElement {

	private String url;
	private String types;
	private String classes;
	private int rank;
	
	public XmlElement(String url,String types,String classes,int rank){
	  this.url = url;
	  this.types = types;
	  this.classes = classes;
	  this.rank = rank;
	}
	
	public String getUrl()
	{
		return this.url;
	}
	public void  setUrl(String url)
	{
		  this.url = url;
	}
	
	public String getTypes()
	{
		return this.types;
	}
	
	public void setTypes(String types)
	{
		 this.types = types;
	}
	
	public String getClasses()
	{
		  return this.classes;
	}
	
	public void setClasses(String classes)
	{
		  this.classes = classes;
	}

	public int getRank() {
		return rank;
	}

	public void setRank(int rank) {
		this.rank = rank;
	}
}
