using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        Graphics G; // 表單的畫布
        int H, W;  // 表單的寬高
        Pen myPenBlack = new Pen(Color.Black, 1);
        Pen myPen = new Pen(Color.Red, 2);

        Brush myBrushRed = new SolidBrush(Color.Red);
        Brush myBrushAqua = new SolidBrush(Color.Aqua);
        Brush myBrushBlueViolet = new SolidBrush(Color.BlueViolet);

        Point[] up = new Point[10];   // 10個開始的圓形端點 座標
        Point[] down = new Point[10]; // 10個結束的方形端點 座標

        int[,] nodes = new int[9, 10];// 前九條垂直線的節點
        int X, Y;
        int LineNo; // 0,1,2,.. 9
        int Dir;    // 1 下,2 左,3 右     方向

        Random rd = new Random();
        int Target = 5; // 目標號碼
        Color[] color = new Color[] { 
            Color.Blue, Color.Crimson, Color.DarkOrange,
            Color.BlueViolet, Color.Brown,Color.DarkCyan,
            Color.Red,Color.OliveDrab,Color.Fuchsia,Color.Green};

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            G = this.CreateGraphics(); // 得到 Graphics 物件

            H = this.ClientSize.Height; // 得到 視窗客戶區 的高
            W = this.ClientSize.Width;  // 得到 視窗客戶區 的寬

            for (int i = 0; i < 10; i++) // 先算出上下各十個點的座標
            {
                up[i].X = (i + 1) * W / 11;
                up[i].Y = 20;

                down[i].X = (i + 1) * W / 11;
                down[i].Y = 440;
            }
            Compute_Nodes();
        }

        // 計算 前九條垂直線 的中間節點
        // 這裡要避免 節點的左右兩邊 是相同的情況
        void Compute_Nodes()
        {
            // 每條垂直線有 10 個節點 所以是 11 個區間
            // 計算 每個區間 的間距
            int k = (down[0].Y - up[0].Y) / 11;

            // 第1條垂直線 的中間節點 要加入亂數
            for (int i = 0; i < 10; i++)
                nodes[0, i] = (i + 1) * k + rd.Next(5, k);

            // 其後8條垂直線 的中間節點
            // 每個節點 不能和 前一個節點 同樣的 Y 軸座標
            for (int i = 1; i < 9; i++)
            {
                for (int j = 0; j < 10; j++)
                {
                    do
                    {
                        nodes[i, j] = (j + 1) * k + rd.Next(5, k);
                    } while (nodes[i, j] == nodes[i - 1, j]);
                }
            }
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Graphics G = e.Graphics;
            char[] a2J = new char[10] { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J' };

            // 畫 10 條垂直線
            for (int i = 0; i < 10; i++)
                G.DrawLine(myPenBlack, up[i].X, up[i].Y, down[i].X, down[i].Y);

            // 畫上端圓形 與 下端方形
            for (int i = 0; i < 10; i++)
            {
                G.FillEllipse(myBrushAqua, up[i].X - 10, up[i].Y - 10, 20, 20);
                G.DrawEllipse(myPenBlack, up[i].X - 10, up[i].Y - 10, 20, 20);

                G.DrawString(a2J[i].ToString(), this.Font, myBrushBlueViolet, up[i].X - 5, up[i].Y - 5);

                G.FillRectangle(myBrushBlueViolet, down[i].X - 10, down[i].Y - 10, 20, 20);
                G.DrawRectangle(myPenBlack, down[i].X - 10, down[i].Y - 10, 20, 20);
            }

            // 畫目標方形
            G.FillRectangle(myBrushRed, down[Target].X - 10, down[Target].Y - 10, 20, 20);
            G.DrawRectangle(myPenBlack, down[Target].X - 10, down[Target].Y - 10, 20, 20);

            // 畫橫線 是往右畫的
            for (int i = 0; i < 9; i++)
            {
                for (int j = 0; j < 10; j++)
                {
                    G.DrawLine(myPenBlack, up[i].X, nodes[i, j], up[i + 1].X, nodes[i, j]);
                }
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            int Y1 = down[0].Y; // 下一個 右端 的可轉彎 Y 軸座標
            int Y2 = down[0].Y; // 下一個 左端 的可轉彎 Y 軸座標
            int x, y;
            if (Y >= down[0].Y) // 到達底端
            {
                timer1.Enabled = false;
                return;
            }

            // Dir 1 下,2 右,3 左 
            if (Dir == 1) //往下走
            {
                if (LineNo != 9) // 如果不是最後一條 就有可右轉彎的節點 Y 軸座標
                {
                    for (int j = 0; j < 10; j++)
                    {
                        if (nodes[LineNo, j] > Y)
                        {
                            Y1 = nodes[LineNo, j];  //  右轉彎的節點 
                            break;
                        }
                    }
                }

                if (LineNo != 0) // 如果不是第一條 就有可左轉彎的節點 Y 軸座標
                {
                    for (int j = 0; j < 10; j++)
                    {
                        if (nodes[LineNo - 1, j] > Y)
                        {
                            Y2 = nodes[LineNo - 1, j]; //  左轉彎的節點
                            break;
                        }
                    }
                }

                y = Y + 10; // 試著往下走 10 個像素
                x = X;
                if (y < Y1 && y < Y2) // 如果還未遇到 左右端節點
                {
                    G.DrawLine(myPen, X, Y, x, y);
                }
                else if (Y1 <= Y2)  // y > Y1 && Y1 <= Y2 走右邊
                {
                    y = Y1;
                    G.DrawLine(myPen, X, Y, x, y);
                    Dir = 2; // 下一次要往右走
                }
                else if (Y2 < Y1)  // y > Y2 && Y2 <= Y1 走左邊
                {
                    y = Y2;
                    G.DrawLine(myPen, X, Y, x, y);
                    Dir = 3; // 下一次要往左走
                }
                X = x; // 目前的座標
                Y = y;
            }
            else if (Dir == 2) // 走右邊
            {
                x = X + 10; // 試著往右走 10 個像素
                if (x >= up[LineNo + 1].X) // 過頭了
                {
                    x = up[LineNo + 1].X; // 停在右邊下一條
                    LineNo++;
                    Dir = 1; // 下一次要往下走
                }
                y = Y;

                G.DrawLine(myPen, X, Y, x, y);
                X = x;
                Y = y;
            }
            else if (Dir == 3) // 走左邊
            {
                x = X - 10; // 試著往左走 10 個像素
                if (x <= up[LineNo - 1].X)  // 過頭了
                {
                    x = up[LineNo - 1].X; // 停在左邊上一條
                    LineNo--;
                    Dir = 1; // 下一次要往下走
                }
                y = Y;

                G.DrawLine(myPen, X, Y, x, y);
                X = x;
                Y = y;
            };
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            int x, y;
            int d;

            if (timer1.Enabled) return; // 如果目前正在走動 就不要理會玩家的動作

            x = e.X; y = e.Y;   // 滑鼠位置

            for (int i = 0; i < 10; i++)
            {
                d = (up[i].X - x) * (up[i].X - x) + (up[i].Y - y) * (up[i].Y - y);
                if (d < 400) // 20 x 20
                {
                    X = up[i].X;
                    Y = up[i].Y;
                    LineNo = i; // 0,1,2,.. 9 是第幾條被點到
                    Dir = 1; // 1 下,2 右,3 左
                    myPen.Color = color[LineNo];
                    timer1.Enabled = true;
                    break;
                }
            }
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Space)  // 空白鍵 更新畫面
            {
                timer1.Enabled = false;
                this.Invalidate();
            }
            else if (e.KeyCode == Keys.Enter) // Enter鍵 重算節點 更新畫面
            {
                timer1.Enabled = false;
                Target = rd.Next(10);  // 目標號碼
                Compute_Nodes();
                this.Invalidate();
            }
        }
    }
}