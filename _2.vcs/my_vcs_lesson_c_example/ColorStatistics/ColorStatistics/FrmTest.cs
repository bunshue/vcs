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
        string filename = @"D:\_git\vcs\_1.data\______test_files1\ims01.bmp";

        List<Statistics.MajorColor> MC;
        int PixelAmount = 0;

        public FrmTest()
        {
            InitializeComponent();
        }

        private void FrmTest_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            pictureBox1.Image = Image.FromFile(filename);

            CmdDeal_Click(sender, e);
        }

        private void CmdOpen_Click(object sender, EventArgs e)
        {
            openFileDialog1.InitialDirectory = @"D:\_git\vcs\_1.data\______test_files1\";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                pictureBox1.Image = (Bitmap)Bitmap.FromFile(openFileDialog1.FileName);
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
                int offset0 = 10;
                int offset1 = 60;
                int offset2 = 180;
                int offset3 = 400;
                int dy = 26;
                double total = 0;
                e.Graphics.Clear(PicR.BackColor);
                Font font = new Font("標楷體", 12);
                SolidBrush B = new SolidBrush(Color.Black);
                e.Graphics.DrawString("顏色", font, B, new PointF(offset1, 0));
                e.Graphics.DrawString("百分比", font, B, new PointF(offset2, 0));
                e.Graphics.DrawString("數量", font, B, new PointF(offset3, 0));
                B.Dispose();
                for (int i = 0; i < MC.Count; i++)
                {
                    B = new SolidBrush(IntToColor(MC[i].Color));

                    e.Graphics.DrawString((i + 1).ToString(), font, B, new PointF(offset0, (i + 1) * dy + 3));

                    e.Graphics.FillRectangle(B, new Rectangle(offset1, (i + 1) * dy, 100, 15));
                    e.Graphics.DrawString(((double)MC[i].Amount / PixelAmount).ToString(), font, B, new PointF(offset2, (i + 1) * dy + 3));
                    total += (double)MC[i].Amount / PixelAmount;
                    e.Graphics.DrawString(MC[i].Amount.ToString(), font, B, new PointF(offset3, (i + 1) * dy + 3));
                    B.Dispose();
                }
                e.Graphics.DrawString(PixelAmount.ToString(), font, Brushes.Red, new PointF(offset2, 22 * dy + 3));

                font.Dispose();
            }
        }

        private void CmdDeal_Click(object sender, EventArgs e)
        {

            if (pictureBox1.Image != null)
            {
                Stopwatch Sw = new Stopwatch();
                Sw.Start();
                MC = Statistics.PrincipalColorAnalysis((Bitmap)pictureBox1.Image, SliderColorAmount.Value, SliderDelta.Value);

                richTextBox1.Text += "len =" + MC.Count.ToString() + "\n";
                int len = MC.Count;
                int i;
                for (i = 0; i < len; i++)
                {
                    richTextBox1.Text += (i + 1).ToString() + "\t" + MC[i].Color + "\t" + MC[i].Amount + "\n";

                }



                Sw.Stop();
                LblStatus.Text = "計算主成分用時: " + Sw.ElapsedMilliseconds.ToString() + " 毫秒";
                PixelAmount = pictureBox1.Image.Width * pictureBox1.Image.Height;
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

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }
    }
}

