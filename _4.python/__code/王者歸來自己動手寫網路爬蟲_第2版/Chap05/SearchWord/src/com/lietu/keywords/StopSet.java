/*
 * Created on 2006-1-16
 *
 */
package com.lietu.keywords;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.HashSet;

/**
 * @author Administrator
 *
 */
public class StopSet extends HashSet<String>
{
	/**
	 * 
	 */
	private static final long serialVersionUID = -5739693689170303932L;
	private static StopSet stopSet = new StopSet();

	/**
	 * 
	 * @return the singleton of basic dictionary
	 */
	public static StopSet getInstance()
	{
		return stopSet;
	}
	
	private StopSet()
	{
		super(1000);
		String sParagraph;
		try{
			String dic = "/stopword.txt";
			InputStream file = null;
			if (System.getProperty("dic.dir") == null)
				file = getClass().getResourceAsStream(CnPhraseDic.getDir()+dic);
			else
				file = new FileInputStream(new File(CnPhraseDic.getDir()+dic));
			
			BufferedReader in;
			in = new BufferedReader(new InputStreamReader(file,"GBK"));
			
	    	while( true )
	    	{
	    		sParagraph = in.readLine();
	    		if (sParagraph == null )
	    			break;
	    		
				if (!"".equals(sParagraph))
				{
					this.add(sParagraph);
				}
	    	}
	    	in.close();
		}catch (Exception e)
		{
			e.printStackTrace(System.err);
		}
	}
}
