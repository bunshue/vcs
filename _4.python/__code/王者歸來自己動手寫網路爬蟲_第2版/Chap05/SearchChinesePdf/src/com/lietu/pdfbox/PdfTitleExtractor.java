package com.lietu.pdfbox;

import java.awt.Color;
import java.io.File;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.TreeSet;
import java.util.Map.Entry;

import org.apache.pdfbox.exceptions.InvalidPasswordException;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.pdmodel.PDDocumentInformation;
import org.apache.pdfbox.pdmodel.PDPage;
import org.apache.pdfbox.pdmodel.common.PDRectangle;

public class PdfTitleExtractor {

	public static class FloatValue {
		public float value;
	}

	public static ArrayList<PdfTitle> getCandiateTitle(String fileName,
			StringBuilder allContent, FloatValue pageHeight) throws Exception {
		File pdfFile = new File(fileName);
		
		ArrayList<PdfTitle> titles = new ArrayList<PdfTitle>();

		String titleFileName = getFirstName(pdfFile.getName());
		
		if(titleFileName.length()<MAX_LENGTH )
		{
			PdfTitle filePdfTitle = new PdfTitle(titleFileName, pageHeight.value / 2);
			titles.add(filePdfTitle);
			System.out.println(titleFileName);
			allContent.append(titleFileName);
		}
		
		PDDocument document = null;
		try {
			document = PDDocument.load(pdfFile);
			if (document.isEncrypted()) {
				try {
					document.decrypt("");
					System.out.println("decrypt");
				} catch (InvalidPasswordException e) {
					System.err
							.println("Error: Document is encrypted with a password.");
					System.exit(1);
				}
			}

			PDDocumentInformation info = document.getDocumentInformation();
			String metaTitle = info.getTitle();
			if (metaTitle != null && !"".equals(metaTitle)) {
				metaTitle = metaTitle.trim();
				if(metaTitle.toLowerCase().endsWith(".doc"))
				{
					metaTitle = metaTitle.substring(0,metaTitle.length()-4);
				}
				if(metaTitle.length()<MAX_LENGTH)
				{
					PdfTitle metaPdfTitle = new PdfTitle(metaTitle, pageHeight.value / 2);
					titles.add(metaPdfTitle);
				}
			}

			List allPages = document.getDocumentCatalog().getAllPages();

			PDPage firstPage = (PDPage) allPages.get(0);
			System.out.println("Processing page: " + 0);
			if (firstPage.findResources() == null) {
				System.out.println("page.findResources(): isnull");
			}
			if (firstPage.getContents().getStream() == null) {
				System.out.println("page.getContents().getStream(): isnull");
			}
			PDRectangle pageSize = firstPage.findMediaBox();
			//System.out.println("page Height: " + pageSize.getHeight());
			System.out.println("page Width: " + pageSize.getWidth());
			float maxHeight = pageSize.getHeight() * 0.8f;
			pageHeight.value = pageSize.getHeight();

			TextPageDrawer printer = new TextPageDrawer(titles, maxHeight,
					allContent);
			printer.processStream(firstPage, firstPage.findResources(),
					firstPage.getContents().getStream());

			titles.add(printer.getLastTile());

		} finally {
			if (document != null) {
				document.close();
			}
		}
		return titles;
	}
	
	public static String getFirstName(String fileName)
	{
		int pos = fileName.indexOf('.');
		return fileName.substring(0,pos);
	}
	
	public static int MAX_LENGTH = 120;

	public static HashMap<PdfTitle, Double> rankTitle(
			ArrayList<PdfTitle> titles, String allContent,float pageHeight) {
		HashMap<PdfTitle, Double> socres = new HashMap<PdfTitle, Double>();
		for (PdfTitle t : titles) {
			if (t.title.length() > MAX_LENGTH) {
				break;
			}
			if(	isProSendGovUnit(t.title,t.textColor))
			{
				continue;
			}
			if(isProReceiGovUnit(t.title,t.textColor))
			{
				continue;
			}
			if(isFileNum(t.title,t.textColor))
			{
				continue;
			}
			double hanziCount = getHanziNum(t.title);
			if (hanziCount == 0)
				continue;
			double score = hanziCount * sweetSpotLength(t.title.length());
			if (t.textColor.equals(Color.RED)) {
				score *= 0.5;
			}

			//帶正文的頁面才計算標題的概括性
			if(allContent.length()>100)
			{
				int summaryScore = getSummaryScore(t.title, replace(allContent,
						t.title, ""));
				score *= summaryScore;
				System.out.println("summaryScore:" + summaryScore);

				double summaryRatio = getSummaryRatio(t.title, replace(allContent,
						t.title, ""));
				//* summaryRatio
				score *= summaryRatio ;
			}
			
			score *= t.fontSize ;
			score *=getNoDupRatio(t.title);
			
			score *= sweetSpotHeight(t.y/pageHeight);
			socres.put(t, score);
			System.out.println("PdfTitle:" + t);
		}
		return socres;
	}
	
	public static PdfTitle getBiggestTitle(ArrayList<PdfTitle> titles) {
		int longest=0;
		PdfTitle biggestTitle = null;
		for (PdfTitle t : titles) {
			if (t.title.length() > longest) {
				longest = t.title.length();
				biggestTitle = t;
			}
		}
		return biggestTitle;
	}

	public static String replace(final String aInput,
								final String aOldPattern,
								final String aNewPattern)
	{
		if (aOldPattern.equals("")) {

			throw new IllegalArgumentException("Old pattern must have content.");
		}

		final StringBuffer result = new StringBuffer();

		// startIdx and idxOld delimit various chunks of aInput; these
		// chunks always end where aOldPattern begins

		int startIdx = 0;

		int idxOld = 0;

		while ((idxOld = aInput.indexOf(aOldPattern, startIdx)) >= 0) {

			// grab a part of aInput which does not include aOldPattern
			result.append(aInput.substring(startIdx, idxOld));

			// add aNewPattern to take place of aOldPattern
			result.append(aNewPattern);

			// reset the startIdx to just after the current match, to see
			// if there are any further matches
			startIdx = idxOld + aOldPattern.length();
		}

		// the final chunk will go to the end of aInput
		result.append(aInput.substring(startIdx));

		return result.toString();

	}

	// 候選標題和其餘內容比較相似性
	public static int getSummaryScore(String title, String restContent) {
		TreeSet<Character> set1 = getNoDupCharSet(title);
									//getCharacter(title);
		TreeSet<Character> set2 = getCharacter(restContent);
		//System.out.println("title--->"+title+"\r\n"+"content--->"+restContent);
		
		TreeSet<Character> setDiff = (TreeSet<Character>) set1.clone();
		setDiff.retainAll(set2);

		return setDiff.size();
	}

	//判斷冗余度 例如:宜賓市人事局 宜賓市國家稅務局 宜賓市地方稅務局
	public static double getDupScore(String title) {
		TreeSet<Character> set = getCharacter(title);
		
		return (double)set.size()/(double)title.length();
	}

	public static double getSummaryRatio(String title, String restContent) {
		TreeSet<Character> set1 = getCharacter(title);
		TreeSet<Character> set2 = getCharacter(restContent);
		//System.out.println("title--->"+title+"\r\n"+"content--->"+restContent);
		
		TreeSet<Character> setDiff = (TreeSet<Character>) set1.clone();
		setDiff.retainAll(set2);

		return (double)setDiff.size()/(double)set1.size();
	}

	public static TreeSet<Character> getCharacter(String t) {
		TreeSet<Character> set = new TreeSet<Character>();
		for (int i = 0; i < t.length(); ++i) {
			char c = t.charAt(i);
			if (c != '局' && c != '市') {
				set.add(c);
			}
		}
		return set;
	}

	public static double getNoDupRatio(String title) {
		TreeSet<Character> setNoDup = getNoDupCharSet(title);
		TreeSet<Character> setDup = geDupCharSet(title);
		double dupCount = setDup.size();
		if(dupCount==0.0)
		{
			dupCount=1.0;
		}
		return (double)setNoDup.size()/dupCount;
	}

	public static TreeSet<Character> getNoDupCharSet(String t) {
		TreeSet<Character> allSet = new TreeSet<Character>();
		TreeSet<Character> noDupSet = new TreeSet<Character>();
		
		for (int i = 0; i < t.length(); ++i) {
			char c = t.charAt(i);
			if(allSet.contains(c))
			{
				noDupSet.remove(c);
				continue;
			}
			allSet.add(c);
			if (c != '局' && c != '市') {
				noDupSet.add(c);
			}
		}
		return noDupSet;
	}

	public static TreeSet<Character> geDupCharSet(String t) {
		TreeSet<Character> allSet = new TreeSet<Character>();
		TreeSet<Character> dupSet = new TreeSet<Character>();
		
		for (int i = 0; i < t.length(); ++i) {
			char c = t.charAt(i);
			if(allSet.contains(c))
			{
				dupSet.add(c);
			}
			allSet.add(c);
		}
		return dupSet;
	}
	
	public static String getBestTitle(HashMap<PdfTitle, Double> scores) {
		double score = 0;
		String bestTitle = null;
		for (Entry<PdfTitle, Double> e : scores.entrySet()) {
			if (e.getValue() > score) {
				bestTitle = e.getKey().title;
				score = e.getValue();
			}
		}
		return bestTitle;
	}

	/*
	 This method  try to identify File number.
	 example: 某機關（2009）27號  人社部發[2008]120號 川國稅發（2007）065 號
	 */	
	public static boolean isFileNum(String s,Color tcolor)
	{
		if(!tcolor.equals(Color.BLACK))
		{
			return false;
		}
		boolean isSymbol = false;
	
		boolean markBegSym = false;
		boolean markEndSym = false;
		
		for(int index=0; index<s.length(); index++)
		{
			if('[' == s.charAt(index))
			{
				markBegSym = true;
				for(int i =index+1; i<s.length(); i++)
				{
					if(!markEndSym)
					{   
						if((s.charAt(i)>='0'&& s.charAt(i)<='9')||s.charAt(i) ==' '
							||(s.charAt(i)>='０'&& s.charAt(i)<='９'))
					    {}
					    else if(s.charAt(i) == ']')
					    {
						   markEndSym = true;
						   i++;
					    }
					     else
					    {
						   markBegSym = false;
						   markEndSym = false;
					    }
					}
					if(markBegSym && markEndSym)
					{
						if((s.charAt(i)>='0'&& s.charAt(i)<='9')||s.charAt(i) ==' '
							||(s.charAt(i)>='０'&& s.charAt(i)<='９'))
						{}
						else if(s.charAt(i) == '號')
						{
							isSymbol = true;
							index = s.length();
						}
					}
				}
			}
			else if('（' == s.charAt(index))
			{
				markBegSym = true;
				for(int i =index+1; i<s.length(); i++)
				{
					if(!markEndSym)
					{   
						if((s.charAt(i)>='0'&& s.charAt(i)<='9')||s.charAt(i) ==' '
							||(s.charAt(i)>='０'&& s.charAt(i)<='９'))
					    {}
					    else if(s.charAt(i) == '）')
					    {
						   markEndSym = true;
						   i++;
					    }
					     else
					    {
						   markBegSym = false;
						   markEndSym = false;
					    }
					}
					if(markBegSym && markEndSym)
					{
						if((s.charAt(i)>='0'&& s.charAt(i)<='9')||s.charAt(i) ==' '
							||(s.charAt(i)>='０'&& s.charAt(i)<='９'))
						{}
						else if(s.charAt(i) == '號')
						{
							isSymbol = true;
							index = s.length();
						}
						
					}
				}
			}
			else if ('〔' == s.charAt(index))
			{
				markBegSym = true;
				for(int i =index+1; i<s.length(); i++)
				{
					if(!markEndSym)
					{   
						if((s.charAt(i)>='0'&& s.charAt(i)<='9')||s.charAt(i) ==' '
							||(s.charAt(i)>='０'&& s.charAt(i)<='９'))
					    {}
					    else if(s.charAt(i) == '〕')
					    {
						   markEndSym = true;
						   i++;
					    }
					     else
					    {
						   markBegSym = false;
						   markEndSym = false;
					    }
					}
					if(markBegSym && markEndSym)
					{
						if((s.charAt(i)>='0'&& s.charAt(i)<='9')||s.charAt(i) ==' '
							||(s.charAt(i)>='０'&& s.charAt(i)<='９'))
						{}
						else if(s.charAt(i) == '號')
						{
							isSymbol = true;
							index = s.length();
						}
						
					}
				}
			}
			
		}
		
		return isSymbol;
	}
	

	private static int ln_min = 10;
	private static int ln_max = 40;
	private static float ln_steep = 0.01f;

	/**
	 * Implemented as: <code>
	   * 1/sqrt( steepness * (abs(x-min) + abs(x-max) - (max-min)) + 1 )
	   * </code>.
	 * 
	 * <p>
	 * This degrades to <code>1/sqrt(x)</code> when min and max are both 1 and
	 * steepness is 0.5
	 * </p>
	 * 
	 * <p>
	 * :TODO: potential optimiation is to just flat out return 1.0f if numTerms
	 * is between min and max.
	 * </p>
	 */
	public static double sweetSpotLength(int length) {
		return (float) (1.0f / Math.sqrt((ln_steep * (float) (Math.abs(length
				- ln_min)
				+ Math.abs(length - ln_max) - (ln_max - ln_min))) + 1.0f));
	}
	
	private static float height_min = 0.1f;
	private static float height_max = 0.8f;

	/**
	 * Implemented as: <code>
	   * 1/sqrt( steepness * (abs(x-min) + abs(x-max) - (max-min)) + 1 )
	   * </code>.
	 * 
	 * <p>
	 * This degrades to <code>1/sqrt(x)</code> when min and max are both 1 and
	 * steepness is 0.5
	 * </p>
	 * 
	 * <p>
	 * :TODO: potential optimiation is to just flat out return 1.0f if numTerms
	 * is between min and max.
	 * </p>
	 */
	public static double sweetSpotHeight(float height) {
		return (1.0f / Math.sqrt((ln_steep * (Math.abs(height
				- height_min)
				+ Math.abs(height - height_max) - (height_max - height_min))) + 1.0f));
	}

	//
	public static boolean isYearTime(String sNum, int start) {
		int nLen = sNum.length();

		int i = start;
		while (i < nLen) {
			char c = sNum.charAt(i);
			// System.out.println(c);
			if (c < '0' || c > '9')
				break;
			i++;
		}
		if ((i - start) == 4)
			return true;

		return false;
	}
	
	/**
	 * 判斷是否發文機關
	 * @param s
	 * @param tcolor
	 * @return
	 */
	public static boolean isProSendGovUnit(String s,Color tcolor)
	{
		double pro = 0;
		
		if(tcolor.equals(Color.RED))
		{
			pro+=0.2;
		}
		
		if(s.endsWith("檔案"))
		{
			pro+=0.4;
		}
		
		int numBlank = 0;
		int numGovUnit = 0;
		for(int i=0; i<s.length(); i++)
		{
			char c = s.charAt(i);
			if(c == ' ')
			{
				numBlank ++;
			}
			else if(c == '廳'||
					c == '所'||
					c == '局'||
					c == '會'||
					c == '委'||
					c == '府')
				numGovUnit++;
		}
		if(numBlank > 0)
		{
			pro += (0.6*((double)numGovUnit+(double)numBlank)/((double)numBlank+s.length()));
		}
		//System.out.println("pro:"+pro);
		if(pro > 0.6)
			return true;
		return false;
	}
	
	/**
	 * 判斷是否收文機關
	 * @param s
	 * @param tcolor
	 * @return
	 */
	public static boolean isProReceiGovUnit(String s,Color tcolor)
	{
		if(!tcolor.equals(Color.BLACK))
		{
			return false;
		}
		
	    float pro =0 ;
		if(s.endsWith("：") || s.endsWith(":"))
		{
			pro += 0.5;
		}

		for(int i=0; i<s.length(); i++)
		{
			char c = s.charAt(i);
			if(c == '、'|| c == '（'|| c == '）'|| c == '，')
			{
				pro +=0.2;
			}
			else if(c == '廳'||
					c == '部'||
					c == '所'||
					c == '局'||
					c == '會'||
					c == '委'||
					c == '縣'||
					c == '區'||
					c == '市'||
					c == '省')
				pro +=0.11;
		}
		pro = pro/s.length();
		//System.out.println(pro);
		if(pro >= 0.07)
			return true;
	    return false;
	}

	public static double getHanziNum(String title) {
		double hanZiCount = 0;
		double markCount =1.0;
		for (int i = 0; i < title.length(); ++i) {
			char c = title.charAt(i);
			if (c >= 19968 && c <= 40869) {
				hanZiCount+=1.0;
			}
			if(c=='「'|| c=='」'||c=='：' || c=='，' )
			{
				markCount +=1.0;
			}
		}
		return hanZiCount/markCount;
	}
}
