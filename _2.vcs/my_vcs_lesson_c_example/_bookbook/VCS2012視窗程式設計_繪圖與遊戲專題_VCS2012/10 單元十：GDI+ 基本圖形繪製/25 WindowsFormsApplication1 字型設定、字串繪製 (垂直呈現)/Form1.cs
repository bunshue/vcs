using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;  // HatchBrush

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        Font myFont = new Font("標楷體", 24); // 字型
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            string text = "VC# 繪圖程式好容易！"; // 文字字串
            StringFormat stringFormat = new StringFormat();　// 字串 繪出格式
            stringFormat.FormatFlags = StringFormatFlags.DirectionVertical;　// 垂直

            int stringWidth = 100; // 字串　最大的寬度

            SizeF stringSize = e.Graphics.MeasureString(text, myFont, stringWidth, stringFormat); // 文字字串的寬高
            float X = this.ClientSize.Width / 2 - stringSize.Width / 2; // 左上角的座標
            float Y = this.ClientSize.Height / 2 - stringSize.Height / 2;

            e.Graphics.DrawString(text,  // 繪出文字字串
                myFont,
                Brushes.Red,
                X, Y, stringFormat);
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}