using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;  //  for BinaryWriter BinaryReader

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
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
            BinaryWriter outFile = new BinaryWriter(File.Open("myFile.dat", FileMode.Create)); // 開啟檔案

            outFile.Write(a_string); // 寫入 字串
            outFile.Write(a_float);  // 寫入 四位元組浮點數
            outFile.Write(an_int);   // 寫入 整數
            outFile.Write(a_bool);   // 寫入 一位元組的 Boolean 值

            outFile.Close(); // 關閉檔案
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (!File.Exists("myFile.dat")) return; // 先確定檔案存在
            BinaryReader inFile = new BinaryReader(File.Open("myFile.dat", FileMode.Open)); // 開啟檔案

            string my_string;
            float my_float;
            int my_int;
            bool my_bool;

            textBox1.Text = ""; // 文字方塊 先清空
            while (inFile.PeekChar() != -1) // 傳回下一個可供使用的字元，但不消耗它
            {
                my_string = inFile.ReadString(); // 讀出 字串
                my_float = inFile.ReadSingle();  // 讀出 四位元組浮點數
                my_int = inFile.ReadInt32();     // 讀出 整數
                my_bool = inFile.ReadBoolean();  // 讀出 一位元組的 Boolean 值

                textBox1.Text = textBox1.Text + my_string + Environment.NewLine;
                textBox1.Text = textBox1.Text + my_float.ToString() + Environment.NewLine;
                textBox1.Text = textBox1.Text + my_int.ToString() + Environment.NewLine;
                textBox1.Text = textBox1.Text + my_bool.ToString() + Environment.NewLine;
            }

            inFile.Close(); // 關閉檔案
        }
    }
}