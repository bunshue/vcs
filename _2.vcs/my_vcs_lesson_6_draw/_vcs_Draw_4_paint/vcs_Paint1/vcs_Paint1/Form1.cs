using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_Paint1
{
    public partial class Form1 : Form
    {
        Graphics g;
        Graphics ig;        //繪製bitmap的Graphics實例
        Pen PenStyle;
        Pen p;
        Bitmap bitmap1;

        Color foreColor = Color.Red;
        Color backColor = Color.White;

        private Point startPoint, oldPoint; //繪圖時紀錄滑鼠位置
        //枚举类型，各种绘图工具
        private enum drawTools
        {
            Pen = 0, Line, Circle, Rectangle, String, Erase, None
        };
        //当前使用的工具
        //private drawTools drawTool = drawTools.Pen;
        private drawTools drawTool = drawTools.Line;
        private bool isDrawing = false;     //是否正在繪圖

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            comboBox1.SelectedIndex = 1;
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            p = new Pen(Color.Red, 3);
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 800;
            y_st = 10;
            dx = 120;
            dy = 50;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            button25.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 8);

            comboBox1.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            richTextBox1.Size = new Size(richTextBox1.Size.Width, this.Height - richTextBox1.Location.Y - 50);

            pictureBox1.Location = new Point(10, 150);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //指定畫布大小
            pictureBox1.Width = 640;
            pictureBox1.Height = 480;

            //創建一個bitmap
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            ig = Graphics.FromImage(bitmap1);
            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);


            PenStyle = new Pen(foreColor);
            PenStyle.Width = (int)numericUpDown1.Value;
            PenStyle.StartCap = System.Drawing.Drawing2D.LineCap.Round;
            PenStyle.EndCap = System.Drawing.Drawing2D.LineCap.Round;
            PenStyle.Color = foreColor;

            //PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.Bevel;
            PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.Round;

            g.Clear(backColor);
            ig.Clear(backColor);

            pictureBox1.Image = bitmap1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            if (bitmap1 != null)
            {
                //bitmap1 = null;
                //pictureBox1.Image = null;
                g.Clear(backColor);
                ig.Clear(backColor);
                pictureBox1.Image = bitmap1;
            }
            else
            {
                richTextBox1.Text += "尚未開啟檔案\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            bitmap1 = new Bitmap(filename);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            //pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox1.Image = bitmap1; //顯示在 pictureBox1 圖片控制項中
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            switch (comboBox1.SelectedIndex)
            {
                case 0:
                    richTextBox1.Text += "Normal\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
                    break;
                case 1:
                    richTextBox1.Text += "AutoSize\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
                    break;
                case 2:
                    richTextBox1.Text += "CenterImage\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.CenterImage;
                    break;
                case 3:
                    richTextBox1.Text += "StretchImage\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
                    break;
                case 4:
                    richTextBox1.Text += "Zoom\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
                    break;
                default:
                    richTextBox1.Text += "xxxxxxxxxx\n";
                    break;
            }
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
                    /*  原方法
                    bitmap1.Save(@filename1, ImageFormat.Jpeg);
                    bitmap1.Save(@filename2, ImageFormat.Bmp);
                    bitmap1.Save(@filename3, ImageFormat.Png);
                    */

                    //改用匯出picturebox上的內容
                    int w = pictureBox1.Width;
                    int h = pictureBox1.Height;

                    Bitmap bm = new Bitmap(w, h);

                    //panel1.DrawToBitmap(bm, new Rectangle(0, 0, width, height));
                    pictureBox1.DrawToBitmap(bm, new Rectangle(0, 0, w, h));


                    bm.Save(@filename1, ImageFormat.Jpeg);
                    bm.Save(@filename2, ImageFormat.Bmp);
                    bm.Save(@filename3, ImageFormat.Png);

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

        private void button25_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        private void button26_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        /*
        int x_old = 0;
        int y_old = 0;

        bool flag_eraser_mode = false;
        bool enable_erase = false;
        */

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox1.Checked == true)
            {
                //flag_eraser_mode = true;
                //pictureBox1.Visible = false;

                //g = this.CreateGraphics();
                //p = new Pen(Color.Red, 6);
                backColor = Color.White;
                PenStyle = new Pen(backColor);
                PenStyle.Width = (int)numericUpDown1.Value;
                //PenStyle.Color = backColor;
            }
            else
            {
                //flag_eraser_mode = false;
                //pictureBox1.Visible = true;
                PenStyle.Color = foreColor;
            }
        }

        private void button6_Click(object sender, EventArgs e)
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
                //drawTool = drawTools.Pen;
                drawTool = drawTools.Line;
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

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (bitmap1 == null)
                return;

            if (e.Button == MouseButtons.Left)
            {
                //如果开始绘制，则开始记录鼠标位置
                if ((isDrawing = !isDrawing) == true)
                {
                    //isDrawing = true;
                    startPoint = new Point(e.X, e.Y);
                    oldPoint = new Point(e.X, e.Y);
                }
            }
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            //this.Text = e.X.ToString() + ", " + e.Y.ToString();   //same
            this.Text = "(" + System.Windows.Forms.Cursor.Position.X.ToString() + ", " + System.Windows.Forms.Cursor.Position.Y.ToString() + ")";

            if (bitmap1 == null)
                return;

            if (isDrawing == true)
            {
                if (drawTool == drawTools.Pen)
                {
                    g.DrawLine(PenStyle, oldPoint, new Point(e.X, e.Y));
                    ig.DrawLine(PenStyle, oldPoint, new Point(e.X, e.Y));
                    oldPoint.X = e.X;
                    oldPoint.Y = e.Y;
                    pictureBox1.Image = bitmap1;
                }
                else if (drawTool == drawTools.Line)
                {
                    g.DrawLine(PenStyle, oldPoint, new Point(e.X, e.Y));
                    ig.DrawLine(PenStyle, oldPoint, new Point(e.X, e.Y));
                    oldPoint.X = e.X;
                    oldPoint.Y = e.Y;
                    pictureBox1.Image = bitmap1;
                }
                else if (drawTool == drawTools.Rectangle)
                {
                    //首先恢复此次操作之前的图像，然后再添加Rectangle
                    //this.Form1_Paint(this, new PaintEventArgs(this.CreateGraphics(), this.ClientRectangle));
                    //this.pictureBox1_Paint(this, new PaintEventArgs(this.CreateGraphics(), this.ClientRectangle));

                    //g.DrawRectangle(new Pen(foreColor, 1), startPoint.X, startPoint.Y, e.X - startPoint.X, e.Y - startPoint.Y);
                    //ig.DrawRectangle(new Pen(foreColor, 1), startPoint.X, startPoint.Y, e.X - startPoint.X, e.Y - startPoint.Y);
                    pictureBox1.Image = bitmap1;
                }
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (bitmap1 == null)
                return;

            isDrawing = false;
            if (drawTool == drawTools.Rectangle)
            {
                g.DrawRectangle(new Pen(foreColor, 1), startPoint.X, startPoint.Y, e.X - startPoint.X, e.Y - startPoint.Y);
                ig.DrawRectangle(new Pen(foreColor, 1), startPoint.X, startPoint.Y, e.X - startPoint.X, e.Y - startPoint.Y);
                pictureBox1.Image = bitmap1;
            }
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
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
    }
}

