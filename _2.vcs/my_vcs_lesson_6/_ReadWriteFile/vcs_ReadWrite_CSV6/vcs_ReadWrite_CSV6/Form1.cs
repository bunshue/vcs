using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

// Open the Add Reference dialog. On the COM tab,
// add a reference to "Microsoft.Office.Interop.Excel"
using Excel = Microsoft.Office.Interop.Excel;

namespace vcs_ReadWrite_CSV6
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

        // Open a delimited file in Excel.
        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\__RW\_csv\F0035CH1.CSV";

            richTextBox1.Text += "開啟檔案 : " + filename + "\n";

            // Get the Excel application object.
            Excel.Application excel_app = new Excel.ApplicationClass();

            // Make Excel visible (optional).
            excel_app.Visible = true;

            // Open the file.
            excel_app.Workbooks.Open(
                filename,                   // Filename
                Type.Missing,
                Type.Missing,
                Excel.XlFileFormat.xlCSV,   // Format
                Type.Missing,
                Type.Missing,
                Type.Missing,
                Type.Missing,
                ",",                        // Delimiter
                Type.Missing,
                Type.Missing,
                Type.Missing,
                Type.Missing,
                Type.Missing,
                Type.Missing);


        }
    }
}
