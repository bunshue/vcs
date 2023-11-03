package test.com.lietu.filter;

import com.lietu.filter.WordReader;

public class TestWordReader {

	public static void main(String[] args) throws Exception {
		String fileName = // "D:/lg/work/xiaoxishu/Solr布署.doc";
		// "D:/lg/DM/利用决策树评价生产方案.doc";
		// "D:/lg/work/train/自己动手写搜索引擎.doc";
		"D:/lg/work/hblocaltax/doc/1243847838.doc";
		// "D:/lg/work/hblocaltax/doc/20090409114958129.doc";

		String text = WordReader.getWordTitle(fileName);
		System.out.println("最佳标题：" + text);
	}
	
	public static void testGetCandiate() throws Exception {
		String fileName = // "D:/lg/work/xiaoxishu/Solr布署.doc";
		// "D:/lg/DM/利用决策树评价生产方案.doc";
		// "D:/lg/work/train/自己动手写搜索引擎.doc";
		"D:/lg/work/hblocaltax/doc/1243847838.doc";
		// "D:/lg/work/hblocaltax/doc/20090409114958129.doc";
		
		String text = WordReader.getWordTitle(fileName);
		System.out.println("最佳标题：" + text);
	}

}
