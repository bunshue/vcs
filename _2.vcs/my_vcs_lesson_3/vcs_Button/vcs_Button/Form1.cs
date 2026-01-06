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
            show_item_location();

            this.AllowDrop = true;//for 程序執行時拖曳組件

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

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

            button1a.Location = new Point(0, 0);

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
            button1b.Location = new Point(220, 0);
            button1b.SetBounds(
                button1b.Location.X,
                button1b.Location.Y,
                200, 200);	//SetBounds : 設定控件的位置與大小

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //繪製圓角按鈕 BMW
            SetButtonRegion();

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //文字化按鈕 button4 ST
            GraphicsPath gpstirng = new GraphicsPath();
            FontFamily family = new FontFamily("細明體");
            int fontStyle = (int)FontStyle.Italic;
            int emSize = 40;

            Point origin = new Point(0, 0);
            StringFormat format = StringFormat.GenericDefault;

            gpstirng.AddString("文字化按鈕", family, fontStyle, emSize, origin, format);
            button4.Region = new Region(gpstirng);
            //文字化按鈕 button4 SP

            bt_exit_setup();

            btn_word_20.Text = "";
            btn_word_21.Text = "";
            btn_word_22.Text = "";
            btn_word_23.Text = "";
            btn_word_24.Text = "";

            btn_word_20.BackgroundImage = new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\__pic\_書畫字圖\_臨江仙\26幾.jpeg");
            btn_word_21.BackgroundImage = new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\__pic\_書畫字圖\_臨江仙\27度.jpeg");
            btn_word_22.BackgroundImage = new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\__pic\_書畫字圖\_臨江仙\28夕.jpeg");
            btn_word_23.BackgroundImage = new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\__pic\_書畫字圖\_臨江仙\29陽.jpeg");
            btn_word_24.BackgroundImage = new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\__pic\_書畫字圖\_臨江仙\30紅.jpeg");
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

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            groupBox1.Size = new Size(500 + 130, 200);
            groupBox1.Location = new Point(10, 10);
            bt_star.Location = new Point(350, 10);
            bt_bmw.Location = new Point(350 + 140, 10);
            button4.Location = new Point(260, 150);//文字化按鈕

            //button
            x_st = 670;
            y_st = 50;
            dx = 108 + 5;
            dy = 108 + 5;
            lb_puzzle.Location = new Point(x_st + dx * 0, y_st + dy * 0 - 30);
            bt_puzzle0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_puzzle1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_puzzle2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_puzzle3.Location = new Point(x_st + dx * 1, y_st + dy * 1);

            //button
            x_st = 720 + 200;
            y_st = 10;
            dx = 110 + 10;
            dy = 120 + 10;

            btn_word_00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            btn_word_01.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            btn_word_02.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            btn_word_10.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            btn_word_11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            btn_word_12.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button18.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            btn_word_20.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            btn_word_21.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            btn_word_22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            btn_word_23.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            btn_word_24.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            btn_word_30.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            btn_word_31.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            btn_word_32.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            btn_word_33.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            btn_word_34.Location = new Point(x_st + dx * 4, y_st + dy * 3);

            //button1.BackgroundImage = new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\__pic\_logo\csharp-programming_210700275.jpg.ashx.jpg");
            //button1.BackgroundImageLayout = ImageLayout.None;
            button1.Image = new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\__pic\_logo\csharp-programming_210700275.jpg.ashx.jpg");
            //button1.ImageAlign = ContentAlignment.BottomRight;

            button6.Image = new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\__pic\_logo\csharp-programming_210700275.jpg.ashx.jpg");
            button6.ImageAlign = ContentAlignment.MiddleCenter;
            button6.MouseMove += new MouseEventHandler(button6_MouseMove);
            button6.MouseLeave += new EventHandler(button6_MouseLeave);

            richTextBox1.Size = new Size(600, 200);
            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //this.Size = new Size(1220, 800);
            this.Text = "vcs_Button";
        }

        void button6_MouseMove(object sender, MouseEventArgs e)
        {
            button6.ImageAlign = ContentAlignment.MiddleLeft;
        }

        void button6_MouseLeave(object sender, EventArgs e)
        {
            button6.ImageAlign = ContentAlignment.MiddleCenter;
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1a_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了不規則形狀Button\t向右\n";
        }

        private void button1b_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了不規則形狀Button\t圓形\n";
        }

        //在Button上畫圖
        private void button1b_Paint(object sender, PaintEventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_icon\Recording.bmp";
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
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_貓咪\cat1.png";
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
            richTextBox1.Text += "你按了不規則形狀Button\t文字化按鈕\n";
        }

        private void bt_star_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了不規則形狀Button\tstar\n";
        }

        private void bt_bmw_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了不規則形狀Button\tbmw\n";
        }

        private void bt_star_Paint(object sender, PaintEventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_icon\star.bmp";
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

        public void SetButtonRegion()
        {
            GraphicsPath ButtonPath;
            ButtonPath = new GraphicsPath();
            Rectangle rect = new Rectangle(0, 0, this.bt_bmw.Width, this.bt_bmw.Height);
            ButtonPath = GetRoundedRectPath(rect, 70);
            this.bt_bmw.Region = new Region(ButtonPath);

            Bitmap bmp = new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\__pic\BMW.jfif");

            bt_bmw.BackgroundImageLayout = ImageLayout.Zoom;
            bt_bmw.BackgroundImage = bmp;
        }

        private GraphicsPath GetRoundedRectPath(Rectangle rect, int radius)
        {
            int diameter = radius;
            Rectangle arcRect = new Rectangle(rect.Location, new Size(diameter, diameter));
            GraphicsPath path = new GraphicsPath();
            //   左上角  
            path.AddArc(arcRect, 180, 90);
            //   右上角  
            arcRect.X = rect.Right - diameter;
            path.AddArc(arcRect, 270, 90);
            //   右下角  
            arcRect.Y = rect.Bottom - diameter;
            path.AddArc(arcRect, 0, 90);
            //   左下角  
            arcRect.X = rect.Left;
            path.AddArc(arcRect, 90, 90);
            path.CloseFigure();
            return path;
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

        ContentAlignment image_align = ContentAlignment.TopLeft;
        private void button5_Click(object sender, EventArgs e)
        {
            if (image_align == ContentAlignment.TopLeft)
            {
                //     內容垂直靠上對齊，且水平置中對齊。
                image_align = ContentAlignment.TopCenter;
                button1.ImageAlign = image_align;
            }
            else if (image_align == ContentAlignment.TopCenter)
            {
                //     內容垂直靠上對齊，且水平靠右對齊。
                image_align = ContentAlignment.TopRight;
                button1.ImageAlign = image_align;
            }
            else if (image_align == ContentAlignment.TopRight)
            {
                //     內容垂直居中對齊，且水平靠左對齊。
                image_align = ContentAlignment.MiddleLeft;
                button1.ImageAlign = image_align;
            }
            else if (image_align == ContentAlignment.MiddleLeft)
            {
                //     內容垂直居中對齊，且水平置中對齊。
                image_align = ContentAlignment.MiddleCenter;
                button1.ImageAlign = image_align;
            }
            else if (image_align == ContentAlignment.MiddleCenter)
            {
                //     內容垂直居中對齊，且水平置中對齊。
                image_align = ContentAlignment.MiddleRight;
                button1.ImageAlign = image_align;
            }
            else if (image_align == ContentAlignment.MiddleRight)
            {
                //     內容垂直靠下對齊，且水平靠左對齊。
                image_align = ContentAlignment.BottomLeft;
                button1.ImageAlign = image_align;
            }
            else if (image_align == ContentAlignment.BottomLeft)
            {
                //     內容垂直靠下對齊，且水平置中對齊。
                image_align = ContentAlignment.BottomCenter;
                button1.ImageAlign = image_align;
            }
            else if (image_align == ContentAlignment.BottomCenter)
            {
                //     內容垂直靠下對齊，且水平靠右對齊。
                image_align = ContentAlignment.BottomRight;
                button1.ImageAlign = image_align;
            }
            else if (image_align == ContentAlignment.BottomRight)
            {
                //     內容垂直靠上對齊，且水平靠左對齊。
                image_align = ContentAlignment.TopLeft;
                button1.ImageAlign = image_align;
            }
            else
            {
                richTextBox1.Text += "XXXXXXXXXXXXXXXXXXX\n";
            }
        }

        //------------------------------------------------------------  // 60個

        //程序執行時拖曳組件 ST
        //調用移動方法
        private void bt_puzzle0_MouseDown(object sender, MouseEventArgs e)
        {
            DoDragDrop(bt_puzzle0, DragDropEffects.Move);
        }

        private void bt_puzzle1_MouseDown(object sender, MouseEventArgs e)
        {
            DoDragDrop(bt_puzzle1, DragDropEffects.Move);
        }

        private void bt_puzzle2_MouseDown(object sender, MouseEventArgs e)
        {
            DoDragDrop(bt_puzzle2, DragDropEffects.Move);
        }

        private void bt_puzzle3_MouseDown(object sender, MouseEventArgs e)
        {
            DoDragDrop(bt_puzzle3, DragDropEffects.Move);
        }

        private void Form1_DragDrop(object sender, DragEventArgs e)
        {
            //判斷接對哪個按鈕操作//移動後的坐標
            object data = e.Data.GetData(typeof(Button));
            if (data == bt_puzzle0)
            {
                bt_puzzle0.Top = this.PointToClient(new Point(e.X, e.Y)).Y;
                bt_puzzle0.Left = this.PointToClient(new Point(e.X, e.Y)).X;
            }
            if (data == bt_puzzle1)
            {
                bt_puzzle1.Top = this.PointToClient(new Point(e.X, e.Y)).Y;
                bt_puzzle1.Left = this.PointToClient(new Point(e.X, e.Y)).X;
            }
            if (data == bt_puzzle2)
            {
                bt_puzzle2.Top = this.PointToClient(new Point(e.X, e.Y)).Y;
                bt_puzzle2.Left = this.PointToClient(new Point(e.X, e.Y)).X;
            }
            if (data == bt_puzzle3)
            {
                bt_puzzle3.Top = this.PointToClient(new Point(e.X, e.Y)).Y;
                bt_puzzle3.Left = this.PointToClient(new Point(e.X, e.Y)).X;
            }
        }

        //設置以何種方式移動
        private void Form1_DragEnter(object sender, DragEventArgs e)
        {
            object data = e.Data.GetData(typeof(Button));
            if (data != null)
            {
                e.Effect = DragDropEffects.Move;
            }
            else
            {
                e.Effect = DragDropEffects.None;
            }
        }
        //程序執行時拖曳組件 SP

        //------------------------------------------------------------  // 60個
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


