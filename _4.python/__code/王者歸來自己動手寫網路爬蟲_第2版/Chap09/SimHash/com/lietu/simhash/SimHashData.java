package com.lietu.simhash;

public class SimHashData {
	

	//資料
	public long q;
	
	//在原始資料中的序號
	public long no;
	
	public SimHashData(long qp)
	{
		q = qp;
		no = qp;
	}

	public SimHashData(long qp,long n)
	{
		q = qp;
		no = n;
	}

	public int hashCode() {
		return (int)no;
	}
	
	public boolean equals(Object obj){
		if (obj instanceof SimHashData ) {
			if(((SimHashData)obj).no == this.no )
				return true;
		}
		return false;
	}
}
