using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.IO;

namespace UpdateFileAndDirectory
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            folderBrowserDialog1.ShowDialog();
            textBox1.Text = folderBrowserDialog1.SelectedPath;
            DirectoryInfo dir = new DirectoryInfo(textBox1.Text);
            FileInfo[] f =dir.GetFiles();
            for (int i = 0; i < f.Length; i++)
            {
                listBox1.Items.Add(f[i]);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Directory.Move(textBox1.Text,textBox2.Text);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            File.Move(textBox1.Text+"\\"+listBox1.SelectedItem.ToString(), textBox1.Text+"\\"+textBox2.Text);
        }
    }
}