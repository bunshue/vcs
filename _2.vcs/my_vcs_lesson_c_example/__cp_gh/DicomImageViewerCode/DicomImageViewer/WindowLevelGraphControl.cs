using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Windows.Forms;

// Program to view simple DICOM images.
// Written by Amarnath S, Mahesh Reddy S, Bangalore, India, April 2009.
// Updated by Amarnath, July 2010 to handle RGB images coming from Ultrasound modality.
// Updated Aug 2012, to fix some issues

namespace DicomImageViewer
{
    public partial class WindowLevelGraphControl : UserControl
    {
        int marginLeft;
        int marginRight;
        int marginTop;
        int marginBottom;
        int graphWidth;
        int graphHeight;

        int winWidth;
        int winCentre;
        int winMin;
        int winMax;

        ImageBitsPerPixel iBpp;
        bool signedImage;

        Color c1 = Color.Purple;
        Color c2 = Color.DarkBlue;

        public WindowLevelGraphControl()
        {
            InitializeComponent();
            DoubleBuffered = true;
            marginLeft = 22;
            marginRight = 3;
            marginTop = 20;
            marginBottom = 85;

            winWidth = 0;
            winCentre = 0;
            signedImage = false;

            label1.Text = "";
            label2.Text = "";

            label1.ForeColor = c1;
            label3.ForeColor = c2;
        }

        public void SetWindowWidthCentre(int minVal, int maxVal, int widthVal, int centreVal, 
            ImageBitsPerPixel bpp, bool sign)
        {
            winMin = minVal;
            winMax = maxVal;
            winWidth = widthVal;
            winCentre = centreVal;
            iBpp = bpp;
            signedImage = sign;
            Invalidate();
        }

        void DrawEndPatches(Graphics gr)
        {
            Point pt1 = new Point(marginLeft, marginTop);
            Point pt2 = new Point(Width - marginRight, marginTop);
            Point pt3 = new Point(Width - marginRight, Height - marginBottom);
            Point pt4 = new Point(marginLeft, Height - marginBottom);            
            Brush br = new SolidBrush(SystemColors.Control);

            Point p1 = new Point(0,0);
            Size sz1 = new Size(marginLeft - 1, Height);
            Rectangle rect1 = new Rectangle(p1, sz1);
            gr.FillRectangle(br, rect1);

            Point p2 = new Point(Width - marginRight, 0);
            Size sz2 = new Size(marginRight, Height);
            Rectangle rect2 = new Rectangle(p2, sz2);
            gr.FillRectangle(br, rect2);

            br.Dispose();
        }

        void DrawBoundaryAndGrid(Graphics g)
        {
            // Boundary and Background
            Point pt1 = new Point(marginLeft, marginTop);
            Point pt2 = new Point(Width - marginRight, marginTop);
            Point pt3 = new Point(Width - marginRight, Height - marginBottom);
            Point pt4 = new Point(marginLeft, Height - marginBottom);
            Pen p = new Pen(Color.MediumAquamarine);
            Brush br = new SolidBrush(Color.LightYellow);

            // Background for the graph area
            Rectangle rect = new Rectangle(pt1.X, pt1.Y, pt2.X - pt1.X, pt3.Y - pt1.Y);
            g.FillRectangle(br, rect);

            Point pv11, pv21, ph11, ph21;
            pv11 = new Point();
            pv21 = new Point();
            ph11 = new Point();
            ph21 = new Point();

            int i, iNoVDivisions = 10, iNoHDivisions = 10;
            int iVertSpace = Convert.ToInt32((Height - marginTop - marginBottom) / iNoVDivisions);
            int iHorizSpace = Convert.ToInt32((Width - marginLeft - marginRight) / iNoHDivisions);

            // Horizontal grid lines
            for (i = 1; i < iNoVDivisions; ++i)
            {
                pv11.X = marginLeft;
                pv11.Y = marginTop + i * iVertSpace;
                pv21.X = Width - marginRight;
                pv21.Y = pv11.Y;
                g.DrawLine(p, pv11, pv21);
            }

            // Vertical grid lines
            for (i = 1; i < iNoHDivisions; ++i)
            {
                ph11.X = marginLeft + i * iHorizSpace;
                ph11.Y = marginTop;
                ph21.X = ph11.X;
                ph21.Y = Height - marginBottom;
                g.DrawLine(p, ph11, ph21);
            }

            // Boundary of the rectangle
            p.Color = Color.Firebrick;
            p.Width = 2;
            g.DrawLine(p, pt1, pt2);
            g.DrawLine(p, pt2, pt3);
            g.DrawLine(p, pt3, pt4);
            g.DrawLine(p, pt4, pt1);

            p.Dispose();
            br.Dispose();
        }

        void DrawLines(Graphics g)
        {
            graphWidth = Width - marginLeft - marginRight;
            graphHeight = Height - marginTop - marginBottom;
            int distFromOrig1, distFromOrig2;

            if (iBpp == ImageBitsPerPixel.Eight || iBpp == ImageBitsPerPixel.TwentyFour)
            {
                distFromOrig1 = ((winMin * graphWidth) / 256);
                distFromOrig2 = ((winMax * graphWidth) / 256);
            }
            else //if (iBpp == ImageBitsPerPixel.Sixteen)
            {
                distFromOrig1 = ((winMin * graphWidth) / 65536);
                distFromOrig2 = ((winMax * graphWidth) / 65536);
            }
            
            Point pt1 = new Point();
            Point pt2 = new Point();
            pt1.Y = marginTop + graphHeight;
            pt1.X = distFromOrig1 + marginLeft;

            pt2.Y = marginTop;
            pt2.X = distFromOrig2 + marginLeft;

            Pen p = new Pen(Color.Blue, 3);
            g.DrawLine(p, pt1, pt2);

            // Draw the line representing Window width 
            int marginBottom2 = marginBottom - 24;
            pt1.Y = Height - marginBottom2;
            pt2.Y = pt1.Y;
            p.Width = 4;
            p.Color = c1;
            if ((distFromOrig1 < 0) || (distFromOrig2 > graphWidth))
                p.DashStyle = DashStyle.Dash;
            g.DrawLine(p, pt1, pt2);

            // Draw the line representing Window centre or level
            Point pt3 = new Point();
            Point pt4 = new Point();
            p.Width = 2;
            pt3.X = (pt1.X + pt2.X) / 2;
            pt4.X = pt3.X;
            pt3.Y = pt1.Y - 5;  // 5 and 10 are magic numbers
            pt4.Y = pt3.Y + 10;
            p.Color = c2;
            p.DashStyle = DashStyle.Solid;
            g.DrawLine(p, pt3, pt4);

            p.Dispose();
        }

        private void DrawAxesLabels(Graphics gr)
        {
            Font f = new Font("Calibri", 10);
            Brush br = new SolidBrush(Color.Black); 
            PointF p = new PointF();

            // Labels on the vertical axis
            p.X = marginLeft - 24;
            p.Y = marginTop - 2;
            gr.DrawString("255", f, br, p);

            p.X = marginLeft - 10;
            p.Y = marginTop + graphHeight - 12;
            gr.DrawString("0", f, br, p);

            string strMax = "255";
            string strMin = "0";

            p.X = marginLeft - 5;
            p.Y = marginTop + graphHeight + 2;

            // Left label on the horizontal axis
            p.X = marginLeft - 2;            

            if (iBpp == ImageBitsPerPixel.Eight || iBpp == ImageBitsPerPixel.TwentyFour)
            {
                gr.DrawString(strMin, f, br, p);
                p.X = marginLeft + graphWidth - 24;
            }
            else // if(iBpp == ImageBitsPerPixel.Sixteen)
            {
                if (signedImage == true)
                {
                    strMax = "32767";
                    strMin = "-32768";
                }
                else
                {
                    strMax = "65535";
                    strMin = "0";
                }
                // Draw the left label on the horizontal axis
                gr.DrawString(strMin, f, br, p);
                p.X = marginLeft + graphWidth - 34;                
            }

            // Right label on the Horizontal Axis
            gr.DrawString(strMax, f, br, p);
            br.Dispose();

            br = new SolidBrush(Color.RosyBrown);

            p.X = marginLeft + 37;
            p.Y = marginTop + graphHeight + 2;
            gr.DrawString("Input Pix Val", f, br, p);

            p.X = marginLeft - 20;
            p.Y = marginTop +  25;
            StringFormat sf = new StringFormat(StringFormatFlags.DirectionVertical);
            gr.DrawString("Output Pix Val", f, br, p, sf);            

            f.Dispose();
            br.Dispose();
        }

        // Use double buffering to avoid flicker
        private void WindowLevelControl_Paint(object sender, PaintEventArgs e)
        {
            Bitmap bmp = new Bitmap(this.Width, this.Height);
            Graphics gr = Graphics.FromImage(bmp);

            // Do all drawing on the back buffer (double buffer)
            DrawBoundaryAndGrid(gr);
            if ((winWidth * winCentre) != 0) DrawLines(gr);
            DrawEndPatches(gr);
            if ((winWidth * winCentre) != 0) DrawAxesLabels(gr);

            // To display as numbers
            int winCentreToDisplay = winCentre;
            int winMinToDisplay = winMin;
            int winMaxToDisplay = winMax;

            if (signedImage == true)
            {
                winCentreToDisplay += short.MinValue;
                winMinToDisplay += short.MinValue;
                winMaxToDisplay += short.MinValue;
            }

            label1.Text = "Width=" + winWidth.ToString(); 
            label3.Text = "Level=" + winCentreToDisplay.ToString();
            label2.Text = "Win Min = " + winMinToDisplay.ToString() + "; Max = " + winMaxToDisplay.ToString();

            // Render the finished image on the graphics of the control
            e.Graphics.DrawImageUnscaled(bmp, 0, 0);
            gr.Dispose();
        }
    }
}
