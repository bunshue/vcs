using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_BarcodeScanner
{
    public partial class Form1 : Form
    {
        private const int BORDER = 30;

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
            int W = 640;
            int H = 480;
            int x_st = BORDER;
            int y_st = BORDER;
            int dx = 140 + 50;
            int dy = 50 + 15;

            //pictureBox1.Size = new Size(W, H);
            //pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            //richTextBox1.Size = new Size(300, 600);
            //richTextBox1.Location = new Point(x_st + dx * 4 + 70, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        int ccc = 0;
        int timer_cnt = 0;
        private void timer_barcode_Tick(object sender, EventArgs e)
        {
            ccc++;
            if ((ccc % 4) == 0)
                lb_main_mesg1.Text = "等待輸入第 1 筆資料 \\";
            else if ((ccc % 4) == 1)
                lb_main_mesg1.Text = "等待輸入第 1 筆資料 |";
            else if ((ccc % 4) == 2)
                lb_main_mesg1.Text = "等待輸入第 1 筆資料 /";
            else
                lb_main_mesg1.Text = "等待輸入第 1 筆資料 -";

            if ((timer_cnt++ % 10) == 0)
            {
                richTextBox1.Text += "八";
                if (this.tb_wait_barcode_data.Focused == false)
                {
                    this.tb_wait_barcode_data.Focus();
                    richTextBox1.Text += "F8";
                }
            }

            int len;
            len = tb_wait_barcode_data.Text.Length;

            if (len > 2000)   //太長, 直接放棄
            {
                tb_wait_barcode_data.Clear();
                //richTextBox1.Text += "X1";
                return;
            }
            else if (len > 5)    //檢查是否換行
            {
                if ((tb_wait_barcode_data.Text[len - 2] == 0x0D) || (tb_wait_barcode_data.Text[len - 1] == 0x0A))
                {
                    tb_wait_barcode_data.Text = tb_wait_barcode_data.Text.Trim();
                    richTextBox1.Text += "OK";
                }
                else
                {
                    richTextBox1.Text += "X2";
                    return;
                }
            }
            else    //太短  留著累計
            {
                //richTextBox1.Text += "X3";
                return;
            }

            if (tb_wait_barcode_data.Text.Length > 0)
            {
                richTextBox1.Text += "取得資料1 : " + tb_wait_barcode_data.Text + "\n";
                tb_barcode_data.Text = tb_wait_barcode_data.Text;
                tb_wait_barcode_data.Text = "";
            }
        }

        private void button01_Click(object sender, EventArgs e)
        {
            //網頁連線

        }


    }
}


