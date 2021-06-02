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
using Excel = Microsoft.Office.Interop.Excel;

namespace vcs_DataGridView6_Excel
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\__RW\_excel\Books.xlsx";

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

            // Get the sheet's values.
            object[,] values = (object[,])used_range.Value2;

            // Get the column titles.
            SetGridColumns(dataGridView1, values, max_col);

            // Get the data.
            SetGridContents(dataGridView1, values, max_row, max_col);

            // Close the workbook without saving changes.
            workbook.Close(false, Type.Missing, Type.Missing);

            // Close the Excel server.
            excel_app.Quit();
        }

        // Set the grid's column names from row 1.
        private void SetGridColumns(DataGridView dgv,
            object[,] values, int max_col)
        {
            dataGridView1.Columns.Clear();

            // Get the title values.
            for (int col = 1; col <= max_col; col++)
            {
                string title = (string)values[1, col];
                dgv.Columns.Add("col_" + title, title);
            }
        }

        // Set the grid's contents.
        private void SetGridContents(DataGridView dgv,
            object[,] values, int max_row, int max_col)
        {
            // Copy the values into the grid.
            for (int row = 2; row <= max_row; row++)
            {
                object[] row_values = new object[max_col];
                for (int col = 1; col <= max_col; col++)
                {
                    row_values[col - 1] = values[row, col];
                }
                dgv.Rows.Add(row_values);
            }
        }
    }
}
