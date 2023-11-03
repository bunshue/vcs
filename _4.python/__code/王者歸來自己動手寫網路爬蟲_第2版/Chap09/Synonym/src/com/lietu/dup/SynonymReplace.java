package com.lietu.dup;



public class SynonymReplace {


	/** The word list with score. */
	public static SynonymDic synonymDic = SynonymDic.getInstance();
	
	public static String replace(String content) throws Exception
	{
		if (content == null){
			return null;
		}
		int len = content.length();
		StringBuilder ret = new StringBuilder(len);
		SynonymDic.PrefixRet matchRet = new SynonymDic.PrefixRet(null,null);
		
		for(int i=0;i<len;)
		{
			//檢查是否存在從目前位置開始的同義字
			synonymDic.checkPrefix(content,i,matchRet);
			if(matchRet.value == SynonymDic.Prefix.Match)
			{
				ret.append(matchRet.data);
				i=matchRet.next;//下一個比對位置
			}
			else //從下一個字符開始比對
			{
				ret.append(content.charAt(i));
				++i;
			}
		}
		
		return ret.toString();
	}
}
