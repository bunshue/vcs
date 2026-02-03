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
        Button bt_clear = new Button();

        public Form_Setup()
        {
            InitializeComponent();
        }

        private void Form_Setup_Load(object sender, EventArgs e)
        {
            show_item_location();

            bool flag_show_big_files_only = Properties.Settings.Default.show_big_files_only;
            bool flag_show_video_files_only = Properties.Settings.Default.show_video_files_only;
            bool flag_show_audio_files_only = Properties.Settings.Default.show_audio_files_only;
            bool flag_show_file_path = Properties.Settings.Default.show_file_path;

            if (flag_show_big_files_only == true)
            {
                richTextBox1.Text += "僅顯示大檔, ";
                rb_search_big_files.Checked = true;
            }
            else
            {
                richTextBox1.Text += "顯示所有檔案\n";
                rb_search_big_files.Checked = false;
            }

            long file_size_limit = 0;   //檔案界限
            file_size_limit = Properties.Settings.Default.file_size_limit * 1024 * 1024;
            richTextBox1.Text += "檔案界限 : " + file_size_limit.ToString() + "\n";
            tb_filesize_mb.Text = Properties.Settings.Default.file_size_limit.ToString();

            if (flag_show_video_files_only == true)
            {
                richTextBox1.Text += "只搜尋影片檔\n";
                cb_search_video_files.Checked = true;
            }
            else
            {
                cb_search_video_files.Checked = false;
            }

            if (flag_show_audio_files_only == true)
            {
                richTextBox1.Text += "只搜尋音樂檔\n";
                cb_search_audio_files.Checked = true;
            }
            else
            {
                cb_search_audio_files.Checked = false;
            }

            if (flag_show_file_path == true)
            {
                richTextBox1.Text += "顯示檔名\n";
                cb_show_file_path.Checked = true;
            }
            else
            {
                richTextBox1.Text += "不顯示檔名\n";
                cb_show_file_path.Checked = false;
            }

            lb_main_mesg1.Text = "AAAA";
            lb_main_mesg2.Text = "BBBB";
            tb_filesize_mb.Focus();
        }

        void show_item_location()
        {
            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            //this.FormBorderStyle = FormBorderStyle.FixedSingle;
            //this.WindowState = FormWindowState.Maximized;  // 設定表單最大化

            this.Size = new Size(600, 520);

            int x_st;
            int y_st;
            int dx;
            int dy;
            int W = 300;
            int H = 45;

            x_st = 15;
            y_st = 15;
            dx = 110;
            dy = 35;

            groupBox_search.Size = new Size(W, H * 2);
            groupBox_search_type.Size = new Size(W, H * 2);
            groupBox_file.Size = new Size(W, H);
            groupBox_video.Size = new Size(W, H);
            groupBox_text_mode.Size = new Size(W, H);
            groupBox_auto_save.Size = new Size(W, H);
            groupBox_show_file_content.Size = new Size(W, H);
            groupBox_file.Enabled = false;
            groupBox_video.Enabled = false;
            groupBox_text_mode.Enabled = false;
            groupBox_auto_save.Enabled = false;
            //groupBox_show_file_content.Enabled = false;

            groupBox_search.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox_search_type.Location = new Point(x_st + dx * 0, y_st + dy * 0 + H * 2);
            groupBox_file.Location = new Point(x_st + dx * 0, y_st + dy * 0 + H * 4);
            groupBox_video.Location = new Point(x_st + dx * 0, y_st + dy * 0 + H * 5);
            groupBox_text_mode.Location = new Point(x_st + dx * 0, y_st + dy * 0 + H * 6);
            groupBox_auto_save.Location = new Point(x_st + dx * 0, y_st + dy * 0 + H * 7);
            groupBox_show_file_content.Location = new Point(x_st + dx * 0, y_st + dy * 0 + H * 8);

            // groupBox_search
            rb_search_big_files.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            tb_filesize_mb.Location = new Point(x_st + dx * 1 + 40, y_st + dy * 0);
            rb_search_all_files.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            // groupBox_search_type
            cb_search_video_files.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            cb_search_audio_files.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            // groupBox_text_mode
            rb_text_mode_ascii.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            rb_text_mode_binary.Location = new Point(x_st + dx * 0 + 120, y_st + dy * 0);

            // groupBox_auto_save
            rb_auto_save_on.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            rb_auto_save_off.Location = new Point(x_st + dx * 0 + 120, y_st + dy * 0);

            // groupBox_show_file_content
            cb_show_file_path.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            bt_save.Location = new Point(x_st + dx * 0 + 210, y_st + dy * 12 + 40);

            lb_main_mesg1.Location = new Point(x_st + dx * 0, y_st + dy * 12);
            lb_main_mesg2.Location = new Point(x_st + dx * 0, y_st + dy * 13);

            richTextBox1.Size = new Size(270, 461);
            richTextBox1.Dock = DockStyle.Right;

            bt_exit_setup();

            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H
            bt_clear.Width = w;
            bt_clear.Height = h;
            bt_clear.Text = "";
            bt_clear.Name = "bt_clear";
            bt_clear.BackgroundImage = vcs_SendTo_All.Properties.Resources.clear;
            bt_clear.BackgroundImageLayout = ImageLayout.Zoom;
            bt_clear.Location = new Point(this.ClientSize.Width - w - 5, this.ClientSize.Height - h - 5);
            // 加入按鈕事件
            //bt_clear.Click += new EventHandler(bt_clear_Click);   //same
            bt_clear.Click += bt_clear_Click;
            this.Controls.Add(bt_clear);
            bt_clear.BringToFront();
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

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            Properties.Settings.Default.show_big_files_only = rb_search_big_files.Checked;
            Properties.Settings.Default.show_video_files_only = cb_search_video_files.Checked;
            Properties.Settings.Default.show_audio_files_only = cb_search_audio_files.Checked;
            Properties.Settings.Default.show_file_path = cb_show_file_path.Checked;

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
            this.Close();
        }

        private void tb_filesize_mb_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (Char)13)
            {
                bt_save_Click(sender, e);
            }
        }
    }
}
