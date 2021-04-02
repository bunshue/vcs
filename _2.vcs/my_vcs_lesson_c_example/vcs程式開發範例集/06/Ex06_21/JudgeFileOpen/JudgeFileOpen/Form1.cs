using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace JudgeFileOpen
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            checkBox1.Checked = false;
            checkBox2.Checked = true;
            openFileDialog1.ShowDialog();
            try
            {
                System.IO.File.Move(openFileDialog1.FileName, openFileDialog1.FileName);
            }
            catch(Exception ee)
            {
                    checkBox2.Checked = false;
                    checkBox1.Checked = true;
            }
        }
    }
}