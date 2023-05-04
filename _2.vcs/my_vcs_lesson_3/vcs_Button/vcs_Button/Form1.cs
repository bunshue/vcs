using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;     //for GraphicsPath

namespace vcs_Button
{
    public partial class Form1 : Form
    {
        public enum SwitchState
        {
            On,
            Off
        }

        private SwitchState _state;
        public SwitchState State
        {
            get
            {
                return _state;
            }
            set
            {
                if (_state == value)
                    return;
                _state = value;
                AdjustOnOffButton();
            }
        }


        private void AdjustOnOffButton()
        {
            switch (State)
            {
                case SwitchState.On:
                    OnOffButton.Dock = DockStyle.Top;
                    break;
                case SwitchState.Off:
                    OnOffButton.Dock = DockStyle.Bottom;
                    break;
                default:
                    break;
            }
        }

        public void Toggle()
        {
            State = State == SwitchState.On ? SwitchState.Off : SwitchState.On;
        }

        public Form1()
        {
            InitializeComponent();
            State = SwitchState.Off;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //加選
            //this.button1a.UseVisualStyleBackColor = true;

            // Shape the button.  button1a
            // Define the points in the polygonal path.
            Point[] pts1 = {
                new Point( 20,  60),
                new Point(140,  60),
                new Point(140,  20),
                new Point(220, 100),
                new Point(140, 180),
                new Point(140, 140),
                new Point( 20, 140)
            };

            // Make the GraphicsPath.
            GraphicsPath polygon_path1 = new GraphicsPath(FillMode.Winding);
            polygon_path1.AddPolygon(pts1);

            // Convert the GraphicsPath into a Region.
            Region polygon_region1 = new Region(polygon_path1);

            // Constrain the button to the region.
            button1a.Region = polygon_region1;

            // Make the button big enough to hold the whole region.
            button1a.SetBounds(
                button1a.Location.X,
                button1a.Location.Y,
                pts1[3].X + 5, pts1[4].Y + 5);	//SetBounds : 設定控件的位置與大小



            // Shape the button.  button1b
            // Define the points in the polygonal path.
            int cx = 128 / 2;
            int cy = 128 / 2;
            int r = 128 / 2;
            Point[] pts2 = {
                new Point( cx+(int)(r*Math.Cos(Math.PI*0/180)),  cy+(int)(r*Math.Sin(Math.PI*0/180))),
                new Point( cx+(int)(r*Math.Cos(Math.PI*20/180)),  cy+(int)(r*Math.Sin(Math.PI*20/180))),
                new Point( cx+(int)(r*Math.Cos(Math.PI*40/180)),  cy+(int)(r*Math.Sin(Math.PI*40/180))),
                new Point( cx+(int)(r*Math.Cos(Math.PI*60/180)),  cy+(int)(r*Math.Sin(Math.PI*60/180))),
                new Point( cx+(int)(r*Math.Cos(Math.PI*80/180)),  cy+(int)(r*Math.Sin(Math.PI*80/180))),
                new Point( cx+(int)(r*Math.Cos(Math.PI*100/180)),  cy+(int)(r*Math.Sin(Math.PI*100/180))),
                new Point( cx+(int)(r*Math.Cos(Math.PI*120/180)),  cy+(int)(r*Math.Sin(Math.PI*120/180))),
                new Point( cx+(int)(r*Math.Cos(Math.PI*140/180)),  cy+(int)(r*Math.Sin(Math.PI*140/180))),
                new Point( cx+(int)(r*Math.Cos(Math.PI*160/180)),  cy+(int)(r*Math.Sin(Math.PI*160/180))),
                new Point( cx+(int)(r*Math.Cos(Math.PI*180/180)),  cy+(int)(r*Math.Sin(Math.PI*180/180))),
                new Point( cx+(int)(r*Math.Cos(Math.PI*200/180)),  cy+(int)(r*Math.Sin(Math.PI*200/180))),
                new Point( cx+(int)(r*Math.Cos(Math.PI*220/180)),  cy+(int)(r*Math.Sin(Math.PI*220/180))),
                new Point( cx+(int)(r*Math.Cos(Math.PI*240/180)),  cy+(int)(r*Math.Sin(Math.PI*240/180))),
                new Point( cx+(int)(r*Math.Cos(Math.PI*260/180)),  cy+(int)(r*Math.Sin(Math.PI*260/180))),
                new Point( cx+(int)(r*Math.Cos(Math.PI*280/180)),  cy+(int)(r*Math.Sin(Math.PI*280/180))),
                new Point( cx+(int)(r*Math.Cos(Math.PI*300/180)),  cy+(int)(r*Math.Sin(Math.PI*300/180))),
                new Point( cx+(int)(r*Math.Cos(Math.PI*320/180)),  cy+(int)(r*Math.Sin(Math.PI*320/180))),
                new Point( cx+(int)(r*Math.Cos(Math.PI*340/180)),  cy+(int)(r*Math.Sin(Math.PI*340/180)))
            };

            // Make the GraphicsPath.
            GraphicsPath polygon_path2 = new GraphicsPath(FillMode.Winding);
            polygon_path2.AddPolygon(pts2);

            // Convert the GraphicsPath into a Region.
            Region polygon_region2 = new Region(polygon_path2);

            // Constrain the button to the region.
            button1b.Region = polygon_region2;

            // Make the button big enough to hold the whole region.
            button1b.SetBounds(
                button1b.Location.X,
                button1b.Location.Y,
                200, 200);	//SetBounds : 設定控件的位置與大小





            //文字化按鈕 button4 ST
            GraphicsPath gpstirng = new GraphicsPath();
            FontFamily family = new FontFamily("細明體");
            int fontStyle = (int)FontStyle.Italic;
            int emSize = 55;

            Point origin = new Point(0, 0);
            StringFormat format = StringFormat.GenericDefault;

            gpstirng.AddString("Conan", family, fontStyle, emSize, origin, format);
            button4.Region = new Region(gpstirng);
            //文字化按鈕 button4 SP

            bt_exit_setup();

            btn_word_20.Text = "";
            btn_word_21.Text = "";
            btn_word_22.Text = "";
            btn_word_23.Text = "";
            btn_word_24.Text = "";

            btn_word_20.BackgroundImage = new Bitmap(@"C:\______test_files1\__pic\_書畫字圖\_臨江仙\26幾.jpeg");
            btn_word_21.BackgroundImage = new Bitmap(@"C:\______test_files1\__pic\_書畫字圖\_臨江仙\27度.jpeg");
            btn_word_22.BackgroundImage = new Bitmap(@"C:\______test_files1\__pic\_書畫字圖\_臨江仙\28夕.jpeg");
            btn_word_23.BackgroundImage = new Bitmap(@"C:\______test_files1\__pic\_書畫字圖\_臨江仙\29陽.jpeg");
            btn_word_24.BackgroundImage = new Bitmap(@"C:\______test_files1\__pic\_書畫字圖\_臨江仙\30紅.jpeg");
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void button1a_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "向右\n";
        }

        private void button1b_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "圓形button\n";
        }

        //在Button上畫圖
        private void button1b_Paint(object sender, PaintEventArgs e)
        {
            string filename = @"C:\______test_files1\__pic\_icon\Recording.bmp";
            Bitmap bmp;//實例Bitmap對像
            bmp = new Bitmap(filename);
            Graphics g = e.Graphics;
            TextureBrush myBrush = new TextureBrush(bmp);
            g.FillRectangle(myBrush, this.ClientRectangle);
        }

        private void OnOffButton_Click(object sender, EventArgs e)
        {
            Toggle();
        }

        private void Form1_SizeChanged(object sender, EventArgs e)
        {
            OnOffButton.Height = this.Height / 2;
        }

        private void bt1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Button變大\n";
            bt2.Size = new Size(bt2.Size.Width + 5, bt2.Size.Height + 5);
        }

        private void bt2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Button變大變小\n";
            bt2.Size = new Size(bt2.Size.Width + 5, bt2.Size.Height + 5);
        }

        private void bt3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Button變小\n";
            bt2.Size = new Size(bt2.Size.Width - 5, bt2.Size.Height - 5);
        }

        //在Button上畫圖
        private void button2_Paint(object sender, PaintEventArgs e)
        {
            string filename = @"C:\______test_files1\__pic\_cat\cat1.png";
            Bitmap bmp;//實例Bitmap對像
            bmp = new Bitmap(filename);
            Graphics g = e.Graphics;
            TextureBrush myBrush = new TextureBrush(bmp);
            g.FillRectangle(myBrush, this.ClientRectangle);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "在Button上畫圖\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            MessageBox.Show("你按了快捷键 Alt + F\n只要在Text改 快捷鍵 (&F) 即可");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了文字化按鈕\n";
        }

        private void bt_star_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了不規則形狀Button\n";
        }

        private void bt_star_Paint(object sender, PaintEventArgs e)
        {
            string filename = @"C:\_git\vcs\_2.vcs\______test_files1\__pic\_icon\star.bmp";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            GraphicsPath graphicsPath = CalculateControlGraphicsPath(bitmap1);
            this.bt_star.Region = new Region(graphicsPath);

            this.bt_star.Cursor = Cursors.Hand;
        }

        private static GraphicsPath CalculateControlGraphicsPath(Bitmap bitmap)
        {
            GraphicsPath graphicsPath = new GraphicsPath();
            Color colorTransparent = bitmap.GetPixel(0, 0);
            //Color colorTransparent = Color.Black;
            int colOpaquePixel = 0;
            for (int row = 0; row < bitmap.Height; row++)
            {
                colOpaquePixel = 0;

                for (int col = 0; col < bitmap.Width; col++)
                {
                    if (bitmap.GetPixel(col, row) != colorTransparent)
                    {
                        colOpaquePixel = col;
                        int colNext = col;
                        for (colNext = colOpaquePixel; colNext < bitmap.Width; colNext++)
                        {
                            if (bitmap.GetPixel(colNext, row) == colorTransparent)
                            {
                                break;
                            }
                        }
                        graphicsPath.AddRectangle(new Rectangle(colOpaquePixel, row, colNext - colOpaquePixel, 1));
                        col = colNext;
                    }
                }
            }
            return graphicsPath;
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //臨江仙 幾度夕陽紅 左右顛倒

            Graphics g;

            Font f = new Font("微軟正黑體", 64);
            //f.Style = (int)FontStyle.Bold;

            g = this.btn_word_10.CreateGraphics();
            g.TextRenderingHint = System.Drawing.Text.TextRenderingHint.AntiAliasGridFit;
            g.ScaleTransform(-1, 1);
            g.DrawString("臨", f, Brushes.Black, -110, 0);

            g = this.btn_word_11.CreateGraphics();
            g.TextRenderingHint = System.Drawing.Text.TextRenderingHint.AntiAliasGridFit;
            g.ScaleTransform(-1, 1);
            g.DrawString("江", f, Brushes.Black, -110, 0);

            g = this.btn_word_12.CreateGraphics();
            g.TextRenderingHint = System.Drawing.Text.TextRenderingHint.AntiAliasGridFit;
            g.ScaleTransform(-1, 1);
            g.DrawString("仙", f, Brushes.Black, -110, 0);

            //水平Mirror處理中~~~~~~
            int xx;
            int yy;
            int ww;
            int hh;

            Bitmap bitmap1;
            Bitmap bitmap2;

            bitmap1 = new Bitmap(btn_word_20.BackgroundImage);
            bitmap2 = new Bitmap(btn_word_20.BackgroundImage);
            ww = bitmap2.Width / 2;
            hh = bitmap2.Height / 1;
            for (yy = 0; yy < hh; yy++)
            {
                for (xx = 0; xx < ww; xx++)
                {
                    Color pp = bitmap2.GetPixel(bitmap1.Width - xx - 1, yy);
                    bitmap2.SetPixel(bitmap2.Width - xx - 1, yy, bitmap2.GetPixel(xx, yy));
                    bitmap2.SetPixel(xx, yy, pp);
                }
            }
            btn_word_30.BackgroundImage = bitmap2;
            Application.DoEvents();

            bitmap1 = new Bitmap(btn_word_21.BackgroundImage);
            bitmap2 = new Bitmap(btn_word_21.BackgroundImage);
            ww = bitmap2.Width / 2;
            hh = bitmap2.Height / 1;
            for (yy = 0; yy < hh; yy++)
            {
                for (xx = 0; xx < ww; xx++)
                {
                    Color pp = bitmap2.GetPixel(bitmap1.Width - xx - 1, yy);
                    bitmap2.SetPixel(bitmap2.Width - xx - 1, yy, bitmap2.GetPixel(xx, yy));
                    bitmap2.SetPixel(xx, yy, pp);
                }
            }
            btn_word_31.BackgroundImage = bitmap2;
            Application.DoEvents();

            bitmap1 = new Bitmap(btn_word_22.BackgroundImage);
            bitmap2 = new Bitmap(btn_word_22.BackgroundImage);
            ww = bitmap2.Width / 2;
            hh = bitmap2.Height / 1;
            for (yy = 0; yy < hh; yy++)
            {
                for (xx = 0; xx < ww; xx++)
                {
                    Color pp = bitmap2.GetPixel(bitmap1.Width - xx - 1, yy);
                    bitmap2.SetPixel(bitmap2.Width - xx - 1, yy, bitmap2.GetPixel(xx, yy));
                    bitmap2.SetPixel(xx, yy, pp);
                }
            }
            btn_word_32.BackgroundImage = bitmap2;
            Application.DoEvents();

            bitmap1 = new Bitmap(btn_word_23.BackgroundImage);
            bitmap2 = new Bitmap(btn_word_23.BackgroundImage);
            ww = bitmap2.Width / 2;
            hh = bitmap2.Height / 1;
            for (yy = 0; yy < hh; yy++)
            {
                for (xx = 0; xx < ww; xx++)
                {
                    Color pp = bitmap2.GetPixel(bitmap1.Width - xx - 1, yy);
                    bitmap2.SetPixel(bitmap2.Width - xx - 1, yy, bitmap2.GetPixel(xx, yy));
                    bitmap2.SetPixel(xx, yy, pp);
                }
            }
            btn_word_33.BackgroundImage = bitmap2;
            Application.DoEvents();

            bitmap1 = new Bitmap(btn_word_24.BackgroundImage);
            bitmap2 = new Bitmap(btn_word_24.BackgroundImage);
            ww = bitmap2.Width / 2;
            hh = bitmap2.Height / 1;
            for (yy = 0; yy < hh; yy++)
            {
                for (xx = 0; xx < ww; xx++)
                {
                    Color pp = bitmap2.GetPixel(bitmap1.Width - xx - 1, yy);
                    bitmap2.SetPixel(bitmap2.Width - xx - 1, yy, bitmap2.GetPixel(xx, yy));
                    bitmap2.SetPixel(xx, yy, pp);
                }
            }
            btn_word_34.BackgroundImage = bitmap2;
        }

    }
}
