using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Imaging;
using System.Text;
using System.Windows.Forms;

namespace HistogramEqualization
{
  public partial class Form1 : Form
  {
    OpenFileDialog ofd = new OpenFileDialog();
    HistogramBitmap imgSrc;

    public Form1()
    {
      InitializeComponent();
    }

    private void openToolStripMenuItem_Click_1(object sender, EventArgs e)
    {
      if (ofd.ShowDialog() == DialogResult.OK)
      {
        try 
        {
          Bitmap bmp = new Bitmap(ofd.FileName);
          imgSrc = new HistogramBitmap(bmp);
          pictureBox1.BackgroundImage = bmp;
          List<Histogram> histograms = imgSrc.GetHistograms();
          histogramPanel1.SetHistogram(histograms[0]);
          histogramPanel2.SetHistogram(histograms[0]);
        }
        catch (Exception exc)
        {
          MessageBox.Show(exc.Message);
        }    
      }
    }

    private void Form1_SizeChanged(object sender, EventArgs e)
    {
      panel1.Width = this.Width / 2;
    }

    private void linear0255ToolStripMenuItem_Click(object sender, EventArgs e)
    {
      pictureBox1.BackgroundImage = imgSrc.GetBitmap();
      histogramPanel2.SetHistogram(imgSrc.GetHistograms()[0]);
    }

    private void linearToolStripMenuItem_Click(object sender, EventArgs e)
    {
      HistogramBitmap newBmp = ContrastStretch.SimpleLinearStretch(imgSrc);
      pictureBox1.BackgroundImage = newBmp.GetBitmap(); ;
      histogramPanel2.SetHistogram(newBmp.GetHistograms()[0]);
    }

    private void linear2ToolStripMenuItem_Click(object sender, EventArgs e)
    {
      HistogramBitmap newBmp = ContrastStretch.TwoPercentLinear(imgSrc);
      pictureBox1.BackgroundImage = newBmp.GetBitmap(); ;
      histogramPanel2.SetHistogram(newBmp.GetHistograms()[0]);
    }

    private void equalizationToolStripMenuItem_Click(object sender, EventArgs e)
    {
      HistogramBitmap newBmp = ContrastStretch.HistogramEqualize(imgSrc);
      pictureBox1.BackgroundImage = newBmp.GetBitmap(); ;
      histogramPanel2.SetHistogram(newBmp.GetHistograms()[0]);
    }
  }
}