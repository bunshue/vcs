using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Globalization;

using System.IO;

//加入參考Microsoft.VisualBasic.dll

using Microsoft.VisualBasic.FileIO;

//using System.Net;   //for WebClient

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {
            int c = 0; // 定義此變量主要是來判斷目錄中是否有文件
            foreach (string s1 in Directory.GetFiles("c:\\______test_files.old")) // 返回文件名稱字符串行時的枚舉類型
            {
                ++c;
                richTextBox1.Text += "find file " + s1 + "\n";
            }

            /*
            if (c > 0) //判斷是否存在文件如果 c > 0則回收站有文件，反之則沒有
            {
                DialogResult r = MessageBox.Show("是否確定？", "垃圾處理！",
                        MessageBoxButtons.YesNo, MessageBoxIcon.Question);
                // 顯示"確定"和"取消"二個按鈕，圖標顯示是一個問號。
                int ss = (int)r;
                if (ss == 6) // 按動確定按鈕
                {
                    foreach (string s in Directory.GetFiles("c:\recycled"))
                    // 把全路徑名稱房子 s中
                    {
                        //File.Delete(s); //刪除此文件
                    }
                }
            }
            */

        }

        private void button1_Click(object sender, EventArgs e)
        {

            //在本文中是通过foreach 来列举出在"C:\Recycled"存在的所有被删除的文件信息的。

            int c = 0; // 定义此变量主要是来判断目录中是否有文件
            foreach (string s1 in Directory.GetFiles("c:\\recycled")) // 返回文件名称字符串行时的枚举类型
            {
                ++c;
            }
            if (c > 0) //判断是否存在文件如果 c > 0则回收站有文件，反之则没有
            {
                richTextBox1.Text += "c = " + c.ToString() + "\n";
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //使用資源回收筒刪除檔案
            FileSystem.DeleteFile("C:\\______test_files\\blog.png", UIOption.OnlyErrorDialogs, RecycleOption.SendToRecycleBin);
            richTextBox1.Text += "已將檔案移至資源回收筒\n";
        }


        
        private void button3_Click(object sender, EventArgs e)
        {
            //不使用資源回收筒刪除檔案
            //DirectoryInfo.Delete()相當於Windows Command Del(快捷鍵Shift + Del)是不會保存在資源回收筒
            //DirectoryInfo.Delete("C:\\______test_files\\blog.png");
        }







    }


    

}
