package com.lietu.filter;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map.Entry;

import org.apache.poi.hwpf.HWPFDocument;
import org.apache.poi.hwpf.extractor.WordExtractor;
import org.apache.poi.hwpf.usermodel.CharacterRun;
import org.apache.poi.hwpf.usermodel.Paragraph;
import org.apache.poi.hwpf.usermodel.Range;
import org.apache.poi.hwpf.usermodel.Section;
import com.lietu.seg.result.Tagger;
import com.lietu.seg.result.CnToken;

public class WordReader {

	public static class TitleInfo {
		public String title, fontName;
		public int color, fontSize, position, mergeTo;
		public double weight;
		public HashMap<String, Double> words;//

		public TitleInfo(String t, int c, int fs, int posi, String fn) {
			title = t;
			color = c;
			fontSize = fs;
			weight = 1;
			fontName = fn;
			mergeTo = -1;
			position = posi;
		}
		
		public String toString()
		{
			return title + " -> Fontsize:"+fontSize +" color:"+color+" weight:"+weight;
		}
	}

	public static String readDoc(String filepath) throws Exception {
		//
		InputStream is = new FileInputStream(filepath);
		WordExtractor extractor = new WordExtractor(is);
		//	
		String text = extractor.getText();

		return text;
	}

	public static String stopwordFilePath = "";

	public static ArrayList<TitleInfo> getCandidates(String fileName,
			StringBuffer content) throws Exception {
		ArrayList<TitleInfo> titles = new ArrayList<TitleInfo>();
		InputStream is = new FileInputStream(fileName);
		HWPFDocument doc = new HWPFDocument(is);
		Range r = doc.getRange();
		Section s = r.getSection(0);

		int maxFontSize = 0;
		for (int i = 0; i < s.numParagraphs(); i++)
		{
			maxFontSize = Math.max(s.getParagraph(i).getCharacterRun(0)
					.getFontSize(), maxFontSize);
		}//
		
		int position = 0;
		for (int i = 0; i < s.numParagraphs(); i++) {
			Paragraph para = s.getParagraph(i);
			int maxFont = para.getCharacterRun(0).getFontSize();
			int justification = para.getJustification();
			
			if (justification == 1 || maxFont == maxFontSize)
			{
				//居中或字体最大的
				String title = "";
				
				for (int j = 0; j < para.numCharacterRuns(); j++) {
					CharacterRun run = para.getCharacterRun(j);

					title = title + run.text();
					maxFont = Math.max(maxFont, run.getFontSize());
					if (j == para.numCharacterRuns() - 1)
						titles.add(new TitleInfo(title, run.getColor(),
								maxFont, position, run.getFontName()));
				}
			} else // content part
			{
				for (int j = 0; j < para.numCharacterRuns(); j++) {
					content.append(para.getCharacterRun(j).text().trim() + " ");
				}
			}
			position ++;
		}
		is.close();
		
		return titles;
	}
	
	public static String getWordTitle(String filepath) throws Exception {
		StringBuffer content = new StringBuffer();
		ArrayList<TitleInfo> titles = getCandidates(filepath,content);
		if (titles.size() == 0)// 没有候选标题,暂时没做
			return "";
		else if (titles.size() == 1)
			return titles.get(0).title;
		else
			return getBestTitle(titles, content.toString());
	}

	@SuppressWarnings("finally")
	private static HashSet<String> getStopWords(String filePath) {
		HashSet<String> sw = new HashSet<String>();
		try {
			BufferedReader source = new BufferedReader(new FileReader(filePath));
			String sLine = null;

			while (true) {
				sLine = source.readLine();
				sw.add(sLine);
			}

		} catch (IOException e) {
			;
		} finally {
			return sw;
		}
	}

	private static String getBestTitle(ArrayList<TitleInfo> titles,
			String content) {
		// Tagger.segName = false;
		// Tagger.segSZ = false;
		HashSet<String> stopWords = getStopWords(stopwordFilePath);
		HashMap<String, Double> contentWords = new HashMap<String, Double>();

		int maxLength = 0;
		int maxFontSize = 0;
		int firstPosition = 9999;
		
		int width = 440;// 正文宽度
		for (int i = 0, j = 1; j < titles.size(); i++, j++)// 第一步：合并可能的标题
		{
			TitleInfo ti = titles.get(i);
			TitleInfo tj = titles.get(j);
			firstPosition = Math.min(firstPosition, ti.position);
			
			if (ti.color == tj.color && ti.fontSize == tj.fontSize
					&& ti.position +1 ==tj.position 
					&& titles.get(i).title.length() > 1
					&& titles.get(j).title.length() > 1)// 字体大小一样
			{
				if (!(tj.title.startsWith(" "))) {
					TitleInfo tTmp = ti;
					tj.mergeTo = i;
					while (tTmp.mergeTo != -1) {
						tj.mergeTo = tTmp.mergeTo;
						tTmp = titles.get(tTmp.mergeTo);
					}
					// 向前合并标题同时删除；
					titles.get(tj.mergeTo).title = titles.get(tj.mergeTo).title
							.trim()
							+ tj.title.trim();
					tj.title = "   ";
					if (ti.fontSize * ti.title.length() > width)// 因为字符过多而换行的
					{
						width *= 2;
						titles.get(tj.mergeTo).weight += 0.2;
					}
				}
			}
		}

		// 第二步：分词，确定候选标题的长度与位置范围
		for(TitleInfo m:titles)
		{
			if (m.title.trim().length() >= 2) {
				maxLength = Math.max(maxLength, m.title.length());
				maxFontSize = Math.max(maxFontSize, m.fontSize);

				// 标题分词 建向量
				ArrayList<CnToken> taggedTitle = Tagger
						.getFormatSegResult(m.title);
				// System.out.println(taggedTitle.size());
				m.words = new HashMap<String, Double>();
				for(CnToken ct:taggedTitle){
					if ("m".equals(ct.type()) || "t".equals(ct.type())
							|| stopWords.contains(ct.termText()))
						continue;// 去除废词

					Double val = m.words.get(ct.termText());
					if (val!=null) {
						m.words.put(ct.termText(), new Double(val + 1.0));
					} else
						m.words.put(ct.termText(), new Double(1.0));
				}
				// System.out.println(m.words.size());
			}
			m.position -= firstPosition ;
		}
		
		// 正文分词，建向量
		ArrayList<CnToken> taggedContent = Tagger.getFormatSegResult(content);
		
		for(CnToken ct:taggedContent)
		{
			if ("w".equals(ct.type()) || "m".equals(ct.type())
					|| "t".equals(ct.type())
					|| stopWords.contains(ct.termText()))
				continue;// 去除废词

			Double val = contentWords.get(ct.termText());
			if (val!=null) {
				contentWords.put(ct.termText(), new Double(val + 1));
			} else
				contentWords.put(ct.termText(), new Double(1.0));
		}
		double contentNorm = calculateNorm(contentWords);

		// 第三步：综合评价候选标题权重，
		double max = 0;
		int maxid = 0;
		for (int i = 0; i < titles.size(); i++)
		{
			TitleInfo t = titles.get(i);
			if (t.title.trim().length() >= 2) {
				double lengthWeight = getLengthWeight(t.title.length());
				double fontSizeWeight = getFontSizeWeight(t.fontSize,
						maxFontSize);
				double positionWeight = getPositionWeight(t.position);
				double semanticWeight = getSimilarity(t.words, contentWords,
						contentNorm);

				Double compositiveWeight = new Double(t.weight
						* Math.pow(lengthWeight * fontSizeWeight
								* positionWeight, 1.0 / 3) * semanticWeight);

				if (compositiveWeight >= max) {
					max = compositiveWeight;
					maxid = i;
				}
			}
		}

		return titles.get(maxid).title;
	}

	private static double getPositionWeight(int position) {
	//  return (double)(maxPosition - position)/maxPosition;
	//	double eachStep = (double) maxPosition / 10;
	//	return 1.0 - 0.1 * (int) ((double) position / eachStep);
		return 2.5 * Math.log(position + 2.0)/(position + 2.0) - 0.2 ;
	}

	private static double getFontSizeWeight(int fontSize, int maxFontSize) {
		// 字体越大值越大，线性单调递减
		return (double) fontSize / maxFontSize;
	}

	private static double getLengthWeight(int titleLength) {
		// 凸函数 20个字权值最大？
		if (titleLength <= 20)
			return (double) (titleLength + 5) / 25;
		else if (titleLength > 60)
			return 0.2;
		else
			return 1.0 - ((double) (titleLength - 20) / 40) * 0.8;
	}

	private static double getSimilarity(HashMap<String, Double> titleWords,
			HashMap<String, Double> contentWords, double contentNorm) {
		double innerProduct = 0;
		double titleNorm = 0;

		for (Entry<String, Double> tword : titleWords.entrySet()) {
			titleNorm += tword.getValue() * tword.getValue();
			if (contentWords.containsKey(tword.getKey()))
				innerProduct += tword.getValue()
						* contentWords.get(tword.getKey());
		}
		return innerProduct / Math.sqrt(titleNorm * contentNorm);
	}

	private static double calculateNorm(HashMap<String, Double> contentWords) {
		double contentNorm = 0;
		for (Entry<String, Double> word : contentWords.entrySet())
			contentNorm += word.getValue() * word.getValue();
		return contentNorm;
	}

}