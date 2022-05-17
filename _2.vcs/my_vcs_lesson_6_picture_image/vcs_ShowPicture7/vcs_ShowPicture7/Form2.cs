using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ShowPicture7
{
    public partial class Form2 : Form
    {
        string filename = string.Empty;
        public Form2(string pic_filename)
        {
            InitializeComponent();

            filename = pic_filename;
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            //Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式

            int W = bitmap1.Width;
            int H = bitmap1.Height;

            float ratio = 1.0f;

            int WW = Screen.PrimaryScreen.Bounds.Width / 2;
            int HH = Screen.PrimaryScreen.Bounds.Height / 2;

            for (ratio = 1.0f; ratio < 10; ratio += 0.1f)
            {
                if (((W / ratio) < WW) && ((H / ratio) < HH))
                {
                    break;
                }

            }
            //this.Text = "ratio = " + ratio.ToString();

            W = (int)(W / ratio);
            H = (int)(H / ratio);

            pictureBox1.Image = bitmap1;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Location = new Point(0, 0);
            pictureBox1.ClientSize = new Size(W, H);
            this.ClientSize = new Size(W, H);
            //this.Text = "W = " + W.ToString() + ", H = " + H.ToString();

            //this.FormBorderStyle = FormBorderStyle.None;
            this.ShowInTaskbar = false;

            //限制新圖出現的地方
            Random r = new Random();
            int dd = 200;
            WW = Screen.PrimaryScreen.Bounds.Width;
            HH = Screen.PrimaryScreen.Bounds.Height;
            int x_st = dd + r.Next(WW - W - dd);
            int y_st = r.Next(HH - H);
            this.Location = new Point(x_st, y_st);

            this.Text = "W = " + W.ToString() + ", H = " + H.ToString() + ", x = " + x_st.ToString() + ", y = " + y_st.ToString();
        }

        bool flag_pictureBox1_mouse_down = false;
        private const int PB3_DEFAULT_POSITION_X = 600 - 10;
        private const int PB3_DEFAULT_POSITION_Y = 700;
        int pictureBox1_position_x_old = PB3_DEFAULT_POSITION_X;
        int pictureBox1_position_y_old = PB3_DEFAULT_POSITION_Y;
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_pictureBox1_mouse_down = true;
            //richTextBox1.Text += "Down : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            pictureBox1_position_x_old = e.X;
            pictureBox1_position_y_old = e.Y;


        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_pictureBox1_mouse_down == true)
            {
                //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                int dx = e.X - pictureBox1_position_x_old;
                int dy = e.Y - pictureBox1_position_y_old;

                //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
                //pictureBox1.Location = new Point(pictureBox1.Location.X + dx, pictureBox1.Location.Y + dy);
                this.Location = new Point(this.Location.X + dx, this.Location.Y + dy);
            }

        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_pictureBox1_mouse_down = false;
            //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            int dx = e.X - pictureBox1_position_x_old;
            int dy = e.Y - pictureBox1_position_y_old;

            //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
            //pictureBox1.Location = new Point(pictureBox1.Location.X + dx, pictureBox1.Location.Y + dy);
            this.Location = new Point(this.Location.X + dx, this.Location.Y + dy);

        }
    }
}
