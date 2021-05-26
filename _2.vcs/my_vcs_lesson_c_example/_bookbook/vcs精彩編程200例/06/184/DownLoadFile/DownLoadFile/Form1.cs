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
using System.Runtime.InteropServices;

namespace DownLoadFile
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        string strName = "";//记录要下载的文件名

        private void Form1_Load(object sender, EventArgs e)
        {
            try
            {
                //监视剪贴板是否有数据
                string strPath = Clipboard.GetData(DataFormats.Text).ToString();
                //验证网址格式
                if (Regex.IsMatch(strPath, @"http(s)?://([\w-]+\.)+[\w-]+(/[\w- ./?%&=]*)?"))
                {
                    textBox1.Text = strPath;
                    strName = strPath.Substring(strPath.LastIndexOf("/") + 1);
                }
                //读取文件存放的默认路径
                textBox2.Text = ReadString("SysSet", "RootPath", "", Application.StartupPath + "\\SysSet.ini");
                textBox3.Text = strName;
            }
            catch { }
        }

        //下载文件
        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox2.Text.EndsWith("\\"))
                DownloadFile(textBox2.Text + strName, textBox1.Text);
            else
                DownloadFile(textBox2.Text + "\\" + strName, textBox1.Text);
        }

        //选择存放路径，并存储到INI文件中
        private void button4_Click(object sender, EventArgs e)
        {
            folderBrowserDialog1.SelectedPath = ReadString("SysSet", "RootPath", "", Application.StartupPath + "\\SysSet.ini");
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                textBox2.Text = folderBrowserDialog1.SelectedPath;
                WritePrivateProfileString("SysSet", "RootPath", folderBrowserDialog1.SelectedPath, Application.StartupPath + "\\SysSet.ini");
            }
        }

        //下载地址改变时，相应的下载文件发生改变
        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            if (textBox1.Text.Contains("/"))
            {
                textBox3.Text = textBox1.Text.Substring(textBox1.Text.LastIndexOf("/") + 1);
                strName = textBox3.Text;
            }
        }

        #region 以断点续传方式下载文件
        /// <summary>
        /// 以断点续传方式下载文件
        /// </summary>
        /// <param name="strFileName">下载文件的保存路径</param>
        /// <param name="strUrl">文件下载地址</param>
        public void DownloadFile(string strFileName, string strUrl)
        {
            //打开上次下载的文件或新建文件
            long SPosition = 0;
            FileStream FStream;
            if (File.Exists(strFileName))
            {
                FStream = File.OpenWrite(strFileName);
                SPosition = FStream.Length;
                FStream.Seek(SPosition, SeekOrigin.Current);//移动文件流中的当前指针
            }
            else
            {
                FStream = new FileStream(strFileName, FileMode.Create);
                SPosition = 0;
            }
            //打开网络连接
            try
            {
                HttpWebRequest myRequest = (HttpWebRequest)HttpWebRequest.Create(strUrl);
                if (SPosition > 0)
                    myRequest.AddRange((int)SPosition);//设置Range值
                //向服务器请求，获得服务器的回应数据流
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
                MessageBox.Show("文件下载完成！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            catch
            {
                FStream.Close();
            }
        }
        #endregion

        #region 为INI文件中指定的节点取得字符串
        /// <summary>
        /// 为INI文件中指定的节点取得字符串
        /// </summary>
        /// <param name="lpAppName">欲在其中查找关键字的节点名称</param>
        /// <param name="lpKeyName">欲获取的项名</param>
        /// <param name="lpDefault">指定的项没有找到时返回的默认值</param>
        /// <param name="lpReturnedString">指定一个字串缓冲区，长度至少为nSize</param>
        /// <param name="nSize">指定装载到lpReturnedString缓冲区的最大字符数量</param>
        /// <param name="lpFileName">INI文件名</param>
        /// <returns>复制到lpReturnedString缓冲区的字节数量，其中不包括那些NULL中止字符</returns>
        [DllImport("kernel32")]
        public static extern int GetPrivateProfileString(
            string lpAppName,
            string lpKeyName,
            string lpDefault,
            StringBuilder lpReturnedString,
            int nSize,
            string lpFileName);
        #endregion

        #region 修改INI文件中内容
        /// <summary>
        /// 修改INI文件中内容
        /// </summary>
        /// <param name="lpApplicationName">欲在其中写入的节点名称</param>
        /// <param name="lpKeyName">欲设置的项名</param>
        /// <param name="lpString">要写入的新字符串</param>
        /// <param name="lpFileName">INI文件名</param>
        /// <returns>非零表示成功，零表示失败</returns>
        [DllImport("kernel32")]
        public static extern int WritePrivateProfileString(
            string lpApplicationName,
            string lpKeyName,
            string lpString,
            string lpFileName);
        #endregion

        #region 从INI文件中读取指定节点的内容
        /// <summary>
        /// 从INI文件中读取指定节点的内容
        /// </summary>
        /// <param name="section">INI节点</param>
        /// <param name="key">节点下的项</param>
        /// <param name="def">没有找到内容时返回的默认值</param>
        /// <param name="def">要读取的INI文件</param>
        /// <returns>读取的节点内容</returns>
        public static string ReadString(string section, string key, string def, string fileName)
        {
            StringBuilder temp = new StringBuilder(1024);
            GetPrivateProfileString(section, key, def, temp, 1024, fileName);
            return temp.ToString();
        }
        #endregion

        private void button3_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}