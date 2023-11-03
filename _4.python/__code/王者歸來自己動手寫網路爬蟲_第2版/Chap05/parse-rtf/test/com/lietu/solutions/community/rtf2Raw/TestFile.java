package com.lietu.solutions.community.rtf2Raw;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;

import com.lietu.rtf.extract.RtfExtractor;

public class TestFile {

	/**
	 * @param args
	 * @throws Exception 
	 */
	public static void main(String[] args) throws Exception {
		String file = //"D:/lg/work/cnlist/minimal.rtf";
			//"D:/lg/work/cnlist/ANBOUND-每日金融-第2564期.rtf";
			//"D:/lg/work/cnlist/test.rtf";
			//"D:/lg/work/cnlist/n.rtf";
			//"D:/lg/work/cnlist/4.rtf";  // error
			//"D:/lg/work/cnlist/c.rtf";  // error
			//"D:/lg/work/cnlist/z.rtf";
			"D:/lg/work/cnlist/test/2.rtf";
			//"D:/lg/work/cnlist/ANBOUND-每日金融-第2564期.rtf";
			//"D:/lg/work/cnlist/t.rtf";
			//"D:/lg/work/cnlist/6.rtf";
		String stream=getRtfFile(file);
		//System.out.println(stream);
		RtfExtractor  extractor=new RtfExtractor(stream);
		String text = extractor.getText();
		
		System.out.println("text:"+text);
	}
	
	public static String getRtfFile(String fileName) throws IOException{
		String str = "";
		Scanner scanner = new Scanner(new File(fileName));
		scanner.useDelimiter("\\z");
		while(scanner.hasNext())
		{
			String buffer = scanner.next();
			str=str+ buffer;
		}
		scanner.close();
		return str;
	}

}
