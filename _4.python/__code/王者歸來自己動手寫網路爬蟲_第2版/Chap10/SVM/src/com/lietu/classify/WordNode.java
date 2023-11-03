package com.lietu.classify;

public class WordNode {
	static final double dZero = 1.0E-10;
	
	//	�b�S�x��ܪ��ɭԥΨ��x�s�S�x�����O�Ϥ���
	//�b�S�x��ܧ�������A���Ψ��x�s�C�ӯS�x��"log(�V�m����`��/�S�x������W�v)"��
	public float m_dWeight;
	public int m_nAllocLen;
	public int m_nWordID;           //�S�x��ID
	public double[] catWeight = null;   //�S�x���C�����O���Ϥ���
	//�S�x�b��Ӥ�󶰤�������W�v,��ڴN�O���GetDocNum()�Ǧ^����
	//�p�G�S�x���O�q�V�m��󶰤���ܱo�쪺�A�N�L�k�ϥ�GetDocNum()�o��S�x������W�v
	//�ҥH�A���B�ϥ�m_lDocFreq�ӰO���S�x������W�v
	public int m_lDocFreq;         //�S�x�b��Ӥ�󶰤�������W�v
	//�S�x�b��Ӥ�󶰤������W,��ڴN�O���GetWordNum()�Ǧ^����
	//�p�G�S�x���O�q�V�m��󶰤���ܱo�쪺�A�N�L�k�ϥ�GetWordNum()�o��S�x�����W
	//�ҥH�A���B�ϥ�m_lWordFreq�ӰO���S�x�����W
	public int m_lWordFreq;        //�S�x�b��Ӥ�󶰤������W
	public long[] m_pCataDocFreq = null;    //�S�x�b�C�@�����O��������W�v
	public long[] m_pCataWordFreq = null;   //�S�x�b�C�@�����O�������W
	public long m_lDocID;           //�o��S�x������W�v���ɭԥΨ�
	
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

	//	����ƼȥB�u�b���h�������Ψ�,��ƦW�٩M���{���\��ݰ_�Ӧ��I���P
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
	
	//	�Ω�p��S�x���v���A�Ѽ�sum�N���󶰤�������`��
	//	�p�GbMult=true�Bm_dWeight�j��0, �h�N�S�x���Ϥ����W�v���Wm_dWeight��Ӫ���, �A�x�s�즨���ܼ�m_dWeight��
	//	�_�h, �N�S�x���Ϥ����W�v���x�s�즨���ܼ�m_dWeight��
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
