package com.lietu.simhash;

import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.List;

import com.lietu.data.AccessManager;
import com.lietu.similarity.Record;
import com.lietu.tel.TelNumber;
import com.lietu.tel.TelSeg;

public class POISimHash {
	

	public int[] weights ;
	public String[] features = new String[37];
	public POISimHash(){
		this.weights=getWeights();
	}
	
	public static void evaluate(int[] weights, int[] tempweit)// 將暫存在連續陣列中的權重值賦到weights中
	{
		weights[0] = tempweit[0];
		weights[1] = tempweit[1];
		weights[3] = tempweit[2];
		weights[4] = tempweit[4];
		weights[9] = tempweit[3];
		weights[11] = tempweit[5];
		weights[12] = tempweit[6];
		weights[13] = tempweit[7];
		weights[18] = tempweit[8];
		weights[22] = tempweit[9];
		weights[24] = tempweit[10];
		weights[27] = tempweit[11];
		weights[28] = tempweit[12];
		weights[34] = tempweit[13];
	}

	public static void evaluateA(int[] weights, int[] tempweit)// 將暫存在連續陣列中的權重值賦到weights中
	{
		tempweit[0] = weights[0];
		tempweit[1] = weights[1];
		tempweit[2] = weights[3];
		tempweit[3] = weights[9];
		tempweit[4] = weights[4];
		tempweit[5] = weights[11];
		tempweit[6] = weights[12];
		tempweit[7] = weights[13];
		tempweit[8] = weights[18];
		tempweit[9] = weights[22];
		tempweit[10] = weights[24];
		tempweit[11] = weights[27];
		tempweit[12] = weights[28];
		tempweit[13] = weights[34];
	}

	// 合併地址，path參數用於指定access資料表儲存的位置
	public static void mergeAddress(String tableName, String path) {
		try {
			List<String> lsname;
			lsname = com.lietu.data.AccessManager.init("select * from "
					+ tableName, "名稱");
			List<String> addname;
			addname = com.lietu.data.AccessManager.init("select * from "
					+ tableName, "地址");
			List<String> proname;
			proname = com.lietu.data.AccessManager.init("select * from "
					+ tableName, "省份");
			List<String> cityname;
			cityname = com.lietu.data.AccessManager.init("select * from "
					+ tableName, "市");
			List<String> sectname;
			sectname = com.lietu.data.AccessManager.init("select * from "
					+ tableName, "區縣");

			Connection conn = AccessManager.getConnection();
			Statement stmt = conn.createStatement();

			for (int i = 0; i < lsname.size(); i++) {
				String result = getAddressString(addname.get(i),
						proname.get(i), cityname.get(i), sectname.get(i));

				String a = "update " + tableName + " set 合併地址='" + result
						+ "' where 名稱='" + lsname.get(i) + "'";
				stmt.executeUpdate(a);
			}
			stmt.close();
			conn.close();

		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	public static String getAddressString(String addname, String proname,
			String cityname, String sectname) {
		String result;

		if (addname.startsWith("中國"))
			addname = addname.replaceFirst("中國", "");

		if (sectname != null && addname.indexOf(sectname) < 0) {
			result = sectname + addname;
		} else {
			result = addname;
		}

		if (cityname != null && result.indexOf(cityname) < 0) {
			result = cityname + result;
		}

		if (proname != null && result.indexOf(proname) < 0) {
			result = proname + result;
		}

		return result;
	}

////	public static int[] getWeights()
//	{
//		int[] weights = new int[38];
//		weights[0] = 12;//;//區域方位詞
//		weights[1] = 58;//8;///關鍵詞
//		weights[2] = 60;//14;行業特徵
//		weights[3] = 26;//47;///功能詞
//		weights[4] = 30;//10;關鍵詞
//		weights[5] = 26;//10;區域方位詞
//		weights[6] = 27;//15;功能詞
//		weights[7] = 6;//區域方位詞
//		weights[8] = 6;//功能詞
//		weights[9] = 2;//1;//
//		
//		weights[10] = 65;//1;國
//		weights[11] = 125;//15;///省
//		weights[12] = 95;//5;///市
//		weights[13] = 75;//1;/// 縣級市
//		weights[14] = 25;//4;鄉
//		weights[15] = 7;//3;村
//		weights[16] = 1;//5;//1;村門牌
//		weights[17] = 9;//5;區
//		weights[18] = 11;//5;///路
//		weights[19] = 1;//道路方位
//		weights[20] = 2;//11;//4;路
//		weights[21] = 1;//1;道路方位
//		weights[22] = 2;//1;///*交叉路口
//		weights[23] = 1;//交叉路口方位
//		weights[24] = 2;//1;///路門牌
//		weights[25] = 1;//1;路門牌
//		weights[26] = 2; // 門牌方位 3
//		weights[27] = 15;//門牌設施
//		weights[28] = 3;//1;//詳細描述
//		weights[29] = 1;//1;子設施
//		weights[30] = 1;//1;
//		weights[31] = 1;//1;
//		weights[32] = 1;//1;
//		weights[33] = 1;//1;
//		weights[34] = 1;///*
//		weights[35] = 6;//25;//電話號碼權重
//		weights[36] = 128;
//		weights[37] = 16;
//		return weights;
//	}
	public static int[] getWeights()
	{
		int[] weights = new int[37];
		weights[0] = 18;//13;//區域方位詞
		weights[1] = 68;//8;///關鍵詞
		weights[2] = 60;//14;行業特徵
		weights[3] = 29;//47;///功能詞
		weights[4] = 30;//10;關鍵詞
		weights[5] = 20;//10;區域方位詞
		weights[6] = 21;//15;功能詞
		weights[7] = 6;//區域方位詞
		weights[8] = 6;//功能詞
		weights[9] = 2;//1;//
		
		weights[10] = 65;//1;國
		weights[11] = 155;//15;///省
		weights[12] = 155;//5;///市
		weights[13] = 85;//1;/// 縣級市
		weights[14] = 55;//4;鄉
		weights[15] = 7;//3;村
		weights[16] = 1;//5;//1;村門牌
		weights[17] = 9;//5;區
		weights[18] = 3;//5;///路
		weights[19] = 1;//道路方位
		weights[20] = 2;//11;//4;路
		weights[21] = 1;//1;道路方位
		weights[22] = 2;//1;///*交叉路口
		weights[23] = 1;//交叉路口方位
		weights[24] = 2;//1;///路門牌
		weights[25] = 1;//1;路門牌
		weights[26] = 2; // 門牌方位 3
		weights[27] = 1;//1;//門牌設施
		weights[28] = 1;//1;//詳細描述
		weights[29] = 1;//1;子設施
		weights[30] = 1;//1;
		weights[31] = 1;//1;
		weights[32] = 1;//1;
		weights[33] = 1;//1;
		weights[34] = 2;///*
		weights[35] = 5;//25;//電話號碼權重
		weights[36] =122;
		
		return weights;
	} 
	
//	public static int[] getWeights()
//	{
//		int[] weights = new int[37];
//		weights[0] = 8;//;//區域方位詞
//		weights[1] = 58;//8;///關鍵詞
//		weights[2] = 60;//14;行業特徵
//		weights[3] = 30;//47;///功能詞
//		weights[4] = 45;//10;關鍵詞
//		weights[5] = 26;//10;區域方位詞
//		weights[6] = 27;//15;功能詞
//		weights[7] = 6;//區域方位詞
//		weights[8] = 6;//功能詞
//		weights[9] = 2;//1;//
//		
//		weights[10] = 65;//1;國
//		weights[11] = 125;//15;///省
//		weights[12] = 95;//5;///市
//		weights[13] = 75;//1;/// 縣級市
//		weights[14] = 25;//4;鄉
//		weights[15] = 7;//3;村
//		weights[16] = 1;//5;//1;村門牌
//		weights[17] = 9;//5;區
//		weights[18] = 11;//5;///路
//		weights[19] = 1;//道路方位
//		weights[20] = 2;//11;//4;路
//		weights[21] = 1;//1;道路方位
//		weights[22] = 2;//1;///*交叉路口
//		weights[23] = 1;//交叉路口方位
//		weights[24] = 2;//1;///路門牌
//		weights[25] = 1;//1;路門牌
//		weights[26] = 2; // 門牌方位 3
//		weights[27] = 10;//門牌設施
//		weights[28] = 3;//1;//詳細描述
//		weights[29] = 1;//1;子設施
//		weights[30] = 1;//1;
//		weights[31] = 1;//1;
//		weights[32] = 1;//1;
//		weights[33] = 1;//1;
//		weights[34] = 1;///*
//		weights[35] = 5;//25;//電話號碼權重
//		weights[36] = 138;
//		//weights[37] = 9;
//		return weights;
//	}
	
//	public static int[] getWeights()
//	{
//		int[] weights = new int[37];
//		weights[0] = 18;//13;//區域方位詞
//		weights[1] = 68;//8;///關鍵詞
//		weights[2] = 60;//14;行業特徵
//		weights[3] = 29;//47;///功能詞
//		weights[4] = 30;//10;關鍵詞
//		weights[5] = 20;//10;區域方位詞
//		weights[6] = 21;//15;功能詞
//		weights[7] = 6;//區域方位詞
//		weights[8] = 6;//功能詞
//		weights[9] = 2;//1;//
//		
//		weights[10] = 65;//1;國
//		weights[11] = 155;//15;///省
//		weights[12] = 155;//5;///市
//		weights[13] = 85;//1;/// 縣級市
//		weights[14] = 55;//4;鄉
//		weights[15] = 7;//3;村
//		weights[16] = 1;//5;//1;村門牌
//		weights[17] = 9;//5;區
//		weights[18] = 6;//5;///路
//		weights[19] = 1;//道路方位
//		weights[20] = 2;//11;//4;路
//		weights[21] = 1;//1;道路方位
//		weights[22] = 2;//1;///*交叉路口
//		weights[23] = 1;//交叉路口方位
//		weights[24] = 2;//1;///路門牌
//		weights[25] = 1;//1;路門牌
//		weights[26] = 2; // 門牌方位 3
//		weights[27] = 1;//1;//門牌設施
//		weights[28] = 1;//1;//詳細描述
//		weights[29] = 1;//1;子設施
//		weights[30] = 1;//1;
//		weights[31] = 1;//1;
//		weights[32] = 1;//1;
//		weights[33] = 1;//1;
//		weights[34] = 2;///*
//		weights[35] = 5;//25;//電話號碼權重
//		weights[36] =122;
//		
//		return weights;
//	} 
	
//	public static int[] getWeights(float value)
//	{
//		int[] weights = new int[37];
//		weights[0] = 24;//13;//區域方位詞
//		weights[1] = 58;//8;///關鍵詞
//		weights[2] = 30;//14;行業特徵
//		weights[3] = 26;//47;///功能詞
//		weights[4] = 30;//10;關鍵詞
//		weights[5] = 20;//10;區域方位詞
//		weights[6] = 21;//15;功能詞
//		weights[7] = 6;//區域方位詞
//		weights[8] = 6;//功能詞
//		weights[9] = 2;//1;//
//		
//		weights[10] = 80;//1;國
//		weights[11] = 75;//15;///省
//		weights[12] = 75;//5;///市
//		weights[13] = 75;//1;/// 縣級市
//		weights[14] = 25;//4;鄉
//		weights[15] = 7;//3;村
//		weights[16] = 1;//5;//1;村門牌
//		weights[17] = 9;//5;區
//		weights[18] = (int)((1-value)*180)+4;//5;///路
//		weights[19] = 1;//道路方位
//		weights[20] = 2;//11;//4;路
//		weights[21] = 1;//1;道路方位
//		weights[22] = 2;//1;///*交叉路口
//		weights[23] = 1;//交叉路口方位
//		weights[24] = 2;//1;///路門牌
//		weights[25] = 1;//1;路門牌
//		weights[26] = 2; // 門牌方位 3
//		weights[27] = 5;//(int)((1-value)*165)+1;//1;//門牌設施
//		weights[28] = 1;//1;//詳細描述
//		weights[29] = 1;//1;子設施
//		weights[30] = 1;//1;
//		weights[31] = 1;//1;
//		weights[32] = 1;//1;
//		weights[33] = 1;//1;
//		weights[34] = 2;///*
//		weights[35] = 5;//25;//電話號碼權重
//		weights[36] =(int)(128*value*value);
//		
//		return weights;
//
//	}
	

	// 對地址、公司名和電話號碼進行拆分，防止在特徵陣列中
	public void setFeatures(String poiA, String addressA, String tel) {
		// if(poiA.equals(addressA))return;
		if (poiA == null)return;
		com.lietu.poi.POI aapoi = com.lietu.orgs.PoiTagger.getPoi(poiA);
		if(aapoi == null)return;
		features[0] = aapoi.place1;
		features[1] = aapoi.keyWord1.replaceAll("七", "7");
		features[2] = aapoi.feature1;
		features[3] = aapoi.function1;
		features[4] = aapoi.keyWord2.replaceAll("七", "7");
		features[5] = aapoi.place2;
		features[6] = aapoi.function2;
		features[7] = aapoi.place3;
		features[8] = aapoi.function3;
		features[9] = aapoi.other;

		com.lietu.address.Address aaaddress = com.lietu.address.AddressTagger.structAddress(addressA);
		features[10] = aaaddress.country;
		features[11] = aaaddress.provinceCode == 0 ? aaaddress.province
				: String.valueOf(aaaddress.provinceCode);
		features[12] = aaaddress.cityCode == 0 ? aaaddress.city : String
				.valueOf(aaaddress.cityCode);
		features[13] = aaaddress.county;
		features[14] = aaaddress.town;
		features[15] = aaaddress.village;
		features[16] = aaaddress.villageNo;
		features[17] = aaaddress.district;
		features[18] = aaaddress.road1;
		features[19] = aaaddress.roadPosition1;
		features[20] = aaaddress.road2;
		features[21] = aaaddress.roadPosition2;
		features[22] = aaaddress.isCrossing ? "1" : "0";
		features[23] = aaaddress.crossingPosition;
		features[24] = aaaddress.roadNo1;
		features[25] = aaaddress.roadNo2;
		features[26] = aaaddress.doorplatePosition;
		features[27] = aaaddress.doorplateFacility;
		features[28] = aaaddress.detailDesc;
		features[29] = aaaddress.childFacility;
		features[30] = aaaddress.indicationFacility1;
		features[31] = aaaddress.indicationPosition1;
		features[32] = aaaddress.indicationFacility2;
		features[33] = aaaddress.indicationPosition2;
		features[34] = aaaddress.other;
		
		TelNumber telNum = TelSeg.getTelNumber(tel);
		features[35] = telNum.tailCode;
		features[36] = poiA;
		
//		 for(int i=0;i<features.length;i++){
//		 	System.out.println("\nfeatures["+i+"]"+features[i]);
//		 }
		
		if (aaaddress.provinceCode == 0 && telNum.proCode != 0) {
			features[11] = String.valueOf(telNum.proCode);
		}
		if (aaaddress.cityCode == 0 && telNum.cityCode != 0) {
			features[12] = String.valueOf(telNum.cityCode);
		}
		if("".equals(aapoi.place1)&&telNum.proCode != 0)
		{
			features[0] = String.valueOf(telNum.cityCode);
		}
		if("".equals(aapoi.place1)&&telNum.cityCode != 0)
		{
			features[0] = String.valueOf(telNum.cityCode);
		}
		if("".equals(aapoi.place1)&&telNum.cityCode == 0&&!"".equals(aapoi.code))
		{
			features[0] = aapoi.code;
		}
		if("".equals(aapoi.place1))
		{
			features[0] = features[10]+features[11]+features[12];
		}
	}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

	/**
	 * 產生hash碼
	 */
	public long getHash(String poiA, String addressA, String tel) {
		// 對地址、公司名和電話號碼進行拆分，防止在特徵陣列中
		setFeatures(poiA, addressA, tel);
		return POISimHash.simHash(features, weights);
	}

	/**
	 * Calculates the similarity hash.
	 */
	public static long getHash(Record data) {
		/* Clear histogram */
		int[] hist = new int[64];

		long addressHash = GeneralHashFunctionLibrary.DJBHash(data.address);
		int weight = 3;
		/* Update histogram */
		for (int c = 0; c < 64; c++)
			hist[c] += (addressHash & (1 << c)) == 0 ? -weight : weight;

		// long provHash = GeneralHashFunctionLibrary.DJBHash(data.province);
		// weight = 5;
		/* Update histogram */
		// for (int c=0; c<64; c++)
		// hist[c] += (provHash & (1 << c)) == 0 ? -weight : weight;
		long poiHash = GeneralHashFunctionLibrary.DJBHash(data.poi);
		weight = 5;
		/* Update histogram */
		for (int c = 0; c < 64; c++)
			hist[c] += (poiHash & (1 << c)) == 0 ? -weight : weight;

		long telHash = GeneralHashFunctionLibrary.DJBHash(data.tel);
		weight = 4;
		/* Update histogram */
		for (int c = 0; c < 64; c++)
			hist[c] += (telHash & (1 << c)) == 0 ? -weight : weight;

		for (int c = 0; c < 64; c++) {
			System.out.print(hist[c] + ":");
		}
	//	System.out.println("");

		/* Calculate a bit vector from the histogram */
		long simHash = 0;
		for (int c = 0; c < 64; c++) {
			long t = ((hist[c] >= 0) ? 1 : 0);
			t <<= c;
			simHash |= t;
		}
		return simHash;
	}

	public static long simHash(String[] features, int[] weights) {
		/* Clear histogram */
		int[] hist = new int[64];
		// SynonymsMap sm = new SynonymsMap();
		for (int i = 0; i < features.length; ++i) {
			// System.out.println(i+":"+features[i]);
			if (features[i] == null || features[i] == "")
				continue;
			// 同義字替換
			// if(sm.getSynonyms(features[i]) != null)
			// features[i] = sm.getSynonyms(features[i]);
			// long addressHash =
			// GeneralHashFunctionLibrary.JSHash(features[i]);

			int weight = weights[i];
			//if (i == 0 || i == 1 || i ==4 || i == 11 || i == 12 || i == 13
					//|| i == 24 || i == 35 || i==36)
			if (i == 0 || i == 1|| i == 2|| i ==3 || i ==4 || i == 11 || i == 12|| i == 13
					|| i==18 || i==36) {
				// long featureHash = MurmurHash.stringHash64(features[i],i);
				long featureHash = JenkinsHash.stringHash(features[i]) + MurmurHash.stringHash64(features[i],i);
				// if(i==1){
				//System.out.println(featureHash+"================="+features[i]);
				// }

				/* Update histogram */
				for (int c = 0; c < 64; c++)
					hist[c] += (featureHash & (1L << c)) == 0 ? -weight
							: weight;
			} else {
				long featureHash = GeneralHashFunctionLibrary
						.JSHash(features[i]);
				//System.out.println(featureHash+"----------------"+features[i]);
				/* Update histogram */
				for (int c = 0; c < 64; c++)
					hist[c] += (featureHash & (1L << c)) == 0 ? -weight
							: weight;
			}
		}

		// for (int c=0; c<64; c++)
		// {
		// System.out.print(hist[c]+":");
		// }
		// System.out.println("");

		/* Calculate a bit vector from the histogram */
		long simHash = 0;
		for (int c = 0; c < 64; c++) {
			long t = ((hist[c] >= 0) ? 1 : 0);
			t <<= c;
			simHash |= t;
		}

		return simHash;
	}

}
