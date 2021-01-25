using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Excel = Microsoft.Office.Interop.Excel;

namespace vcs_ReadWrite_EXCEL3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
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
    }
}
