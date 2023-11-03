package com.lietu.keywords;

public class KeyWord implements Comparable<KeyWord>{
	public String one = null;
	public String two = null;
	public String three = null;
	
	public KeyWord(String o)
	{
		one = o;
		two = null;
		three = null;
	}

	public KeyWord(String o,String t)
	{
		one = o;
		two = t;
		three = null;
	}

	public KeyWord(String o,String t,String h)
	{
		one = o;
		two = t;
		three = h;
	}

 	public String toString()
 	{
 		String temp=one;
 		if(two == null)
 			return temp;
 		temp += two;
 		if(three == null)
 			return temp; 		
 		temp += three;
 		return temp;
	}

 	public int compareTo(KeyWord o2){
 		int ret = 0;

		if(this.one==null)
		{
			if(o2.one == null)
				return 0;
			return -1;
		}
		
		ret = this.one.compareTo(o2.one);
		if(ret!=0)
		{
			return ret;
		}

		if(this.two==null)
		{
			if(o2.two == null)
				return 0;
			return -1;
		}

		ret = this.two.compareTo(o2.two);
		if(ret!=0)
		{
			return ret;
		}

		if(this.three==null)
		{
			if(o2.three == null)
				return 0;
			return -1;
		}

		ret = this.three.compareTo(o2.three);
		return ret;
	}
 	
    public boolean equals(Object obj) {
 		//System.out.println("enter equals");
    	KeyWord o2 = (KeyWord)obj;
    	
 		//System.out.println(this.one+":"+this.two+":"+this.three);
 		//System.out.println(o2.one+":"+o2.two+":"+o2.three);
 		boolean ret = this.one.equals(o2.one);
 		
 		if(this.two==null)
 		{
 			if(o2.three == null)
				return true;
			return false;
 		}
 		ret = ret && this.two.equals(o2.two);

		if(this.three==null)
		{
			if(o2.three == null)
				return true;
			return false;
		}

    	return ( this.three.equals(o2.three) );
    }
    
    public int hashCode()
    {
    	int ret = this.one.hashCode();
    	if(this.two!=null)
    	{
    		ret = ret ^ this.two.hashCode();
    	}
    	if(this.three!=null)
    	{
    		ret = ret ^ this.three.hashCode();
    	}
    	return ret;
    }
}
