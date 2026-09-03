using System;
using System.Drawing;
using System.Collections.Generic;
using System.Text;
using System.Drawing.Imaging;

namespace HistogramEqualization
{
  public class ContrastStretch
  {
    public static HistogramBitmap HistogramEqualize(HistogramBitmap bmp)
    {
      Bitmap newBmp = new Bitmap(bmp.GetBitmap());

      // Cumulative distribution function
      int[] cdfsR = new int[256];
      int[] cdfsG = new int[256];
      int[] cdfsB = new int[256];

      // Calculate cumulative distribution function
      int cdfR = 0;
      int cdfG = 0;
      int cdfB = 0;
      for (int i = 0; i < 256; i++)
      {
        if (bmp.GetHistograms()[0].freqs[i] != 0)
        {
          cdfR += bmp.GetHistograms()[0].freqs[i];
          cdfsR[i] = cdfR;
        }
        if (bmp.GetHistograms()[1].freqs[i] != 0)
        {
          cdfG += bmp.GetHistograms()[1].freqs[i];
          cdfsG[i] = cdfG;
        }
        if (bmp.GetHistograms()[2].freqs[i] != 0)
        {
          cdfB += bmp.GetHistograms()[2].freqs[i];
          cdfsB[i] = cdfB;
        }
      }

      // Find min cdfs
      int cdfRMin = int.MaxValue;
      int cdfGMin = int.MaxValue;
      int cdfBMin = int.MaxValue;
      for (int i = 0; i < 256; i++)
      {
        cdfRMin = Math.Min(cdfRMin, cdfsR[i]);
        cdfGMin = Math.Min(cdfGMin, cdfsG[i]);
        cdfBMin = Math.Min(cdfBMin, cdfsB[i]);
      }
      double rSize = bmp.GetBitmap().Height * bmp.GetBitmap().Width - cdfRMin;
      double gSize = bmp.GetBitmap().Height * bmp.GetBitmap().Width - cdfGMin;
      double bSize = bmp.GetBitmap().Height * bmp.GetBitmap().Width - cdfBMin;

      // Equalize pixel values
      BitmapData bmpData = newBmp.LockBits(new Rectangle(0, 0, newBmp.Width, newBmp.Height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
      unsafe
      {
        byte* imgPtr = (byte*)(bmpData.Scan0);
        for (int i = 0; i < bmpData.Height; i++)
        {
          for (int j = 0; j < bmpData.Width; j++)
          {
            double valR = Bound(0, 255, Math.Round((cdfsR[imgPtr[0]] - cdfRMin) / rSize * 255.0));
            double valG = Bound(0, 255, Math.Round((cdfsG[imgPtr[1]] - cdfGMin) / gSize * 255.0));
            double valB = Bound(0, 255, Math.Round((cdfsB[imgPtr[2]] - cdfRMin) / bSize * 255.0));
            imgPtr[0] = Convert.ToByte(valR);
            imgPtr[1] = Convert.ToByte(valG);
            imgPtr[2] = Convert.ToByte(valB);
            imgPtr += 3;
          }
          imgPtr += bmpData.Stride - bmpData.Width * 3;
        }
      }

      newBmp.UnlockBits(bmpData);
      return new HistogramBitmap(newBmp);
    }

    public static HistogramBitmap SimpleLinearStretch(HistogramBitmap img)
    {
      Bitmap newBmp = new Bitmap(img.GetBitmap());

      // Find scale
      List<Histogram> lHistograms = img.GetHistograms();
      List<int> lMinVals = new List<int>();
      List<double> lRanges = new List<double>();
      for (int i = 0; i < img.GetNumBands(); i++)
      {
        int minVal = lHistograms[i].GetLowFrequencyBin();
        lRanges.Add(lHistograms[i].GetHighFrequencyBin() - minVal);
        lMinVals.Add(minVal);
      }

      // Stretch pixel values
      BitmapData bmpData = newBmp.LockBits(new Rectangle(0, 0, newBmp.Width, newBmp.Height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
      unsafe
      {
        byte* imgPtr = (byte*)(bmpData.Scan0);
        for (int i = 0; i < bmpData.Height; i++)
        {
          for (int j = 0; j < bmpData.Width; j++)
          {
            for (int k = 0; k < img.GetNumBands(); k++)
            {
              imgPtr[0] = Convert.ToByte(Math.Round((imgPtr[0] - lMinVals[k]) / lRanges[k] * 255.0));
              imgPtr++;
            }
          }
          imgPtr += bmpData.Stride - bmpData.Width * img.GetNumBands();
        }
      }
      newBmp.UnlockBits(bmpData);

      HistogramBitmap newImg = new HistogramBitmap(newBmp);
      return newImg;
    }

    public static HistogramBitmap TwoPercentLinear(HistogramBitmap bmp)
    {
      List<Histogram> histograms = bmp.GetHistograms();
      int totalSamples = 0;
      for (int i = 0; i < 256; i++)
      {
        totalSamples += histograms[0].freqs[i];
      }
      int twoPercent = (int)(totalSamples * 0.02);
      int botVal = histograms[0].GetLowFrequencyBin();
      int topVal = histograms[0].GetHighFrequencyBin();
      int cnt = 0;
      while (cnt < twoPercent)
      {
        cnt += (int)histograms[0].freqs[botVal];
        botVal++;
      }
      botVal--;
      cnt = 0;
      while (cnt < twoPercent)
      {
        cnt += histograms[0].freqs[topVal];
        topVal--;
      }
      double range = topVal - botVal;

      Bitmap newBmp = new Bitmap(bmp.GetBitmap());
      BitmapData bmpData = newBmp.LockBits(new Rectangle(0, 0, newBmp.Width, newBmp.Height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
      unsafe
      {
        byte* imgPtr = (byte*)(bmpData.Scan0);
        for (int i = 0; i < bmpData.Height; i++)
        {
          for (int j = 0; j < bmpData.Width; j++)
          {
            imgPtr[0] = Convert.ToByte(Bound(0, 255, Math.Round((imgPtr[0] - botVal) / range * 255.0)));
            imgPtr[1] = Convert.ToByte(Bound(0, 255,Math.Round((imgPtr[1] - botVal) / range * 255.0)));
            imgPtr[2] = Convert.ToByte(Bound(0, 255,Math.Round((imgPtr[2] - botVal) / range * 255.0)));
            imgPtr += 3;
          }
          imgPtr += bmpData.Stride - bmpData.Width * 3;
        }
      }

      newBmp.UnlockBits(bmpData);
      return new HistogramBitmap(newBmp);
    }

    static double Bound(double lowerBound, double upperBound, double val)
    {
      if (val < lowerBound)
        return lowerBound;
      if (val > upperBound)
        return upperBound;
      return val;
    }

    static int FindLowIdx(int[] vals)
    {
      int idx = 0;
      while (vals[idx] == 0 && idx < 255)
        idx++;
      return idx;
    }

    static int FindHighIdx(int[] vals)
    {
      int idx = 255;
      while (vals[idx] == 0 && idx > 0)
        idx--;
      return idx;
    }
  }
}
