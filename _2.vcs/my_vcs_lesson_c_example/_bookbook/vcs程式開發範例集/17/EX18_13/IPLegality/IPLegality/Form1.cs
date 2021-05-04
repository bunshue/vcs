using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace IPLegality
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string[] lines = new string[4];
            string s =".";
            lines = textBox1.Text.Split(s.ToCharArray(), 4);
            label2.Text = "合法 ";
            for (int i = 0; i < 4;i++ )
            {
                if (Convert.ToInt32(lines[i]) >= 255)
                {
                    label2.Text = "不合法 ";
                }
            }
        }
    }
}