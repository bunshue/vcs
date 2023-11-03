package com.lietu.solutions.community.rtf2Raw;

import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;

import com.lietu.rtf.extract.RtfExtractor;

public class TestWeb {

	/**
	 * @param args
	 * @throws Exception 
	 */
	public static void main(String[] args) throws Exception {
		String urlStr = //"http://www.maranatha-bpc.com/ChineseWorshipService/TheSummontowitnessforChrist.rtf";
		//"http://www.silo.net/LaReja-2005-05-07/texto_chino_7M.rtf"
			//"http://www.csrc.gov.cn/n575458/n575667/n642011/n1994218.files/n1994219.1062401804016.rtf";
			//"http://images.juren.com/file/quick/beijingchunji.RTF";
			//"http://www.gffunds.com.cn/data/File/20061012093946_0_gfwjzmsmszygx2006%201h.rtf";
			//"http://www.zzym518.com/leadbbs/images/upload/2007/08/16/204935.rtf";
			//"http://ghjz.tjuci.edu.cn/jingpin/waijianshi_class/kejian/zuoye/°q.rtf";
			//"http://www.cscs.org.au/Anti-SARS%20Report.rtf";
		"http://www.ynem.com.cn/jcinfo/StateStation200351.rtf";
		URL u = new URL(urlStr);
		
		// Create a URLConnection object
		URLConnection uc = u.openConnection();
		
		// now lets get the response and print it out
		InputStream is = uc.getInputStream();
		
		RtfExtractor  extractor=new RtfExtractor(is);
		String text = extractor.getText();
		
		is.close();
		System.out.println("text:"+text);
		
	}

}
