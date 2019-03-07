using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MyClock
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int flag_count_down_mode = 0;
        int total_count_down_sec = 0;

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (flag_count_down_mode == 0)
            {
                digitalDisplayControl1.DigitText = DateTime.Now.ToString("HH:mm:ss");
            }
            else if (flag_count_down_mode == 1)
            { 
            
            
            }

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            digitalDisplayControl1.DigitText = DateTime.Now.ToString("HH:mm:ss");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int hh = (int)numericUpDown1.Value;
            int mm = (int)numericUpDown2.Value;
            int ss = (int)numericUpDown3.Value;
            total_count_down_sec = hh * 60 * 60 + mm * 60 + ss;
            richTextBox1.Text += "total_sec = " + total_count_down_sec.ToString() + "\n";

            //flag_count_down_mode = 1;
        }
    }
}
