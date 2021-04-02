using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace AtomizationImage
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public Image AtomizationEffect(PictureBox Pict, int effect)
        {
            int Var_W = Pict.Width;
            int Var_H = Pict.Height;
            Bitmap Var_bmp = new Bitmap(Var_W, Var_H);
            Bitmap Var_SaveBmp = (Bitmap)Pict.Image;
            for (int i = 0; i < Var_W; i++)
            {
                for (int j = 0; j < Var_H; j++)
                {
                    Random Var_random = new Random();
                    int k = Var_random.Next(200000);
                    int tem_w = i + k % effect;
                    int tem_h = j + k % effect;
                    if (tem_w >= Var_W)
                        tem_w = Var_W - 1;
                    if (tem_h >= Var_H)
                        tem_h = Var_H - 1;
                    Color tem_Color = Var_SaveBmp.GetPixel(tem_w, tem_h);
                    Var_bmp.SetPixel(i, j, tem_Color);
                }
            }
            return Var_bmp;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = AtomizationEffect(pictureBox1, 10);
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
        }
    }
}
