using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void openMenuItem_Click(object sender, EventArgs e)
        {
            if(openDialog.ShowDialog() == DialogResult.OK){
                System.IO.StreamReader sr = new System.IO.StreamReader(openDialog.FileName, Encoding.Default);
                richTextBox.Text = sr.ReadToEnd();
                sr.Close();
            }
        }

        private void saveMenuItem_Click(object sender, EventArgs e)
        {
            if (saveDialog.ShowDialog() == DialogResult.OK)
            {
                System.IO.StreamWriter sw = new System.IO.StreamWriter(saveDialog.FileName);
                sw.Write(richTextBox.Text);
                sw.Flush();
                sw.Close();
            }
        }

        private void closeMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
