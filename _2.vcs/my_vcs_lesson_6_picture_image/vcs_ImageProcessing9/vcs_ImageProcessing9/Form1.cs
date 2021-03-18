using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;
using System.Runtime.InteropServices;   //for Marshal

namespace vcs_ImageProcessing9
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\picture1.jpg";
        private Bitmap bitmap1;
        byte[] srcData;
        //int[] histoData;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            LoadBitmap(filename);
        }

        // load and initialize from file
        private void LoadBitmap(string filename)
        {
            // read from file
            bitmap1 = (Bitmap)Image.FromFile(filename);
            pictureBox1.Image = bitmap1;

            int W = bitmap1.Width;
            int H = bitmap1.Height;

            // read byte data
            BitmapData bmpData = bitmap1.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, PixelFormat.Format8bppIndexed);
            srcData = new byte[W * H];
            IntPtr srcPtr = bmpData.Scan0;
            Marshal.Copy(srcPtr, srcData, 0, W * H);
            // pay attention: order in byte array: height first
            bitmap1.UnlockBits(bmpData);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int len = srcData.Length;
            int W = bitmap1.Width;
            int H = bitmap1.Height;

            richTextBox1.Text += "len = " + len.ToString() + "\n";
            richTextBox1.Text += "W = " + W.ToString() + "\n";
            richTextBox1.Text += "H = " + H.ToString() + "\n";
            int i;
            int j;
            for (j = 0; j < H; j++)
            {
                for (i = 0; i < W; i++)
                {
                    //richTextBox1.Text += srcData[j * H + i].ToString("X2") + " ";
                    //richTextBox1.Text += srcData[j * H + i].ToString() + " ";

                    //srcData[j * H + i] = (byte)(255 - srcData[j * H + i]);

                }
                //richTextBox1.Text += "\n";
            }

            //準備修改srcData值  並把 srcData恢復成圖片


            for (i = 0; i < 305 * 10; i++)
            {
                srcData[i] = 0;

            }
            
            richTextBox1.Text += "\n";
            richTextBox1.Text += "\n";
            richTextBox1.Text += "\n";


            for (i = 0; i < 150; i++)
            {
                //richTextBox1.Text += srcData[i].ToString() + " ";

            }
            richTextBox1.Text += "\n";


        }


    }
}
