package test.com.lietu;

import java.io.File;
import java.net.MalformedURLException;

import org.apache.pdfbox.pdmodel.PDDocument;

import com.lietu.pdfbox.PDFTextStripper;

public class TestContent {

	/**
	 * @param args
	 * @throws Exception 
	 */
	public static void main(String[] args) throws Exception {
		String fileName = "D:/lg/work/hblocaltax/pdf���ǽT���/2008422112514481.pdf";
		String content = getText(new File(fileName));
		System.out.println(content);
	}

	public static String getText(File file) throws Exception {
		// �O�_�Ƨ�
		boolean sort = false;
		// �Ǧ^��r
		String outStr = null;
		// �}�l���R����
		int startPage = 1;
		// �������R����
		int endPage = 10;
		// �O���餤�x�s��PDF DOcument
		PDDocument document = null;
		try {
			try {
				// ��@�@��URL�ӥ[���ɮ�
				document = PDDocument.load(file);
			} catch (MalformedURLException e) {
			}
			// ��PDFTextStripper�Ӥ��R��r
			PDFTextStripper stripper = new PDFTextStripper();
			// �]�w�O�_�Ƨ�
			stripper.setSortByPosition(sort);
			// �]�w�_�l��
			stripper.setStartPage(startPage);
			// �]�w������
			stripper.setEndPage(endPage);

			outStr = stripper.getText(document);

			return (outStr);
		} catch (Exception e) {
			return "";
		} finally {
			if (document != null) {
				document.close();
			}
		}
	}
	
}
