using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ZoomPicture1
{
    public partial class Form1 : Form
    {
        Graphics g;	//設定一個畫布g
        int ratio = 100;

        bool flag_mouse_down = false;
        int mouse_down_position_x = 0;
        int mouse_down_position_y = 0;
        int mouse_up_position_x = 0;
        int mouse_up_position_y = 0;
        int move_x;
        int move_y;
        int picture_start_position_x = 0;
        int picture_start_position_y = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            g = this.CreateGraphics();	//這個視窗，就是畫布
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Image image = Image.FromFile(@"C:\_git\vcs\_1.data\______test_files1\_case1\pic2.jpg");
            //pictureBox1.Image = image1;
            int width = image.Width;
            int height = image.Height;
            Bitmap bmp = new Bitmap(image, width * ratio / 100, height * ratio / 100);
            //g.DrawImage(bmp, 50, 50);
            //g.DrawImage(bmp, this.ClientSize.Width / 2 - width * ratio / 100 / 2, this.ClientSize.Height / 2 - height * ratio / 100 / 2);

            if (flag_mouse_down == false)
            {
                move_x = mouse_up_position_x - mouse_down_position_x;
                move_y = mouse_up_position_y - mouse_down_position_y;
                picture_start_position_x += move_x;
                picture_start_position_y += move_y;
                g.DrawImage(bmp, this.ClientSize.Width / 2 - width * ratio / 100 / 2 + picture_start_position_x, this.ClientSize.Height / 2 - height * ratio / 100 / 2 + picture_start_position_y);
            }

            //g.DrawImage(bmp, 0, 0);
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)   //根據e.KeyCode分別執行
            {
                case Keys.Add:
                    if (ratio < 500)
                        ratio += 10;
                    this.Refresh();
                    break;
                case Keys.Subtract:
                    if (ratio > 10)
                        ratio -= 10;
                    this.Refresh();
                    break;
                case Keys.Up:
                    picture_start_position_y -= 100;
                    this.Refresh();
                    break;
                case Keys.Down:
                    picture_start_position_y += 100;
                    this.Refresh();
                    break;
                case Keys.Left:
                    picture_start_position_x -= 100;
                    this.Refresh();
                    break;
                case Keys.Right:
                    picture_start_position_x += 100;
                    this.Refresh();
                    break;
                case Keys.NumPad0:
                    ratio = 100;
                    mouse_down_position_x = 0;
                    mouse_down_position_y = 0;
                    mouse_up_position_x = 0;
                    mouse_up_position_y = 0;
                    move_x = 0;
                    move_y = 0;
                    picture_start_position_x = 0;
                    picture_start_position_y = 0;
                    this.Refresh();
                    break;
                default:
                    break;
            }
        }

    }
}
