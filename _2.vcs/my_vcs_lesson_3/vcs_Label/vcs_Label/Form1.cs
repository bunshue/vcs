using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Text;  //for TextRenderingHint
using System.Drawing.Drawing2D; //for MatrixOrder

namespace vcs_Label
{
    public partial class Form1 : Form
    {
        int move_d = 1;   //記錄跑馬燈文字移動方向    0:向左 1:向右 2:向上 3:向下

        bool isPress = false;   //判斷是否有按下
        int oldX, oldY;         //記錄按下的位置

        public Form1()
        {
            InitializeComponent();
        }

        // Hide the labels that position the rotated text.
        private void Form1_Load(object sender, EventArgs e)
        {
            lblRotated1.Visible = false;
            lblRotated2.Visible = false;
            lblRotated3.Visible = false;
            label_run.Text = DateTime.Now.ToString();

            //向右
            this.timer_left.Stop();
            this.timer_right.Start();

            //使用滑鼠拖曳圖片 圖片藏在label裏 ST
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_angry_bird\AB_red.jpg";
            Image image = Image.FromFile(filename);
            int width = image.Width;
            int height = image.Height;

            //要在Properties.Resources放入圖片
            label_picture.Text = "";
            label_picture.AutoSize = false;
            //關閉自動調整大小
            label_picture.Width = image.Width;
            label_picture.Height = image.Height;
            label_picture.Image = image;
            label_picture.Cursor = Cursors.Cross;    //移到控件上，改變鼠標

            label_picture.MouseDown += new MouseEventHandler(label_picture_MouseDown);
            label_picture.MouseMove += new MouseEventHandler(label_picture_MouseMove);
            label_picture.MouseUp += new MouseEventHandler(label_picture_MouseUp);
            label_picture.MouseEnter += new EventHandler(label_picture_MouseEnter);
            label_picture.MouseHover += new EventHandler(label_picture_MouseHover);
            //使用滑鼠拖曳圖片 圖片藏在label裏 SP
        }

        //使用滑鼠拖曳圖片 圖片藏在label裏 ST
        private void label_picture_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == System.Windows.Forms.MouseButtons.Left)
            {
                label_picture.Cursor = Cursors.Hand;
                isPress = true;
                oldX = e.X;
                oldY = e.Y;
            }
        }

        private void label_picture_MouseMove(object sender, MouseEventArgs e)
        {
            if (isPress)
            {
                label_picture.Left = e.X + (label_picture.Left - oldX);
                label_picture.Top = e.Y + (label_picture.Top - oldY);
                //按下的點，可能在圖上的任一點，所以抓出對應的座標並加回去
            }
        }

        private void label_picture_MouseUp(object sender, MouseEventArgs e)
        {
            isPress = false;
            label_picture.Cursor = Cursors.Cross;    //移到控件上，改變鼠標
        }

        private void label_picture_MouseEnter(object sender, EventArgs e)
        {
            label_picture.Cursor = Cursors.Cross;    //移到控件上，改變鼠標
        }

        private void label_picture_MouseHover(object sender, EventArgs e)
        {
            label_picture.Cursor = Cursors.Cross;    //移到控件上，改變鼠標
        }
        //使用滑鼠拖曳圖片 圖片藏在label裏 SP

        // Draw rotated text.
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            using (StringFormat string_format = new StringFormat())
            {
                string_format.Alignment = StringAlignment.Center;
                string_format.LineAlignment = StringAlignment.Center;

                e.Graphics.TextRenderingHint =
                    TextRenderingHint.AntiAliasGridFit;
                DrawSidewaysText(e.Graphics, Font, Brushes.Black,
                    lblRotated1.Bounds, string_format, "Row 1");
                DrawSidewaysText(e.Graphics, Font, Brushes.Black,
                    lblRotated2.Bounds, string_format, "Row 2");
                DrawSidewaysText(e.Graphics, Font, Brushes.Black,
                    lblRotated3.Bounds, string_format, "Row 3");
            }
        }

        // Draw sideways text in the indicated rectangle.
        private void DrawSidewaysText(Graphics gr, Font font, Brush brush, Rectangle bounds, StringFormat string_format, string txt)
        {
            // Make a rotated rectangle at the origin.
            Rectangle rotated_bounds = new Rectangle(
                0, 0, bounds.Height, bounds.Width);

            // Rotate.
            gr.ResetTransform();
            gr.RotateTransform(-90);

            // Translate to move the rectangle to the correct position.
            gr.TranslateTransform(bounds.Left, bounds.Bottom, MatrixOrder.Append);

            // Draw the text.
            gr.DrawString(txt, font, brush, rotated_bounds, string_format);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            lb_moving.Left -= 2;
            if (lb_moving.Right < 0)
            {
                lb_moving.Left = this.Width;
            }

            if (move_d == 0)      //向左
            {
                label_run.Left -= 10;
                if (label_run.Left <= -label_run.Width)
                {
                    label_run.Left = this.Width;
                }
            }
            else if (move_d == 1)      //向右
            {
                label_run.Left += 10;
                if (label_run.Left >= this.Width)
                {
                    label_run.Left = -label_run.Width;
                }
            }
            else if (move_d == 2)      //向上
            {
                label_run.Top -= 10;
                if (label_run.Top <= -label_run.Height)
                {
                    label_run.Top = this.Height;
                }
            }
            else if (move_d == 3)      //向下
            {
                label_run.Top += 10;
                if (label_run.Top >= this.Height)
                {
                    label_run.Top = -label_run.Height;
                }
            }
            else
            {
            }
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            lb_moving2.Text = lb_moving2.Text.Substring(1) + lb_moving2.Text.Substring(0, 1);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //向左
            move_d = 0;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //向右
            move_d = 1;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //向上
            move_d = 2;

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //向下
            move_d = 3;

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //置中
            int W = this.ClientSize.Width;
            int H = this.ClientSize.Height;
            label_run.Left = W / 2;
            label_run.Top = H / 2;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //向右
            this.timer_left.Stop();
            this.timer_right.Start();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //向左
            this.timer_right.Stop();
            this.timer_left.Start();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //暫停
            this.timer_right.Stop();
            this.timer_left.Stop();
        }

        private void timer_right_Tick(object sender, EventArgs e)
        {
            //向右
            this.label_run2.Left += 8;  //向右移動3個像素
            if (this.label_run2.Left > this.Width)
            {
                this.label_run2.Left = 0 - label_run2.Width;   //標簽左位置為當前控件寬度
            }
        }

        private void timer_left_Tick(object sender, EventArgs e)
        {
            //向左
            this.label_run2.Left -= 8;  //向右移動3個像素
            if (this.label_run2.Right < 0)
            {
                this.label_run2.Left = this.Width;   //標簽左位置為當前控件寬度
            }
        }

        int cnt = 0;
        private void button9_Click(object sender, EventArgs e)
        {
            label_auto.Text += "abc" + cnt.ToString();
            label_auto.AutoSize = false;
            label_auto.Width = 120;
            label_auto.Height = 200;
        }

        int cnt_use_top_left = 0;
        private void timer_use_top_left_Tick(object sender, EventArgs e)
        {
            cnt_use_top_left++;
            if (cnt_use_top_left < 20)
            {
                lb_use_top_left.Left += 5;//右移
            }
            else if (cnt_use_top_left < 40)
            {
                lb_use_top_left.Top += 5;//下移
            }
            else if (cnt_use_top_left < 60)
            {
                lb_use_top_left.Left -= 5;//左移
            }
            else if (cnt_use_top_left < 80)
            {
                lb_use_top_left.Top -= 5;//上移
            }
            else
            {
                cnt_use_top_left = 0;
            }
        }
    }
}
