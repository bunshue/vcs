package com.lietu.classify;

//用來記錄文件向量中每一維特徵的權重
public class WeightNode {
	public int s_idxWord=0;    //特徵的ID
	public short s_tfi=0;        //特徵在文件中出現的頻次
	public float s_dWeight=0;    //特徵的權重
	
	public String toString()
	{
		return "tfi:"+s_tfi;
	}
}
