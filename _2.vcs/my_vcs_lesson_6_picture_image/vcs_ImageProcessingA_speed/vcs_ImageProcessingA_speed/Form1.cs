using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading.Tasks;   //for Parallel
using System.Drawing.Imaging;   //BitmapData

namespace vcs_ImageProcessingA_speed
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\doraemon.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.Image = Image.FromFile(filename);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            var bmp = new Bitmap(filename);
            pictureBox1.Image = bmp;
            var sw = new System.Diagnostics.Stopwatch();
            richTextBox1.Text += "各種影像處理速度比較 ST\n";
            Application.DoEvents();
            sw.Start();
            // GetPixel、SetPixel
            NegativeImage1(bmp);
            sw.Stop();
            pictureBox1.Refresh();
            richTextBox1.Text += "NegativeImage1: " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
            Application.DoEvents();
            sw.Reset();
            sw.Start();
            // Method in consideration of the arrangement
            NegativeImage2(bmp);
            sw.Stop();
            pictureBox1.Refresh();
            richTextBox1.Text += "NegativeImage2: " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
            Application.DoEvents();
            sw.Reset();
            sw.Start();
            // MershalのReadByte、WriteByte
            NegativeImage3(bmp);
            sw.Stop();
            pictureBox1.Refresh();
            richTextBox1.Text += "NegativeImage3: " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
            Application.DoEvents();
            sw.Reset();
            sw.Start();
            // usafe pointer
            NegativeImage4(bmp);
            sw.Stop();
            pictureBox1.Refresh();
            richTextBox1.Text += "NegativeImage4: " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
            Application.DoEvents();
            sw.Reset();
            sw.Start();
            // parallel processing of usafe pointer
            NegativeImage5(bmp);
            sw.Stop();
            pictureBox1.Refresh();
            richTextBox1.Text += "NegativeImage5: " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
            Application.DoEvents();
            sw.Reset();
            sw.Start();
            // parallel processing of usafe pointer
            NegativeImage6(bmp);
            sw.Stop();
            pictureBox1.Refresh();
            richTextBox1.Text += "NegativeImage6: " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";




            richTextBox1.Text += "各種影像處理速度比較 SP\n\n";
        }





        /// <summary>
        /// Set up the brightness value with GetPixel、SetPixel
        /// </summary>
        /// <param name="bmp"></param>
        private void NegativeImage1(Bitmap bmp)
        {
            var W = bmp.Width;
            var H = bmp.Height;
            Color col;
            int r, g, b;
            for (int y = 0; y < H; y++)
            {
                for (int x = 0; x < W; x++)
                {
                    // Obtaining brightness value
                    col = bmp.GetPixel(x, y);
                    r = col.R;
                    g = col.G;
                    b = col.B;
                    // color reversal
                    col = Color.FromArgb(255 - r, 255 - g, 255 - b);
                    // set up brightness value
                    bmp.SetPixel(x, y, col);
                }
            }
        }

        /// <summary>
        /// Obtain the image data at Lock Bits, Unlock Bits with pointer and process the data in sequence 
        /// </summary>
        /// <param name="bmp"></param>
        private void NegativeImage2(Bitmap bmp)
        {
            var W = bmp.Width;
            var H = bmp.Height;
            // Lock Bitmap
            var bmpData = bmp.LockBits(
            new Rectangle(0, 0, W, H),
            System.Drawing.Imaging.ImageLockMode.ReadWrite,
            bmp.PixelFormat
            );
            // Obtain Bytes of memory width
            var stride = Math.Abs(bmpData.Stride);
            // Arrange image data for saving
            var data = new byte[stride * bmpData.Height];
            // Copy Bitmap data
            System.Runtime.InteropServices.Marshal.Copy(
            bmpData.Scan0,
            data,
            0,
            stride * bmpData.Height
            );
            byte r, g, b;
            int lineIndex = 0;
            for (int y = 0; y < H; y++)
            {
                for (int x = 0; x < W * 3; x += 3)
                {
                    // Obtain the brightness value
                    r = data[lineIndex + x + 2];
                    g = data[lineIndex + x + 1];
                    b = data[lineIndex + x]; ;
                    // Set up the brightness value
                    data[lineIndex + x + 2] = (byte)(255 - r);
                    data[lineIndex + x + 1] = (byte)(255 - g);
                    data[lineIndex + x] = (byte)(255 - b);
                }
                lineIndex += stride;
            }
            // Copy the arrangement as Bitmap data
            System.Runtime.InteropServices.Marshal.Copy(
            data,
            0,
            bmpData.Scan0,
            stride * bmpData.Height
            );
            // Unlock
            bmp.UnlockBits(bmpData);
        }

        /// <summary>
        /// How to obtain brightness value with ReadByte, WriteByte in Marshal class
        /// </summary>
        /// <param name="bmp"></param>
        private void NegativeImage3(Bitmap bmp)
        {
            var W = bmp.Width;
            var H = bmp.Height;
            // Lock the Bitmap
            var bmpData = bmp.LockBits(
            new Rectangle(0, 0, W, H),
            System.Drawing.Imaging.ImageLockMode.ReadWrite,
            bmp.PixelFormat
            );
            // Obtain Bytes of memory width
            var stride = Math.Abs(bmpData.Stride);
            byte r, g, b;
            int lineIndex = 0;
            var ptr = bmpData.Scan0;
            for (int y = 0; y < H; y++)
            {
                for (int x = 0; x < W * 3; x += 3)
                {
                    // Obtain brightness value
                    r = System.Runtime.InteropServices.Marshal.ReadByte(ptr, lineIndex + x + 2);
                    g = System.Runtime.InteropServices.Marshal.ReadByte(ptr, lineIndex + x + 1);
                    b = System.Runtime.InteropServices.Marshal.ReadByte(ptr, lineIndex + x);
                    // Set up brightness value
                    System.Runtime.InteropServices.Marshal.WriteByte(ptr, lineIndex + x + 2, (byte)(255 - r));
                    System.Runtime.InteropServices.Marshal.WriteByte(ptr, lineIndex + x + 1, (byte)(255 - g));
                    System.Runtime.InteropServices.Marshal.WriteByte(ptr, lineIndex + x, (byte)(255 - b));
                }
                lineIndex += stride;
            }
            // Unlock
            bmp.UnlockBits(bmpData);
        }

        /// <summary>
        /// How to obtain brightness value by using unsafe pointer
        /// </summary>
        /// <param name="bmp"></param>
        private void NegativeImage4(Bitmap bmp)
        {
            var W = bmp.Width;
            var H = bmp.Height;
            // Bitmap Lock
            var bmpData = bmp.LockBits(
            new Rectangle(0, 0, W, H),
            System.Drawing.Imaging.ImageLockMode.ReadWrite,
            bmp.PixelFormat
            );
            // Obtain Bytes of memory width
            var stride = Math.Abs(bmpData.Stride);
            unsafe
            {
                // Arrange image data for saving
                var ptr = (byte*)bmpData.Scan0;
                byte r, g, b;
                byte* pLine = ptr;
                for (int y = 0; y < H; y++)
                {
                    // The first point of the line
                    ptr = pLine;
                    for (int x = 0; x < W; x++)
                    {
                        // Obtain brightness value
                        r = ptr[2];
                        g = ptr[1];
                        b = ptr[0];
                        // Set up brightness value
                        ptr[2] = (byte)(255 - r);
                        ptr[1] = (byte)(255 - g);
                        ptr[0] = (byte)(255 - b);
                        // Move to the next pixel 
                        ptr += 3;
                    }
                    // Move to the next line 
                    pLine += stride;
                }
            }
            // Unlock
            bmp.UnlockBits(bmpData);
        }

        /// <summary>
        /// Parallel processing of the brightness value acquiring setup using usafe pointer
        /// </summary>
        /// <param name="bmp"></param>
        private void NegativeImage5(Bitmap bmp)
        {
            var W = bmp.Width;
            var H = bmp.Height;
            // Bitmap Lock
            var bmpData = bmp.LockBits(
            new Rectangle(0, 0, W, H),
            System.Drawing.Imaging.ImageLockMode.ReadWrite,
            bmp.PixelFormat
            );
            // Obtain Bytes of memory width
            var stride = Math.Abs(bmpData.Stride);
            unsafe
            {
                // Arrange image data for saving
                var ptr = (byte*)bmpData.Scan0;
                Parallel.For(0, H, y =>
                {
                    // The first pointer of the line
                    byte* pLine = ptr + y * stride;
                    for (int x = 0; x < W; x++)
                    {
                        // Obtain brightness value
                        byte r = pLine[2];
                        byte g = pLine[1];
                        byte b = pLine[0];
                        // Set up brightness value
                        pLine[2] = (byte)(255 - r);
                        pLine[1] = (byte)(255 - g);
                        pLine[0] = (byte)(255 - b);
                        // Move to the next pixel
                        pLine += 3;
                    }
                }
                );
            }
            // Unlock
            bmp.UnlockBits(bmpData);
        }

        /// <summary>
        /// 使用BitmapData處理
        /// </summary>
        /// <param name="bmp"></param>
        private void NegativeImage6(Bitmap bmp)
        {
            var W = bmp.Width;
            var H = bmp.Height;

            //richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
            BitmapData bData = bmp.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);

            unsafe
            {
                byte* p = (byte*)bData.Scan0.ToPointer();
                for (int y = 0; y < H; y++)
                {
                    for (int x = 0; x < W; x++)
                    {
                        //檢查圖片是否全白或全黑
                        if ((p[0] != 255 && p[0] != 0) || (p[1] != 255 && p[1] != 0) || (p[2] != 255 && p[2] != 0))
                        {
                            //NotNULL = true;
                            //break;
                        }

                        /*
                        //修改圖片的數值
                        p[0] -= 50;
                        p[1] -= 50;
                        p[2] -= 50;
                        */

                        //反相
                        p[0] = (byte)(255 - p[0]);
                        p[1] = (byte)(255 - p[1]);
                        p[2] = (byte)(255 - p[2]);

                        p += 3;
                    }
                    //if (NotNULL == true)
                    //break;
                }
                bmp.UnlockBits(bData);
            }
        }
    }
}

