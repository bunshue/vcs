using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace ExistFile
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (System.IO.File.Exists(textBox1.Text) == false)
            {
                MessageBox.Show("文件不存在");
            }
            else
            {
                MessageBox.Show("文件存在");
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }
    }
}