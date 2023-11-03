/*
 * Created on 2004-11-21
 *
 */
package com.lietu.keywords;

/**
 * @author Administrator
 *
 */
public class Bigrams {
	String one;
	String two;
	private int hashvalue = 0;
	
 	Bigrams(String first, String second) {
 		this.one = first;
 		this.two = second;
 		hashvalue = (one.hashCode() ^ two.hashCode());
 		//System.out.println("bigram:"+this.one +" "+this.two);
 	}
 	
 	public String toString(){
 		return one+"@"+two;
 	}
 	
    /**
     * Override equals and hashcode to ensure Index objects
     * behave correctly when used as keys in a hash table.
     */
    public boolean equals(Object obj)
    {
      if (obj instanceof Bigrams)
      {
      	Bigrams index = (Bigrams) obj;
        return ((one .equals( index.one)) && (two.equals(index.two)));
      }
      else
      {
        return false;
      }
    }

    /**
     * return hash code
     */
    public int hashCode()
    {
      return hashvalue;
    }
}
