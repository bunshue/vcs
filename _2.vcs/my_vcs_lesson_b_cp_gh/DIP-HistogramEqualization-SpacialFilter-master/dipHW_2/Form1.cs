using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace dipHW_2
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\picture1.jpg";
        private Bitmap img;
        byte[] srcData;
        int[] histoData;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            LoadBitmap(filename);
        }

        // load and initialize from file
        private void LoadBitmap(string path) {
            // read from file
            img = (Bitmap)Image.FromFile(path);
            pictureBox1.Image = img;
            label1.Text = img.Width + "*" + img.Height;

            // read byte data
            BitmapData bitmapData = img.LockBits(new Rectangle(0, 0, img.Width, img.Height),
                ImageLockMode.ReadWrite, PixelFormat.Format8bppIndexed);
            srcData = new byte[img.Width * img.Height];
            IntPtr srcPtr = bitmapData.Scan0;
            Marshal.Copy(srcPtr, srcData, 0, img.Width * img.Height);
            // pay attention: order in byte array: height first
            img.UnlockBits(bitmapData);
        }

        // build a new bitmap with byte data
        private void BuildBitmap(int width, int height, byte[] newData) {
            // pay attention to the PixelFormat
            Bitmap newImg = new Bitmap(width, height, PixelFormat.Format8bppIndexed);
            // write in the byte data
            BitmapData bitmapData = newImg.LockBits(new Rectangle(0, 0, width, height),
                ImageLockMode.ReadWrite, PixelFormat.Format8bppIndexed);
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
        private void Cal_Hist() {
            // width and height of the image
            int width = img.Width;
            int height = img.Height;
            histoData = new int[256];
            for (int i = 0; i < 256; ++i)
                histoData[i] = 0;
            for (int i = 0; i < height; ++i) {
                for (int j = 0; j < width; ++j) {
                    histoData[srcData[i * width + j]]++;
                } 
            }
        }

        // histogram equalization
        private void Equalize_Hist(byte[] srcData) {
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
            for (int i = 0; i < 256; ++i) {
                sum += histoData[i];
                histoChange[i] = 255 * sum / pixels;
            }
            // change the original image;
            for (int i = 0; i < height; ++i)
                for (int j = 0; j < width; ++j) {
                    tempData[i * width + j] = (byte)histoChange[srcData[i * width + j]];
                }
            BuildBitmap(width, height, tempData);
        }

        // filter
        private void Filter2d(byte[] srcData, int level, double[] filter) {
            // width and height of the image
            int width = img.Width;
            int height = img.Height;
            // array to hold the new data
            byte[] tempData = new byte[width * height];
            // generize the offset from current pixel
            int[] offset = new int[level * level];
            int temNum = 0;
            for (int i = - level / 2; i <= level/2; ++i) {
                for (int j = -level / 2; j <= level / 2; ++j) {
                    offset[temNum++] = i * width + j;
                }
            }
            // generize new imgae data
            for (int i = 0; i < height; ++i)
                for (int j = 0; j < width; ++j) {
                    int temp = 0;
                    for (int k = 0; k < level * level; ++k) {
                        // zero padding
                        int pos = i * width + j + offset[k];
                        double data;
                        if (pos >= 0 && pos < height * width)
                        {
                            data = srcData[pos];
                        }
                        else {
                            data = 0;
                        }
                        // applying filter
                        temp += (int)(data * filter[k]);
                    }
                    // formatting into byte
                    if (temp < 0) temp = 0;
                    if (temp > 255) temp = 255;
                    tempData[i * width + j] = (byte)temp;
                }
            // write the new image
            BuildBitmap(width, height, tempData);
        }

        // histogram equation
        private void button2_Click(object sender, EventArgs e)
        {
            if (pictureBox1.Image == null) return;
            // histogram equalization
            Equalize_Hist(srcData);
        }

        // reload the image
        private void button4_Click(object sender, EventArgs e)
        {
            if (filename == "")
                return;
            LoadBitmap(filename);
        }

        // show histogram
        private void button6_Click(object sender, EventArgs e)
        {
            if (pictureBox1.Image == null) return;
            // calculate the histogram data
            Cal_Hist();
            // show the histogram in a new form
            Form2 form2 = new Form2(histoData);
            form2.Show();
        }

        // average filter
        private void button5_Click(object sender, EventArgs e)
        {
            if (pictureBox1.Image == null) return;
            int level = Int32.Parse(textBox3.Text);
            // calculate the average 
            double[] filter = new double[level * level];
            for (int i = 0; i < level * level; ++i)
            {
                filter[i] = 255.0 / (double)(level * level);
            }
            // filter it
            Filter2d(srcData, level, filter);
        }

        // customized 3*3 filter
        private void button7_Click(object sender, EventArgs e)
        {
            if (pictureBox1.Image == null) return;
            double[] filter = new double[9];
            // get all the customed filter values
            TextBox[] filterBox = new TextBox[9] {
                filter1, filter2, filter3, filter4, filter5, filter6, filter7, filter8, filter9};
            // initialize the filter
            for (int i = 0; i < 9; ++i) {
                filter[i] = Double.Parse(filterBox[i].Text);
            }
            // filter it
            Filter2d(srcData, 3, filter);
        }

    }
}
