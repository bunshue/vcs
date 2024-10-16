using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Excel = Microsoft.Office.Interop.Excel;

using System.Data.OleDb;    //for OleDbConnection, 表示資料來源的開啟連接

/*
參考/加入參考/COM/Microsoft Excel 12.0 Object Library

加入必要的 using 指示詞
using Excel = Microsoft.Office.Interop.Excel;
*/

namespace vcs_ReadWrite_EXCEL4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
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

        private void button1_Click(object sender, EventArgs e)
        {
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

            //結尾加入下列程式碼，以調整資料行寬度以容納內容。
            xlsWookSheet.Columns[1].AutoFit();
            xlsWookSheet.Columns[2].AutoFit();
            xlsWookSheet.Columns[3].AutoFit();
            xlsWookSheet.Columns[4].AutoFit();
            xlsWookSheet.Columns[5].AutoFit();
            xlsWookSheet.Columns[6].AutoFit();

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

        private void button2_Click(object sender, EventArgs e)
        {
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
            openFileDialog1.InitialDirectory = @"C:\_git\vcs\_1.data\______test_files1\__RW\_excel";  //預設開啟的路徑
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
    }
}

