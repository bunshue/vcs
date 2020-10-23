using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DrawMouseLine
{
    public partial class Form1 : Form
    {
        Point[] pt = new Point[30];
        int pt_index = -1;
        Image img = Image.FromFile("c:\\______test_files\\picture1.jpg");
        bool flag_mouse_down = false;

        int flag_operation_mode = MODE_1;

        private const int MODE_1 = 0x01;
        private const int MODE_2 = 0x02;
        private const int MODE_3 = 0x03;
        private const int MODE_4 = 0x04;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_mouse_down = true;

            if ((flag_operation_mode == MODE_1) || (flag_operation_mode == MODE_3))
            {

                if (pt_index < (pt.Length - 1)) // 如果一維陣列內的 100 個位置還沒裝滿
                {
                    pt_index++;  // 一維陣列 的索引往前
                    pt[pt_index] = new Point(e.X, e.Y); // 存入 滑鼠游標位置
                    //this.Text = pt_index.ToString();
                    this.Text = e.X.ToString() + ", " + e.Y.ToString();
                    this.Invalidate(); // 要求表單重畫
                }
            }
            else if (flag_operation_mode == MODE_2)
            {
                pt_index = -1;
                this.Invalidate(); // 要求表單重畫
            }
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_operation_mode == MODE_2)
            {
                if (pt_index < (pt.Length - 1)) // 如果一維陣列內的 100 個位置還沒裝滿
                {
                    pt_index++;  // 一維陣列 的索引往前
                    pt[pt_index] = new Point(e.X, e.Y); // 存入 滑鼠游標位置
                    //this.Text = pt_index.ToString();
                    this.Text = e.X.ToString() + ", " + e.Y.ToString();
                    this.Invalidate(); // 要求表單重畫
                }
            }

        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down = false;
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            /*
            for (int i = 0; i <= pt_index; i++)
            {
                e.Graphics.DrawImage(img,
                pt[i].X - img.Width / 2, pt[i].Y - img.Height / 2, //影像左上角在表單的位置
                img.Width, img.Height); //影像的寬高

            }
            */
            //richTextBox1.Text += "index " + pt_index.ToString() + "\n";

            if (radioButton1.Checked == true)
            {
                if (pt_index < 1)
                    return;

                Point[] pt2 = new Point[pt_index + 1];
                int i;
                for (i = 0; i <= pt_index; i++)
                {
                    pt2[i] = pt[i];
                }

                e.Graphics.DrawLines(new Pen(Color.Red, 2), pt2);
            }
            else if (radioButton2.Checked == true)
            {
                //richTextBox1.Text += "idx = " + pt_index.ToString() + "\n";
                //Point[] pt2 = new Point[pt_index + 1];
                int i;
                for (i = 0; i <= pt_index; i++)
                {
                    //richTextBox1.Text += "draw i = " + i.ToString() + "\n";
                    e.Graphics.DrawEllipse(new Pen(Color.Red, 1), pt[i].X, pt[i].Y, 20, 20);
                }
            }
            else if (radioButton3.Checked == true)
            {
                //richTextBox1.Text += "idx = " + pt_index.ToString() + "\n";
                //Point[] pt2 = new Point[pt_index + 1];
                Bitmap bmp = new Bitmap("c:\\______test_files\\BMW.jfif");
                int i;
                for (i = 0; i <= pt_index; i++)
                {
                    //richTextBox1.Text += "draw i = " + i.ToString() + "\n";
                    //e.Graphics.DrawEllipse(new Pen(Color.Red, 1), pt[i].X, pt[i].Y, 20, 20);
                    e.Graphics.DrawImage(bmp, pt[i].X, pt[i].Y, 100, 100);
                }
            }




        }

        private void radioButton_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton1.Checked == true)
                flag_operation_mode = MODE_1;
            else if (radioButton2.Checked == true)
                flag_operation_mode = MODE_2;
            else if (radioButton3.Checked == true)
                flag_operation_mode = MODE_3;
            else if (radioButton4.Checked == true)
                flag_operation_mode = MODE_4;
            else
                flag_operation_mode = 0;

            pt_index = -1;
            this.Invalidate(); // 要求表單重畫
        }

    }
}
