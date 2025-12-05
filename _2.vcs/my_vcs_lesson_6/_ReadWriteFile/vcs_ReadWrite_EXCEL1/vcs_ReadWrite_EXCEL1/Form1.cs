using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

// Include a reference to:
//      Microsoft Excel 14.0 Object Library

using System.IO;    //for File

//參考/加入參考/.NET/Microsoft.Office.Interop.Excel, 內嵌Interop型別改False
using Excel = Microsoft.Office.Interop.Excel;	//for excel write

//tmp using System.Data.OleDb;                        //for excel read
//tmp 方案總管/參考/加入參考/COM/Microsoft Excel 11.0 Object Library


using System.Data.OleDb;    //for OleDbConnection, 表示資料來源的開啟連接

//參考/加入參考/COM/Microsoft Excel 12.0 Object Library

//using System.Diagnostics;
//using System.Runtime.InteropServices;

/*
順序
1. 加入以上using
2. 參考/加入參考/COM/Microsoft Office 12.0 Object Library
                     Microsoft Excel 12.0 Object Library

參考/加入參考/COM/Microsoft Excel 12.0 Object Library (用此即可)
*/


/*
// Open the Add References dialog. On the COM tab, select:
//
//      Microsoft.Office.Interop.Excel 14.0.0.0
//
// Or whatever version you have installed on your system.

// More examples of automating Excel from C#:
//
//      http://support.microsoft.com/kb/302084
//      https://support.microsoft.com/help/311452/info-develop-microsoft-office-solutions-with-visual-studio--net

using Excel = Microsoft.Office.Interop.Excel;
using System.IO;

// 1. 參考/加入參考/Microsoft Office 15.0 Object Library 和 Microsoft.Office.Interop.Excel.dll
// 2. Microsoft.Office.Interop.Excel屬性/內嵌Interop型別改成False
// 3. 加入上述using
*/


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
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 5;
            dy = 60 + 5;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            dataGridView1.Size = new Size(600, 200);
            dataGridView1.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            richTextBox1.Size = new Size(600, 640-210);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0+210);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1260, 700);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {

        }

        private void button0_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_excel\Books.xlsx";

            // Get the Excel application object.
            Excel.Application excel_app = new Excel.ApplicationClass();

            // Make Excel visible (optional).
            excel_app.Visible = true;

            // Open the workbook read-only.
            Excel.Workbook workbook = excel_app.Workbooks.Open(
                filename,
                Type.Missing, true, Type.Missing, Type.Missing,
                Type.Missing, Type.Missing, Type.Missing, Type.Missing,
                Type.Missing, Type.Missing, Type.Missing, Type.Missing,
                Type.Missing, Type.Missing);

            // Get the first worksheet.
            Excel.Worksheet sheet = (Excel.Worksheet)workbook.Sheets[1];

            // Get the used range.
            Excel.Range used_range = sheet.UsedRange;

            // Get the maximum row and column number.
            int max_row = used_range.Rows.Count;
            int max_col = used_range.Columns.Count;
            richTextBox1.Text += "共有 : " + max_col.ToString() + " 個欄位\n";
            richTextBox1.Text += "共有 : " + max_row.ToString() + " 筆資料\n";

            // Get the sheet's values.
            object[,] values = (object[,])used_range.Value2;
            //richTextBox1.Text += values + "\n";

            richTextBox1.Text += "設定 GDV, " + max_col.ToString() + " 欄\n";
            // Get the title values.
            for (int col = 1; col <= max_col; col++)
            {
                string title = (string)values[1, col];
                richTextBox1.Text += "C = " + col.ToString() + ", 取得標題 : " + title + "\n";
            }

            for (int row = 2; row <= max_row; row++)
            {
                object[] row_values = new object[max_col];
                for (int col = 1; col <= max_col; col++)
                {
                    richTextBox1.Text += "C = " + col.ToString() + "R = " + row.ToString() + " : " + values[row, col] + "\n";
                }
            }

            // Close the workbook without saving changes.
            workbook.Close(false, Type.Missing, Type.Missing);

            // Close the Excel server.
            excel_app.Quit();

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //製作EXCEL檔案
            string filename = "tmp_excel_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".xls";
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

        private void button2_Click(object sender, EventArgs e)
        {
            //製作一個xlsx檔案
            richTextBox1.Text += "製作一個xlsx檔案 ST\n";

            // Get the Excel application object.
            Excel.Application excel_app = new Excel.ApplicationClass();

            // Make Excel visible (optional).
            excel_app.Visible = true;

            // Create the workbook.
            Excel.Workbook workbook = excel_app.Workbooks.Add(Type.Missing);

            // Get the first worksheet.
            Excel.Worksheet sheet = (Excel.Worksheet)workbook.Sheets[1];

            // Add some random data to a range of cells.
            object[,] values = 
            { 
                { "Salesperson",  2005,  2006, 2007, 2008, 2009, 2010},
                { "Ann", 0, 0, 0, 0, 0, 0},
                { "Bob", 0, 0, 0, 0, 0, 0},
                { "Cat", 0, 0, 0, 0, 0, 0},
                { "Don", 0, 0, 0, 0, 0, 0},
            };
            Random rand = new Random();
            for (int i = 1; i < 5; i++)
            {
                for (int j = 1; j < 7; j++)
                {
                    values[i, j] = rand.Next(60, 101);
                }
            }
            Excel.Range value_range = sheet.get_Range("A1", "G5");
            value_range.Value2 = values;

            Excel.Range colA = (Excel.Range)sheet.Columns[1, Type.Missing];
            colA.ColumnWidth = 12;

            // Create the chart.
            Excel.Shape chart_shape = sheet.Shapes.AddChart(
                Excel.XlChartType.xlLine, 400, 5, 300, 200);
            Excel.Chart chart = chart_shape.Chart;

            // Set the data.
            Excel.Range chart_range = sheet.get_Range("A2", "G5");
            chart.SetSourceData(chart_range, Excel.XlRowCol.xlRows);

            // Set the X axis labels.
            Excel.Range axis_range = sheet.get_Range("B1", "G1");
            Excel.Series series = (Excel.Series)chart.SeriesCollection(1);
            series.XValues = axis_range;

            // Delete the saved file if it already exists.
            string filename = Application.StartupPath + "\\excel_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".xlsx";

            System.IO.File.Delete(filename);

            // Save the changes and close the workbook.
            workbook.SaveAs(filename, Type.Missing, Type.Missing,
                Type.Missing, Type.Missing, Type.Missing,
                Excel.XlSaveAsAccessMode.xlExclusive, Type.Missing,
                Type.Missing, Type.Missing, Type.Missing,
                Type.Missing);
            workbook.Close(true, Type.Missing, Type.Missing);

            // Close the Excel server.
            excel_app.Quit();

            richTextBox1.Text += "製作一個xlsx檔案 完成\n";

        }

        public class Account
        {
            public int ID { get; set; }
            public double Balance { get; set; }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //匯出資料至Excel, 並存檔
            //匯出資料至Excel, 並存檔
            //搬移中 TBD, 從 vcs_ReadWrite_EXCEL5


            return;

            //System.Diagnostics.Debug.WriteLine("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX");

            // Create a list of accounts.
            var bankAccounts = new List<Account> 
            {
                new Account { 
                              ID = 345678,
                              Balance = 541.27
                            },
                new Account {
                              ID = 1230221,
                              Balance = -127.44
                            }
            };

            // Display the list in an Excel spreadsheet.    電子表格程序
            DisplayInExcel(bankAccounts);



        }

        void DisplayInExcel(IEnumerable<Account> accounts)
        {
            /*
            var excelApp = new Excel.Application();
            // Make the object visible.
            excelApp.Visible = true;

            // Create a new, empty workbook and add it to the collection returned 
            // by property Workbooks. The new workbook becomes the active workbook.
            // Add has an optional parameter for specifying a praticular template. 
            // Because no argument is sent in this example, Add creates a new workbook. 
            excelApp.Workbooks.Add();

            // This example uses a single workSheet. 
            Excel._Worksheet workSheet = excelApp.ActiveSheet;

            // Earlier versions of C# require explicit casting.
            //Excel._Worksheet workSheet = (Excel.Worksheet)excelApp.ActiveSheet;

            //設定標題
            // Establish column headings in cells A1 and B1.
            workSheet.Cells[1, "A"] = "ID Number";
            workSheet.Cells[1, "B"] = "Current Balance";

            //加入資料
            var row = 1;
            foreach (var acct in accounts)
            {
                row++;
                workSheet.Cells[row, "A"] = acct.ID;
                workSheet.Cells[row, "B"] = acct.Balance;
            }

            //在 DisplayInExcel 結尾加入下列程式碼，以調整資料行寬度以容納內容。
            workSheet.Columns[1].AutoFit();
            workSheet.Columns[2].AutoFit();

            //加入表格的其他格式
            // Call to AutoFormat in Visual C#. This statement replaces the 
            // two calls to AutoFit.
            // Call to AutoFormat in Visual C# 2010.
            workSheet.Range["A1", "B3"].AutoFormat(Excel.XlRangeAutoFormat.xlRangeAutoFormatClassic2);

            //Copy 方法會將工作表加入剪貼簿
            // Put the spreadsheet contents on the clipboard. The Copy method has one
            // optional parameter for specifying a destination. Because no argument  
            // is sent, the destination is the Clipboard.
            workSheet.Range["A1:B3"].Copy();

            string filename = Application.StartupPath + "\\excel_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".xlsx";
            workSheet.SaveAs(filename);
            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename + "\n";
            */
        }

        class AnimalData
        {
            public string Name_C { get; set; }
            public string Name_E { get; set; }
            public string Name_N { get; set; }
            public int Age { get; set; }
            public int Weight { get; set; }
            public DateTime Birthday { get; set; }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //匯出資料到Excel
            //二維陣列
            AnimalData[] AnimalDataArray = new AnimalData[]{
            new AnimalData { Name_C = "鼠", Name_E = "mouse", Name_N = "Mickey", Age= 20 , Weight = 5, Birthday = DateTime.Parse("1928/11/18") },
            new AnimalData { Name_C = "牛", Name_E = "bull", Name_N = "Benny", Age= 30 , Weight = 82, Birthday = DateTime.Parse("2000/8/14") },
            new AnimalData { Name_C = "虎", Name_E = "tiger", Name_N = "Eric", Age= 15 , Weight = 55, Birthday = DateTime.Parse("1993/12/13") },
            new AnimalData { Name_C = "兔", Name_E = "rabbit", Name_N = "Cony", Age= 22 , Weight = 12, Birthday = DateTime.Parse("2013/4/17") }
            };

            Excel.Application xlsApp = new Excel.Application();
            Excel.Workbook xlsWookBook;
            Excel.Worksheet xlsWookSheet;
            object misValue = System.Reflection.Missing.Value;
            xlsWookBook = xlsApp.Workbooks.Add(misValue);
            xlsWookSheet = (Excel.Worksheet)xlsWookBook.Worksheets.get_Item(1);
            xlsApp.Visible = true;

            richTextBox1.Text += "data:\n";

            richTextBox1.Text += "len = " + AnimalDataArray.Length.ToString() + "\n";

            //第一列放標題
            xlsWookSheet.Cells[1, "A"] = "中文名";
            xlsWookSheet.Cells[1, "B"] = "英文名";
            xlsWookSheet.Cells[1, "C"] = "名字";
            xlsWookSheet.Cells[1, "D"] = "年齡";
            xlsWookSheet.Cells[1, "E"] = "體重";
            xlsWookSheet.Cells[1, "F"] = "生日";

            int i;
            int j;
            for (i = 0; i < AnimalDataArray.Length; i++)
            {
                richTextBox1.Text += AnimalDataArray[i].Name_C + "\t" + AnimalDataArray[i].Name_E + "\t" + AnimalDataArray[i].Name_N + "\t"
                    + AnimalDataArray[i].Age.ToString() + "\t" + AnimalDataArray[i].Weight.ToString() + "\t" + AnimalDataArray[i].Birthday + "\n";

                //資料從第二列開始放
                j = 0; xlsWookSheet.Cells[i + 2, j + 1] = AnimalDataArray[i].Name_C;
                j = 1; xlsWookSheet.Cells[i + 2, j + 1] = AnimalDataArray[i].Name_E;
                j = 2; xlsWookSheet.Cells[i + 2, j + 1] = AnimalDataArray[i].Name_N;
                j = 3; xlsWookSheet.Cells[i + 2, j + 1] = AnimalDataArray[i].Age;
                j = 4; xlsWookSheet.Cells[i + 2, j + 1] = AnimalDataArray[i].Weight;
                j = 5; xlsWookSheet.Cells[i + 2, j + 1] = AnimalDataArray[i].Birthday;
            }

            /*
            for (int i = 0; i <= dgv.Rows.Count - 1; i++)
            {
                for (int j = 0; j < dgv.Columns.Count; j++)
                {
                    DataGridViewCell dgvCell = dgv[j, i];
                    richTextBox1.Text += dgvCell.Value + "\t";
                    xlsWookSheet.Cells[i + 1, j + 1] = dgvCell.Value;
                }
                richTextBox1.Text += "\n";
            }
            */
            /* NG
            //結尾加入下列程式碼，以調整資料行寬度以容納內容。
            xlsWookSheet.Columns[1].AutoFit();
            xlsWookSheet.Columns[2].AutoFit();
            xlsWookSheet.Columns[3].AutoFit();
            xlsWookSheet.Columns[4].AutoFit();
            xlsWookSheet.Columns[5].AutoFit();
            xlsWookSheet.Columns[6].AutoFit();
            */
            //加入表格的其他格式
            // Call to AutoFormat in Visual C#. This statement replaces the 
            // two calls to AutoFit.
            // Call to AutoFormat in Visual C# 2010.
            xlsWookSheet.Range["A1", "F5"].AutoFormat(Excel.XlRangeAutoFormat.xlRangeAutoFormatClassic2);

            String filename = Application.StartupPath + "\\excel_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".xls";

            xlsWookBook.SaveAs(filename, Excel.XlFileFormat.xlWorkbookNormal, misValue, misValue, misValue, misValue, Excel.XlSaveAsAccessMode.xlExclusive, misValue, misValue, misValue, misValue, misValue);
            xlsWookBook.Close(true, misValue, misValue);
            xlsApp.Quit();
            xlsWookSheet = null;
            xlsWookBook = null;
            xlsApp = null;

            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename + "\n";

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //讀取Excel資料
            //sugar can not use this

            //在C# 使用 OleDb 讀取 Excel
            openFileDialog1.Title = "匯入Excel資料";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.xls";
            //openFileDialog1.Filter = "文字檔(*.txt)|*.txt|Word檔(*.doc)|*.txt|Excel檔(*.xls)|*.txt|所有檔案(*.*)|*.*";   //存檔類型
            openFileDialog1.Filter = "Excel Files (*.xls;*.xlsx)|*.xls;*.xlsx|All files (*.*)|*.*";   //檔案類型
            openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            openFileDialog1.InitialDirectory = @"D:\_git\vcs\_1.data\______test_files1\__RW\_excel";  //預設開啟的路徑
            openFileDialog1.Multiselect = false;    //允許多選檔案
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "已選取檔案: " + openFileDialog1.FileName + "\n";
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
                return;
            }

            DataTable dt = ReadExcelData(openFileDialog1.FileName, "Sheet1");

            if (dt == null)
            {
                richTextBox1.Text += "無法讀取Excel資料\n";
                return;
            }

            dataGridView1.DataSource = dt;


            int c;
            int cols = dataGridView1.ColumnCount;
            for (c = 0; c < cols; c++)
            {
                richTextBox1.Text += "CurrentRow" + c.ToString() + " = " + dataGridView1.Columns[c].Name + "\n";
            }

            print_dataGridView_data(dataGridView1);
        }

        public DataTable ReadExcelData(string filename, string SheetName)
        {
            DataTable dt = new DataTable();

            //定義OleDb======================================================
            //1.檔案位置
            string FilePath = filename;

            //2.提供者名稱  Microsoft.Jet.OLEDB.4.0適用於2003以前版本，Microsoft.ACE.OLEDB.12.0 適用於2007以後的版本處理 xlsx 檔案
            string ProviderName = "Microsoft.ACE.OLEDB.12.0;";

            //3.Excel版本，Excel 8.0 針對Excel2000及以上版本，Excel5.0 針對Excel97。
            string ExtendedString = "'Excel 8.0;";

            //4.第一行是否為標題(;結尾區隔)
            string HDR = "No;";

            //5.IMEX=1 通知驅動程序始終將「互混」數據列作為文本讀取(;結尾區隔,'文字結尾)
            string IMEX = "0';";

            //=============================================================
            //連線字串
            string connectString =
                    "Data Source=" + FilePath + ";" +
                    "Provider=" + ProviderName +
                    "Extended Properties=" + ExtendedString +
                    "HDR=" + HDR +
                    "IMEX=" + IMEX;
            //=============================================================

            using (OleDbConnection Connect = new OleDbConnection(connectString))
            {
                Connect.Open();
                string queryString = "SELECT * FROM [" + SheetName + "$]";
                try
                {
                    using (OleDbDataAdapter dr = new OleDbDataAdapter(queryString, Connect))
                    {
                        dr.Fill(dt);
                    }
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "異常訊息:" + ex.Message + "\n";
                    return null;
                }
            }
            return dt;
        }

        void print_dataGridView_data(DataGridView dgv)
        {
            int r;
            int c;
            int rows = dgv.RowCount;
            int cols = dgv.ColumnCount;
            richTextBox1.Text += "ROWS = " + rows.ToString() + "\n";
            richTextBox1.Text += "COLS = " + cols.ToString() + "\n";
            richTextBox1.Text += "Content:\n";

            for (r = 0; r < rows; r++)
            {
                richTextBox1.Text += "r = " + r.ToString() + "\t";
                for (c = 0; c < cols; c++)
                {
                    //richTextBox1.Text += dataGridView1[c, r].Value + "\t";
                    DataGridViewCell dgvCell = dgv[c, r];
                    richTextBox1.Text += dgvCell.Value + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //匯出資料至Excel, 並存檔

            //System.Diagnostics.Debug.WriteLine("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX");

            // Create a list of accounts.
            var bankAccounts = new List<Account> 
            {
                new Account { 
                              ID = 345678,
                              Balance = 541.27
                            },
                new Account {
                              ID = 1230221,
                              Balance = -127.44
                            }
            };

            // Display the list in an Excel spreadsheet.    電子表格程序
            DisplayInExcel(bankAccounts);
        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {
            //將Excel檔案讀出並存至PDF
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_excel\vcs_ReadWrite_PDF2_Items.xlsx";

            // Write into the Excel workbook.

            // Get the Excel application object.
            Excel.ApplicationClass excel_app = new Excel.ApplicationClass();

            // Make Excel visible (optional).
            excel_app.Visible = true;

            // See if the workbook already exists.
            Excel.Workbook workbook = null;
            if (File.Exists(filename))
            {
                // Open the workbook.
                workbook = excel_app.Workbooks.Open(filename,
                    Type.Missing, Type.Missing, Type.Missing, Type.Missing,
                    Type.Missing, Type.Missing, Type.Missing, Type.Missing,
                    Type.Missing, Type.Missing, Type.Missing, Type.Missing,
                    Type.Missing, Type.Missing);
            }
            else
            {
                // Create the workbook.
                workbook = excel_app.Workbooks.Add(Type.Missing);
                workbook.SaveAs(filename, Type.Missing, Type.Missing,
                    Type.Missing, Type.Missing, Type.Missing,
                    Excel.XlSaveAsAccessMode.xlShared, Type.Missing,
                    Type.Missing, Type.Missing, Type.Missing, Type.Missing);
            }

            // See if the worksheet already exists.
            string sheet_name = DateTime.Now.ToString("MM-dd-yy");

            Excel.Worksheet sheet = FindSheet(workbook, sheet_name);
            if (sheet == null)
            {
                // Add the worksheet at the end.
                sheet = (Excel.Worksheet)workbook.Sheets.Add(
                    Type.Missing, workbook.Sheets[workbook.Sheets.Count],
                    1, Excel.XlSheetType.xlWorksheet);
                sheet.Name = sheet_name;
            }

            // Add some data to individual cells.
            sheet.Cells[1, 1] = "A";
            sheet.Cells[1, 2] = "B";
            sheet.Cells[1, 3] = "C";

            // Make that range of cells bold and red.
            Excel.Range header_range = sheet.get_Range("A1", "C1");
            header_range.Font.Bold = true;
            header_range.Font.Color =
                System.Drawing.ColorTranslator.ToOle(System.Drawing.Color.Red);
            header_range.Interior.Color =
                System.Drawing.ColorTranslator.ToOle(System.Drawing.Color.Pink);

            // Add some data to a range of cells.
            int[,] values =
            {
                {2, 4, 6},
                {3, 6, 9},
                {4, 8, 12},
                {5, 10, 15},
            };
            Excel.Range value_range = sheet.get_Range("A2", "C5");
            value_range.Value2 = values;

            // Save into a PDF.
            //string filename2 = filename.Replace(".xlsx", ".pdf");

            string filename2 = Application.StartupPath + "\\pdf_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".pdf";


            const int xlQualityStandard = 0;
            sheet.ExportAsFixedFormat(
                Excel.XlFixedFormatType.xlTypePDF,
                filename2, xlQualityStandard, true, false,
                Type.Missing, Type.Missing, true, Type.Missing);

            // Save the changes and close the workbook.
            workbook.Close(true, Type.Missing, Type.Missing);

            // Close the Excel server.
            excel_app.Quit();

            richTextBox1.Text += "done\n";
        }

        // Return the worksheet with the given name.
        private Excel.Worksheet FindSheet(Excel.Workbook workbook, string sheet_name)
        {
            foreach (Excel.Worksheet sheet in workbook.Sheets)
            {
                if (sheet.Name == sheet_name) return sheet;
            }
            return null;
        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }

        private void button20_Click(object sender, EventArgs e)
        {

        }

        private void button21_Click(object sender, EventArgs e)
        {

        }

        private void button22_Click(object sender, EventArgs e)
        {

        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button25_Click(object sender, EventArgs e)
        {

        }

        private void button26_Click(object sender, EventArgs e)
        {

        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        private void button28_Click(object sender, EventArgs e)
        {

        }

        private void button29_Click(object sender, EventArgs e)
        {

        }
    }
}

