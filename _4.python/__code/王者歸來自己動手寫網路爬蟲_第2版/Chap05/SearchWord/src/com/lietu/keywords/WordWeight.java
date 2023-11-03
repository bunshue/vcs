package com.lietu.keywords;

public class WordWeight implements Comparable {
	public KeyWord word;
	public double weight;

	/**
	 *  Constructor method.
	 *
	 */
	protected WordWeight(KeyWord word, double weight) {
		this.word = word;
		this.weight = weight;
	}
	
	public String toString()
	{
		return word+":"+weight;
	}

	public int compareTo(Object obj){
		WordWeight that = (WordWeight)obj;
		
		return (int)(that.weight - weight);
	}
}