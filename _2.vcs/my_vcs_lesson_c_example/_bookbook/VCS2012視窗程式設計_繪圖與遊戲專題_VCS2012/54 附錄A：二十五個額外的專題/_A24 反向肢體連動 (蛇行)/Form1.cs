/* 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2009-09 */
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace WindowsApplication1
{
    public partial class Form1 : Form
    {
        ClassBall ball1, ball2;
        DraggingSegments snake01, snake02, snake03;

        public Form1()
        {
            InitializeComponent();

            snake01 = new DraggingSegments(10, 60, 20, Color.Red, Color.Blue);
            snake02 = new DraggingSegments(20, 30, 10, Color.Black, Color.White);
            snake03 = new DraggingSegments(20, 30, 10, Color.Black, Color.White);

            ball1 = new ClassBall(
                new Point(this.ClientSize.Width / 2, this.ClientSize.Height / 2),
                new Point(5, 3),
                new Size(this.ClientSize.Width, this.ClientSize.Height),
                30,
                Color.Green);

            ball2 = new ClassBall(
                new Point(this.ClientSize.Width / 4, this.ClientSize.Height / 4),
                new Point(3, 1),
                new Size(this.ClientSize.Width, this.ClientSize.Height),
                10,
                Color.Green);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // 反鋸齒呈現
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            snake01.Draw(e.Graphics);
            snake02.Draw(e.Graphics);
            snake03.Draw(e.Graphics);
            //e.Graphics.ResetTransform();
            //ball1.Draw(e.Graphics);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            ball1.Move();
            snake01.Update(ball1.position.X, ball1.position.Y);

            ball2.Move();
            snake02.Update(ball2.position.X, ball2.position.Y);

            snake03.Update(this.ClientSize.Width- ball2.position.X,
                this.ClientSize.Height - ball2.position.Y);

            this.Invalidate();
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            ball1.clientSize = this.ClientSize;
            ball2.clientSize = this.ClientSize;
            this.Invalidate();
        }
    }
}