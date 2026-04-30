using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Net;
using System.Text.RegularExpressions;

namespace vcs_DownloadFile
{
    public partial class Form1 : Form
    {
        string strName = "";//記錄要下載的文件名

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            try
            {
                //監視剪貼板是否有數據
                string strPath = Clipboard.GetData(DataFormats.Text).ToString();
                //驗證網址格式
                if (Regex.IsMatch(strPath, @"http(s)?://([\w-]+\.)+[\w-]+(/[\w- ./?%&=]*)?"))
                {
                    textBox1.Text = strPath;
                    strName = strPath.Substring(strPath.LastIndexOf("/") + 1);
                }
                textBox3.Text = strName;
            }
            catch { }
        }

        //下載文件
        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox2.Text.EndsWith("\\"))
            {
                DownloadFile(textBox2.Text + strName, textBox1.Text);
            }
            else
            {
                DownloadFile(textBox2.Text + "\\" + strName, textBox1.Text);
            }
        }

        //下載地址改變時，相應的下載文件發生改變
        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            if (textBox1.Text.Contains("/"))
            {
                textBox3.Text = textBox1.Text.Substring(textBox1.Text.LastIndexOf("/") + 1);
                strName = textBox3.Text;
            }
        }

        // 以斷點續傳方式下載文件 ST
        /// <summary>
        /// 以斷點續傳方式下載文件
        /// </summary>
        /// <param name="strFileName">下載文件的保存路徑</param>
        /// <param name="strUrl">文件下載地址</param>
        public void DownloadFile(string strFileName, string strUrl)
        {
            //打開上次下載的文件或新建文件
            long SPosition = 0;
            FileStream FStream;
            if (File.Exists(strFileName))
            {
                FStream = File.OpenWrite(strFileName);
                SPosition = FStream.Length;
                FStream.Seek(SPosition, SeekOrigin.Current);//移動文件流中的當前指針
            }
            else
            {
                FStream = new FileStream(strFileName, FileMode.Create);
                SPosition = 0;
            }
            //打開網絡連接
            try
            {
                HttpWebRequest myRequest = (HttpWebRequest)HttpWebRequest.Create(strUrl);
                if (SPosition > 0)
                    myRequest.AddRange((int)SPosition);//設置Range值
                //向服務器請求，獲得服務器的回應數據流
                Stream myStream = myRequest.GetResponse().GetResponseStream();
                byte[] btContent = new byte[512];
                int intSize = 0;
                intSize = myStream.Read(btContent, 0, 512);
                while (intSize > 0)
                {
                    FStream.Write(btContent, 0, intSize);
                    intSize = myStream.Read(btContent, 0, 512);
                }
                FStream.Close();
                myStream.Close();
                MessageBox.Show("文件下載完成！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            catch
            {
                FStream.Close();
            }
        }
        // 以斷點續傳方式下載文件 SP

        private void button3_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
