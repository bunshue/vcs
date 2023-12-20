using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_SendTo_All
{
    public partial class Form_Setup : Form
    {
        public Form_Setup()
        {
            InitializeComponent();
        }

        private void Form_Setup_Load(object sender, EventArgs e)
        {
            show_item_location();

            bool flag_show_big_files_only = Properties.Settings.Default.show_big_files_only;

            if (flag_show_big_files_only == true)
            {
                richTextBox1.Text += "僅顯示大檔, ";
                cb_search_big_files.Checked = true;
            }
            else
            {
                richTextBox1.Text += "顯示所有檔案\n";
                cb_search_big_files.Checked = false;
            }

            long file_size_limit = 0;   //檔案界限
            file_size_limit = Properties.Settings.Default.file_size_limit * 1024 * 1024;
            richTextBox1.Text += "檔案界限 : " + file_size_limit.ToString() + "\n";
            tb_filesize_mb.Text = Properties.Settings.Default.file_size_limit.ToString();

            lb_main_mesg1.Text = "";
            lb_main_mesg2.Text = "";
        }

        void show_item_location()
        {
            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            //this.FormBorderStyle = FormBorderStyle.FixedSingle;
            //this.WindowState = FormWindowState.Maximized;  // 設定表單最大化

            int x_st;
            int y_st;
            int dx;
            int dy;

            x_st = 20;
            y_st = 50;
            dx = 110;
            dy = 55;

            cb_search_big_files.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            tb_filesize_mb.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            lb_filesize.Location = new Point(x_st + dx * 1, y_st + dy * 1);

            bt_save.Location = new Point(x_st + dx * 1, y_st + dy * 3);

            lb_main_mesg1.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            lb_main_mesg2.Location = new Point(x_st + dx * 0, y_st + dy * 6);

            bt_exit_setup();
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            this.Close();
            //Application.Exit();
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

        private void bt_save_Click(object sender, EventArgs e)
        {
            Properties.Settings.Default.show_big_files_only = cb_search_big_files.Checked;

            int file_size_limit = 0;
            bool conversionSuccessful = int.TryParse(tb_filesize_mb.Text, out file_size_limit);    //out為必須
            if (conversionSuccessful == true)
            {
                richTextBox1.Text += "得到int數字： " + file_size_limit + "\n";
                Properties.Settings.Default.file_size_limit = file_size_limit;
            }
            else
            {
                richTextBox1.Text += "int.TryParse 失敗\n";
            }

            //richTextBox1.Text += "檔案界限 : " + file_size_limit.ToString() + "\n";

            Properties.Settings.Default.Save();
        }
    }
}
