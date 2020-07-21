using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace 小畫家大全
{
    public partial class Form1 : Form
    {
        private Point startPoint, oldPoint; //繪圖時紀錄滑鼠位置
        //枚举类型，各种绘图工具
        private enum drawTools
        {
            Pen = 0, Line, Circle, Rectangle, String, Erase, None
        };
        //当前使用的工具
        private drawTools drawTool = drawTools.Pen;
        private bool isDrawing = false;     //是否正在繪圖

        Graphics g;         //Graphics實例
        Pen PenStyle;
        //SolidBrush sb;
        Bitmap bitmap1;

        Graphics ig;        //繪製bitmap的Graphics實例

        Color foreColor = Color.Red;
        Color backColor = Color.White;

        public Form1()
        {
            InitializeComponent();

            //創建一個bitmap
            bitmap1 = new Bitmap(this.ClientRectangle.Width, this.ClientRectangle.Height);
            g = this.CreateGraphics();
            ig = Graphics.FromImage(bitmap1);
            //ig.Clear(backColor);

            PenStyle = new Pen(foreColor);
            PenStyle.Width = (int)numericUpDown1.Value;
            PenStyle.StartCap = System.Drawing.Drawing2D.LineCap.Round;
            PenStyle.EndCap = System.Drawing.Drawing2D.LineCap.Round;
            PenStyle.Color = foreColor;

            //PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.Bevel;
            PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.Round;

            g.Clear(backColor);
            ig.Clear(backColor);

        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                //如果开始绘制，则开始记录鼠标位置
                if ((isDrawing = !isDrawing) == true)
                {
                    startPoint = new Point(e.X, e.Y);
                    oldPoint = new Point(e.X, e.Y);
                }
            }
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isDrawing)
            {
                if (drawTool == drawTools.Pen)
                {
                    g.DrawLine(PenStyle, oldPoint, new Point(e.X, e.Y));
                    ig.DrawLine(PenStyle, oldPoint, new Point(e.X, e.Y));
                    oldPoint.X = e.X;
                    oldPoint.Y = e.Y;
                }
                else if (drawTool == drawTools.Rectangle)
                {
                    //首先恢复此次操作之前的图像，然后再添加Rectangle
                    this.Form1_Paint(this, new PaintEventArgs(this.CreateGraphics(), this.ClientRectangle));
                    g.DrawRectangle(new Pen(foreColor, 1), startPoint.X, startPoint.Y, e.X - startPoint.X, e.Y - startPoint.Y);
                }
            }

        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            isDrawing = false;
            if (drawTool == drawTools.Rectangle)
            {
                ig.DrawRectangle(new Pen(foreColor, 1), startPoint.X, startPoint.Y, e.X - startPoint.X, e.Y - startPoint.Y);
            }


        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            /*
            //将Image中保存的图像，绘制出来
            Graphics g = this.CreateGraphics();
            if (bitmap1 != null)
            {
                g.Clear(Color.White);
                g.DrawImage(bitmap1, this.ClientRectangle);
            }
            */
        }

        void save_image_to_drive()
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                String filename1 = filename + ".jpg";
                String filename2 = filename + ".bmp";
                String filename3 = filename + ".png";

                try
                {
                    bitmap1.Save(@filename1, ImageFormat.Jpeg);
                    bitmap1.Save(@filename2, ImageFormat.Bmp);
                    bitmap1.Save(@filename3, ImageFormat.Png);

                    richTextBox1.Text += "存檔成功\n";
                    richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename3 + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
            else
                richTextBox1.Text += "無圖可存\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            g.Clear(backColor);
            ig.Clear(backColor);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                foreColor = colorDialog1.Color;
                PenStyle.Color = foreColor;
            }

        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            PenStyle.Width = (int)numericUpDown1.Value;
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton1.Checked == true)
                drawTool = drawTools.Pen;
            else if (radioButton2.Checked == true)
                drawTool = drawTools.Line;
            else if (radioButton3.Checked == true)
                drawTool = drawTools.Rectangle;
            else if (radioButton4.Checked == true)
                drawTool = drawTools.Circle;
            else if (radioButton5.Checked == true)
                drawTool = drawTools.String;
            else if (radioButton6.Checked == true)
                drawTool = drawTools.Erase;
            else
                drawTool = drawTools.None;

        }

        private void Form1_SizeChanged(object sender, EventArgs e)
        {
            this.Form1_Paint(this, new PaintEventArgs(this.CreateGraphics(), this.ClientRectangle));
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            g.Clear(backColor);
            ig.Clear(backColor);

        }


    }
}
