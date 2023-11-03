package com.lietu.classify;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

public class ClassifierParam {
	//�V�m�ɻݭn�ϥΪ��Ѽ�
	public	String m_txtTrainDir;
	public	String m_txtResultDir;
	public	int		m_nFSMode;        //�S�x�������
	public	int     m_nWordSize;      //�S�x�ƥ�
	public	int     m_nSelMode;       //���������٬O�����O�����p��S�x���Ϥ���
	public	int     m_nOpMode;        //�p����v���覡
	public	int     m_nLanguageType;  //��󪺻y��
	public	boolean    m_bStem;          //�O�_�i����z���
	public	int     m_nWeightMode;    //�S�x�[�v����k
	
	//�����ɻݭn�ϥΪ��Ѽ�
	public  int m_nClassifyType;              //0  ��������; 1 �h������
	public  boolean m_bEvaluation;               //�O�_�ݭn����յ��G�i�����
	public  boolean m_bCopyFiles;                //�O�_�N���n���O���ɮ׫����쵲�G�ؿ��U
	public  String m_strTestDir;             //���դ��Ψ�Ҧb���ؿ�
	public  String m_strResultDir;           //���յ��G�Ҧb���ؿ�
	public  String m_strModelFile;
	public  int m_nKNN;                       //KNN��k��k��
	public  int m_nDocFormat;                 //���դ�󪺮榡
	public  double m_dThreshold;              //�h�������ɨϥΪ��H��
	public  int m_nClassifierType;            //������������: -1 ����, 0 �N��KNN, 1 �N��SVM
	
	public String toString()
	{
		StringBuilder strParam = new StringBuilder();
		
		strParam.setLength(0);
		strParam.append("�V�m���ؿ�:\t\t");
		strParam.append(m_txtTrainDir);
		strParam.append("\r\n");
		
		strParam.append("�V�m���G�ؿ�:\t\t");
		strParam.append(m_txtResultDir);
		strParam.append("\r\n");
		
		strParam.append("���v�����k:\t\t");
		if(m_nOpMode==ClassifierParam.nOpDocMode)
			strParam.append("�����έp\r\n");
		else if(m_nOpMode==ClassifierParam.nOpWordMode)
			strParam.append("�����W�έp\r\n");
		else
			strParam.append("����\r\n");
		
		strParam.append("�S�x��ܤ�k:\t\t");
		if(m_nFSMode==ClassifierParam.nFS_IGMode)
			strParam.append("��T�W�q\r\n");
		else if(m_nFSMode==ClassifierParam.nFS_MIMode)
			strParam.append("����T\r\n");
		else if(m_nFSMode==ClassifierParam.nFS_CEMode)
			strParam.append("�����e�i\r\n");
		else if(m_nFSMode==ClassifierParam.nFS_X2Mode)
			strParam.append("X^2�έp\r\n");
		else if(m_nFSMode==ClassifierParam.nFS_WEMode)
			strParam.append("��r�Ҿ��v��\r\n");
		else if(m_nFSMode==ClassifierParam.nFS_XXMode)
			strParam.append("�k�b��T�W�q\r\n");
		else
			strParam.append("����\r\n");

		strParam.append("�S�x��ܤ覡:\t\t");
		if(m_nSelMode==ClassifierParam.nFSM_GolbalMode)
			strParam.append("�������\r\n");
		else if(m_nSelMode==ClassifierParam.nFSM_IndividualModel)
			strParam.append("�����O��W���\r\n");
		else
			strParam.append("����\r\n");

		strParam.append("���y������:\t\t");
		if(m_nLanguageType==ClassifierParam.nLT_Chinese)
			strParam.append("����\r\n");
		else if(m_nLanguageType==ClassifierParam.nLT_English)
		{
			strParam.append("�^��\r\n");
			if(m_bStem)
				strParam.append("�O�_���z���:\t\t�O\r\n");
			else
				strParam.append("�O�_���z���:\t\t�_\r\n");
		}
		else
			strParam.append("����\r\n");

		strParam.append("�S�x�[�v��k:\t\t");
		if(m_nWeightMode==ClassifierParam.nWM_TF_IDF)
			strParam.append("TF*IDF\r\n");
		else if(m_nWeightMode==ClassifierParam.nWM_TF_DIFF)
			strParam.append("TF*�S�x������ƭ�\r\n");
		else if(m_nWeightMode==ClassifierParam.nWM_TF_IDF_DIFF)
			strParam.append("TF*IDF*�S�x������ƭ�\r\n");
		else
			strParam.append("����\r\n");

		String strWordSize;
		strWordSize=String.format("�S�x�Ŷ�����:\t\t%d\r\n",m_nWordSize);
		strParam.append(strWordSize);

		//CString nstrWordSize;
		//int			nDistinctWordNum = theClassifier.m_lstWordList.GetCount();
		//nstrWordSize.Format("�V�m��󶰤������ƪ���r�`��:\t\t%d\r\n",nDistinctWordNum);
		//strParam+=nstrWordSize;

		if(m_nClassifierType==ClassifierParam.nCT_KNN)
			strParam.append("����������: \t\tKNN\r\n");
		else if(m_nClassifierType==ClassifierParam.nCT_SVM)
			strParam.append("����������: \t\tSVM\r\n");
		else
			strParam.append("�Х��}�Ҥ@�Ӥ����ҫ��ɮ�!");
		
		return strParam.toString();
	}
	
	// calculation model
	public static final int nOpDocMode = 0;      // based on document number model
	public static final int nOpWordMode = 1;     // based on word number model
	
	// feature evaluation fuction
	public static final int nFS_IGMode  = 0;      // Information gain feature selection
	public static final int nFS_MIMode  = 1;      // Mutual Informaiton feature selection
	public static final int nFS_CEMode  = 2;      // Cross Entropy for text feature selection
	public static final int nFS_X2Mode  = 3;      // X^2 Statistics feature selection
	public static final int nFS_WEMode  = 4;      // Weight of Evielence for text feature selection
	public static final int nFS_XXMode  = 5;      // Right half of IG
	
	// how to select features
	public static final int nFSM_GolbalMode=0;  // ������
	public static final int nFSM_IndividualModel=1; // ��W��

	// classifier type
	public static final int nCT_Unknown=-1;     // Unknown
	public static final int nCT_KNN=0;         // KNN
	public static final int nCT_SVM=1;         // SVM

	// document language type
	public static final int nLT_Chinese=0;     // Chinese
	public static final int nLT_English=1;     // English

	// document format
	public static final int nDF_Directory=0;   // Directory
	public static final int nDF_Smart=1;       // Smart

	// classify type
	public static final int nFT_Single=0;      // Single Classification
	public static final int nFT_Multi=1;       // Multiple Classification

	// weight mode
	public static final int nWM_TF_IDF=0;      // TF*IDF
	public static final int nWM_TF_DIFF=1;     // TF*DIFF
	public static final int nWM_TF_IDF_DIFF=2; // TF*IDF*DIFF
	
	public ClassifierParam(){
		//�V�m�ɻݭn�ϥΪ��Ѽ�
		m_txtTrainDir = "";
		m_txtResultDir = "";
		m_nFSMode = ClassifierParam.nFS_X2Mode;//ClassifierParam.nFS_IGMode;
		m_nWordSize = 5000;
		m_nSelMode= ClassifierParam.nFSM_GolbalMode;
		m_nOpMode= ClassifierParam.nOpWordMode;//ClassifierParam.nOpDocMode;
		m_nLanguageType= ClassifierParam.nLT_Chinese;
		m_bStem=false;
		m_nWeightMode=0;
		//�����ɻݭn�ϥΪ��Ѽ�
		m_nClassifyType=0;//��������
		m_bEvaluation=true;
		m_bCopyFiles=false;
		m_strTestDir="";
		m_strResultDir="";
		m_strModelFile="model";
		m_nDocFormat=ClassifierParam.nDF_Directory;
		m_nKNN=35;
		m_dThreshold=60;
		m_nClassifierType=ClassifierParam.nCT_SVM;
	}
	
	public void dumpToFile(String strFileName){
		LEDataOutputStream fBinOut = null;
		try {
			fBinOut = new LEDataOutputStream(new FileOutputStream(
					strFileName));
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		try {
			fBinOut.writeGBKString(m_txtTrainDir);
			fBinOut.writeGBKString(m_txtResultDir);
			fBinOut.writeInt(m_nFSMode);
			fBinOut.writeInt(m_nWordSize);
			fBinOut.writeInt(m_nSelMode);
			fBinOut.writeInt(m_nOpMode);
			fBinOut.writeInt(m_nLanguageType);
			fBinOut.writeBoolean(m_bStem);
			fBinOut.writeInt(m_nWeightMode);
			fBinOut.writeInt(m_nClassifyType);
			fBinOut.writeBoolean(m_bEvaluation);
			fBinOut.writeBoolean(m_bCopyFiles);
			fBinOut.writeGBKString(m_strTestDir);
			fBinOut.writeGBKString(m_strResultDir);
			fBinOut.writeGBKString(m_strModelFile);
			fBinOut.writeInt(m_nDocFormat);
			fBinOut.writeInt(m_nKNN);
			fBinOut.writeDouble(m_dThreshold);
			fBinOut.writeInt(m_nClassifierType);
			
			fBinOut.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public boolean getFromFile(String strFileName)
	{
		//System.out.println("ClassifierParam.file:"+strFileName);
		
		LEDataInputStream fBinIn = null;
		
		try
		{
			fBinIn = new LEDataInputStream(new FileInputStream(
				strFileName));
		}catch(Exception e)
		{
			e.printStackTrace();
			System.out.println("�L�k�}���ɮ�"+strFileName+"!") ;
			return false;
		}

		try
		{
			//�V�m�ɻݭn�ϥΪ��Ѽ�
			m_txtTrainDir= fBinIn.readGBKString();			
			m_txtResultDir= fBinIn.readGBKString();			
			m_nFSMode = fBinIn.readInt();
			m_nWordSize = fBinIn.readInt();
			m_nSelMode = fBinIn.readInt();
			m_nOpMode = fBinIn.readInt();
			m_nLanguageType = fBinIn.readInt();
			m_bStem = fBinIn.readBoolean();
			m_nWeightMode = fBinIn.readInt();
			//�����ɻݭn�ϥΪ��Ѽ�
			m_nClassifyType = fBinIn.readInt();
			m_bEvaluation = fBinIn.readBoolean();
			m_bCopyFiles = fBinIn.readBoolean();
			m_strTestDir= fBinIn.readGBKString();
			m_strResultDir= fBinIn.readGBKString();

			m_strModelFile= fBinIn.readGBKString();
			m_nDocFormat = fBinIn.readInt();
			m_nKNN = fBinIn.readInt();
			m_dThreshold= fBinIn.readDouble();
			m_nClassifierType = fBinIn.readInt();
			
			fBinIn.close();
		}
		catch(Exception e)
		{
			System.out.println("�L�kŪ�ɮ�"+strFileName+"!") ;
			return false;
		}
		return true;
	}
}
