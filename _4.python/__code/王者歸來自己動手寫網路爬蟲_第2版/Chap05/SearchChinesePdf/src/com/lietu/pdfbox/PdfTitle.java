package com.lietu.pdfbox;

import java.awt.Color;
import java.util.ArrayList;

import org.apache.pdfbox.util.TextPosition;

public class PdfTitle {
	public String title = null;
	public Color textColor = null;
	public float fontSize;
	public float y;
	ArrayList<TextPosition> texts;
	
	public PdfTitle(String t,float h)
	{
		title = t;
		fontSize = 1f;
		y=h;
		textColor = java.awt.Color.BLACK;
	}
	
	public PdfTitle(Color c,float f,float h,ArrayList<TextPosition> text)
	{
		title = delOverlap(text);
		textColor = c;
		fontSize = f;
		y = h;
		texts = text;

		/*if(texts!=null)
		{
			for (TextPosition e : texts) {
				System.out.println(e.getCharacter());
			}
		}*/
	}
	
	public ArrayList<PdfTitle> split()
	{
		if(texts == null || texts.size()<=1)
			return null;
		float maxMargin = getMaxMargin();
		if(maxMargin<=0.0f)
		{
			return null;
		}
		//System.out.println("max margin:"+maxMargin);
		
		float lastY = 0f;
		int last=0;
		ArrayList<PdfTitle> subTitle = new ArrayList<PdfTitle>();
		for(int i=0;i<texts.size();++i)
		{
			TextPosition tp = texts.get(i);
			if(lastY==0f)
			{
				lastY = tp.getY();
			}
			float margin = (tp.getY() - lastY);
			
			if(margin==maxMargin)
			{
				//System.out.println("meet max margin "+maxMargin);
				//merge title from last to i
				subTitle.add(getTitle(last,i-1));
				last=i;
			}
			lastY = tp.getY();
		}

		if(last<(texts.size()-1))
		{
			subTitle.add(getTitle(last,texts.size()-1));
		}
		
		return subTitle;
	}
	
	public PdfTitle getTitle(int begin,int end)
	{
		//String content = "";
		ArrayList<TextPosition> tps = new ArrayList<TextPosition>(end - begin +1);
		for(int i=begin;i<=end;++i)
		{
			TextPosition tp = texts.get(i);
			//content += tp.getCharacter();
			tps.add(tp);
		}
		
		float y = texts.get(end).getY(); // - texts.get(begin).getY();
		
		return new PdfTitle(textColor,fontSize,y,tps);
	}
	
	public float getMaxMargin()
	{
		float maxMargin = 0f;
		float lastY = 0f;
		
		for(TextPosition tp:texts)
		{
			float margin = 0f;
			if(lastY==0f)
			{
				//System.out.println("begin Margin:"+maxMargin);
				lastY = tp.getY();
			}
			if(tp.getY()>lastY)
			{
				margin = (tp.getY() - lastY);
				//System.out.println("Margin:"+tp.getY()+" "+lastY);
				lastY = tp.getY();
			}
			if(margin>maxMargin)
			{
				//System.out.println("max Margin:"+margin + " "+tp.getCharacter());
				maxMargin = margin;
			}
			//System.out.println("Margin:"+margin + " "+tp.getCharacter());
		}
		//System.out.println("maxMargin:"+maxMargin);
		return maxMargin;
	}	

    public static String delOverlap(ArrayList<TextPosition> texts)
    {
    	if(texts==null)
    		return null;
    	//System.out.println("enter del overlap");
    	boolean overlap = false;
		for(int i=0;i<texts.size();++i)
		{
			//System.out.println("enter del overlap"+texts.get(i).getCharacter() );
			for(int j=1;j<texts.size();++j)
			{
				if(i==j)
				{
					continue;
				}
				if(overlap(texts.get(i),texts.get(j)))
				{
					texts.remove(j);
					j--;
					overlap = true;
				}
			}
		}
		StringBuilder sb = new StringBuilder();
		for (TextPosition e : texts) {
			sb.append(e.getCharacter());
		}
		return sb.toString().trim();
    }

    public static boolean overlap( TextPosition tp1, TextPosition tp2 )
    {
    	if(!tp1.getCharacter().equals(tp2.getCharacter()))
    		return false;
    	
    	if(!within(tp1.getHeight(),tp2.getHeight(), 1.1f))
    		return false;
    	
    	float diff = (tp1.getHeight() + tp2.getHeight())*0.02f;
        return within( tp1.getX(), tp2.getX(), diff) && within( tp1.getY(), tp2.getY(), diff) ;
    }

    /**
     * This will determine of two floating point numbers are within a specified variance.
     *
     * @param first The first number to compare to.
     * @param second The second number to compare to.
     * @param variance The allowed variance.
     */
    private static boolean within( float first, float second, float variance )
    {
        return second > first - variance && second < first + variance;
    }

	public String toString()
	{
		return title+" textColor:"+textColor+" fontSize:"+fontSize+ " length:"+title.length();
	}
}
