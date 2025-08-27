using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

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

namespace vcs_ReadWrite_PDF2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
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


    }
}
