/*
 * Created on 2006-1-16
 *
 */
package com.lietu.pdfbox;

import java.util.HashSet;

/**
 * @author Administrator
 *
 */
public class OperatorSet extends HashSet<String>
{
	/**
	 * 
	 */
	private static final long serialVersionUID = -5739693689170303932L;
	private static OperatorSet opSet = new OperatorSet();

	/**
	 * 
	 * @return the singleton of basic dictionary
	 */
	public static OperatorSet getInstance()
	{
		return opSet;
	}
	
	private OperatorSet()
	{
		super(30);
        this.add("Do");
        //path
        this.add("n");
        this.add("re");
        this.add("h");
        this.add("c");
        this.add("v");
        this.add("y");
        this.add("b");
        this.add("B");
        this.add("b*");
        this.add("B*");
        this.add("W*");
        this.add("m");
        this.add("l");
        this.add("f");
        this.add("F");
        this.add("f*");
        this.add("S");
        
        //line
        this.add("d");
        this.add("J");
        this.add("j");
        this.add("M");
        this.add("w");
	}
}
