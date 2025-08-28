using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
方案總管 / 右鍵 / 加入 / 新增項目 選 類別

把 Class1.cs 改成 Color2Gray.cs
*/

namespace vcs_Class2
{
    public partial class Form1 : Form
    {
        string filename2 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

        Color2Gray c2g; // 宣告一個物件

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            c2g = new Color2Gray(new Bitmap(filename2));
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //c2g.do_Color2Gray();

            pictureBox1.Image = c2g.bitmap1;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            c2g.do_Color2Gray();

            pictureBox1.Image = c2g.bitmap2;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            c2g.Draw();

            pictureBox1.Image = c2g.bitmap2;
        }
    }
}


