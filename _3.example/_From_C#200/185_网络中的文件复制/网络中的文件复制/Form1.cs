using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Microsoft.VisualBasic.FileIO;
namespace 网络中的文件复制
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        //引用API
      
        private void Form1_Load(object sender, EventArgs e)
        {
            
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (this.openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                this.textBox1.Text = this.openFileDialog1.FileName;
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (this.folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                this.textBox2.Text = this.folderBrowserDialog1.SelectedPath + this.textBox1.Text.Substring(this.textBox1.Text.LastIndexOf("\\"));
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                FileSystem.CopyFile(this.textBox1.Text, this.textBox2.Text);
                MessageBox.Show("传输成功！！！");
            }
            catch(Exception ey)
            {
                MessageBox.Show(ey.Message);
            }
         
        }
    }
}