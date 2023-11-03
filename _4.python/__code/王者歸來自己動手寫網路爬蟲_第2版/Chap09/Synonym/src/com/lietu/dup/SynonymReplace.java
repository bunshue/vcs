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
			//�ˬd�O�_�s�b�q�ثe��m�}�l���P�q�r
			synonymDic.checkPrefix(content,i,matchRet);
			if(matchRet.value == SynonymDic.Prefix.Match)
			{
				ret.append(matchRet.data);
				i=matchRet.next;//�U�@�Ӥ���m
			}
			else //�q�U�@�Ӧr�Ŷ}�l���
			{
				ret.append(content.charAt(i));
				++i;
			}
		}
		
		return ret.toString();
	}
}
