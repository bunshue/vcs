using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MousePaint4
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;
        Font f;
        bool flag_print_mouse_cursor = false;

        Point pt;  // 滑鼠游標座標
        Pen pen = new Pen(Color.Black, 4); // 粗的黑筆

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // 外部的滑鼠游標圖形檔案
            this.Cursor = new Cursor("../../pen.cur");

            // 內嵌的滑鼠游標圖形
            this.Cursor = new Cursor(GetType(), "3dgarro.cur");

            p = new Pen(Color.Red, 3);

            pictureBox1.Dock = DockStyle.Fill;
            pictureBox1.MouseMove += new MouseEventHandler(pictureBox1_MouseMove);
            pictureBox1.Paint += new PaintEventHandler(pictureBox1_Paint);

        }

        int x_old = 0;
        int y_old = 0;

        bool flag_eraser_mode = false;
        bool enable_erase = false;

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox1.Checked == true)
            {
                flag_eraser_mode = true;

                g = this.CreateGraphics();
                p = new Pen(Color.Red, 6);
            }
            else
            {
                flag_eraser_mode = false;
            }

        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            //richTextBox1.Text += "Mouse Down\n";
            enable_erase = true;

            x_old = e.X;
            y_old = e.Y;
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            //this.Text = e.X.ToString() + ", " + e.Y.ToString();
            this.Text = String.Format("X：{0}, Y：{1}", e.X, e.Y);    //格式化字串

            if ((flag_eraser_mode == true) && (enable_erase == true))
            {
                sb = new SolidBrush(Color.Red);
                //g.FillEllipse(sb, e.X, e.Y, 10, 10);

                g.DrawLine(new Pen(Color.Red, 10), x_old, y_old, e.X, e.Y);

                x_old = e.X;
                y_old = e.Y;
            }

            //this.Invalidate();  // 要求表單重畫
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            //richTextBox1.Text += "Mouse Up\n";
            enable_erase = false;

            if (flag_print_mouse_cursor == true)
            {
                Graphics myGraphics = this.CreateGraphics();
                Cursor.Draw(myGraphics, new Rectangle(e.X, e.Y, 10, 10));
            }
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Point pt = Cursor.Position; // 滑鼠座標
            pt = this.PointToClient(pt); // 螢幕座標 -> 視窗客戶區座標
            this.Text = pt.X.ToString() + ", " + pt.Y.ToString();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            if (button0.Text == "在Form上印出滑鼠游標形狀")
            {
                flag_print_mouse_cursor = true;
                this.Cursor = Cursors.Hand;
                button0.Text = "停止印出滑鼠游標形狀";
            }
            else
            {
                flag_print_mouse_cursor = false;
                this.Cursor = Cursors.Default;
                button0.Text = "在Form上印出滑鼠游標形狀";
            }
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            pt = e.Location; // 得到滑鼠游標座標
            this.pictureBox1.Invalidate(); // 要求重畫
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            Rectangle rect = new Rectangle(100, 50, 200, 100);
            e.Graphics.FillRectangle(Brushes.LightGreen, rect); //淡綠色矩形區塊

            Rectangle rectMouse = new Rectangle(pt.X - 40, pt.Y - 40, 80, 80); //紅色矩形區塊

            bool pointInRect = rect.Contains(pt);  // 點在矩形區域中
            bool RectinRect = rect.Contains(rectMouse); // 矩形區域在矩形區域
            bool intersect = rect.IntersectsWith(rectMouse); // 矩形區域和矩形區域有交集

            if (pointInRect == true)
            {
                this.pictureBox1.Cursor = Cursors.Cross; // 改變游標形狀
            }
            else
            {
                this.pictureBox1.Cursor = Cursors.Default;
            }

            if (RectinRect == true)
            {
                e.Graphics.FillRectangle(Brushes.DarkGreen, rectMouse); //深綠色矩形區塊
                label2.Text = "深綠色矩形區塊";
            }
            else
            {
                e.Graphics.FillRectangle(Brushes.Red, rectMouse); //紅色矩形區塊
                label2.Text = "紅色矩形區塊";
            }

            if (intersect == true)
            {
                e.Graphics.DrawRectangle(pen, rect); //綠色矩形區塊 加外框
                label1.Text = "有交集";
            }
            else
            {
                label1.Text = "無交集";
            }

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //this.Invalidate();  // 要求表單重畫
        }
    }
}
