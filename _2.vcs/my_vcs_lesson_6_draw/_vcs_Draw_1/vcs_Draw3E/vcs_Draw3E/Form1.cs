using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//using System.Drawing.Drawing2D; //for SmoothingMode, PixelOffsetMode
//using System.Drawing.Text;      //for TextRenderingHint
//using System.IO;                //for File

namespace vcs_Draw3E
{
    public partial class Form1 : Form
    {
        int W = 250;
        int H = 250;

        float Tension0 = 0; // 張力 0 ~ 1
        float Tension = 0; // 張力 0 ~ 1
        float Tension_D = 0.05f; // 張力增減值

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
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
            pictureBox11.Size = new Size(W, H);
            pictureBox12.Size = new Size(W, H);
            pictureBox13.Size = new Size(W, H);
            pictureBox14.Size = new Size(W, H);

            x_st = 10;
            y_st = 30;
            dx = W + 40;
            dy = H + 50;

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
            int dd = 26;
            label0.Location = new Point(x_st + dx * 0, y_st + dy * 0 - dd);
            label1.Location = new Point(x_st + dx * 1, y_st + dy * 0 - dd);
            label2.Location = new Point(x_st + dx * 2, y_st + dy * 0 - dd);
            label3.Location = new Point(x_st + dx * 3, y_st + dy * 0 - dd);
            label4.Location = new Point(x_st + dx * 4, y_st + dy * 0 - dd);
            label5.Location = new Point(x_st + dx * 0, y_st + dy * 1 - dd);
            label6.Location = new Point(x_st + dx * 1, y_st + dy * 1 - dd);
            label7.Location = new Point(x_st + dx * 2, y_st + dy * 1 - dd);
            label8.Location = new Point(x_st + dx * 3, y_st + dy * 1 - dd);
            label9.Location = new Point(x_st + dx * 4, y_st + dy * 1 - dd);
            label10.Location = new Point(x_st + dx * 0, y_st + dy * 2 - dd);
            label11.Location = new Point(x_st + dx * 1, y_st + dy * 2 - dd);
            label12.Location = new Point(x_st + dx * 2, y_st + dy * 2 - dd);
            label13.Location = new Point(x_st + dx * 3, y_st + dy * 2 - dd);
            label14.Location = new Point(x_st + dx * 4, y_st + dy * 2 - dd);
            label0.Text = "畫曲線 DrawCurve";
            label1.Text = "畫曲線 DrawCurve 跳動";
            label2.Text = "";
            label3.Text = "";
            label4.Text = "";
            label5.Text = "";
            label6.Text = "";
            label7.Text = "";
            label8.Text = "";
            label9.Text = "";
            label10.Text = "";
            label11.Text = "";
            label12.Text = "";
            label13.Text = "";
            label14.Text = "";

            richTextBox1.Size = new Size(W, H * 3 + 100);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1740, 940);
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

        private void pictureBox0_Paint(object sender, PaintEventArgs e)
        {
            label0.Text = "DrawCurve： 張力 = " + Tension0.ToString();

            int Cx = 100;  // 基準點
            int Cy = 200;
            int D = 60; // 偏移值

            Point[] pt = new Point[4]; // 定義 四個點
            pt[0] = new Point(Cx - D, Cy + D);
            pt[1] = new Point(Cx - D, Cy - D);
            pt[2] = new Point(Cx + D, Cy - D);
            pt[3] = new Point(Cx + D, Cy + D);

            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            e.Graphics.DrawCurve(Pens.Black, pt, Tension0);  // 曲線的繪出

            for (int i = 0; i < pt.Length; i++) // 控制點的繪出
            {
                e.Graphics.DrawEllipse(Pens.Black, pt[i].X - 2, pt[i].Y - 2, 4, 4);
            }

            //------------------------------------------------------------  # 60個

            //this.Text = "畫封閉的曲線  DrawClosedCurve： 張力 = " + Tension0.ToString();
            //int Cx = 300;  // 基準點
            //int Cy = 200;
            Cx += 200;

            //int D = 60; // 偏移值

            //Point[] pt = new Point[4]; // 定義 四個點
            pt[0] = new Point(Cx - D, Cy + D);
            pt[1] = new Point(Cx - D, Cy - D);
            pt[2] = new Point(Cx + D, Cy - D);
            pt[3] = new Point(Cx + D, Cy + D);

            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            e.Graphics.DrawClosedCurve(Pens.Black, pt, Tension0, System.Drawing.Drawing2D.FillMode.Alternate);  // 曲線的繪出

            for (int i = 0; i < pt.Length; i++) // 控制點的繪出
            {
                e.Graphics.DrawEllipse(Pens.Black, pt[i].X - 2, pt[i].Y - 2, 4, 4);
            }
        }

        private void timer0_Tick(object sender, EventArgs e)
        {
            Tension0 += 0.1f;
            if (Tension0 > 1.0)
            {
                Tension0 = 0;
            }
            this.pictureBox0.Invalidate();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            Point[] pt = new Point[3]; // 定義 三個點
            pt[0] = new Point(100, this.pictureBox1.ClientSize.Height / 2);
            //pt[1] = new Point(300, 100);
            pt[2] = new Point(this.pictureBox1.ClientSize.Width - 100, this.pictureBox1.ClientSize.Height / 2);

            for (int i = 0; i < this.pictureBox1.ClientSize.Height; i = i + 10)
            {
                pt[1] = new Point(this.pictureBox1.ClientSize.Width / 2, i);
                e.Graphics.DrawCurve(Pens.Black, pt, Tension); // 曲線的繪出
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Tension = Tension + Tension_D; // 調整張力
            if (Tension >= 2 || Tension <= -1)
            {
                Tension_D = -Tension_D;
            }
            this.pictureBox1.Invalidate();
        }

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
        }


        private void pictureBox3_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer3_Tick(object sender, EventArgs e)
        {
        }

        private void pictureBox4_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer4_Tick(object sender, EventArgs e)
        {
        }

        private void pictureBox5_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer5_Tick(object sender, EventArgs e)
        {
        }

        private void pictureBox6_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer6_Tick(object sender, EventArgs e)
        {
        }


        private void pictureBox7_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer7_Tick(object sender, EventArgs e)
        {
        }


        private void pictureBox8_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer8_Tick(object sender, EventArgs e)
        {
        }


        private void pictureBox9_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer9_Tick(object sender, EventArgs e)
        {
        }

        private void pictureBox10_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer10_Tick(object sender, EventArgs e)
        {
        }

        private void pictureBox11_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer11_Tick(object sender, EventArgs e)
        {
        }

        private void pictureBox12_Paint(object sender, PaintEventArgs e)
        {

        }

        private void timer12_Tick(object sender, EventArgs e)
        {
        }

        private void pictureBox13_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer13_Tick(object sender, EventArgs e)
        {
        }


        private void pictureBox14_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer14_Tick(object sender, EventArgs e)
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


