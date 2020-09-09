using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.IO;
using System.Threading;

namespace 用vcs下载http文件
{
    public partial class Form1 : Form
    {
        private WebClient client = new WebClient();

        string srcAddress = "http://weisico.com/program/2015/0630/237.html";
        string tarAddress = @"C:\______test_files\";

        public Form1()
        {
            InitializeComponent();
        }

        private void StartDownload()
        {
            string URL = srcAddress;
            int n = URL.LastIndexOf("/");
            string URLAddress = URL;//.Substring(0, n);
            string fileName = URL.Substring(n + 1, URL.Length - n - 1);
            string Dir = tarAddress;
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
                    MessageBox.Show("下载完毕!");
                }
                catch (WebException exp)
                {
                    MessageBox.Show(exp.Message, "Error");
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
            catch (Exception exp)
            {
                MessageBox.Show(exp.Message);
                //MessageBox.Show("请输入正确的文件地址");
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (srcAddress == "" || tarAddress == "")
            {
                richTextBox1.Text += "下载源地址和目标地址不能为空\n";
            }
            else
            {
                Thread th = new Thread(new ThreadStart(StartDownload));
                th.Start();
            }


        }
    }
}
