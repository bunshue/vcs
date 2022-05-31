using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Windows.Forms;

using System.Drawing.Imaging;
using System.IO;

namespace vcs_Warholizer
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Warholize.
        private void btnGo_Click(object sender, EventArgs e)
        {
            pictureBox2.Image = null;
            pictureBox2.Refresh();

            // Get the input and output color data.
            PictureBox[] in_boxes = { picFromColor0, picFromColor1, picFromColor2, picFromColor3, picFromColor4 };
            PictureBox[] out_boxes = { picToColor0, picToColor1, picToColor2, picToColor3, picToColor4 };
            byte[] in_r = new byte[in_boxes.Length];
            byte[] in_g = new byte[in_boxes.Length];
            byte[] in_b = new byte[in_boxes.Length];
            byte[] out_r = new byte[in_boxes.Length];
            byte[] out_g = new byte[in_boxes.Length];
            byte[] out_b = new byte[in_boxes.Length];
            for (int i = 0; i < in_boxes.Length; i++)
            {
                in_r[i] = in_boxes[i].BackColor.R;
                in_g[i] = in_boxes[i].BackColor.G;
                in_b[i] = in_boxes[i].BackColor.B;
                out_r[i] = out_boxes[i].BackColor.R;
                out_g[i] = out_boxes[i].BackColor.G;
                out_b[i] = out_boxes[i].BackColor.B;
            }

            // Get and lock the Bitmap32.
            Bitmap original_bm = pictureBox1.Image as Bitmap;
            Bitmap bm = new Bitmap(original_bm);
            Bitmap32 bm32 = new Bitmap32(bm);
            bm32.LockBitmap();

            // Process the pixels.
            for (int y = 0; y < bm.Height; y++)
            {
                for (int x = 0; x < bm.Width; x++)
                {
                    // Process pixel (row, col).
                    byte r, g, b, a;
                    bm32.GetPixel(x, y, out r, out g, out b, out a);
                    int best_i = 0;
                    int best_dist = int.MaxValue;
                    for (int i = 0; i < in_boxes.Length; i++)
                    {
                        // Compute the distance from this pixel to input pixel i.
                        int dr = r - in_r[i];
                        int dg = g - in_g[i];
                        int db = b - in_b[i];
                        int dist = dr * dr + dg * dg + db * db;

                        // See if this is an improvement.
                        if (dist < best_dist)
                        {
                            best_dist = dist;
                            best_i = i;
                        }
                    }

                    // Update the pixel.
                    bm32.SetPixel(x, y, out_r[best_i], out_g[best_i], out_b[best_i], 255);
                }
            }

            // Unlock the Bitmap32.
            bm32.UnlockBitmap();

            // Display the result.
            pictureBox2.Image = bm;
        }

        // Let the user pick a new color.
        private void picColor_Click(object sender, EventArgs e)
        {
            PictureBox pic = sender as PictureBox;
            cdColor.Color = pic.BackColor;
            if (cdColor.ShowDialog() == DialogResult.OK)
            {
                pic.BackColor = cdColor.Color;
            }
        }

        // Let the user select a file.
        private void mnuFileOpen_Click(object sender, EventArgs e)
        {
            if (ofdOriginal.ShowDialog() == DialogResult.OK)
            {
                int margin = pictureBox1.Left;
                pictureBox1.Image = Bitmap.FromFile(ofdOriginal.FileName);
                pictureBox2.Image = null;
                pictureBox2.Left = pictureBox1.Right + margin;
                pictureBox2.ClientSize = pictureBox1.ClientSize;
                this.ClientSize = new Size(
                    pictureBox2.Right + margin,
                    pictureBox2.Bottom + margin);
            }
        }

        // Save the result image.
        private void mnuFileSave_Click(object sender, EventArgs e)
        {
            //自動檔名 與 存檔語法
            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            try
            {
                //bitmap1.Save(@file1, ImageFormat.Jpeg);
                pictureBox2.Image.Save(filename, ImageFormat.Bmp);
                //bitmap1.Save(@file3, ImageFormat.Png);

                //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                //richTextBox1.Text += "已存檔 : " + filename + "\n";
                //richTextBox1.Text += "已存檔 : " + file3 + "\n";
            }
            catch (Exception ex)
            {
                //richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        // Standard color sets.
        private void mnuColorsSet1_Click(object sender, EventArgs e)
        {
            picFromColor0.BackColor = Color.Red;
            picFromColor1.BackColor = Color.Green;
            picFromColor2.BackColor = Color.Blue;
            picFromColor3.BackColor = Color.Black;
            picFromColor4.BackColor = Color.White;
            picToColor0.BackColor = Color.Red;
            picToColor1.BackColor = Color.Green;
            picToColor2.BackColor = Color.Blue;
            picToColor3.BackColor = Color.Black;
            picToColor4.BackColor = Color.White;
        }

        private void mnuColorsSet2_Click(object sender, EventArgs e)
        {
            picFromColor0.BackColor = Color.Red;
            picFromColor1.BackColor = Color.Green;
            picFromColor2.BackColor = Color.Blue;
            picFromColor3.BackColor = Color.Black;
            picFromColor4.BackColor = Color.White;
            picToColor0.BackColor = Color.Yellow;
            picToColor1.BackColor = Color.Orange;
            picToColor2.BackColor = Color.Purple;
            picToColor3.BackColor = Color.Violet;
            picToColor4.BackColor = Color.Lime;
        }

        private void mnuColorsSet3_Click(object sender, EventArgs e)
        {
            picFromColor0.BackColor = Color.Pink;
            picFromColor1.BackColor = Color.LightGreen;
            picFromColor2.BackColor = Color.LightBlue;
            picFromColor3.BackColor = Color.Gray;
            picFromColor4.BackColor = Color.White;
            picToColor0.BackColor = Color.Pink;
            picToColor1.BackColor = Color.LightGreen;
            picToColor2.BackColor = Color.LightBlue;
            picToColor3.BackColor = Color.Gray;
            picToColor4.BackColor = Color.White;
        }

        private void mnuColorsSet4_Click(object sender, EventArgs e)
        {
            picFromColor0.BackColor = Color.Red;
            picFromColor1.BackColor = Color.Green;
            picFromColor2.BackColor = Color.Blue;
            picFromColor3.BackColor = Color.Black;
            picFromColor4.BackColor = Color.White;
            picToColor0.BackColor = Color.Pink;
            picToColor1.BackColor = Color.LightGreen;
            picToColor2.BackColor = Color.LightBlue;
            picToColor3.BackColor = Color.Gray;
            picToColor4.BackColor = Color.Khaki;
        }
    }
}
