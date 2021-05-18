using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for SmoothingMode
using System.Drawing.Text;      //for TextRenderingHint
using System.IO;                //for File

namespace vcs_Draw3C
{
    public partial class Form1 : Form
    {
        int W = 250;
        int H = 250;

        //數字 8 雙扭線 (Lemniscate of Bernoulli) ST
        G2D_LemniscateOfBernoulli lob;

        int angle0 = 0; // 數字 8 曲線公式的參數值(角度 0 ~ 359)

        int cx0, cy0;  // 中心點
        int radius0; // 半徑
        //數字 8 雙扭線 (Lemniscate of Bernoulli) SP

        //Maurer Rose 玫瑰線 ST
        double rose_x0, rose_y0, rose_x1, rose_y1;
        float k_rose = 2;  // 係數
        float d_rose = 29; // 係數
        //Maurer Rose 玫瑰線 SP

        //picturebox11 蝴蝶曲線 Butterfly curve ST
        double butterfly_x0, butterfly_y0, butterfly_x1, butterfly_y1;  // 兩個點畫一直線
        int butterfly_n = 1;   // 畫幾圈 蝴蝶曲線
        //picturebox11 蝴蝶曲線 Butterfly curve SP

        //picturebox12 蝴蝶曲線 Butterfly curve ST
        G2D_Butterfly butterfly; // 蝴蝶物件
        int eX = 100;  // 蝴蝶 的目標點座標
        int eY = 100;
        //picturebox12 蝴蝶曲線 Butterfly curve SP


        //追逐滑鼠游標的蝴蝶 ST
        NPC npc;
        Point MousePos = new Point();
        //追逐滑鼠游標的蝴蝶 SP

        //漫遊演算法 ST
        GC_2D_Wander gc; // 宣告一個物件
        GC_2D_MovableCircle cir;
        //漫遊演算法 SP

        //橢圓形的軌跡 ST
        G2D_Circle_Grad cir01;
        G2D_EllipsePath ellipsePath;
        PointF center;
        float theta = 0;
        //橢圓形的軌跡 SP

        //在多點網格移動的小球 ST
        List<ClassMovingPoint> mpList = new List<ClassMovingPoint>(); // 可移動點的動態陣列
        List<int> pathList = new List<int>(); // 小球 在 可移動點動態陣列 的路徑
        int mp_Selected = -1;  // 動態陣列 的第幾個 被選到
        bool dragging = false; // 是否拖拉中

        Pen myPen = new Pen(Color.Green, 1);  // 
        int D = 10; // 小球的半徑

        BallInNet ball; // 
        //在多點網格移動的小球 SP

        //雷達圖 pictureBox6 ST
        G2D_Radar rada;
        //雷達圖 pictureBox6 SP

        //雷達圖 pictureBox7 ST
        G2D_Radar2 rada2;
        //雷達圖 pictureBox7 SP

        //直線和圓的互動 ST
        G2D_OvalLine ovalLine01;
        //直線和圓的互動 SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //數字 8 雙扭線 (Lemniscate of Bernoulli) ST
            this.pictureBox1.ClientSize = new Size(250, 250);
            cx0 = this.pictureBox1.ClientSize.Width / 2;
            cy0 = this.pictureBox1.ClientSize.Height / 2;
            radius0 = (int)(Math.Min(cx0, cy0) * 2 * 0.3);

            lob = new G2D_LemniscateOfBernoulli(radius0);
            //數字 8 雙扭線 (Lemniscate of Bernoulli) SP

            //picturebox12 蝴蝶曲線 Butterfly curve ST
            butterfly = new G2D_Butterfly(3, 30);
            //picturebox12 蝴蝶曲線 Butterfly curve SP

            //追逐滑鼠游標的蝴蝶 ST
            this.pictureBox1.KeyDown += new KeyEventHandler(pictureBox1_KeyDown);
            this.ActiveControl = this.pictureBox1;//选中pictureBox1，不然没法触发事件

            string filename1 = @"C:\______test_files\__RW\_png\butterfly.png";

            Rectangle rect = new Rectangle(0, 0, this.pictureBox1.ClientSize.Width, this.pictureBox1.ClientSize.Height);
            npc = new NPC(new Bitmap(filename1));
            npc.SetLocation(this.pictureBox1.ClientSize.Width / 2, this.pictureBox1.ClientSize.Height / 2);
            npc.SetAngle(0, -90);
            npc.SetBoundary(rect); // 設定視窗客戶區的邊界

            //追逐滑鼠游標的蝴蝶 SP

            //漫遊演算法 ST
            string filename2 = @"C:\______test_files\__RW\_png\ladybug.png";
            gc = new GC_2D_Wander(new Bitmap(filename2));
            cir = new GC_2D_MovableCircle(20, new Point(this.pictureBox2.ClientSize.Width / 2, this.pictureBox2.ClientSize.Height / 2));
            gc.Update();
            //漫遊演算法 SP

            //橢圓形的軌跡 ST
            cir01 = new G2D_Circle_Grad(128, 0.1f, Color.White);
            center = new PointF(300 / 2, 200 / 2);
            ellipsePath = new G2D_EllipsePath(center, 200 / 3, 100 / 3);
            //橢圓形的軌跡 SP

            //在多點網格移動的小球 ST

            myPen.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;

            this.ClientSize = new Size(900, 600);
            // 加入5個可移動點  當作 網格 的個頂點
            Point[] pts = new Point[5];
            int Cx, Cy;
            Cx = this.pictureBox3.ClientSize.Width / 2;
            Cy = this.pictureBox3.ClientSize.Height / 2;

            double theta = -Math.PI / 2;
            for (int i = 0; i < pts.Length; i++)
            {
                pts[i].X = (int)(Cx + 100 * Math.Cos(theta));
                pts[i].Y = (int)(Cy + 100 * Math.Sin(theta));
                theta = theta + 2 * Math.PI / pts.Length;
            }

            ClassMovingPoint mp;
            mp = new ClassMovingPoint(pts[0], 10, Color.Blue, "p0");
            mpList.Add(mp);
            mp = new ClassMovingPoint(pts[1], 10, Color.Blue, "p1");
            mpList.Add(mp);
            mp = new ClassMovingPoint(pts[2], 10, Color.Blue, "p2");
            mpList.Add(mp);
            mp = new ClassMovingPoint(pts[3], 10, Color.Blue, "p3");
            mpList.Add(mp);
            mp = new ClassMovingPoint(pts[4], 10, Color.Blue, "p4");
            mpList.Add(mp);

            pathList.Add(0);
            pathList.Add(2);
            pathList.Add(1);
            pathList.Add(3);
            pathList.Add(4);

            ball = new BallInNet(mpList, pathList,
                5,
                D,
                Color.Red);

            //在多點網格移動的小球 SP

            //雷達圖 pictureBox6 ST
            rada = new G2D_Radar(120, 120, 240);
            //雷達圖 pictureBox6 SP

            //雷達圖 pictureBox7 ST
            rada2 = new G2D_Radar2(120, 120, 240);
            //雷達圖 pictureBox7 SP

            //直線和圓的互動 ST
            int Cx2 = this.pictureBox4.ClientSize.Width / 2;
            int Cy2 = this.pictureBox4.ClientSize.Height / 2;
            ovalLine01 = new G2D_OvalLine(Cx2, Cy2, 0.01, Color.Blue);
            //直線和圓的互動 SP
        }

        void show_item_location()
        {
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);

            int x_st;
            int y_st;
            int dx;
            int dy;

            x_st = 20;
            y_st = 20;
            dx = 160;
            dy = 50;

            pictureBox0.Size = new Size(W, H);
            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox4.Size = new Size(W, H);
            pictureBox5.Size = new Size(W, H);
            pictureBox6.Size = new Size(W, H);
            pictureBox7.Size = new Size(W, H);
            pictureBox8.Size = new Size(W, H);
            pictureBox9.Size = new Size(W, H);
            pictureBox10.Size = new Size(W, H);
            pictureBox11.Size = new Size(W, H);
            pictureBox12.Size = new Size(W, H);
            pictureBox13.Size = new Size(W, H);
            pictureBox14.Size = new Size(W, H);

            x_st = 10;
            y_st = 10;
            dx = W + 70;
            dy = H + 45;

            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox4.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            pictureBox5.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox6.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox7.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            pictureBox8.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            pictureBox9.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            pictureBox10.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            pictureBox11.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            pictureBox12.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            pictureBox13.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            pictureBox14.Location = new Point(x_st + dx * 4, y_st + dy * 2);

            label3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            label4.Location = new Point(x_st + dx * 0, y_st + dy * 3 + 30);
            label1.Location = new Point(x_st + dx * 0, y_st + dy * 3 + 60);
            numericUpDown1.Location = new Point(x_st + dx * 0 + 50, y_st + dy * 3 + 60);
            button1.Location = new Point(x_st + dx * 0 + 50 + 80, y_st + dy * 3 + 60);
            label2.Location = new Point(x_st + dx * 0, y_st + dy * 3 + 90);
            numericUpDown2.Location = new Point(x_st + dx * 0 + 50, y_st + dy * 3 + 90);

            x_st = 1810;
            y_st = 80;
            dx = 120;
            dy = 50;

            richTextBox1.Location = new Point(x_st + dx * 0 - 300, y_st + dy * 12);
            richTextBox1.Size = new Size(400, 380);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();

        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
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

        //數字 8 雙扭線 (Lemniscate of Bernoulli) ST

        // http://en.wikipedia.org/wiki/Lemniscate_of_Bernoulli

        // Converting between polar and Cartesian coordinates
        // x = r cos(θ)
        // y = r sin(θ)

        private void pictureBox0_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            lob.Draw(e.Graphics, cx0, cy0);

            PointF pt = lob.GetPos(angle0, cx0, cy0);
            e.Graphics.FillEllipse(Brushes.Red, pt.X - 10, pt.Y - 10, 20, 20);

        }

        private void timer0_Tick(object sender, EventArgs e)
        {
            angle0++;
            angle0 %= 360;
            this.pictureBox0.Invalidate();
        }
        //數字 8 雙扭線 (Lemniscate of Bernoulli) SP

        //追逐滑鼠游標的蝴蝶 ST
        private void timer1_Tick(object sender, EventArgs e)
        {
            this.pictureBox1.Invalidate();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            npc.Update(MousePos);

            //npc.Turn(1);
            npc.Draw(e.Graphics);
            e.Graphics.DrawString("追逐滑鼠游標的蝴蝶", new Font("標楷體", 16), Brushes.Navy, 10, 10);
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            MousePos.X = e.X;
            MousePos.Y = e.Y;
        }

        void pictureBox1_KeyDown(object sender, KeyEventArgs e)
        {
            //加速減速功能 但在richtextbox存在下 picturebox_keydown之功能不能用
            if (e.KeyCode == Keys.Up)
            {
                richTextBox1.Text += "加速\n";
                npc.ChangeSpeed(1);
            }
            else if (e.KeyCode == Keys.Down)
            {
                richTextBox1.Text += "減速\n";
                npc.ChangeSpeed(-1);
            }
        }
        //追逐滑鼠游標的蝴蝶 SP

        //Maurer Rose 玫瑰線 ST

        // http://en.wikipedia.org/wiki/Maurer_rose
        //  Maurer rose was introduced by Peter M. Maurer in his article entitled A Rose is a Rose

        // (r, θ) = (a * sin(kθ), θ) where (θ = 0, d, 2d, 3d, ..., 360d)
        // Converting between polar and Cartesian coordinates
        // x = r cos(θ)
        // y = r sin(θ)

        private void pictureBox10_Paint(object sender, PaintEventArgs e)
        {
            // 畫布設定為較佳的輸出品質 
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            int Cx = this.pictureBox10.ClientSize.Width / 2;  // 中心點
            int Cy = this.pictureBox10.ClientSize.Height / 2;
            int a = (int)(Math.Min(Cx, Cy) * 0.9); // 半徑
            double r; // 極座標的 r
            double theta; // 極座標的θ

            for (int t = 0; t <= 360; t = t + 1)  // 361個點  = 360 條直線
            {
                rose_x0 = rose_x1; // 求該點之前 先存成為上個點
                rose_y0 = rose_y1;
                theta = t * d_rose * Math.PI / 180;
                r = a * Math.Sin(k_rose * theta);  // 極座標
                rose_x1 = r * Math.Cos(theta);  // 直角座標
                rose_y1 = r * Math.Sin(theta);
                if (t != 0)  // 第一個點不畫
                {
                    e.Graphics.DrawLine(Pens.Red, Cx + (float)rose_x0, Cy - (float)rose_y0, Cx + (float)rose_x1, Cy - (float)rose_y1);
                }
            }
        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            k_rose = (int)numericUpDown1.Value;
            this.pictureBox10.Invalidate();
        }

        private void numericUpDown2_ValueChanged(object sender, EventArgs e)
        {
            d_rose = (int)numericUpDown2.Value;
            this.pictureBox10.Invalidate();
        }

        private void timer10_Tick(object sender, EventArgs e)
        {
            k_rose++;
            if (k_rose > (int)numericUpDown1.Maximum)
            {
                k_rose = (int)numericUpDown1.Minimum;
            }
            numericUpDown1.Value = (decimal)k_rose;
            this.pictureBox10.Invalidate();

        }

        private void button1_Click(object sender, EventArgs e)
        {
            timer10.Enabled = !timer10.Enabled;
            if (timer10.Enabled)
                button1.Text = "停止";
            else
                button1.Text = "K 自動增加";

        }
        //Maurer Rose 玫瑰線 SP


        //蝴蝶曲線 Butterfly curve ST
        // http://en.wikipedia.org/wiki/Butterfly_curve_(transcendental)

        private void pictureBox11_Paint(object sender, PaintEventArgs e)
        {
            // 反鋸齒設定 -- 畫布設定為較佳的輸出品質 
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            int Cx = this.pictureBox11.ClientSize.Width / 2;  // 中心點
            int Cy = this.pictureBox11.ClientSize.Height / 2;
            double d = Math.Min(this.pictureBox11.ClientSize.Width, this.pictureBox11.ClientSize.Height) / 8.0;  // 半徑

            double t;  // 極座標的θ
            double r;  // 極座標的 r
            for (int k = 0; k <= 360 * butterfly_n; k++)
            {
                butterfly_x0 = butterfly_x1;  // 先儲存 成為上個點
                butterfly_y0 = butterfly_y1;

                // 計算該點 (極座標)
                t = k * Math.PI / 180;
                r = d * (Math.Pow(Math.E, Math.Cos(t)) - 2 * Math.Cos(4 * t) - Math.Pow(Math.Sin(t / 12), 5));

                // 轉成直角座標
                butterfly_x1 = r * Math.Sin(t);
                butterfly_y1 = r * Math.Cos(t);

                if (t != 0)  // 第一個點不畫
                {
                    e.Graphics.DrawLine(Pens.Red, Cx + (float)butterfly_x0, Cy - (float)butterfly_y0, Cx + (float)butterfly_x1, Cy - (float)butterfly_y1);
                }
            }
            e.Graphics.DrawString(butterfly_n.ToString(), new Font("標楷體", 20), Brushes.Navy, 10, pictureBox11.Height - 30);
        }

        private void timer11_Tick(object sender, EventArgs e)
        {
            butterfly_n++;
            if (butterfly_n >= 12)
                butterfly_n = 1;

            this.pictureBox11.Invalidate();
        }

        //蝴蝶曲線 Butterfly curve SP

        //picturebox12 蝴蝶曲線 Butterfly curve ST
        // http://en.wikipedia.org/wiki/Butterfly_curve_(transcendental)

        private void pictureBox12_MouseDown(object sender, MouseEventArgs e)
        {
            eX = e.X;
            eY = e.Y;
            this.pictureBox12.Invalidate();
        }

        private void pictureBox12_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            e.Graphics.FillEllipse(Brushes.Red, eX - 5, eY - 5, 10, 10); // 畫出 目標點

            butterfly.Draw(e.Graphics);  // 畫出 蝴蝶圖案
        }

        private void timer12_Tick(object sender, EventArgs e)
        {
            butterfly.Update(eX, eY);
            this.pictureBox12.Invalidate();
        }

        //picturebox12 蝴蝶曲線 Butterfly curve SP

        //漫遊演算法 ST
        private void pictureBox2_MouseDown(object sender, MouseEventArgs e)
        {
            cir.CheckSelected(e.X, e.Y);
        }

        private void pictureBox2_MouseMove(object sender, MouseEventArgs e)
        {
            cir.Update(e.X, e.Y);
        }

        private void pictureBox2_MouseUp(object sender, MouseEventArgs e)
        {
            cir.dragging = false;
        }

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.ResetTransform();
            cir.Draw(e.Graphics);
            gc.Draw(e.Graphics);
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            gc.Wander_Center = cir.pos;
            gc.Update();
            this.pictureBox2.Invalidate();
        }

        //漫遊演算法 SP

        //派形風扇 ST

        int startAngle = -10; // 開始的角度

        private void timer5_Tick(object sender, EventArgs e)
        {
            startAngle = startAngle + 1; // 更新開始的角度
            this.pictureBox5.Invalidate();
        }

        private void pictureBox5_Paint(object sender, PaintEventArgs e)
        {
            int W = pictureBox5.ClientSize.Width;
            int H = pictureBox5.ClientSize.Height;
            int cx = W / 2;
            int cy = H / 2;
            int d = (int)(Math.Min(W, H) / 2) - 10; //半徑

            for (int i = 0; i < 18; i++)
            {
                if (i % 2 == 0)  // 偶數才要繪出
                {
                    e.Graphics.DrawPie(Pens.Black, cx - d, cy - d, 2 * d, 2 * d, startAngle + i * 20, 20); // 繪出派形
                }
            }
        }

        //派形風扇 SP

        //橢圓形的軌跡 ST
        private void pictureBox9_Paint(object sender, PaintEventArgs e)
        {
            ellipsePath.Draw(e.Graphics);

            PointF p = ellipsePath.GetPath(theta);
            e.Graphics.DrawImage(cir01.bitmap, new PointF(p.X - cir01.bitmap.Width / 2, p.Y - cir01.bitmap.Height / 2));
        }

        private void timer9_Tick(object sender, EventArgs e)
        {
            theta = theta + 0.01f;
            this.pictureBox9.Invalidate();
        }
        //橢圓形的軌跡 SP


        //在多點網格移動的小球 ST

        private void pictureBox3_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            for (int i = 0; i < mpList.Count; i++)
            {
                mpList[i].Draw(e.Graphics);
            }

            for (int i = 0; i < mpList.Count - 1; i++)
            {
                for (int j = i + 1; j < mpList.Count; j++)
                {
                    e.Graphics.DrawLine(myPen, mpList[i].pos, mpList[j].pos);
                }
            }

            ball.Draw(e.Graphics);
        }

        // 檢查是哪一個點被 選到
        private void pictureBox3_MouseDown(object sender, MouseEventArgs e)
        {
            for (int i = 0; i <= mpList.Count - 1; i++)
            {
                if (mpList[i].CheckSelected(e.X, e.Y))
                {
                    mp_Selected = i;
                    dragging = true;
                    break;
                }
            }
        }

        // 更新 被選到的點 的座標
        private void pictureBox3_MouseMove(object sender, MouseEventArgs e)
        {
            if (dragging)
            {
                mpList[mp_Selected].Move(e.X, e.Y);

                this.Invalidate();
                this.pictureBox3.Invalidate();
            }
        }

        // 解除 被選到的點
        private void pictureBox3_MouseUp(object sender, MouseEventArgs e)
        {
            mp_Selected = -1;
            dragging = false;

        }

        private void timer3_Tick(object sender, EventArgs e)
        {
            ball.Update();
            this.pictureBox3.Invalidate();
        }
        //在多點網格移動的小球 SP





        //雷達圖 pictureBox6 ST
        private void timer6_Tick(object sender, EventArgs e)
        {
            this.pictureBox6.Invalidate();

        }

        private void pictureBox6_Paint(object sender, PaintEventArgs e)
        {
            rada.Draw(e.Graphics);

        }

        //雷達圖 pictureBox6 SP

        //雷達圖 pictureBox7 ST
        private void pictureBox7_Paint(object sender, PaintEventArgs e)
        {
            rada2.Draw(e.Graphics);
        }

        private void timer7_Tick(object sender, EventArgs e)
        {
            this.pictureBox7.Invalidate();
        }
        //雷達圖 pictureBox7 SP


        //直線和圓的互動 ST
        private void timer4_Tick(object sender, EventArgs e)
        {
            ovalLine01.Update();
            this.pictureBox4.Invalidate();
        }

        private void pictureBox4_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            ovalLine01.Draw(e.Graphics);
        }
        //直線和圓的互動 SP

        int heart_type = 0;

        private void timer14_Tick(object sender, EventArgs e)
        {
            this.pictureBox14.Invalidate();
            heart_type++;
            if (heart_type > 4)
                heart_type = 0;
        }

        private void pictureBox14_Paint(object sender, PaintEventArgs e)
        {
            //GraphicsPath - FillPath() 心形

            GraphicsPath gp = new GraphicsPath();
            int Cx = this.pictureBox14.ClientSize.Width / 2; // 視窗客戶區的中心點
            int Cy = this.pictureBox14.ClientSize.Height / 2;

            int D = 20;    // 每格 寬
            int x = Cx;    // 心臟的起始點
            int y = Cy - 2 * D;

            //心臟右邊的曲線 由上往下
            PointF[] pt = new PointF[]{
                          new PointF(x, y),
                          new PointF(x+3*D, y - 1.5f*D),
                          new PointF(x+5*D, y),
                          new PointF(x+4*D, y+3*D),
                          new PointF(x, y+ 7 *D),
                          };
            gp.AddCurve(pt, 0.6f);

            //心臟左邊的曲線 順時間方向 由下往上 定義點的座標
            PointF[] pt2 = new PointF[]{
                          new PointF(x, y+ 7 *D),
                          new PointF(x-4*D, y+3*D),
                          new PointF(x-5*D, y),
                          new PointF(x-3*D, y - 1.5f*D),
                          new PointF(x, y),
                          };
            gp.AddCurve(pt2, 0.6f);


            if (heart_type == 0)
            {
                //空心
            }
            else if (heart_type == 1)   //單色塗刷
            {
                e.Graphics.FillPath(Brushes.Red, gp); // 填滿形狀區域 //SolidBrush - Red
            }
            else if (heart_type == 2)   //樣式塗刷一
            {
                HatchBrush myBrush1 = new HatchBrush(HatchStyle.DiagonalCross, Color.Yellow, Color.Blue);   //HatchBrush - DiagonalCross
                e.Graphics.FillPath(myBrush1, gp); //填滿形狀區域
            }
            else if (heart_type == 3)   //樣式塗刷二
            {
                HatchBrush myBrush2 = new HatchBrush(HatchStyle.SolidDiamond, Color.Yellow, Color.Blue);    //HatchBrush - SolidDiamond
                e.Graphics.FillPath(myBrush2, gp); //填滿形狀區域
            }
            else if (heart_type == 4)   //使用圖形塗刷
            {
                Bitmap bm = new Bitmap(Properties.Resources.Butterfly);
                TextureBrush myBrush3 = new TextureBrush(bm);  // 圖形塗刷  //TextureBrush
                e.Graphics.FillPath(myBrush3, gp); //填滿形狀區域
            }
            e.Graphics.DrawPath(Pens.Black, gp); //繪出圖形軌跡



        }

    }
}

