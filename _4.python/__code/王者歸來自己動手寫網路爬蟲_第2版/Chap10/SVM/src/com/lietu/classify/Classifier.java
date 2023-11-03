package com.lietu.classify;

import java.io.FileInputStream;

import com.lietu.svmLight.Model;
import com.lietu.svmLight.SVM;

//�����ɻݭn�Ψ쪺�p�������ܼ�
public class Classifier {
	
	// �V�m������O��
	private int m_nClassNum;

	public ClassifierParam m_paramClassifier = new ClassifierParam();
	public WordList m_lstTrainWordList = new WordList();
	// �V�m�ɻݭn�Ψ쪺,�Ψ��x�s�b�S���i��S�x��ܤ��e�V�m�����Ҧ����S�x
	public WordList m_lstWordList = new WordList();
	public CatalogList m_lstTrainCatalogList = new CatalogList();
	public CatalogList m_lstTestCatalogList;
	public SVM docSVM = new SVM();
	Model[] models;

	// �����ҫ��ɮ��Y�лx��
	private static int dwModelFileID = 0xFFEFFFFF;

	public int SVMCategory(String content) {
		/*
		 * java.util.Calendar now = java.util.Calendar.getInstance(); if(
		 * (now.get(java.util.Calendar.YEAR) >2007) ) {
		 * System.err.print("�藍�_�A�եδ��w��"); System.exit(-1); }
		 */
		com.lietu.seg.result.Tagger.segSZ = false;

		WeightNode[] weightNode=new WeightNode[m_lstTrainWordList.getCount()];
		
		int nCataID = -1;
		double[] m_pResults = SVMClassify(content, weightNode);
		if (m_pResults!=null) {
			nCataID = singleCategory(m_pResults);
		}
		return nCataID;
	}

	public Classifier(String strFileName) {
		try {
			LEDataInputStream fIn = new LEDataInputStream(new FileInputStream(
					strFileName));
			(new java.io.File(strFileName)).isFile();
			// long startTime=System.currentTimeMillis();
			// System.out.println("���b�}�Ҥ����ҫ��ɮסA�еy��...");
			String str = null;
			String strPath;
			int dwFileID;

			// Ū�J�ɮ׮榡�лx��
			strPath = strFileName.substring(0, strFileName.lastIndexOf('/'));
			dwFileID = fIn.readInt();

			if (dwFileID != dwModelFileID) {
				fIn.close();
				// System.out.println(dwModelFileID);
				System.out.println("�����ҫ��ɮת��榡�����T!");
			}

			str = fIn.readString();
			if (!m_paramClassifier.getFromFile(strPath + "/" + str)) {
				System.out.println("�L�k�}�ҰV�m�Ѽ��ɮ�" + str + "!");
			}
			// System.out.println(m_paramClassifier);
			m_paramClassifier.m_txtResultDir = strPath;

			if (m_paramClassifier.m_nClassifierType == ClassifierParam.nCT_KNN) {
				str = fIn.readString();
				System.out.println(str);
				m_lstTrainWordList.initWordList();
				if (!m_lstTrainWordList.getFromFile(strPath + "/" + str)) {
					System.out.println("�L�k�}�үS�x�����ɮ�" + str + "!");
				}

				str = fIn.readString();
				System.out.println(str);
				
				try
				{
					m_lstTrainCatalogList = new CatalogList(strPath + "/" + str);
				}
				catch (Exception e)
				{
					System.out.println("�L�k�}�ҰV�m���C���ɮ�" + str + "!");
				}
			} else {
				str = fIn.readString();
				// System.out.println(str);
				m_lstTrainWordList.initWordList();
				if (!m_lstTrainWordList.getFromFile(strPath + "/" + str)) {
					System.out.println("�L�k�}�үS�x�����ɮ�" + str + "!");
					// return false;
				}
				// ���SVM�����_�ӻ�m_lstTrainCatalogList���S��
				// ���BŪ�J���u�O���F�bCLeftViw����ܬY�ǲέp��T�ɨϥ�
				str = fIn.readString();
				// System.out.println(str);

				try
				{
					m_lstTrainCatalogList = new CatalogList(strPath + "/" + str);
				}
				catch (Exception e)
				{
					System.out.println("�L�k�}�ҰV�m���C���ɮ�" + str + "!");
				}

				str = fIn.readString();
				// System.out.println(str);
				if (!docSVM.param.GetFromFile(strPath + "/" + str)) {
					System.out.println("�L�k�}��SVM�V�m�Ѽ��ɮ�" + str + "!");
					// return false;
				}
				docSVM.param.trainfile = strPath + "/train.txt";
				docSVM.param.resultpath = strPath;
			}
			fIn.close();
			
			m_nClassNum = m_lstTrainCatalogList.getCataNum();
			
			// �V�m��󪺭Ӽ�		
			int m_lDocNum = m_lstTrainCatalogList.getDocNum();
			if(m_lDocNum<=0)
				throw new Exception("train doc num cannot be "+m_lDocNum);
			
			if (m_paramClassifier.m_nKNN > m_lDocNum)
				m_paramClassifier.m_nKNN = m_lDocNum;
			
			if (m_paramClassifier.m_nClassifierType == ClassifierParam.nCT_SVM) {
				models = new Model[m_nClassNum];

				for (int i = 0; i < m_nClassNum; i++) {
					// System.out.println("m_paramClassifier.m_strModelFile:"+
					// m_paramClassifier.m_strModelFile);
					String modelfile = m_paramClassifier.m_txtResultDir + "/"
							+ m_paramClassifier.m_strModelFile + (i + 1) + ".mdl";
					docSVM.param.modelfile = modelfile;

					models[i] = new Model(modelfile);
				}
			}
			// long totalTime=System.currentTimeMillis()-startTime;
			// System.out.println(("�����ҫ��ɮפw�g�}�ҡA�Ӯ�")+totalTime/1000+"��\r\n");
			// System.out.println(m_paramClassifier);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	// �o���󪺩������OnMaxCatID
	private int singleCategory(double[] simRatio) {
		// System.out.println("enter SingleCategory");
		
		int nCataID = 0;
		double dMaxNum = simRatio[nCataID];
		// System.out.println("SimRatio"+0+":"+pSimRatio[0]+"\t"+
		// m_lstTrainCatalogList.GetCataName(0));
		// System.out.println("ClassNum:"+m_nClassNum);
		for (int i = 1; i < m_nClassNum; i++) {
			// System.out.println("SimRatio"+i+":"+pSimRatio[i]+"\t"+
			// m_lstTrainCatalogList.GetCataName(i));
			if (simRatio[i] > dMaxNum) {
				dMaxNum = simRatio[i];
				nCataID = i;
			}
		}
		//docNode.m_nCataID = nCataID;
		return nCataID;
	}

	public String getCategoryName(String content) {
		int id = SVMCategory(content);

		String className = null;
		if (id >= 0) {
			className = m_lstTrainCatalogList.getCataName(id);
		}
		return className;
	}

	public double[] SVMClassify(String content,
			WeightNode[] weightNode) {
		DocNode docNode = new DocNode();
		
		// System.out.println("enter SVMClassify");
		int nCount = 0;
		if (m_paramClassifier.m_nLanguageType == ClassifierParam.nLT_Chinese)
			nCount = docNode.scanChineseStringWithDict(content,
					m_lstTrainWordList,weightNode);
		else
			nCount = docNode.scanEnglishStringWithDict(content,
					m_lstTrainWordList, m_paramClassifier.m_bStem,weightNode);

		if (nCount > 0) {
			com.lietu.svmLight.Doc doc = new com.lietu.svmLight.Doc();
			docNode.genDocVector(doc,weightNode);
			
			//���P�C�����O���ۦ���
			double[] simRatio = new double[m_nClassNum];

			for (int i = 0; i < m_nClassNum; i++) {
				if (models == null) {
					System.out.println("models[i] is null");
					return null;
				}

				simRatio[i] = docSVM.svm_classify(doc, models[i]);
			}
			return simRatio;
		}

		return null;
	}
}
