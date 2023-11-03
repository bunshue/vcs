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
	
	public static void evaluate(int[] weights, int[] tempweit)// �N�Ȧs�b�s��}�C�����v���Ƚ��weights��
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

	public static void evaluateA(int[] weights, int[] tempweit)// �N�Ȧs�b�s��}�C�����v���Ƚ��weights��
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

	// �X�֦a�}�Apath�ѼƥΩ���waccess��ƪ��x�s����m
	public static void mergeAddress(String tableName, String path) {
		try {
			List<String> lsname;
			lsname = com.lietu.data.AccessManager.init("select * from "
					+ tableName, "�W��");
			List<String> addname;
			addname = com.lietu.data.AccessManager.init("select * from "
					+ tableName, "�a�}");
			List<String> proname;
			proname = com.lietu.data.AccessManager.init("select * from "
					+ tableName, "�٥�");
			List<String> cityname;
			cityname = com.lietu.data.AccessManager.init("select * from "
					+ tableName, "��");
			List<String> sectname;
			sectname = com.lietu.data.AccessManager.init("select * from "
					+ tableName, "�Ͽ�");

			Connection conn = AccessManager.getConnection();
			Statement stmt = conn.createStatement();

			for (int i = 0; i < lsname.size(); i++) {
				String result = getAddressString(addname.get(i),
						proname.get(i), cityname.get(i), sectname.get(i));

				String a = "update " + tableName + " set �X�֦a�}='" + result
						+ "' where �W��='" + lsname.get(i) + "'";
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

		if (addname.startsWith("����"))
			addname = addname.replaceFirst("����", "");

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
//		weights[0] = 12;//;//�ϰ����
//		weights[1] = 58;//8;///�����
//		weights[2] = 60;//14;��~�S�x
//		weights[3] = 26;//47;///�\���
//		weights[4] = 30;//10;�����
//		weights[5] = 26;//10;�ϰ����
//		weights[6] = 27;//15;�\���
//		weights[7] = 6;//�ϰ����
//		weights[8] = 6;//�\���
//		weights[9] = 2;//1;//
//		
//		weights[10] = 65;//1;��
//		weights[11] = 125;//15;///��
//		weights[12] = 95;//5;///��
//		weights[13] = 75;//1;/// ���ť�
//		weights[14] = 25;//4;�m
//		weights[15] = 7;//3;��
//		weights[16] = 1;//5;//1;�����P
//		weights[17] = 9;//5;��
//		weights[18] = 11;//5;///��
//		weights[19] = 1;//�D�����
//		weights[20] = 2;//11;//4;��
//		weights[21] = 1;//1;�D�����
//		weights[22] = 2;//1;///*��e���f
//		weights[23] = 1;//��e���f���
//		weights[24] = 2;//1;///�����P
//		weights[25] = 1;//1;�����P
//		weights[26] = 2; // ���P��� 3
//		weights[27] = 15;//���P�]�I
//		weights[28] = 3;//1;//�ԲӴy�z
//		weights[29] = 1;//1;�l�]�I
//		weights[30] = 1;//1;
//		weights[31] = 1;//1;
//		weights[32] = 1;//1;
//		weights[33] = 1;//1;
//		weights[34] = 1;///*
//		weights[35] = 6;//25;//�q�ܸ��X�v��
//		weights[36] = 128;
//		weights[37] = 16;
//		return weights;
//	}
	public static int[] getWeights()
	{
		int[] weights = new int[37];
		weights[0] = 18;//13;//�ϰ����
		weights[1] = 68;//8;///�����
		weights[2] = 60;//14;��~�S�x
		weights[3] = 29;//47;///�\���
		weights[4] = 30;//10;�����
		weights[5] = 20;//10;�ϰ����
		weights[6] = 21;//15;�\���
		weights[7] = 6;//�ϰ����
		weights[8] = 6;//�\���
		weights[9] = 2;//1;//
		
		weights[10] = 65;//1;��
		weights[11] = 155;//15;///��
		weights[12] = 155;//5;///��
		weights[13] = 85;//1;/// ���ť�
		weights[14] = 55;//4;�m
		weights[15] = 7;//3;��
		weights[16] = 1;//5;//1;�����P
		weights[17] = 9;//5;��
		weights[18] = 3;//5;///��
		weights[19] = 1;//�D�����
		weights[20] = 2;//11;//4;��
		weights[21] = 1;//1;�D�����
		weights[22] = 2;//1;///*��e���f
		weights[23] = 1;//��e���f���
		weights[24] = 2;//1;///�����P
		weights[25] = 1;//1;�����P
		weights[26] = 2; // ���P��� 3
		weights[27] = 1;//1;//���P�]�I
		weights[28] = 1;//1;//�ԲӴy�z
		weights[29] = 1;//1;�l�]�I
		weights[30] = 1;//1;
		weights[31] = 1;//1;
		weights[32] = 1;//1;
		weights[33] = 1;//1;
		weights[34] = 2;///*
		weights[35] = 5;//25;//�q�ܸ��X�v��
		weights[36] =122;
		
		return weights;
	} 
	
//	public static int[] getWeights()
//	{
//		int[] weights = new int[37];
//		weights[0] = 8;//;//�ϰ����
//		weights[1] = 58;//8;///�����
//		weights[2] = 60;//14;��~�S�x
//		weights[3] = 30;//47;///�\���
//		weights[4] = 45;//10;�����
//		weights[5] = 26;//10;�ϰ����
//		weights[6] = 27;//15;�\���
//		weights[7] = 6;//�ϰ����
//		weights[8] = 6;//�\���
//		weights[9] = 2;//1;//
//		
//		weights[10] = 65;//1;��
//		weights[11] = 125;//15;///��
//		weights[12] = 95;//5;///��
//		weights[13] = 75;//1;/// ���ť�
//		weights[14] = 25;//4;�m
//		weights[15] = 7;//3;��
//		weights[16] = 1;//5;//1;�����P
//		weights[17] = 9;//5;��
//		weights[18] = 11;//5;///��
//		weights[19] = 1;//�D�����
//		weights[20] = 2;//11;//4;��
//		weights[21] = 1;//1;�D�����
//		weights[22] = 2;//1;///*��e���f
//		weights[23] = 1;//��e���f���
//		weights[24] = 2;//1;///�����P
//		weights[25] = 1;//1;�����P
//		weights[26] = 2; // ���P��� 3
//		weights[27] = 10;//���P�]�I
//		weights[28] = 3;//1;//�ԲӴy�z
//		weights[29] = 1;//1;�l�]�I
//		weights[30] = 1;//1;
//		weights[31] = 1;//1;
//		weights[32] = 1;//1;
//		weights[33] = 1;//1;
//		weights[34] = 1;///*
//		weights[35] = 5;//25;//�q�ܸ��X�v��
//		weights[36] = 138;
//		//weights[37] = 9;
//		return weights;
//	}
	
//	public static int[] getWeights()
//	{
//		int[] weights = new int[37];
//		weights[0] = 18;//13;//�ϰ����
//		weights[1] = 68;//8;///�����
//		weights[2] = 60;//14;��~�S�x
//		weights[3] = 29;//47;///�\���
//		weights[4] = 30;//10;�����
//		weights[5] = 20;//10;�ϰ����
//		weights[6] = 21;//15;�\���
//		weights[7] = 6;//�ϰ����
//		weights[8] = 6;//�\���
//		weights[9] = 2;//1;//
//		
//		weights[10] = 65;//1;��
//		weights[11] = 155;//15;///��
//		weights[12] = 155;//5;///��
//		weights[13] = 85;//1;/// ���ť�
//		weights[14] = 55;//4;�m
//		weights[15] = 7;//3;��
//		weights[16] = 1;//5;//1;�����P
//		weights[17] = 9;//5;��
//		weights[18] = 6;//5;///��
//		weights[19] = 1;//�D�����
//		weights[20] = 2;//11;//4;��
//		weights[21] = 1;//1;�D�����
//		weights[22] = 2;//1;///*��e���f
//		weights[23] = 1;//��e���f���
//		weights[24] = 2;//1;///�����P
//		weights[25] = 1;//1;�����P
//		weights[26] = 2; // ���P��� 3
//		weights[27] = 1;//1;//���P�]�I
//		weights[28] = 1;//1;//�ԲӴy�z
//		weights[29] = 1;//1;�l�]�I
//		weights[30] = 1;//1;
//		weights[31] = 1;//1;
//		weights[32] = 1;//1;
//		weights[33] = 1;//1;
//		weights[34] = 2;///*
//		weights[35] = 5;//25;//�q�ܸ��X�v��
//		weights[36] =122;
//		
//		return weights;
//	} 
	
//	public static int[] getWeights(float value)
//	{
//		int[] weights = new int[37];
//		weights[0] = 24;//13;//�ϰ����
//		weights[1] = 58;//8;///�����
//		weights[2] = 30;//14;��~�S�x
//		weights[3] = 26;//47;///�\���
//		weights[4] = 30;//10;�����
//		weights[5] = 20;//10;�ϰ����
//		weights[6] = 21;//15;�\���
//		weights[7] = 6;//�ϰ����
//		weights[8] = 6;//�\���
//		weights[9] = 2;//1;//
//		
//		weights[10] = 80;//1;��
//		weights[11] = 75;//15;///��
//		weights[12] = 75;//5;///��
//		weights[13] = 75;//1;/// ���ť�
//		weights[14] = 25;//4;�m
//		weights[15] = 7;//3;��
//		weights[16] = 1;//5;//1;�����P
//		weights[17] = 9;//5;��
//		weights[18] = (int)((1-value)*180)+4;//5;///��
//		weights[19] = 1;//�D�����
//		weights[20] = 2;//11;//4;��
//		weights[21] = 1;//1;�D�����
//		weights[22] = 2;//1;///*��e���f
//		weights[23] = 1;//��e���f���
//		weights[24] = 2;//1;///�����P
//		weights[25] = 1;//1;�����P
//		weights[26] = 2; // ���P��� 3
//		weights[27] = 5;//(int)((1-value)*165)+1;//1;//���P�]�I
//		weights[28] = 1;//1;//�ԲӴy�z
//		weights[29] = 1;//1;�l�]�I
//		weights[30] = 1;//1;
//		weights[31] = 1;//1;
//		weights[32] = 1;//1;
//		weights[33] = 1;//1;
//		weights[34] = 2;///*
//		weights[35] = 5;//25;//�q�ܸ��X�v��
//		weights[36] =(int)(128*value*value);
//		
//		return weights;
//
//	}
	

	// ��a�}�B���q�W�M�q�ܸ��X�i�����A����b�S�x�}�C��
	public void setFeatures(String poiA, String addressA, String tel) {
		// if(poiA.equals(addressA))return;
		if (poiA == null)return;
		com.lietu.poi.POI aapoi = com.lietu.orgs.PoiTagger.getPoi(poiA);
		if(aapoi == null)return;
		features[0] = aapoi.place1;
		features[1] = aapoi.keyWord1.replaceAll("�C", "7");
		features[2] = aapoi.feature1;
		features[3] = aapoi.function1;
		features[4] = aapoi.keyWord2.replaceAll("�C", "7");
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
	 * ����hash�X
	 */
	public long getHash(String poiA, String addressA, String tel) {
		// ��a�}�B���q�W�M�q�ܸ��X�i�����A����b�S�x�}�C��
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
			// �P�q�r����
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
