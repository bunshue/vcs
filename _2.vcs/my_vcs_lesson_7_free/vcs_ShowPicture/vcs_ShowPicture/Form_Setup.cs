using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_ShowPicture
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
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            x_st = 30;
            y_st = 50;
            dx = 150;
            dy = 50;

            rb_mode0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            rb_mode1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            rb_mode2.Location = new Point(x_st + dx * 0, y_st + dy * 2);

            rb_mode0.Text = "全屏隨機位置 顯示 圖片";
            rb_mode1.Text = "全屏單圖 置中 滿屏 顯示圖片";
            rb_mode2.Text = "全屏單圖 靠右 顯示圖片";

            groupBox1.Location = new Point(50, 200);
            groupBox1.Size = new Size(400, 200);

            groupBox2.Location = new Point(50 + 410, 200);
            groupBox2.Size = new Size(400, 200);


            x_st = 700;
            y_st = 420;
            dx = 80;
            dy = 20;

            bt_ok.Location = new Point(x_st, y_st);
            bt_cancel.Location = new Point(x_st + dx, y_st);

            bt_open_picture.BackgroundImage = vcs_ShowPicture.Properties.Resources.open_folder;

        }

        private void bt_open_picture_Click(object sender, EventArgs e)
        {
            folderBrowserDialog1.SelectedPath = Application.StartupPath;    //預設開啟的路徑
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                tb_picture_folder_name.Text = folderBrowserDialog1.SelectedPath;
            }
            else
            {
                //richTextBox2.Text = "未選取資料夾\n";
            }

        }

        private void bt_ok_Click(object sender, EventArgs e)
        {
            string foldername = tb_picture_folder_name.Text;
            if (Directory.Exists(foldername) == false)     //確認資料夾是否存在
            {
                //richTextBox1.Text += "資料夾: " + foldername + " 不存在，離開\n";

                MessageBox.Show("圖片資料夾不存在, 離開", "ShowPicture", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            else
            {
                //存到系統參數裏
                Properties.Settings.Default.picture_foldername = foldername;
                Properties.Settings.Default.Save();
                this.Close();
            }
        }

        private void bt_cancel_Click(object sender, EventArgs e)
        {

        }

    }
}

