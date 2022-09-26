using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for File

using Excel = Microsoft.Office.Interop.Excel;	//for excel write
using System.Data.OleDb;                        //for excel read

//方案總管/參考/加入參考/COM/Microsoft Excel 11.0 Object Library

namespace vcs_ReadWrite_EXCEL1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 設定儲存檔名，不用設定副檔名，系統自動判斷 excel 版本，產生 .xls 或 .xlsx 副檔名
            string filename = Application.StartupPath + "\\excel_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");

            Excel.Application excelApp;
            Excel._Workbook wBook;
            Excel._Worksheet wSheet;
            Excel.Range wRange;

            // 開啟一個新的應用程式
            excelApp = new Excel.Application();

            // 讓Excel文件可見
            excelApp.Visible = true;

            // 停用警告訊息
            excelApp.DisplayAlerts = false;

            // 加入新的活頁簿
            excelApp.Workbooks.Add(Type.Missing);

            // 引用第一個活頁簿
            wBook = excelApp.Workbooks[1];

            // 設定活頁簿焦點
            wBook.Activate();

            // 引用第一個工作表
            wSheet = (Excel._Worksheet)wBook.Worksheets[1];

            // 命名工作表的名稱
            wSheet.Name = "Sheet1";

            // 設定工作表焦點
            wSheet.Activate();

            // 設定第1列資料
            excelApp.Cells[1, 1] = "名稱";
            excelApp.Cells[1, 2] = "重量";
            excelApp.Cells[1, 3] = "生日";
            // 設定第1列顏色
            wRange = wSheet.Range[wSheet.Cells[1, 1], wSheet.Cells[1, 3]];
            wRange.Select();
            wRange.Font.Color = ColorTranslator.ToOle(Color.White);
            wRange.Interior.Color = ColorTranslator.ToOle(Color.DimGray);

            // 設定第2列資料
            excelApp.Cells[2, 1] = "elephant";
            excelApp.Cells[2, 2] = "895";
            excelApp.Cells[2, 3] = "2013/5/10";

            // 設定第3列資料
            excelApp.Cells[3, 1] = "lion";
            excelApp.Cells[3, 2] = "250";
            excelApp.Cells[3, 3] = "2010/01/31";

            // 設定第4列資料
            excelApp.Cells[4, 1] = "cat";
            excelApp.Cells[4, 2] = "15";
            excelApp.Cells[4, 3] = "2008/12/05";

            // 設定第5列資料
            excelApp.Cells[5, 1] = "dog";
            excelApp.Cells[5, 2] = "25";
            excelApp.Cells[5, 3] = "2003/9/28";

            // 設定第6列資料
            excelApp.Cells[6, 1] = "光26";
            excelApp.Cells[6, 2] = "123";
            excelApp.Cells[6, 3] = "1900/1/1";

            // 設定第7列資料
            //excelApp.Cells[7, 1] = "總計";
            // 設定總和公式 =SUM(B2:B4)
            //excelApp.Cells[7, 2].Formula = string.Format("=SUM(B{0}:B{1})", 2, 5);
            // 設定第7列顏色
            //wRange = wSheet.Range[wSheet.Cells[7, 1], wSheet.Cells[7, 3]];
            wRange.Select();
            wRange.Font.Color = ColorTranslator.ToOle(Color.Red);
            wRange.Interior.Color = ColorTranslator.ToOle(Color.Yellow);

            // 自動調整欄寬
            wRange = wSheet.Range[wSheet.Cells[1, 1], wSheet.Cells[6, 3]];
            wRange.Select();
            wRange.Columns.AutoFit();
            //另存活頁簿
            wBook.SaveAs(filename, Type.Missing, Type.Missing, Type.Missing, Type.Missing, Type.Missing, Excel.XlSaveAsAccessMode.xlNoChange, Type.Missing, Type.Missing, Type.Missing, Type.Missing, Type.Missing);

            //關閉活頁簿
            wBook.Close(false, Type.Missing, Type.Missing);

            //關閉Excel
            excelApp.Quit();

            //釋放Excel資源
            System.Runtime.InteropServices.Marshal.ReleaseComObject(excelApp);
            wBook = null;
            wSheet = null;
            wRange = null;
            excelApp = null;
            GC.Collect();

            richTextBox1.Text += "存檔檔名: " + filename + ",  xls or xlsx\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\excel_20210602_131921.xls";

            //string filename = pathFile + ".xls";
            if (File.Exists(filename) == false)
            {
                richTextBox1.Text += "檔案: " + filename + " 不存在，無法開啟。\n";
                return;
            }
            else
            {
                richTextBox1.Text += "開啟檔案: " + filename + "\n";
            }

            //string xlsPath = @"C:\tttt.xls";

            //string sheetName = "Sheet1";

            /*步驟1：設定Excel的屬性、路徑*/
            //設定讀取的Excel屬性
            string strCon = "Provider=Microsoft.Jet.OLEDB.4.0;" +
                //路徑(檔案讀取路徑)
            "Data Source=C:\\______test_files\\__RW\\_excel\\vcs_test_excel.xls;" +
                //選擇Excel版本
                //Excel 12.0 針對Excel 2010、2007版本(OLEDB.12.0)
                //Excel 8.0 針對Excel 97-2003版本(OLEDB.4.0)
                //Excel 5.0 針對Excel 97(OLEDB.4.0)
            "Extended Properties='Excel 8.0;" +
                //開頭是否為資料
                //若指定值為 Yes，代表 Excel 檔中的工作表第一列是欄位名稱，oleDB直接從第二列讀取
                //若指定值為 No，代表 Excel 檔中的工作表第一列就是資料了，沒有欄位名稱，oleDB直接從第一列讀取
            "HDR=NO;" +
                //IMEX=0 為「匯出模式」，能對檔案進行寫入的動作。
                //IMEX=1 為「匯入模式」，能對檔案進行讀取的動作。
                //IMEX=2 為「連結模式」，能對檔案進行讀取與寫入的動作。
            "IMEX=1'";
            /*步驟2：依照Excel的屬性及路徑開啟檔案*/
            //Excel路徑及相關資訊匯入
            OleDbConnection GetXLS = new OleDbConnection(strCon);
            //打開檔案
            GetXLS.Open();
            /*步驟3：搜尋此Excel的所有工作表，找到特定工作表進行讀檔，並將其資料存入List*/
            //搜尋xls的工作表(工作表名稱需要加$字串)
            DataTable Table = GetXLS.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null);
            //查詢此Excel所有的工作表名稱
            string SelectSheetName = "";
            foreach (DataRow row in Table.Rows)
            {
                //抓取Xls各個Sheet的名稱(+'$')-有的名稱需要加名稱''，有的不用
                SelectSheetName = (string)row["TABLE_NAME"];
                richTextBox1.Text += "\n" + "工作表: " + SelectSheetName + "\n";
                //工作表名稱有特殊字元、空格，需加'工作表名稱$'，ex：'Sheet_A$'
                //工作表名稱沒有特殊字元、空格，需加工作表名稱$，ex：SheetA$
                //所有工作表名稱為Sheet1，讀取此工作表的內容
                //if (SelectSheetName == "SheetA$")
                if (SelectSheetName == "Sheet1$")   //第一頁
                {
                    //select 工作表名稱
                    OleDbCommand cmSheetA = new OleDbCommand(" SELECT * FROM [Sheet1$] ", GetXLS);
                    OleDbDataReader drSheetA = cmSheetA.ExecuteReader();

                    //讀取工作表SheetA資料
                    //List<string> ListSheetA = new List<string>();
                    int cnt = 0;
                    while (drSheetA.Read())
                    {
                        //工作表SheetA的資料存入List
                        //ListSheetA.Add(drSheetA[cnt].ToString());
                        richTextBox1.Text += "列" + cnt.ToString() + "\t" + drSheetA[0].ToString() + "\t" + drSheetA[1].ToString() + "\t" + drSheetA[2].ToString() + "\n";
                        cnt++;
                    }
                    /*步驟4：關閉檔案*/
                    //結束關閉讀檔(必要，不關會有error)
                    drSheetA.Close();
                    GetXLS.Close();
                }
            }

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //讀取EXCEL檔案到dataGridView
            //sugar can not use this
            //Excel數據導入到dataGridView
            //http://weisico.com/program/2018/0531/370.html

            string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\vcs_ReadWrite_EXCEL2.xls";

            try
            {
                string tableName = GetExcelFirstTableName(filename);
                richTextBox1.Text += "tableName = " + tableName + "\n";
                //設置T_Sql
                string TSql = "SELECT  * FROM [" + tableName + "]";
                richTextBox1.Text += "TSql = " + TSql + "\n";
                //讀取數據
                DataTable table = ExcelToDataSet(filename, TSql).Tables[0];
                dataGridView1.DataSource = table;

                int cols = table.Columns.Count;
                int rows = table.Rows.Count;
                richTextBox1.Text += "cols = " + cols.ToString() + "\n";
                richTextBox1.Text += "rows = " + rows.ToString() + "\n";
                int i;
                int j;
                for (i = 0; i < cols; i++)
                {
                    richTextBox1.Text += table.Columns[i] + "\t";
                }
                richTextBox1.Text += "\n";
                for (i = 0; i < rows; i++)
                {
                    for (j = 0; j < cols; j++)
                    {
                        richTextBox1.Text += table.Rows[i][j] + "\t";
                    }
                    richTextBox1.Text += "\n";
                }
                richTextBox1.Text += "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        /// <summary>
        /// 動態取Excel表名
        /// </summary>
        /// <param name="fullPath">文件路徑</param>
        /// <returns></returns>
        public string GetExcelFirstTableName(string fullPath)
        {
            string tableName = null;
            if (File.Exists(fullPath))
            {
                using (OleDbConnection conn = new OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Extended Properties=Excel 8.0;Data Source=" + fullPath))
                {
                    conn.Open();

                    richTextBox1.Text += "t0 = " + conn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null).Rows[0][0].ToString().Trim() + "\n";
                    richTextBox1.Text += "t1 = " + conn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null).Rows[0][1].ToString().Trim() + "\n";

                    richTextBox1.Text += "s1 = " + conn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null).Rows[0][2].ToString().Trim() + "\n";
                    richTextBox1.Text += "s2 = " + conn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null).Rows[1][2].ToString().Trim() + "\n";
                    richTextBox1.Text += "s3 = " + conn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null).Rows[2][2].ToString().Trim() + "\n";

                    richTextBox1.Text += "t3 = " + conn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null).Rows[0][3].ToString().Trim() + "\n";

                    richTextBox1.Text += "\n\n";

                    tableName = conn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null).Rows[0][2].ToString().Trim();
                    richTextBox1.Text += "GetExcelFirstTableName tableName = " + tableName + "\n";
                }
            }
            return tableName;
        }


        /// <summary>
        /// 返回Excel數據源
        /// </summary>
        /// <param name="filename">文件路徑</param>
        /// <param name="TSql">TSql</param>
        /// <returns>DataSet</returns>
        public static DataSet ExcelToDataSet(string filename, string TSql)
        {
            DataSet ds;
            string strCon = "Provider=Microsoft.Jet.OLEDB.4.0;Extended Properties=Excel 8.0;data source=" + filename;
            OleDbConnection myConn = new OleDbConnection(strCon);
            string strCom = TSql;
            myConn.Open();
            OleDbDataAdapter myCommand = new OleDbDataAdapter(strCom, myConn);
            ds = new DataSet();
            myCommand.Fill(ds);
            myConn.Close();
            return ds;
        }


        //配置Excel的OleDb連接字符串
        public const string OledbConnString = "Provider = Microsoft.Jet.OLEDB.4.0 ; Data Source = {0};Extended Properties='Excel 8.0;HDR=Yes;IMEX=1;'"; //Excel的 OleDb 連接字符串

        private void button4_Click(object sender, EventArgs e)
        {
            //讀取EXCEL檔案到dataGridView
            //another
            //C# Excel文件導入操作

            string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\excel_test_data.xls";

            richTextBox1.Text += "開啟檔案 : " + filename + "\n";

            DataTable excelTbl = this.GetExcelTable(filename);  //調用函數獲取Excel中的信息
            if (excelTbl == null)
            {
                return;
            }

            dataGridView1.DataSource = excelTbl;


        }

        /// 
        /// 獲取Excel文件中的信息，保存到一個DataTable中
        /// 

        /// 文件路徑
        /// 返回生成的DataTable
        private DataTable GetExcelTable(string path)
        {
            try
            {
                //獲取excel數據
                DataTable dt1 = new DataTable("excelTable");
                string strConn = string.Format(OledbConnString, path);
                OleDbConnection conn = new OleDbConnection(strConn);
                conn.Open();
                DataTable dt = conn.GetSchema("Tables");
                //判斷excel的sheet頁數量，查詢第1頁
                if (dt.Rows.Count > 0)
                {
                    string selSqlStr = string.Format("select * from [{0}]", dt.Rows[0]["TABLE_NAME"]);
                    OleDbDataAdapter oleDa = new OleDbDataAdapter(selSqlStr, conn);
                    oleDa.Fill(dt1);
                }
                conn.Close();
                return dt1;
            }
            catch (Exception ex)
            {
                MessageBox.Show("Excel轉換DataTable出錯：" + ex.Message);
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                return null;
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //Sugar can not open file
            string filename = Application.StartupPath + "\\excel_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".xls";
            FileStream fs = new FileStream(filename, FileMode.Create, FileAccess.Write);
            StreamWriter sw = new StreamWriter(fs, System.Text.Encoding.GetEncoding("big5"));
            string s = "第1欄位\t第2欄位\t第3欄位\t第4欄位\t第5欄位\t";
            sw.WriteLine(s); //設置Excel標題

            //寫入Excel檔資料
            for (int i = 0; i < 10; i++)  //i代表行，總共10行
            {
                s = "";
                for (int j = 0; j < 5; j++)    //j代表欄位，總共5欄
                {
                    s = s + (i * 10 + j).ToString() + "\t";
                }
                sw.WriteLine(s);
            }
            sw.Close();     //寫入Excel檔資料

            richTextBox1.Text += "存檔檔名: " + filename + "，此檔不能用程式讀取。\n";
        }
    }
}
