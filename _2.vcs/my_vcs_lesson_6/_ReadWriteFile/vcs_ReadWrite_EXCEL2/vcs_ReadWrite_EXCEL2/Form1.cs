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

using Excel = Microsoft.Office.Interop.Excel;	//for excel write
using System.Data.OleDb;                        //for excel read

//方案總管/參考/加入參考/COM/Microsoft Excel 11.0 Object Library




namespace vcs_ReadWrite_EXCEL2
{
    public partial class Form1 : Form
    {
        string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_excel\Books.xlsx";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void btnLoad_Click(object sender, EventArgs e)
        {
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

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }
    }
}
