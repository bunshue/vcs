package test.com.lietu;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map.Entry;

import com.lietu.pdfbox.PdfTitleExtractor;
import com.lietu.pdfbox.PdfTitle;

public class TestPDF {

	public static void main(String[] args) throws Exception {
		String fileName =  //"D:/lg/work/hblocaltax/P020080327288707150004.pdf";
		 //"D:/lg/work/hblocaltax/122EF584d01.pdf";
		 //"D:/lg/work/hblocaltax/7D19A80Ed01.pdf"; //encrpt error
		 //"D:/lg/work/hblocaltax/D751503Dd01.pdf";
		 //"D:/lg/work/hblocaltax/n11261961.pdf";
		 //"D:/lg/work/hblocaltax/468456C0d01.pdf";
		 //"D:/lg/work/hblocaltax/217712CEd01.pdf";
		 //"D:/lg/work/hblocaltax/49B10CA1d01.pdf";
		 //"D:/lg/work/hblocaltax/9BA17857d01.pdf"; 
		 //"D:/lg/work/hblocaltax/9364DA0Dd01.pdf";
		 //"D:/lg/work/hblocaltax/C8674AACd01.pdf";

		 //"D:/lg/work/hblocaltax/DB182628d01.pdf";
		 //"D:/lg/work/hblocaltax/BF4FADF9d01.pdf";
		 //"D:/lg/work/hblocaltax/不準確文件/table1100.pdf";
		 //"D:/lg/work/hblocaltax/不準確文件/P020090731329583595091.pdf";
		 //"D:/lg/work/hblocaltax/不準確文件/485.pdf";
		 //"D:/lg/work/hblocaltax/不準確文件/20090224153208138.pdf";
		 //"D:/lg/work/hblocaltax/不準確文件/20090224153331324.pdf";
		 //"D:/lg/work/hblocaltax/不準確文件/guoshuifa200929.pdf";
		
		 //"D:/lg/work/hblocaltax/pdf不準確文件/049-2005-003.pdf";
		 //"D:/lg/work/hblocaltax/pdf不準確文件/1235726038.pdf";
		//"D:/lg/work/hblocaltax/pdf不準確文件/2820410421c330460121c43365b90014.pdf"; //error
		 //"D:/lg/work/hblocaltax/pdf不準確文件/20080115001.pdf"; //error 宜賓市人事局 宜賓市國家稅務局 宜賓市地方稅務局
		//"D:/lg/work/hblocaltax/pdf不準確文件/282041042257bcdd01226236d7fa0010.pdf";
		 //"D:/lg/work/hblocaltax/pdf不準確文件/1174947360427RB06B327C.pdf";//error
		//"D:/lg/work/hblocaltax/pdf不準確文件/1200738994605846-1200738994607128.pdf";
		 //"D:/lg/work/hblocaltax/pdf不準確文件/2008422112514481.pdf";
		 //"D:/lg/work/hblocaltax/pdf不準確文件/200931911265575927.pdf";
		 //"D:/lg/work/hblocaltax/pdf不準確文件/200932611134335141.pdf";
		 //"D:/lg/work/hblocaltax/pdf不準確文件/20060921165000043352.pdf"; 
		 //"D:/lg/work/hblocaltax/pdf不準確文件/P020090216384534682797.pdf";
		 //"D:/lg/work/hblocaltax/pdf不準確文件/關於轉發國家稅務總局《跨地區經營匯總納稅企業所得稅徵收管理暫行辦法》的通知.pdf";
		 
		 //"D:/lg/work/hblocaltax/pdf不準確文件/FDCSDS.pdf"; //code error
		
		//"D:/lg/work/hblocaltax/pdf不準確文件/chinavvv_0902191053455390.pdf";
		 "D:/lg/work/hblocaltax/pdf不準確文件/guoshuifa200945.pdf";
		 //"D:/lg/work/hblocaltax/pdf不準確文件/P020090216384534682797.pdf";
		//"D:/lg/work/hblocaltax/73BC14F4d01.pdf";
			//"D:/lg/work/hblocaltax/EBA962C2d01.pdf";
			//"D:/lg/work/hblocaltax/FD513A81d01.pdf";
			//"D:/lg/work/hblocaltax/365BF08Ad01.pdf";
		
		testGetTitle(fileName);
		//testSummaryRatio();
		//testLengthSocre();

		// String content = PDFBox.getText(new File(fileName));
		// System.out.println(content);

		// testDraw(fileName);

		// String title = PDFBox.getTitle(content);

		// System.out.println(text);
		// System.out.println(title);
	}
	
	public static void testLengthSocre()
	{
		System.out.println(PdfTitleExtractor.sweetSpotLength(67));
	}
	
	public static void testSummaryRatio() throws Exception {
		String title = //"宜賓市人事局 宜賓市國家稅務局 宜賓市地方稅務局";
		//"關於轉發關於做好2008年度註冊稅務師 執業資格考試工作的通知";
			//"北京市科學技術委員會 北京市財政局 北京市國家稅務局 北京市地方稅務局";
			"北京市科學技術委員會、北京市財政局、北京市國家稅務局、北京市地方稅務局關於公示 北京市2009年度第三批擬認定高新技術 企業名單的通知";
		//System.out.println(PdfTitleExtractor.getDupScore(title));
		System.out.println(PdfTitleExtractor.getNoDupRatio(title));
	}

	public static void testGetTitle(String fileName) throws Exception {
		StringBuilder allContent = new StringBuilder();
		PdfTitleExtractor.FloatValue pageHeight = new PdfTitleExtractor.FloatValue();
		ArrayList<PdfTitle> titles = PdfTitleExtractor.getCandiateTitle(
				fileName, allContent, pageHeight);

		//for (PdfTitle e : titles) {
		//	System.out.println("PdfTitle:" + e);
		//}
		
		HashMap<PdfTitle, Double> scores = PdfTitleExtractor.rankTitle(titles,
				allContent.toString(), pageHeight.value);
		System.out.println("scores size:" + scores.size());
		for (Entry<PdfTitle, Double> e : scores.entrySet()) {
			System.out.println("PdfTitle:" + e.getKey());
			System.out.println("PdfTitle score:" + e.getValue());
		}
		
		String bestTitle = PdfTitleExtractor.getBestTitle(scores);
		System.out.println("best title1:" + bestTitle);

		for (PdfTitle t : titles) {
			System.out.println("Pdf Candiate Title:" + t);
			ArrayList<PdfTitle> subTitles = t.split();
			if(subTitles == null)
			{
				continue;
			}
			//System.out.println("sub Pdf Candiate Title size:" + subTitles.size());
			//for(PdfTitle subTitle : subTitles)
			//{
			//	System.out.println("sub Pdf Candiate Title:" + subTitle);
			//}
		}
		if(bestTitle==null)
		{
			PdfTitle biggestTitle = PdfTitleExtractor.getBiggestTitle(titles);

			System.out.println("biggest Title:" + biggestTitle);
			ArrayList<PdfTitle> subTitles = biggestTitle.split();
			if(subTitles == null)
			{
				return;
			}
			System.out.println("sub Pdf Candiate Title size:" + subTitles.size());
			for(PdfTitle subTitle : subTitles)
			{
				System.out.println("sub Pdf Candiate Title:" + subTitle);
			}
			
			scores = PdfTitleExtractor.rankTitle(subTitles,
					allContent.toString(), pageHeight.value);
			bestTitle = PdfTitleExtractor.getBestTitle(scores);
		}

		System.out.println("best title:" + bestTitle);
	}
}
