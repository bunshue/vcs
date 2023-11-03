package com.lietu.rtf.parser;

import java.util.HashMap;

public class CodePage2Locale {

	static HashMap<Integer,String> map = new HashMap<Integer,String>();
	
	public CodePage2Locale()
	{
		map.put(950, "BIG5");
		map.put(1250, "CP1250");
		map.put(1251, "CP1251");
		map.put(1252,"GBK");
		map.put(1253, "CP1253");
		map.put(1254, "CP1254");
		map.put(1255, "CP1255");
		map.put(1256,"CP1256");
		map.put(1257,"CP1257");
		map.put(1258,"CP1258");
		map.put(932,"CP932");
		map.put(936,"CP936");
		map.put(949 ,"CP949");
		map.put(950,"CP950");
		map.put(20932,"EUCJP");
		map.put(936 ,"GBK");
		map.put(37,"IBM037");
		map.put(1026,"IBM1026");
		map.put(424,"IBM424");
		map.put(437,"IBM437");
		map.put(500,"IBM500");
		map.put(850,"IBM850");
		map.put(852,"IBM852");
		map.put(855,"IBM855");
		map.put(857,"IBM857");
		map.put(860,"IBM860");
		map.put(861,"IBM861");
		map.put(862,"IBM862");
		map.put( 863,"IBM863");
		map.put(864,"IBM864");
		map.put(865,"IBM865");
		map.put(866,"IBM866");
		map.put(869,"IBM869");
		map.put(874,"IBM874");
		map.put(875,"IBM875");
		map.put(28591,"ISO88591");
		map.put(28600,"ISO885910");
		map.put(28603,"ISO885913");
		map.put(28604,"ISO885914");
		map.put(28605,"ISO885915");
		map.put(28606,"ISO885916");
		map.put(28592,"ISO88592");
		map.put(28593,"ISO88593");
		map.put(28594,"ISO88594");
		map.put(28595,"ISO88595" );
		map.put(28596,"ISO88596" );
		map.put(28597,"ISO88597");
		map.put(28598,"ISO88598");
		map.put(28599,"ISO88599");
		map.put(20866,"KOI8R");
		map.put(21866,"KOI8U");
		map.put(65001,"UTF8");
	}
	public String getLocale(int key)
	{
		return map.get(key);
	}

}
