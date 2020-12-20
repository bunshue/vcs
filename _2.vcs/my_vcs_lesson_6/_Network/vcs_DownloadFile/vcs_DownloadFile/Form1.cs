using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;

namespace vcs_DownloadFile
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename_remote = @"http://www.csharphelper.com/examples/howto_download_file.zip";
            string filename_local = @"aaaa.zip";

            richTextBox1.Text += "遠端檔案: " + filename_remote + "\n";
            richTextBox1.Text += "本地檔案: " + filename_local + "\n";
            richTextBox1.Text += "\n開始下載檔案...\n\n";

            Application.DoEvents();

            try
            {
                // Make a WebClient.
                WebClient web_client = new WebClient();

                // Download the file.
                web_client.DownloadFile(filename_remote, filename_local);

                richTextBox1.Text += "下載完成\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "下載失敗，原因: \t" + ex.Message + "\n";
            }
        }
    }
}
