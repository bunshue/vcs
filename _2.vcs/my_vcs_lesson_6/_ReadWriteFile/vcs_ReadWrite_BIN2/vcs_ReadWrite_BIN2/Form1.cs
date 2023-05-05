using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;  //  for BinaryWriter BinaryReader

namespace vcs_ReadWrite_BIN2
{
    public partial class Form1 : Form
    {
        string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_bin\txt_rw.bin";

        string a_string = "Wonderful";  // 字串
        float a_float = 3.1415926f;     // 四位元組浮點數
        int an_int = 99;                // 整數
        bool a_bool = true;             // 一位元組的 Boolean 值

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            BinaryWriter bw = new BinaryWriter(File.Open(filename, FileMode.Create)); // 開啟檔案

            bw.Write(a_string); // 寫入 字串
            bw.Write(a_float);  // 寫入 四位元組浮點數
            bw.Write(an_int);   // 寫入 整數
            bw.Write(a_bool);   // 寫入 一位元組的 Boolean 值

            bw.Close(); // 關閉檔案
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (!File.Exists(filename))
            {
                richTextBox1.Text += "檔案 : " + filename + " 不存在\n";
                return; // 先確定檔案存在
            }
            richTextBox1.Clear();
            BinaryReader br = new BinaryReader(File.Open(filename, FileMode.Open)); // 開啟檔案

            string my_string;
            float my_float;
            int my_int;
            bool my_bool;

            textBox1.Text = ""; // 文字方塊 先清空
            while (br.PeekChar() != -1) // 傳回下一個可供使用的字元，但不消耗它
            {
                my_string = br.ReadString(); // 讀出 字串
                my_float = br.ReadSingle();  // 讀出 四位元組浮點數
                my_int = br.ReadInt32();     // 讀出 整數
                my_bool = br.ReadBoolean();  // 讀出 一位元組的 Boolean 值

                textBox1.Text = textBox1.Text + my_string + Environment.NewLine;
                textBox1.Text = textBox1.Text + my_float.ToString() + Environment.NewLine;
                textBox1.Text = textBox1.Text + my_int.ToString() + Environment.NewLine;
                textBox1.Text = textBox1.Text + my_bool.ToString() + Environment.NewLine;
                richTextBox1.Text += my_string + "\n";
                richTextBox1.Text += my_float + "\n";
                richTextBox1.Text += my_int + "\n";
                richTextBox1.Text += my_bool + "\n";
            }

            br.Close(); // 關閉檔案
        }
    }
}
