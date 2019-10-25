﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Microsoft.VisualBasic.FileIO;

//先將Microsoft.VisualBasic.Dll加入參考。
//參考/加入參考/.NET/Microsoft.VisualBasic

//引用Microsoft.VisualBasic.FileIO命名空間。


namespace test_use_recycle_bin
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                FileSystem.DeleteFile(openFileDialog1.FileName,
        UIOption.OnlyErrorDialogs,
        RecycleOption.SendToRecycleBin);


            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            int i;
            for (i = 0x64C2; i < 0x64C2 + 10; i++)
            {
                richTextBox1.Text += "unicode value = 0x" + i.ToString("X4") + ", code = " + ((char)i).ToString() + "\n";
            }

        }

        private void button3_Click(object sender, EventArgs e)
        {
        }



    }
}
