using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Threading;//線程序的命名空間

namespace FileCopyPlan
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private System.Threading.Thread thdAddFile; //建立一個線程
        private string str = "";
        FileStream FormerOpen;//實例化FileStream類
        FileStream ToFileOpen;//實例化FileStream類

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.InitialDirectory = @"C:\_git\vcs\_1.data\______test_files1\";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)//打開文件對話框
            {
                textBox1.Text = openFileDialog1.FileName;//取得源文件的路徑
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)//打開文件夾對話框
            {
                textBox2.Text = folderBrowserDialog1.SelectedPath;//取得目的文件的路徑
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (textBox1.Text.Length == 0 || textBox2.Text.Length == 0)
            {
                richTextBox1.Text += "請選擇原文件路徑或目的文件路徑。\n";
                return;
            }
            else
            {
                str = textBox1.Text;//記錄源文件的路徑
                str = "\\" + str.Substring(str.LastIndexOf('\\') + 1, str.Length - str.LastIndexOf('\\') - 1);//取得源文件的名稱
                thdAddFile = new Thread(new ThreadStart(SetAddFile));//建立一個線程
                thdAddFile.Start();//執行目前線程
            }
        }

        public delegate void AddFile();//定義委託
        /// <summary>
        /// 在線程上執行委託
        /// </summary>
        public void SetAddFile()
        {
            this.Invoke(new AddFile(RunAddFile));//在線程上執行指定的委託
        }

        /// <summary>
        /// 對文件進行複製，並在複製完成後關閉線程
        /// </summary>
        public void RunAddFile()
        {
            CopyFile(textBox1.Text, textBox2.Text + str, 1024, progressBar1);//複製文件
            thdAddFile.Abort();//關閉線程
        }

        /// <summary>
        /// 文件的複製
        /// </summary>
        /// <param FormerFile="string">源文件路徑</param>
        /// <param toFile="string">目的文件路徑</param> 
        /// <param SectSize="int">傳輸大小</param> 
        /// <param progressBar="ProgressBar">ProgressBar控制元件</param> 
        public void CopyFile(string FormerFile, string toFile, int SectSize, ProgressBar progressBar1)
        {
            progressBar1.Value = 0;//設定進度欄的目前位置為0
            progressBar1.Minimum = 0;//設定進度欄的最小值為0
            FileStream fileToCreate = new FileStream(toFile, FileMode.Create);//建立目的文件，如果已存在將被覆蓋
            fileToCreate.Close();//關閉所有資源
            fileToCreate.Dispose();//釋放所有資源
            FormerOpen = new FileStream(FormerFile, FileMode.Open, FileAccess.Read);//以只讀方式打開源文件
            ToFileOpen = new FileStream(toFile, FileMode.Append, FileAccess.Write);//以寫方式打開目的文件
            int max = Convert.ToInt32(Math.Ceiling((double)FormerOpen.Length / (double)SectSize));//根據一次傳輸的大小，計算傳輸的個數
            progressBar1.Maximum = max;//設定進度欄的最大值
            int FileSize;//要拷貝的文件的大小
            if (SectSize < FormerOpen.Length)//如果分段拷貝，即每次拷貝內容小於文件總長度
            {
                byte[] buffer = new byte[SectSize];//根據傳輸的大小，定義一個字節數組
                int copied = 0;//記錄傳輸的大小
                int tem_n = 1;//設定進度欄中進度塊的增加個數
                while (copied <= ((int)FormerOpen.Length - SectSize))//拷貝主體部分
                {
                    FileSize = FormerOpen.Read(buffer, 0, SectSize);//從0開始讀，每次最大讀SectSize
                    FormerOpen.Flush();//清空快取
                    ToFileOpen.Write(buffer, 0, SectSize);//向目的文件寫入字節
                    ToFileOpen.Flush();//清空快取
                    ToFileOpen.Position = FormerOpen.Position;//使源文件和目的文件流的位置相同
                    copied += FileSize;//記錄已拷貝的大小
                    progressBar1.Value = progressBar1.Value + tem_n;//增加進度欄的進度塊
                }
                int left = (int)FormerOpen.Length - copied;//取得剩餘大小
                FileSize = FormerOpen.Read(buffer, 0, left);//讀取剩餘的字節
                FormerOpen.Flush();//清空快取
                ToFileOpen.Write(buffer, 0, left);//寫入剩餘的部分
                ToFileOpen.Flush();//清空快取
            }
            else//如果整體拷貝，即每次拷貝內容大於文件總長度
            {
                byte[] buffer = new byte[FormerOpen.Length];//取得文件的大小
                FormerOpen.Read(buffer, 0, (int)FormerOpen.Length);//讀取源文件的字節
                FormerOpen.Flush();//清空快取
                ToFileOpen.Write(buffer, 0, (int)FormerOpen.Length);//寫放字節
                ToFileOpen.Flush();//清空快取
            }
            FormerOpen.Close();//釋放所有資源
            ToFileOpen.Close();//釋放所有資源
            if (MessageBox.Show("複製完成") == DialogResult.OK)//顯示"複製完成"提示對話框
            {
                progressBar1.Value = 0;//設定進度欄的當有位置為0
                textBox1.Clear();//清空文字
                textBox2.Clear();
                str = "";
            }
        }
    }
}
