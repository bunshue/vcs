using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

//C# GDI在控件上繪圖

namespace draw
{
    public partial class Form1 : Form
    {
        public Point firstPoint = new Point(0, 0);  //鼠標第一點 
        public Point secondPoint = new Point(0, 0);  //鼠標第二點 
        public bool begin = false;   //是否開始畫矩形 
        /// <summary>
        /// 在from上畫矩形
        /// </summary>
        Graphics g;

        /// <summary>
        /// 在chart1控件上畫矩形
        /// </summary>
        Graphics g2;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //窗體
            g = this.CreateGraphics();
            //chart控件
            g2 = this.chart1.CreateGraphics();

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        /// <summary>
        /// 在窗體上按下鼠標事件
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            begin = true;
            firstPoint = new Point(e.X, e.Y);
        }

        /// <summary>
        /// 在窗體上鼠標移動開始繪圖
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (begin)
            {
                //清除窗體繪圖面,相當於刷新了一次窗體界面然後重新繪制
                g.Clear(this.BackColor);
                //獲取新的右下角坐標 
                secondPoint = new Point(e.X, e.Y);
                //獲取兩個數中的大者或小者
                int minX = Math.Min(firstPoint.X, secondPoint.X);
                int minY = Math.Min(firstPoint.Y, secondPoint.Y);
                int maxX = Math.Max(firstPoint.X, secondPoint.X);
                int maxY = Math.Max(firstPoint.Y, secondPoint.Y);

                //畫框 
                g.DrawRectangle(new Pen(Color.Red), minX, minY, maxX - minX, maxY - minY);
                //ControlPaint.DrawReversibleFrame(new Rectangle(minX, minY, maxX - minX, maxY - minY),this.BackColor,FrameStyle.Dashed);

            }
        }

        /// <summary>
        /// 鼠標松開停止繪圖
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            begin = false;
        }


        /// <summary>
        /// 在chart控件上按下鼠標
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void chart1_MouseDown(object sender, MouseEventArgs e)
        {
            begin = true;
            firstPoint = new Point(e.X, e.Y);
        }


        /// <summary>
        /// 在chart控件上移動鼠標繪圖
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void chart1_MouseMove(object sender, MouseEventArgs e)
        {
            if (begin)
            {
                //重新在chart上面繪圖，此處不能用clear方法，clear會清除整個繪圖界面chart控件會被清除
                this.Refresh();
                //獲取新的右下角坐標 
                secondPoint = new Point(e.X, e.Y);
                int minX = Math.Min(firstPoint.X, secondPoint.X);
                int minY = Math.Min(firstPoint.Y, secondPoint.Y);
                int maxX = Math.Max(firstPoint.X, secondPoint.X);
                int maxY = Math.Max(firstPoint.Y, secondPoint.Y);

                //畫矩形
                g2.DrawRectangle(new Pen(Color.Red), minX, minY, maxX - minX, maxY - minY);

            }
        }

        /// <summary>
        /// 鼠標松開停止繪圖
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void chart1_MouseUp(object sender, MouseEventArgs e)
        {
            begin = false;
        }






    }
}
