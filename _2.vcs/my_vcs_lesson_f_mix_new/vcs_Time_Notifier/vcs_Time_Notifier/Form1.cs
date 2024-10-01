using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Time_Notifier
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            DateTime dt = DateTime.Now;

            digitalDisplayControl1.DigitText = dt.ToString("HH:mm:ss");

            int yy = dt.Year;

            richTextBox1.Text += yy + "\n";

            numericUpDown1.Value = dt.Year;
            numericUpDown2.Value = dt.Month;
            numericUpDown3.Value = dt.Day;

            textBox1.Text = dt.ToString("HHmm");

            //lb_time1.Text = "PC時間 : " + DateTime.Now.ToString("yyyy" + '/' + "MM" + '/' + "dd ") + weekday + DateTime.Now.ToString(" HH" + ':' + "mm" + ':' + "ss");

        }

        void show_item_location()
        {

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            richTextBox1.Text += DateTime.Now.ToString("ss") + " ";

            DateTime dt_now = DateTime.Now;
            toolStripStatusLabel1.Text = dt_now.ToString();

            digitalDisplayControl1.DigitText = DateTime.Now.ToString("HH:mm:ss");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string dt = textBox1.Text;
            int len = dt.Length;
            if (len != 4)
            {
                richTextBox1.Text += "時間錯誤\n";
                textBox1.Clear();
                return;
            }
            int i;
            for (i = 0; i < 4; i++)
            {
                if (((int)dt[i] < '0') || ((int)dt[i] > '9'))
                {
                    richTextBox1.Text += "時間錯誤\n";
                    textBox1.Clear();
                    return;

                }
            }
            int hh = int.Parse(dt[0].ToString() + dt[1].ToString());
            int mm = int.Parse(dt[2].ToString() + dt[3].ToString());

            if ((hh < 0) || hh > 23)
            {
                richTextBox1.Text += "時間錯誤\n";
                textBox1.Clear();
                return;
            }

            if ((mm < 0) || mm > 59)
            {
                richTextBox1.Text += "時間錯誤\n";
                textBox1.Clear();
                return;
            }

            richTextBox1.Text += "時間正確\t" + hh.ToString() + " 時 " + mm.ToString() + " 分" + "\n";




        }
    }
}
