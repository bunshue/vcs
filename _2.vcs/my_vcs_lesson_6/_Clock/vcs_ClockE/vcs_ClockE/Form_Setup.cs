using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ClockE
{
    public partial class Form_Setup : Form
    {
        DateTime EventDate;
        Button btn1;
        Button btn2;
        Button btn3;
        NumericUpDown nud1;
        NumericUpDown nud2;
        NumericUpDown nud3;
        Label lb_time;
        Label lb1;
        Label lb2;
        Label lb3;



        public Form_Setup()
        {
            InitializeComponent();
        }

        private void Form_Setup_Load(object sender, EventArgs e)
        {
            int x_st = 0;
            int y_st = 0;
            int dx = 0;
            int W = 100;
            int H = 40;

            x_st = 120;
            y_st = 100;

            // 實例化按鈕
            lb_time = new Label();
            lb_time.AutoSize = true;
            lb_time.Font = new Font("Courier New", 20);
            lb_time.Text = "設定時間";
            lb_time.Location = new Point(x_st + dx * 0, y_st);
            this.pictureBox1.Controls.Add(lb_time); // 將此控件加入pictureBox中

            x_st = 205;
            y_st = 210;
            dx = 150;

            // 實例化按鈕
            lb1 = new Label();
            lb1.AutoSize = true;
            lb1.Font = new Font("Courier New", 18);
            lb1.Text = "時";
            lb1.Location = new Point(x_st + dx * 0, y_st);
            this.pictureBox1.Controls.Add(lb1); // 將此控件加入pictureBox中

            // 實例化按鈕
            lb2 = new Label();
            lb2.AutoSize = true;
            lb2.Font = new Font("Courier New", 18);
            lb2.Text = "分";
            lb2.Location = new Point(x_st + dx * 1, y_st);
            this.pictureBox1.Controls.Add(lb2); // 將此控件加入pictureBox中

            // 實例化按鈕
            lb3 = new Label();
            lb3.AutoSize = true;
            lb3.Font = new Font("Courier New", 18);
            lb3.Text = "秒";
            lb3.Location = new Point(x_st + dx * 2, y_st);
            this.pictureBox1.Controls.Add(lb3); // 將此控件加入pictureBox中

            x_st = 100;
            y_st = 200;
            dx = 150;
            W = 100;
            H = 40;
            // 實例化按鈕
            nud1 = new NumericUpDown();
            nud1.Name = "nud1";
            nud1.Width = W;
            nud1.Height = H;
            nud1.Font = new Font("Courier New", 30);
            nud1.TextAlign = HorizontalAlignment.Center;
            nud1.Maximum = 23;
            nud1.Minimum = 0;
            nud1.Value = 0;
            nud1.Location = new Point(x_st + dx * 0, y_st);
            // 加入按鈕事件
            //nud1.ValueChanged += new EventHandler(nud_ValueChanged);   //same
            nud1.ValueChanged += nud_ValueChanged;
            this.pictureBox1.Controls.Add(nud1);    // 將此控件加入pictureBox中

            nud2 = new NumericUpDown();
            nud2.Name = "nud2";
            nud2.Width = W;
            nud2.Height = H;
            nud2.Font = new Font("Courier New", 30);
            nud2.TextAlign = HorizontalAlignment.Center;
            nud2.Maximum = 59;
            nud2.Minimum = 0;
            nud2.Value = 10;
            nud2.Location = new Point(x_st + dx * 1, y_st);
            // 加入按鈕事件
            //nud2.ValueChanged += new EventHandler(nud_ValueChanged);   //same
            nud2.ValueChanged += nud_ValueChanged;
            this.pictureBox1.Controls.Add(nud2);    // 將此控件加入pictureBox中

            nud3 = new NumericUpDown();
            nud3.Name = "nud3";
            nud3.Width = W;
            nud3.Height = H;
            nud3.Font = new Font("Courier New", 30);
            nud3.TextAlign = HorizontalAlignment.Center;
            nud3.Maximum = 59;
            nud3.Minimum = 0;
            nud3.Value = 0;
            nud3.Location = new Point(x_st + dx * 2, y_st);
            // 加入按鈕事件
            //nud3.ValueChanged += new EventHandler(nud_ValueChanged);   //same
            nud3.ValueChanged += nud_ValueChanged;
            this.pictureBox1.Controls.Add(nud3);    // 將此控件加入pictureBox中

            x_st = 100;
            y_st = 300;
            dx = 150;
            W = 100;
            H = 60;

            // 實例化按鈕
            btn1 = new Button();
            btn1.Width = W;
            btn1.Height = H;
            btn1.Font = new Font("Courier New", 16);
            btn1.Text = "Start";
            btn1.Name = "bt_start";
            btn1.Location = new Point(x_st + dx * 0, y_st);
            // 加入按鈕事件
            //btn1.Click += new EventHandler(myClick);   //same
            btn1.Click += button_Click;
            this.pictureBox1.Controls.Add(btn1);    // 將此控件加入pictureBox中

            // 實例化按鈕
            btn2 = new Button();
            btn2.Width = W;
            btn2.Height = H;
            btn2.Font = new Font("Courier New", 16);
            btn2.Text = "Reset";
            btn2.Name = "bt_reset";
            btn2.Location = new Point(x_st + dx * 1, y_st);
            // 加入按鈕事件
            //btn2.Click += new EventHandler(button_Click);   //same
            btn2.Click += button_Click;
            this.pictureBox1.Controls.Add(btn2);    // 將此控件加入pictureBox中

            // 實例化按鈕
            btn3 = new Button();
            btn3.Width = W;
            btn3.Height = H;
            btn3.Font = new Font("Courier New", 16);
            btn3.Text = "Exit";
            btn3.Name = "bt_exit";
            btn3.Location = new Point(x_st + dx * 2, y_st);
            // 加入按鈕事件
            //btn3.Click += new EventHandler(button_Click);   //same
            btn3.Click += button_Click;
            this.pictureBox1.Controls.Add(btn3);    // 將此控件加入pictureBox中

            lb_time.Text = "設定時間 : " + nud1.Value.ToString() + "時 " + nud3.Value.ToString() + "分 " + nud3.Value.ToString() + "秒" + "\n";
        }

        private void nud_ValueChanged(object sender, EventArgs e)
        {
            if (((NumericUpDown)sender).Name == "nud1")
            {
                //richTextBox1.Text += "你按了nud1 value = " + ((NumericUpDown)sender).Value.ToString() + "\n";
            }
            else if (((NumericUpDown)sender).Name == "nud2")
            {
                //richTextBox1.Text += "你按了nud2 value = " + ((NumericUpDown)sender).Value.ToString() + "\n";
            }
            else if (((NumericUpDown)sender).Name == "nud3")
            {
                //richTextBox1.Text += "你按了nud3 value = " + ((NumericUpDown)sender).Value.ToString() + "\n";
            }

            int hh = (int)nud1.Value;
            int mm = (int)nud2.Value;
            int ss = (int)nud3.Value;

            lb_time.Text = "設定時間 : " + hh.ToString() + "時 " + mm.ToString() + "分 " + ss.ToString() + "秒" + "\n";
        }

        private void button_Click(object sender, EventArgs e)
        {
            if (((Button)sender).Name == "bt_start")
            {
                this.pictureBox1.Controls.Remove(btn1);
                this.pictureBox1.Controls.Remove(btn2);
                this.pictureBox1.Controls.Remove(btn3);
                this.pictureBox1.Controls.Remove(nud1);
                this.pictureBox1.Controls.Remove(nud2);
                this.pictureBox1.Controls.Remove(nud3);
                this.pictureBox1.Controls.Remove(lb_time);
                this.pictureBox1.Controls.Remove(lb1);
                this.pictureBox1.Controls.Remove(lb2);
                this.pictureBox1.Controls.Remove(lb3);


                int hh = (int)nud1.Value;
                int mm = (int)nud2.Value;
                int ss = (int)nud3.Value;

                //richTextBox1.Text += "設定時間 : " + hh.ToString() + "時 " + mm.ToString() + "分 " + ss.ToString() + "秒" + "\n";

                //一段時間以後的寫法
                EventDate = DateTime.Now + new TimeSpan(0, hh, mm, ss);    //現在時間 + 0天hh時mm分ss秒

                //最大化螢幕
                this.FormBorderStyle = FormBorderStyle.None;
                this.WindowState = FormWindowState.Maximized;
                pictureBox1.Location = new Point(0, 0);
                pictureBox1.Size = new Size(1920, 1080);
                //flag_countdown_start = true;
                //richTextBox1.Visible = false;
                //timer1.Enabled = true;
            }
            else if (((Button)sender).Name == "bt_reset")
            {
                nud1.Value = 0;
                nud2.Value = 10;
                nud3.Value = 0;
            }
            else if (((Button)sender).Name == "bt_exit")
            {
                Application.Exit();
            }
            else
            {
                //richTextBox1.Text += "你按了按鈕 Name : " + ((Button)sender).Name + "\n";
            }
        }
    }
}
