using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MyCalculator
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
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 60;
            dx = 120 + 10;
            dy = 60 + 10;

            textBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox_type1.Location = new Point(x_st + dx * 1, y_st + dy * 0-15);
            label0.Location = new Point(x_st + dx * 1+100, y_st + dy * 0);
            textBox1.Location = new Point(x_st + dx * 3-50, y_st + dy * 0);
            label1.Location = new Point(x_st + dx * 3 - 100, y_st + dy * 0);
            bt_calculate0.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            textBox2.Location = new Point(x_st + dx * 4+80, y_st + dy * 0);



            richTextBox1.Size = new Size(500, 400);
            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1000, 810);
            this.Text = "vcs_MyCalculator";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        bool check_textbox_number(KeyPressEventArgs e)
        {
            // 限制 TextBox只能輸入十進位碼、小數點、Backspace、Enter
            // e.KeyChar == (Char)48 ~ 57 -----> 0~9
            // e.KeyChar == (Char)46 ----------> .
            // e.KeyChar == (Char)8 -----------> Backspace
            // e.KeyChar == (Char)13-----------> Enter            

            if ((e.KeyChar >= (Char)48 && e.KeyChar <= (Char)57) || (e.KeyChar == (Char)13) || (e.KeyChar == (Char)8) || (e.KeyChar == (Char)46))
            {
                return false;  // e.Handled = false; 未處理, 表示要顯示出來
            }
            else
            {
                return true;  // e.Handled = true; 已處理, 表示不顯示出來
            }
        }

        private void textBox0_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = check_textbox_number(e);

            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                bt_calculate0_Click(sender, e);
            }
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {

        }

        private void bt_calculate0_Click(object sender, EventArgs e)
        {
            float number0 = 0;
            bool conversionSuccessful0 = float.TryParse(textBox0.Text, out number0);    //out為必須
            if (conversionSuccessful0 == true)
            {
                richTextBox1.Text += "得到float數字： " + number0 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗\n";
            }

            float number1 = 0;
            bool conversionSuccessful1 = float.TryParse(textBox1.Text, out number1);    //out為必須
            if (conversionSuccessful1 == true)
            {
                richTextBox1.Text += "得到float數字： " + number1 + "\n";
            }
            else
            {
                richTextBox1.Text += "float.TryParse 失敗\n";
            }

            if ((conversionSuccessful0 == false) || (conversionSuccessful1 == false))
            {
                richTextBox1.Text += "資料不足, 離開\n";
                textBox0.Text = "";
                textBox1.Text = "1";
                return;
            }

            int KBS = 1;
            if (rb_type1a.Checked == true)
            {
                KBS = 1024;
            }

            float total_size = number0 * 1024 * KBS * 60 * 60 * number1;

            richTextBox1.Text += "total_size = " + total_size.ToString() + "\t檔案大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
            textBox2.Text = ByteConversionTBGBMBKB(Convert.ToInt64(total_size));
        }

        private void bt_calculate1_Click(object sender, EventArgs e)
        {
            int i;
            Int64 total_size = 0;

            total_size = 123;
            for (i = 1; i < 20; i++)
            {
                total_size *= i;
                richTextBox1.Text += "total_size = " + total_size.ToString() + "\t檔案大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
            }
        }

        const Int64 TB = (Int64)GB * 1024;//定義TB的計算常量
        const int GB = 1024 * 1024 * 1024;//定義GB的計算常量
        const int MB = 1024 * 1024;//定義MB的計算常量
        const int KB = 1024;//定義KB的計算常量
        public string ByteConversionTBGBMBKB(Int64 size)
        {
            if (size < 0)
                return "不合法的數值";
            else if (size / TB >= 1024)//如果目前Byte的值大於等於1024TB
                return "無法表示";
            else if (size / TB >= 1)//如果目前Byte的值大於等於1TB
                return (Math.Round(size / (float)TB, 2)).ToString() + " TB";//將其轉換成TB
            else if (size / GB >= 1)//如果目前Byte的值大於等於1GB
                return (Math.Round(size / (float)GB, 2)).ToString() + " GB";//將其轉換成GB
            else if (size / MB >= 1)//如果目前Byte的值大於等於1MB
                return (Math.Round(size / (float)MB, 2)).ToString() + " MB";//將其轉換成MB
            else if (size / KB >= 1)//如果目前Byte的值大於等於1KB
                return (Math.Round(size / (float)KB, 2)).ToString() + " KB";//將其轉換成KB
            else
                return size.ToString() + " Byte";//顯示Byte值
        }

        private void textBox0_Click(object sender, EventArgs e)
        {
            textBox0.SelectAll();
        }

        private void textBox1_Click(object sender, EventArgs e)
        {
            textBox1.SelectAll();
        }


    }
}
