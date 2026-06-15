using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Class4
{
    public partial class Form1 : Form
    {
        G2D_ColorRect rect01, rect02;  // 兩個顏色矩形物件


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            int Cx = this.ClientSize.Width / 2;   // 視窗客戶區的中心點
            int Cy = this.ClientSize.Height / 2;

            rect01 = new G2D_ColorRect(Cx, Cy, 200, 100, Color.Black);
            rect02 = new G2D_ColorRect(Cx, Cy, 100, 200, Color.Black);
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            richTextBox1.Size = new Size(300, 690);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1000, 750);
            this.Text = "顏色混合";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        // 滑鼠按下 看看是否能夠選到 顏色矩形物件
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            rect01.check(e.X, e.Y);
            rect02.check(e.X, e.Y);
        }

        // 滑鼠移動 被選到的 顏色矩形物件 要更新位置
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            rect01.update(e.X, e.Y);
            rect02.update(e.X, e.Y);
            this.Invalidate();
        }

        // 滑鼠放開 沒顏色矩形物件 被選到
        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            rect01.drag = false;
            rect02.drag = false;
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            rect01.Draw(e.Graphics); // 兩個顏色矩形物件 繪出
            rect02.Draw(e.Graphics);

            // 混色
            int red = trackBar_color1r.Value + trackBar_color2r.Value;
            //if (red > 255) red = 255;
            red = Math.Min(red, 255);

            int green = trackBar_color1g.Value + trackBar_color2g.Value;
            if (green > 255)
            {
                green = 255;
            }

            int blue = trackBar_color1b.Value + trackBar_color2b.Value;
            if (blue > 255)
            {
                blue = 255;
            }

            this.Text = "( " + red.ToString() + ", " + green.ToString() + ", " + blue.ToString() + " )";
            SolidBrush myBrush = new SolidBrush(Color.FromArgb(red, green, blue));

            Rectangle r1 = rect01.GetRect();
            Rectangle r2 = rect02.GetRect();
            Rectangle r3 = Rectangle.Intersect(r1, r2);   // 交集

            e.Graphics.FillRectangle(myBrush, r3);    // 混色的塗刷
            e.Graphics.DrawRectangle(Pens.White, r3); // 交集區域的繪出
        }

        // 第一個顏色矩形物件的 顏色調整
        private void trackBar_color1_Scroll(object sender, EventArgs e)
        {
            Color color;
            color = Color.FromArgb(trackBar_color1r.Value, trackBar_color1g.Value, trackBar_color1b.Value);
            rect01.color = color;
            groupBox1.Text = "( " + trackBar_color1r.Value.ToString() + ", " + trackBar_color1g.Value.ToString() + ", " + trackBar_color1b.Value.ToString() + " )";
            this.Invalidate();
        }

        // 第二個顏色矩形物件的 顏色調整 
        private void trackBar_color2_Scroll(object sender, EventArgs e)
        {
            Color color;
            color = Color.FromArgb(trackBar_color2r.Value, trackBar_color2g.Value, trackBar_color2b.Value);
            rect02.color = color;
            groupBox2.Text = "( " + trackBar_color2r.Value.ToString() + ", " + trackBar_color2g.Value.ToString() + ", " + trackBar_color2b.Value.ToString() + " )";
            this.Invalidate();
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


