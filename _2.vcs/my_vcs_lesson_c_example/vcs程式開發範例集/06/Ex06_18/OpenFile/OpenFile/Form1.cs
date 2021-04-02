using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.IO;

namespace OpenFile
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            openFileDialog1.ShowDialog();
            StreamReader sr = new StreamReader(openFileDialog1.FileName);
            richTextBox1.Text = sr.ReadToEnd();
            sr.Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Close();
        }
    }
}