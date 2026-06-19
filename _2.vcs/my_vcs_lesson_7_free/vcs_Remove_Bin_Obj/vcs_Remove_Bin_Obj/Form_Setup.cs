using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Remove_Bin_Obj
{
    public partial class Form_Setup : Form
    {
        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE
        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;

        public Form_Setup()
        {
            InitializeComponent();
        }

        private void Form_Setup_Load(object sender, EventArgs e)
        {
            lb_main_mesg.Text = "";

            lb_setup0.Text = "Git命令";
            tb_setup0.Text = Properties.Settings.Default.git_command;

            show_item_location();
        }

        void show_item_location()
        {
            int x_st = 20;
            int y_st = 50;
            int dx = 170;
            int dy = 55;

            lb_setup0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            lb_main_mesg.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            tb_setup0.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            int dxx = 80;
            bt_setup_save.Location = new Point(x_st + dx * 4 + dxx, y_st + dy * 7);

            bt_exit_setup();

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            //Application.Exit();
            this.Close();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_setup_save_Click(object sender, EventArgs e)
        {
            //儲存
            Properties.Settings.Default.git_command = tb_setup0.Text;
            Properties.Settings.Default.Save();

            show_main_message("儲存設定完成", S_OK, 30);
        }

        void show_main_message(string mesg, int number, int timeout)
        {
            lb_main_mesg.Text = mesg;
            //playSound(number);

            timer_display_show_main_mesg_count = 0;
            timer_display_show_main_mesg_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        private void timer_display_Tick(object sender, EventArgs e)
        {
            if (timer_display_show_main_mesg_count < timer_display_show_main_mesg_count_target)      //display main message timeout
            {
                timer_display_show_main_mesg_count++;
                if (timer_display_show_main_mesg_count >= timer_display_show_main_mesg_count_target)
                {
                    lb_main_mesg.Text = "";
                }
            }
        }

    }
}
