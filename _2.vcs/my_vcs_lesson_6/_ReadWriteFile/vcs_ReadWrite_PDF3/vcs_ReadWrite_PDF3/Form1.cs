using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;


//參考/加入參考/PdfSharp.dll

using System.IO;
using System.Diagnostics;

using PdfSharp;
using PdfSharp.Pdf;
using PdfSharp.Drawing;

namespace vcs_ReadWrite_PDF3
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

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                string filename1 = @"C:\______test_files\picture1.jpg";
                //string filename2 = @"aaaaa.pdf";

                PdfDocument doc = new PdfDocument();
                doc.Pages.Add(new PdfPage());
                XGraphics xgr = XGraphics.FromPdfPage(doc.Pages[0]);
                XImage img = XImage.FromFile(filename1);

                xgr.DrawImage(img, 0, 0);

                string filename2 = Application.StartupPath + "\\pdf_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".pdf";

                try
                {

                    doc.Save(filename2);
                    richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
                doc.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
