package com.lietu.classify;

public class WordNode {
	static final double dZero = 1.0E-10;
	
	//	在特徵選擇的時候用來儲存特徵的類別區分度
	//在特徵選擇完成之後，它用來儲存每個特徵的"log(訓練文件總數/特徵的文件頻率)"值
	public float m_dWeight;
	public int m_nAllocLen;
	public int m_nWordID;           //特徵的ID
	public double[] catWeight = null;   //特徵對於每個類別的區分度
	//特徵在整個文件集中的文件頻率,實際就是函數GetDocNum()傳回的值
	//如果特徵不是從訓練文件集中選擇得到的，就無法使用GetDocNum()得到特徵的文件頻率
	//所以，此處使用m_lDocFreq來記錄特徵的文件頻率
	public int m_lDocFreq;         //特徵在整個文件集中的文件頻率
	//特徵在整個文件集中的詞頻,實際就是函數GetWordNum()傳回的值
	//如果特徵不是從訓練文件集中選擇得到的，就無法使用GetWordNum()得到特徵的詞頻
	//所以，此處使用m_lWordFreq來記錄特徵的詞頻
	public int m_lWordFreq;        //特徵在整個文件集中的詞頻
	public long[] m_pCataDocFreq = null;    //特徵在每一個類別中的文件頻率
	public long[] m_pCataWordFreq = null;   //特徵在每一個類別中的詞頻
	public long m_lDocID;           //得到特徵的文件頻率的時候用到
	
	public WordNode()
	{
		m_dWeight=0.0f;
		m_nAllocLen=0;
		catWeight=null;
		m_pCataDocFreq=null;
		m_pCataWordFreq=null;
		m_lDocFreq=0;
		m_lWordFreq=0;
		m_nWordID=-1;
		m_lDocID=-1;
	}

	public String toString()
	{
		StringBuilder sb = new StringBuilder();
		sb.append("m_nWordID:");
		sb.append(m_nWordID);
		sb.append('\n');
		
		sb.append("m_dWeight:");
		sb.append(m_dWeight);
		sb.append('\n');

		sb.append("m_lDocFreq:");
		sb.append(m_lDocFreq);
		sb.append('\n');

		sb.append("m_lWordFreq:");
		sb.append(m_lWordFreq);
		sb.append('\n');

		sb.append("catWeight:");
		for(double cw:catWeight)
		{
			sb.append(cw);
			sb.append(" ");
		}
		sb.append('\n');
		
		sb.append("m_pCataDocFreq:");
		for(long cw:m_pCataDocFreq)
		{
			sb.append(cw);
			sb.append(" ");
		}
		sb.append('\n');

		sb.append("m_pCataWordFreq:");
		for(long cw:m_pCataWordFreq)
		{
			sb.append(cw);
			sb.append(" ");
		}
		sb.append('\n');
		
		return sb.toString();
	}
	
	public void initBuffer(int nLen)
	{
		if(nLen<=0) return;
		if(m_nAllocLen<=0&&catWeight==null&&
			m_pCataDocFreq==null&&m_pCataWordFreq==null)
		{
			m_nAllocLen=nLen;
			catWeight=new double[m_nAllocLen];
			//for(int i=0;i<m_nAllocLen;++i)
			//{
			//	catWeight[i]=0;
			//}
			m_pCataDocFreq=new long[m_nAllocLen];

			//for(int i=0;i<m_nAllocLen;++i)
			//{
			//	m_pCataDocFreq[i]=0;
			//}
			m_pCataWordFreq=new long[m_nAllocLen];

			//for(int i=0;i<m_nAllocLen;++i)
			//{
			//	m_pCataWordFreq[i]=0;
			//}
		}
	}

	//	此函數暫且只在階層分類中用到,函數名稱和其實現的功能看起來有點不同
	public void copy(WordNode wordNode)
	{
		m_dWeight=wordNode.m_dWeight;
		m_nAllocLen=0;
		m_nWordID=wordNode.m_nWordID;
		m_lDocFreq=wordNode.m_lDocFreq;
		catWeight=null;
		m_pCataDocFreq=null;
		m_pCataWordFreq=null;
		m_lDocID=0;
	}
	
	public long getWordNum()
	{
		long sum=0;
		if(m_nAllocLen>0)
		{
			for(int i=0;i<m_nAllocLen;i++)
				sum+=m_pCataWordFreq[i];
		}
		else sum=m_lWordFreq;
		return sum;
	}
	
	public long getDocNum()
	{
		long sum=0;
		if(m_nAllocLen>0)
		{
			for(int i=0;i<m_nAllocLen;i++)
				sum+=m_pCataDocFreq[i];
		}
		else sum=m_lDocFreq;
		return sum;
	}
	
	public long getCataWordNum(int cataID)
	{
		return m_pCataWordFreq[cataID];	
	}
	
	public long getCataDocNum(int cataID)
	{
		long sum=0;
		if(m_nAllocLen>0)
		{
			for(int i=0;i<m_nAllocLen;i++)
				sum+=m_pCataDocFreq[i];
		}
		else sum=m_lDocFreq;
		return sum;
	}
	
	//	用於計算特徵的權重，參數sum代表文件集中的文件總數
	//	如果bMult=true且m_dWeight大於0, 則將特徵的反比文件頻率乘上m_dWeight原來的值, 再儲存到成員變數m_dWeight中
	//	否則, 將特徵的反比文件頻率值儲存到成員變數m_dWeight中
	public void computeWeight(long sum, boolean bMult)
	{
		long docFreq=getDocNum();
		if(docFreq<=0&&sum<=0)
		{
			m_dWeight=0.0f;
			return;
		}
		float weight=(float)Math.log((double)sum/(double)docFreq);
		if(bMult&&m_dWeight>dZero)
			m_dWeight*=weight;
		else
			m_dWeight=weight;
	}
	
	public void computeWeight(long sum)
	{
		computeWeight(sum, false);
	}
}
