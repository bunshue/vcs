using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Media;


namespace WindowsApplication11
{
    public partial class Form1 : Form
    {
        List<ClassSmallBall> R = new List<ClassSmallBall>(); // 紀錄 多顆小球座標的動態陣列
        const int smallBallCount = 500;
        Point Mouse = new Point(); // 滑鼠的座標
        PointF BigBall = new Point(); // 大球的座標
        Random rd = new Random();  // 變數

        public Form1()
        {
            InitializeComponent();
            
            ClassSmallBall smallBall;
            for (int i = 0; i < smallBallCount; i++)  // 初始化 200 顆小球
            {
                smallBall = new ClassSmallBall(this.ClientSize.Width, this.ClientSize.Height, i);
                R.Add(smallBall);
            }
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // 繪出大球
            e.Graphics.FillEllipse(Brushes.Black, (int)(BigBall.X - 15), (int)(BigBall.Y - 15), 30, 30);

            // 繪出小球
            for(int i= 0; i <= R.Count-1; i++)
            {
                R[i].Draw(e.Graphics);
            }
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            // 紀錄滑鼠的座標
            Mouse.X = e.X;
            Mouse.Y = e.Y;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            // 讓大球 逐漸 逼近 滑鼠的座標
            BigBall.X = BigBall.X + (Mouse.X - BigBall.X) / 10;
            if (Math.Abs(Mouse.X - BigBall.X) < 1) BigBall.X = Mouse.X;

            BigBall.Y = BigBall.Y + (Mouse.Y - BigBall.Y) / 10;
            if (Math.Abs(Mouse.Y - BigBall.Y) < 1) BigBall.Y = Mouse.Y;

            for (int i = 0; i <= R.Count - 1; i++)
            {
                R[i].Update(BigBall);
            }
            this.Invalidate();
        }
    }
}