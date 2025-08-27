using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Path

//參考/加入參考/PdfSharp.dll
using PdfSharp;
using PdfSharp.Pdf;
using PdfSharp.Drawing;

namespace vcs_ReadWrite_PDF5
{
    public partial class Form1 : Form
    {
        string filename1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
        string filename2 = string.Empty;

        bool success = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            filename2 =
                Path.GetDirectoryName(filename1) + "\\" +
                Path.GetFileNameWithoutExtension(filename1) + ".pdf";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            success = false;
            backgroundWorker1.RunWorkerAsync(new string[2] { filename1, filename2 });
        }

        private void backgroundWorker1_DoWork(object sender, DoWorkEventArgs e)
        {
            try
            {
                string source = (e.Argument as string[])[0];
                string destinaton = (e.Argument as string[])[1];

                PdfDocument doc = new PdfDocument();
                doc.Pages.Add(new PdfPage());
                XGraphics xgr = XGraphics.FromPdfPage(doc.Pages[0]);
                XImage img = XImage.FromFile(source);

                xgr.DrawImage(img, 0, 0);
                doc.Save(destinaton);
                doc.Close();
                success = true;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void backgroundWorker1_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {

            if (success == true)
            {
                richTextBox1.Text += "圖片 : " + filename1 + "\n";
                richTextBox1.Text += "pdf :  " + filename2 + "\n";
                richTextBox1.Text += "轉換完成\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            try
            {
                string filename1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
                string filename2 = Application.StartupPath + "\\pdf_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".pdf";

                PdfDocument doc = new PdfDocument();
                doc.Pages.Add(new PdfPage());
                XGraphics xgr = XGraphics.FromPdfPage(doc.Pages[0]);
                XImage img = XImage.FromFile(filename1);

                xgr.DrawImage(img, 0, 0);

                try
                {

                    doc.Save(filename2);
                    richTextBox1.Text += "存檔成功\n";
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

