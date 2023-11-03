using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace CH1610
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender,
           PaintEventArgs pe)
        {
            TextureBrush brush;
            Image img = Image.FromFile(
               @"D:\C#Lab\Sample\006.jpg");
            Graphics gs = pe.Graphics;//宣告Graphics物件
                                      //呼叫DrawImage()方法從表單左上角繪製圖片
            gs.DrawImage(img, 0, 0);
            brush = new TextureBrush(img, WrapMode.TileFlipXY);
            gs.FillRectangle(brush, 0, 0, this.Size.Width,
               this.Size.Height);
        }
    }
}
