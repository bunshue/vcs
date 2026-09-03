using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices;  // for Marshal
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace dipHW_2
{
    public partial class Form1 : Form
    {
        private Bitmap img;
        byte[] srcData;
        int[] histoData;
        string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            LoadBitmap(filename);
        }

        // load and initialize from file
        private void LoadBitmap(string path)
        {
            // read from file
            img = (Bitmap)Image.FromFile(path);
            pictureBox1.Image = img;

            label1.Text = img.Width + "*" + img.Height;

            // read byte data
            BitmapData bitmapData = img.LockBits(new Rectangle(0, 0, img.Width, img.Height), ImageLockMode.ReadWrite, PixelFormat.Format8bppIndexed);
            srcData = new byte[img.Width * img.Height];
            IntPtr srcPtr = bitmapData.Scan0;
            Marshal.Copy(srcPtr, srcData, 0, img.Width * img.Height);
            // pay attention: order in byte array: height first
            img.UnlockBits(bitmapData);
        }

        // build a new bitmap with byte data
        private void BuildBitmap(int width, int height, byte[] newData)
        {
            // pay attention to the PixelFormat
            Bitmap newImg = new Bitmap(width, height, PixelFormat.Format8bppIndexed);
            // write in the byte data
            BitmapData bitmapData = newImg.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, PixelFormat.Format8bppIndexed);
            IntPtr srcPtr = bitmapData.Scan0;

            // width of stride, which sometimes can be different from width
            // for instance: 450*300 of the homeworkk
            int stride = bitmapData.Stride;
            int offset = stride - width;

            // two pointers for scan and data
            int posScan = 0, posData = 0;
            byte[] scanData = new byte[stride * height];
            for (int i = 0; i < height; ++i)
            {
                for (int j = 0; j < width; ++j)
                {
                    scanData[posScan++] = newData[posData++];
                }
                // jump over the offside at the end of each line
                posScan += offset;
            }

            // neglect the stride, which will cause error
            // Marshal.Copy(newData, 0, srcPtr, height * width);
            // accurate way
            Marshal.Copy(scanData, 0, srcPtr, height * stride);
            newImg.UnlockBits(bitmapData);

            // another method:
            // user setPixel to set color to every pixel
            // for (int i = 0; i < width; ++i)
            //     for (int j = 0; j < height; ++j)
            //         newImg.SetPixel(i, j, Color.FromArgb(newData[j * width + i], newData[j * width + i], newData[j * width + i]));

            // override the color palette to be grayscale
            ColorPalette tempPalette;
            using (Bitmap tempBmp = new Bitmap(1, 1, PixelFormat.Format8bppIndexed))
            {
                tempPalette = tempBmp.Palette;
            }
            for (int i = 0; i < 256; i++)
            {
                tempPalette.Entries[i] = Color.FromArgb(i, i, i);
            }

            newImg.Palette = tempPalette;

            // rewrite and show
            img = newImg;
            srcData = newData;
            label1.Text = img.Width + "*" + img.Height;
            pictureBox1.Image = img;
        }

        // calculate the histogram data
        private void Cal_Hist()
        {
            // width and height of the image
            int width = img.Width;
            int height = img.Height;
            histoData = new int[256];

            for (int i = 0; i < 256; ++i)
            {
                histoData[i] = 0;
            }

            for (int i = 0; i < height; ++i)
            {
                for (int j = 0; j < width; ++j)
                {
                    histoData[srcData[i * width + j]]++;
                }
            }
        }

        // histogram equalization
        private void Equalize_Hist(byte[] srcData)
        {
            // width and height and  pixels of the image
            int width = img.Width;
            int height = img.Height;
            int pixels = width * height;
            // array to hold the new data
            byte[] tempData = new byte[pixels];
            // calculate histogram data
            Cal_Hist();
            // calculate the histo-qualization function
            int[] histoChange = new int[256];
            int sum = 0;
            for (int i = 0; i < 256; ++i)
            {
                sum += histoData[i];
                histoChange[i] = 255 * sum / pixels;
            }
            // change the original image;
            for (int i = 0; i < height; ++i)
            {
                for (int j = 0; j < width; ++j)
                {
                    tempData[i * width + j] = (byte)histoChange[srcData[i * width + j]];
                }
            }
            BuildBitmap(width, height, tempData);
        }

        // histogram equation
        private void button2_Click(object sender, EventArgs e)
        {
            //顯示均衡化

            if (pictureBox1.Image == null)
            {
                return;
            }
            // histogram equalization
            Equalize_Hist(srcData);
        }

        // reload the image
        private void button4_Click(object sender, EventArgs e)
        {
            LoadBitmap(filename);
        }

        // show histogram
        private void button6_Click(object sender, EventArgs e)
        {
            //顯示直方圖
            if (pictureBox1.Image == null)
            {
                return;
            }

            // calculate the histogram data
            Cal_Hist();

            // show the histogram in a new form
            Form2 form2 = new Form2(histoData);
            form2.Show();
        }

    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個


