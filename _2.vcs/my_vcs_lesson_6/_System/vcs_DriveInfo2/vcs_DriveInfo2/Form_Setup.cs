using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_DriveInfo2
{
    public partial class Form_Setup : Form
    {
        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE
        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;

        int hdd_space_threshold1 = 80; //一級警戒
        int hdd_space_threshold2 = 90; //二級警戒, 二級較嚴重
        string upload_source_directory = string.Empty;
        string upload_destination_directory = string.Empty;
        int upload_interval = 10;
        bool flag_upload_enabled = false;

        public Form_Setup()
        {
            InitializeComponent();
        }

        private void Form_Setup_Load(object sender, EventArgs e)
        {
            lb_main_mesg.Text = "";
            lb_setup0.Text = "一級低容量警戒(%)";
            lb_setup1.Text = "二級低容量警戒(%)\n二級較嚴重";
            lb_setup2.Text = "上拋檔案來源地";
            lb_setup3.Text = "上拋檔案目的地";
            lb_setup4.Text = "上拋時間間隔(分鐘)";
            cb_setup5.Text = "開啟上拋功能";

            tb_setup0.Text = Properties.Settings.Default.hdd_space_threshold1.ToString();
            tb_setup1.Text = Properties.Settings.Default.hdd_space_threshold2.ToString();
            tb_setup2.Text = Properties.Settings.Default.upload_source_directory;
            tb_setup3.Text = Properties.Settings.Default.upload_destination_directory;
            tb_setup4.Text = Properties.Settings.Default.upload_interval.ToString();
            cb_setup5.Checked = Properties.Settings.Default.upload_enabled;

            show_item_location();
            update_default_setting();
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
            dx = 200;
            dy = 55;

            lb_setup0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            lb_setup1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            lb_setup2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            lb_setup3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            lb_setup4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            cb_setup5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            lb_main_mesg.Location = new Point(x_st + dx * 0, y_st + dy * 6 - 25);

            tb_setup0.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            tb_setup1.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            tb_setup2.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            tb_setup3.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            tb_setup4.Location = new Point(x_st + dx * 1, y_st + dy * 4);

            //bt_setup0.Location = new Point(x_st + dx * 4-80, y_st + dy * 0);
            //bt_setup1.Location = new Point(x_st + dx * 4 - 80, y_st + dy * 1);
            bt_setup2.Location = new Point(x_st + dx * 4 - 240, y_st + dy * 2 - 10);
            bt_setup3.Location = new Point(x_st + dx * 4 - 240, y_st + dy * 3 - 10);
            //bt_setup4.Location = new Point(x_st + dx * 4 - 80, y_st + dy * 4);
            bt_setup5.Location = new Point(x_st + dx * 4 - 280, y_st + dy * 6);
            bt_setup6.Location = new Point(x_st + dx * 4 - 280 - 120, y_st + dy * 6);

            bt_setup2.BackgroundImageLayout = ImageLayout.Zoom;
            bt_setup2.BackgroundImage = Properties.Resources.open_folder;
            bt_setup3.BackgroundImageLayout = ImageLayout.Zoom;
            bt_setup3.BackgroundImage = Properties.Resources.open_folder;

            bt_exit_setup();
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
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

        void update_default_setting()
        {
            hdd_space_threshold1 = Properties.Settings.Default.hdd_space_threshold1;
            hdd_space_threshold2 = Properties.Settings.Default.hdd_space_threshold2;
            upload_interval = Properties.Settings.Default.upload_interval;
            flag_upload_enabled = Properties.Settings.Default.upload_enabled;
            upload_source_directory = Properties.Settings.Default.upload_source_directory;
            upload_destination_directory = Properties.Settings.Default.upload_destination_directory;

            /*
            richTextBox1.Text += "取得 一級警戒 : " + hdd_space_threshold1.ToString() + "\n";
            richTextBox1.Text += "取得 二級警戒 : " + hdd_space_threshold2.ToString() + "\n";
            richTextBox1.Text += "取得 上拋間隔 : " + upload_interval.ToString() + "\n";
            richTextBox1.Text += "取得 上拋功能 : " + flag_upload_enabled.ToString() + "\n";
            richTextBox1.Text += "取得 上拋來源資料夾 : " + upload_source_directory + "\n";
            richTextBox1.Text += "取得 上拋目的資料夾 : " + upload_destination_directory + "\n";
            */

        }

        private void bt_setup2_Click(object sender, EventArgs e)
        {
            folderBrowserDialog1.SelectedPath = "C:\\"; //預設開啟的路徑
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                tb_setup2.Text = folderBrowserDialog1.SelectedPath;
            }
            else
            {
                //richTextBox2.Text = "未選取資料夾\n";
            }
        }

        private void bt_setup3_Click(object sender, EventArgs e)
        {
            folderBrowserDialog1.SelectedPath = "C:\\"; //預設開啟的路徑
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                tb_setup3.Text = folderBrowserDialog1.SelectedPath;
            }
            else
            {
                //richTextBox2.Text = "未選取資料夾\n";
            }

        }

        private void bt_setup5_Click(object sender, EventArgs e)
        {
            show_main_message("取消 並 離開", S_OK, 30);
        }

        private void bt_setup6_Click(object sender, EventArgs e)
        {
            //檢查數字合不合理

            int hdd_space_threshold1 = int.Parse(tb_setup0.Text); //一級警戒
            int hdd_space_threshold2 = int.Parse(tb_setup1.Text); //二級警戒, 二級較嚴重
            string upload_source_directory = tb_setup2.Text;
            string upload_destination_directory = tb_setup3.Text;
            int upload_interval = int.Parse(tb_setup4.Text);
            bool flag_upload_enabled = cb_setup5.Checked;

            string mesg = hdd_space_threshold1.ToString() + " " + hdd_space_threshold2.ToString() + " " +
                upload_source_directory + " " + upload_destination_directory + " " + upload_interval.ToString() + " " + flag_upload_enabled.ToString();

            show_main_message(mesg, S_OK, 30);

            bool flag_parameter_reasonable = true;
            if ((hdd_space_threshold1 < 0) || (hdd_space_threshold1 > 100))
            {
                mesg = "一級警戒 範圍應為 0 ~ 100";
                flag_parameter_reasonable = false;
            }
            if (flag_parameter_reasonable == false)
            {
                show_main_message(mesg, S_OK, 30);
                return;
            }

            if ((hdd_space_threshold2 < 0) || (hdd_space_threshold2 > 100))
            {
                mesg = "二級警戒 範圍應為 0 ~ 100";
                flag_parameter_reasonable = false;
            }
            if (flag_parameter_reasonable == false)
            {
                show_main_message(mesg, S_OK, 30);
                return;
            }

            if (hdd_space_threshold1 >= hdd_space_threshold2)
            {
                mesg = "二級警戒 應該比較嚴重, 二級警戒 要大於 一級警戒";
                flag_parameter_reasonable = false;
            }
            if (flag_parameter_reasonable == false)
            {
                show_main_message(mesg, S_OK, 30);
                return;
            }

            if (upload_interval < 0)
            {
                mesg = "上傳間隔時間應大於0分鐘";
                flag_parameter_reasonable = false;
            }
            if (flag_parameter_reasonable == false)
            {
                show_main_message(mesg, S_OK, 30);
                return;
            }

            if (upload_source_directory != "")
            {
                if (Directory.Exists(upload_source_directory) == false)
                {
                    mesg = "上拋來源資料夾 設定錯誤";
                    flag_parameter_reasonable = false;
                }
            }
            if (flag_parameter_reasonable == false)
            {
                show_main_message(mesg, S_OK, 30);
                return;
            }

            if (upload_destination_directory != "")
            {
                if (Directory.Exists(upload_destination_directory) == false)
                {
                    mesg = "上拋目的資料夾 設定錯誤";
                    flag_parameter_reasonable = false;
                }
            }
            if (flag_parameter_reasonable == false)
            {
                show_main_message(mesg, S_OK, 30);
                return;
            }

            if (flag_upload_enabled == true)    //若有開啟上拋功能, 要多考慮 上拋來源/目的資料夾
            {
                if (upload_source_directory == "")
                {
                    mesg = "未設定上拋來源資料夾";
                    flag_parameter_reasonable = false;
                }
                else
                {
                    if (Directory.Exists(upload_source_directory) == false)
                    {
                        mesg = "上拋來源資料夾 設定錯誤";
                        flag_parameter_reasonable = false;
                    }
                }
                if (flag_parameter_reasonable == false)
                {
                    show_main_message(mesg, S_OK, 30);
                    return;
                }

                if (upload_destination_directory == "")
                {
                    mesg = "未設定上拋目的資料夾";
                    flag_parameter_reasonable = false;
                }
                else
                {
                    if (Directory.Exists(upload_destination_directory) == false)
                    {
                        mesg = "上拋來源資料夾 設定錯誤";
                        flag_parameter_reasonable = false;
                    }
                }
                if (flag_parameter_reasonable == false)
                {
                    show_main_message(mesg, S_OK, 30);
                    return;
                }
            }
            if (flag_parameter_reasonable == false)
            {
                show_main_message("XXXXXXXXXXXXXXXXXXXXX", S_OK, 30);
                return;
            }
            else
            {
                //儲存
                Properties.Settings.Default.hdd_space_threshold1 = hdd_space_threshold1;
                Properties.Settings.Default.hdd_space_threshold2 = hdd_space_threshold2;
                Properties.Settings.Default.upload_source_directory = upload_source_directory;
                Properties.Settings.Default.upload_destination_directory = upload_destination_directory;
                Properties.Settings.Default.upload_interval = upload_interval;
                Properties.Settings.Default.upload_enabled = flag_upload_enabled;

                Properties.Settings.Default.Save();
                show_main_message("儲存設定完成", S_OK, 30);
            }
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
