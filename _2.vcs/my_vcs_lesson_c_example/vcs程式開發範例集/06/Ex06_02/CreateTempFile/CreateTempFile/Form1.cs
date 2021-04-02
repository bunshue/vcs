using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.IO;
namespace CreateTempFile
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
           textBox1.Text = Path.GetTempFileName();
           FileInfo fin = new FileInfo(textBox1.Text);
           fin.AppendText();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Close();
        }
    }
}