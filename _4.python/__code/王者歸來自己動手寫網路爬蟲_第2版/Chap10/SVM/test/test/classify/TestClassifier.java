package test.classify;

import java.io.File;
import java.util.Scanner;

import com.lietu.classify.CatalogList;
import com.lietu.classify.Classifier;
import com.lietu.classify.ClassifierParam;
import com.lietu.classify.Trainer;
import com.lietu.classify.WordList;
import java.util.Map;
import java.util.Iterator;
import java.util.Set;
import java.util.HashMap;

public class TestClassifier {
	static Map<String, Integer> human = new HashMap<String, Integer>();
	static Map<String, Integer> correct = new HashMap<String, Integer>();
	static Map<String, Integer> automatic = new HashMap<String, Integer>();

	public static void printResult(Map<String, Integer> m) {
		for (Map.Entry<String, Integer> e : m.entrySet()) {
			System.out.println(e.getKey() + "\t" + e.getValue() + "\n");
		}

		System.out.println("\n");
	}

	/**
	 * @param args
	 * @throws Exception
	 */
	public static void main(String[] args) throws Exception {
		testTrain();
		testResult();

		// ��Xcorrect;
		System.out.print("The number of correctly classified files:\n");
		printResult(correct);

		// ��Xhuman;
		System.out.print("The number of human classified files:\n");
		printResult(human);

		// ��Xautomatic
		System.out.print("The result of svm classifier:\n");
		printResult(automatic);

	}

	/**
	 * @param fileToBeClassified
	 * @return
	 * @throws Exception
	 */
	public static boolean testSVMClassify(File fileToBeClassified)
			throws Exception {
		String modelDir = "C:/Classifier/model/model.prj";
		Classifier theClassifier = new Classifier(modelDir);

		// modified 20090714: �令Ū�J�ɮ�
		Scanner scanner = new Scanner(fileToBeClassified, "GBK");
		scanner.useDelimiter("\\z");
		String content = "";
		if (scanner.hasNext()) {
			content = scanner.next();
		}

		System.out.println("SVM�����}�l");

		String catName = theClassifier.getCategoryName(content);
		Integer value = automatic.get(catName);
		if (value == null) {
			automatic.put(catName, 1);
		} else {
			automatic.put(catName, value + 1);
		}

		String filePath = fileToBeClassified.getParent().toString();
		String fileCategoryByHuman = filePath.substring(filePath
				.lastIndexOf("\\") + 1, filePath.length());
		try {
			if (catName.equals(fileCategoryByHuman)) {
				return true;
			} else {
				return false;
			}
		} catch (Exception e)// catName = null
		{
			System.out.print(fileToBeClassified + "\t");
			System.out.print(e.toString() + "\n");
			return false;
		}

	}

	public static void testSVMClassifyFolder(File file,
			TestCorrectAndHumanClassified thisResults) throws Exception {
		File[] files = file.listFiles();
		for (int i = 0; i < files.length; i++) {
			if (files[i].isFile()) {
				if (testSVMClassify(files[i].getAbsoluteFile())) {
					thisResults.correctlyClassified++;
				}
				thisResults.humanClassified++;
			} else {
				testSVMClassifyFolder(files[i], thisResults);
			}
		}

	}

	public static void testResult() throws Exception {

		File testFolder = new File("C:/Classifier/Test");
		if (testFolder.isFile()) {
			System.out.print("Test folder cannot be a single file!!!");
		} else {
			File[] files = testFolder.listFiles();
			for (int i = 0; i < files.length; i++) {
				if (files[i].isFile()) {
					System.out.print("Category name cannot be a file!!!");
				} else {

					TestCorrectAndHumanClassified thisCorrectAndHumanClassified = new TestCorrectAndHumanClassified();
					testSVMClassifyFolder(files[i],
							thisCorrectAndHumanClassified);
					human.put(files[i].getName(),
							thisCorrectAndHumanClassified.humanClassified);
					correct.put(files[i].getName(),
							thisCorrectAndHumanClassified.correctlyClassified);
				}
			}

		}
	}

	public static void testTrain() throws Exception {
		Trainer svmClassifier = new Trainer();
		svmClassifier.setTrainSet("C:/Classifier/Train");
		svmClassifier.setModel("C:/Classifier/model");
		svmClassifier.train(ClassifierParam.nFS_IGMode); // ��ܯS�x��ܤ�k
		/*
		 * ��T�W�q nFS_IGMode, 0 ����T nFS_MIMode, 1 �����e�i nFS_CEMode, 2 X^2�έp
		 * nFS_X2Mode, 3 ��r�Ҿ��v�� nFS_WEMode, 4 �k�b��T�W�q nFS_XXMode, 5
		 */
	}

}
