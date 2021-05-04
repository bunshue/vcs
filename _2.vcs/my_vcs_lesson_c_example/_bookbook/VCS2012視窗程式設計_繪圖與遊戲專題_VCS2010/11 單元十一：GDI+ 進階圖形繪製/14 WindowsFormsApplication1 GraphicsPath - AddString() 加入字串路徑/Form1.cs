using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;  // for GraphicsPath

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            GraphicsPath gp = new GraphicsPath(); // GraphicsPath物件

            string text = "VC# 繪圖程式好容易！"; // 文字字串

            FontFamily family = new FontFamily("標楷體");
            StringFormat format = StringFormat.GenericDefault;
            // format.FormatFlags = StringFormatFlags.DirectionVertical;　// 垂直

            gp.AddString(text,  // 繪出文字字串
                family,
                (int)FontStyle.Regular,
                80,
                new Point(40, 40),
                format);

            // 將 gp 內的形狀 繪出
            e.Graphics.DrawPath(Pens.Black, gp); // 繪出GraphicsPath物件
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}