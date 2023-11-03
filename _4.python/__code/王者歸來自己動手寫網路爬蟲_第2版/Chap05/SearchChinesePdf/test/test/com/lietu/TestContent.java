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
		String fileName = "D:/lg/work/hblocaltax/pdf不準確文件/2008422112514481.pdf";
		String content = getText(new File(fileName));
		System.out.println(content);
	}

	public static String getText(File file) throws Exception {
		// 是否排序
		boolean sort = false;
		// 傳回文字
		String outStr = null;
		// 開始分析頁數
		int startPage = 1;
		// 結束分析頁數
		int endPage = 10;
		// 記憶體中儲存的PDF DOcument
		PDDocument document = null;
		try {
			try {
				// 當作一個URL來加載檔案
				document = PDDocument.load(file);
			} catch (MalformedURLException e) {
			}
			// 用PDFTextStripper來分析文字
			PDFTextStripper stripper = new PDFTextStripper();
			// 設定是否排序
			stripper.setSortByPosition(sort);
			// 設定起始頁
			stripper.setStartPage(startPage);
			// 設定結束頁
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
