using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_PictureSpilit
{
    public partial class Form1 : Form
    {
        PictureBox[,] pbox = new PictureBox[3, 3];
        List<PictureBox> pbox_list = new List<PictureBox>();    //把所有pbox集合起來

        private const int COLUMN = 4;
        private const int ROW = 3;
        int x_st = 100;
        int y_st = 100;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            RemoveAllPictureBox();
            SpilitPicture();
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
            string filename = @"C:\______test_files\picture1.jpg";

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

            for (int x = 0; x < COLUMN; x++)     //COLUMN
            {
                for (int y = 0; y < ROW; y++) //ROW
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

            string filename = @"C:\______test_files\picture1.jpg";

            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            int w = W / COLUMN;
            int h = H / ROW;
            int dx = w * 12 / 10;
            int dy = h * 12 / 10;
            dx = w + 0;
            dy = h + 0;

            int index = 0;

            for (int x = 0; x < COLUMN; x++)     //COLUMN
            {
                for (int y = 0; y < ROW; y++) //ROW
                {
                    pbox[sequence[index] % COLUMN, sequence[index] / COLUMN].Location = new Point(x_st + x * dx, y_st + y * dy);
                    index++;
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "pbox_list 個數 " + pbox_list.Count.ToString() + "\n";
            richTextBox1.Text += "COLUMN = " + pbox.GetLength(0).ToString() + "\n";
            richTextBox1.Text += "ROW = " + pbox.GetLength(1).ToString() + "\n";

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
            }
        }
    }
}

