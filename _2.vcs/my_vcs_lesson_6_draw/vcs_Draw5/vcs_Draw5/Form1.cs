using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D; //for GraphicsPath, LinearGradientBrush

namespace vcs_Draw5
{
    public partial class Form1 : Form
    {
        Graphics g;
        public Form1()
        {
            InitializeComponent();
            pictureBox1.Image = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            //g = pictureBox1.CreateGraphics();
            g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(100, 100, 100, 100));
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(200, 200, 100, 100));
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(300, 300, 100, 100));
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(400, 400, 239, 79));
            pictureBox1.Refresh();
        }

        private void button19_Click(object sender, EventArgs e)
        {
            //pictureBox1.Image = null;
            //Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            pictureBox1.Refresh();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            /*
            // 寫法一
            // Create a Graphics object for the Control.
            Graphics g = pictureBox1.CreateGraphics();
            // Create pen.
            Pen penStyle = new Pen(Color.Red, 5);
            // Create location and size of ellipse.
            //畫圓
            g.DrawEllipse(penStyle, 0, 0, 200, 200);

            // Clean up the Graphics object.
            g.Dispose();
            */

            // 寫法二
            //Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));
            g.DrawEllipse(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));
            g.DrawEllipse(new Pen(Color.Black), new Rectangle(100, 100, 100, 100));
            g.DrawEllipse(new Pen(Color.Black), new Rectangle(200, 200, 100, 100));
            g.DrawEllipse(new Pen(Color.Black), new Rectangle(200, 200, 200, 100));
            g.DrawEllipse(new Pen(Color.Black), new Rectangle(300, 300, 100, 100));
            g.DrawEllipse(new Pen(Color.Black), new Rectangle(300, 300, 300, 100));
            g.DrawEllipse(new Pen(Color.Black), new Rectangle(400, 400, 79, 79));
            g.DrawEllipse(new Pen(Color.Black), new Rectangle(400, 400, 239, 79));
            pictureBox1.Refresh();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));
            g.DrawPie(new Pen(Color.Black), new Rectangle(0, 0, 100, 100), 0, 180);
            g.DrawPie(new Pen(Color.Black), new Rectangle(100, 100, 100, 100), 0, 180);
            g.DrawPie(new Pen(Color.Black), new Rectangle(200, 200, 100, 100), 0, 180);
            g.DrawPie(new Pen(Color.Black), new Rectangle(200, 200, 200, 100), 0, 180);
            g.DrawPie(new Pen(Color.Black), new Rectangle(300, 300, 100, 100), 0, 180);
            g.DrawPie(new Pen(Color.Black), new Rectangle(300, 300, 300, 100), 0, 180);
            g.DrawPie(new Pen(Color.Black), new Rectangle(400, 400, 79, 79), 0, 180);
            g.DrawPie(new Pen(Color.Black), new Rectangle(400, 400, 239, 79), 0, 180);
            pictureBox1.Refresh();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));
            Point[] pts = new Point[5];
            pts[0].X = 10;
            pts[0].Y = 10;
            pts[1].X = 20;
            pts[1].Y = 10;
            pts[2].X = 30;
            pts[2].Y = 20;
            pts[3].X = 20;
            pts[3].Y = 20;
            pts[4].X = 10;
            pts[4].Y = 30;
            g.DrawPolygon(new Pen(Color.Black), pts);
            pictureBox1.Refresh();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));

            //using System.Drawing.Drawing2D;
            GraphicsPath gPath = new GraphicsPath();
            gPath.AddLine(new Point(10, 10), new Point(60, 60));
            gPath.AddLine(new Point(60, 10), new Point(10, 60));
            gPath.AddRectangle(new Rectangle(10, 10, 50, 50));
            g.DrawPath(new Pen(Color.Black), gPath);
            pictureBox1.Refresh();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            g.DrawLine(new Pen(Color.Black), 0, 0, 100, 0);
            g.DrawLine(new Pen(Color.Black), 100, 0, 100, 100);
            g.DrawLine(new Pen(Color.Black), 100, 100, 200, 100);
            g.DrawLine(new Pen(Color.Black), 200, 100, 200, 200);
            g.DrawLine(new Pen(Color.Black), 200, 200, 300, 200);
            g.DrawLine(new Pen(Color.Black), 300, 200, 300, 300);
            g.DrawLine(new Pen(Color.Black), 300, 300, 400, 300);
            g.DrawLine(new Pen(Color.Black), 400, 300, 400, 400);
            g.DrawLine(new Pen(Color.Black), 400, 400, 479, 400);
            g.DrawLine(new Pen(Color.Black), 479, 400, 479, 479);
            g.DrawLine(new Pen(Color.Black), 479, 479, 639, 479);
            pictureBox1.Refresh();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));
            g.DrawArc(new Pen(Color.Black), new Rectangle(0, 0, 100, 100), 90, 180);
            g.DrawArc(new Pen(Color.Black), new Rectangle(100, 100, 100, 100), 90, 180);
            g.DrawArc(new Pen(Color.Black), new Rectangle(200, 200, 100, 100), 90, 180);
            g.DrawArc(new Pen(Color.Black), new Rectangle(300, 300, 100, 100), 90, 180);
            g.DrawArc(new Pen(Color.Black), new Rectangle(400, 400, 79, 79), 90, 180);
            pictureBox1.Refresh();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));
            g.DrawBezier(new Pen(Color.Black), 10, 10, 20, 60, 60, 60, 50, 10);
            pictureBox1.Refresh();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));
            Point[] pts = new Point[5];
            pts[0].X = 10;
            pts[0].Y = 10;
            pts[1].X = 20;
            pts[1].Y = 60;
            pts[2].X = 30;
            pts[2].Y = 10;
            pts[3].X = 40;
            pts[3].Y = 60;
            pts[4].X = 50;
            pts[4].Y = 10;
            g.DrawCurve(new Pen(Color.Black), pts);
            pictureBox1.Refresh();
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));
            g.DrawString("畫字串", this.Font, new SolidBrush(Color.Black), 0, 0);
            g.DrawString("畫字串", this.Font, new SolidBrush(Color.Black), 100, 100);
            g.DrawString("畫字串", this.Font, new SolidBrush(Color.Black), 200, 200);
            g.DrawString("畫字串", this.Font, new SolidBrush(Color.Black), 300, 300);
            g.DrawString("畫字串", this.Font, new SolidBrush(Color.Black), 400, 400);
            pictureBox1.Refresh();
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            g.FillRectangle(new SolidBrush(Color.Lime), new Rectangle(0, 0, 100, 100));
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));
            g.FillRectangle(new SolidBrush(Color.Lime), new Rectangle(100, 100, 100, 100));
            g.FillRectangle(new SolidBrush(Color.Lime), new Rectangle(200, 200, 100, 100));
            g.FillRectangle(new SolidBrush(Color.Lime), new Rectangle(300, 300, 100, 100));
            g.FillRectangle(new SolidBrush(Color.Lime), new Rectangle(400, 400, 239, 79));
            pictureBox1.Refresh();
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));
            g.FillEllipse(new SolidBrush(Color.Lime), new Rectangle(0, 0, 100, 100));
            g.FillEllipse(new SolidBrush(Color.Lime), new Rectangle(100, 100, 100, 100));
            g.FillEllipse(new SolidBrush(Color.Lime), new Rectangle(200, 200, 100, 100));
            g.FillEllipse(new SolidBrush(Color.Lime), new Rectangle(300, 300, 100, 100));
            g.FillEllipse(new SolidBrush(Color.Lime), new Rectangle(400, 400, 239, 79));
            pictureBox1.Refresh();
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));
            g.FillPie(new SolidBrush(Color.Lime), new Rectangle(0, 0, 100, 100), 0, 180);
            g.FillPie(new SolidBrush(Color.Lime), new Rectangle(100, 100, 100, 100), 0, 180);
            g.FillPie(new SolidBrush(Color.Lime), new Rectangle(200, 200, 100, 100), 0, 180);
            g.FillPie(new SolidBrush(Color.Lime), new Rectangle(300, 300, 100, 100), 0, 180);
            g.FillPie(new SolidBrush(Color.Lime), new Rectangle(400, 400, 239, 79), 0, 180);

            pictureBox1.Refresh();
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));
            Point[] pts = new Point[5];
            pts[0].X = 10;
            pts[0].Y = 10;
            pts[1].X = 20;
            pts[1].Y = 10;
            pts[2].X = 30;
            pts[2].Y = 20;
            pts[3].X = 20;
            pts[3].Y = 20;
            pts[4].X = 10;
            pts[4].Y = 30;
            g.FillPolygon(new SolidBrush(Color.Lime), pts);
            pictureBox1.Refresh();
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));

            //using System.Drawing.Drawing2D;
            GraphicsPath gPath = new GraphicsPath();
            gPath.AddLine(new Point(10, 10), new Point(60, 60));
            gPath.AddLine(new Point(60, 10), new Point(10, 60));
            gPath.AddRectangle(new Rectangle(10, 10, 50, 50));
            g.FillPath(new SolidBrush(Color.Lime), gPath);
            pictureBox1.Refresh();
        }

        private void button21_Click(object sender, EventArgs e)
        {
            int w = pictureBox1.Width;
            int h = pictureBox1.Height;
            Bitmap bmp = new Bitmap(w, h);
            //Graphics g = Graphics.FromImage(bmp);
            g.Clear(Color.White);
            //pictureBox1.Image = bmp;
        }

        private void button20_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                pictureBox1.Load(openFileDialog1.FileName);
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void button10_Click(object sender, EventArgs e)
        {
            // Create a Graphics object for the Control.
            //Graphics g = pictureBox1.CreateGraphics();

            // Create a new pen.
            Pen PenStyle = new Pen(Brushes.DeepSkyBlue);

            // Set the pen's width.
            PenStyle.Width = 8.0F;

            #region 設定轉彎接線
            // Set the LineJoin property.
            PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.Bevel;
            // Draw a rectangle.
            g.DrawRectangle(PenStyle, new Rectangle(10, 10, 80, 80));

            // Set the LineJoin property.
            PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.Miter;
            // Draw a rectangle.
            g.DrawRectangle(PenStyle, new Rectangle(110, 10, 80, 80));

            // Set the LineJoin property.
            PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.MiterClipped;
            // Draw a rectangle.
            g.DrawRectangle(PenStyle, new Rectangle(210, 10, 80, 80));

            // Set the LineJoin property.
            PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.Round;
            // Draw a rectangle.
            g.DrawRectangle(PenStyle, new Rectangle(310, 10, 80, 80));
            #endregion

            #region 設定DashStyle property
            // Set the DashStyle property.
            PenStyle.DashStyle = System.Drawing.Drawing2D.DashStyle.Custom;
            // Draw a rectangle.
            g.DrawRectangle(PenStyle, new Rectangle(10, 110, 80, 80));

            // Set the DashStyle property.
            PenStyle.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash;
            // Draw a rectangle.
            g.DrawRectangle(PenStyle, new Rectangle(110, 110, 80, 80));

            // Set the DashStyle property.
            PenStyle.DashStyle = System.Drawing.Drawing2D.DashStyle.DashDot;
            // Draw a rectangle.
            g.DrawRectangle(PenStyle, new Rectangle(210, 110, 80, 80));

            // Set the DashStyle property.
            PenStyle.DashStyle = System.Drawing.Drawing2D.DashStyle.DashDotDot;
            // Draw a rectangle.
            g.DrawRectangle(PenStyle, new Rectangle(310, 110, 80, 80));

            // Set the DashStyle property.
            PenStyle.DashStyle = System.Drawing.Drawing2D.DashStyle.Dot;
            // Draw a rectangle.
            g.DrawRectangle(PenStyle, new Rectangle(410, 110, 80, 80));

            // Set the DashStyle property.
            PenStyle.DashStyle = System.Drawing.Drawing2D.DashStyle.Solid;
            // Draw a rectangle.
            g.DrawRectangle(PenStyle, new Rectangle(510, 110, 80, 80));
            #endregion

            #region 設定顏色
            // Set the DashStyle property.
            //skyBluePen.DashStyle = System.Drawing.Drawing2D.DashStyle.Solid;
            PenStyle.Brush = System.Drawing.Brushes.Aquamarine;
            // Draw a rectangle.
            g.DrawRectangle(PenStyle, new Rectangle(10, 210, 80, 80));
            #endregion

            //Dispose of the pen.
            PenStyle.Dispose();


        }

        private void DrawXY()//画X轴Y轴
        {
            //Graphics g = this.pictureBox1.CreateGraphics();
            System.Drawing.Point px1 = new System.Drawing.Point(0, this.pictureBox1.Height);
            System.Drawing.Point px2 = new System.Drawing.Point(this.pictureBox1.Width, this.pictureBox1.Height);
            g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
            System.Drawing.Point py1 = new System.Drawing.Point(0, this.pictureBox1.Height);
            System.Drawing.Point py2 = new System.Drawing.Point(0, 0);
            g.DrawLine(new Pen(Brushes.Black, 5), py1, py2);
            pictureBox1.Refresh();
            //g.Dispose();
        }

        private void DrawXLine()    //画X轴平行线
        {
            //Graphics g = this.pictureBox1.CreateGraphics();
            for (int i = 1; i < 9; i++)
            {
                Point px1 = new Point(0, this.pictureBox1.Height - i * 50);
                Point px2 = new Point(this.pictureBox1.Width, this.pictureBox1.Height - i * 50);
                g.DrawLine(new Pen(Brushes.Black, 1), px1, px2);
            }
            //g.Dispose();
            pictureBox1.Refresh();
        }
        private void DrawYLine()    //画X轴刻度
        {
            //Graphics g = this.pictureBox1.CreateGraphics();
            for (int i = 1; i < 9; i++)
            {
                System.Drawing.Point py1 = new System.Drawing.Point(100 * i, this.pictureBox1.Height - 5);
                System.Drawing.Point py2 = new System.Drawing.Point(100 * i, this.pictureBox1.Height);
                g.DrawLine(new Pen(Brushes.Red, 1), py1, py2);
            }
            pictureBox1.Refresh();
            //g.Dispose();
        }

        private void button25_Click(object sender, EventArgs e)
        {
            DrawXY();
        }

        private void button27_Click(object sender, EventArgs e)
        {
            DrawXLine();
        }

        private void button26_Click(object sender, EventArgs e)
        {
            DrawYLine();
        }

        private void button22_Click(object sender, EventArgs e)
        {
            colorDialog1.AllowFullOpen = true;
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                //richTextBox1.BackColor = colorDialog1.Color;
                bt_color.BackColor = colorDialog1.Color;
            }
        }

        private void button23_Click(object sender, EventArgs e)
        {
            int position_x = int.Parse(tb_x.Text);
            int position_y = int.Parse(tb_y.Text);
            int size_w = int.Parse(tb_w.Text);
            int size_h = int.Parse(tb_h.Text);
            int linewidth = (int)numericUpDown_linewidth.Value;
            int drawtype = comboBox_drawtype.SelectedIndex;
            int jointype = comboBox_jointype.SelectedIndex;
            int dashtype = comboBox_dashtype.SelectedIndex;

            // Create a Graphics object for the Control.
            //Graphics g = pictureBox1.CreateGraphics();

            // Create a new pen.
            Pen PenStyle = new Pen(bt_color.BackColor);

            // Set the pen's width.
            PenStyle.Width = linewidth;

            // Set the LineJoin property.
            switch (jointype)
            {
                case 0: PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.Bevel; break;
                case 1: PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.Miter; break;
                case 2: PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.MiterClipped; break;
                case 3: PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.Round; break;
                default:
                    PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.Bevel; break;
            }

            // Set the DashStyle property.
            switch (dashtype)
            {
                case 0: PenStyle.DashStyle = System.Drawing.Drawing2D.DashStyle.Custom; break;
                case 1: PenStyle.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash; break;
                case 2: PenStyle.DashStyle = System.Drawing.Drawing2D.DashStyle.DashDot; break;
                case 3: PenStyle.DashStyle = System.Drawing.Drawing2D.DashStyle.DashDotDot; break;
                case 4: PenStyle.DashStyle = System.Drawing.Drawing2D.DashStyle.Dot; break;
                case 5: PenStyle.DashStyle = System.Drawing.Drawing2D.DashStyle.Solid; break;
                default:
                    PenStyle.DashStyle = System.Drawing.Drawing2D.DashStyle.Custom; break;
            }

            // Draw
            switch (drawtype)
            {
                case 0: g.DrawRectangle(PenStyle, new Rectangle(position_x, position_y, size_w, size_h)); break;
                case 1: g.DrawEllipse(PenStyle, new Rectangle(position_x, position_y, size_w, size_h)); break;
                case 2: g.DrawPie(PenStyle, new Rectangle(position_x, position_y, size_w, size_h), 0, 180); break;
                case 3: g.DrawArc(PenStyle, new Rectangle(position_x, position_y, size_w, size_h), 90, 180); break;
                //case 4: g.DrawString("畫字串", this.Font, new SolidBrush(Color.Black), position_x, position_y); break;
                case 4: g.DrawString("畫字串", this.Font, new SolidBrush(bt_color.BackColor), position_x, position_y); break;
                default:
                    PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.Bevel; break;
            }

            //Dispose of the pen.
            PenStyle.Dispose();

        }

        private void button31_Click(object sender, EventArgs e)
        {
        }

        private void button22_Click_1(object sender, EventArgs e)
        {
            colorDialog1.AllowFullOpen = true;
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                //richTextBox1.BackColor = colorDialog1.Color;
                bt_color2.BackColor = colorDialog1.Color;
            }

        }

        private void button22_Click_2(object sender, EventArgs e)
        {
        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {
            GradientColor(e);
        }

        //抽取成一個方法實現漸變色,在Paint中引用
        private void GradientColor(PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            Color FColor = Color.Green;
            Color TColor = Color.Yellow;

            Brush b = new LinearGradientBrush(this.ClientRectangle, FColor, TColor, LinearGradientMode.ForwardDiagonal);

            g.FillRectangle(b, this.ClientRectangle);

            /*
             * Horizontal = 0　　　　　　摘要:指定從左到右的漸變。
             * 
             * Vertical = 1　　　　　　　摘要: 指定從上到下的漸變。
             * 
             * ForwardDiagonal = 2　　  摘要:指定從左上到右下的漸變。
             * 
             * BackwardDiagonal = 3　　 摘要:指定從右上到左下的漸變。
             */
        }

    }
}
