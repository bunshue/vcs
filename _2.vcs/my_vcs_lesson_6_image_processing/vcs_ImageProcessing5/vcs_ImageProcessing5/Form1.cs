using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for PixelFormat
using System.IO;    //for Path
using System.Diagnostics;   //for Stopwatch

namespace vcs_ImageProcessing5
{
    public partial class Form1 : Form
    {
        string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";

        Stopwatch sw = new Stopwatch();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

            btnEmboss1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            btnEmboss2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            btnEmboss3.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            btnBlur1.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            btnBlur2.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            btnHighPass1.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            btnHighPass2.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            btnEdge1.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            btnEdge2.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            btnEdge3.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            btnAverage.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            btnGrayscale.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            btnRed.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            btnGreen.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            btnBlue.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            btnInvert.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            label1.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            txtRank.Location = new Point(x_st + dx * 1 + 60, y_st + dy * 6);
            btnMaximum.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            btnMinimum.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            btnPixellate.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            btnPointellate.Location = new Point(x_st + dx * 1, y_st + dy * 10);
            btnGrayscale2.Location = new Point(x_st + dx * 1, y_st + dy * 11);

            bt_image_process_a0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_image_process_a1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_image_process_a2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_image_process_a3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_image_process_a4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            bt_image_process_a5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            bt_image_process_a6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            bt_image_process_a7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            bt_image_process_b0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_image_process_b1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_image_process_b2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_image_process_b3.Location = new Point(x_st + dx * 0, y_st + dy * 3);

            groupBox1.Size = new Size(200 + 20, 220);
            groupBox2.Size = new Size(200 + 20, 420);
            groupBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            groupBox2.Location = new Point(x_st + dx * 2, y_st + dy * 3 + 20);

            pictureBox1.Size = new Size(800, 600);
            pictureBox1.Location = new Point(x_st + dx * 3 + 20, y_st + dy * 0);
            bt_reset.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_reset.Size.Width, pictureBox1.Location.Y);

            richTextBox1.Size = new Size(200, 600);
            richTextBox1.Location = new Point(x_st + dx * 7, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1700, 880);
            this.Text = "vcs_ImageProcessing5";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_reset_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;
        }

        // Apply a filter.
        private void ApplyFilter(Bitmap32.Filter filter)
        {
            Bitmap bm = new Bitmap(filename);

            this.Cursor = Cursors.WaitCursor;
            DateTime start_time = DateTime.Now;

            Bitmap32 bm32 = new Bitmap32(bm);

            // Apply the filter.
            Bitmap32 new_bm32 = bm32.ApplyFilter(filter, false);

            // Display the result.
            pictureBox1.Image = new_bm32.bitmap1;

            DateTime stop_time = DateTime.Now;
            this.Cursor = Cursors.Default;

            TimeSpan elapsed_time = stop_time - start_time;
            richTextBox1.Text += "作業時間 :" + elapsed_time.TotalSeconds.ToString("0.000000") + " 秒\n";
        }

        //浮雕1
        private void btnEmboss1_Click(object sender, EventArgs e)
        {
            ApplyFilter(Bitmap32.EmbossingFilter);
        }

        //浮雕2
        private void btnEmboss2_Click(object sender, EventArgs e)
        {
            ApplyFilter(Bitmap32.EmbossingFilter2);
        }

        //浮雕3
        private void btnEmboss3_Click(object sender, EventArgs e)
        {
            ApplyFilter(Bitmap32.EmbossingFilter3);
        }

        //高斯模糊 5X5
        private void btnBlur1_Click(object sender, EventArgs e)
        {
            ApplyFilter(Bitmap32.BlurFilter5x5Gaussian);
        }

        //平均模糊 5X5
        private void btnBlur2_Click(object sender, EventArgs e)
        {
            ApplyFilter(Bitmap32.BlurFilter5x5Mean);
        }

        //高通1 3X3
        private void btnHighPass1_Click(object sender, EventArgs e)
        {
            ApplyFilter(Bitmap32.HighPassFilter3x3);
        }

        //高通2 5X5
        private void btnHighPass2_Click(object sender, EventArgs e)
        {
            ApplyFilter(Bitmap32.HighPassFilter5x5);
        }

        //邊緣檢測 1
        private void btnEdge1_Click(object sender, EventArgs e)
        {
            ApplyFilter(Bitmap32.EdgeDetectionFilterULtoLR);
        }

        //邊緣檢測 2
        private void btnEdge2_Click(object sender, EventArgs e)
        {
            ApplyFilter(Bitmap32.EdgeDetectionFilterTopToBottom);
        }

        //邊緣檢測 3
        private void btnEdge3_Click(object sender, EventArgs e)
        {
            ApplyFilter(Bitmap32.EdgeDetectionFilterLeftToRight);
        }

        // Average the colors.
        private void btnAverage_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(filename);

            this.Cursor = Cursors.WaitCursor;
            DateTime start_time = DateTime.Now;

            Bitmap32 bm32 = new Bitmap32(bm);

            // Average the colors.
            bm32.Average();

            // Display the result.
            pictureBox1.Image = bm;

            DateTime stop_time = DateTime.Now;
            this.Cursor = Cursors.Default;

            TimeSpan elapsed_time = stop_time - start_time;
            richTextBox1.Text += "作業時間 :" + elapsed_time.TotalSeconds.ToString("0.000000") + " 秒\n";
        }

        // Convert to grayscale.
        private void btnGrayscale_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(filename);

            this.Cursor = Cursors.WaitCursor;
            DateTime start_time = DateTime.Now;

            Bitmap32 bm32 = new Bitmap32(bm);

            // Convert to grayscale.
            bm32.Grayscale();

            // Display the result.
            pictureBox1.Image = bm;

            DateTime stop_time = DateTime.Now;
            this.Cursor = Cursors.Default;

            TimeSpan elapsed_time = stop_time - start_time;
            richTextBox1.Text += "作業時間 :" + elapsed_time.TotalSeconds.ToString("0.000000") + " 秒\n";
        }

        // Convert to a red scale.
        private void btnRed_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(filename);

            this.Cursor = Cursors.WaitCursor;
            DateTime start_time = DateTime.Now;

            Bitmap32 bm32 = new Bitmap32(bm);

            // Convert to red.
            bm32.ClearGreen();
            bm32.ClearBlue();

            // Display the result.
            pictureBox1.Image = bm;

            DateTime stop_time = DateTime.Now;
            this.Cursor = Cursors.Default;

            TimeSpan elapsed_time = stop_time - start_time;
            richTextBox1.Text += "作業時間 :" + elapsed_time.TotalSeconds.ToString("0.000000") + " 秒\n";
        }

        // Convert to a green scale.
        private void btnGreen_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(filename);

            this.Cursor = Cursors.WaitCursor;
            DateTime start_time = DateTime.Now;

            Bitmap32 bm32 = new Bitmap32(bm);

            // Convert to green.
            bm32.ClearRed();
            bm32.ClearBlue();

            // Display the result.
            pictureBox1.Image = bm;

            DateTime stop_time = DateTime.Now;
            this.Cursor = Cursors.Default;

            TimeSpan elapsed_time = stop_time - start_time;
            richTextBox1.Text += "作業時間 :" + elapsed_time.TotalSeconds.ToString("0.000000") + " 秒\n";
        }

        // Convert to a blue scale.
        private void btnBlue_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(filename);

            this.Cursor = Cursors.WaitCursor;
            DateTime start_time = DateTime.Now;

            Bitmap32 bm32 = new Bitmap32(bm);

            // Convert to blue.
            bm32.ClearRed();
            bm32.ClearGreen();

            // Display the result.
            pictureBox1.Image = bm;

            DateTime stop_time = DateTime.Now;
            this.Cursor = Cursors.Default;

            TimeSpan elapsed_time = stop_time - start_time;
            richTextBox1.Text += "作業時間 :" + elapsed_time.TotalSeconds.ToString("0.000000") + " 秒\n";
        }

        // Invert the image.
        private void btnInvert_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(filename);

            this.Cursor = Cursors.WaitCursor;
            DateTime start_time = DateTime.Now;

            Bitmap32 bm32 = new Bitmap32(bm);

            // Convert to blue.
            bm32.Invert();

            // Display the result.
            pictureBox1.Image = bm;

            DateTime stop_time = DateTime.Now;
            this.Cursor = Cursors.Default;

            TimeSpan elapsed_time = stop_time - start_time;
            richTextBox1.Text += "作業時間 :" + elapsed_time.TotalSeconds.ToString("0.000000") + " 秒\n";
        }

        // Pick the maximum brightness for pixels in areas.
        private void btnMaximum_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(filename);

            this.Cursor = Cursors.WaitCursor;
            DateTime start_time = DateTime.Now;

            Bitmap32 bm32 = new Bitmap32(bm);

            // Pick the maximum brightness colors.
            Bitmap32 new_bm32 = bm32.RankMaximum(int.Parse(txtRank.Text), false);

            // Display the result.
            pictureBox1.Image = new_bm32.bitmap1;

            DateTime stop_time = DateTime.Now;
            this.Cursor = Cursors.Default;

            TimeSpan elapsed_time = stop_time - start_time;
            richTextBox1.Text += "作業時間 :" + elapsed_time.TotalSeconds.ToString("0.000000") + " 秒\n";
        }

        // Pick the minimum brightness for pixels in areas.
        private void btnMinimum_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(filename);

            this.Cursor = Cursors.WaitCursor;
            DateTime start_time = DateTime.Now;

            Bitmap32 bm32 = new Bitmap32(bm);

            // Pick the minimum brightness colors.
            Bitmap32 new_bm32 = bm32.RankMinimum(int.Parse(txtRank.Text), false);

            // Display the result.
            pictureBox1.Image = new_bm32.bitmap1;

            DateTime stop_time = DateTime.Now;
            this.Cursor = Cursors.Default;

            TimeSpan elapsed_time = stop_time - start_time;
            richTextBox1.Text += "作業時間 :" + elapsed_time.TotalSeconds.ToString("0.000000") + " 秒\n";
        }

        // Pixellate the image.
        private void btnPixellate_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(filename);

            this.Cursor = Cursors.WaitCursor;
            DateTime start_time = DateTime.Now;

            Bitmap32 bm32 = new Bitmap32(bm);

            // Pixellate.
            bm32.Pixellate(int.Parse(txtRank.Text), false);

            // Display the result.
            pictureBox1.Image = bm;

            DateTime stop_time = DateTime.Now;
            this.Cursor = Cursors.Default;

            TimeSpan elapsed_time = stop_time - start_time;
            richTextBox1.Text += "作業時間 :" + elapsed_time.TotalSeconds.ToString("0.000000") + " 秒\n";
        }

        // Pointellate the image.
        private void btnPointellate_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(filename);

            this.Cursor = Cursors.WaitCursor;
            DateTime start_time = DateTime.Now;

            Bitmap32 bm32 = new Bitmap32(bm);

            // Pixellate.
            int rank = int.Parse(txtRank.Text);
            Bitmap new_bm = bm32.Pointellate(rank, rank, false);

            // Display the result.
            pictureBox1.Image = new_bm;

            DateTime stop_time = DateTime.Now;
            this.Cursor = Cursors.Default;

            TimeSpan elapsed_time = stop_time - start_time;
            richTextBox1.Text += "作業時間 :" + elapsed_time.TotalSeconds.ToString("0.000000") + " 秒\n";
        }

        private void btnGrayscale2_Click(object sender, EventArgs e)
        {
            //用Bitmap32做灰階

            Bitmap bitmap1 = new Bitmap(filename);

            int W = bitmap1.Width;
            int H = bitmap1.Height;

            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";

            // Make a Bitmap32 object.
            Bitmap32 bm32 = new Bitmap32(bitmap1);

            // Lock the bitmap.
            bm32.LockBitmap();

            // Process the pixels.
            for (int x = 0; x < W; x++)
            {
                for (int y = 0; y < H; y++)
                {
                    byte r = bm32.GetRed(x, y);
                    byte g = bm32.GetGreen(x, y);
                    byte b = bm32.GetBlue(x, y);
                    byte gray = (byte)(0.3 * r + 0.5 * g + 0.2 * b);
                    bm32.SetPixel(x, y, gray, gray, gray, 255);
                }
            }
            bm32.UnlockBitmap();

            pictureBox1.Image = bitmap1;
        }

        private void DisplayWarpedImage(Bitmap32.WarpOperations warp_op)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            //Bitmap bitmap1 = new Bitmap(filename);

            Bitmap bm = new Bitmap(filename);
            pictureBox1.Image = bm;

            this.Cursor = Cursors.WaitCursor;
            DateTime start_time = DateTime.Now;

            // Make a Bitmap32 object.
            Bitmap32 bm32 = new Bitmap32(bm);

            // Apply the warping operation.
            Bitmap32 new_bm32 = bm32.Warp(warp_op, false);

            // Display the result.
            pictureBox1.Image = new_bm32.bitmap1;

            DateTime stop_time = DateTime.Now;
            this.Cursor = Cursors.Default;

            //TimeSpan elapsed_time = stop_time - start_time;
            //lb_elapsed.Text = elapsed_time.TotalSeconds.ToString("0.000000");
        }

        private void bt_image_process_a0_Click(object sender, EventArgs e)
        {
            //Fish Eye
            DisplayWarpedImage(Bitmap32.WarpOperations.FishEye);
        }

        private void bt_image_process_a1_Click(object sender, EventArgs e)
        {
            //Twist
            DisplayWarpedImage(Bitmap32.WarpOperations.Twist);
        }

        private void bt_image_process_a2_Click(object sender, EventArgs e)
        {
            //Wave
            DisplayWarpedImage(Bitmap32.WarpOperations.Wave);
        }

        private void bt_image_process_a3_Click(object sender, EventArgs e)
        {
            //Small Top
            DisplayWarpedImage(Bitmap32.WarpOperations.SmallTop);
        }

        private void bt_image_process_a4_Click(object sender, EventArgs e)
        {
            //Wiggles
            DisplayWarpedImage(Bitmap32.WarpOperations.Wiggles);
        }

        private void bt_image_process_a5_Click(object sender, EventArgs e)
        {
            //Double Wave
            DisplayWarpedImage(Bitmap32.WarpOperations.DoubleWave);
        }

        private void bt_image_process_a6_Click(object sender, EventArgs e)
        {

        }

        private void bt_image_process_a7_Click(object sender, EventArgs e)
        {

        }

        private const int NUM_TRIALS = 5;
        // Invert the image without Lockbits.
        private void bt_image_process_b0_Click(object sender, EventArgs e)
        {
            //No Lock Bits
            const byte BYTE_255 = 255;
            Cursor = Cursors.WaitCursor;

            sw.Reset();
            sw.Start();

            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            for (int trial = 0; trial < NUM_TRIALS; trial++)
            {
                // Invert the pixels.
                byte red, green, blue;
                for (int y = 0; y < bitmap1.Height; y++)
                {
                    for (int x = 0; x < bitmap1.Width; x++)
                    {
                        Color clr = bitmap1.GetPixel(x, y);
                        red = (byte)(BYTE_255 - clr.R);
                        green = (byte)(BYTE_255 - clr.G);
                        blue = (byte)(BYTE_255 - clr.B);
                        clr = Color.FromArgb(
                            255 - clr.R,
                            255 - clr.G,
                            255 - clr.B);

                        bitmap1.SetPixel(x, y, Color.FromArgb(red, green, blue));
                    }
                }
            }
            pictureBox1.Image = bitmap1;
            Cursor = Cursors.Default;
            sw.Stop();
            richTextBox1.Text += "耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";

            richTextBox1.Text += "經過時間 : " + sw.Elapsed.TotalSeconds.ToString("0.000000") + " 秒\n";


        }

        // Invert the image using Lockbits.
        private void bt_image_process_b1_Click(object sender, EventArgs e)
        {
            //Lock Bits
            const byte BYTE_255 = 255;

            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            Cursor = Cursors.WaitCursor;

            sw.Reset();
            sw.Start();

            for (int trial = 0; trial < NUM_TRIALS; trial++)
            {
                // Make a Bitmap32 object.
                Bitmap32 bm32 = new Bitmap32(bitmap1);

                // Lock the bitmap.
                bm32.LockBitmap();

                // Invert the pixels.
                byte red, green, blue, alpha;
                for (int y = 0; y < bm32.Height; y++)
                {
                    for (int x = 0; x < bm32.Width; x++)
                    {
                        bm32.GetPixel(x, y, out red, out green, out blue, out alpha);
                        red = (byte)(BYTE_255 - red);
                        green = (byte)(BYTE_255 - green);
                        blue = (byte)(BYTE_255 - blue);
                        bm32.SetPixel(x, y, red, green, blue, alpha);
                    }
                }

                /*
                //same but slower
                // Invert the pixels.
                for (int i = 0; i < bm.Height * bm32.RowSizeBytes; i++)
                {
                    // bm32.ImageBytes[i] = Convert.ToByte(BYTE_255 - bm32.ImageBytes[i]);
                    bm32.ImageBytes[i] = (byte)(BYTE_255 - bm32.ImageBytes[i]);
                }
                */

                // Unlock the bitmap.
                bm32.UnlockBitmap();
            }
            pictureBox1.Image = bitmap1;

            Cursor = Cursors.Default;
            sw.Stop();
            richTextBox1.Text += "耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";

            richTextBox1.Text += "經過時間 : " + sw.Elapsed.TotalSeconds.ToString("0.000000") + " 秒\n";

        }

        private void bt_image_process_b2_Click(object sender, EventArgs e)
        {
            //Quarter
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            Cursor = Cursors.WaitCursor;

            sw.Reset();
            sw.Start();

            // Make a Bitmap32 object.
            Bitmap32 bm32 = new Bitmap32(bitmap1);

            // Lock the bitmap.
            bm32.LockBitmap();

            // Invert the pixels.
            int xmid = bm32.Width / 2;
            int ymid = bm32.Height / 2;
            for (int y = 0; y < ymid; y++)
            {
                for (int x = 0; x < xmid; x++)
                {
                    bm32.SetGreen(x, y, 0);
                    bm32.SetBlue(x, y, 0);
                    bm32.SetAlpha(x, y, 220);
                }
            }
            for (int y = ymid; y < bm32.Height; y++)
            {
                for (int x = 0; x < xmid; x++)
                {
                    bm32.SetRed(x, y, 0);
                    bm32.SetGreen(x, y, 0);
                    bm32.SetAlpha(x, y, 220);
                }
            }
            for (int y = 0; y < ymid; y++)
            {
                for (int x = xmid; x < bm32.Width; x++)
                {
                    bm32.SetRed(x, y, 0);
                    bm32.SetBlue(x, y, 0);
                    bm32.SetAlpha(x, y, 220);
                }
            }
            byte red, green, blue, alpha;
            for (int y = ymid; y < bm32.Height; y++)
            {
                for (int x = xmid; x < bm32.Width; x++)
                {
                    red = (byte)(255 - bm32.GetRed(x, y));
                    green = (byte)(255 - bm32.GetGreen(x, y));
                    blue = (byte)(255 - bm32.GetBlue(x, y));
                    alpha = 220;
                    bm32.SetPixel(x, y, red, green, blue, alpha);
                }
            }

            // Unlock the bitmap.
            bm32.UnlockBitmap();
            pictureBox1.Image = bitmap1;
            Cursor = Cursors.Default;

            /*
            // Make a new bitmap.
            Bitmap final_bm = new Bitmap(pictureBox0.Image);
            using (Graphics gr = Graphics.FromImage(final_bm))
            {
                // Draw an ellispe in the center.
                gr.Clear(Color.Black);
                gr.FillEllipse(Brushes.White,
                    new Rectangle((int)(bm.Width * 0.2), (int)(bm.Height * 0.2),
                        (int)(bm.Width * 0.6), (int)(bm.Height * 0.6)));

                // Copy the quartered bitmap onto this one.
                gr.DrawImage(bm, 0, 0);
            }

            // Display the result.
            pictureBox1.Image = final_bm;
            */
            sw.Stop();
            Cursor = Cursors.Default;

            richTextBox1.Text += "耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";

            richTextBox1.Text += "經過時間 : " + sw.Elapsed.TotalSeconds.ToString("0.000000") + " 秒\n";
        }

        private void bt_image_process_b3_Click(object sender, EventArgs e)
        {

        }
    }
}
