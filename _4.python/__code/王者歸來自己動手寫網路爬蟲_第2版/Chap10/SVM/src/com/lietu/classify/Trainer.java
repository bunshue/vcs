package com.lietu.classify;

import java.io.File;
import java.io.FileOutputStream;
import java.util.Arrays;
import java.util.Map.Entry;

import com.lietu.svmLight.Model;
import com.lietu.svmLight.SVM;

public class Trainer {

	public static class SortType implements Comparable<SortType> {
		String word;
		double dWeight;
		WordNode pclsWordNode;
		
		public String toString()
		{
			return "word:"+word+ " dWeight:"+dWeight;
		}

		@Override
		public int compareTo(SortType o) {
			if (this.dWeight > o.dWeight)
				return -1;
			else if (this.dWeight < o.dWeight)
				return 1;
			return 0;
		}
	}

	public ClassifierParam m_paramClassifier = new ClassifierParam();
	
	public CatalogList m_lstTrainCatalogList = new CatalogList();
	public CatalogList m_lstTestCatalogList;
	public SVM docSVM = new SVM();
	Model[] models;

	// 分類模型檔案頭標誌符
	private static int dwModelFileID = 0xFFEFFFFF;

	public Trainer() {
	}

	public void setTrainSet(String path) {
		m_paramClassifier.m_txtTrainDir = path;
	}

	public void setModel(String path) {
		m_paramClassifier.m_txtResultDir = path;
	}

	// 參數bGenDic=false代表無需重新掃瞄文件得到訓練文件集中所有特徵,一般在階層分類時使用
	// 參數nType用來決定分類模型的類別,nType=0代表KNN分類器,nType=1代表SVM分類器
	public boolean train(int featherSelectionAlgorithmn) throws Exception {
		long startTime = System.currentTimeMillis();
		long totalTime;
		
		// 產生所有候選特徵項，將其儲存在m_lstWordList中
		WordList m_lstWordList = genDic();

		if (m_lstWordList == null)
			return false;
		int distinctWordNum = m_lstWordList.getCount();
		if (distinctWordNum == 0)
			return false;
		
		System.out.println("訓練文件集中不重複的單字總數:" + distinctWordNum);
		if (m_lstTrainCatalogList.getCataNum() == 0)
			return false;

		// 為特徵項列表m_lstWordList中的每個特徵加權
		System.out.println("開始計算候選特徵集中每個特徵的類別區分度，請稍候...");
		startTime = System.currentTimeMillis();
		featherWeight(m_lstWordList, featherSelectionAlgorithmn);
		totalTime = System.currentTimeMillis() - startTime;
		System.out.println("特徵區分度計算結束，耗時" + totalTime / 1000 + "秒");

		
		System.out.println("開始進行特徵選擇，請稍候...");
		startTime = System.currentTimeMillis();

		// 從特徵項列表m_lstWordList中選出最優特徵
		WordList m_lstTrainWordList = featherSelection(m_lstWordList);
		if(m_lstTrainWordList == null)
		{
			throw new Exception("error WordList cannot be null");
		}
		
		m_lstTrainWordList.indexWord();
		totalTime = System.currentTimeMillis() - startTime;
		System.out.println("特徵選擇結束，耗時" + totalTime / 1000 + "秒");

		System.out.println("開始產生文件向量，請稍候...");
		startTime = System.currentTimeMillis();
		genModel(m_lstTrainWordList);
		totalTime = System.currentTimeMillis() - startTime;
		System.out.println("文件向量產生結束，耗時" + totalTime / 1000 + "秒");

		System.out.println("開始儲存分類模型，請稍候...");
		startTime = System.currentTimeMillis();
		File modelDir = new File(m_paramClassifier.m_txtResultDir);
		if (!modelDir.exists()) {
			modelDir.mkdir();
		}
		WriteModel(m_paramClassifier.m_txtResultDir + "\\model.prj",m_lstTrainWordList);
		totalTime = System.currentTimeMillis() - startTime;
		System.out.println("儲存分類模型結束，耗時" + totalTime / 1000 + "秒");

		// 訓練SVM分類器必須在儲存訓練文件的文件向量後進行
		System.out.println("開始訓練SVM，請稍候...");
		m_lstTrainCatalogList.initCatalogList2(); // 刪除文件向量所佔用的空間
		startTime = System.currentTimeMillis();
		trainSVM();
		totalTime = System.currentTimeMillis() - startTime;
		System.out.println("SVM分類器訓練結束，耗時" + totalTime / 1000 + "秒");

		// 為分類做好準備,否則不能進行分類
		// Prepare();
		return true;
	}

	// generate original dictionary (the largest one)
	// form train files
	public WordList genDic() {
		// 訓練時需要用到的,用來儲存在沒有進行特徵選擇之前訓練集中所有的特徵
		WordList m_lstWordList = new WordList();
		
		long startTime;
		long totalTime;

		startTime = System.currentTimeMillis();
		System.out.println("開始掃瞄訓練文件，請稍候...");
		if (m_lstTrainCatalogList.buildLib(m_paramClassifier.m_txtTrainDir) <= 0) {
			System.out.println("訓練文件的總數為0!");
			return null;
		}

		int nCount;
		int nCataNum = m_lstTrainCatalogList.getCataNum();
		for (CatalogNode catalogNode : m_lstTrainCatalogList.catalogList) {
			for (DocNode docnode : catalogNode.docList) {
				if (m_paramClassifier.m_nLanguageType == ClassifierParam.nLT_Chinese) {
					// System.out.println("掃瞄中文文件"+docnode.m_strDocName);

					nCount = docnode.scanChinese(catalogNode.m_strDirName,
							m_lstWordList, nCataNum, catalogNode.m_idxCata);
				} else {
					nCount = docnode.scanEnglish(catalogNode.m_strDirName,
							m_lstWordList, nCataNum, catalogNode.m_idxCata,
							m_paramClassifier.m_bStem);
				}
				if (nCount == 0) {
					// System.out.println("檔案"+catalognode.m_strDirName+"/"+
					// docnode.m_strDocName+"無內容!");
					continue;
				} else if (nCount < 0) {
					System.out.println("檔案" + catalogNode.m_strDirName + "/"
							+ docnode.m_strDocName + "無法開啟!");
					continue;
				}
				catalogNode.m_lTotalWordNum += nCount;// information collection
														// point
			}
		}

		totalTime = System.currentTimeMillis() - startTime;
		System.out.println("掃瞄訓練文件結束，耗時" + totalTime / 1000 + "秒");
		return m_lstWordList;
	}

	public void trainSVM() {
		long tmStart;
		long tmSpan;

		m_paramClassifier.m_strModelFile = "model";
		for (int i = 1; i <= m_lstTrainCatalogList.getCataNum(); i++) {
			tmStart = System.currentTimeMillis();
			System.out.println("正在訓練第" + i + "個SVM分類器，請稍侯...");
			docSVM.param.trainfile = m_paramClassifier.m_txtResultDir
					+ "/train.txt";
			docSVM.param.modelfile = (m_paramClassifier.m_txtResultDir + "/"
					+ m_paramClassifier.m_strModelFile + i + ".mdl");
			docSVM.svm_learn_main(i);
			tmSpan = System.currentTimeMillis() - tmStart;
			System.out.println("第" + i + "個SVM分類器訓練完成，耗時" + tmSpan + "!");
		}
	}

	// Give m_lstWordList & m_lstTrainCatalogList
	// Output the present vector of each document;
	// bFlag=false 階層分類別的時候使用
	public void genModel(WordList m_lstTrainWordList) {
		int m_nAllocTempLen = m_lstTrainWordList.getCount();
		
		//System.out.println("AllocTempBuffer:"+nLen);
		WeightNode[] m_pTemp=new WeightNode[m_nAllocTempLen];
		
		// for each catalog
		for (CatalogNode cataNode : m_lstTrainCatalogList.catalogList) 
		{
			// 取類列表中的每一個類
			// CCatalogNode& cataNode = m_lstTrainCatalogList.GetNext(pos_cata);
			// POSITION pos_doc = cataNode.GetFirstPosition();
			for (DocNode docNode : cataNode.docList) {
				if (m_paramClassifier.m_nLanguageType == ClassifierParam.nLT_Chinese)
				{
					docNode.scanChineseWithDict(cataNode.m_strDirName,
							m_lstTrainWordList,m_pTemp);
				}
				else
				{
					docNode.scanEnglishWithDict(cataNode.m_strDirName,
							m_lstTrainWordList, m_paramClassifier.m_bStem,
							m_pTemp);
				}
				docNode.genDocVector(m_pTemp);
				// System.out.println("產生文件"+docNode.m_strDocName+"的文件向量");
			}
		}
	}

	public void featherWeight(WordList wordList, int featherSelectionMethod) {
		
		m_paramClassifier.m_nFSMode = featherSelectionMethod;
		//----------------------------------------------------------------------
		// --------
		// based on document number model
		long N; // 總體文件數;
		int N_c; // C類別的文件數
		long N_ft; // 含有ft的文件數
		long N_c_ft; // C類中含有ft的文件數
		//----------------------------------------------------------------------
		// --------
		// based on word number model
		long N_W; // 總體詞數 m_lWordNum;
		long N_W_C; // C類詞數 CCatalogNode.m_lTotalWordNum;
		long N_W_f_t; // f_t出現的總次數
		long N_W_C_f_t;// C類中f_t出現的次數
		//----------------------------------------------------------------------
		// --------
		double P_c_ft, P_c_n_ft, P_n_c_ft, P_n_c_n_ft;
		double P_c, P_n_c;
		double P_ft, P_n_ft;

		// calculate the weight of each word to all catalog
		N = m_lstTrainCatalogList.getDocNum(); //文件總數
		N_W = wordList.getWordNum(); // 總體詞數


		for (Entry<String, WordNode> e : wordList.m_lstWordList.entrySet()) // for
																			// each
																			// word
		{
			WordNode wordNode = e.getValue();
			wordNode.m_dWeight = 0;

			N_ft = wordNode.getDocNum();//文件總數
			//System.out.println("特徵:"+e.getKey()+"...N_ft "+N_ft);
			N_W_f_t = wordNode.getWordNum();//詞總數
			int nCataCount = 0;
			for (CatalogNode cataNode : m_lstTrainCatalogList.catalogList)
			{
				N_c = cataNode.getDocNum();
				//System.out.println("特徵:"+e.getKey()+"...N_c "+N_c);
				N_W_C = cataNode.m_lTotalWordNum;
				N_c_ft = wordNode.getCataDocNum(cataNode.m_idxCata);
				N_W_C_f_t = wordNode.getCataWordNum(cataNode.m_idxCata);
				// calculation model 如果計算機率的方式是基於詞頻統計
				if (m_paramClassifier.m_nOpMode == ClassifierParam.nOpWordMode) {
					P_c = 1.0 * N_W_C / N_W;
					P_ft = 1.0 * N_W_f_t / N_W;
					P_c_ft = 1.0 * N_W_C_f_t / N_W;
				} else // if(m_paramClassifier.m_nOpMode==CClassifierParam::
						// nOpDocMode)如果計算機率的方式是基於文件的統計
				{
					P_c = 1.0 * N_c / N;
					P_ft = 1.0 * N_ft / N;
					P_c_ft = 1.0 * N_c_ft / N;
				}

				P_n_c = 1 - P_c;
				P_n_ft = 1 - P_ft;
				P_n_c_ft = P_ft - P_c_ft;
				P_c_n_ft = P_c - P_c_ft;
				P_n_c_n_ft = P_n_ft - P_c_n_ft;

				wordNode.catWeight[nCataCount] = 0;
				// feature selection model
				if (m_paramClassifier.m_nFSMode == ClassifierParam.nFS_XXMode) {
					// Right half of IG
					if ((Math.abs(P_c * P_n_ft) > Double.MIN_VALUE)
							&& (Math.abs(P_c_n_ft) > Double.MIN_VALUE)) {
						wordNode.catWeight[nCataCount] += P_c_n_ft
								* Math.log(P_c_n_ft / (P_c * P_n_ft));
					}
				} else if (m_paramClassifier.m_nFSMode == ClassifierParam.nFS_MIMode) {
					// Mutual Informaiton feature selection
					if ((Math.abs(P_c * P_ft) > Double.MIN_VALUE)
							&& (Math.abs(P_c_ft) > Double.MIN_VALUE)) {
						wordNode.catWeight[nCataCount] += P_c
								* Math.log(P_c_ft / (P_c * P_ft));
					}
				} else if (m_paramClassifier.m_nFSMode == ClassifierParam.nFS_CEMode) {
					// Cross Entropy for text feature selection
					if ((Math.abs(P_c * P_ft) > Double.MIN_VALUE)
							&& (Math.abs(P_c_ft) > Double.MIN_VALUE)) {
						wordNode.catWeight[nCataCount] += P_c_ft
								* Math.log(P_c_ft / (P_c * P_ft));
					}
				} else if (m_paramClassifier.m_nFSMode == ClassifierParam.nFS_X2Mode) {
					// X^2 Statistics feature selection
					if ((Math.abs(P_n_c * P_ft * P_n_ft) > Double.MIN_VALUE)) {
						wordNode.catWeight[nCataCount] += (P_c_ft
								* P_n_c_n_ft - P_n_c_ft * P_c_n_ft)
								* (P_c_ft * P_n_c_n_ft - P_n_c_ft * P_c_n_ft)
								/ (P_ft * P_n_c * P_n_ft);
					}
				} else if (m_paramClassifier.m_nFSMode == ClassifierParam.nFS_WEMode) {
					// Weight of Evielence for text feature selection
					double odds_c_ft;
					double odds_c;
					double P_c_inv_ft = P_c_ft / P_ft;

					if (Math.abs(P_c_inv_ft) < Double.MIN_VALUE)
						odds_c_ft = 1.0 / (N * N - 1);
					else if (Math.abs(P_c_inv_ft - 1) < Double.MIN_VALUE)
						odds_c_ft = N * N - 1;
					else
						odds_c_ft = P_c_inv_ft / (1.0 - P_c_inv_ft);

					if (Math.abs(P_c) < Double.MIN_VALUE)
						odds_c = 1.0 / (N * N - 1);
					else if (Math.abs(P_c - 1) < Double.MIN_VALUE)
						odds_c = N * N - 1;
					else
						odds_c = P_c / (1.0 - P_c);
					if (Math.abs(odds_c) > Double.MIN_VALUE
							&& Math.abs(odds_c_ft) > Double.MIN_VALUE)
						wordNode.catWeight[nCataCount] += P_c * P_ft
								* Math.abs(Math.log(odds_c_ft / odds_c));
				} else // if(m_paramClassifier.m_nFSMode==CClassifierParam::
						// nFS_IGMode)
				{
					// Information gain feature selection
					if ((Math.abs(P_c * P_n_ft) > Double.MIN_VALUE)
							&& (Math.abs(P_c_n_ft) > Double.MIN_VALUE)) {
						wordNode.catWeight[nCataCount] += P_c_n_ft
								* Math.log(P_c_n_ft / (P_c * P_n_ft));
					}
					if ((Math.abs(P_c * P_ft) > Double.MIN_VALUE)
							&& (Math.abs(P_c_ft) > Double.MIN_VALUE)) {
						wordNode.catWeight[nCataCount] += P_c_ft
								* Math.log(P_c_ft / (P_c * P_ft));
					}
				}
				wordNode.m_dWeight += wordNode.catWeight[nCataCount];
				nCataCount++;
			}
			// ASSERT(nCataCount==nTotalCata);
		}
	}

	// 從m_lstWordList選出最優特徵子集,存到dstWordList中
	public WordList featherSelection(WordList m_lstWordList) {
		if (m_lstWordList.getCount() <= 0)
			return null;
		
		WordList dstWordList = new WordList();
		m_lstWordList.indexWord();

		SortType[] psSortBuf;
		int nDistinctWordNum = m_lstWordList.getCount();

		// the distinct number of the word
		psSortBuf = new SortType[nDistinctWordNum];
		for (int i = 0; i < nDistinctWordNum; ++i) {
			psSortBuf[i] = new SortType();
		}
		long lDocNum = m_lstTrainCatalogList.getDocNum();
		for (int i = 0; i < nDistinctWordNum; i++) {
			psSortBuf[i].pclsWordNode = null;
			psSortBuf[i].dWeight = 0;
		}
		
		// total selecting
		System.out.println("FeatherSelection GolbalMode");
		genSortBuf(m_lstWordList, psSortBuf);// -1 mean sum all catalog
		Arrays.sort(psSortBuf);

		int nSelectWordNum = m_paramClassifier.m_nWordSize;
		if (nSelectWordNum > nDistinctWordNum)
			nSelectWordNum = nDistinctWordNum;

		for (int i = 0; i < nSelectWordNum; i++) {
			WordNode wordNode = new WordNode();
			if (m_paramClassifier.m_nWeightMode == ClassifierParam.nWM_TF_IDF)
				psSortBuf[i].pclsWordNode.computeWeight(lDocNum);
			else if (m_paramClassifier.m_nWeightMode == ClassifierParam.nWM_TF_IDF_DIFF)
				psSortBuf[i].pclsWordNode.computeWeight(lDocNum, true);
			wordNode.m_dWeight = psSortBuf[i].pclsWordNode.m_dWeight;
			wordNode.m_lDocFreq = psSortBuf[i].pclsWordNode.m_lDocFreq;
			wordNode.m_lWordFreq = psSortBuf[i].pclsWordNode.m_lWordFreq;
			dstWordList.put(psSortBuf[i].word, wordNode);
		}
		
		return dstWordList;
	}

	public void genSortBuf(WordList wordList,
							SortType[] psSortBuf) {
		int lWordCount = 0;
		
		// for each word
		for (Entry<String, WordNode> e : wordList.m_lstWordList.entrySet())
		{
			WordNode wordNode = e.getValue();
			String str = e.getKey();
			psSortBuf[lWordCount].pclsWordNode = wordNode;
			psSortBuf[lWordCount].word = str;
			//System.out.println(psSortBuf[lWordCount].dWeight);
			psSortBuf[lWordCount].dWeight = wordNode.m_dWeight;
			
			lWordCount++;
		}
	}

	// 參數nType用來決定分類模型的類別,nType=0代表KNN分類器,nType=1代表SVM分類器
	public boolean WriteModel(String strFileName,WordList m_lstTrainWordList) throws Exception {
		LEDataOutputStream fOut = new LEDataOutputStream(new FileOutputStream(
				strFileName));

		m_lstTrainWordList.dumpToFile(m_paramClassifier.m_txtResultDir
				+ "/features.dat");
		m_lstTrainWordList.dumpWordList(m_paramClassifier.m_txtResultDir
				+ "/features.txt");
		m_lstTrainCatalogList.dumpToFile(m_paramClassifier.m_txtResultDir
				+ "/train.dat", 1);
		m_lstTrainCatalogList.dumpDocList(m_paramClassifier.m_txtResultDir
				+ "/train.txt");
		m_paramClassifier.dumpToFile(m_paramClassifier.m_txtResultDir
				+ "/params.dat");

		docSVM.param.classifier_num = m_lstTrainCatalogList.getCataNum();
		docSVM.param.trainfile = "train.txt";
		docSVM.param.resultpath = m_paramClassifier.m_txtResultDir;
		docSVM.param.DumpToFile(m_paramClassifier.m_txtResultDir
				+ "/svmparams.dat");

		fOut.writeInt(dwModelFileID);
		fOut.writeString("params.dat");
		fOut.writeString("features.dat");
		fOut.writeString("train.dat");
		fOut.writeString("svmparams.dat");

		fOut.close();
		return true;
	}
}
