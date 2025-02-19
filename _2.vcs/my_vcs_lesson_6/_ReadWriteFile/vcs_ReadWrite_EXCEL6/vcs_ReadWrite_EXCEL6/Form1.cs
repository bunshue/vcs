﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

// Open the Add References dialog. On the COM tab, select:
//
//      Microsoft 12.0 Object Library
//
// (Or whatever version you have installed on your system.)

// More examples of automating Excel from C#:
//
//      http://support.microsoft.com/kb/302084
//      http://support.microsoft.com/default.aspx?scid=kb;en-us;311452

using Excel = Microsoft.Office.Interop.Excel;

namespace vcs_ReadWrite_EXCEL6
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

        // Read from the Excel workbook.
        private void btnRead_Click(object sender, EventArgs e)
        {
            string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\Items.xlsx";

            richTextBox1.Text += "開啟檔案 : " + filename + "\n";

            // Get the Excel application object.
            Excel.Application excel_app = new Excel.ApplicationClass();

            // Make Excel visible (optional).
            excel_app.Visible = true;

            // Open the workbook read-only.
            Excel.Workbook workbook = excel_app.Workbooks.Open(filename,
                Type.Missing, true, Type.Missing, Type.Missing,
                Type.Missing, Type.Missing, Type.Missing, Type.Missing,
                Type.Missing, Type.Missing, Type.Missing, Type.Missing,
                Type.Missing, Type.Missing);

            // Get the first worksheet.
            Excel.Worksheet sheet = (Excel.Worksheet)workbook.Sheets[1];

            // Get the titles and values.
            SetTitleAndListValues(sheet, 1, 1, lblTitle1, lstItems1);
            SetTitleAndListValues(sheet, 1, 2, lblTitle2, lstItems2);

            // Close the workbook without saving changes.
            workbook.Close(false, Type.Missing, Type.Missing);

            // Close the Excel server.
            excel_app.Quit();
        }

        // Set a title Label and the values in a ListBox.
        // Get the title from cell (row, col). Get the values from
        // cell (row + 1, col) to the end of the column.
        private void SetTitleAndListValues(Excel.Worksheet sheet, int row, int col, Label lbl, ListBox lst)
        {
            richTextBox1.Text += "R = " + row.ToString() + ", C = " + col.ToString() + "\n";

            Excel.Range range;

            // Set the title.
            range = (Excel.Range)sheet.Cells[row, col];

            lbl.Text = (string)range.Value2;
            lbl.ForeColor = System.Drawing.ColorTranslator.FromOle((int)(double)range.Font.Color);
            lbl.BackColor = System.Drawing.ColorTranslator.FromOle((int)(double)range.Interior.Color);

            richTextBox1.Text += "取得Title : " + (string)range.Value2 + "\n";

            // Get the values.
            // Find the last cell in the column.
            range = (Excel.Range)sheet.Columns[col, Type.Missing];
            Excel.Range last_cell = range.get_End(Excel.XlDirection.xlDown);

            // Get a Range holding the values.
            Excel.Range first_cell = (Excel.Range)sheet.Cells[row + 1, col];
            Excel.Range value_range = (Excel.Range)sheet.get_Range(first_cell, last_cell);

            // Get the values.
            object[,] range_values = (object[,])value_range.Value2;

            // Convert this into a 1-dimensional array.
            // Note that the Range's array has lower bounds 1.
            int num_items = range_values.GetUpperBound(0);
            string[] values1 = new string[num_items];
            for (int i = 0; i < num_items; i++)
            {
                values1[i] = (string)range_values[i + 1, 1];
                richTextBox1.Text += "取得Item : " + values1[i] + "\n";
            }

            // Display the values in the ListBox.
            lst.DataSource = values1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //開啟Excel檔並新增工作表
            string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\vcs_ReadWrite_EXCEL6_Items.xlsx";
            richTextBox1.Text += "開啟檔案 : " + filename + "\n";

            // Get the Excel application object.
            Excel.Application excel_app = new Excel.ApplicationClass();

            // Make Excel visible (optional).
            excel_app.Visible = true;

            // Open the workbook.
            Excel.Workbook workbook = excel_app.Workbooks.Open(filename,
                Type.Missing, Type.Missing, Type.Missing, Type.Missing,
                Type.Missing, Type.Missing, Type.Missing, Type.Missing,
                Type.Missing, Type.Missing, Type.Missing, Type.Missing,
                Type.Missing, Type.Missing);

            // See if the worksheet already exists.
            string sheet_name = DateTime.Now.ToString("MM-dd-yy");

            Excel.Worksheet sheet = FindSheet(workbook, sheet_name);
            if (sheet == null)
            {
                // Add the worksheet at the end.
                sheet = (Excel.Worksheet)workbook.Sheets.Add(
                    Type.Missing, workbook.Sheets[workbook.Sheets.Count],
                    1, Excel.XlSheetType.xlWorksheet);
                sheet.Name = DateTime.Now.ToString("MM-dd-yy");
            }

            // Add some data to individual cells.
            sheet.Cells[1, 1] = "A";
            sheet.Cells[1, 2] = "B";
            sheet.Cells[1, 3] = "C";

            // Make that range of cells bold and red.
            Excel.Range header_range = sheet.get_Range("A1", "C1");
            header_range.Font.Bold = true;
            header_range.Font.Color = System.Drawing.ColorTranslator.ToOle(System.Drawing.Color.Red);
            header_range.Interior.Color = System.Drawing.ColorTranslator.ToOle(System.Drawing.Color.Pink);

            // Add some data to a range of cells.
            int[,] values = 
            { 
                { 2,  4,  6},
                { 3,  6,  9},
                { 4,  8, 12},
                { 5, 10, 15},
            };
            Excel.Range value_range = sheet.get_Range("A2", "C5");
            value_range.Value2 = values;

            // Save the changes and close the workbook.
            workbook.Close(true, Type.Missing, Type.Missing);

            // Close the Excel server.
            excel_app.Quit();

            richTextBox1.Text += "完成\n";
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
    }
}
