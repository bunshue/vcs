using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw3c
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen pen;
        Font font;
        Brush brush;

        int center_x = 200;
        int center_y = 200;
        float radius = 150;

        int angle = 0;
        int point_x = 0;
        int point_y = 0;
        int uvw_offset = 550;
        int y_offset = 50;
        int weight = 2;

        int uvw_y_offset = 200;

        private void DrawUVWSignal()
        {
            int x_offset = 10 + uvw_offset;

            int ha_line = uvw_y_offset + 40;
            int hb_line = uvw_y_offset + 80;
            int hc_line = uvw_y_offset + 120;
            int height = 30;

            Point[] pt = new Point[6];    //一維陣列內有6個Point

            // Create pens.
            Pen redPen = new Pen(Color.Red, 3);

            pt[0].X = x_offset;
            pt[0].Y = ha_line;
            pt[1].X = x_offset;
            pt[1].Y = ha_line - height;
            pt[2].X = x_offset + 180 * weight;
            pt[2].Y = ha_line - height;
            pt[3].X = x_offset + 180 * weight;
            pt[3].Y = ha_line;
            pt[4].X = x_offset + 360 * weight;
            pt[4].Y = ha_line;
            pt[5].X = x_offset + 360 * weight;
            pt[5].Y = ha_line - height;
            g.DrawLines(redPen, pt);   //畫直線連線
        }

        private void DrawHallSignal()
        {
            int x_offset = 10 + uvw_offset;

            int ha_line = y_offset + 40;
            int hb_line = y_offset + 80;
            int hc_line = y_offset + 120;
            int height = 30;

            Point[] pt = new Point[6];    //一維陣列內有6個Point

            // Create pens.
            Pen redPen = new Pen(Color.Red, 3);

            pt[0].X = x_offset;
            pt[0].Y = ha_line;
            pt[1].X = x_offset;
            pt[1].Y = ha_line - height;
            pt[2].X = x_offset + 180 * weight;
            pt[2].Y = ha_line - height;
            pt[3].X = x_offset + 180 * weight;
            pt[3].Y = ha_line;
            pt[4].X = x_offset + 360 * weight;
            pt[4].Y = ha_line;
            pt[5].X = x_offset + 360 * weight;
            pt[5].Y = ha_line - height;
            g.DrawLines(redPen, pt);   //畫直線連線

            pt[0].X = x_offset;
            pt[0].Y = hb_line - height;
            pt[1].X = x_offset + 60 * weight;
            pt[1].Y = hb_line - height;
            pt[2].X = x_offset + 60 * weight;
            pt[2].Y = hb_line;
            pt[3].X = x_offset + 240 * weight;
            pt[3].Y = hb_line;
            pt[4].X = x_offset + 240 * weight;
            pt[4].Y = hb_line - height;
            pt[5].X = x_offset + 360 * weight;
            pt[5].Y = hb_line - height;
            g.DrawLines(redPen, pt);   //畫直線連線

            pt[0].X = x_offset;
            pt[0].Y = hc_line;
            pt[1].X = x_offset + 120 * weight;
            pt[1].Y = hc_line;
            pt[2].X = x_offset + 120 * weight;
            pt[2].Y = hc_line - height;
            pt[3].X = x_offset + 300 * weight;
            pt[3].Y = hc_line - height;
            pt[4].X = x_offset + 300 * weight;
            pt[4].Y = hc_line;
            pt[5].X = x_offset + 360 * weight;
            pt[5].Y = hc_line;
            g.DrawLines(redPen, pt);   //畫直線連線
        }

        private void draw_hall_map()
        {
            Color customColor = Color.FromArgb(255, Color.Pink);
            SolidBrush brushstyle = new SolidBrush(customColor);

            DrawPie(brushstyle, center_x,center_y,(int)radius, 0, 60);
            brushstyle.Color = Color.Green; DrawPie(brushstyle, center_x, center_y, (int)radius, 60, 60);
            brushstyle.Color = Color.Blue; DrawPie(brushstyle, center_x, center_y, (int)radius, 120, 60);
            brushstyle.Color = Color.Yellow; DrawPie(brushstyle, center_x, center_y, (int)radius, 180, 60);
            brushstyle.Color = Color.Lime; DrawPie(brushstyle, center_x, center_y, (int)radius, 240, 60);
            brushstyle.Color = Color.Navy ; DrawPie(brushstyle, center_x, center_y, (int)radius, 300, 60);

            // Create pens.
            Pen redPen = new Pen(Color.Red, 3);
            DrawHallSignal();

            DrawUVWSignal();

            //Draw 3 Hall sensors
            //g.DrawRectangle(new Pen(Color.Black), new Rectangle(center_x - 25, center_y + (int)radius + 10, 50, 30));
            //DrawCircle(new Pen(Color.Black), new Rectangle(center_x - 25, center_y + (int)radius + 10, 50, 30));
            int hall_position_x;
            int hall_position_y;

            hall_position_x = center_x;
            hall_position_y = center_y + (int)radius + 25;
            DrawCircle(hall_position_x, hall_position_y, 20);
            g.DrawString("HA", this.Font, new SolidBrush(Color.Red), hall_position_x - 10, hall_position_y - 5);

            hall_position_x = center_x + (int)((radius + 25) * Math.Cos(Math.PI * 30 / 180));
            hall_position_y = center_y - (int)((radius + 25) * Math.Sin(Math.PI * 30 / 180));
            DrawCircle(hall_position_x, hall_position_y, 20);
            g.DrawString("HB", this.Font, new SolidBrush(Color.Red), hall_position_x - 10, hall_position_y - 5);

            hall_position_x = center_x - (int)((radius + 25) * Math.Cos(Math.PI * 30 / 180));
            hall_position_y = center_y - (int)((radius + 25) * Math.Sin(Math.PI * 30 / 180));
            DrawCircle(hall_position_x, hall_position_y, 20);
            g.DrawString("HC", this.Font, new SolidBrush(Color.Red), hall_position_x - 10, hall_position_y - 5);
        }
        private void DrawPie(SolidBrush brushstyle, int center_x, int center_y, int radius, int angle_st, int angle)
        {
            // Draw the circle
            //g.DrawEllipse(PenStyle, new Rectangle(center_x - radius, center_y - radius, radius * 2, radius * 2));

            // Draw the pie
            g.FillPie(brushstyle, new Rectangle(center_x - radius, center_y - radius, radius * 2, radius * 2), angle_st, angle);
        }

        private void DrawCircle(int center_x, int center_y, int radius)
        {
            //int linewidth = (int)numericUpDown_linewidth2.Value;
            int linewidth = 5;
            // Create a Graphics object for the Control.
            //Graphics g = pictureBox1.CreateGraphics();

            // Create a new pen.
            //顏色、線寬分開寫
            //Pen PenStyle = new Pen(bt_color2.BackColor);
            // Set the pen's width.
            //PenStyle.Width = linewidth;

            //顏色、線寬寫在一起
            Pen PenStyle = new Pen(Color.Red, linewidth);

            // Draw the circle
            g.DrawEllipse(PenStyle, new Rectangle(center_x - radius, center_y - radius, radius * 2, radius * 2));
            //Dispose of the pen.
            PenStyle.Dispose();
        }

        public Form1()
        {
            InitializeComponent();
            this.ClientSize = new System.Drawing.Size(1300, 600);
            g = this.CreateGraphics();
            pen = new Pen(Color.Black, 3);
            font = new Font("標楷體", 16);
            brush = new SolidBrush(Color.Black);
            
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Brush brush = new SolidBrush(Color.Blue);
            label1.Text = "W = " + this.Size.Width.ToString() + " H = " + this.Size.Height.ToString() + " x = " + center_x.ToString() + " y = " + center_y.ToString() + " r = " + radius.ToString();
            //g.DrawRectangle(new Pen(Color.Black), new Rectangle(10, 10, this.Size.Width - 30, this.Size.Height - 50));

            //畫邊界
            g.DrawRectangle(new Pen(Color.Red), new Rectangle(00, 00, this.ClientSize.Width - 1, this.ClientSize.Height - 1));

            point_x = (int)(1* radius * Math.Cos(Math.PI*angle/180));
            point_y = (int)(1* radius * Math.Sin(Math.PI * angle / 180));

            point_x = center_x + point_x;
            point_y = center_y + point_y;

            label2.Text = "半徑 = " + radius.ToString() + ", 軸心 x = " + center_x.ToString() + ", y = " + center_y.ToString() + " 角度 = " + angle.ToString() + ", point_x = " + point_x.ToString() + ", point_y = " + point_y.ToString();


            draw_hall_map();
            DrawCircle(center_x, center_y, (int)radius);
            DrawCircle(center_x, center_y, (int)radius/4);

            Pen blackPen = new Pen(Color.Black, 10);
            g.DrawLine(blackPen, center_x, center_y, point_x, point_y);
            //DrawCircle(point_x, point_y, 10);

            int x_offset = 10 + uvw_offset;
            int hall_poistion_x1, hall_poistion_y1, hall_poistion_x2, hall_poistion_y2;
            hall_poistion_x1 = angle * weight;
            hall_poistion_x2 = angle * weight;
            hall_poistion_y1 = y_offset;
            hall_poistion_y2 = y_offset + 140;

            Point point_hall_1 = new Point(hall_poistion_x1 + x_offset, hall_poistion_y1);
            Point point_hall_2 = new Point(hall_poistion_x2 + x_offset, hall_poistion_y2);

            Point[] hallPoints = { point_hall_1, point_hall_2 };

            //System.Drawing.Point px1 = new System.Drawing.Point(0, this.panel1.Height);
            //System.Drawing.Point px2 = new System.Drawing.Point(this.panel1.Width, this.panel1.Height);
            g.DrawLine(new Pen(Brushes.Black, 2), point_hall_1, point_hall_2);
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)   //根據e.KeyCode分別執行
            {
                case Keys.Up:
                    if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                    {
                        //MessageBox.Show("+");
                    }
                    else
                    {
                        //MessageBox.Show("上");
                    }
                    this.Refresh();
                    break;
                case Keys.Down:
                    if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                    {
                        //MessageBox.Show("-");
                    }
                    else
                    {
                        //MessageBox.Show("下");
                    }
                    this.Refresh();
                    break;
                case Keys.Left:
                    if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                    {
                    }
                    else
                    {
                        //MessageBox.Show("左");
                    }
                    this.Refresh();
                    break;
                case Keys.Right:
                    if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                    {
                    }
                    else
                    {
                        //MessageBox.Show("右");
                    }
                    this.Refresh();
                    break;
                case Keys.Add:
                    //MessageBox.Show("+");
                    this.Refresh();
                    break;
                case Keys.Subtract:
                    //MessageBox.Show("-");
                    this.Refresh();
                    break;
                case Keys.X:
                    //MessageBox.Show("X");
                    Application.Exit();
                    break;
                case Keys.M:
                    this.Refresh();
                    break;
                case Keys.N:
                    this.Refresh();
                    break;
                case Keys.Space:
                    this.Refresh();
                    break;
                default:
                    //MessageBox.Show("x, KeyCode: " + e.KeyCode.ToString());
                    break;
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            angle += 5;
            if (angle > 360)
                angle -= 360;
            this.Refresh();

        }

        private void button1_Click(object sender, EventArgs e)
        {
            timer1.Enabled = true;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            timer1.Enabled = false;
        }

    }
}
