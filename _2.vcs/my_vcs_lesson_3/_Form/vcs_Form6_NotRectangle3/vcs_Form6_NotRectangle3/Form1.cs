using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Form6_NotRectangle3
{
    public partial class Form1 : Form
    {
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_bmp\not_rectangle.bmp";
            //string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_png\ladybug.png"; //128X128

            bitmap1 = new Bitmap(filename); //從指定的圖像初始化Bitmap對象
            bitmap1.MakeTransparent(Color.Blue);//使用默認的透明顏色對Bitmap位圖透明
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            e.Graphics.DrawImage((Image)bitmap1, new Point(0, 0));//在窗體上繪制圖片
        }
    }
}

