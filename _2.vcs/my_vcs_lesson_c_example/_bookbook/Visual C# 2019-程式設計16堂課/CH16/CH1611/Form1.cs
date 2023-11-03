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

namespace CH1611
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
            Rectangle sR, dR;
            Image img = Image.FromFile(
               @"D:\C#Lab\Sample\005.jpg");
            Graphics gs = pe.Graphics;//宣告Graphics物件
                                      //呼叫DrawImage()方法從表單左上角繪製圖片
            gs.DrawImage(img, 0, 0);
            sR = new Rectangle(400, 80, 400, 400);
            dR = new Rectangle(0, 0, this.Size.Width,
               this.Size.Height);
            brush = new TextureBrush(img, WrapMode.TileFlipXY);
            gs.DrawImage(img, dR, sR, GraphicsUnit.Pixel);
        }
    }
}
