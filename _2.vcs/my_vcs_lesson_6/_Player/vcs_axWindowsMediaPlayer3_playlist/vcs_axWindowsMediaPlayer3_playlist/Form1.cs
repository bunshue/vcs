using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_axWindowsMediaPlayer3_playlist
{
    public partial class Form1 : Form
    {
        string filename_r = @"C:\______test_files\_mp3\list.m3u";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.Text = "mp3播放器";
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);


        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void br_clear_listbox_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.InitialDirectory = @"C:\______test_files\_mp3";
            openFileDialog1.Multiselect = true;
            openFileDialog1.FileName = "";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                foreach (string str in openFileDialog1.FileNames)
                {
                    //richTextBox1.Text += "str = " + str + "\n";
                    listBox1.Items.Add(str);
                }

                if (openFileDialog1.FileNames.Length == listBox1.Items.Count)   //初次加入清單 預設播放第一首
                {
                    this.Text = listBox1.Items[0].ToString();
                    axWindowsMediaPlayer1.URL = listBox1.Items[0].ToString();
                }

                richTextBox1.Text += "本次開啟檔案 : " + openFileDialog1.FileNames.Length.ToString() + " 個\t";
                richTextBox1.Text += "清單內共有檔案 : " + listBox1.Items.Count.ToString() + " 個\n";
            }

        }


        private void listBox1_DoubleClick(object sender, EventArgs e)
        {
            string str = listBox1.Items[listBox1.SelectedIndex].ToString();
            this.Text = str;
            axWindowsMediaPlayer1.URL = str;

        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (button3.Text == "暫停")
            {
                button3.Text = "繼續";
                axWindowsMediaPlayer1.Ctlcontrols.pause();
            }
            else
            {
                button3.Text = "暫停";
                axWindowsMediaPlayer1.Ctlcontrols.play();
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "old filename = " + openFileDialog1.FileName + "\n";
            richTextBox1.Text += "url = " + axWindowsMediaPlayer1.URL + "\n";
            if (axWindowsMediaPlayer1.URL == "")
            {
                richTextBox1.Text += "無檔可播\n";
            }
            else
            {
                this.Text = axWindowsMediaPlayer1.URL;
                axWindowsMediaPlayer1.Ctlcontrols.play();
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            axWindowsMediaPlayer1.Ctlcontrols.stop();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //讀入清單
            richTextBox1.Text += "讀取檔案 : " + filename_r + "\n";
            StreamReader sr = new StreamReader(filename_r, Encoding.Default);
            while (sr.Peek() >= 0)
            {
                string line = sr.ReadLine();
                if (line != "")
                {
                    richTextBox1.Text += "加入項目 : " + line + "\n";
                    listBox1.Items.Add(line);
                }
            }
            sr.Close();

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //匯出清單
            string filename_w = Application.StartupPath + "\\m3u_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".m3u";

            int len = listBox1.Items.Count;
            if (len > 0)
            {
                FileStream fs = new FileStream(filename_w, FileMode.Create, FileAccess.Write);
                StreamWriter sw = new StreamWriter(fs, Encoding.GetEncoding("Unicode"));   //指名編碼格式

                int i;
                for (i = 0; i < len; i++)
                {
                    richTextBox1.Text += "i = " + i.ToString() + "\t" + listBox1.Items[i] + "\n";
                    sw.WriteLine(listBox1.Items[i]);
                }

                sw.Flush();
                sw.Close();

            }
            else
            {
                richTextBox1.Text += "播放清單內沒有項目\n";
            }

        }


        public void m3uCreate(string FileDir)   //建立 m3u 檔案
        {
            FileStream fs;//宣告一個公開以文件為主的 Stream對象，既支援同步讀寫操作，也支援異步讀寫操作
            Byte[] info;//宣告一個字節數組
            if (File.Exists(FileDir)) //如果文件存在,則退出操作
            {
                //MessageBox.Show("文件已存在，請重新設定文件名！");//彈出訊息提示
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

        public void m3uWrite(string FDir, string FileDir)
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

        private void button7_Click(object sender, EventArgs e)
        {
            //建立mp3播放清單m3u檔案

            string m3u_filename = Application.StartupPath + "\\m3u_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".m3u"; //播放清單檔案
            richTextBox1.Text += "建立一個M3U文件 : " + m3u_filename + "\n";
            m3uCreate(m3u_filename);//建立一個M3U文件

            string full_filename;   //全名
            string short_filename;  //簡名

            full_filename = @"C:\______test_files\_mp3\16.監獄風雲.mp3";
            short_filename = Path.GetFileNameWithoutExtension(full_filename);//保存打開的文件的文件名
            m3uWrite(full_filename, m3u_filename);//向M3U文件中寫入內容

            /*
            full_filename = @"D:\內視鏡影片\16.010.mp3";
            short_filename = Path.GetFileNameWithoutExtension(full_filename);//保存打開的文件的文件名
            m3uWrite(full_filename, m3u_filename);//向M3U文件中寫入內容

            full_filename = @"D:\內視鏡影片\16.010.mp3";
            short_filename = Path.GetFileNameWithoutExtension(full_filename);//保存打開的文件的文件名
            m3uWrite(full_filename, m3u_filename);//向M3U文件中寫入內容
            */

            full_filename = @"C:\_git\vcs\_2.vcs\______test_files\_wav\start.wav";
            short_filename = Path.GetFileNameWithoutExtension(full_filename);//保存打開的文件的文件名
            m3uWrite(full_filename, m3u_filename);//向M3U文件中寫入內容

        }




    }
}
