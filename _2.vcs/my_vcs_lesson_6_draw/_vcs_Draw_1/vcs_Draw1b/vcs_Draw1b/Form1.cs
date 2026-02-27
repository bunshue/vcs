using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_Draw1b
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.Size = new Size(1200, 860);
            this.Text = "vcs_Draw1b";
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((1920 - this.Size.Width) / 2, (1080 - this.Size.Height) / 2);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            Pen pen = new Pen(Color.Black, 1);

            draw_grid(g);

            Font f_index = new Font("Arial", 80, FontStyle.Bold);
            SolidBrush sb = new SolidBrush(Color.FromArgb(128, 255, 0, 0));

            int x_center = 110;
            int y_center = 120;
            g.DrawString("1", f_index, sb, new PointF(x_center, y_center));
            g.DrawRectangle(Pens.Red, x_center, y_center, 100, 100);

            double radius = 100;

            double[] x = new double[10];
            double[] y = new double[10];

            for (int i = 0; i <= 9; i++)
            {
                x[i] = x_center + radius * Math.Sin(36 * i * Math.PI / 180.0);
                y[i] = y_center + radius * Math.Cos(36 * i * Math.PI / 180);
            }

            for (int i = 0; i <= 9; i++)
            {
                for (int j = 0; j <= 9; j++)
                {
                    g.DrawLine(pen, (int)x[i], (int)y[i], (int)x[j], (int)y[j]);
                }
            }

            //------------------------------------------------------------  # 60個

            double xx;
            double yy;
            Point[] pts = new Point[100];

            x_center = 380;
            y_center = 120;
            g.DrawString("2", f_index, sb, new PointF(x_center, y_center));
            g.DrawRectangle(Pens.Red, x_center, y_center, 100, 100);

            radius = 100;

            for (int i = 0; i <= 99; i++)
            {
                xx = x_center + radius * Math.Sin(36 * i * Math.PI / 180);
                yy = y_center + radius * Math.Cos(36 * i * Math.PI / 180);
                pts[i] = new Point((int)xx, (int)yy);
                radius -= 1;
            }
            g.DrawLines(pen, pts);

            //------------------------------------------------------------  # 60個

            HatchBrush hatchBrush1;
            Single p1, p2, p3;
            int x_st = 500;
            int y_st = 0;

            g.DrawString("3", f_index, sb, new PointF(x_st, y_st));
            g.DrawRectangle(Pens.Red, x_st, y_st, 100, 100);

            p1 = 180;
            p2 = 125;
            p3 = 160;

            hatchBrush1 = new HatchBrush(HatchStyle.DashedDownwardDiagonal, Color.White, Color.Red);
            g.FillRectangle(hatchBrush1, x_st + 70, y_st + 250 - p1, 30, p1);

            hatchBrush1 = new HatchBrush(HatchStyle.DarkUpwardDiagonal, Color.White, Color.Blue);
            g.FillRectangle(hatchBrush1, x_st + 120, y_st + 250 - p2, 30, p2);

            hatchBrush1 = new HatchBrush(HatchStyle.DiagonalCross, Color.White, Color.Green);
            g.FillRectangle(hatchBrush1, x_st + 170, y_st + 250 - p3, 30, p3);

            g.DrawLine(new Pen(Color.Black, 2), new Point(x_st + 10, y_st + 250), new Point(x_st + 280, y_st + 250));

            //------------------------------------------------------------  # 60個

            x_st = 800;
            y_st = 0;

            g.DrawString("4", f_index, sb, new PointF(x_st, y_st));
            g.DrawRectangle(Pens.Red, x_st, y_st, 100, 100);

            HatchBrush hatchBrush2 = new HatchBrush(HatchStyle.DashedDownwardDiagonal, Color.Black, Color.Red);
            Font f = new Font("Arial", 25, FontStyle.Bold);
            g.DrawString("Visual Studio", f, hatchBrush2, new PointF(x_st + 20, y_st + 10));
            hatchBrush2 = new HatchBrush(HatchStyle.DarkUpwardDiagonal, Color.Black, Color.Blue);

            f = new Font("Garamond", 16, FontStyle.Strikeout);
            g.DrawString("Visual Studio I love it.", f, hatchBrush2, new PointF(x_st + 10, y_st + 60));
            hatchBrush2 = new HatchBrush(HatchStyle.DashedDownwardDiagonal, Color.Black, Color.Green);

            f = new Font("Broadway", 22, FontStyle.Underline);
            g.DrawString(".NET Framework", f, hatchBrush2, new PointF(x_st + 30, y_st + 100));

            //------------------------------------------------------------  # 60個

            x_st = 800;
            y_st = 150;
            g.DrawString("5", f_index, sb, new PointF(x_st, y_st));
            g.DrawRectangle(Pens.Red, x_st, y_st, 100, 100);

            Rectangle R2;
            LinearGradientBrush lgb2;

            R2 = new Rectangle(x_st + 20, y_st + 50, 80, 80);
            lgb2 = new LinearGradientBrush(R2, Color.Green, Color.Yellow, -45);
            g.FillPie(lgb2, R2, 30, 300);

            R2 = new Rectangle(x_st + 120, y_st + 70, 50, 50);
            lgb2 = new LinearGradientBrush(R2, Color.Green, Color.Yellow, -45);
            g.FillPie(lgb2, R2, 30, 300);

            R2 = new Rectangle(x_st + 190, y_st + 85, 30, 30);
            lgb2 = new LinearGradientBrush(R2, Color.Green, Color.Yellow, -45);
            g.FillPie(lgb2, R2, 30, 300);

            //------------------------------------------------------------  # 60個

            string pic_filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_ic\ic1.jpg";
            TextureBrush textureBrush1;
            Image img = Image.FromFile(pic_filename);
            g.DrawImage(img, 1100, 400);

            textureBrush1 = new TextureBrush(img, WrapMode.TileFlipXY);
            int W = this.Size.Width;
            int H = this.Size.Height;
            //g.FillRectangle(textureBrush1, 0, 0, this.Size.Width, this.Size.Height);
            //g.FillRectangle(textureBrush1, W * 4 / 5, H * 4 / 5, W / 5, H / 5);

            g.FillRectangle(textureBrush1, W * 2 / 3, H * 2 / 3, W / 3, H / 3);

            //------------------------------------------------------------  # 60個

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            TextureBrush textureBrush2;
            Rectangle sR, dR;
            img = Image.FromFile(filename);
            //g.DrawImage(img, 10, 10);

            sR = new Rectangle(100, 100, 100, 100);//來源矩形
            dR = new Rectangle(W * 1 / 3 - 50, H * 2 / 3 - 100, W / 3, H / 3);//目標矩形

            textureBrush2 = new TextureBrush(img, WrapMode.TileFlipXY);
            g.DrawImage(img, dR, sR, GraphicsUnit.Pixel);

            //------------------------------------------------------------  # 60個

            img = Image.FromFile(filename);
            g.DrawImage(img, 0, 10 + 500);
            g.DrawImageUnscaled(img, 250, 10 + 500);
        }

        void draw_grid(Graphics g)
        {
            int W = this.Width;
            int H = this.Height;
            int i;
            int j;

            for (i = 0; i <= W; i += 100)
            {
                g.DrawLine(Pens.Gray, i, 0, i, H);
            }
            for (j = 0; j <= H; j += 100)
            {
                g.DrawLine(Pens.Gray, 0, j, W, j);
            }
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

