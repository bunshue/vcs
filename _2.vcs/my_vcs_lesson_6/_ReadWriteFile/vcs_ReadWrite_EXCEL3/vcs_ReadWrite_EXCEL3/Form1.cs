﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using Excel = Microsoft.Office.Interop.Excel;

namespace vcs_ReadWrite_EXCEL3
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

        private void btnCreateChart_Click(object sender, EventArgs e)
        {
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

        private void button1_Click(object sender, EventArgs e)
        {
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
    }
}
