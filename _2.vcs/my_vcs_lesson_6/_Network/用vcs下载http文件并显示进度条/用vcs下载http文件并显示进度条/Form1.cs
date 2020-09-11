using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 用vcs下载http文件并显示进度条
{
    public partial class Form1 : Form
    {
        string srcAddress = "http://weisico.com/program/2015/0630/237.html";
        string tarAddress = @"C:\______test_files\aaaaaaaa.html";

        public Form1()
        {
            InitializeComponent();
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


        private void button1_Click(object sender, EventArgs e)
        {
            //textBox1存放URL地址，textBox2存放另存为路径
            DownloadFile(srcAddress, tarAddress, progressBar1, label1);

        }


    }
}
