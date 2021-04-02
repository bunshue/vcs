using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.IO;

namespace GetDirectoryFile
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            folderBrowserDialog1.ShowDialog();
            textBox1.Text = folderBrowserDialog1.SelectedPath;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string[] files = Directory.GetFiles(textBox1.Text);
            for (int i = 0; i < files.Length; i++)
            {
                textBox2.Lines = files;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Close();
        }
    }
}