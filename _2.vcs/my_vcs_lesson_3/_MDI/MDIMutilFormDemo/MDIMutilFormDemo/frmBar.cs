using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace MDIMutilFormDemo
{
    public partial class frmBar : Form
    {
        public frmBar()
        {
            InitializeComponent();
        }

        // 宣告p[0]~p[3]的PictureBox陣列，可存放用來存放0.jpg~3.jpg
        // 其中p[0]不使用，p[1]~p[3]代表三個拉霸圖示
        PictureBox[] p = new PictureBox[4];
        // 宣告num[0]~num[3]的整數陣列，用來存放0~3的數值
        // 其中num[0]不使用
        int[] num = new int[4];
        int t; //宣告t用來計算timer1共執行幾次

        //表單載入時執行Form1_Load事件處理函式
        private void frmBar_Load(object sender, EventArgs e)
        {
            // 使表單無法被調整大小
            this.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            picBtn.Image = new Bitmap("barImg/up.jpg"); //使picBtn顯示up.jpg
            // 使載入的圖片隨picBtn大小伸縮
            picBtn.SizeMode = PictureBoxSizeMode.StretchImage;
            p[1] = pic1;  // 將pic1指定給p(1)
            p[2] = pic2; // 將pic2指定給p(2)
            p[3] = pic3;// 將pic3指定給p(3)
            // 使用迴圈使pic1~pic3顯示0.jpg圖
            for (int i = 1; i <= p.GetUpperBound(0); i++)
            {
                p[i].Image = new Bitmap("barImg/0.jpg");
                p[i].SizeMode = PictureBoxSizeMode.Zoom;
            }
            timer1.Interval = 100;  // 使timer1計時器每0.1秒執行一次
            lblSum.Text = "50";      // 可投注的總數量lblSum為50
        }

        // 按下picBtn鈕時會執行picBtn_Click事件處理函式
        private void picBtn_Click(object sender, EventArgs e)
        {
            // 判斷 投注量nudQty.Value是否大於 0
            // 且 投注量nudQty.Value是否大於可投注總數量lblSum.Text
            if (nudQty.Value > 0 && nudQty.Value <= Convert.ToInt32(lblSum.Text))
            {
                timer1.Enabled = true;    //計時器timer1啟動
                //可投注量減掉本次的的投注題
                lblSum.Text = Convert.ToString((Convert.ToInt32(lblSum.Text) - nudQty.Value));
                nudQty.Enabled = false;  // 無法投注
                picBtn.Image = new Bitmap("barImg/down.jpg"); //使picBtn顯示down.jpg
                picBtn.Enabled = false;  // picBtn圖片按鈕失效
            }
            else
            {  //若投注量小於0且投注量大於可投注的總數量
                MessageBox.Show("投注有誤");
            }
        }

        // 當timer1啟動時，每0.1秒皆會執行timer1_Tick事件處理函式一次
        private void timer1_Tick(object sender, EventArgs e)
        {
            Random r = new Random();  //建立亂數物件r
            //使用迴圈讓pic1~pic3每次執行皆亂數的方式顯示0.jpg~3.jpg

            for (int i = 1; i <= p.GetUpperBound(0); i++)
            {
                num[i] = r.Next(0, 4);   // 產生 0~3 的亂數並指定給 num[1]~num[3]
                // 使pic1~pic3以亂數的方式顯示 0.jpg~3.jpg
                p[i].Image = new Bitmap("barImg/" + Convert.ToString(num[i]) + ".jpg");
            }
            t += 1;
            // 當計時器執行20次時，即馬上判斷是否中獎
            if (t == 20)
            {
                timer1.Enabled = false;  //計時器Timer1停止
                nudQty.Enabled = true;   //可以開始投注
                picBtn.Enabled = true;   // picBtn圖形按鈕可啟用
                //當num[1]為0且num[2]為0且num[3]為0表示pic1~pic3三個圖示皆是荔枝
                if (num[1] == 0 && num[2] == 0 && num[3] == 0)
                {
                    lblSum.Text = (Convert.ToInt32(lblSum.Text) + (nudQty.Value * 5)).ToString();
                    MessageBox.Show("中獎了! 投注量*5");
                }
                // 當num[1]為1且num[2]為1且num[3]為1表示pic1~pic3三個圖示皆是星星
                else if (num[1] == 1 && num[2] == 1 & num[3] == 1)
                {
                    lblSum.Text = (Convert.ToInt32(lblSum.Text) + (nudQty.Value * 10)).ToString();
                    MessageBox.Show("中獎了! 投注量*10");
                }
                //當num[1]為2且num[2]為2且num[3]為2表示pic1~pic3三個圖示皆是西瓜
                else if (num[1] == 2 && num[2] == 2 && num[3] == 2)
                {
                    lblSum.Text = (Convert.ToInt32(lblSum.Text) + (nudQty.Value * 15)).ToString();
                    MessageBox.Show("中獎了! 投注量*15");
                }
                // 當num[1]為3且num[2]為3且num[3]為3表示pic1~pic3三個圖示皆是BAR
                else if (num[1] == 3 && num[2] == 3 && num[3] == 3)
                {
                    lblSum.Text = (Convert.ToInt32(lblSum.Text) + (nudQty.Value * 20)).ToString();
                    MessageBox.Show("中獎了! 投注量*20");
                }
                picBtn.Image = new Bitmap("barImg/up.jpg"); //使picBtn顯示up.jpg
                t = 0;
            }
        }
    }
}
