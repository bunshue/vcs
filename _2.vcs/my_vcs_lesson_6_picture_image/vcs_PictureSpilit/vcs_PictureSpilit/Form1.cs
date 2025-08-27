using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat
using System.Diagnostics;       //for Stopwatch

namespace vcs_PictureSpilit
{
    public partial class Form1 : Form
    {
        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";


        PictureBox[,] pbox = new PictureBox[3, 3];
        List<PictureBox> pbox_list = new List<PictureBox>();    //把所有pbox集合起來
        Stopwatch stopwatch = new Stopwatch();

        private const int COLUMN = 4;
        private const int ROW = 3;
        int border_x = 20;
        int border_y = 20;
        int x_st = 0;
        int y_st = 0;
        int W = 0;
        int H = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            x_st = border_x;
            y_st = border_y;

            show_item_location();

            Bitmap bitmap1 = new Bitmap(filename);
            W = bitmap1.Width;
            H = bitmap1.Height;

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();

            RemoveAllPictureBox();
            SpilitPicture();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 20;
            y_st = 30;
            dx = 130;
            dy = 70;

            x_st = 1300;

            richTextBox1.Location = new Point(x_st + dx * 2, y_st);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            lb_time.Text = "";
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

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;

            int width = 10;
            Pen p = new Pen(Color.Gray, width);
            e.Graphics.DrawRectangle(p, x_st, y_st, W, H);

            int dx = W / COLUMN;
            int dy = H / ROW;
            for (int x = 0; x < W; x += dx)     //COLUMN
            {
                e.Graphics.DrawLine(p, x_st + x, y_st + 0, x_st + x, y_st + H);
            }

            for (int y = 0; y < H; y += dy) //ROW
            {
                e.Graphics.DrawLine(p, x_st + 0, y_st + y, x_st + W, y_st + y);
            }

            e.Graphics.DrawRectangle(p, x_st + W + 100, y_st + 200, W / 2, H / 2);

        }

        void RemoveAllPictureBox()
        {
            //richTextBox1.Text += "遍歷所有控件\n";
            int i;
            for (i = 0; i < 10; i++)
            {
                foreach (Control con in this.Controls)
                {
                    String strControl = con.GetType().ToString();//获得控件的类型
                    String strControlName = con.Name.ToString();//获得控件的名称

                    //richTextBox1.Text += "Type\t" + strControl + "\tName\t" + strControlName + "\n";

                    if (strControl == "System.Windows.Forms.PictureBox")
                    {
                        //richTextBox1.Text += "remove this.....\n";
                        this.Controls.Remove(con);

                    }
                }
            }
            pbox_list.Clear();
        }

        void SpilitPicture()
        {
            pbox_list.Clear();

            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            int w = W / COLUMN;
            int h = H / ROW;
            int dx = w * 12 / 10;
            int dy = h * 12 / 10;
            dx = w + 0;
            dy = h + 0;

            Bitmap bitmap2 = new Bitmap(w, h);
            RectangleF rect;
            pbox = new PictureBox[COLUMN, ROW];

            //Random r = new Random();

            for (int y = 0; y < ROW; y++) //ROW
            {
                for (int x = 0; x < COLUMN; x++)     //COLUMN
                {
                    rect = new RectangleF(x * w, y * h, w, h);
                    bitmap2 = bitmap1.Clone(rect, PixelFormat.Format32bppArgb);

                    pbox[x, y] = new PictureBox();
                    pbox[x, y].Size = new Size(w, h);
                    pbox[x, y].Text = "";
                    pbox[x, y].Location = new Point(x_st + x * dx, y_st + y * dy);
                    //pbox[x, y].Location = new Point(x_st + r.Next(400), y_st + r.Next(400));
                    pbox[x, y].Name = "( " + x.ToString() + ", " + y.ToString() + ")";
                    pbox[x, y].BackColor = Color.Pink;
                    pbox[x, y].BorderStyle = BorderStyle.None;
                    pbox[x, y].SizeMode = PictureBoxSizeMode.Normal;   //圖片Zoom的方法
                    pbox[x, y].BorderStyle = BorderStyle.FixedSingle;
                    pbox[x, y].Image = bitmap2;
                    pbox[x, y].MouseDown += PictureBox_MouseDown;
                    pbox[x, y].MouseMove += PictureBox_MouseMove;
                    pbox[x, y].MouseUp += PictureBox_MouseUp;
                    //panel.Controls.Add(pbox[x, y]);
                    this.Controls.Add(pbox[x, y]);
                    pbox_list.Add(pbox[x, y]);  //把圖加入物件陣列
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //打亂重排

            //RemoveAllPictureBox();  //移除掉目前所有的pbox控件

            Random r = new Random();

            int[] sequence = new int[COLUMN * ROW];
            int i;
            for (i = 0; i < COLUMN * ROW; i++)
            {
                sequence[i] = i;
            }

            for (i = 0; i < sequence.Length; i++)
            {
                richTextBox1.Text += sequence[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";


            int tmp;

            for (i = 0; i < sequence.Length; i++)
            {
                int n = r.Next(sequence.Length);
                //richTextBox1.Text += "第" + i.ToString() + "項和第" + n.ToString() + "項交換\n";
                tmp = sequence[i];
                sequence[i] = sequence[n];
                sequence[n] = tmp;
            }
            /*
            richTextBox1.Text += "結果：";
            for (i = 0; i < sequence.Length; i++)
            {
                richTextBox1.Text += sequence[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";
            */

            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            int w = W / COLUMN;
            int h = H / ROW;
            int dx = w * 12 / 10;
            int dy = h * 12 / 10;
            dx = w + 0;
            dy = h + 0;

            for (i = 0; i < sequence.Length; i++)
            {
                richTextBox1.Text += sequence[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

            /*
            int index = 0;
            for (int y = 0; y < ROW; y++) //ROW
            {
                for (int x = 0; x < COLUMN; x++)     //COLUMN
                {
                    pbox[sequence[index] % COLUMN, sequence[index] / COLUMN].Location = new Point(x_st + x * dx, y_st + y * dy);
                    index++;
                }
            }
            */

            /*
            int index = 0;
            for (index = 0; index < ROW * COLUMN; index++)
            {
                int xx = x_st + W + 100 + r.Next(W / 2 - w);
                int yy = y_st + 200 + r.Next(H / 2 - h);
                pbox[sequence[index] % COLUMN, sequence[index] / COLUMN].Location = new Point(xx, yy);
            }
            */

            int index = 0;
            for (index = 0; index < ROW * COLUMN; index++)
            {
                int xx = x_st + W + 100 + r.Next(W / 2 - w);
                int yy = y_st + 200 + r.Next(H / 2 - h);
                richTextBox1.Text += "index = " + sequence[index].ToString() + " ";
                pbox[sequence[index] % COLUMN, sequence[index] / COLUMN].Location = new Point(xx, yy);
                pbox[sequence[index] % COLUMN, sequence[index] / COLUMN].BringToFront();
            }

            timer1.Enabled = true;

            stopwatch = new Stopwatch();
            // Begin timing
            stopwatch.Start();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "pbox_list 個數 " + pbox_list.Count.ToString() + "\n";
            richTextBox1.Text += "COLUMN = " + pbox.GetLength(0).ToString() + "\n";
            richTextBox1.Text += "ROW = " + pbox.GetLength(1).ToString() + "\n";

            int index = 0;
            //for (int x = 0; x < COLUMN; x++)     //COLUMN
            {
                //for (int y = 0; y < ROW; y++) //ROW

                for (index = 0; index < COLUMN * ROW; index++)
                {
                    //pbox[sequence[index] % COLUMN, sequence[index] / COLUMN].Location = new Point(x_st + x * dx, y_st + y * dy);

                    //int xx = x_st + W + 100 + r.Next(W / 2 - w);
                    //int yy = y_st + 200 + r.Next(H / 2 - h);
                    int ix = index % COLUMN;
                    int iy = index / COLUMN;
                    richTextBox1.Text += "index = " + index.ToString() + "\tpbox[" + ix.ToString() + ", " + iy.ToString() + "] \tlocation = " + pbox[ix, iy].Location.ToString() + "\n";

                    //index++;
                }
            }
        }

        bool flag_pictureBox_mouse_down = false;
        int pictureBox_position_x_old = 0;
        int pictureBox_position_y_old = 0;
        private void PictureBox_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                flag_pictureBox_mouse_down = true;
                //richTextBox1.Text += "Down : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                pictureBox_position_x_old = e.X;
                pictureBox_position_y_old = e.Y;
                ((PictureBox)sender).BringToFront();    //選中的那一片拉到最上層顯示
            }
        }

        private void PictureBox_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_pictureBox_mouse_down == true)
            {
                //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                int dx = e.X - pictureBox_position_x_old;
                int dy = e.Y - pictureBox_position_y_old;

                //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
                ((PictureBox)sender).Location = new Point(((PictureBox)sender).Location.X + dx, ((PictureBox)sender).Location.Y + dy);
            }
        }

        private void PictureBox_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                flag_pictureBox_mouse_down = false;
                //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                int dx = e.X - pictureBox_position_x_old;
                int dy = e.Y - pictureBox_position_y_old;

                //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
                ((PictureBox)sender).Location = new Point(((PictureBox)sender).Location.X + dx, ((PictureBox)sender).Location.Y + dy);


                check_picture_close_position((PictureBox)sender);

                bool check_ok = check_picture_position();
                if (check_ok == true)
                {
                    richTextBox1.Text += "OK ";
                    richTextBox1.Text += "完成";
                    timer1.Enabled = false;
                }
                else
                {
                    richTextBox1.Text += "NG ";
                }
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            long msec = stopwatch.ElapsedMilliseconds;
            lb_time.Text = (msec/1000).ToString() + "."+(msec%1000).ToString("D3") + " 秒\n";

            //richTextBox1.Text += "燒錄驗證完成時間: " + stopwatch.ElapsedMilliseconds.ToString() + " msec\n";

        }

        void check_picture_close_position(PictureBox pbx)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            int w = W / COLUMN;
            int h = H / ROW;
            int dx = w * 12 / 10;
            int dy = h * 12 / 10;
            dx = w + 0;
            dy = h + 0;

            richTextBox1.Text += "position = " + pbx.Location.ToString() + "\n";

            int xx = (pbx.Location.X - border_x) % w;
            int yy = (pbx.Location.Y - border_y) % h;

            int xxx = 0;
            int yyy = 0;

            if (xx < w / 2)
            {
                xxx = (pbx.Location.X / w) * w;
            }
            else
            {
                xxx = (pbx.Location.X / w + 1) * w;
            }

            if (yy < h / 2)
            {
                yyy = (pbx.Location.Y / h) * h;
            }
            else
            {
                yyy = (pbx.Location.Y / h + 1) * h;
            }
            pbx.Location = new Point(border_x + xxx, border_y + yyy);

        }

        bool check_picture_position()
        {
            bool check_picture_position_correct = true;


            //與右邊的那個相比
            for (int y = 0; y < ROW; y++) //ROW
            {
                for (int x = 0; x < (COLUMN-1); x++)     //COLUMN
                {
                    if (pbox[x, y].Location.X > pbox[x + 1, y].Location.X)
                    {
                        check_picture_position_correct = false;
                        break;
                    }
                }
                if (check_picture_position_correct == false)
                    break;
            }

            //與下面的那個相比
            for (int x = 0; x < COLUMN; x++)     //COLUMN
            {
                for (int y = 0; y < (ROW - 1); y++) //ROW
                {
                    if (pbox[x, y+1].Location.Y > pbox[x, y+1].Location.Y)
                    {
                        check_picture_position_correct = false;
                        break;
                    }
                }
                if (check_picture_position_correct == false)
                    break;
            }
            return check_picture_position_correct;
        }

    }
}

