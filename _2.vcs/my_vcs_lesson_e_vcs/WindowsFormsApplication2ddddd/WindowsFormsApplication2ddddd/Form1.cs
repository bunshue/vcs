using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Runtime.InteropServices;
using Microsoft.Win32;

namespace WindowsFormsApplication2ddddd
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            HardDiskVal hddval = new HardDiskVal();
            richTextBox1.Text += "C : " + hddval.HDVal("C") + "\n";
            richTextBox1.Text += "D : " + hddval.HDVal("D") + "\n";

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //模擬MSN窗體抖動1

            int rand = 50;
            int recordx = this.Left;　//保存原來窗體的左上角的x坐標
            int recordy = this.Top;　//保存原來窗體的左上角的y坐標

            Random random = new Random();

            for (int i = 0; i < 100; i++)
            {
                int x = random.Next(rand);
                int y = random.Next(rand);
                if (x % 2 == 0)
                {
                    this.Left = this.Left + x;
                }
                else
                {
                    this.Left = this.Left - x;
                }
                if (y % 2 == 0)
                {
                    this.Top = this.Top + y;
                }
                else
                {
                    this.Top = this.Top - y;
                }

                this.Left = recordx;　//還原原始窗體的左上角的x坐標
                this.Top = recordy;　//還原原始窗體的左上角的y坐標
            }

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //模擬MSN窗體抖動2

            int rand = 10;
            int recordx = this.Left;
            int recordy = this.Top;
            Random random = new Random();
            for (int i = 0; i < 50; i++)
            {
                int x = random.Next(rand);
                int y = random.Next(rand);
                if (x % 2 == 0)
                {
                    this.Left = this.Left + x;
                }
                else
                {
                    this.Left = this.Left - x;
                }
                if (y % 2 == 0)
                {
                    this.Top = this.Top + y;
                }
                else
                {
                    this.Top = this.Top - y;
                }
                System.Threading.Thread.Sleep(1);
            }
            this.Left = recordx;
            this.Top = recordy;

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //使用byte[]數據，生成Bitmap

            int W = 256;
            int H = 256;
            byte[] imagedata = new byte[W * H];

            int i;
            int j;
            for (j = 0; j < H; j++)
            {
                for (i = 0; i < W; i++)
                {
                    imagedata[256 * i + j] = (byte)i;
                }
            }

            Bitmap bitmap1 = CreateBitmap(imagedata, W, H);
            pictureBox1.Image = bitmap1;


        }



        //C#中使用byte[]數據，生成Bitmap

        /// <summary>

        /// 使用byte[]數據，生成256色灰度　BMP 位圖

        /// </summary>

        /// <param name="originalImageData"></param>

        /// <param name="originalWidth"></param>

        /// <param name="originalHeight"></param>

        /// <returns></returns>

        public static Bitmap CreateBitmap(byte[] originalImageData, int originalWidth, int originalHeight)
        {

            //指定8位格式，即256色

            Bitmap resultBitmap = new Bitmap(originalWidth, originalHeight, System.Drawing.Imaging.PixelFormat.Format8bppIndexed);

            //將該位圖存入內存中

            MemoryStream curImageStream = new MemoryStream();

            resultBitmap.Save(curImageStream, System.Drawing.Imaging.ImageFormat.Bmp);

            curImageStream.Flush();

            //由於位圖數據需要DWORD對齊（4byte倍數），計算需要補位的個數

            int curPadNum = ((originalWidth * 8 + 31) / 32 * 4) - originalWidth;

            //最終生成的位圖數據大小

            int bitmapDataSize = ((originalWidth * 8 + 31) / 32 * 4) * originalHeight;

            //數據部分相對文件開始偏移，具體可以參考位圖文件格式

            int dataOffset = ReadData(curImageStream, 10, 4);

            //改變調色板，因為默認的調色板是32位彩色的，需要修改為256色的調色板

            int paletteStart = 54;

            int paletteEnd = dataOffset;

            int color = 0;

            for (int i = paletteStart; i < paletteEnd; i += 4)
            {

                byte[] tempColor = new byte[4];

                tempColor[0] = (byte)color;

                tempColor[1] = (byte)color;

                tempColor[2] = (byte)color;

                tempColor[3] = (byte)0;

                color++;

                curImageStream.Position = i;

                curImageStream.Write(tempColor, 0, 4);

            }

            //最終生成的位圖數據，以及大小，高度沒有變，寬度需要調整

            byte[] destImageData = new byte[bitmapDataSize];

            int destWidth = originalWidth + curPadNum;

            //生成最終的位圖數據，注意的是，位圖數據 從左到右，從下到上，所以需要顛倒

            for (int originalRowIndex = originalHeight - 1; originalRowIndex >= 0; originalRowIndex--)
            {

                int destRowIndex = originalHeight - originalRowIndex - 1;

                for (int dataIndex = 0; dataIndex < originalWidth; dataIndex++)
                {

                    //同時還要注意，新的位圖數據的寬度已經變化destWidth，否則會產生錯位

                    destImageData[destRowIndex * destWidth + dataIndex] = originalImageData[originalRowIndex * originalWidth + dataIndex];

                }

            }

            //將流的Position移到數據段　　

            curImageStream.Position = dataOffset;

            //將新位圖數據寫入內存中

            curImageStream.Write(destImageData, 0, bitmapDataSize);

            curImageStream.Flush();

            //將內存中的位圖寫入Bitmap對象

            resultBitmap = new Bitmap(curImageStream);

            return resultBitmap;

        }

        /// <summary>

        /// 從內存流中指定位置，讀取數據

        /// </summary>

        /// <param name="curStream"></param>

        /// <param name="startPosition"></param>

        /// <param name="length"></param>

        /// <returns></returns>

        public static int ReadData(MemoryStream curStream, int startPosition, int length)
        {

            int result = -1;

            byte[] tempData = new byte[length];

            curStream.Position = startPosition;

            curStream.Read(tempData, 0, length);

            result = BitConverter.ToInt32(tempData, 0);

            return result;

        }

        /// <summary>

        /// 向內存流中指定位置，寫入數據

        /// </summary>

        /// <param name="curStream"></param>

        /// <param name="startPosition"></param>

        /// <param name="length"></param>

        /// <param name="value"></param>

        public static void WriteData(MemoryStream curStream, int startPosition, int length, int value)
        {

            curStream.Position = startPosition;

            curStream.Write(BitConverter.GetBytes(value), 0, length);

        }
    }


    /// <summary>
    /// HardDiskVal 的摘要說明。
    /// 讀取指定盤符的硬盤序列號
    /// 功能：讀取指定盤符的硬盤序列號
    /// </summary>
    public class HardDiskVal
    {
        [DllImport("kernel32.dll")]
        private static extern int GetVolumeInformation(

        string lpRootPathName,

        string lpVolumeNameBuffer,

        int nVolumeNameSize,

        ref int lpVolumeSerialNumber,

        int lpMaximumComponentLength,

        int lpFileSystemFlags,

        string lpFileSystemNameBuffer,

        int nFileSystemNameSize

        );

        /// <summary>

        /// 獲得盤符為drvID的硬盤序列號，缺省為C

        /// </summary>

        /// <param name="drvID"></param>

        /// <returns></returns>

        public string HDVal(string drvID)
        {

            const int MAX_FILENAME_LEN = 256;

            int retVal = 0;

            int a = 0;

            int b = 0;

            string str1 = null;

            string str2 = null;

            int i = GetVolumeInformation(

            drvID + @":/",

            str1,

            MAX_FILENAME_LEN,

            ref retVal,

            a,

            b,

            str2,

            MAX_FILENAME_LEN

            );

            return retVal.ToString();

        }

        public string HDVal()
        {

            const int MAX_FILENAME_LEN = 256;

            int retVal = 0;

            int a = 0;

            int b = 0;

            string str1 = null;

            string str2 = null;

            int i = GetVolumeInformation(

            "c://",

            str1,

            MAX_FILENAME_LEN,

            ref retVal,

            a,

            b,

            str2,

            MAX_FILENAME_LEN

            );

            return retVal.ToString();

        }

    }


}
