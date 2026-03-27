using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
製作不規則窗體

Form1 的 屬性

FormBorderStyle 設置為 None
BackgroundImage 設置為指定的圖片
TransparencyKey 設置指定的顏色
（此屬性告訴應用程序窗體中的哪些部分需要設置為透明。 ）
*/

//製作不規則形狀表單 將部分顏色設置為透明
//1. 要拉一個比圖示還要大的表單, 在 Form1_Load 設置表單屬性
//2. 直接貼上 OnPaint 部分(重寫窗體的 OnPaint 方法)

namespace vcs_Form6_NotRectangle1
{
    public partial class Form1 : Form
    {
        int mode = 0;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            if (mode == 0)
            {
                this.BackgroundImage = new Bitmap("../../img/minion-yellow.png");
                this.FormBorderStyle = FormBorderStyle.None;  // 設定無邊框
                this.Width = this.BackgroundImage.Width;
                this.Height = this.BackgroundImage.Height;
                this.TransparencyKey = Color.FromArgb(240, 240, 240);
            }
            else if (mode == 1)
            {
                //string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_png\ladybug.png"; //128X128
                string filename = @"../../img/matlab.png";  //圖很大 900X800, 後面要改成Zoom
                this.BackgroundImage = Bitmap.FromFile(filename);
                this.BackgroundImageLayout = ImageLayout.Zoom;

                this.FormBorderStyle = FormBorderStyle.None;  // 設定無邊框
                this.TransparencyKey = Color.FromArgb(240, 240, 240);   //指名要變成透明的顏色
                //this.TransparencyKey = Color.White;   //指名要變成透明的顏色
                //全圖的指明顏色部分 都會變成透明可穿透 不只邊緣部分
            }
            else if (mode == 2)
            {
                /*
                表單Form1的屬性/ 

                BackColor 改 White
                FormBorderStyle 改 None
                TransparencyKey = 改 White
    
                選一張圖，白色部分就會變成透明
                BackgroundImage
                BackgroundImageLayout 改 Center
                */
                string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
                this.BackgroundImage = Bitmap.FromFile(filename);
                this.BackColor = Color.White;
                this.FormBorderStyle = FormBorderStyle.None;  // 設定無邊框
                this.TransparencyKey = Color.White;
                this.BackgroundImageLayout = ImageLayout.Center;
            }
            else if (mode == 3)
            {
                //將窗體的 TransparencyKey 屬性設為 Control，FormBorderStyle 設為 None。
                this.TransparencyKey = System.Drawing.SystemColors.Control; //將多餘的背景顏色設定為透明(用透明色將窗體設置透明)
                this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;   //去除表單外框
            }
            else if (mode == 4)
            {
                string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_bmp\not_rectangle.bmp";
                //string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_png\ladybug.png"; //128X128

                bitmap1 = new Bitmap(filename); //從指定的圖像初始化Bitmap對象
                bitmap1.MakeTransparent(Color.Blue);//使用默認的透明顏色對Bitmap位圖透明
                this.TransparencyKey = System.Drawing.SystemColors.Control; //將多餘的背景顏色設定為透明(用透明色將窗體設置透明)
                this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;   //去除表單外框
            }
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            if (mode == 3)
            {
                string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\banner_ims.png";

                Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
                bitmap1.MakeTransparent(Color.Red);     //使用默認的透明顏色進行透明設置
                bitmap1.MakeTransparent(Color.Pink);    //使用默認的透明顏色進行透明設置
                bitmap1.MakeTransparent(Color.Blue);    //使用默認的透明顏色進行透明設置

                e.Graphics.DrawImage((Image)bitmap1, new Point(0, 0));  //將圖片畫出
            }
            else if (mode == 4)
            {
                e.Graphics.DrawImage((Image)bitmap1, new Point(0, 0));//在窗體上繪制圖片
            }
        }
    }
}
