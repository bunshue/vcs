using System;
using System.Collections.Generic;
using System.Text;

namespace HistogramEqualization
{
  public class Histogram
  {
    public int botBin = 0;
    public int topBin = 0;
    public int[] freqs = new int[0];

    public Histogram(int botBin, int topBin)
    {
      this.botBin = botBin;
      this.topBin = topBin;
      freqs = new int[topBin - botBin + 1];
    }

    public int GetLowFrequencyBin()
    {
      int idx = botBin;
      while (freqs[idx] == 0 && idx < topBin)
        idx++;
      return idx;
    }

    public int GetHighFrequencyBin()
    {
      int idx = topBin;
      while (freqs[idx] == 0 && idx > botBin)
        idx--;
      return idx;
    }

    public int GetMaxFrequency()
    {
      int maxFreq = 0;
      for (int i = 0; i < freqs.Length; i++)
        maxFreq = Math.Max(maxFreq, freqs[i]);
      return maxFreq;
    }

    public int GetNumSamples()
    {
      int numSamples = 0;
      for (int i = 0; i < freqs.Length; i++)
        numSamples += freqs[i];
      return numSamples;
    }

    public bool AddSample(int idx)
    {
      if (idx >= freqs.Length)
        return false;

      freqs[idx]++;
      return true;
    }
  }
}
