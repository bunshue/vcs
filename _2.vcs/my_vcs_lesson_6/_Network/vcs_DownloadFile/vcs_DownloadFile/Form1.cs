using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.IO;        //for StreamReader
using System.Threading; //for Thread
namespace vcs_DownloadFile
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        //用C#下载http文件 ST
        private WebClient client = new WebClient();
        string srcAddress = "http://weisico.com/program/2015/0630/237.html";
        string tarAddress = Application.StartupPath;

        private void button2_Click(object sender, EventArgs e)
        {
            Thread th = new Thread(new ThreadStart(StartDownload));
            th.Start();
        }

        private void StartDownload()
        {
            string URL = srcAddress;
            int n = URL.LastIndexOf("/");
            string URLAddress = URL;//.Substring(0, n);
            string fileName = URL.Substring(n + 1, URL.Length - n - 1);
            string Dir = tarAddress + "\\";
            //下载文件，直接覆盖
            string Path = Dir + fileName;

            //Datetime.Now.ToFileTime.ToString()用于区别下载时间
            // string Path = Dir +DateTime.Now.ToFileTime().ToString() + fileName  ;

            try
            {
                WebRequest myre = WebRequest.Create(URLAddress);

                Stream stream = client.OpenRead(URLAddress);
                StreamReader reader = new StreamReader(stream);

                FileStream outputStream = new FileStream(Path, FileMode.OpenOrCreate);
                try
                {
                    int bufferSize = 100; // 网络速度快的话可以设置大一点，慢的话可以小一点
                    int nRealCount;
                    byte[] bBuffer = new byte[bufferSize];
                    nRealCount = stream.Read(bBuffer, 0, bufferSize);

                    // 下载，一面读一面下载是最好的方式。这样就不用声明多大的数组了
                    while (nRealCount > 0)
                    {
                        outputStream.Write(bBuffer, 0, nRealCount);
                        nRealCount = stream.Read(bBuffer, 0, bBuffer.Length);
                    }
                    //richTextBox1.Text += "下載完畢, 檔案 : " + Path + "\n";
                    MessageBox.Show("下載完畢, 檔案 : " + Path);
                }
                catch (WebException ex)
                {
                    //richTextBox1.Text += "下載錯誤, 原因 : " + ex.Message + "\n";
                    MessageBox.Show(ex.Message, "Error");
                    this.Text = "";
                }
                finally
                {
                    stream.Close();
                    reader.Close();
                    outputStream.Close();
                }

                //Application.Exit();

            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
                //MessageBox.Show("请输入正确的文件地址");
            }
        }
        //用C#下载http文件 SP

        //用C#下载http文件 並顯示進度條 ST
        private void button3_Click(object sender, EventArgs e)
        {
            string srcAddress = "http://weisico.com/program/2015/0630/237.html";
            //string tarAddress = @"C:\______test_files\aaaaaaaa.html";
            string tarAddress = Application.StartupPath + "\\" + "aaaaaaaa.html";

            DownloadFile(srcAddress, tarAddress, progressBar1, label1);

            richTextBox1.Text += "下載完畢, 檔案 : " + tarAddress + "\n";
        }

        /// <summary>
        /// c#,.net 下载文件
        /// </summary>
        /// <param name="URL">下载文件地址</param>
        ///
        /// <param name="Filename">下载后的存放地址</param>
        /// <param name="Prog">用于显示的进度条</param>
        ///
        public void DownloadFile(string URL, string filename, System.Windows.Forms.ProgressBar prog, System.Windows.Forms.Label label1)
        {
            if (URL == "")
            {
                MessageBox.Show("URL为空", "消息提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
                return;
            }
            float percent = 0;
            try
            {
                System.Net.HttpWebRequest Myrq = (System.Net.HttpWebRequest)System.Net.HttpWebRequest.Create(URL);
                System.Net.HttpWebResponse myrp = (System.Net.HttpWebResponse)Myrq.GetResponse();
                long totalBytes = myrp.ContentLength;
                if (prog != null)
                {
                    prog.Maximum = (int)totalBytes;
                }
                System.IO.Stream st = myrp.GetResponseStream();
                System.IO.Stream so = new System.IO.FileStream(filename, System.IO.FileMode.Create);
                long totalDownloadedByte = 0;
                byte[] by = new byte[1024];
                int osize = st.Read(by, 0, (int)by.Length);
                while (osize > 0)
                {
                    totalDownloadedByte = osize + totalDownloadedByte;
                    System.Windows.Forms.Application.DoEvents();
                    so.Write(by, 0, osize);
                    if (prog != null)
                    {
                        prog.Value = (int)totalDownloadedByte;
                    }
                    osize = st.Read(by, 0, (int)by.Length);

                    percent = (float)totalDownloadedByte / (float)totalBytes * 100;
                    label1.Text = "当前下载进度" + percent.ToString("00.00") + "%";
                    System.Windows.Forms.Application.DoEvents(); //必须加注这句代码，否则label1将因为循环执行太快而来不及显示信息
                    if (percent == 100)
                    {
                        MessageBox.Show("下载完成", "消息提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    }
                }
                so.Close();
                st.Close();
            }
            catch (System.Exception ee)
            {
                //throw;
                richTextBox1.Text += ee.Message + "\n";
            }
        }





    }
}
