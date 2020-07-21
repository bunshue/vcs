using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace 小畫家大全2
{
    public partial class Form1 : Form
    {
        private Point startPoint, oldPoint; //繪圖時紀錄滑鼠位置
        //枚举类型，各种绘图工具
        private enum drawTools
        {
            Pen = 0, Line, Circle, Rectangle, String, Erase, None
        };
        //当前使用的工具
        private drawTools drawTool = drawTools.Pen;
        private bool isDrawing = false;     //是否正在繪圖

        Graphics g;         //Graphics實例
        Pen PenStyle;
        //SolidBrush sb;
        Bitmap bitmap1;

        Graphics ig;        //繪製bitmap的Graphics實例

        Color foreColor = Color.Red;
        Color backColor = Color.White;

        public Form1()
        {
            InitializeComponent();
            //創建一個bitmap
            bitmap1 = new Bitmap(this.ClientRectangle.Width, this.ClientRectangle.Height);
            g = this.CreateGraphics();
            ig = Graphics.FromImage(bitmap1);
            //ig.Clear(backColor);

            PenStyle = new Pen(foreColor);
            PenStyle.Width = (int)numericUpDown1.Value;
            PenStyle.StartCap = System.Drawing.Drawing2D.LineCap.Round;
            PenStyle.EndCap = System.Drawing.Drawing2D.LineCap.Round;
            PenStyle.Color = foreColor;

            //PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.Bevel;
            PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.Round;

            g.Clear(backColor);
            ig.Clear(backColor);
        }

        private void panel1_MouseDown(object sender, MouseEventArgs e)
        {

        }

        private void panel1_MouseMove(object sender, MouseEventArgs e)
        {

        }

        private void panel1_MouseUp(object sender, MouseEventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {

        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void Form1_SizeChanged(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
