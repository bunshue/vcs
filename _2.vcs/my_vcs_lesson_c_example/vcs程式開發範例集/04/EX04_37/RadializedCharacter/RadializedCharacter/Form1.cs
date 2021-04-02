using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
//新增的命名空間
using System.Drawing.Drawing2D;
using System.Drawing.Text;

namespace RadializedCharacter
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public static Image ImageLightEffect(string Str, Font F, Color ColorFore, Color ColorBack, int BlurConsideration)
        {
            Bitmap Var_Bitmap = null;//實例化Bitmap類
            using (Graphics g = Graphics.FromHwnd(IntPtr.Zero))//實例化Graphics類
            {
                SizeF Var_Size = g.MeasureString(Str, F);//對字串進行測量
                using (Bitmap Var_bmp = new Bitmap((int)Var_Size.Width, (int)Var_Size.Height))//透過文字的大小實例化Bitmap類
                using (Graphics Var_G_Bmp = Graphics.FromImage(Var_bmp))//實例化Bitmap類
                using (SolidBrush Var_BrushBack = new SolidBrush(Color.FromArgb(16, ColorBack.R, ColorBack.G, ColorBack.B)))//根據RGB的值定義畫刷
                using (SolidBrush Var_BrushFore = new SolidBrush(ColorFore))//定義畫刷
                {
                    Var_G_Bmp.SmoothingMode = SmoothingMode.HighQuality;//設定為高質量
                    Var_G_Bmp.InterpolationMode = InterpolationMode.HighQualityBilinear;//設定為高質量的收合
                    Var_G_Bmp.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;//消除鋸齒
                    Var_G_Bmp.DrawString(Str, F, Var_BrushBack, 0, 0);//給制文字
                    Var_Bitmap = new Bitmap(Var_bmp.Width + BlurConsideration, Var_bmp.Height + BlurConsideration);//根據發光文字的大小實例化Bitmap類
                    using (Graphics Var_G_Bitmap = Graphics.FromImage(Var_Bitmap))//實例化Graphics類
                    {
                        Var_G_Bitmap.SmoothingMode = SmoothingMode.HighQuality;//設定為高質量
                        Var_G_Bitmap.InterpolationMode = InterpolationMode.HighQualityBilinear;//設定為高質量的收合
                        Var_G_Bitmap.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;//消除鋸齒
                        //搜尋發光文字的各象素點
                        for (int x = 0; x <= BlurConsideration; x++)
                        {
                            for (int y = 0; y <= BlurConsideration; y++)
                            {
                                Var_G_Bitmap.DrawImageUnscaled(Var_bmp, x, y);//繪製發光文字的點
                            }
                        }
                        Var_G_Bitmap.DrawString(Str, F, Var_BrushFore, BlurConsideration / 2, BlurConsideration / 2);//繪製文字
                    }
                }
            }

            return Var_Bitmap;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            using (Font fnt = new Font("Arial", 40, FontStyle.Bold))//定義字體
            {
                this.pictureBox1.Image = (Bitmap)ImageLightEffect("發光效果文字", fnt, Color.Yellow, Color.Red, 10);//呼叫自定義方法ImageLightEffect
            }
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }
    }
}
