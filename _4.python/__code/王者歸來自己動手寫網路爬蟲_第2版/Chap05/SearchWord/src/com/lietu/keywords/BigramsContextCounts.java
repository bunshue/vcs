/*
 * Created on 2004-11-25
 *
 */
package com.lietu.keywords;

import java.io.Serializable;

/**
 * @author Administrator
 *
 */
public class BigramsContextCounts  implements Serializable ,Comparable {
	/**
	 * 
	 */
	private static final long serialVersionUID = -1852465567213729102L;
	public int count;
	public String one;
	public String two;
 	double entropy;
	
 	public BigramsContextCounts(int count, double entropy,String one,String two)
 	{
 		this.count = count;
 		this.entropy = entropy;
 		this.one = one;
 		this.two = two;
 	}
 	public int compareTo(Object o2){
		double i1 = this.entropy;
		double i2 = ((BigramsContextCounts)o2).entropy;
		if(i1 == i2) return 0;
		return ((i1 > i2) ? -1 : +1);
	}
 	
 	public String toString()
 	{
 		String temp=one+":"+two+" count:"+count+" ent:"+entropy ; 		
 			
 		return temp;
	}
}
