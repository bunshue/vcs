using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace AcuteImage
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public Image AcuteEffect(PictureBox Pict)
        {
            int Var_W = Pict.Width;
            int Var_H = Pict.Height;
            Bitmap Var_bmp = new Bitmap(Var_W, Var_H);
            Bitmap Var_SaveBmp = (Bitmap)Pict.Image;
            int[] Laplacian = { -1, -1, -1, -1, 9, -1, -1, -1, -1 };
            for (int i = 1; i < Var_W-1; i++)
                for (int j = 1; j < Var_H-1; j++)
                {
                    int tem_r = 0, tem_g = 0, tem_b = 0, tem_index = 0;
                    for (int c=-1;c<=1;c++)
                        for (int r = -1; r <= 1; r++)
                        {
                            Color tem_color = Var_SaveBmp.GetPixel(i + r, j + c);
                            tem_r += tem_color.R * Laplacian[tem_index];
                            tem_g += tem_color.G * Laplacian[tem_index];
                            tem_b += tem_color.B * Laplacian[tem_index];
                            tem_index++;
                        }
                    tem_r = tem_r > 255 ? 255 : tem_r;
                    tem_r = tem_r < 0 ? 0 : tem_r;
                    tem_g = tem_g > 255 ? 255 : tem_g;
                    tem_g = tem_g < 0 ? 0 : tem_g;
                    tem_b = tem_b > 255 ? 255 : tem_b;
                    tem_b = tem_b < 0 ? 0 : tem_b;
                    Var_bmp.SetPixel(i - 1, j - 1, Color.FromArgb(tem_r, tem_g, tem_b));
                }
            return Var_bmp;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = AcuteEffect(pictureBox1);
        }
    }
}
