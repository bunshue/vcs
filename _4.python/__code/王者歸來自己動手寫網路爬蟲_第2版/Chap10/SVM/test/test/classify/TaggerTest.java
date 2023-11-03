/*
 * Created on 2005-2-9
 *
 */
package test.classify;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.SortedSet;

import com.lietu.seg.result.CnToken;
import com.lietu.seg.result.WordIndex;

/**
 * @author luogang
 *
 */
public class TaggerTest {

	public static void main(String[] args) throws Exception
	{
		//testNormalSeg();
		//testOrg();
		//testPlace();
		//testPOS();
		//testBrand();
		testFormatSeg();
		//testSplit();
		//testSplitWords();
	}
	
    public static void testFormatSeg() throws Exception{
    	long startTime;
    	long endTime;
    	
    	com.lietu.seg.result.Tagger.makeTag= true;//false;
    	com.lietu.seg.result.Tagger.segSZ = false;
    	String sentence =//"邁向充滿希望的新世紀";
    		//"有關劉曉慶偷稅案";
    		"在廣州分別設有UPS不間斷電源和免維護蓄電池生產基地。";
    		//"上海雷天軟件科技有限... 公司，  ，上海雷天軟件科技有限公司是一家從事通訊軟件製作的公司，為適應市場的高速發展，組織有更具潛力的團隊，現誠聘請有資深經驗，渴望成就與新挑戰並能承受快速發展壓力的年輕才俊加盟。戶籍不限，唯才是用。 聯繫方式： 電 話：021-36030126 E-mail：zhujc@linghui.com 職位1： 軟件開發工程師 職位描述： JAVA軟件工程師（3-4人）責任：負責java軟件程式解碼工作，";//"其中包括興安至全州、桂林至興安、全州至黃沙河、陽朔至平樂、桂林至陽朔、桂林市國道過境線靈川至三塘段、平樂至鍾山、桂林至三江高速公路。";
    	//"許可和權利";
    		//"許可制度";
    	//seg.result.Tagger tagger = new seg.result.Tagger();
    	ArrayList result = com.lietu.seg.result.Tagger.getFormatSegResult(sentence);
    	
    	startTime = System.currentTimeMillis();
    	for (int i=0; i<result.size();i++)
    	{
    		CnToken t = (CnToken)result.get(i);
            System.out.println(t.termText() + " " + t.startOffset() + " "
                               + t.endOffset() + " "+t.type());
        }
    	endTime = System.currentTimeMillis();
    	System.out.println("first seg time cost:" + ( endTime - startTime));
    }

    /*public static void testSplitWords() throws Exception{
    	long startTime;
    	long endTime;
    	
    	StringBuffer sentence =//"邁向充滿希望的新世紀";
    		//"有關劉曉慶偷稅案";
    		new StringBuffer("上海雷天軟件科技有限... 公司，  ，上海雷天軟件科技有限公司是一家從事通訊軟件製作的公司，為適應市場的高速發展，組織有更具潛力的團隊，現誠聘請有資深經驗，渴望成就與新挑戰並能承受快速發展壓力的年輕才俊加盟。戶籍不限，唯才是用。 聯繫方式： 電 話：021-36030126 E-mail：zhujc@linghui.com 職位1： 軟件開發工程師 職位描述： JAVA軟件工程師（3-4人）責任：負責java軟件程式解碼工作，");//"其中包括興安至全州、桂林至興安、全州至黃沙河、陽朔至平樂、桂林至陽朔、桂林市國道過境線靈川至三塘段、平樂至鍾山、桂林至三江高速公路。";
    	//"許可和權利";
    		//"許可制度";
    	int offset = 0;
    	SortedSet<WordIndex> result = seg.result.Tagger.splitWords(sentence,offset,sentence.length() - offset);
    	
    	startTime = System.currentTimeMillis();
    	
    	Iterator<WordIndex> iterator = result.iterator();
        while (iterator.hasNext())
        {
        	WordIndex item = iterator.next();
            System.out.print( item .word() + " " + item.index() + "\n" );
        }

    	//for (int i=0; i<result.size();i++)
    	//{
        //    System.out.println(result.);
        //}
    	endTime = System.currentTimeMillis();
    	System.out.println("first seg time cost:" + ( endTime - startTime));
    }*/
    
	public static void testNormalSeg() throws Exception
	{
		//seg.result.Tagger tagger = new seg.result.Tagger();
		
		//seg.result.Tagger.makeTag = false;
		com.lietu.seg.result.Tagger.segName = true;
		
		String sSentence="全亞洲僅有的兩名提前錄取生之一、每年4.5萬美元的全額獎學金資助---復旦附中高三女生湯玫捷獲得了哈佛大學最優厚的入學待遇。";
		String sSentenceResult;
		
		long startTime = System.currentTimeMillis();
		sSentenceResult= com.lietu.seg.result.Tagger.getNormalSegResult(sSentence);
		System.out.println("seg time cost:" + (System.currentTimeMillis() - startTime)); 
		
		System.out.println(sSentenceResult);
		
		sSentence="標準制定的家電廠商，";//"從美國返台的俞揚和，相當低調";
		sSentenceResult= com.lietu.seg.result.Tagger.getNormalSegResult(sSentence);
		System.out.println(sSentenceResult);
		
		sSentence="新華社記者黃智敏";
		sSentenceResult= com.lietu.seg.result.Tagger.getNormalSegResult(sSentence);
		System.out.println(sSentenceResult);
		
		sSentence="陳忠和不假遲疑地答";//"夏衍、劉白羽、姚雪垠、王蒙、李德倫、張光年、管樺、魏巍、諶容、劉長瑜、董學文等文藝界知名人士先後發言。";
		sSentenceResult= com.lietu.seg.result.Tagger.getNormalSegResult(sSentence);
		System.out.println(sSentenceResult);
	}
	
	
	public static void testPlace() throws Exception
	{
		//seg.result.Tagger tagger = new seg.result.Tagger();

		//seg.result.Tagger.makeTag = true;
		com.lietu.seg.result.Tagger.segSZ = false;
		
		String sSentence="中華人民共和國普通高等學校聯合招收華僑、港澳、台灣省學生辦公室（簡稱中國聯合招辦）附設在廣東省招生辦內，";
		String sSentenceResult;

		long startTime = System.currentTimeMillis();
		sSentenceResult = com.lietu.seg.result.Tagger.getNormalSegResult(sSentence);
		//141
		System.out.println("seg time cost:" + (System.currentTimeMillis() - startTime)); 
		System.out.println(sSentenceResult);
	}

	public static void testOrg() throws Exception
	{
		//seg.result.Tagger tagger = new seg.result.Tagger();

		//seg.result.Tagger.makeTag = true;
		com.lietu.seg.result.Tagger.segSZ = false;
		
		String sSentence="醴陵市城區,。國星陶瓷銷售處。。";
		String sSentenceResult;

		long startTime = System.currentTimeMillis();
		sSentenceResult = com.lietu.seg.result.Tagger.getNormalSegResult(sSentence);
		com.lietu.seg.result.Tagger.reLoad();
		com.lietu.seg.result.Tagger.getFormatSegResult(sSentence);
		//141
		System.out.println("seg time cost:" + (System.currentTimeMillis() - startTime)); 
		System.out.println(sSentenceResult);
	}
}
