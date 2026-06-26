using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
點開 方案總管/vcs_XXXXX/Properties/Settings.settings
加入要儲存的參數 的 名稱 型別 預設值
若是數字 一定要給預設值
儲存參數到 Properties.Settings.Default
方案總管/Properties/Settings.settings點開 加入名稱 型別 範圍/預設值
*/

namespace vcs_PropertiesSettingsDefault
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        //在程式開啟時把資料讀出來
        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            label1.Text = "記住表單的大小和位置,\n程式關閉時記住,\n程式開啟時讀出並套用";

            richTextBox1.Text += "取得預設資料 :\n";
            richTextBox1.Text += "Left : \t" + Properties.Settings.Default.Left.ToString() + "\n";
            richTextBox1.Text += "Top : \t" + Properties.Settings.Default.Top.ToString() + "\n";
            richTextBox1.Text += "Right : \t" + Properties.Settings.Default.Right.ToString() + "\n";
            richTextBox1.Text += "Bottom : \t" + Properties.Settings.Default.Bottom.ToString() + "\n";

            int x_st = Properties.Settings.Default.Left;
            int y_st = Properties.Settings.Default.Top;
            int w = Properties.Settings.Default.Right - Properties.Settings.Default.Left;
            int h = Properties.Settings.Default.Bottom - Properties.Settings.Default.Top;
            this.SetBounds(x_st, y_st, w, h);   //SetBounds : 設定控件的位置與大小
        }

        //在程式關閉時把資料存起來
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Properties.Settings.Default.Left = this.Left;
            Properties.Settings.Default.Top = this.Top;
            Properties.Settings.Default.Right = this.Right;
            Properties.Settings.Default.Bottom = this.Bottom;

            Properties.Settings.Default.Save();
        }

        void show_item_location()
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Text = "vcs_PropertiesSettingsDefault";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        void show_form_information()
        {
            tb_left.Text = "左 : " + this.Left.ToString();
            tb_top.Text = "上 : " + this.Top.ToString();
            tb_right.Text = "右 : " + this.Right.ToString();
            tb_bottom.Text = "下 : " + this.Bottom.ToString();

            tb_location.Text = "位置 : (" + this.Left.ToString() + ", " + this.Top.ToString() + ")";
            tb_w.Text = "寬 : " + (this.Right - this.Left).ToString();
            tb_h.Text = "高 : " + (this.Bottom - this.Top).ToString();
        }

        private void Form1_Move(object sender, EventArgs e)
        {
            show_form_information();
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            show_form_information();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "讀取程式預設值\n";
            ReadSettings();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "寫入程式預設值\n";
            SaveSettings();
        }

        private void SaveSettings()
        {
            string dir_name = @"D:\_git\vcs\_1.data\______test_files1\__pic\_書畫字圖\_peony2";

            Properties.Settings.Default.PictureDirectory = dir_name;
            Properties.Settings.Default.UpdateRegistry = true;
            Properties.Settings.Default.Location = Location;
            Properties.Settings.Default.Size = Size;
            Properties.Settings.Default.Delay = 123;
            Properties.Settings.Default.Save();
        }

        private void ReadSettings()
        {
            richTextBox1.Text += "Default.PictureDirectory" + "\t" + Properties.Settings.Default.PictureDirectory + "\n";
            richTextBox1.Text += "Default.UpdateRegistry" + "\t" + Properties.Settings.Default.UpdateRegistry + "\n";
            richTextBox1.Text += "Default.Location" + "\t" + Properties.Settings.Default.Location + "\n";
            richTextBox1.Text += "Default.Size" + "\t" + Properties.Settings.Default.Size.ToString() + "\n";
            richTextBox1.Text += "Default.Delay" + "\t" + Properties.Settings.Default.Delay.ToString() + "\n";
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/



/*
//Properties Save ST

            this.SetBounds(
                Properties.Settings.Default.Left,
                Properties.Settings.Default.Top,
                Properties.Settings.Default.Width,
                Properties.Settings.Default.Height);

            txtScale.Text = Properties.Settings.Default.Scale;

        // Save parameters.
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Properties.Settings.Default.Left = this.Left;
            Properties.Settings.Default.Top = this.Top;
            Properties.Settings.Default.Width = this.Width;
            Properties.Settings.Default.Height = this.Height;

            Properties.Settings.Default.Directory = txtDirectory.Text;
            Properties.Settings.Default.Scale = txtScale.Text;

            Properties.Settings.Default.Save();
        }

有需要存檔的資料
1. 最後存取的路徑
2. 視窗大小
3. 最後選取的設定項目


若是我的筆記本

properties.save
還要儲存字型 大小 前景色背景色
表單大小位置 

//Properties Save SP
*/
//------------------------------------------------------------  # 60個


