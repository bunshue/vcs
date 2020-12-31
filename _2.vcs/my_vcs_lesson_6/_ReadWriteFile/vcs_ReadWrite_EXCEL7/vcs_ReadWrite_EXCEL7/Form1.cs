using System;
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

namespace vcs_ReadWrite_EXCEL7
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            txtFile.Text = Path.GetFullPath(
                Path.Combine(Application.StartupPath, @"..\..")) +
                @"\Items.xlsx";
        }

        // Write into the Excel workbook.
        private void btnWrite_Click(object sender, EventArgs e)
        {
            // Get the Excel application object.
            Excel.Application excel_app = new Excel.ApplicationClass();

            // Make Excel visible (optional).
            excel_app.Visible = true;

            // Open the workbook.
            Excel.Workbook workbook = excel_app.Workbooks.Open(txtFile.Text,
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
            header_range.Font.Color = 
                System.Drawing.ColorTranslator.ToOle(System.Drawing.Color.Red);
            header_range.Interior.Color = 
                System.Drawing.ColorTranslator.ToOle(System.Drawing.Color.Pink);

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

            MessageBox.Show("Done");
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
