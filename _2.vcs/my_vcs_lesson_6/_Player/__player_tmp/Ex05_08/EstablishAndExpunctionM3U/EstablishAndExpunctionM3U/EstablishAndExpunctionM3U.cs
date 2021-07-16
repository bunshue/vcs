using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace EstablishAndExpunctionM3U
{
    public partial class EstablishAndExpunctionM3U : Form
    {
        string filename_w;  //播放清單檔案

        #region 變數宣告
        private static string temp = null;//保存打開文件的文件路徑
        #endregion

        #region  建立m3u文件
        /// <summary>
        /// 建立m3u文件
        /// </summary>
        /// <param FileDir="string">m3u路徑</param>
        public void m3uCreate(string FileDir)
        {
            FileStream fs;//宣告一個公開以文件為主的 Stream對象，既支援同步讀寫操作，也支援異步讀寫操作
            Byte[] info;//宣告一個字節數組
            if (File.Exists(FileDir)) //如果文件存在,則退出操作
            {
                MessageBox.Show("文件已存在，請重新設定文件名！");//彈出訊息提示
                return;//直接傳回
            }
            else    //如果文件不存在,則建立File.CreateText對像
            {
                fs = File.Create(FileDir);//建立M3U文件
            }
            info = new UTF8Encoding(true).GetBytes("#EXTM3U");//定義M3U文件的編碼方式
            fs.Write(info, 0, info.Length);//向數據流中寫入內容
            fs.Close();//關閉FileStream對像
            fs.Dispose();//釋放FileStream對像所佔用的資源
        }
        #endregion

        #region  寫入m3u文件
        /// <summary>
        /// 寫入m3u文件
        /// </summary>
        /// <param FName="string">播放文件名</param>
        /// <param FDir="string">播放文件路徑</param>
        /// <param FileDir="string">m3u路徑</param>
        public void m3uWrite(string FName, string FDir, string FileDir)
        {
            if (!File.Exists(FileDir))//當不存在文件路徑時
            {
                MessageBox.Show("文件不存在！aaaa");//彈出訊息提示
                return;//直接傳回
            }
            StreamWriter sw = new StreamWriter(FileDir, true, Encoding.Default);//定義完成一個 TextWriter對象，使其以一種特定的編碼向流中寫入字符
            sw.WriteLine();//將行結束符寫入文字流
            sw.Write(FDir, Encoding.Default);//將數據流中的文件以特定的編碼方式寫入指定路徑中的文件
            sw.Flush();//清理目前編寫器的所有緩衝區，並使所有緩衝數據寫入基礎串流
            sw.Close();//關閉目前的 StreamWriter 對像和基礎串流
            sw.Dispose();//釋放由此 TextWriter 對像使用的所有資源
        }
        #endregion

        public EstablishAndExpunctionM3U()
        {
            InitializeComponent();
        }

        private void EstablishAndExpunctionM3U_Load(object sender, EventArgs e)
        {
            filename_w = Application.StartupPath + "\\m3u_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".m3u"; //播放清單檔案
            richTextBox1.Text += "建立一個M3U文件 : " + filename_w + "\n";
            m3uCreate(filename_w);//建立一個M3U文件
            M3UPath.Text = filename_w;
        }

        private void openMusic_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "開啟\n";
            string filename = @"C:\______test_files\_mp3\16.監獄風雲.mp3";

            musicPath.Text = filename;
            musicName.Text = Path.GetFileNameWithoutExtension(musicPath.Text);//保存打開的文件的文件名
        }

        private void writeIn_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "匯出清單\t";
            richTextBox1.Text += "內容 : " + musicName.Text + "\t" + musicPath.Text + "\t" + M3UPath.Text + "\n";
            m3uWrite(musicName.Text, musicPath.Text, M3UPath.Text);//向M3U文件中寫入內容
        }
    }
}
