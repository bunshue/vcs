using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Collections;   //for ArrayList
using System.IO;

using System.Text.RegularExpressions;
using System.Diagnostics;

/*
用C#寫的讀寫CSV文件，

用C#寫的讀取CSV文件的源代碼

CSV文件的格子中包含逗號，引號，換行等，都能輕松讀取，而且可以把數據轉化成DATATABLE格式
*/

namespace vcs_ReadWrite_CSV7
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //讀取一CSV檔至DataTable

        }
    }



    #region 類說明信息

    /// <summary>
    ///  <DL>
    ///  <DT><b>讀CSV文件類,讀取指定的CSV文件，可以導出DataTable</b></DT>
    ///   <DD>
    ///    <UL> 
    ///    </UL>
    ///   </DD>
    ///  </DL>
    ///  <Author>yangzhihong</Author>   
    ///  <CreateDate>2006/01/16</CreateDate>
    ///  <Company></Company>
    ///  <Version>1.0</Version>
    /// </summary>
    #endregion
    public class CsvStreamReader
    {
        private ArrayList rowAL;        //行鏈表,CSV文件的每一行就是一個鏈
        private string fileName;       //文件名

        private Encoding encoding;       //編碼

        public CsvStreamReader()
        {
            this.rowAL = new ArrayList();
            this.fileName = "";
            this.encoding = Encoding.Default;
        }

        /// <summary>
        ///
        /// </summary>
        /// <param name="fileName">文件名,包括文件路徑</param>
        public CsvStreamReader(string fileName)
        {
            this.rowAL = new ArrayList();
            this.fileName = fileName;
            this.encoding = Encoding.Default;
            LoadCsvFile();
        }

        /// <summary>
        ///
        /// </summary>
        /// <param name="fileName">文件名,包括文件路徑</param>
        /// <param name="encoding">文件編碼</param>
        public CsvStreamReader(string fileName, Encoding encoding)
        {
            this.rowAL = new ArrayList();
            this.fileName = fileName;
            this.encoding = encoding;
            LoadCsvFile();
        }

        /// <summary>
        /// 文件名,包括文件路徑
        /// </summary>
        public string FileName
        {
            set
            {
                this.fileName = value;
                LoadCsvFile();
            }
        }

        /// <summary>
        /// 文件編碼
        /// </summary>

        public Encoding FileEncoding
        {
            set
            {
                this.encoding = value;
            }
        }

        /// <summary>
        /// 獲取行數
        /// </summary>
        public int RowCount
        {
            get
            {
                return this.rowAL.Count;
            }
        }

        /// <summary>
        /// 獲取列數
        /// </summary>
        public int ColCount
        {
            get
            {
                int maxCol;

                maxCol = 0;
                for (int i = 0; i < this.rowAL.Count; i++)
                {
                    ArrayList colAL = (ArrayList)this.rowAL[i];

                    maxCol = (maxCol > colAL.Count) ? maxCol : colAL.Count;
                }

                return maxCol;
            }
        }


        /// <summary>
        /// 獲取某行某列的數據

        /// row:行,row = 1代表第一行

        /// col:列,col = 1代表第一列  
        /// </summary>
        public string this[int row, int col]
        {
            get
            {
                //數據有效性驗證

                CheckRowValid(row);
                CheckColValid(col);
                ArrayList colAL = (ArrayList)this.rowAL[row - 1];

                //如果請求列數據大於當前行的列時,返回空值

                if (colAL.Count < col)
                {
                    return "";
                }

                return colAL[col - 1].ToString();
            }
        }


        /// <summary>
        /// 根據最小行，最大行，最小列，最大列，來生成一個DataTable類型的數據

        /// 行等於1代表第一行

        /// 列等於1代表第一列

        /// maxrow: -1代表最大行
        /// maxcol: -1代表最大列
        /// </summary>
        public DataTable this[int minRow, int maxRow, int minCol, int maxCol]
        {
            get
            {
                //數據有效性驗證

                CheckRowValid(minRow);
                CheckMaxRowValid(maxRow);
                CheckColValid(minCol);
                CheckMaxColValid(maxCol);
                if (maxRow == -1)
                {
                    maxRow = RowCount;
                }
                if (maxCol == -1)
                {
                    maxCol = ColCount;
                }
                if (maxRow < minRow)
                {
                    throw new Exception("最大行數不能小於最小行數");
                }
                if (maxCol < minCol)
                {
                    throw new Exception("最大列數不能小於最小列數");
                }
                DataTable csvDT = new DataTable();
                int i;
                int col;
                int row;

                //增加列

                for (i = minCol; i <= maxCol; i++)
                {
                    csvDT.Columns.Add(i.ToString());
                }
                for (row = minRow; row <= maxRow; row++)
                {
                    DataRow csvDR = csvDT.NewRow();

                    i = 0;
                    for (col = minCol; col <= maxCol; col++)
                    {
                        csvDR[i] = this[row, col];
                        i++;
                    }
                    csvDT.Rows.Add(csvDR);
                }

                return csvDT;
            }
        }


        /// <summary>
        /// 檢查行數是否是有效的

        /// </summary>
        /// <param name="col"></param>  
        private void CheckRowValid(int row)
        {
            if (row <= 0)
            {
                throw new Exception("行數不能小於0");
            }
            if (row > RowCount)
            {
                throw new Exception("沒有當前行的數據");
            }
        }

        /// <summary>
        /// 檢查最大行數是否是有效的

        /// </summary>
        /// <param name="col"></param>  
        private void CheckMaxRowValid(int maxRow)
        {
            if (maxRow <= 0 && maxRow != -1)
            {
                throw new Exception("行數不能等於0或小於-1");
            }
            if (maxRow > RowCount)
            {
                throw new Exception("沒有當前行的數據");
            }
        }

        /// <summary>
        /// 檢查列數是否是有效的

        /// </summary>
        /// <param name="col"></param>  
        private void CheckColValid(int col)
        {
            if (col <= 0)
            {
                throw new Exception("列數不能小於0");
            }
            if (col > ColCount)
            {
                throw new Exception("沒有當前列的數據");
            }
        }

        /// <summary>
        /// 檢查檢查最大列數是否是有效的

        /// </summary>
        /// <param name="col"></param>  
        private void CheckMaxColValid(int maxCol)
        {
            if (maxCol <= 0 && maxCol != -1)
            {
                throw new Exception("列數不能等於0或小於-1");
            }
            if (maxCol > ColCount)
            {
                throw new Exception("沒有當前列的數據");
            }
        }

        /// <summary>
        /// 載入CSV文件
        /// </summary>
        private void LoadCsvFile()
        {
            //對數據的有效性進行驗證

            if (this.fileName == null)
            {
                throw new Exception("請指定要載入的CSV文件名");
            }
            else if (!File.Exists(this.fileName))
            {
                throw new Exception("指定的CSV文件不存在");
            }
            else
            {
            }
            if (this.encoding == null)
            {
                this.encoding = Encoding.Default;
            }

            StreamReader sr = new StreamReader(this.fileName, this.encoding);
            string csvDataLine;

            csvDataLine = "";
            while (true)
            {
                string fileDataLine;

                fileDataLine = sr.ReadLine();
                if (fileDataLine == null)
                {
                    break;
                }
                if (csvDataLine == "")
                {
                    csvDataLine = fileDataLine;//GetDeleteQuotaDataLine(fileDataLine);
                }
                else
                {
                    csvDataLine += "/r/n" + fileDataLine;//GetDeleteQuotaDataLine(fileDataLine);
                }
                //如果包含偶數個引號，說明該行數據中出現回車符或包含逗號
                if (!IfOddQuota(csvDataLine))
                {
                    AddNewDataLine(csvDataLine);
                    csvDataLine = "";
                }
            }
            sr.Close();
            //數據行出現奇數個引號
            if (csvDataLine.Length > 0)
            {
                throw new Exception("CSV文件的格式有錯誤");
            }
        }

        /// <summary>
        /// 獲取兩個連續引號變成單個引號的數據行
        /// </summary>
        /// <param name="fileDataLine">文件數據行</param>
        /// <returns></returns>
        private string GetDeleteQuotaDataLine(string fileDataLine)
        {
            return fileDataLine.Replace("\"\"", "\"");
        }

        /// <summary>
        /// 判斷字符串是否包含奇數個引號
        /// </summary>
        /// <param name="dataLine">數據行</param>
        /// <returns>為奇數時，返回為真；否則返回為假</returns>
        private bool IfOddQuota(string dataLine)
        {
            int quotaCount;
            bool oddQuota;

            quotaCount = 0;
            for (int i = 0; i < dataLine.Length; i++)
            {
                if (dataLine[i] == '\"')
                {
                    quotaCount++;
                }
            }

            oddQuota = false;
            if (quotaCount % 2 == 1)
            {
                oddQuota = true;
            }

            return oddQuota;
        }

        /// <summary>
        /// 判斷是否以奇數個引號開始

        /// </summary>
        /// <param name="dataCell"></param>
        /// <returns></returns>
        private bool IfOddStartQuota(string dataCell)
        {
            int quotaCount;
            bool oddQuota;

            quotaCount = 0;
            for (int i = 0; i < dataCell.Length; i++)
            {
                if (dataCell[i] == '\"')
                {
                    quotaCount++;
                }
                else
                {
                    break;
                }
            }

            oddQuota = false;
            if (quotaCount % 2 == 1)
            {
                oddQuota = true;
            }

            return oddQuota;
        }

        /// <summary>
        /// 判斷是否以奇數個引號結尾
        /// </summary>
        /// <param name="dataCell"></param>
        /// <returns></returns>
        private bool IfOddEndQuota(string dataCell)
        {
            int quotaCount;
            bool oddQuota;

            quotaCount = 0;
            for (int i = dataCell.Length - 1; i >= 0; i--)
            {
                if (dataCell[i] == '\"')
                {
                    quotaCount++;
                }
                else
                {
                    break;
                }
            }

            oddQuota = false;
            if (quotaCount % 2 == 1)
            {
                oddQuota = true;
            }

            return oddQuota;
        }

        /// <summary>
        /// 加入新的數據行

        /// </summary>
        /// <param name="newDataLine">新的數據行</param>
        private void AddNewDataLine(string newDataLine)
        {
            Debug.WriteLine("NewLine:" + newDataLine);

            //return;

            ArrayList colAL = new ArrayList();
            string[] dataArray = newDataLine.Split(',');
            bool oddStartQuota;       //是否以奇數個引號開始

            string cellData;

            oddStartQuota = false;
            cellData = "";
            for (int i = 0; i < dataArray.Length; i++)
            {
                if (oddStartQuota)
                {
                    //因為前面用逗號分割,所以要加上逗號
                    cellData += "," + dataArray[i];
                    //是否以奇數個引號結尾
                    if (IfOddEndQuota(dataArray[i]))
                    {
                        colAL.Add(GetHandleData(cellData));
                        oddStartQuota = false;
                        continue;
                    }
                }
                else
                {
                    //是否以奇數個引號開始

                    if (IfOddStartQuota(dataArray[i]))
                    {
                        //是否以奇數個引號結尾,不能是一個雙引號,並且不是奇數個引號

                        if (IfOddEndQuota(dataArray[i]) && dataArray[i].Length > 2 && !IfOddQuota(dataArray[i]))
                        {
                            colAL.Add(GetHandleData(dataArray[i]));
                            oddStartQuota = false;
                            continue;
                        }
                        else
                        {

                            oddStartQuota = true;
                            cellData = dataArray[i];
                            continue;
                        }
                    }
                    else
                    {
                        colAL.Add(GetHandleData(dataArray[i]));
                    }
                }
            }
            if (oddStartQuota)
            {
                throw new Exception("數據格式有問題");
            }
            this.rowAL.Add(colAL);
        }


        /// <summary>
        /// 去掉格子的首尾引號，把雙引號變成單引號

        /// </summary>
        /// <param name="fileCellData"></param>
        /// <returns></returns>
        private string GetHandleData(string fileCellData)
        {
            if (fileCellData == "")
            {
                return "";
            }
            if (IfOddStartQuota(fileCellData))
            {
                if (IfOddEndQuota(fileCellData))
                {
                    return fileCellData.Substring(1, fileCellData.Length - 2).Replace("\"\"", "\""); //去掉首尾引號，然後把雙引號變成單引號
                }
                else
                {
                    throw new Exception("數據引號無法匹配" + fileCellData);
                }
            }
            else
            {
                //考慮形如""    """"      """"""   
                if (fileCellData.Length > 2 && fileCellData[0] == '\"')
                {
                    fileCellData = fileCellData.Substring(1, fileCellData.Length - 2).Replace("\"\"", "\""); //去掉首尾引號，然後把雙引號變成單引號
                }
            }

            return fileCellData;
        }
    }

    #region 類說明信息
    /// <summary>
    ///  <DL>
    ///  <DT><b>寫CSV文件類,首先給CSV文件賦值,最後通過Save方法進行保存操作</b></DT>
    ///   <DD>
    ///    <UL> 
    ///    </UL>
    ///   </DD>
    ///  </DL>
    ///  <Author>yangzhihong</Author>   
    ///  <CreateDate>2006/01/16</CreateDate>
    ///  <Company></Company>
    ///  <Version>1.0</Version>
    /// </summary>
    #endregion
    public class CsvStreamWriter
    {
        private ArrayList rowAL;        //行鏈表,CSV文件的每一行就是一個鏈
        private string fileName;       //文件名
        private Encoding encoding;       //編碼

        public CsvStreamWriter()
        {
            this.rowAL = new ArrayList();
            this.fileName = "";
            this.encoding = Encoding.Default;
        }

        /// <summary>
        ///
        /// </summary>
        /// <param name="fileName">文件名,包括文件路徑</param>
        public CsvStreamWriter(string fileName)
        {
            this.rowAL = new ArrayList();
            this.fileName = fileName;
            this.encoding = Encoding.Default;
        }

        /// <summary>
        ///
        /// </summary>
        /// <param name="fileName">文件名,包括文件路徑</param>
        /// <param name="encoding">文件編碼</param>
        public CsvStreamWriter(string fileName, Encoding encoding)
        {
            this.rowAL = new ArrayList();
            this.fileName = fileName;
            this.encoding = encoding;
        }

        /// <summary>
        /// row:行,row = 1代表第一行
        /// col:列,col = 1代表第一列
        /// </summary>
        public string this[int row, int col]
        {
            set
            {
                //對行進行判斷
                if (row <= 0)
                {
                    throw new Exception("行數不能小於0");
                }
                else if (row > this.rowAL.Count) //如果當前列鏈的行數不夠，要補齊
                {
                    for (int i = this.rowAL.Count + 1; i <= row; i++)
                    {
                        this.rowAL.Add(new ArrayList());
                    }
                }
                else
                {
                }
                //對列進行判斷
                if (col <= 0)
                {
                    throw new Exception("列數不能小於0");
                }
                else
                {
                    ArrayList colTempAL = (ArrayList)this.rowAL[row - 1];

                    //擴大長度
                    if (col > colTempAL.Count)
                    {
                        for (int i = colTempAL.Count; i <= col; i++)
                        {
                            colTempAL.Add("");
                        }
                    }
                    this.rowAL[row - 1] = colTempAL;
                }
                //賦值
                ArrayList colAL = (ArrayList)this.rowAL[row - 1];

                colAL[col - 1] = value;
                this.rowAL[row - 1] = colAL;
            }
        }


        /// <summary>
        /// 文件名,包括文件路徑
        /// </summary>
        public string FileName
        {
            set
            {
                this.fileName = value;
            }
        }

        /// <summary>
        /// 文件編碼
        /// </summary>

        public Encoding FileEncoding
        {
            set
            {
                this.encoding = value;
            }
        }

        /// <summary>
        /// 獲取當前最大行
        /// </summary>
        public int CurMaxRow
        {
            get
            {
                return this.rowAL.Count;
            }
        }

        /// <summary>
        /// 獲取最大列
        /// </summary>
        public int CurMaxCol
        {
            get
            {
                int maxCol;

                maxCol = 0;
                for (int i = 0; i < this.rowAL.Count; i++)
                {
                    ArrayList colAL = (ArrayList)this.rowAL[i];

                    maxCol = (maxCol > colAL.Count) ? maxCol : colAL.Count;
                }

                return maxCol;
            }
        }

        /// <summary>
        /// 添加表數據到CSV文件中
        /// </summary>
        /// <param name="dataDT">表數據</param>
        /// <param name="beginCol">從第幾列開始,beginCol = 1代表第一列</param>
        public void AddData(DataTable dataDT, int beginCol)
        {
            if (dataDT == null)
            {
                throw new Exception("需要添加的表數據為空");
            }
            int curMaxRow;

            curMaxRow = this.rowAL.Count;
            for (int i = 0; i < dataDT.Rows.Count; i++)
            {
                for (int j = 0; j < dataDT.Columns.Count; j++)
                {
                    this[curMaxRow + i + 1, beginCol + j] = dataDT.Rows[i][j].ToString();
                }
            }
        }

        /// <summary>
        /// 保存數據,如果當前硬盤中已經存在文件名一樣的文件，將會覆蓋
        /// </summary>
        public void Save()
        {
            //對數據的有效性進行判斷
            if (this.fileName == null)
            {
                throw new Exception("缺少文件名");
            }
            else if (File.Exists(this.fileName))
            {
                File.Delete(this.fileName);
            }
            if (this.encoding == null)
            {
                this.encoding = Encoding.Default;
            }
            System.IO.StreamWriter sw = new StreamWriter(this.fileName, false, this.encoding);

            for (int i = 0; i < this.rowAL.Count; i++)
            {
                sw.WriteLine(ConvertToSaveLine((ArrayList)this.rowAL[i]));
            }

            sw.Close();
        }

        /// <summary>
        /// 保存數據,如果當前硬盤中已經存在文件名一樣的文件，將會覆蓋
        /// </summary>
        /// <param name="fileName">文件名,包括文件路徑</param>
        public void Save(string fileName)
        {
            this.fileName = fileName;
            Save();
        }

        /// <summary>
        /// 保存數據,如果當前硬盤中已經存在文件名一樣的文件，將會覆蓋
        /// </summary>
        /// <param name="fileName">文件名,包括文件路徑</param>
        /// <param name="encoding">文件編碼</param>
        public void Save(string fileName, Encoding encoding)
        {
            this.fileName = fileName;
            this.encoding = encoding;
            Save();
        }


        /// <summary>
        /// 轉換成保存行
        /// </summary>
        /// <param name="colAL">一行</param>
        /// <returns></returns>
        private string ConvertToSaveLine(ArrayList colAL)
        {
            string saveLine;

            saveLine = "";
            for (int i = 0; i < colAL.Count; i++)
            {
                saveLine += ConvertToSaveCell(colAL[i].ToString());
                //格子間以逗號分割
                if (i < colAL.Count - 1)
                {
                    saveLine += ",";
                }
            }

            return saveLine;
        }

        /// <summary>
        /// 字符串轉換成CSV中的格子
        /// 雙引號轉換成兩個雙引號，然後首尾各加一個雙引號
        /// 這樣就不需要考慮逗號及換行的問題
        /// </summary>
        /// <param name="cell">格子內容</param>
        /// <returns></returns>
        private string ConvertToSaveCell(string cell)
        {
            cell = cell.Replace("\"", "\"\"");

            return "\"" + cell + "\"";
        }
    }
}

