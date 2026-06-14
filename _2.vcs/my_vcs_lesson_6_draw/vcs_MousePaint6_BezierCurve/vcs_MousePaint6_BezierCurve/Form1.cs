using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for SmoothingMode

// 滑鼠操作畫圖相關

namespace vcs_MousePaint6_BezierCurve
{
    public partial class Form1 : Form
    {
        Pen penRed = new Pen(Color.Red, 3);

        //------------------------------------------------------------  # 60個

        //pictureBox3 貝茲線與控制點 ST
        List<MovingPoint> mpList3 = new List<MovingPoint>(); // 可移動點的動態陣列
        int mp_Selected3 = -1;  // 動態陣列 的第幾個 被選到
        bool dragging3 = false; // 是否拖拉中
        //pictureBox3 貝茲線與控制點 SP

        //------------------------------------------------------------  # 60個

        //pictureBox4 連續貝茲線與控制點 ST
        List<MovingPoint> mpList4 = new List<MovingPoint>(); // 可移動點的動態陣列
        int mp_Selected4 = -1;  // 動態陣列 的第幾個 被選到
        bool dragging4 = false; // 是否拖拉中
        //pictureBox4 連續貝茲線與控制點 SP

        //------------------------------------------------------------  # 60個

        //pictureBox5 ST
        List<MovingPoint> mpList5 = new List<MovingPoint>(); // 可移動點的動態陣列
        int mp_Selected5 = -1;  // 動態陣列 的第幾個 被選到
        bool dragging5 = false; // 是否拖拉中
        //pictureBox5 SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            this.DoubleBuffered = true;

            //------------------------------------------------------------  # 60個

            //pictureBox3 貝茲線與控制點 ST
            MovingPoint mp3;
            mp3 = new MovingPoint(new Point(100, 200));
            mpList3.Add(mp3); // 第一個控制點

            mp3 = new MovingPoint(new Point(200, 100));
            mpList3.Add(mp3); // 第二個控制點

            mp3 = new MovingPoint(new Point(300, 300));
            mpList3.Add(mp3); // 第三個控制點

            mp3 = new MovingPoint(new Point(400, 200));
            mpList3.Add(mp3); // 第四個控制點
            //pictureBox3 貝茲線與控制點 SP

            //------------------------------------------------------------  # 60個

            //pictureBox4 連續貝茲線與控制點 ST
            MovingPoint mp4;
            mp4 = new MovingPoint(new Point(50, 200));
            mpList4.Add(mp4); // 第一個控制點

            mp4 = new MovingPoint(new Point(100, 100));
            mpList4.Add(mp4); // 第二個控制點

            mp4 = new MovingPoint(new Point(150, 300));
            mpList4.Add(mp4); // 第三個控制點

            mp4 = new MovingPoint(new Point(200, 200));
            mpList4.Add(mp4); // 第四個控制點

            mp4 = new MovingPoint(new Point(250, 100));
            mpList4.Add(mp4); // 第五個控制點

            mp4 = new MovingPoint(new Point(300, 300));
            mpList4.Add(mp4); // 第六個控制點

            mp4 = new MovingPoint(new Point(350, 200));
            mpList4.Add(mp4); // 第七個控制點
            //pictureBox4 連續貝茲線與控制點 SP

            //------------------------------------------------------------  # 60個

            //pictureBox5 ST
            MovingPoint mp5;
            mp5 = new MovingPoint(new Point(100, 200));
            mpList5.Add(mp5); // 第一個控制點

            mp5 = new MovingPoint(new Point(200, 100));
            mpList5.Add(mp5); // 第二個控制點

            mp5 = new MovingPoint(new Point(300, 300));
            mpList5.Add(mp5); // 第三個控制點

            mp5 = new MovingPoint(new Point(400, 200));
            mpList5.Add(mp5); // 第四個控制點
            //pictureBox5 SP
        }

        void show_item_location()
        {
            int W = 460;
            int H = 400;
            int x_st = 10;
            int y_st = 30;
            int dx = W + 20;
            int dy = H + 50;
            pictureBox0.Size = new Size(W, H);
            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox4.Size = new Size(W, H);
            pictureBox5.Size = new Size(W, H);
            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox5.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            int dd = 26;
            label0.Location = new Point(x_st + dx * 0, y_st + dy * 0 - dd);
            label1.Location = new Point(x_st + dx * 1, y_st + dy * 0 - dd);
            label2.Location = new Point(x_st + dx * 2, y_st + dy * 0 - dd);
            label3.Location = new Point(x_st + dx * 0, y_st + dy * 1 - dd);
            label4.Location = new Point(x_st + dx * 1, y_st + dy * 1 - dd);
            label5.Location = new Point(x_st + dx * 2, y_st + dy * 1 - dd);
            label0.Text = "";
            label1.Text = "";
            label2.Text = "";
            label3.Text = "貝茲線與控制點";
            label4.Text = "連續貝茲線與控制點";
            label5.Text = "Region - 貝茲曲線與控制點 (Region and GraphicsPath)";
            richTextBox1.Size = new Size(W - 200, H * 2 + 60);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1740, 940);
            this.Text = "vcs_MousePaint6_BezierCurve";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        // Force all threads to end.
        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            Environment.Exit(0);
        }

        //------------------------------------------------------------  # 60個

        private void pictureBox0_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox0_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox0_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox0_Paint(object sender, PaintEventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void pictureBox2_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox2_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox2_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void pictureBox3_MouseDown(object sender, MouseEventArgs e)
        {
            // 端點或控制點 是否被點選到
            for (int i = 0; i <= mpList3.Count - 1; i++)
            {
                if (mpList3[i].CheckSelected(e.X, e.Y))
                {
                    mp_Selected3 = i;
                    dragging3 = true;
                    break;
                }
            }
        }

        private void pictureBox3_MouseMove(object sender, MouseEventArgs e)
        {
            if (dragging3) // 移動端點或控制點
            {
                mpList3[mp_Selected3].Move(e.X, e.Y);
                this.pictureBox3.Invalidate();
            }
        }

        private void pictureBox3_MouseUp(object sender, MouseEventArgs e)
        {
            // 解除 端點或控制點 的點選狀況
            mp_Selected3 = -1;
            dragging3 = false;
        }

        private void pictureBox3_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawBezier(penRed, mpList3[0].p, mpList3[1].p, mpList3[2].p, mpList3[3].p);

            //繪出切線
            e.Graphics.DrawLine(Pens.Black, mpList3[0].p, mpList3[1].p);
            e.Graphics.DrawLine(Pens.Black, mpList3[2].p, mpList3[3].p);

            //繪出 端點和控制點
            e.Graphics.DrawEllipse(Pens.Black, mpList3[0].p.X - 10, mpList3[0].p.Y - 10, 20, 20);
            e.Graphics.DrawRectangle(Pens.Black, mpList3[1].p.X - 10, mpList3[1].p.Y - 10, 20, 20);
            e.Graphics.DrawRectangle(Pens.Black, mpList3[2].p.X - 10, mpList3[2].p.Y - 10, 20, 20);
            e.Graphics.DrawEllipse(Pens.Black, mpList3[3].p.X - 10, mpList3[3].p.Y - 10, 20, 20);
        }

        private void pictureBox4_MouseDown(object sender, MouseEventArgs e)
        {
            // 端點或控制點 是否被點選到
            for (int i = 0; i <= mpList4.Count - 1; i++)
            {
                if (mpList4[i].CheckSelected(e.X, e.Y))
                {
                    mp_Selected4 = i;
                    dragging4 = true;
                    break;
                }
            }
        }

        private void pictureBox4_MouseMove(object sender, MouseEventArgs e)
        {
            if (dragging4) // 移動端點或控制點
            {
                mpList4[mp_Selected4].Move(e.X, e.Y);
                this.pictureBox4.Invalidate();
            }
        }

        private void pictureBox4_MouseUp(object sender, MouseEventArgs e)
        {
            // 解除 端點或控制點 的點選狀況
            mp_Selected4 = -1;
            dragging4 = false;
        }

        private void pictureBox4_Paint(object sender, PaintEventArgs e)
        {
            Point[] mpArray = new Point[7];
            for (int i = 0; i <= mpList4.Count - 1; i++)
            {
                mpArray[i] = mpList4[i].p;
            }
            e.Graphics.DrawBeziers(penRed, mpArray);

            //繪出切線
            e.Graphics.DrawLine(Pens.Black, mpList4[0].p, mpList4[1].p);
            e.Graphics.DrawLine(Pens.Black, mpList4[2].p, mpList4[3].p);

            e.Graphics.DrawLine(Pens.Black, mpList4[3].p, mpList4[4].p);
            e.Graphics.DrawLine(Pens.Black, mpList4[5].p, mpList4[6].p);

            //繪出 端點和控制點
            e.Graphics.DrawEllipse(Pens.Black, mpList4[0].p.X - 10, mpList4[0].p.Y - 10, 20, 20);
            e.Graphics.DrawRectangle(Pens.Black, mpList4[1].p.X - 10, mpList4[1].p.Y - 10, 20, 20);
            e.Graphics.DrawRectangle(Pens.Black, mpList4[2].p.X - 10, mpList4[2].p.Y - 10, 20, 20);
            e.Graphics.DrawEllipse(Pens.Black, mpList4[3].p.X - 10, mpList4[3].p.Y - 10, 20, 20);
            e.Graphics.DrawRectangle(Pens.Black, mpList4[4].p.X - 10, mpList4[4].p.Y - 10, 20, 20);
            e.Graphics.DrawRectangle(Pens.Black, mpList4[5].p.X - 10, mpList4[5].p.Y - 10, 20, 20);
            e.Graphics.DrawEllipse(Pens.Black, mpList4[6].p.X - 10, mpList4[6].p.Y - 10, 20, 20);
        }

        private void pictureBox5_MouseDown(object sender, MouseEventArgs e)
        {
            // 端點或控制點 是否被點選到
            for (int i = 0; i <= mpList5.Count - 1; i++)
            {
                if (mpList5[i].CheckSelected(e.X, e.Y))
                {
                    mp_Selected5 = i;
                    dragging5 = true;
                    break;
                }
            }
        }

        private void pictureBox5_MouseMove(object sender, MouseEventArgs e)
        {
            if (dragging5) // 移動端點或控制點
            {
                mpList5[mp_Selected5].Move(e.X, e.Y);
                this.pictureBox5.Invalidate();
            }
        }

        private void pictureBox5_MouseUp(object sender, MouseEventArgs e)
        {
            // 解除 端點或控制點 的點選狀況
            mp_Selected5 = -1;
            dragging5 = false;
        }

        private void pictureBox5_Paint(object sender, PaintEventArgs e)
        {
            GraphicsPath gp = new GraphicsPath(); // 圖形軌跡物件

            //加入 兩條切線
            gp.AddLine(mpList5[0].p, mpList5[1].p);
            gp.CloseFigure(); // 關閉目前的圖形

            gp.AddLine(mpList5[2].p, mpList5[3].p);
            gp.CloseFigure(); // 關閉目前的圖形

            //加入 兩個端點 和 兩個控制點
            gp.AddEllipse(mpList5[0].p.X - 10, mpList5[0].p.Y - 10, 20, 20);
            Rectangle rect1, rect2;
            rect1 = new Rectangle(mpList5[1].p.X - 10, mpList5[1].p.Y - 10, 20, 20);
            rect2 = new Rectangle(mpList5[2].p.X - 10, mpList5[2].p.Y - 10, 20, 20);
            gp.AddRectangle(rect1);
            gp.AddRectangle(rect2);
            gp.AddEllipse(mpList5[3].p.X - 10, mpList5[3].p.Y - 10, 20, 20);

            // 只含貝茲曲線 的 GraphicsPath圖形軌跡物件
            GraphicsPath gp2 = new GraphicsPath(); // 圖形軌跡物件
            gp2.AddBezier(mpList5[0].p, mpList5[1].p, mpList5[2].p, mpList5[3].p);
            Region r1 = new Region(gp2); // 新增 區域表面 物件
            e.Graphics.FillRegion(Brushes.Yellow, r1); // 區域表面 繪出

            gp.AddPath(gp2, false); // 將 gp2 加入 gp 中
            e.Graphics.DrawPath(Pens.Black, gp); // 圖形軌跡 繪出
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/

