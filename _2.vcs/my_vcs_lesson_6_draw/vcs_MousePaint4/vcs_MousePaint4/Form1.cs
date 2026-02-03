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

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            p = new Pen(Color.Red, 3);
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
    }
}
