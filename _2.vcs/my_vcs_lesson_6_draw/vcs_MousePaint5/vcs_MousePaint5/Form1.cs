using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;  // for SmoothingMode

// 滑鼠操作畫圖相關

namespace vcs_MousePaint5
{
    public partial class Form1 : Form
    {
        //pictureBox0 畫多邊形 ST

        // Each polygon is represented by a List<Point>.
        private List<List<Point>> Polygons0 = new List<List<Point>>();

        // Points for the new polygon.
        private List<Point> NewPolygon0 = null;

        // The current mouse position while drawing a new polygon.
        private Point NewPoint0;

        //pictureBox0 直多邊形 SP

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

            hScrollBar1.Size = new Size(W, 20);
            hScrollBar2.Size = new Size(W, 20);
            hScrollBar1.Location = new Point(x_st + dx * 1, y_st + dy * 0 + H - 20);
            hScrollBar2.Location = new Point(x_st + dx * 2, y_st + dy * 0 + H - 20);

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
            this.Text = "vcs_MousePaint5";

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

        // Start or continue drawing a new polygon.
        private void pictureBox0_MouseDown(object sender, MouseEventArgs e)
        {
            // See if we are already drawing a polygon.
            if (NewPolygon0 != null)
            {
                // We are already drawing a polygon.
                // If it's the right mouse button, finish this polygon.
                if (e.Button == MouseButtons.Right)
                {
                    // Finish this polygon.
                    if (NewPolygon0.Count > 2)
                    {
                        Polygons0.Add(NewPolygon0);
                    }
                    NewPolygon0 = null;
                }
                else
                {
                    // Add a point to this polygon.
                    if (NewPolygon0[NewPolygon0.Count - 1] != e.Location)
                    {
                        NewPolygon0.Add(e.Location);
                    }
                }
            }
            else
            {
                // Start a new polygon.
                NewPolygon0 = new List<Point>();
                NewPoint0 = e.Location;
                NewPolygon0.Add(e.Location);
            }

            // Redraw.
            pictureBox0.Invalidate();
        }

        // Move the next point in the new polygon.
        private void pictureBox0_MouseMove(object sender, MouseEventArgs e)
        {
            if (NewPolygon0 == null)
            {
                return;
            }
            NewPoint0 = e.Location;
            pictureBox0.Invalidate();
        }

        private void pictureBox0_MouseUp(object sender, MouseEventArgs e)
        {
        }

        // Redraw old polygons in blue. Draw the new polygon in green.
        // Draw the final segment dashed.
        private void pictureBox0_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.Clear(pictureBox0.BackColor);

            e.Graphics.DrawString("左鍵點選頂點", new Font("標楷體", 30), new SolidBrush(Color.Green), new PointF(10, 10));
            e.Graphics.DrawString("右鍵結束", new Font("標楷體", 30), new SolidBrush(Color.Green), new PointF(10, 10 + 40));

            // Draw the old polygons.
            foreach (List<Point> polygon in Polygons0)
            {
                e.Graphics.FillPolygon(Brushes.White, polygon.ToArray());
                e.Graphics.DrawPolygon(Pens.Blue, polygon.ToArray());
            }

            // Draw the new polygon.
            if (NewPolygon0 != null)
            {
                // Draw the new polygon.
                if (NewPolygon0.Count > 1)
                {
                    e.Graphics.DrawLines(Pens.Green, NewPolygon0.ToArray());
                }

                // Draw the newest edge.
                if (NewPolygon0.Count > 0)
                {
                    using (Pen dashed_pen = new Pen(Color.Green))
                    {
                        dashed_pen.DashPattern = new float[] { 3, 3 };
                        e.Graphics.DrawLine(dashed_pen, NewPolygon0[NewPolygon0.Count - 1], NewPoint0);
                    }
                }
            }
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
