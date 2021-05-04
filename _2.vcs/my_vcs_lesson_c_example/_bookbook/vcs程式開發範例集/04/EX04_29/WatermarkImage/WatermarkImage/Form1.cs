using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Imaging;

namespace WatermarkImage
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public Image pp(PictureBox Pict, int x, int y, int R, float better)//R強光照射面的半徑，即」光暈」
        {
            Bitmap Var_Bmp = new Bitmap(Pict.Image, Pict.Width, Pict.Height);//根據圖像實例化Bitmap類
            int tem_W = Var_Bmp.Width;//獲取圖像的寬度
            int tem_H = Var_Bmp.Height;//獲取圖像的高度
            //定義一個Bitmap類的復本
            Bitmap Var_SaveBmp = Var_Bmp.Clone(new RectangleF(0, 0, tem_W, tem_H), System.Drawing.Imaging.PixelFormat.DontCare);
            Point Var_Center = new Point(x, y);//光暈的中心點
            //遍歷圖像中的各象素
            for (int i = tem_W - 1; i >= 1; i--)
            {
                for (int j = tem_H - 1; j >= 1; j--)
                {
                    float Var_Length = (float)Math.Sqrt(Math.Pow((i - Var_Center.X), 2) + Math.Pow((j - Var_Center.Y), 2));//設置光暈的範圍
                    //如果像素位於」光暈」之內
                    if (Var_Length < R)
                    {
                        Color Var_Color = Var_SaveBmp.GetPixel(i, j);
                        int r, g, b;
                        float Var_Pixel = better * (1.0f - Var_Length / R);//設置光亮度的強弱
                        r = Var_Color.R + (int)Var_Pixel;//設置加強後的R值
                        r = Math.Max(0, Math.Min(r, 255));//如果R值不在顏色值的範圍內，對R值進行設置
                        g = Var_Color.G + (int)Var_Pixel;//設置加強後的G值
                        g = Math.Max(0, Math.Min(g, 255));//如果G值不在顏色值的範圍內，對G值進行設置
                        b = Var_Color.B + (int)Var_Pixel;//設置加強後的B值
                        b = Math.Max(0, Math.Min(b, 255));//如果B值不在顏色值的範圍內，對B值進行設置
                        Var_SaveBmp.SetPixel(i, j, Color.FromArgb(255, r, g, b));//將增亮後的像素值回寫到位圖
                    }
                }
            }
            return Var_SaveBmp;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = pp(pictureBox1,49,47,40,100F);
        }
    }
}
