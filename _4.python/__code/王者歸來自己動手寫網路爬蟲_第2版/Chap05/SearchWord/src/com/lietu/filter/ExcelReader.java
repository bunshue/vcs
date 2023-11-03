package com.lietu.filter;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Iterator;

import org.apache.poi.hssf.extractor.ExcelExtractor;
import org.apache.poi.hssf.usermodel.HSSFCell;
import org.apache.poi.hssf.usermodel.HSSFCellStyle;
import org.apache.poi.hssf.usermodel.HSSFFont;
import org.apache.poi.hssf.usermodel.HSSFRow;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.poifs.filesystem.POIFSFileSystem;

public class ExcelReader {

	/**
	 * @param args
	 */
	public class CellInfo 
	{
		public String text;//文本内容
		public short fontSize;//字体大小
		public short alignment;//对齐方式
		public boolean boldness;//是否黑体
		public int rowPos;//所在行的位置
		public double weight;//重要度
		public boolean isUnique;//独立成行
		public CellInfo(String t, short fs, int rp, short align, boolean bold){
			text = t;
			fontSize = fs;
			rowPos = rp;
			alignment = align;
			boldness = bold;
			weight = 1.0;
			isUnique = false;
		}
	}
	
	public class TitleInf
	{
		public String text;//文本内容
		public double weight;//重要度
		
		public TitleInf(String t, double w)
		{
			text = t;
			weight = w;
		}
	}
	
	public static String readDoc(String fileurl) throws Exception {
		InputStream is = new FileInputStream(fileurl);
		HSSFWorkbook wb = new HSSFWorkbook(new POIFSFileSystem(is));
		ExcelExtractor extractor = new ExcelExtractor(wb);

		extractor.setFormulasNotResults(true);
		extractor.setIncludeSheetNames(false);
		String text = extractor.getText();
		//text = StringFilter.filterExcel(text);
		is.close();
		return text;
	}
	
	private TitleInf getSheetBestTitle(HSSFSheet sheet, HSSFWorkbook wb)
	{
		Iterator<HSSFRow> riter = sheet.rowIterator();//按行遍历工作表
		ArrayList<CellInfo> titles = new ArrayList<CellInfo>();
		
		int maxFontSize = 0;
		int rowCount = 0;
		while (riter.hasNext())
		{
			rowCount ++;
			int columnCount = 0;
			HSSFRow row = (HSSFRow) riter.next();
			Iterator<HSSFCell> citer = row.cellIterator();//每行再按列遍历
			
			while(citer.hasNext())
			{
				HSSFCell cell = citer.next();
				int cellType = cell.getCellType();
				HSSFCellStyle cellStyle = cell.getCellStyle();
				
				if (cellType != HSSFCell.CELL_TYPE_BLANK )//非空
				{
					columnCount ++;
				}
				if (cellType == HSSFCell.CELL_TYPE_STRING) //字符型
				{
					String cellString =  cell.toString().trim();//取得单元格内的文本
					if (cellString.length() >= 2)
					{
						HSSFFont cellFont = cell.getCellStyle().getFont(wb);
						
						short fontheight = cellFont.getFontHeight();
						short al = cellStyle.getAlignment();
						short boldness = cellFont.getBoldweight() ;
						maxFontSize = Math.max(maxFontSize, (int)fontheight);
						CellInfo ci = new CellInfo(cellString,
													fontheight,
													rowCount,
													al,
													boldness == HSSFFont.BOLDWEIGHT_BOLD);
						titles.add(ci);
					}
				}
			}
			if (columnCount == 1) //这行只有这个
				titles.get(titles.size() - 1).isUnique = true;
		}
		
		if (titles.size() == 0)
			return new TitleInf("",0);
		else 
			return selectBestTitle(titles, maxFontSize, rowCount);
	}
	
	public String getTitle(String fileName) throws Exception
	{
		InputStream is = new FileInputStream(fileName);
		HSSFWorkbook wb = new HSSFWorkbook(new POIFSFileSystem(is));
		ArrayList<TitleInf> candidate = new ArrayList<TitleInf>();
		int activeSheetIndex = wb.getSelectedTab();//或者调用wb.getActiveSheetIndex();
		
		int sheetsNum = wb.getNumberOfSheets();
		for (int i = 0 ; i < sheetsNum ; i++)
		{
			TitleInf bti = getSheetBestTitle(wb.getSheetAt(i),  wb);
			if (i == activeSheetIndex)
				bti.weight *= 3.0;
			candidate.add(bti);
		}
		
		//取得最评分最高的候选标题
		double maxWeight = 0;
		String bestTitle = null;
		for (TitleInf curTitle : candidate)
		{
			if (curTitle.weight >= maxWeight){
				maxWeight = curTitle.weight;
				bestTitle = curTitle.text;
			}
		}

		is.close();
		return bestTitle;
	}
	
	private TitleInf selectBestTitle(ArrayList<CellInfo> titles, int maxFontSize, int rowNum)
	{
		double max = 0;
		int maxid = 0;
		double compositiveWeight = 0;
		double fontSizeWeight;
		double positionWeight;
		double LengthWeight;
		
		for( int i = 0; i< titles.size(); i++)
		{
			CellInfo ci = titles.get(i);
			fontSizeWeight = getFontSizeWeight(ci.fontSize, maxFontSize);
			positionWeight = getPositionWeight(ci.rowPos, rowNum);
			LengthWeight = getLengthWeight(ci.text.length());
			compositiveWeight = fontSizeWeight * positionWeight * LengthWeight;
			
			if (ci.boldness)// 粗体
				compositiveWeight *= 1.2;
			
			if (ci.alignment == HSSFCellStyle.ALIGN_CENTER) //居中
				compositiveWeight *= 1.3;
			
			if (ci.isUnique == true)//此行唯一，是标题概率大
				compositiveWeight *= 2.0;
			
			ci.weight = compositiveWeight;
			if (compositiveWeight >= max){
				max = compositiveWeight;
				maxid = i;
			}
		}
		
		return new TitleInf(titles.get(maxid).text, titles.get(maxid).weight);
	}
	
	private static double getPositionWeight(int position, int maxPosition)
	{
		//越前越大，最简单的方式：线性单调递减？
		return (double)(maxPosition - position)/maxPosition;
		//分10段 阶梯递减；
		//double eachStep = (double)maxPosition / 10;
		//return 1.0 - 0.1 * (int)((double)position / eachStep );
	}
	
	private static double getFontSizeWeight(int fontSize, int maxFontSize)
	{
		//字体越大值越大，线性单调递减
		return (double)fontSize / maxFontSize;
	}
	
	private static double getLengthWeight(int titleLength)
	{
		//凸函数 20个字权值最大？
		if (titleLength <= 15)
			return (double)(titleLength + 5) / 20;
		else if (titleLength > 50)
			return 0.2;
		else
			return  1.0 - ((double)(titleLength - 15) / 35) * 0.8; 
	}

	public static String readDoc(InputStream is) throws IOException{
		HSSFWorkbook wb = new HSSFWorkbook(new POIFSFileSystem(is));
		ExcelExtractor extractor = new ExcelExtractor(wb);
	
		extractor.setFormulasNotResults(true);
		extractor.setIncludeSheetNames(false);
		String text = extractor.getText();
		return text;
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		//application/vnd.ms-powerpoint
		try{
			String fileName = "D:/aa.xls";
			InputStream is = new FileInputStream(fileName);
			String text=ExcelReader.readDoc(is);
			//System.out.println(getTitle(text));
			System.out.println(text);
			
			ExcelReader er = new ExcelReader();
			
			String aa = er.getTitle(fileName);
			System.out.println(aa);
		}catch(Exception e){
			e.printStackTrace();
		}
	}}
