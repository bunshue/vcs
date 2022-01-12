using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;

/*
一個簡單的統計圖像主顏色的算法（C#源代碼)

算法的原理很簡單，就是統計出圖像中各種顏色的分布情況，然後取前N個顏色作為主成分。

當然，實際上如果直接對圖像的各通道256個色階進行統計，得到的結果可能是沒有意義的，所以一般都需要先把256個色階線性的隱射到更少的色階范圍。
*/

namespace ColorStatistics
{
    public partial class FrmTest : Form
    {
        List<Statistics.MajorColor> MC;
        int PixelAmount = 0;

        public FrmTest()
        {
            InitializeComponent();
        }

        private void FrmTest_Load(object sender, EventArgs e)
        {
            CmdDeal_Click(sender, e);
        }

        private void CmdOpen_Click(object sender, EventArgs e)
        {
            openFileDialog1.InitialDirectory = @"C:\______test_files\";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                Thumb.Image = (Bitmap)Bitmap.FromFile(openFileDialog1.FileName);
            }
        }

        public static Color IntToColor(int color)
        {
            int R = color & 255;
            int G = (color & 65280) / 256;
            int B = (color & 16711680) / 65536;
            return Color.FromArgb(255, R, G, B);
        }

        private void PicR_Click(object sender, EventArgs e)
        {

        }

        private void PicR_Paint(object sender, PaintEventArgs e)
        {
            if (MC != null)
            {
                double total = 0;
                e.Graphics.Clear(PicR.BackColor);
                Font font = new Font("宋体", 9f);
                SolidBrush B = new SolidBrush(Color.Black);
                e.Graphics.DrawString("      颜色        ", font, B, new PointF(0, 0));
                e.Graphics.DrawString("     百分比      ", font, B, new PointF(120, 0));
                e.Graphics.DrawString("数量", font, B, new PointF(250, 0));
                B.Dispose();
                for (int i = 0; i < MC.Count; i++)
                {
                    B = new SolidBrush(IntToColor(MC[i].Color));
                    e.Graphics.FillRectangle(B, new Rectangle(0, (i + 1) * 20, 100, 15));
                    e.Graphics.DrawString(((double)MC[i].Amount / PixelAmount).ToString(), font, B, new PointF(120, (i + 1) * 20 + 3));
                    total += (double)MC[i].Amount / PixelAmount;
                    e.Graphics.DrawString(MC[i].Amount.ToString(), font, B, new PointF(250, (i + 1) * 20 + 3));
                    B.Dispose();
                }
                e.Graphics.DrawString(PixelAmount.ToString(), font, Brushes.Red, new PointF(120, 22 * 20 + 3));

                font.Dispose();
            }
        }

        private void CmdDeal_Click(object sender, EventArgs e)
        {

            if (Thumb.Image != null)
            {
                Stopwatch Sw = new Stopwatch();
                Sw.Start();
                MC = Statistics.PrincipalColorAnalysis((Bitmap)Thumb.Image, SliderColorAmount.Value, SliderDelta.Value);
                Sw.Stop();
                LblStatus.Text = "计算主成分用时: " + Sw.ElapsedMilliseconds.ToString() + " 毫秒";
                PixelAmount = Thumb.Image.Width * Thumb.Image.Height;
                PicR.Refresh();
            }
        }

        private void SliderColorAmount_Scroll(object sender, EventArgs e)
        {
            LblAmount.Text = SliderColorAmount.Value.ToString();
        }

        private void SliderDelta_Scroll(object sender, EventArgs e)
        {
            LblDelta.Text = SliderDelta.Value.ToString();
        }
    }
}

