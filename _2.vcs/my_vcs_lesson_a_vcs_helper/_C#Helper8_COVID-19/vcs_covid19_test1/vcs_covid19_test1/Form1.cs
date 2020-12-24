using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;   //for SecurityProtocolType
using System.IO;    //for File
using System.Diagnostics;	//for Stopwatch

namespace vcs_covid19_test1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Allow TLS 1.1 and TLS 1.2 protocols for file download.
            ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // Compose the local data file name.
            string filename = "state_data" + DateTime.Now.ToString("yyyy_MM_dd") + ".csv";


            // Download today's data.
            const string url = "https://covidtracking.com/api/v1/states/daily.csv";

            richTextBox1.Text += "LoadData \tURL : " + url + "\tfile : " + filename + "\n";

            Stopwatch sw = new Stopwatch();
            sw.Start();

            DownloadFile(url, filename);

            sw.Stop();
            richTextBox1.Text += "經過時間 : " + sw.Elapsed.TotalSeconds.ToString("0.00") + " 秒\n";
            richTextBox1.Text += "經過時間 : " + sw.Elapsed.TotalSeconds.ToString() + " 秒\n";
            richTextBox1.Text += "經過時間 : " + sw.Elapsed.TotalMilliseconds.ToString() + " 毫秒\n";
        }

        // Download today's data.
        private void DownloadFile(string url, string filename)
        {
            // See if we have today's file.
            if (!File.Exists(filename))
            {
                // Download the file.
                this.Cursor = Cursors.WaitCursor;
                Application.DoEvents();

                try
                {
                    // Make a WebClient.
                    WebClient web_client = new WebClient();

                    // Download the file.
                    web_client.DownloadFile(url, filename);
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message, "Download Error",
                        MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
                }
                finally
                {
                    this.Cursor = Cursors.Default;
                }
            }
        }

    }

    public class Protocols
    {
        public const SecurityProtocolType
            protocol_SystemDefault = 0,
            protocol_Ssl3 = (SecurityProtocolType)48,
            protocol_Tls = (SecurityProtocolType)192,
            protocol_Tls11 = (SecurityProtocolType)768,
            protocol_Tls12 = (SecurityProtocolType)3072;
    }

}
