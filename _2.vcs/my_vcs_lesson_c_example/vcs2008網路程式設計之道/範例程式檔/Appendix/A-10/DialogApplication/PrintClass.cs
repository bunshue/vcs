using System;
using System.Drawing;
using System.Drawing.Printing;
using System.IO;

namespace DialogApplication
{
  public class PrintClass : System.Drawing.Printing.PrintDocument
  {
    private StreamReader streamReader;

    public PrintClass(StreamReader streamReader)
    {
      this.streamReader = streamReader;
    }

    protected override void OnPrintPage(PrintPageEventArgs ev)
    {
      Font font = null;
      float linesPerPage = 0;
      float yPos = 0;
      int count = 0;
      float leftMargin = ev.MarginBounds.Left;
      float topMargin = ev.MarginBounds.Top;
      String line = null;

      font = new Font("Arial", 10);

      linesPerPage = ev.MarginBounds.Height / font.GetHeight(ev.Graphics);

      while (count < linesPerPage && ((line = streamReader.ReadLine()) != null))
      {
        yPos = topMargin + count * font.GetHeight(ev.Graphics);
        ev.Graphics.DrawString(line, font, Brushes.Black, leftMargin, yPos, new StringFormat());
        count++;
      }

      if (line != null)
        ev.HasMorePages = true;
      else
        ev.HasMorePages = false;
    }
  }
}
