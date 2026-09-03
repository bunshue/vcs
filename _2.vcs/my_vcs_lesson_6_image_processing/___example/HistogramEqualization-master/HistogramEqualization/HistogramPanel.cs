using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Text;
using System.Windows.Forms;
using HistogramEqualization;

namespace CustomControls
{
  public partial class HistogramPanel : UserControl
  {
    public enum Band
    {
      Red,
      Green,
      Blue
    }

    public const int BORDER = 20;
    public const int BORDERx2 = BORDER * 2;
    public const int INSET = 10;
    public const int INSETx2 = INSET * 2;
    public const int LARGE_TICK_HEIGHT = 8;
    public const int LARGE_TICK_HEIGHTx2 = LARGE_TICK_HEIGHT * 2;
    public const int SMALL_TICK_HEIGHT = 4;
    public const int TICK_START_X = BORDER + INSET;
    public const int TICK_START_Y = BORDER + LARGE_TICK_HEIGHT;
    

    private Pen pen = new Pen(Color.Red, 1);
    private Font font = new Font("Segoe UI", 10);
    private SolidBrush brushWhite = new SolidBrush(Color.White);

    private Point[] linePoints = new Point[0];
    private double tickWidth;

    private string title = "[title]";

    private Rectangle borderRect;
    private Rectangle drawArearRect;

    private Histogram histogram;

    public string Title
    {
      get { return title; }
      set { title = value; }
    }

    public HistogramPanel()
    {
      this.SetStyle(ControlStyles.AllPaintingInWmPaint | ControlStyles.UserPaint | ControlStyles.DoubleBuffer, true);
      InitializeComponent();
    }

    public void SetBand(Band band)
    {
      if (band == Band.Red)
        pen = new Pen(Color.Red, 1);
      else if (band == Band.Green)
        pen = new Pen(Color.Green, 1);
      else
        pen = new Pen(Color.Blue, 1);
      Invalidate();
    }

    public void SetHistogram(Histogram histogram)
    {
      this.histogram = histogram;

      double maxFreq = histogram.GetMaxFrequency();
      double scale = drawArearRect.Height / maxFreq;

      double pxlsPerBin = drawArearRect.Width / (histogram.freqs.Length * 1.0);
      linePoints = new Point[histogram.freqs.Length];
      for (int i = 0; i < linePoints.Length; i++)
      {
        int x = (int)(TICK_START_X + i * pxlsPerBin);
        int y = (int)(drawArearRect.Bottom - scale * histogram.freqs[i]);
        linePoints[i] = new Point(x, y);
      }

      Invalidate();
        
    }

    protected override void OnPaint(PaintEventArgs e)
    {
      Graphics g = e.Graphics;
      g.Clear(Color.Black);

      g.DrawString(title, Font, brushWhite, 8, 4);
      //g.DrawLines(pen, boxPoints);
      g.DrawRectangle(pen, borderRect);

      for (int i = 0; i <= 6; i += 3)
      {
        int x = (int)(TICK_START_X + i * tickWidth);
        g.DrawLine(pen, x, borderRect.Bottom, x, drawArearRect.Bottom);
        g.DrawLine(pen, x, borderRect.Top, x, drawArearRect.Top);
      }
      for (int i = 1; i <= 6; i++)
      {
        int x = (int)(TICK_START_X + i * tickWidth);
        g.DrawLine(pen, x, borderRect.Bottom, x, borderRect.Bottom - SMALL_TICK_HEIGHT);
        g.DrawLine(pen, x, borderRect.Top, x, borderRect.Top + SMALL_TICK_HEIGHT);
      }

      if (linePoints.Length > 1)
        g.DrawLines(pen, linePoints);
      
    }

    private void HistogramPanel_SizeChanged(object sender, EventArgs e)
    {
      borderRect = new Rectangle(BORDER, BORDER, Width - BORDERx2, Height - BORDERx2);
      drawArearRect = new Rectangle(TICK_START_X, TICK_START_Y, borderRect.Width - INSETx2, borderRect.Height - LARGE_TICK_HEIGHTx2);  
      tickWidth = (borderRect.Width - INSETx2) / 6;
      if (histogram != null)
        SetHistogram(histogram);
      Invalidate();
    }
  }
}