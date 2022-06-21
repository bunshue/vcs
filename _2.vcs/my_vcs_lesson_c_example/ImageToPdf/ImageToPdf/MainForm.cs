using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.IO;
using System.Diagnostics;

using PdfSharp;
using PdfSharp.Pdf;
using PdfSharp.Drawing;

namespace ImageToPdf
{
    public partial class MainForm : Form
    {

        private string srcFile, destFile;
        bool success = false;

        public MainForm()
        {
            InitializeComponent();
        }

        private void btnSelectSrc_Click(object sender, EventArgs e)
        {
            if (ofdSrcFile.ShowDialog() != DialogResult.OK)
                return;

            srcFile = ofdSrcFile.FileName;
            txbxSrcFile.Text = srcFile;

            txbxDestFile.Text =
                Path.GetDirectoryName(srcFile) + "\\" +
                Path.GetFileNameWithoutExtension(srcFile) + ".pdf";
            destFile = txbxDestFile.Text;   
        }

        private void btnSelectDest_Click(object sender, EventArgs e)
        {
            if (sfdDestFile.ShowDialog() != DialogResult.OK)
                return;

            destFile = sfdDestFile.FileName;
            txbxDestFile.Text = destFile;
        }

        private void btnConvert_Click(object sender, EventArgs e)
        {
            errProv.Clear();

            if (txbxSrcFile.Text.Length == 0)
            {
                errProv.SetError(txbxSrcFile, "Please point source file.");
                return;
            }
            else if (txbxDestFile.Text.Length == 0)
            {
                errProv.SetError(txbxDestFile, "Please point destination file.");
                return;
            }


            success = false;
            bw.RunWorkerAsync(new string[2] { srcFile, destFile });            
            toolStripProgressBar1.Style = ProgressBarStyle.Marquee;

        }

        private void bw_DoWork(object sender, DoWorkEventArgs e)
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

        private void bw_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            toolStripProgressBar1.Style = ProgressBarStyle.Blocks;
            toolStripProgressBar1.Value = 0;

            if (success)
                MessageBox.Show("The converion ended successfully.", "Done", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            errProv.Clear();

            if (rbSrc.Checked && txbxSrcFile.Text.Length == 0)
            {
                errProv.SetError(txbxSrcFile, "Please point source file.");
                return;
            }
            else if (rbDest.Checked && txbxDestFile.Text.Length == 0)
            {
                errProv.SetError(txbxDestFile, "Please point destination file.");
                return;
            }

            try
            {
                if (rbSrc.Checked)
                    Process.Start(srcFile);
                else if (rbDest.Checked)
                    Process.Start(destFile);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);            
            }

            
            



        }
    }
}