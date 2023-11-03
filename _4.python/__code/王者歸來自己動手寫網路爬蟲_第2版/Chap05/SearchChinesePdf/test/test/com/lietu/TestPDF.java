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
		 //"D:/lg/work/hblocaltax/���ǽT���/table1100.pdf";
		 //"D:/lg/work/hblocaltax/���ǽT���/P020090731329583595091.pdf";
		 //"D:/lg/work/hblocaltax/���ǽT���/485.pdf";
		 //"D:/lg/work/hblocaltax/���ǽT���/20090224153208138.pdf";
		 //"D:/lg/work/hblocaltax/���ǽT���/20090224153331324.pdf";
		 //"D:/lg/work/hblocaltax/���ǽT���/guoshuifa200929.pdf";
		
		 //"D:/lg/work/hblocaltax/pdf���ǽT���/049-2005-003.pdf";
		 //"D:/lg/work/hblocaltax/pdf���ǽT���/1235726038.pdf";
		//"D:/lg/work/hblocaltax/pdf���ǽT���/2820410421c330460121c43365b90014.pdf"; //error
		 //"D:/lg/work/hblocaltax/pdf���ǽT���/20080115001.pdf"; //error �y�����H�Ƨ� �y������a�|�ȧ� �y�����a��|�ȧ�
		//"D:/lg/work/hblocaltax/pdf���ǽT���/282041042257bcdd01226236d7fa0010.pdf";
		 //"D:/lg/work/hblocaltax/pdf���ǽT���/1174947360427RB06B327C.pdf";//error
		//"D:/lg/work/hblocaltax/pdf���ǽT���/1200738994605846-1200738994607128.pdf";
		 //"D:/lg/work/hblocaltax/pdf���ǽT���/2008422112514481.pdf";
		 //"D:/lg/work/hblocaltax/pdf���ǽT���/200931911265575927.pdf";
		 //"D:/lg/work/hblocaltax/pdf���ǽT���/200932611134335141.pdf";
		 //"D:/lg/work/hblocaltax/pdf���ǽT���/20060921165000043352.pdf"; 
		 //"D:/lg/work/hblocaltax/pdf���ǽT���/P020090216384534682797.pdf";
		 //"D:/lg/work/hblocaltax/pdf���ǽT���/������o��a�|���`���m��a�ϸg����`�ǵ|���~�ұo�|�x���޲z�Ȧ��k�n���q��.pdf";
		 
		 //"D:/lg/work/hblocaltax/pdf���ǽT���/FDCSDS.pdf"; //code error
		
		//"D:/lg/work/hblocaltax/pdf���ǽT���/chinavvv_0902191053455390.pdf";
		 "D:/lg/work/hblocaltax/pdf���ǽT���/guoshuifa200945.pdf";
		 //"D:/lg/work/hblocaltax/pdf���ǽT���/P020090216384534682797.pdf";
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
		String title = //"�y�����H�Ƨ� �y������a�|�ȧ� �y�����a��|�ȧ�";
		//"������o���󰵦n2008�~�׵��U�|�Ȯv ���~���Ҹդu�@���q��";
			//"�_�ʥ���ǧ޳N�e���| �_�ʥ��]�F�� �_�ʥ���a�|�ȧ� �_�ʥ��a��|�ȧ�";
			"�_�ʥ���ǧ޳N�e���|�B�_�ʥ��]�F���B�_�ʥ���a�|�ȧ��B�_�ʥ��a��|�ȧ����󤽥� �_�ʥ�2009�~�ײĤT�����{�w���s�޳N ���~�W�檺�q��";
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
