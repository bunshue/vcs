package com.lietu.rtf.extract;

import java.awt.Color;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map.Entry;

import com.lietu.rtf.IRtfGroup;
import com.lietu.rtf.IRtfVisual;
import com.lietu.rtf.IRtfVisualText;
import com.lietu.rtf.RtfTextAlignment;
import com.lietu.rtf.RtfVisualKind;
import com.lietu.rtf.converter.text.RtfTextConverter;
import com.lietu.rtf.interpreter.RtfInterpreterListenerDocumentBuilder;
import com.lietu.rtf.interpreter.RtfInterpreterListenerFileLogger;
import com.lietu.rtf.interpreter.RtfInterpreterListenerLogger;
import com.lietu.rtf.model.RtfDocument;
import com.lietu.rtf.parser.RtfParser;
import com.lietu.rtf.parser.RtfParserListenerFileLogger;
import com.lietu.rtf.parser.RtfParserListenerStructureBuilder;
import com.lietu.rtf.parser.RtfSource;
import com.lietu.rtf.support.RtfInterpreterTool;
import com.lietu.seg.result.CnToken;
import com.lietu.seg.result.Tagger;

public class RTFReader {

	//候選標題資訊
	public static class TitleInfo {
		public String fontName; //字體名
		public int fontSize; //字體大小
		public int position; //位置資訊
		public int mergeTo; //合併塊編號
		public boolean isBold; //是否粗體
		public String text; //內容
		public HashMap<String, Double> words; //內容切分結果
		public double weight; //權重

		public TitleInfo(String t, int fs, int posi, String fn, boolean ibold) {
			text = t;
			fontSize = fs;
			weight = 1;
			fontName = fn;
			mergeTo = -1;
			isBold = ibold;
			position = posi;
		}

		public String toString() {
			return text + " fontSize:" + fontSize + " weight:" + weight;
		}
	}

	/**
	 * Get raw content of a RTF format file
	 * 
	 * @param fileurl
	 *            The filepath of the input rtf
	 * @return raw content of the rtf
	 * @throws Exception
	 */
	public static String readDoc(String fileurl) throws Exception {
		IRtfGroup rtfStructure = ParseRtf(fileurl);

		RtfInterpreterListenerFileLogger interpreterLogger = null;

		RtfTextConverter textConverter = new RtfTextConverter();

		RtfInterpreterTool.Interpret(rtfStructure, interpreterLogger,
				textConverter);

		String text = textConverter.getPlainText();

		return text;
	}

	private static String GetResource(String fileName) throws IOException {
		BufferedReader input = new BufferedReader(new FileReader(fileName));
		StringBuilder str = new StringBuilder();

		String line;
		while ((line = input.readLine()) != null) {
			str.append(line);
		}
		input.close();
		return str.toString();
	}

	/**
	 * Parse rtf file to a special structure
	 * 
	 * @param sourceFile
	 * @return IRtfGroup
	 * @throws Exception
	 */
	private static IRtfGroup ParseRtf(String sourceFile) throws Exception {
		IRtfGroup rtfStructure = null;
		RtfParserListenerFileLogger parserLogger = null;

		String stream = GetResource(sourceFile);

		RtfParserListenerStructureBuilder structureBuilder = new RtfParserListenerStructureBuilder();
		RtfParser parser = new RtfParser(structureBuilder);

		parser.setIgnoreContentAfterRootGroup(true);
		if (parserLogger != null) {
			parser.AddParserListener(parserLogger);
		}

		parser.Parse(new RtfSource(stream));
		rtfStructure = structureBuilder.getStructureRoot();

		return rtfStructure;
	}

	/**
	 * Get the title of a RTF file
	 * 
	 * @param fileName
	 *            The filepath of the input rtf
	 * @return Title string
	 * @throws Exception
	 */
	public static String getRtfTitle(String fileName) throws Exception {
		StringBuffer content = new StringBuffer();

		ArrayList<TitleInfo> candidates = getCandidates(fileName, content);

		if (candidates == null || candidates.size() == 0)// 沒有候選標題
			return "";
		else if (candidates.size() == 1)
			return candidates.get(0).text;
		else {
			// 候選標題評分
			rankTitle(candidates, content.toString());
			// 把評分最高的候選標題作為標題分析結果
			return getBestTitle(candidates);
		}
	}

	public static ArrayList<TitleInfo> getCandidates(String fileName,
			StringBuffer content) throws Exception {
		IRtfGroup rtfStructure = ParseRtf(fileName);// 獲得RTF結構

		RtfInterpreterListenerDocumentBuilder docBuilder = new RtfInterpreterListenerDocumentBuilder(); // 初始化
		RtfInterpreterListenerLogger interpreterLogger = null;

		RtfInterpreterTool.Interpret(rtfStructure, interpreterLogger,
				docBuilder);

		RtfDocument doc = (RtfDocument) docBuilder.getDocument();

		if (doc == null)//讀取失敗
			return null;
		ArrayList<IRtfVisual> rtfVisuals = doc.getVisualContent();

		int maxFontSize = 0;
		int maxPosition = 0;
		for (IRtfVisual rtfv : rtfVisuals)// 找最大字體
		{
			try {
				maxFontSize = Math.max(((IRtfVisualText) (rtfv)).getFormat()
						.getFontSize(), maxFontSize);
			} catch (Exception e) {
			}
		}

		ArrayList<TitleInfo> candidates = new ArrayList<TitleInfo>();
		for (int i = 0; i < rtfVisuals.size(); i++) {
			IRtfVisual rtfv = rtfVisuals.get(i);

			if (RtfVisualKind.Text == rtfv.getKind())//只有Text才有文字屬性
			{
				// 換行前以第一種字符格式作為整行格式，除了字體大小。
				String fontName = ((IRtfVisualText) (rtfv)).getFormat()
						.getFont().getName();// 首字符字體
				Color tc = ((IRtfVisualText) (rtfv)).getFormat()
						.getForegroundColor().getAsDrawingColor();
				boolean isBold = ((IRtfVisualText) (rtfv)).getFormat()
						.getIsBold();
				RtfTextAlignment alignment = ((IRtfVisualText) (rtfv))
						.getFormat().getAlignment();
				int fontSize = ((IRtfVisualText) (rtfv)).getFormat()
						.getFontSize();

				String oneRow = "";
				while (RtfVisualKind.Break != rtfv.getKind())// 換行前的部分是一個整體
				{
					try {// Special, Image類無法強制轉換成Text

						oneRow += ((IRtfVisualText) (rtfv)).getText();
					} catch (Exception e) {
						;
					}
					i++;
					rtfv = rtfVisuals.get(i);
				}

				//公文屬性判斷
				if (isProSendGovUnit(oneRow, tc)
						|| isProReceiGovUnit(oneRow, tc) || isFileNum(oneRow)) {
					maxPosition++;
					continue;
				}

				if (RtfTextAlignment.Center == alignment
						|| fontSize == maxFontSize) {// 居中、最大字體加入候選標題
					candidates.add(new TitleInfo(oneRow, fontSize, maxPosition,
							fontName, isBold));
				} else
					// 不居中的是正文內容
					content.append(oneRow + " ");
			}
			maxPosition++;
		}

		return candidates;
	}

	public static void rankTitle(ArrayList<TitleInfo> titles, String content) {
		HashSet<String> stopWords = StopSet.getInstance();
		HashMap<String, Double> contentWords = new HashMap<String, Double>();

		int maxLength = 0;
		int maxFontSize = 0;
		int width = 440;// 正文寬度
		int firstPosition = 9999;

		for (int i = 0, j = 1; j < titles.size(); i++, j++)// 第一步：合併可能的標題
		{
			TitleInfo ti = titles.get(i);
			TitleInfo tj = titles.get(j);
			firstPosition = Math.min(firstPosition, ti.position);
			if (ti.fontSize == tj.fontSize // 字體大小一致
					&& ti.position + 1 == tj.position // 上下連貫
					&& titles.get(i).text.length() > 1
					&& titles.get(j).text.length() > 1)// 字體大小一樣
			{
				if (!(tj.text.startsWith(" "))) {
					TitleInfo tTmp = ti;
					tj.mergeTo = i;
					while (tTmp.mergeTo != -1) {
						tj.mergeTo = tTmp.mergeTo;
						tTmp = titles.get(tTmp.mergeTo);
					}
					// 向前合併標題同時刪除；
					titles.get(tj.mergeTo).text = titles.get(tj.mergeTo).text
							.trim()
							+ tj.text.trim();
					tj.text = "   ";
					if (ti.fontSize * ti.text.length() > width)// 因為字符過多而換行的
					{
						width *= 2;
						titles.get(tj.mergeTo).weight += 0.2;
					}
				}
			}
		}

		for (TitleInfo m : titles)// 第二步：分詞，確定候選標題的長度與位置範圍
		{
			if (m.text.trim().length() >= 2)// 非空標題分詞
			{
				maxLength = Math.max(maxLength, m.text.length());
				maxFontSize = Math.max(maxFontSize, m.fontSize);

				// 標題分詞 建向量
				ArrayList<CnToken> taggedTitle = Tagger
						.getFormatSegResult(m.text);

				m.words = new HashMap<String, Double>();
				for (CnToken ct : taggedTitle) {
					if ("m".equals(ct.type()) || "t".equals(ct.type())
							|| stopWords.contains(ct.termText()))
						continue;// 去除廢詞

					Double val = m.words.get(ct.termText());
					if (val != null) {
						m.words.put(ct.termText(), new Double(val + 1.0));
					} else
						m.words.put(ct.termText(), new Double(1.0));
				}
				//
				// System.out.println(m.words.size());
			}
			m.position -= firstPosition;
		}
		// 正文分詞，建向量
		ArrayList<CnToken> taggedContent = Tagger.getFormatSegResult(content);
		for (CnToken ct : taggedContent) {
			if ("w".equals(ct.type()) || "m".equals(ct.type())
					|| "t".equals(ct.type())
					|| stopWords.contains(ct.termText()))
				continue;// 去除停用詞

			if (contentWords.containsKey(ct.termText())) {
				contentWords.put(ct.termText(), new Double(contentWords.get(ct
						.termText()) + 1));
			} else
				contentWords.put(ct.termText(), new Double(1.0));
		}
		double contentNorm = calculateNorm(contentWords);

		for (int i = 0; i < titles.size(); i++)// 第三步：綜合評價候選標題權重，
		{
			TitleInfo t = titles.get(i);
			if (t.text.trim().length() >= 2) {
				double lengthWeight = getLengthWeight(t.text.length());
				double fontSizeWeight = getFontSizeWeight(t.fontSize,
						maxFontSize);
				double positionWeight = getPositionWeight(t.position);
				//計算可選標題與全文的相似度，用夾角餘弦來衡量相似度
				double semanticWeight = getSimilarity(t.words, contentWords,
						contentNorm);

				//計算綜合權重
				Double compositiveWeight = new Double(t.weight
						* Math.pow(lengthWeight * fontSizeWeight
								* positionWeight, 1.0 / 3) * semanticWeight);
				//得出標題的最終權重
				if (t.isBold)
					t.weight = compositiveWeight * 1.1;
				else
					t.weight = compositiveWeight;
			}
		}
	}

	public static String getBestTitle(ArrayList<TitleInfo> titles) {
		double max = 0;
		String bestTitle = null;
		for (TitleInfo t : titles) {
			if (t.weight > max && t.text.trim().length() >= 2) {
				max = t.weight;
				bestTitle = t.text;
			}
		}

		return bestTitle;
	}

	private static double getPositionWeight(int position) {// 位置大約在50以後的都會計算為0，
															// 前3的值都比較大，
		return 2.5 * Math.log(position + 2.0) / (position + 2.0) - 0.2;
	}

	private static double getFontSizeWeight(int fontSize, int maxFontSize) {
		// 字體越大值越大，線性單調遞減
		return (double) fontSize / maxFontSize;
	}

	private static double getLengthWeight(int titleLength) {
		// 凸函數 20個字權值最大？
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

	public static boolean isProSendGovUnit(String s, Color tcolor) {
		double pro = 0;

		if (tcolor.equals(Color.RED)) {
			pro += 0.2;
		}

		if (s.endsWith("檔案")) {
			pro += 0.4;
		}

		int numBlank = 0;
		int numGovUnit = 0;
		for (int i = 0; i < s.length(); i++) {
			char c = s.charAt(i);
			if (c == ' ') {
				numBlank++;
			} else if (c == '廳' || c == '所' || c == '局' || c == '會' || c == '委'
					|| c == '府')
				numGovUnit++;
		}
		if (numBlank > 0) {
			pro += (0.6 * ((double) numGovUnit + (double) numBlank) / ((double) numBlank + s
					.length()));
		}
		// System.out.println("pro:"+pro);
		if (pro > 0.6)
			return true;
		return false;
	}

	public static boolean isProReceiGovUnit(String s, Color tcolor) {
		if (!tcolor.equals(Color.BLACK)) {
			return false;
		}

		float pro = 0;
		if (s.endsWith("：") || s.endsWith(":")) {
			pro += 0.5;
		}

		for (int i = 0; i < s.length(); i++) {
			char c = s.charAt(i);
			if (c == '、' || c == '（' || c == '）' || c == '，') {
				pro += 0.2;
			} else if (c == '廳' || c == '部' || c == '所' || c == '局' || c == '會'
					|| c == '委' || c == '縣' || c == '區' || c == '市' || c == '省')
				pro += 0.11;
		}
		pro = pro / s.length();
		// System.out.println(pro);
		if (pro >= 0.07)
			return true;
		return false;
	}

	public static boolean isFileNum(String s) {
		boolean isSymbol = false;

		boolean markBegSym = false;
		boolean markEndSym = false;

		for (int index = 0; index < s.length(); index++) {
			if ('[' == s.charAt(index)) {
				markBegSym = true;
				for (int i = index + 1; i < s.length(); i++) {
					if (!markEndSym) {
						if ((s.charAt(i) >= '0' && s.charAt(i) <= '9')
								|| s.charAt(i) == ' '
								|| (s.charAt(i) >= '０' && s.charAt(i) <= '９')) {
						} else if (s.charAt(i) == ']') {
							markEndSym = true;
							i++;
						} else {
							markBegSym = false;
							markEndSym = false;
						}
					}
					if (markBegSym && markEndSym) {
						if ((s.charAt(i) >= '0' && s.charAt(i) <= '9')
								|| s.charAt(i) == ' '
								|| (s.charAt(i) >= '０' && s.charAt(i) <= '９')) {
						} else if (s.charAt(i) == '號') {
							isSymbol = true;
							index = s.length();
						}
					}
				}
			} else if ('（' == s.charAt(index)) {
				markBegSym = true;
				for (int i = index + 1; i < s.length(); i++) {
					if (!markEndSym) {
						if ((s.charAt(i) >= '0' && s.charAt(i) <= '9')
								|| s.charAt(i) == ' '
								|| (s.charAt(i) >= '０' && s.charAt(i) <= '９')) {
						} else if (s.charAt(i) == '）') {
							markEndSym = true;
							i++;
						} else {
							markBegSym = false;
							markEndSym = false;
						}
					}
					if (markBegSym && markEndSym) {
						if ((s.charAt(i) >= '0' && s.charAt(i) <= '9')
								|| s.charAt(i) == ' '
								|| (s.charAt(i) >= '０' && s.charAt(i) <= '９')) {
						} else if (s.charAt(i) == '號') {
							isSymbol = true;
							index = s.length();
						}

					}
				}
			} else if ('〔' == s.charAt(index)) {
				markBegSym = true;
				for (int i = index + 1; i < s.length(); i++) {
					if (!markEndSym) {
						if ((s.charAt(i) >= '0' && s.charAt(i) <= '9')
								|| s.charAt(i) == ' '
								|| (s.charAt(i) >= '０' && s.charAt(i) <= '９')) {
						} else if (s.charAt(i) == '〕') {
							markEndSym = true;
							i++;
						} else {
							markBegSym = false;
							markEndSym = false;
						}
					}
					if (markBegSym && markEndSym) {
						if ((s.charAt(i) >= '0' && s.charAt(i) <= '9')
								|| s.charAt(i) == ' '
								|| (s.charAt(i) >= '０' && s.charAt(i) <= '９')) {
						} else if (s.charAt(i) == '號') {
							isSymbol = true;
							index = s.length();
						}

					}
				}
			}

		}

		return isSymbol;
	}

}