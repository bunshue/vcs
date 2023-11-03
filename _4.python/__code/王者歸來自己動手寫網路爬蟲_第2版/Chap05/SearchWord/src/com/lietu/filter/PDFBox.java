
package com.lietu.filter;


import java.io.InputStream;
import java.net.MalformedURLException;
import java.util.StringTokenizer;

import org.pdfbox.pdmodel.PDDocument;
import org.pdfbox.util.PDFTextStripper;

public class PDFBox {
	
	public static String getText(InputStream file)throws Exception{
		//是否排序
		boolean sort=false;
		//返回文本
		String outStr=null;
		//开始提取页数
		int startPage=1;
		//结束提取页数
		int endPage=10;
		//内存中存储的PDF DOcument
		PDDocument document=null;
		try{
			try{
				//当作一个URL来装载文件
				document=PDDocument.load(file);
			}catch(MalformedURLException e){
			}
			//用PDFTextStripper来提取文本
			PDFTextStripper stripper =new PDFTextStripper();
			//设置是否排序
			stripper.setSortByPosition(sort);
			//设置起始页
			stripper.setStartPage(startPage);
			//设置结束页
			stripper.setEndPage(endPage);
			
			outStr=stripper.getText(document);
			
			return(outStr);
		}
		catch(Exception e)
		{
			return "";
		}
		finally{
			if(document!=null){
				document.close();
			}
		}
	}
	
	public static boolean isNumber(String str){
		StringTokenizer st=new StringTokenizer(str," ");
		boolean allIsNum=true;
		while(st.hasMoreTokens()){
			String temp=st.nextToken();
			try{
				Integer.parseInt(temp.trim());
			}catch(Exception e) {
				allIsNum=false;
				break;
			}
		}
		return allIsNum;
	}
	
	public static String getTitle(String outStr){
		StringTokenizer st=new StringTokenizer(outStr,"\n");
		String title="";
		
		String[] string={"","","",""};
		int count=0;
		while(count<4){
			if(!st.hasMoreTokens()){
				  break;
			}
			String str1=st.nextToken().trim();
			if(     str1.length()<2
					||str1.length()>100
			                ||(str1.indexOf(".2003")>0)
					||(str1.indexOf(".2004")>0)
					||(str1.indexOf(".2005")>0)
					||(str1.indexOf(".2006")>0)
					||(str1.indexOf(".2002")>0)
					||(str1.indexOf(".2001")>0)
					||(str1.indexOf(".2007")>0)
					||(str1.indexOf("/2003")>0)
					||(str1.indexOf("/2004")>0)
					||(str1.indexOf("/2005")>0)
					||(str1.indexOf("/2006")>0)
					||(str1.indexOf("/2002")>0)
					||(str1.indexOf("/2001")>0)
					||(str1.indexOf("/2007")>0)
					||(str1.indexOf(".com")>0)
					||(str1.indexOf(".cn")>0)
					||(str1.indexOf("copyright")>0)
					||isNumber(str1)
			    )
			{
				continue;
			}
			else
			{
			    string[count] = str1;
			    count++;
			}
		}
		
		title=string[0];
		
		for(int i=1;title.replaceAll(" ", "").length()<=50&&i<4;i++){
			title=title+" "+string[i];
		}
		
		return title;
	}
}