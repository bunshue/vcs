using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;


//製作不規則形狀表單 將部分顏色設置為透明

//1. 要拉一個比圖示還要大的表單, 在 Form1_Load 設置表單屬性
//2. 直接貼上 OnPaint 部分(重寫窗體的 OnPaint 方法)


namespace vcs_Form6_NotRectangle1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //將窗體的 TransparencyKey 屬性設為 Control，FormBorderStyle 設為 None。
            this.TransparencyKey = System.Drawing.SystemColors.Control; //將多餘的背景顏色設定為透明(用透明色將窗體設置透明)
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;   //去除表單外框
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\banner_ims.png";
            Bitmap bitmap1;    //聲明一個System.Drawing.Bitmap類的對象bitmap1

            bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            bitmap1.MakeTransparent(Color.Red);     //使用默認的透明顏色進行透明設置
            bitmap1.MakeTransparent(Color.Pink);    //使用默認的透明顏色進行透明設置
            bitmap1.MakeTransparent(Color.Blue);    //使用默認的透明顏色進行透明設置

            e.Graphics.DrawImage((Image)bitmap1, new Point(0, 0));  //將圖片畫出
        }
    }
}

