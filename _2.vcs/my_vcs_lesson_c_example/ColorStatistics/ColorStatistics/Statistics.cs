using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;
using System.Drawing.Imaging;

using System.Collections;
using System.Runtime.InteropServices;
using System.Windows.Forms;
using System.Diagnostics;

/*
     統計顏色這一塊，其實我一直在尋找一種即不用占很大內存，速度又快的算法，但是一直沒有想到好辦法。 上面的代碼中是分配了64MB的內存來索引計數的，雖然對於很小的圖像也需要這麼大的內存占用量，但是我經過對比發現，比用Dictionary之類的基於字典的統計方法還是要快很多的。

     關於排序，我一直認為自己能寫出比系統更快的算法，但是最終我還是選擇了如上代碼中的簡便方式。在對Amount進行排序的同時，Color的值也跟著隨動了。

     在這種占用比較大內存的代碼中，我認為應該立即調用GC.Collect()釋放掉內存。

     關於Delta的取值，似乎不太好確定，這個只能說試驗確定吧，一般取16-32之間比較合理。

     兩個參考鏈接處也有一些比較好的算法的，不過裡面的代碼是PHP的，改寫成C#的應該說還是有一定的難度的，有興趣的朋友可以自己參考著學習下吧。

     從個人的理解來看，我覺得這種顏色主成分分析 還可以利用 類似於彩色轉索引時 找最佳索引表時用的八叉樹算法；也可以用FCM或者KMEANS之類的聚類算法來實現。待時間充足時我回去實際驗證下。
*/

namespace ColorStatistics
{
    static unsafe class Statistics
    {
        [StructLayout(LayoutKind.Sequential)]
        public struct MajorColor : IComparable<MajorColor>
        {
            internal int Color;
            internal int Amount;
            public MajorColor(int Color, int Amount)
            {
                this.Color = Color;
                this.Amount = Amount;
            }
            public int CompareTo(MajorColor obj)
            {
                return this.Amount.CompareTo(obj.Amount);
            }
        }

        // http://www.coolphptools.com/color_extract
        // http://www.wookmark.com/image/268753/30-inspiring-examples-of-levitation-photography-inspirationfeed-com
        public static List<MajorColor> PrincipalColorAnalysis(Bitmap Bmp, int PCAAmount, int Delta = 24)
        {
            List<MajorColor> MC = new List<MajorColor>();

            int X, Y, Width, Height, Stride, Index, TotalColorAmount = 0;
            int HalfDelta;
            byte* Pointer, Scan0;
            BitmapData BmpData = Bmp.LockBits(new Rectangle(0, 0, Bmp.Width, Bmp.Height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            Height = Bmp.Height; Width = Bmp.Width; Stride = BmpData.Stride; Scan0 = (byte*)BmpData.Scan0;

            int[] Table = new int[256 * 256 * 256];
            int[] NonZero = new int[Width * Height];
            int[] Map = new int[256];

            if (Delta > 2)
                HalfDelta = Delta / 2 - 1;
            else
                HalfDelta = 0;

            for (Y = 0; Y < 256; Y++)
            {
                Map[Y] = ((Y + HalfDelta) / Delta) * Delta;
                if (Map[Y] > 255) Map[Y] = 255;
            }
            for (Y = 0; Y < Height; Y++)
            {
                Pointer = Scan0 + Stride * Y;
                for (X = 0; X < Width; X++)
                {
                    Index = (Map[*Pointer] << 16) + (Map[*(Pointer + 1)] << 8) + Map[*(Pointer + 2)];
                    if (Table[Index] == 0)                  //      還沒有出現過該顏色
                    {
                        NonZero[TotalColorAmount] = Index;  //      記錄下有顏色的位置，同時也記錄下了該顏色
                        TotalColorAmount++;                 //      顏色總數+1
                    }
                    Table[Index]++;                         //      對應的顏色數加1
                    Pointer += 3;                          //      移動到下一個像素
                }
            }
            MajorColor[] Result = new MajorColor[TotalColorAmount];
            for (Y = 0; Y < TotalColorAmount; Y++)
            {
                Result[Y].Amount = Table[NonZero[Y]];
                Result[Y].Color = NonZero[Y];
            }
            Array.Sort(Result);                             // 系統自帶的這個排序算法比一般自己寫的都要快
            Array.Reverse(Result);

            for (Y = 0; Y < PCAAmount; Y++)
                MC.Add(new MajorColor(Result[Y].Color, Result[Y].Amount));
            Bmp.UnlockBits(BmpData);
            GC.Collect();                                   // 立即釋放掉分配的64MB的內存
            return MC;
        }
    }
}

