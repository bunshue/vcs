using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;

/*
//使用C#的BitmapData編程實例

日期：2017/1/4 14:59:43      編輯：關於C#

最近要轉開發平台，正研究C#。C#好是好，不過處理圖片時一個像素一個像素的操作像素不是一般的慢。其實Delphi也一樣，但好在Delphi的Bitmap類提供了ScanLines，可以一行一行的讀圖，效率比較高。C#應該也有類似的東東。經過一番搜索，終於發現了BitmapData類。

先看個例子，這是對一張位圖的每個像素按FF取補，然後輸出到一個新圖（代碼有點啰嗦，不過應該可以說明問題了）。
*/

namespace vcs_BitmapData2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            //pictureBox1.Image = bitmap1;

            int h = bitmap1.Height;
            int w = bitmap1.Width;
            Bitmap bitmap2 = new Bitmap(w, h, PixelFormat.Format24bppRgb);
            BitmapData dataIn = bitmap1.LockBits(new Rectangle(0, 0, w, h), ImageLockMode.ReadOnly, PixelFormat.Format24bppRgb);
            BitmapData dataOut = bitmap2.LockBits(new Rectangle(0, 0, w, h), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            unsafe
            {
                byte* pIn = (byte*)(dataIn.Scan0.ToPointer());
                byte* pOut = (byte*)(dataOut.Scan0.ToPointer());
                for (int y = 0; y < dataIn.Height; y++)
                {
                    for (int x = 0; x < dataIn.Width; x++)
                    {
                        pOut[0] = (byte)(255 - pIn[0]);
                        pOut[1] = (byte)(255 - pIn[1]);
                        pOut[2] = (byte)(255 - pIn[2]);
                        pIn += 3;
                        pOut += 3;
                    }
                    pIn += dataIn.Stride - dataIn.Width * 3;
                    pOut += dataOut.Stride - dataOut.Width * 3;
                }
            }
            bitmap2.UnlockBits(dataOut);
            bitmap1.UnlockBits(dataIn);

            //就是掃描每一行，然後對當前像素點的三個分量做處理

            pictureBox1.Image = bitmap2;


            /*
            C#代碼中的Stride是個什麼東東？

            查找了不少資料，現在我是這麼理解的：

            假設有一張圖片寬度為6，因為是Format24bppRgb格式(每像素3字節。在以下的討論中，除非特別說明，否則Bitmap都被認為是24位RGB)的，顯然，每一行需要6*3=18個字節存儲。對於Bitmap就是如此。但對於BitmapData，雖然BitmapData.Width還是等於Bitmap.Width，但大概是出於顯示性能的考慮，每行的實際的字節數將變成大於等於它的那個離它最近的4的整倍數，此時的實際字節數就是Stride。就此例而言，18不是4的整倍數，而比18大的離18最近的4的倍數是20，所以這個BitmapData.Stride = 20。顯然，當寬度本身就是4的倍數時，BitmapData.Stride = Bitmap.Width * 3。
            */

            /*
            畫個圖可能更好理解。R、G、B 分別代表3個原色分量字節，BGR就表示一個像素。為了看起來方便我在每個像素之間插了個空格，實際上是沒有的。X表示補足4的倍數而自動插入的字節。為了符合人類的閱讀習慣我分行了，其實在計算機內存中應該看成連續的一大段。

            Scan0

            ---------Stride-----------------

            ---------Width-------------　 　 注：Width是圖片（BGR作為一個單位）寬度

            BGR BGR BGR BGR BGR BGR XX

            BGR BGR BGR BGR BGR BGR XX
            .
            .
            .

            現在應該很好理解了。首先用 BitmapData.Scan0找到第0個像素的第0個分量的地址。這個地址指向的是個byte類型，所以當時定義為byte* pIn。

            行掃描時，在當前指針位置（不妨看成當前像素的第0個顏色分量）連續取出三個值（3個原色分量。注意，0 1 2代表的次序是B G R。在取指針指向的值時，貌似p[n]和p += n再取p[0]是等價的），然後下移3個位置（pIn += 3，看成指到下一個像素的第0個顏色分量）。做過Bitmap.Width次操作後，就到達了Bitmap.Width * 3的位置，應該要跳過圖中標記為X的字節了（共有Stride - Width * 3個字節），代碼中就是 pIn += dataIn.Stride - dataIn.Width * 3;

            跳過以後指針就到達下行的第0個像素了。按照此算法,一共需要做Bitmap.Height次行掃描（代碼就是 for (int y = 0; y < dataIn.Height; y++)）。

            另外，因為使用了unsafe，所以編譯的時候需要設置“允許不安全的代碼”。
            */



        }

        private void button2_Click(object sender, EventArgs e)
        {
            //將byte數組轉換為8bit灰度圖像
            //將byte數組轉換為8bit灰度圖像
            byte[] bytes = new byte[10000];
            int k = 0;

            for (int i = 0; i < 100; i++)
            {
                for (int j = 0; j < 100; j++)
                {
                    bytes[k++] = (byte)(i + j);
                }
            }

            Bitmap bitmap1 = ToGrayBitmap(bytes, 100, 100);
            pictureBox1.Image = bitmap1;
            //bitmap1.Save(@"aaaaa.png", ImageFormat.Png);
        }

        //C#中將byte數組轉換為8bit灰度圖像

        /*
        byte數組存放的是圖像每個像素的灰度值，byte類型正好是從0~255，存放8bit灰度圖像的時候，一個 數組元素就是一個像素的灰度值。僅有這個數組還不足以恢復出原來的圖像，還必須事先知道圖像的長、 寬值；

        創建Bitmap類的時候必須指定PixelFormat為Format8bppIndexed，這樣才最符合圖像本身的特性；

        Bitmap類雖然提供了GetPixel()、SetPixel()這樣的方法，但我們絕對不能用這兩個方法來進行大規 模的像素讀寫，因為它們的性能實在很囧；

        托管代碼中，能不用unsafe就盡量不用。在.Net 2.0中已經提供了BitmapData類及其LockBits()、 UnLockBits()操作，能夠安全地進行內存讀寫；

        圖像的width和它存儲時的stride是不一樣的。位圖的掃描線寬度一定是4的倍數，因此圖像在內存中 的大小並不是它的顯示大小；

        Format8bppIndexed類型的PixelFormat是索引格式，其調色板並不是灰度的而是偽彩，因此需要我們 對其加以修改。
        */

        /// <summary>
        /// 將一個字節數組轉換為8bit灰度位圖
        /// </summary>
        /// <param name="rawValues">顯示字節數組</param>
        /// <param name="width">圖像寬度</param>
        /// <param name="height">圖像高度</param>
        /// <returns>位圖</returns>
        public static Bitmap ToGrayBitmap(byte[] rawValues, int width, int height)
        {
            //// 申請目標位圖的變量，並將其內存區域鎖定
            Bitmap bitmap1 = new Bitmap(width, height, PixelFormat.Format8bppIndexed);
            BitmapData bmpData = bitmap1.LockBits(new Rectangle(0, 0, width, height),
            ImageLockMode.WriteOnly, PixelFormat.Format8bppIndexed);

            //// 獲取圖像參數
            int stride = bmpData.Stride;　 // 掃描線的寬度
            int offset = stride - width;　 // 顯示寬度與掃描線寬度的間隙
            IntPtr iptr = bmpData.Scan0;　 // 獲取bmpData的內存起始位置
            int scanBytes = stride * height;　　 // 用stride寬度，表示這是 內存區域的大小

            //// 下面把原始的顯示大小字節數組轉換為內存中實際存放的字節數組
            int posScan = 0, posReal = 0;　　 // 分別設置兩個位置指針，指向 源數組和目標數組
            byte[] pixelValues = new byte[scanBytes];　 //為目標數組分配內 存

            for (int x = 0; x < height; x++)
            {
                //// 下面的循環節是模擬行掃描
                for (int y = 0; y < width; y++)
                {
                    pixelValues[posScan++] = rawValues[posReal++];
                }
                posScan += offset;　 //行掃描結束，要將目標位置指針移過 那段“間隙”
            }

            //// 用Marshal的Copy方法，將剛才得到的內存字節數組復制到 BitmapData中
            System.Runtime.InteropServices.Marshal.Copy(pixelValues, 0, iptr, scanBytes);
            bitmap1.UnlockBits(bmpData);　 // 解鎖內存區域

            //修改過調色板 ST
            //// 下面的代碼是為了修改生成位圖的索引表，從偽彩修改為灰度
            ColorPalette tempPalette;
            using (Bitmap tempBmp = new Bitmap(1, 1, PixelFormat.Format8bppIndexed))
            {
                tempPalette = tempBmp.Palette;
            }
            for (int i = 0; i < 256; i++)
            {
                tempPalette.Entries[i] = Color.FromArgb(i, i, i);
            }
            bitmap1.Palette = tempPalette;
            //修改過調色板 SP

            return bitmap1;
        }
    }
}
