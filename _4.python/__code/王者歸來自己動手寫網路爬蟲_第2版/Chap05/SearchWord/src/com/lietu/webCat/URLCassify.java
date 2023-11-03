package com.lietu.webCat;

public class URLCassify {

	/** The word list with score. */
	public static URLPattern urlDic = URLPattern.getInstance();
	
	public static String check(String content)
	{
		int len = content.length();
		char[] body = content.toCharArray();
		URLPattern.PrefixRet sWordMatch = new URLPattern.PrefixRet(null,null);
		
		for(int i=0;i<len;++i)
		{
			String sWord = String.valueOf(body[i]);
			int j=i+1;
			urlDic.checkPrefix(sWord,sWordMatch);
			
			while(true)
			{
				if (sWordMatch.value==URLPattern.Prefix.MisMatch)
					break;
				
				if(sWordMatch.value == URLPattern.Prefix.Match)
				{
					// find the current word
					String cat = sWordMatch.data;
					
					return cat;
				}
				if ( j>=len)
					break;
				
				sWord+=body[j++];
				//System.out.println("to find prefix of :"+sWord);
				urlDic.checkPrefix(sWord,sWordMatch);
			}
		}
		
		return null;
	}
	
	// Test program
	public static void main( String [ ] args ) throws Exception
	{
		String result=null;
		long start = System.currentTimeMillis();
		//for(int i =0;i<10000;++i)
		String url = "http://www.cybosoft.com.cn/products/labviewmc.html";
		//"http://www.comfile.com.cn/news-2.htm";
			//"http://www.cybosoft.com.cn/products/labviewmc.html";
		//String url = "http://www.comfile.com.cn/company.htm"
			result = URLCassify.check(url);
		long end = System.currentTimeMillis();
		System.out.println("cost times:"+ (end - start) );
		System.out.println("the result:"+result);
	}
}
