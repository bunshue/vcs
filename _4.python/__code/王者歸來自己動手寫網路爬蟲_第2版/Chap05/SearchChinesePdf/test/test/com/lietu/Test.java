package test.com.lietu;

import com.lietu.pdfbox.PdfTitleExtractor;

public class Test {

	/**
	 * @param args
	 */
	public static void main(String[] args) throws Exception {
		//System.out.println(PdfTitleExtractor.sweetSpotLength(300));
		testFileNum();
		//testProSendGovUnit();
		//testProReceiGovUnit();
	}

	public static void testProSendGovUnit()
	{
		String sNum = //"江山市人民政府 關於進一步加強公共衛生工作的意見";
		//"合肥市物價局檔案";
			//"北京市科學技術委員會、北京市財政局、北京市國家稅務局、北京市地方稅務局關於公示 北京市2008年度首批擬認定高新技術企業 名單的通知";
		"國家稅務總局 關於修改若干增值稅規範性檔案參考法規規章條款依據的通知";
		
		System.out.println(PdfTitleExtractor.isProSendGovUnit(sNum,java.awt.Color.RED));
	}

	public static void testProReceiGovUnit()
	{
		String sNum = //"江山市人民政府 關於進一步加強公共衛生工作的意見";
		//"各市經貿委（經委、青島市發改委）、財政局、國稅局、地稅局：";
		//"各縣（市、區）勞動保障局、地稅局、國稅局：";
		//"各區縣人事局、國家稅務局、地方稅務局，市級有關部門：";
			//"北京市科學技術委員會、北京市財政局、北京市國家稅務局、北京市地方稅務局關於公示 北京市2008年度首批擬認定高新技術企業 名單的通知";
			"國家稅務總局 關於修改若干增值稅規範性檔案參考法規規章條款依據的通知";
		
		System.out.println(PdfTitleExtractor.isProReceiGovUnit(sNum,java.awt.Color.BLACK));
	}
	
	public static void testFileNum()
	{
		String sNum = //"泉勞社〔2009〕78 號";
		//"江政發〔2006〕28號";
		//"京科高發〔2009〕283號";
		//"浙國稅所〔2008〕16號";
			" 人社部發 2008 120號  ";
			//"教研辦[1998]1號";
		
		System.out.println(PdfTitleExtractor.isFileNum(sNum,java.awt.Color.BLACK));
	}
	
	public static void testPublishCode()
	{
		String title = " 人社部發 2008 120號  ";
		//"川國稅發（2007）065 號";
		System.out.println(PdfTitleExtractor.isFileNum(title,java.awt.Color.BLACK));
	}
	
	public static void testNum()
	{
		String sNum = "200";
		int start = 0;
		
		System.out.println(PdfTitleExtractor.isYearTime(sNum, start));
	}

}
