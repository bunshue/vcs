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
		String sNum = //"���s���H���F�� ����i�@�B�[�j���@�åͤu�@���N��";
		//"�X�Υ��������ɮ�";
			//"�_�ʥ���ǧ޳N�e���|�B�_�ʥ��]�F���B�_�ʥ���a�|�ȧ��B�_�ʥ��a��|�ȧ����󤽥� �_�ʥ�2008�~�׭������{�w���s�޳N���~ �W�檺�q��";
		"��a�|���`�� ����ק�Y�z�W�ȵ|�W�d���ɮװѦҪk�W�W�����ڨ̾ڪ��q��";
		
		System.out.println(PdfTitleExtractor.isProSendGovUnit(sNum,java.awt.Color.RED));
	}

	public static void testProReceiGovUnit()
	{
		String sNum = //"���s���H���F�� ����i�@�B�[�j���@�åͤu�@���N��";
		//"�U���g�T�e�]�g�e�B�C�q���o��e�^�B�]�F���B��|���B�a�|���G";
		//"�U���]���B�ϡ^�ҰʫO�٧��B�a�|���B��|���G";
		//"�U�Ͽ��H�Ƨ��B��a�|�ȧ��B�a��|�ȧ��A���Ŧ��������G";
			//"�_�ʥ���ǧ޳N�e���|�B�_�ʥ��]�F���B�_�ʥ���a�|�ȧ��B�_�ʥ��a��|�ȧ����󤽥� �_�ʥ�2008�~�׭������{�w���s�޳N���~ �W�檺�q��";
			"��a�|���`�� ����ק�Y�z�W�ȵ|�W�d���ɮװѦҪk�W�W�����ڨ̾ڪ��q��";
		
		System.out.println(PdfTitleExtractor.isProReceiGovUnit(sNum,java.awt.Color.BLACK));
	}
	
	public static void testFileNum()
	{
		String sNum = //"�u�Ҫ��e2009�f78 ��";
		//"���F�o�e2006�f28��";
		//"�ʬ찪�o�e2009�f283��";
		//"����|�ҡe2008�f16��";
			" �H�����o 2008 120��  ";
			//"�Ь��[1998]1��";
		
		System.out.println(PdfTitleExtractor.isFileNum(sNum,java.awt.Color.BLACK));
	}
	
	public static void testPublishCode()
	{
		String title = " �H�����o 2008 120��  ";
		//"�t��|�o�]2007�^065 ��";
		System.out.println(PdfTitleExtractor.isFileNum(title,java.awt.Color.BLACK));
	}
	
	public static void testNum()
	{
		String sNum = "200";
		int start = 0;
		
		System.out.println(PdfTitleExtractor.isYearTime(sNum, start));
	}

}
