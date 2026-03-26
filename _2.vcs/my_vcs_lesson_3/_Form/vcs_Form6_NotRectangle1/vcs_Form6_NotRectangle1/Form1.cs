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
            /*
            this.BackgroundImage = new Bitmap("../../img/minion-yellow.png");
            this.FormBorderStyle = FormBorderStyle.None;  // 設定無邊框
            this.Width = this.BackgroundImage.Width;
            this.Height = this.BackgroundImage.Height;
            this.TransparencyKey = Color.FromArgb(240, 240, 240);
            */

            //6060

            /*
            //string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_png\ladybug.png"; //128X128
            string filename = @"../../img/matlab.png";  //圖很大 900X800, 後面要改成Zoom
            this.BackgroundImage = Bitmap.FromFile(filename);
            this.BackgroundImageLayout = ImageLayout.Zoom;

            this.FormBorderStyle = FormBorderStyle.None;  // 設定無邊框
            this.TransparencyKey = Color.FromArgb(240, 240, 240);   //指名要變成透明的顏色
            //this.TransparencyKey = Color.White;   //指名要變成透明的顏色
            //全圖的指明顏色部分 都會變成透明可穿透 不只邊緣部分
            */

            //6060

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
    }
}
