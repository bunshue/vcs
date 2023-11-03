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

namespace CH1612
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
            Image img = Image.FromFile(
               @"D:\C#Lab\Sample\007.jpg");
            Graphics gs = pe.Graphics;//宣告Graphics物件
                                      //呼叫DrawImage()方法從表單左上角繪製圖片
            gs.DrawImageUnscaled(img, 10, 10);
        }
    }
}
