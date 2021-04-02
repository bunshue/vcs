using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;

namespace FileCopy
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.FileName = "";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
                textBox1.Text = openFileDialog1.FileName;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            folderBrowserDialog1.SelectedPath = "";
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
                textBox2.Text = folderBrowserDialog1.SelectedPath;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (textBox1.Text.Length == 0 || textBox2.Text.Length == 0)
                MessageBox.Show("請選擇原文件路徑或目的文件路徑。");
            else
            {
                string tem_Dfile = textBox1.Text;
                tem_Dfile = tem_Dfile.Substring(tem_Dfile.LastIndexOf("\\") + 1, tem_Dfile.Length - tem_Dfile.LastIndexOf("\\") - 1);
                tem_Dfile = textBox2.Text + "\\" + tem_Dfile;
                CopyFile(textBox1.Text, tem_Dfile, 1024);
            }
        }

        FileStream FormerOpen;
        FileStream ToFileOpen;
        /// <summary>
        /// 文件的複製
        /// </summary>
        /// <param FormerFile="string">源文件路徑</param>
        /// <param toFile="string">目的文件路徑</param> 
        /// <param SectSize="int">傳輸大小</param> 
        /// <param progressBar="ProgressBar">ProgressBar控制元件</param> 
        public void CopyFile(string FormerFile, string toFile, int SectSize)
        {
            FileStream fileToCreate = new FileStream(toFile, FileMode.Create);		//建立目的文件，如果已存在將被覆蓋
            fileToCreate.Close();										//關閉所有資源
            fileToCreate.Dispose();										//釋放所有資源
            FormerOpen = new FileStream(FormerFile, FileMode.Open, FileAccess.Read);//以只讀方式打開源文件
            ToFileOpen = new FileStream(toFile, FileMode.Append, FileAccess.Write);	//以寫方式打開目的文件
            //根據一次傳輸的大小，計算傳輸的個數
            int FileSize;												//要拷貝的文件的大小
            //如果分段拷貝，即每次拷貝內容小於文件總長度
            if (SectSize < FormerOpen.Length)
            {
                byte[] buffer = new byte[SectSize];							//根據傳輸的大小，定義一個字節數組
                int copied = 0;										//記錄傳輸的大小
                while (copied <= ((int)FormerOpen.Length - SectSize))			//拷貝主體部分
                {
                    FileSize = FormerOpen.Read(buffer, 0, SectSize);			//從0開始讀，每次最大讀SectSize
                    FormerOpen.Flush();								//清空快取
                    ToFileOpen.Write(buffer, 0, SectSize);					//向目的文件寫入字節
                    ToFileOpen.Flush();									//清空快取
                    ToFileOpen.Position = FormerOpen.Position;				//使源文件和目的文件流的位置相同
                    copied += FileSize;									//記錄已拷貝的大小
                }
                int left = (int)FormerOpen.Length - copied;						//取得剩餘大小
                FileSize = FormerOpen.Read(buffer, 0, left);					//讀取剩餘的字節
                FormerOpen.Flush();									//清空快取
                ToFileOpen.Write(buffer, 0, left);							//寫入剩餘的部分
                ToFileOpen.Flush();									//清空快取
            }
            //如果整體拷貝，即每次拷貝內容大於文件總長度
            else
            {
                byte[] buffer = new byte[FormerOpen.Length];				//取得文件的大小
                FormerOpen.Read(buffer, 0, (int)FormerOpen.Length);			//讀取源文件的字節
                FormerOpen.Flush();									//清空快取
                ToFileOpen.Write(buffer, 0, (int)FormerOpen.Length);			//寫放字節
                ToFileOpen.Flush();									//清空快取
            }
            FormerOpen.Close();										//釋放所有資源
            ToFileOpen.Close();										//釋放所有資源
            MessageBox.Show("文件複製完成");
        }
    }
}
