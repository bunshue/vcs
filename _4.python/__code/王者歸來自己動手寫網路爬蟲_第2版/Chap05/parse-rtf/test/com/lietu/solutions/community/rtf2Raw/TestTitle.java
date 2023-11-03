package com.lietu.solutions.community.rtf2Raw;

import java.util.ArrayList;

import com.lietu.rtf.extract.RTFReader;
import com.lietu.rtf.extract.RTFReader.TitleInfo;

public class TestTitle {

	public static void main(String[] args) throws Exception {
		//testCandidates();
		//testRank();
		testTitle();
	}
	
	public static void testTitle() throws Exception {
		String fileName = "D:/lg/work/cnlist/test/ANBOUND-每日金融-第2564期.rtf";
		//"e:/lietu/test2/200812176164.rtf"
		String content = RTFReader.getRtfTitle(fileName);
		System.out.println(content);
	}

	public static void testCandidates() throws Exception {
		String fileName = "D:/lg/work/cnlist/test/ANBOUND-每日金融-第2564期.rtf";
		
		StringBuffer content = new StringBuffer();

		ArrayList<TitleInfo> candidates=RTFReader.getCandidates(fileName,content);
		for(TitleInfo t : candidates)
		{
			System.out.println(t);
		}
	}

	public static void testRank() throws Exception {
		String fileName = "D:/lg/work/cnlist/test/ANBOUND-每日金融-第2564期.rtf";
		
		StringBuffer content = new StringBuffer();

		ArrayList<TitleInfo> candidates=RTFReader.getCandidates(fileName,content);

		if (candidates==null || candidates.size()<=1)// 沒有候選標題
			return ;
		
		// title candidates' selection
		RTFReader.rankTitle(candidates, content.toString());
		
		for (TitleInfo t:candidates)
		{
			System.out.println(t);
		}
	}
}
