package com.bitmechanic.spindle;

public class TitleDetectQ {
	private CircularStringBuffer titleQueue = new CircularStringBuffer();

	public TitleDetectQ()
	{
	}
	
	public boolean detect(String newDoc)
	{
		boolean isDuplicate=false;

		if (titleQueue.contains(newDoc))
			isDuplicate = true;
		else
			titleQueue.write(newDoc);
		
		//System.out.println("isDuplicate?"+isDuplicate);

		return isDuplicate;
	}
}
