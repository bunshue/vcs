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
        public EstablishAndExpunctionM3U()
        {
            InitializeComponent();
        }

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
                MessageBox.Show("文件不存在！");//彈出訊息提示
                return;//直接傳回
            }
            StreamWriter ASW = new StreamWriter(FileDir, true, Encoding.Default);//定義完成一個 TextWriter對象，使其以一種特定的編碼向流中寫入字符
            ASW.WriteLine();//將行結束符寫入文字流
            ASW.Write(FDir, Encoding.Default);//將數據流中的文件以特定的編碼方式寫入指定路徑中的文件
            ASW.Flush();//清理目前編寫器的所有緩衝區，並使所有緩衝數據寫入基礎串流
            ASW.Close();//關閉目前的 StreamWriter 對像和基礎串流
            ASW.Dispose();//釋放由此 TextWriter 對像使用的所有資源
        }
        #endregion

        #region  刪除m3u文件
        /// <summary>
        /// 刪除m3u文件
        /// </summary>
        /// <param FileDir="string">m3u路徑</param>
        public void m3uDelete(string FileDir)
        {
            if (!File.Exists(FileDir))//當不存在文件路徑時
            {
                MessageBox.Show("文件不存在!");//彈出訊息提示
                return;//直接傳回
            }
            File.Delete(FileDir);//刪除指定路徑下的文件

        }
        #endregion

        private void found_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\mp3_playlist_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".m3u";
            richTextBox1.Text += "建立\t" + filename + "\n";

            m3uCreate(filename);//建立一個M3U文件
            M3UName.Text = "恭喜你，建立成功！";//在文字框中顯示提示訊息
            M3UName.ForeColor = Color.Red;//設定文字框中文字的顏色
            M3UName.BackColor = Color.Black;//設定文字框的背景顏色
            found.Enabled = false;//設定「建立」按鈕為不可用狀態
        }

        #region 當單擊打開M3U文件的「打開」按鈕時
        private void openM3U_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "開啟\n";
            M3UPath.Text = ListM3UFile();//在文字框中顯示M3U文件的路徑
            richTextBox1.Text += "開啟\t" + M3UPath.Text + "\n";
        }
        #endregion

        #region 自定義一個打開M3U文件方法
        private string ListM3UFile()
        {
            OpenFileDialog M3U_Dialog = new OpenFileDialog(); //宣告一個提示使用者打開文件的對象
            M3U_Dialog.Filter = "M3U文件(*.M3U)|*.M3U"; //取得或設定目前文件名過濾器字串，該字串決定對話框的「另存為文件類型」或「文件類型」框中出現的選擇內容。 （繼承自 FileDialog。）
            if (M3U_Dialog.ShowDialog() == DialogResult.OK)//當選定文件之後單擊「打開」按鈕時
            {
                temp = M3U_Dialog.FileName;//保存所打開的文件名
            }
            return temp;//傳回保存的值
        }
        #endregion


        private void openMusic_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "開啟\n";
            string filename = @"C:\______test_files\_mp3\16.監獄風雲.mp3";

            musicPath.Text = filename;
            musicName.Text = System.IO.Path.GetFileNameWithoutExtension(musicPath.Text);//保存打開的文件的文件名

        }


        #region 單擊「寫入」按鈕時
        private void writeIn_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "寫入\n";
            m3uWrite(musicName.Text, musicPath.Text, M3UPath.Text);//向M3U文件中寫入內容
        }
        #endregion

        #region 單擊「打開」按鈕時
        private void unfold_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "開啟\n";
            fileName.Text = ListM3UFile();//打開一個M3U文件
            richTextBox1.Text += "開啟\t" + fileName.Text + "\n";
        }
        #endregion

        #region 單擊「刪除」按鈕時
        private void Expunction_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "刪除\t" + fileName.Text + "\n";
            m3uDelete(fileName.Text); //刪除指定的文件
            temp = null;//清空變數temp中保存的值
            fileName.Clear();//清空文字框中的內容
            MessageBox.Show("祝賀你，刪除成功！", "訊息提示", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);//彈出訊息提示
        }
        #endregion

        private void M3UName_TextChanged(object sender, EventArgs e)
        {

        }


    }
}
