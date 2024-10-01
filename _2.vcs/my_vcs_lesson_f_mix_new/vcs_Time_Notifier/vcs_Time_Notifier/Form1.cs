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
        private const int BORDER = 20;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            DateTime dt = DateTime.Now;

            digitalDisplayControl1.DigitText = dt.ToString("HH:mm:ss");

            numericUpDown1.Value = dt.Year;
            numericUpDown2.Value = dt.Month;
            numericUpDown3.Value = dt.Day;

            textBox1.Text = dt.ToString("HHmm");
        }

        void show_item_location()
        {
            int W = 1920;
            int H = 1080;
            int w = 640;
            int h = 480;
            int x_st;
            int y_st;
            int dx;
            int dy;

            x_st = BORDER;
            y_st = BORDER;
            digitalDisplayControl1.Location = new Point(x_st, y_st);

            groupBox1.Size = new Size(500, 140);
            groupBox1.Location = new Point(x_st, y_st + 100);

            groupBox2.Size = new Size(500, 250);
            groupBox2.Location = new Point(x_st, y_st + 100 + 140);

            //button
            x_st = BORDER;
            y_st = BORDER;
            dx = 110;
            dy = 60;
            numericUpDown1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            numericUpDown2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            numericUpDown3.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            textBox1.Location = new Point(x_st + dx * 3 + 10, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 3 + 10, y_st + dy * 1);

            dx = 90;
            rb0.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            rb1.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            rb2.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            rb3.Location = new Point(x_st + dx * 3 + 10, y_st + dy * 1);

            richTextBox1.Location = new Point(BORDER + 500 + BORDER, BORDER);
            richTextBox1.Size = new Size(300, 500);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            W = BORDER + 500 + BORDER + 300 + BORDER;
            H = BORDER + 500 + BORDER;
            this.ClientSize = new Size(W, H);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
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
            //int hh = int.Parse(dt[0].ToString() + dt[1].ToString());
            //int mm = int.Parse(dt[2].ToString() + dt[3].ToString());

            int hh = int.Parse(dt.Substring(0, 2));
            int mm = int.Parse(dt.Substring(2, 2));

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


            //richTextBox1.Text += DateTime.Now.ToString("ss") + " ";




            //lb_time1.Text = "PC時間 : " + DateTime.Now.ToString("yyyy" + '/' + "MM" + '/' + "dd ") + weekday + DateTime.Now.ToString(" HH" + ':' + "mm" + ':' + "ss");



        }

    }
}
