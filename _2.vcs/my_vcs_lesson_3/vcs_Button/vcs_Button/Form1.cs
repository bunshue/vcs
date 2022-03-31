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
            //this.button1.UseVisualStyleBackColor = true;

            // Shape the button.  Button1
            // Define the points in the polygonal path.
            Point[] pts = {
                new Point( 20,  60),
                new Point(140,  60),
                new Point(140,  20),
                new Point(220, 100),
                new Point(140, 180),
                new Point(140, 140),
                new Point( 20, 140)
            };

            // Make the GraphicsPath.
            GraphicsPath polygon_path = new GraphicsPath(FillMode.Winding);
            polygon_path.AddPolygon(pts);

            // Convert the GraphicsPath into a Region.
            Region polygon_region = new Region(polygon_path);

            // Constrain the button to the region.
            button1.Region = polygon_region;

            // Make the button big enough to hold the whole region.
            button1.SetBounds(
                button1.Location.X,
                button1.Location.Y,
                pts[3].X + 5, pts[4].Y + 5);	//SetBounds : 設定控件的位置與大小

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

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "向右\n";
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
            string filename = @"C:\______test_files\__pic\_cat\cat1.png";
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
            string filename = @"C:\______test_files\_icon\star.bmp";
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
    }
}

