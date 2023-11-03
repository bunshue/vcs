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

	//�Կ���D��T
	public static class TitleInfo {
		public String fontName; //�r��W
		public int fontSize; //�r��j�p
		public int position; //��m��T
		public int mergeTo; //�X�ֶ��s��
		public boolean isBold; //�O�_����
		public String text; //���e
		public HashMap<String, Double> words; //���e�������G
		public double weight; //�v��

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

		if (candidates == null || candidates.size() == 0)// �S���Կ���D
			return "";
		else if (candidates.size() == 1)
			return candidates.get(0).text;
		else {
			// �Կ���D����
			rankTitle(candidates, content.toString());
			// ������̰����Կ���D�@�����D���R���G
			return getBestTitle(candidates);
		}
	}

	public static ArrayList<TitleInfo> getCandidates(String fileName,
			StringBuffer content) throws Exception {
		IRtfGroup rtfStructure = ParseRtf(fileName);// ��oRTF���c

		RtfInterpreterListenerDocumentBuilder docBuilder = new RtfInterpreterListenerDocumentBuilder(); // ��l��
		RtfInterpreterListenerLogger interpreterLogger = null;

		RtfInterpreterTool.Interpret(rtfStructure, interpreterLogger,
				docBuilder);

		RtfDocument doc = (RtfDocument) docBuilder.getDocument();

		if (doc == null)//Ū������
			return null;
		ArrayList<IRtfVisual> rtfVisuals = doc.getVisualContent();

		int maxFontSize = 0;
		int maxPosition = 0;
		for (IRtfVisual rtfv : rtfVisuals)// ��̤j�r��
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

			if (RtfVisualKind.Text == rtfv.getKind())//�u��Text�~����r�ݩ�
			{
				// ����e�H�Ĥ@�ئr�Ů榡�@�����榡�A���F�r��j�p�C
				String fontName = ((IRtfVisualText) (rtfv)).getFormat()
						.getFont().getName();// ���r�Ŧr��
				Color tc = ((IRtfVisualText) (rtfv)).getFormat()
						.getForegroundColor().getAsDrawingColor();
				boolean isBold = ((IRtfVisualText) (rtfv)).getFormat()
						.getIsBold();
				RtfTextAlignment alignment = ((IRtfVisualText) (rtfv))
						.getFormat().getAlignment();
				int fontSize = ((IRtfVisualText) (rtfv)).getFormat()
						.getFontSize();

				String oneRow = "";
				while (RtfVisualKind.Break != rtfv.getKind())// ����e�������O�@�Ӿ���
				{
					try {// Special, Image���L�k�j���ഫ��Text

						oneRow += ((IRtfVisualText) (rtfv)).getText();
					} catch (Exception e) {
						;
					}
					i++;
					rtfv = rtfVisuals.get(i);
				}

				//�����ݩʧP�_
				if (isProSendGovUnit(oneRow, tc)
						|| isProReceiGovUnit(oneRow, tc) || isFileNum(oneRow)) {
					maxPosition++;
					continue;
				}

				if (RtfTextAlignment.Center == alignment
						|| fontSize == maxFontSize) {// �~���B�̤j�r��[�J�Կ���D
					candidates.add(new TitleInfo(oneRow, fontSize, maxPosition,
							fontName, isBold));
				} else
					// ���~�����O���夺�e
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
		int width = 440;// ����e��
		int firstPosition = 9999;

		for (int i = 0, j = 1; j < titles.size(); i++, j++)// �Ĥ@�B�G�X�֥i�઺���D
		{
			TitleInfo ti = titles.get(i);
			TitleInfo tj = titles.get(j);
			firstPosition = Math.min(firstPosition, ti.position);
			if (ti.fontSize == tj.fontSize // �r��j�p�@�P
					&& ti.position + 1 == tj.position // �W�U�s�e
					&& titles.get(i).text.length() > 1
					&& titles.get(j).text.length() > 1)// �r��j�p�@��
			{
				if (!(tj.text.startsWith(" "))) {
					TitleInfo tTmp = ti;
					tj.mergeTo = i;
					while (tTmp.mergeTo != -1) {
						tj.mergeTo = tTmp.mergeTo;
						tTmp = titles.get(tTmp.mergeTo);
					}
					// �V�e�X�ּ��D�P�ɧR���F
					titles.get(tj.mergeTo).text = titles.get(tj.mergeTo).text
							.trim()
							+ tj.text.trim();
					tj.text = "   ";
					if (ti.fontSize * ti.text.length() > width)// �]���r�ŹL�h�Ӵ��檺
					{
						width *= 2;
						titles.get(tj.mergeTo).weight += 0.2;
					}
				}
			}
		}

		for (TitleInfo m : titles)// �ĤG�B�G�����A�T�w�Կ���D�����׻P��m�d��
		{
			if (m.text.trim().length() >= 2)// �D�ż��D����
			{
				maxLength = Math.max(maxLength, m.text.length());
				maxFontSize = Math.max(maxFontSize, m.fontSize);

				// ���D���� �ئV�q
				ArrayList<CnToken> taggedTitle = Tagger
						.getFormatSegResult(m.text);

				m.words = new HashMap<String, Double>();
				for (CnToken ct : taggedTitle) {
					if ("m".equals(ct.type()) || "t".equals(ct.type())
							|| stopWords.contains(ct.termText()))
						continue;// �h���o��

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
		// ��������A�ئV�q
		ArrayList<CnToken> taggedContent = Tagger.getFormatSegResult(content);
		for (CnToken ct : taggedContent) {
			if ("w".equals(ct.type()) || "m".equals(ct.type())
					|| "t".equals(ct.type())
					|| stopWords.contains(ct.termText()))
				continue;// �h�����ε�

			if (contentWords.containsKey(ct.termText())) {
				contentWords.put(ct.termText(), new Double(contentWords.get(ct
						.termText()) + 1));
			} else
				contentWords.put(ct.termText(), new Double(1.0));
		}
		double contentNorm = calculateNorm(contentWords);

		for (int i = 0; i < titles.size(); i++)// �ĤT�B�G��X�����Կ���D�v���A
		{
			TitleInfo t = titles.get(i);
			if (t.text.trim().length() >= 2) {
				double lengthWeight = getLengthWeight(t.text.length());
				double fontSizeWeight = getFontSizeWeight(t.fontSize,
						maxFontSize);
				double positionWeight = getPositionWeight(t.position);
				//�p��i����D�P���媺�ۦ��סA�Χ����l���ӿŶq�ۦ���
				double semanticWeight = getSimilarity(t.words, contentWords,
						contentNorm);

				//�p���X�v��
				Double compositiveWeight = new Double(t.weight
						* Math.pow(lengthWeight * fontSizeWeight
								* positionWeight, 1.0 / 3) * semanticWeight);
				//�o�X���D���̲��v��
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

	private static double getPositionWeight(int position) {// ��m�j���b50�H�᪺���|�p�⬰0�A
															// �e3���ȳ�����j�A
		return 2.5 * Math.log(position + 2.0) / (position + 2.0) - 0.2;
	}

	private static double getFontSizeWeight(int fontSize, int maxFontSize) {
		// �r��V�j�ȶV�j�A�u�ʳ�ջ���
		return (double) fontSize / maxFontSize;
	}

	private static double getLengthWeight(int titleLength) {
		// �Y��� 20�Ӧr�v�ȳ̤j�H
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

		if (s.endsWith("�ɮ�")) {
			pro += 0.4;
		}

		int numBlank = 0;
		int numGovUnit = 0;
		for (int i = 0; i < s.length(); i++) {
			char c = s.charAt(i);
			if (c == ' ') {
				numBlank++;
			} else if (c == '�U' || c == '��' || c == '��' || c == '�|' || c == '�e'
					|| c == '��')
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
		if (s.endsWith("�G") || s.endsWith(":")) {
			pro += 0.5;
		}

		for (int i = 0; i < s.length(); i++) {
			char c = s.charAt(i);
			if (c == '�B' || c == '�]' || c == '�^' || c == '�A') {
				pro += 0.2;
			} else if (c == '�U' || c == '��' || c == '��' || c == '��' || c == '�|'
					|| c == '�e' || c == '��' || c == '��' || c == '��' || c == '��')
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
								|| (s.charAt(i) >= '��' && s.charAt(i) <= '��')) {
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
								|| (s.charAt(i) >= '��' && s.charAt(i) <= '��')) {
						} else if (s.charAt(i) == '��') {
							isSymbol = true;
							index = s.length();
						}
					}
				}
			} else if ('�]' == s.charAt(index)) {
				markBegSym = true;
				for (int i = index + 1; i < s.length(); i++) {
					if (!markEndSym) {
						if ((s.charAt(i) >= '0' && s.charAt(i) <= '9')
								|| s.charAt(i) == ' '
								|| (s.charAt(i) >= '��' && s.charAt(i) <= '��')) {
						} else if (s.charAt(i) == '�^') {
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
								|| (s.charAt(i) >= '��' && s.charAt(i) <= '��')) {
						} else if (s.charAt(i) == '��') {
							isSymbol = true;
							index = s.length();
						}

					}
				}
			} else if ('�e' == s.charAt(index)) {
				markBegSym = true;
				for (int i = index + 1; i < s.length(); i++) {
					if (!markEndSym) {
						if ((s.charAt(i) >= '0' && s.charAt(i) <= '9')
								|| s.charAt(i) == ' '
								|| (s.charAt(i) >= '��' && s.charAt(i) <= '��')) {
						} else if (s.charAt(i) == '�f') {
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
								|| (s.charAt(i) >= '��' && s.charAt(i) <= '��')) {
						} else if (s.charAt(i) == '��') {
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