
package com.lietu.filter;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.StringTokenizer;

import org.apache.poi.hslf.extractor.PowerPointExtractor;

public class PowerPointReader {

	public static String readDoc(InputStream is) throws IOException{
		//创建PowerPointExtractor
		PowerPointExtractor extractor=new PowerPointExtractor(is);
		//	对PPT文件进行提取
		String text = extractor.getText();
		
		return text;
	}

	public static String getTitle(String str){
		StringTokenizer st=new StringTokenizer(str ,"\n");
		String title=st.nextToken();
		while("".equals(title.trim())){
			if(st.hasMoreTokens()){
				 title=st.nextToken();
			}
			else
			{
				break;
			}
		}
		if(title.length()>50){
			if(title.indexOf(' ')>0)
				title=title.substring(0, title.indexOf(' '));
			else if(title.indexOf('。')>0)
				title=title.substring(0, title.indexOf('。'));
			else if(title.indexOf('.')>0)
				title=title.substring(0, title.indexOf('.'));
		}
		return title;
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		//application/vnd.ms-powerpoint
		try{
			String fileName = "D:/lg/work/SSeg/Doc/企业搜索.ppt";
			InputStream is = new FileInputStream(fileName);
			String text=PowerPointReader.readDoc(is);
			System.out.println(getTitle(text));
			//System.out.println(text);
		}catch(Exception e){
			e.printStackTrace();
		}
	}
	}
