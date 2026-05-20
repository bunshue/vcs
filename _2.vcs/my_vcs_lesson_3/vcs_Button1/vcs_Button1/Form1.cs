using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;  // for GraphicsPath

namespace vcs_Button1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            this.AllowDrop = true;  //for 程序執行時拖曳組件

            //------------------------------------------------------------  # 60個

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

            //------------------------------------------------------------  # 60個

            //不規則形狀Button ST

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
            button1a.SetBounds(button1a.Location.X, button1a.Location.Y, pts1[3].X + 5, pts1[4].Y + 5);	//SetBounds : 設定控件的位置與大小

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
            button1b.SetBounds(button1b.Location.X, button1b.Location.Y, 200, 200);	//SetBounds : 設定控件的位置與大小


            //文字化按鈕 bt_text ST
            GraphicsPath gp_text = new GraphicsPath();
            FontFamily family = new FontFamily("細明體");
            int fontStyle = (int)FontStyle.Italic;
            int emSize = 40;

            Point origin = new Point(0, 0);
            StringFormat format = StringFormat.GenericDefault;

            gp_text.AddString("文字化按鈕", family, fontStyle, emSize, origin, format);
            bt_text.Region = new Region(gp_text);
            //文字化按鈕 bt_text SP

            //不規則形狀Button SP

            //------------------------------------------------------------  # 60個



        }

        private void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            richTextBox1.Size = new Size(200, 690);
            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            groupBox1.Size = new Size(490, 195);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_star.Location = new Point(350, 10);
            bt_text.Location = new Point(260, 150);//文字化按鈕

            //button
            x_st = 750;
            y_st = 50;
            dx = 108 + 5;
            dy = 108 + 5;
            lb_puzzle.Location = new Point(x_st + dx * 0, y_st + dy * 0 - 30);
            bt_puzzle0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_puzzle1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_puzzle2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_puzzle3.Location = new Point(x_st + dx * 1, y_st + dy * 1);


            //button
            x_st = 220;
            y_st = 210;
            dx = 110 + 5;
            dy = 120 + 5;
            btn_word_00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            btn_word_01.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            btn_word_02.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            btn_word_10.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            btn_word_11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            btn_word_12.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            btn_flip.Location = new Point(x_st + dx * 3, y_st + dy * 2 - 45);
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

            this.Size = new Size(1500, 750);
            this.Text = "vcs_Button1";

            //離開按鈕的寫法
            bt_exit_setup();

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
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

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        int long_click = 0;
        private void button0_Click(object sender, EventArgs e)
        {
            //長按Button離開程式
            richTextBox1.Text += "Click\n";
        }

        //------------------------------------------------------------  // 60個

        //建立按鈕串列 ST
        //建立控件串列 與 共用事件

        Button btn0 = new Button();
        Button btn1 = new Button();
        Button btn2 = new Button();
        Button btn3 = new Button();

        private void button1_Click(object sender, EventArgs e)
        {
            // 建立按鈕串列
            // 建立控件串列
            Button[] btn = new Button[4];
            btn[0] = btn0;   // 設定btn[0]即代表btn0
            btn[1] = btn1;   // 設定btn[1]即代表btn1
            btn[2] = btn2;   // 設定btn[2]即代表btn2
            btn[3] = btn3;   // 設定btn[3]即代表btn3

            // 使用for 迴圈設定btn0~btn3上的Text屬性與Click事件要執行的事MyClick
            int x_st = 800;
            int y_st = 500;
            int dx = 100;
            int dy = 50;

            for (int i = 0; i < 4; i++)
            {
                btn[i].Text = "按鈕 " + i.ToString();
                btn[i].Size = new Size(136, 40);
                btn[i].Location = new Point(x_st + dx * 0, y_st + dy * i);
                btn[i].Click += new EventHandler(MyClick);
                this.Controls.Add(btn[i]);
            }
        }

        // 建立MyClick事件處理函式, 用來處理button1~button4的Click事件
        void MyClick(object sender, EventArgs e)
        {
            Button btn = (Button)sender;   // 將sender轉型成Button物件btn
            richTextBox1.Text += "你按了 " + btn.Name + "\t" + btn.Text + "\n";
        }
        //建立按鈕串列 SP

        //------------------------------------------------------------  // 60個

        int cnt = 0;
        private void button2_Click(object sender, EventArgs e)
        {
            //設定按鈕樣式
            //設定按鈕樣式 FlatStyle
            if (cnt == 0)
            {
                button2.FlatStyle = FlatStyle.Flat;
                button2.Text = "Flat";
            }
            else if (cnt == 1)
            {
                button2.FlatStyle = FlatStyle.Popup;
                button2.Text = "Popup";
            }
            else if (cnt == 2)
            {
                button2.FlatStyle = FlatStyle.Standard;
                button2.Text = "Standard";
            }
            else if (cnt == 3)
            {
                button2.FlatStyle = FlatStyle.System;
                button2.Text = "System";
            }
            cnt++;
            if (cnt > 3)
            {
                cnt = 0;
            }
        }

        //------------------------------------------------------------  // 60個

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
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

        private void btn_flip_Click(object sender, EventArgs e)
        {
            if (btn_flip.Text == "左右顛倒")
            {
                btn_flip.Text = "恢復";

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
            else
            {
                btn_flip.Text = "左右顛倒";

                Graphics g;

                g = this.btn_word_10.CreateGraphics();
                g.Clear(Color.LightCoral);

                g = this.btn_word_11.CreateGraphics();
                g.Clear(Color.LightCoral);

                g = this.btn_word_12.CreateGraphics();
                g.Clear(Color.LightCoral);

                btn_word_30.BackgroundImage = null;
                btn_word_31.BackgroundImage = null;
                btn_word_32.BackgroundImage = null;
                btn_word_33.BackgroundImage = null;
                btn_word_34.BackgroundImage = null;
            }
        }

        //------------------------------------------------------------  # 60個

        //不規則形狀Button ST
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

        private void bt_star_Paint(object sender, PaintEventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_icon\star.bmp";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            GraphicsPath gp = CalculateControlGraphicsPath(bitmap1);
            this.bt_star.Region = new Region(gp);

            this.bt_star.Cursor = Cursors.Hand;
        }

        private static GraphicsPath CalculateControlGraphicsPath(Bitmap bitmap)
        {
            GraphicsPath gp = new GraphicsPath();
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
                        gp.AddRectangle(new Rectangle(colOpaquePixel, row, colNext - colOpaquePixel, 1));
                        col = colNext;
                    }
                }
            }
            return gp;
        }

        private void bt_star_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了不規則形狀Button\tstar\n";
        }

        private void bt_text_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了不規則形狀Button\t文字化按鈕\n";
        }

        //不規則形狀Button SP

        //------------------------------------------------------------  # 60個

        //長按Button離開程式 ST

        private void button0_MouseDown(object sender, MouseEventArgs e)
        {
            long_click = 0;
            timer1.Enabled = true;
            button0.Text = "0 / 5";
        }

        private void button0_MouseMove(object sender, MouseEventArgs e)
        {
            long_click = 0;
            timer1.Enabled = false;
            button0.Text = "長按Button離開程式";
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            richTextBox1.Text += "T ";
            long_click++;
            button0.Text = long_click.ToString() + " / 5";
            if (long_click > 5)
            {
                Application.Exit();
            }
        }

        //長按Button離開程式 SP

        //------------------------------------------------------------  # 60個


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
