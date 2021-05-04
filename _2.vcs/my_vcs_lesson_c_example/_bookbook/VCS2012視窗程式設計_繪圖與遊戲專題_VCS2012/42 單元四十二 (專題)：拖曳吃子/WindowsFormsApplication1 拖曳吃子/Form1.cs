using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Diagnostics;
using System.Media;


namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        List<Point> Obstacles = new List<Point>(); // 四散的小圓點
        Point MousePos = new Point();  // 滑鼠的位置
        Point BallPos = new Point();    // 主圓球的位置
        Random rd = new Random();    // 亂數
        Stopwatch sw = new Stopwatch(); // 記錄耗費的時間

        public Form1()
        {
            InitializeComponent();
            this.ClientSize = new Size(800, 600);// 調整視窗客戶區寬高

            BallPos = new Point(this.ClientSize.Width / 2,
                                this.ClientSize.Height / 2);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // 重畫 四散的小圓點
            for (int i = 0; i <= Obstacles.Count - 1; i++)
            {
                e.Graphics.FillEllipse(Brushes.Aqua, Obstacles[i].X - 10, Obstacles[i].Y - 10, 20, 20);
            }

            TimeSpan ts = sw.Elapsed;
            string s = "經過 " + Convert.ToString(ts.Seconds) + "." + Convert.ToString(ts.Milliseconds) + " 秒";
            e.Graphics.DrawString(s, this.Font, Brushes.White, 10, 10);

            // 重畫 主圓球
            e.Graphics.FillEllipse(Brushes.Pink, BallPos.X - 15, BallPos.Y - 15, 30, 30);
        }

        // 記錄滑鼠的位置
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            MousePos.X = e.X;
            MousePos.Y = e.Y;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            // 如果已經沒有 小圓點
            if (Obstacles.Count == 0)
            {
                sw.Stop();
                timer1.Enabled = false;
            }

            // 更新 主圓球的位置
            BallPos.X = BallPos.X + (MousePos.X - BallPos.X) / 10;
            BallPos.Y = BallPos.Y + (MousePos.Y - BallPos.Y) / 10;

            // 更新 小圓點 的位置
            int X, Y;
            for (int i = 0; i <= Obstacles.Count - 1; i++)
            {
                X = Obstacles[i].X + rd.Next(11) - 5;
                Y = Obstacles[i].Y + rd.Next(11) - 5;

                // 如果跑出邊界就不要更新
                if (X < 10 || X > this.ClientSize.Width - 10) X = Obstacles[i].X;
                if (Y < 10 || Y > this.ClientSize.Height - 10) Y = Obstacles[i].Y;

                Obstacles[i] = new Point(X, Y);
            }

            // 碰撞偵測 移除小圓點
            double D;
            for (int i = Obstacles.Count - 1; i >= 0; i--)
            {
                D = Math.Sqrt((Obstacles[i].X - BallPos.X) * (Obstacles[i].X - BallPos.X) +
                    (Obstacles[i].Y - BallPos.Y) * (Obstacles[i].Y - BallPos.Y));

                if (D < 25) // 15+10
                {
                    Obstacles.RemoveAt(i);
                    SystemSounds.Beep.Play();
                }
            }

            this.Invalidate();
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Space) // 空白鍵
            {
                Obstacles.Clear(); // 清除小圓點

                // 依序加入小圓點
                for (int i = 100; i <= 700; i = i + 200)
                    for (int j = 100; j <= 500; j = j + 200)
                        Obstacles.Add(new Point(i, j));

                // 主圓球放置 於 視窗客戶區中心點
                BallPos = new Point(this.ClientSize.Width / 2,
                this.ClientSize.Height / 2);

                sw.Reset();
                sw.Start(); // 開始計時
                timer1.Enabled = true;
            }
        }
    }
}