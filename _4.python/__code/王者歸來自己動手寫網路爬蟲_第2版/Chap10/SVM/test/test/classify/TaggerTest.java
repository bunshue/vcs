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
    	String sentence =//"�ڦV�R���Ʊ檺�s�@��";
    		//"�����B��y���|��";
    		"�b�s�{���O�]��UPS�����_�q���M�K���@�W�q���Ͳ���a�C";
    		//"�W���p�ѳn���ަ���... ���q�A  �A�W���p�ѳn���ަ������q�O�@�a�q�Ƴq�T�n��s�@�����q�A���A�����������t�o�i�A��´������O���ζ��A�{�۸u�Ц���`�g��A���榨�N�P�s�D�Ԩï�Ө��ֳt�o�i���O���~���~�T�[���C���y�����A�ߤ~�O�ΡC �pô�覡�G �q �ܡG021-36030126 E-mail�Gzhujc@linghui.com ¾��1�G �n��}�o�u�{�v ¾��y�z�G JAVA�n��u�{�v�]3-4�H�^�d���G�t�djava�n��{���ѽX�u�@�A";//"�䤤�]�A���w�ܥ��{�B�۪L�ܿ��w�B���{�ܶ��F�e�B���Ҧܥ��֡B�۪L�ܶ��ҡB�۪L����D�L�ҽu�F�t�ܤT��q�B���֦���s�B�۪L�ܤT�����t�����C";
    	//"�\�i�M�v�Q";
    		//"�\�i���";
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
    	
    	StringBuffer sentence =//"�ڦV�R���Ʊ檺�s�@��";
    		//"�����B��y���|��";
    		new StringBuffer("�W���p�ѳn���ަ���... ���q�A  �A�W���p�ѳn���ަ������q�O�@�a�q�Ƴq�T�n��s�@�����q�A���A�����������t�o�i�A��´������O���ζ��A�{�۸u�Ц���`�g��A���榨�N�P�s�D�Ԩï�Ө��ֳt�o�i���O���~���~�T�[���C���y�����A�ߤ~�O�ΡC �pô�覡�G �q �ܡG021-36030126 E-mail�Gzhujc@linghui.com ¾��1�G �n��}�o�u�{�v ¾��y�z�G JAVA�n��u�{�v�]3-4�H�^�d���G�t�djava�n��{���ѽX�u�@�A");//"�䤤�]�A���w�ܥ��{�B�۪L�ܿ��w�B���{�ܶ��F�e�B���Ҧܥ��֡B�۪L�ܶ��ҡB�۪L����D�L�ҽu�F�t�ܤT��q�B���֦���s�B�۪L�ܤT�����t�����C";
    	//"�\�i�M�v�Q";
    		//"�\�i���";
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
		
		String sSentence="���Ȭw�Ȧ�����W���e�����ͤ��@�B�C�~4.5�U���������B���Ǫ���U---�_���������T�k�ʹ�������o�F����j�ǳ��u�p���J�ǫݹJ�C";
		String sSentenceResult;
		
		long startTime = System.currentTimeMillis();
		sSentenceResult= com.lietu.seg.result.Tagger.getNormalSegResult(sSentence);
		System.out.println("seg time cost:" + (System.currentTimeMillis() - startTime)); 
		
		System.out.println(sSentenceResult);
		
		sSentence="�зǨ�w���a�q�t�ӡA";//"�q�����x���\���M�A�۷�C��";
		sSentenceResult= com.lietu.seg.result.Tagger.getNormalSegResult(sSentence);
		System.out.println(sSentenceResult);
		
		sSentence="�s�ت��O�̶�����";
		sSentenceResult= com.lietu.seg.result.Tagger.getNormalSegResult(sSentence);
		System.out.println(sSentenceResult);
		
		sSentence="�����M������æa��";//"�L�l�B�B�զСB�������B���X�B���w�ۡB�i���~�B�޾�B�Q�ޡB�ۮe�B�B����B���Ǥ嵥�����ɪ��W�H�h����o���C";
		sSentenceResult= com.lietu.seg.result.Tagger.getNormalSegResult(sSentence);
		System.out.println(sSentenceResult);
	}
	
	
	public static void testPlace() throws Exception
	{
		//seg.result.Tagger tagger = new seg.result.Tagger();

		//seg.result.Tagger.makeTag = true;
		com.lietu.seg.result.Tagger.segSZ = false;
		
		String sSentence="���ؤH���@�M�괶�q�����Ǯ��p�X�ۦ��ع��B��D�B�x�W�پǥͿ줽�ǡ]²�٤����p�X�ۿ�^���]�b�s�F�٩ۥͿ줺�A";
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
		
		String sSentence="Ŀ��������,�C��P�����P��B�C�C";
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
