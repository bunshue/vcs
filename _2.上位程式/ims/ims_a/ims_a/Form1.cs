using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace ims_a
{
    public partial class Form1 : Form
    {

        private const int LAYER0_WIDTH = 1920;
        private const int LAYER0_HEIGHT = 1080;
        private const int LAYER1_WIDTH = 1216;
        private const int LAYER1_HEIGHT = 912;
        private const int LAYER2_WIDTH = 640;
        private const int LAYER2_HEIGHT = 480;
        private const int LAYER3_WIDTH = 1920;
        private const int LAYER3_HEIGHT = 1080;

        private const int LAYER1_START_X = (LAYER0_WIDTH - LAYER1_WIDTH - BORDER_X);
        private const int LAYER1_START_Y = BORDER_Y;

        private const int LAYER2_START_X = BORDER_X;
        private const int LAYER2_START_Y = (LAYER0_HEIGHT - LAYER2_HEIGHT - BORDER_Y);

        private const int CAMERA_X = 640;
        private const int CAMERA_Y = 480;
        private const int BORDER_X = 16;
        private const int BORDER_Y = 16;


        Graphics g;
        Pen p;

        public Form1()
        {
            InitializeComponent();
            g = pictureBox1.CreateGraphics();
            p = new Pen(Color.Red, 5);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int i;
            int tmp1 = LAYER0_WIDTH - LAYER1_WIDTH - BORDER_X;
            int tmp2 = BORDER_Y;
            int tmp3 = LAYER1_WIDTH;
            int tmp4 = LAYER1_HEIGHT;

            int pic_width = 760;
            int pic_height = 384;

            int ratio = 3;
            int ratio2 = 6;

            int offset_x = 50;
            int offset_y = 50;

            g.DrawRectangle(p, tmp1 / ratio + offset_x, tmp2 / ratio + offset_y, tmp3 / ratio, tmp4 / ratio);

            tmp1 += (LAYER1_WIDTH - pic_width) / 2;
            tmp2 += (LAYER1_HEIGHT - pic_height) / 2;
            tmp3 = pic_width;
            tmp4 = pic_height;

            g.DrawRectangle(p, tmp1 / ratio + offset_x, tmp2 / ratio + offset_y, tmp3 / ratio, tmp4 / ratio);

            g.DrawRectangle(p, 0 + offset_x, 0 + offset_y, LAYER0_WIDTH / ratio, LAYER0_HEIGHT / ratio);							//Layer0

            g.DrawRectangle(p, LAYER1_START_X / ratio + offset_x, LAYER1_START_Y / ratio + offset_y, LAYER1_WIDTH / ratio, LAYER1_HEIGHT / ratio);		//Layer1

            g.DrawRectangle(p, LAYER2_START_X / ratio + offset_x, LAYER2_START_Y / ratio + offset_y, LAYER2_WIDTH / ratio, LAYER2_HEIGHT / ratio);		//Layer2

            tmp1 = 600;
            tmp2 = 2800;
            tmp3 = LAYER1_WIDTH;
            tmp4 = LAYER1_HEIGHT;
            g.DrawRectangle(p, tmp1 / ratio2, tmp2 / ratio2, tmp3 / ratio2, tmp4 / ratio2);

            tmp1 += (LAYER1_WIDTH - pic_width) / 2;
            tmp2 += (LAYER1_HEIGHT - pic_height) / 2;
            tmp3 = pic_width;
            tmp4 = pic_height;
            g.DrawRectangle(p, tmp1 / ratio2, tmp2 / ratio2, tmp3 / ratio2, tmp4 / ratio2);

            tmp1 = 2000;
            tmp2 = 2800;
            tmp3 = LAYER1_WIDTH;
            tmp4 = LAYER1_HEIGHT;
            g.DrawRectangle(p, tmp1 / ratio2, tmp2 / ratio2, tmp3 / ratio2, tmp4 / ratio2);

            tmp1 += (LAYER1_WIDTH - pic_width) / 2;
            tmp2 += (LAYER1_HEIGHT - pic_height) / 2;
            tmp3 = pic_width;
            tmp4 = pic_height;
            g.DrawRectangle(p, tmp1 / ratio2, tmp2 / ratio2, tmp3 / ratio2, tmp4 / ratio2);

            tmp1 = 600 + 1400 + 1400;
            tmp2 = 2800;
            tmp3 = LAYER1_WIDTH;
            tmp4 = LAYER1_HEIGHT;
            g.DrawRectangle(p, tmp1 / ratio2, tmp2 / ratio2, tmp3 / ratio2, tmp4 / ratio2);

            tmp1 += (LAYER1_WIDTH - pic_width) / 2;
            tmp2 += (LAYER1_HEIGHT - pic_height) / 2;
            tmp3 = pic_width;
            tmp4 = pic_height;
            g.DrawRectangle(p, tmp1 / ratio2, tmp2 / ratio2, tmp3 / ratio2, tmp4 / ratio2);

            tmp1 = 600 + 1400 + 1400 + 1400;
            tmp2 = 2800;
            tmp3 = LAYER1_WIDTH;
            tmp4 = LAYER1_HEIGHT;
            g.DrawRectangle(p, tmp1 / ratio2, tmp2 / ratio2, tmp3 / ratio2, tmp4 / ratio2);

            tmp1 += (LAYER1_WIDTH - pic_width) / 2;
            tmp2 += (LAYER1_HEIGHT - pic_height) / 2;
            tmp3 = pic_width;
            tmp4 = pic_height;
            g.DrawRectangle(p, tmp1 / ratio2, tmp2 / ratio2, tmp3 / ratio2, tmp4 / ratio2);
        }
    }
}
