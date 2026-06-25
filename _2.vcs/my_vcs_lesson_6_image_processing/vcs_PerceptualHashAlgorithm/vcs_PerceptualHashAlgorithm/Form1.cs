using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

/*
感知哈希算法——找出相似的圖片

感知哈希算法(Perceptual Hash Algorithm)
意思是為圖片生成一個指紋(字符串格式), 兩張圖片的指紋越相似, 說明兩張圖片就越相似.
但關鍵是如何根據圖片計算出"指紋"呢?
 
 下面用最簡單的步驟來說明一下原理:
第一步 縮小圖片尺寸
        將圖片縮小到8x8的尺寸, 總共64個像素. 這一步的作用是去除各種圖片尺寸和圖片比例的差異, 只保留結構、明暗等基本信息.

第二步 轉為灰度圖片
         將縮小后的圖片, 轉為64級灰度圖片.

第三步 計算灰度平均值
         計算圖片中所有像素的灰度平均值

第四步 比較像素的灰度
        將每個像素的灰度與平均值進行比較, 如果大于或等于平均值記為1, 小于平均值記為0.

第五步 計算哈希值
         將上一步的比較結果, 組合在一起, 就構成了一個64位的二進制整數, 這就是這張圖片的指紋.

第六步 對比圖片指紋
        得到圖片的指紋后, 就可以對比不同的圖片的指紋, 計算出64位中有多少位是不一樣的. 如果不相同的數據位數不超過5, 就說明兩張圖片很相似, 如果大于10, 說明它們是兩張不同的圖片.
*/

namespace vcs_PerceptualHashAlgorithm
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            richTextBox1.Size = new Size(300, 690);
            richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1273, 750);
            this.Text = "vcs_test_all_00_Usually";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            //感知哈希算法 獲取圖片的Hashcode
            string filename = string.Empty;
            string result = string.Empty;

            filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.bmp";

            SimilarPhoto photo = new SimilarPhoto(filename);
            result = photo.GetHash();
            richTextBox1.Text += result + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            //感知哈希算法 獲取圖片的Hashcode

            //谷歌百度以圖搜圖 感知哈希算法
            //感知哈希算法 獲取圖片的Hashcode

            string filename = string.Empty;
            string result = string.Empty;

            filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.bmp";

            result = ImageComparer.GetImageHashCode(filename);
            richTextBox1.Text += result + "\n";
        }
    }

    class SimilarPhoto
    {
        Image SourceImg;

        public SimilarPhoto(string filePath)
        {
            SourceImg = Image.FromFile(filePath);
        }

        public SimilarPhoto(Stream stream)
        {
            SourceImg = Image.FromStream(stream);
        }

        public String GetHash()
        {
            Image image = ReduceSize();
            Byte[] grayValues = ReduceColor(image);
            Byte average = CalcAverage(grayValues);
            String reslut = ComputeBits(grayValues, average);
            return reslut;
        }

        // Step 1 : Reduce size to 8*8
        private Image ReduceSize(int width = 8, int height = 8)
        {
            Image image = SourceImg.GetThumbnailImage(width, height, () => { return false; }, IntPtr.Zero);
            return image;
        }

        // Step 2 : Reduce Color
        private Byte[] ReduceColor(Image image)
        {
            Bitmap bitMap = new Bitmap(image);
            Byte[] grayValues = new Byte[image.Width * image.Height];

            for (int x = 0; x < image.Width; x++)
                for (int y = 0; y < image.Height; y++)
                {
                    Color color = bitMap.GetPixel(x, y);
                    byte grayValue = (byte)((color.R * 30 + color.G * 59 + color.B * 11) / 100);
                    grayValues[x * image.Width + y] = grayValue;
                }
            return grayValues;
        }

        // Step 3 : Average the colors
        private Byte CalcAverage(byte[] values)
        {
            int sum = 0;
            for (int i = 0; i < values.Length; i++)
                sum += (int)values[i];
            return Convert.ToByte(sum / values.Length);
        }

        // Step 4 : Compute the bits
        private String ComputeBits(byte[] values, byte averageValue)
        {
            char[] result = new char[values.Length];
            for (int i = 0; i < values.Length; i++)
            {
                if (values[i] < averageValue)
                    result[i] = '0';
                else
                    result[i] = '1';
            }
            return new String(result);
        }

        // Compare hash
        public static Int32 CalcSimilarDegree(string a, string b)
        {
            if (a.Length != b.Length)
                throw new ArgumentException();
            int count = 0;
            for (int i = 0; i < a.Length; i++)
            {
                if (a[i] != b[i])
                    count++;
            }
            return count;
        }
    }


    //------------------------------------------------------------  # 60個

    // 感知哈希算法 
    public class ImageComparer
    {
        // 獲取圖片的Hashcode
        public static string GetImageHashCode(string imageName)
        {
            int width = 8;
            int height = 8;

            //  第一步 
            //  將圖片縮小到8x8的尺寸，總共64個像素。這一步的作用是去除圖片的細節， 
            //  只保留結構、明暗等基本信息，摒棄不同尺寸、比例帶來的圖片差異。 
            Bitmap bmp = new Bitmap(Thumb(imageName));
            int[] pixels = new int[width * height];

            //  第二步 
            //  將縮小後的圖片，轉為64級灰度。也就是說，所有像素點總共只有64種顏色。 
            for (int i = 0; i < width; i++)
            {
                for (int j = 0; j < height; j++)
                {
                    Color color = bmp.GetPixel(i, j);
                    pixels[i * height + j] = RGBToGray(color.ToArgb());
                }
            }

            //  第三步 
            //  計算所有64個像素的灰度平均值。 
            int avgPixel = Average(pixels);

            //  第四步 
            //  將每個像素的灰度，與平均值進行比較。大於或等於平均值，記為1；小於平均值，記為0。 
            int[] comps = new int[width * height];
            for (int i = 0; i < comps.Length; i++)
            {
                if (pixels[i] >= avgPixel)
                {
                    comps[i] = 1;
                }
                else
                {
                    comps[i] = 0;
                }
            }

            //  第五步 
            //  將上一步的比較結果，組合在一起，就構成了一個64位的整數，這就是這張圖片的指紋。組合的次序並不重要，只要保證所有圖片都采用同樣次序就行了。 
            StringBuilder hashCode = new StringBuilder();
            for (int i = 0; i < comps.Length; i += 4)
            {
                int result = comps[i] * (int)Math.Pow(2, 3) + comps[i + 1] * (int)Math.Pow(2, 2) + comps[i + 2] * (int)Math.Pow(2, 1) + comps[i + 2];
                hashCode.Append(BinaryToHex(result));
            }
            bmp.Dispose();
            return hashCode.ToString();
        }

        // 計算"漢明距離"（Hamming distance）。 
        // 如果不相同的數據位不超過5，就說明兩張圖片很相似；如果大於10，就說明這是兩張不同的圖片。 
        public static int HammingDistance(String sourceHashCode, String hashCode)
        {
            int difference = 0;
            int len = sourceHashCode.Length;

            for (int i = 0; i < len; i++)
            {
                if (sourceHashCode[i] != hashCode[i])
                {
                    difference++;
                }
            }
            return difference;
        }

        // 縮放圖片
        private static Image Thumb(string imageName)
        {
            return Image.FromFile(imageName).GetThumbnailImage(8, 8, () => { return false; }, IntPtr.Zero);
        }

        // 轉為64級灰度 
        private static int RGBToGray(int pixels)
        {
            int _red = (pixels >> 16) & 0xFF;
            int _green = (pixels >> 8) & 0xFF;
            int _blue = (pixels) & 0xFF;
            return (int)(0.3 * _red + 0.59 * _green + 0.11 * _blue);
        }

        // 計算平均值 
        private static int Average(int[] pixels)
        {
            float m = 0;
            for (int i = 0; i < pixels.Length; ++i)
            {
                m += pixels[i];
            }
            m = m / pixels.Length;
            return (int)m;
        }

        private static char BinaryToHex(int binary)
        {
            char ch = ' ';
            switch (binary)
            {
                case 0:
                    ch = '0';
                    break;
                case 1:
                    ch = '1';
                    break;
                case 2:
                    ch = '2';
                    break;
                case 3:
                    ch = '3';
                    break;
                case 4:
                    ch = '4';
                    break;
                case 5:
                    ch = '5';
                    break;
                case 6:
                    ch = '6';
                    break;
                case 7:
                    ch = '7';
                    break;
                case 8:
                    ch = '8';
                    break;
                case 9:
                    ch = '9';
                    break;
                case 10:
                    ch = 'a';
                    break;
                case 11:
                    ch = 'b';
                    break;
                case 12:
                    ch = 'c';
                    break;
                case 13:
                    ch = 'd';
                    break;
                case 14:
                    ch = 'e';
                    break;
                case 15:
                    ch = 'f';
                    break;
                default:
                    ch = ' ';
                    break;
            }
            return ch;
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/


