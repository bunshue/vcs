using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for SmoothingMode

namespace vcs_Clock_All
{
    public partial class Form1 : Form
    {
        //pictureBox0 ST
        Bitmap bmp0;
        Graphics g0;

        //int WIDTH = 150, HEIGHT = 150;
        int WIDTH = 250, HEIGHT = 250;
        int hrHAND = 40;//時針
        int minHAND = 55;//分針
        int secHAND = 70;//秒針

        //center
        int cx;
        int cy;
        //pictureBox0 SP

        //pictureBox3 ST
        const int s_pinlen = 100;//秒針長度
        const int m_pinlen = 75; //分針長度
        const int h_pinlen = 75; //時針長度
        PointF center = new PointF(s_pinlen + 3, s_pinlen + 3);//中心點位置
        SolidBrush sb = new SolidBrush(Color.Black);//時鐘圓心的刷子
        //pictureBox3 SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            this.DoubleBuffered = true;//避免閃爍

            //pictureBox0 ST
            //中心
            cx = WIDTH / 2;
            cy = HEIGHT / 2;

            //時針
            hrHAND = 40 * WIDTH / 150;

            //分針
            minHAND = 55 * WIDTH / 150;

            //秒針
            secHAND = 70 * WIDTH / 150;

            pictureBox0.Size = new Size(WIDTH + 50, HEIGHT + 50);
            pictureBox0.BackColor = Color.Pink;

            //create bitmap
            bmp0 = new Bitmap(WIDTH + 1, HEIGHT + 1);

            timer0_Tick(sender, e);
            //pictureBox0 SP

            //pictureBox3 ST


            //pictureBox3 SP
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
            label3.Text = "";
            label4.Text = "";
            label5.Text = "";
            richTextBox1.Size = new Size(W - 200, H * 2 + 60);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            this.Size = new Size(1740, 940);
            this.Text = "vcs_Clock_All";
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
            Graphics g = e.Graphics;      //定义g为该窗体控件的画布
            // Graphics g = this.CreateGraphics(); //避免使用此方法，会出现闪烁

            //解决闪烁
            //方法二  占用内存
            //SetStyle(ControlStyles.UserPaint, true);
            //SetStyle(ControlStyles.AllPaintingInWmPaint, true); // 禁止擦除背景.
            //SetStyle(ControlStyles.DoubleBuffer, true); // 双缓冲

            //方法三  占用CPU
            //this.SetStyle(ControlStyles.DoubleBuffer | ControlStyles.UserPaint | ControlStyles.AllPaintingInWmPaint, true);
            //this.UpdateStyles();
            // 绘制数字时钟
            int ss = DateTime.Now.Second;
            int mm = DateTime.Now.Minute;
            int hh = DateTime.Now.Hour;
            this.Text = DateTime.Now.ToString("hh:mm:ss");

            //绘制圆形轮廓
            g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;//使画出的指针更平滑、高质量

            int cx = 150;
            int cy = 150;
            int r = 100;

            g.FillEllipse(Brushes.White, cx - r, cy - r, r * 2, r * 2);

            g.DrawEllipse(new Pen(Color.Red, 2), cx - r - 4, cy - r - 4, r * 2 + 8, r * 2 + 8);
            g.DrawEllipse(new Pen(Color.DarkGray, 1), cx - r, cy - r, r * 2, r * 2);
            //绘制数字刻度
            g.ResetTransform();
            g.TranslateTransform(cx, cy);  //重新定位坐标
            Font drawFont = new Font("Arial", 12);
            SolidBrush drawBrush = new SolidBrush(Color.Black);
            //e.Graphics.DrawString("1", drawFont, drawBrush, 30, -70);
            //e.Graphics.DrawString("2", drawFont, drawBrush, 60, -50);
            //e.Graphics.DrawString("5", drawFont, drawBrush, 30, 60);
            //e.Graphics.DrawString("4", drawFont, drawBrush, 65, 30);
            e.Graphics.DrawString("6", drawFont, drawBrush, -7, 70);
            e.Graphics.DrawString("12", drawFont, drawBrush, -9, -80);
            e.Graphics.DrawString("3", drawFont, drawBrush, 70, -7);
            e.Graphics.DrawString("9", drawFont, drawBrush, -80, -7);
            //绘制刻度
            for (int z = 0; z < 60; z++)
            {
                g.ResetTransform();
                g.TranslateTransform(cx, cy); //更改坐标原点
                g.RotateTransform(z * 6);  //旋转，每一秒旋转6度 
                if (z % 5 == 0)
                    g.DrawLine(new Pen(Color.Black, 3.0f), r - 12, 0, r - 5, 0);//小时刻度             
                else
                    g.DrawLine(new Pen(Color.Black, 1.5f), r - 8, 0, r - 5, 0);//分钟标准刻度
            }
            //绘制秒针
            g.ResetTransform();    //恢复默认状态
            g.TranslateTransform(cx, cy);
            g.RotateTransform(ss * 6 + 270);   //以水平线为x轴，从垂直上方开始旋转，每次旋转6度。     
            Pen secPen = new Pen(Color.Red, 1);
            secPen.StartCap = System.Drawing.Drawing2D.LineCap.RoundAnchor; //画线，从圆点开始   
            secPen.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;//画线，结束于箭头
            g.DrawLine(secPen, 0, 0, 65, 0);//65表示线的长度           
            //绘制分针
            g.ResetTransform();
            g.TranslateTransform(cx, cy);
            g.RotateTransform(mm * 6 + 270);
            Pen minPen = new Pen(Color.Blue, 2);
            minPen.StartCap = System.Drawing.Drawing2D.LineCap.RoundAnchor;
            minPen.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;
            g.DrawLine(minPen, 0, 0, 50, 0);
            //绘制时针
            g.ResetTransform();
            g.TranslateTransform(cx, cy);
            g.RotateTransform(hh * 30 + mm * 1 / 2 + 270);
            Pen hourPen = new Pen(Color.Black, 3);
            hourPen.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;
            g.DrawLine(hourPen, 0, 0, 35, 0);
        }

        private void pictureBox2_MouseClick(object sender, MouseEventArgs e)
        {
        }

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

        private void pictureBox3_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox3_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox3_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox3_Paint(object sender, PaintEventArgs e)
        {
        }

        private void pictureBox4_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox4_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox4_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox4_Paint(object sender, PaintEventArgs e)
        {
        }

        private void pictureBox5_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox5_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox5_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox5_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer0_Tick(object sender, EventArgs e)
        {
            //create graphics
            g0 = Graphics.FromImage(bmp0);

            //get time
            int ms = DateTime.Now.Millisecond;
            int ss = DateTime.Now.Second;
            int mm = DateTime.Now.Minute;
            int hh = DateTime.Now.Hour;

            int[] handCoord = new int[2];
            float[] handCoordf = new float[2];

            //clear
            g0.Clear(Color.White);

            g0.DrawRectangle(Pens.Red, 0, 0, WIDTH / 2, HEIGHT / 2);

            //draw circle
            g0.DrawEllipse(new Pen(Color.Black, 1f), 0, 0, WIDTH, HEIGHT);

            //draw figure
            g0.DrawString("12", new Font("Arial", 12), Brushes.Black, new PointF(64 * WIDTH / 150, 1 * HEIGHT / 150));
            g0.DrawString("3", new Font("Arial", 12), Brushes.Black, new PointF(138 * WIDTH / 150, 68 * HEIGHT / 150));
            g0.DrawString("6", new Font("Arial", 12), Brushes.Black, new PointF(68 * WIDTH / 150, 133 * HEIGHT / 150));
            g0.DrawString("9", new Font("Arial", 12), Brushes.Black, new PointF(0 * WIDTH / 150, 68 * HEIGHT / 150));

            //second hand
            //handCoord = msCoord(ss, secHAND); //old
            handCoordf = msCoordf(ss, ms, secHAND);
            //g0.DrawLine(new Pen(Color.Red, 1f), new Point(cx, cy), new Point(handCoord[0], handCoord[1])); //old
            g0.DrawLine(new Pen(Color.Red, 1f), new Point(cx, cy), new Point((int)handCoordf[0], (int)handCoordf[1]));
            //richTextBox1.Text += "(" + (handCoordf[0] - cx).ToString() + ", " + (handCoordf[1] - cy).ToString() + ")\n";

            //minute hand
            handCoord = msCoord(mm, minHAND);
            g0.DrawLine(new Pen(Color.Black, 2f), new Point(cx, cy), new Point(handCoord[0], handCoord[1]));

            //hour hand
            handCoord = hrCoord(hh % 12, mm, hrHAND);
            g0.DrawLine(new Pen(Color.Gray, 3f), new Point(cx, cy), new Point(handCoord[0], handCoord[1]));

            pictureBox0.Image = bmp0;

            g0.Dispose();
        }

        //coord for minute and second hand
        private int[] msCoord(int val, int hlen)
        {
            int[] coord = new int[2];
            val *= 6;   //each minute and second make 6 degree

            if (val >= 0 && val <= 180)
            {
                coord[0] = cx + (int)(hlen * Math.Sin(Math.PI * val / 180));
                coord[1] = cy - (int)(hlen * Math.Cos(Math.PI * val / 180));
            }
            else
            {
                coord[0] = cx - (int)(hlen * -Math.Sin(Math.PI * val / 180));
                coord[1] = cy - (int)(hlen * Math.Cos(Math.PI * val / 180));
            }
            return coord;
        }

        //coord for minute and second hand
        private float[] msCoordf(int val1, int val2, int hlen)
        {
            float[] coord = new float[2];
            if (hlen == 70 * WIDTH / 150)
            {
                //richTextBox1.Text += "sec val = " + val.ToString() + "\t";
            }
            float val;
            val = (float)val1 + (float)val2 / 1000;

            val *= 6;   //each minute and second make 6 degree

            if (val >= 0 && val <= 180)
            {
                coord[0] = cx + (float)(hlen * Math.Sin(Math.PI * val / 180));
                coord[1] = cy - (float)(hlen * Math.Cos(Math.PI * val / 180));
                if (hlen == 70 * WIDTH / 150)
                {
                    //richTextBox1.Text += "111 sec val = " + val.ToString() + "coord[0] = " + coord[0].ToString() + " coord[1] = " + coord[1].ToString() + "\t";
                }
            }
            else
            {
                coord[0] = cx - (float)(hlen * -Math.Sin(Math.PI * val / 180));
                coord[1] = cy - (float)(hlen * Math.Cos(Math.PI * val / 180));
                if (hlen == 70 * WIDTH / 150)
                {
                    //richTextBox1.Text += "222 sec val = " + val.ToString() + "coord[0] = " + coord[0].ToString() + " coord[1] = " + coord[1].ToString() + "\t";
                }
            }
            return coord;
        }

        //coord for hour hand
        private int[] hrCoord(int hval, int mval, int hlen)
        {
            int[] coord = new int[2];

            //each hour makes 30 degree
            //each min makes 0.5 degree
            int val = (int)((hval * 30) + (mval * 0.5));

            if (val >= 0 && val <= 180)
            {
                coord[0] = cx + (int)(hlen * Math.Sin(Math.PI * val / 180));
                coord[1] = cy - (int)(hlen * Math.Cos(Math.PI * val / 180));
            }
            else
            {
                coord[0] = cx - (int)(hlen * -Math.Sin(Math.PI * val / 180));
                coord[1] = cy - (int)(hlen * Math.Cos(Math.PI * val / 180));
            }
            return coord;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.pictureBox1.Invalidate();
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            int hh = DateTime.Now.Hour;
            int mm = DateTime.Now.Minute;
            int ss = DateTime.Now.Second;
            myClock2(hh, mm, ss);
        }

        private void myClock2(int hh, int mm, int ss)
        {
            int h_pinlen = 50;//時針            
            int m_pinlen = 75;//分針
            int s_pinlen = 100;//秒針            

            Graphics g = pictureBox2.CreateGraphics();
            g.Clear(Color.White);
            Pen p = new Pen(Color.Black, 1);
            g.DrawEllipse(p, pictureBox2.ClientRectangle);
            Point CPoint = new Point(pictureBox2.ClientRectangle.Width / 2, pictureBox2.ClientRectangle.Height / 2);
            Point SPoint = new Point((int)(CPoint.X + (Math.Sin(6 * ss * Math.PI / 180)) * s_pinlen), (int)(CPoint.Y - (Math.Cos(6 * ss * Math.PI / 180)) * s_pinlen));
            Point MPoint = new Point((int)(CPoint.X + (Math.Sin(6 * mm * Math.PI / 180)) * m_pinlen), (int)(CPoint.Y - (Math.Cos(6 * mm * Math.PI / 180)) * m_pinlen));
            Point HPoint = new Point((int)(CPoint.X + (Math.Sin(((30 * hh) + (mm / 2)) * Math.PI / 180)) * h_pinlen), (int)(CPoint.Y - (Math.Cos(((30 * hh) + (mm / 2)) * Math.PI / 180)) * h_pinlen));
            g.DrawLine(p, CPoint, SPoint);
            p = new Pen(Color.Black, 2);
            g.DrawLine(p, CPoint, MPoint);
            p = new Pen(Color.Black, 4);
            g.DrawLine(p, CPoint, HPoint);
        }


        private void timer3_Tick(object sender, EventArgs e)
        {
            int h = DateTime.Now.Hour;
            int m = DateTime.Now.Minute;
            int s = DateTime.Now.Second;
            myClock3(h, m, s);//調用畫時鐘表的方法
        }

        //　　方法AngleToPos是根據角度和百分比計算出一個點的坐標函數
        PointF AngleToPos(int angle, float percent)
        {
            PointF pos = new PointF();
            double radian = angle * Math.PI / 180;
            pos.Y = center.Y - s_pinlen * percent * (float)Math.Sin(radian);
            pos.X = center.X + s_pinlen * percent * (float)Math.Cos(radian);
            return pos;
        }

        void myClock3(int h, int m, int s)
        {
            Pen pDisk = new Pen(Color.Orange, 3);//時鐘背景的筆
            Pen pScale = new Pen(Color.Coral);//刻度的筆
            Graphics g = pictureBox3.CreateGraphics();
            g.Clear(Color.White);
            Pen p = new Pen(Color.Black, 2);
            Point CPoint = new Point(s_pinlen, s_pinlen);
            Point SPoint = new Point((int)(CPoint.X + (Math.Sin(6 * s * Math.PI / 180)) * s_pinlen), (int)(CPoint.Y - (Math.Cos(6 * s * Math.PI / 180)) * s_pinlen));
            Point MPoint = new Point((int)(CPoint.X + (Math.Sin(6 * m * Math.PI / 180)) * m_pinlen), (int)(CPoint.Y - (Math.Cos(6 * m * Math.PI / 180)) * m_pinlen));
            Point HPoint = new Point((int)(CPoint.X + (Math.Sin(((30 * h) + (m / 2)) * Math.PI / 180)) * h_pinlen), (int)(CPoint.Y - (Math.Cos(((30 * h) + (m / 2)) * Math.PI / 180)) * h_pinlen));
            g.FillEllipse(sb, center.X - 8, center.Y - 7, 14, 14);
            g.DrawLine(p, CPoint, SPoint);
            p = new Pen(Color.Blue, 4);
            g.DrawLine(p, CPoint, MPoint);
            p = new Pen(Color.Green, 6);
            g.DrawLine(p, CPoint, HPoint);
            g.DrawEllipse(pDisk, 1, 1, s_pinlen * 2, s_pinlen * 2);//畫刻度
            for (int i = 0; i < 360; i += 6)
            {
                Pen tempPen = (i % 30 == 0) ? pDisk : pScale;
                PointF qidian = AngleToPos(i, 0.87f);
                PointF zhongdian = AngleToPos(i, 1.0f);
                g.DrawLine(tempPen, qidian, zhongdian);
            }
        }

        private void timer4_Tick(object sender, EventArgs e)
        {

        }

        private void timer5_Tick(object sender, EventArgs e)
        {

        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

*/
