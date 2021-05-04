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
        List<ClassSmallBall> R = new List<ClassSmallBall>(); // ���� �h���p�y�y�Ъ��ʺA�}�C
        const int smallBallCount = 500;
        Point Mouse = new Point(); // �ƹ����y��
        PointF BigBall = new Point(); // �j�y���y��
        Random rd = new Random();  // �ܼ�

        public Form1()
        {
            InitializeComponent();
            
            ClassSmallBall smallBall;
            for (int i = 0; i < smallBallCount; i++)  // ��l�� 200 ���p�y
            {
                smallBall = new ClassSmallBall(this.ClientSize.Width, this.ClientSize.Height, i);
                R.Add(smallBall);
            }
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // ø�X�j�y
            e.Graphics.FillEllipse(Brushes.Black, (int)(BigBall.X - 15), (int)(BigBall.Y - 15), 30, 30);

            // ø�X�p�y
            for(int i= 0; i <= R.Count-1; i++)
            {
                R[i].Draw(e.Graphics);
            }
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            // �����ƹ����y��
            Mouse.X = e.X;
            Mouse.Y = e.Y;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            // ���j�y �v�� �G�� �ƹ����y��
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