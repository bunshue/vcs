using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for File, FileStream

namespace test1101b
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //錯誤的寫法, 可能會出現"記憶體不足"
            //pictureBox1.Image = Image.FromFile(@"c:\______test_files\bear.bmp");

             //正確的寫法
            FileStream fs = File.OpenRead(@"c:\______test_files\bear.bmp");
            pictureBox1.Image = Image.FromStream(fs);
            fs.Close();

        }
    }
}
