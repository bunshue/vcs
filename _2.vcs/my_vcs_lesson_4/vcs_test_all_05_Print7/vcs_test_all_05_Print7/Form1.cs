using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Printing;

namespace vcs_test_all_05_Print7
{
    public partial class Form1 : Form
    {
        string text_filename = @"D:\_git\vcs\_1.data\______test_files1\article.txt";

        private StreamReader streamReader;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void mnuOpen_Click(object sender, EventArgs e)
        {
            FileStream fileStream = null;

            this.Text = text_filename;

            fileStream = new FileStream(text_filename, FileMode.Open, FileAccess.Read);
            streamReader = new StreamReader(fileStream, System.Text.Encoding.Default);

            TextBox1.Text = streamReader.ReadToEnd();


            streamReader.Close();

            fileStream.Close();
        }

        private void mnuPageSetup_Click(object sender, EventArgs e)
        {
        }

        private void mnuPreview_Click(object sender, EventArgs e)
        {
            streamReader = new StreamReader(text_filename);

            PrintClass printFile = new PrintClass(streamReader);

            //使用 版面設定 的內容
            //if (pageSetting != null)
            //printFile.DefaultPageSettings = pageSetting;

            PrintPreviewDialog1.Document = printFile;
            PrintPreviewDialog1.ShowDialog();

            streamReader.Close();
        }

        private void mnuPrint_Click(object sender, EventArgs e)
        {
            streamReader = new StreamReader(text_filename);

            PrintClass printFile = new PrintClass(streamReader);

            //使用 版面設定 的內容
            //if (pageSetting != null)
            //printFile.DefaultPageSettings = pageSetting;

            PrintDialog1.Document = printFile;
            PrintDialog1.AllowPrintToFile = true;
            PrintDialog1.AllowSelection = true;
            PrintDialog1.AllowSomePages = true;

            if (PrintDialog1.ShowDialog() == DialogResult.OK)
                printFile.Print();

            streamReader.Close();
        }

        private void mnuExit_Click(object sender, EventArgs e)
        {
        }
    }
}
