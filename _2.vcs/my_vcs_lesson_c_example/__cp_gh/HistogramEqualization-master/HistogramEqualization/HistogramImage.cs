using System;
using System.Collections.Generic;
using System.Drawing.Imaging;
using System.Text;
using System.Drawing;

namespace HistogramEqualization
{
  public class HistogramBitmap
  {
    private Bitmap bmp;
    private List<Histogram> lHistograms = new List<Histogram>();
    private int numBands = 0;
    private int bpp = 0;

    public HistogramBitmap(Bitmap bmp)
    {
      this.bmp = new Bitmap(bmp);
      BuildHistograms();
    }

    public Bitmap GetBitmap()
    {
      return bmp;
    }

    public int GetNumBands()
    {
      return numBands;
    }

    public List<Histogram> GetHistograms()
    {
      return lHistograms;
    }

    private void BuildHistograms()
    {
      // Figure out data type
      //switch (bmp.PixelFormat) // TODO: Support more formats
      //{
      //  case PixelFormat.Format32bppArgb:
      //    numBands = 3;
      //    bpp = 8;
      //    break;
      //  default:
      //    throw new InvalidOperationException("Unsupported pixel format");
      //}
      numBands = 3;
      bpp = 8;

      // Build histograms
      lHistograms = new List<Histogram>();
      for (int i = 0; i < numBands; i++)
        lHistograms.Add(new Histogram(0, (int)(Math.Pow(2.0, bpp) - 1)));

      // Get frequencies
      BitmapData bmpData = bmp.LockBits(new Rectangle(0, 0, bmp.Width, bmp.Height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
      unsafe
      {
        byte* imgPtr = (byte*)(bmpData.Scan0);
        for (int i = 0; i < bmpData.Height; i++)
        {
          for (int j = 0; j < bmpData.Width; j++)
          {
            for (int k = 0; k < numBands; k++)
            {
              lHistograms[k].freqs[*imgPtr]++;
              imgPtr++;
            }
          }
          imgPtr += bmpData.Stride - bmpData.Width * numBands;
        }
      }
      bmp.UnlockBits(bmpData);
    }
  }
}
