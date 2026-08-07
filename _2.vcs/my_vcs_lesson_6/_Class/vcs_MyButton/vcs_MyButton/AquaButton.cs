using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;

namespace vcs_MyButton
{
    /*
    class AquaButton
    {
    }
    */
    //自定義Button ST

    /// <summary>  
    /// Summary description for AquaButton.  
    /// </summary>  
    [Serializable]
    public class AquaButton : System.Windows.Forms.Button
    {
        /// <summary>   
        /// Required designer variable.  
        /// </summary>  
        private System.ComponentModel.Container components = null;
        private bool pulseOnFocus;

        ///  
        ///Additional variables to handle pulsing  
        ///  
        private ImageAttributes imgAttr = new ImageAttributes();
        private float gamma;
        private float minGamma;
        private float maxGamma;
        private float gammaStep;
        private Timer pulseTimer = new Timer();
        private Bitmap buttonBitmap;
        private Rectangle buttonBitmapRectangle;

        public AquaButton()
        {
            // This call is required by the Windows.Forms Form Designer.  
            InitializeComponent();

            mouseAction = MouseActionType.None;

            this.SetStyle(ControlStyles.AllPaintingInWmPaint |
                ControlStyles.DoubleBuffer |
                ControlStyles.UserPaint, true);

            //The following defaults are better suited to draw the text outline  
            this.Font = new Font("Arial Black", 12, FontStyle.Bold);
            this.BackColor = Color.DarkTurquoise;
            this.Size = new Size(112, 48);

            //Initialize variables to Pulse button  
            gamma = 1.0f;
            minGamma = 1.0f;
            maxGamma = 2.2f;
            gammaStep = .2f;
            pulseTimer.Interval = 90;
            pulseTimer.Tick += new EventHandler(pulseTimer_Tick);
        }

        [DefaultValue(false)]
        public bool PulseOnFocus
        {
            get { return pulseOnFocus; }
            set { pulseOnFocus = value; Invalidate(); }
        }


        /// <summary>   
        /// Clean up any resources being used.  
        /// </summary>  
        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                if (components != null)
                {
                    components.Dispose();
                }
            }
            base.Dispose(disposing);
        }
        #region Component Designer generated code
        /// <summary>   
        /// Required method for Designer support - do not modify   
        /// the contents of this method with the code editor.  
        /// </summary>  
        private void InitializeComponent()
        {
            components = new System.ComponentModel.Container();
        }
        #endregion

        private enum MouseActionType
        {
            None,
            Hover,
            Click
        }

        private MouseActionType mouseAction;

        protected override void OnPaint(PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            g.Clear(Color.White);
            Color clr = this.BackColor;
            int shadowOffset = 8;
            int btnOffset = 0;
            switch (mouseAction)
            {
                case MouseActionType.Click:
                    shadowOffset = 4;
                    clr = Color.Gold;
                    btnOffset = 2;
                    break;
                case MouseActionType.Hover:
                    clr = Color.Gold;
                    break;
            }
            g.SmoothingMode = SmoothingMode.AntiAlias;

            ///  
            /// Create main colored shape  
            ///   
            Rectangle rc = new Rectangle(btnOffset, btnOffset, this.ClientSize.Width - 8 -
             btnOffset, this.ClientSize.Height - 8 - btnOffset);
            GraphicsPath path1 = this.GetPath(rc, 20);
            LinearGradientBrush br1 = new LinearGradientBrush(new Point(0, 0), new
            Point(0, rc.Height + 6), clr, Color.White);

            ///  
            /// Create shadow  
            ///   
            Rectangle rc2 = rc;
            rc2.Offset(shadowOffset, shadowOffset);
            GraphicsPath path2 = this.GetPath(rc2, 20);
            PathGradientBrush br2 = new PathGradientBrush(path2);
            br2.CenterColor = ControlPaint.DarkDark(Color.Silver);
            br2.SurroundColors = new Color[] { Color.White };

            ///  
            /// Create top water color to give "aqua" effect  
            ///   
            Rectangle rc3 = rc;
            rc3.Inflate(-5, -5);
            rc3.Height = 15;
            GraphicsPath path3 = GetPath(rc3, 20);
            LinearGradientBrush br3 = new LinearGradientBrush(rc3, Color.FromArgb(255,
            Color.White), Color.FromArgb(0, Color.White), LinearGradientMode.Vertical);

            ///  
            ///draw shapes  
            ///  
            g.FillPath(br2, path2); //draw shadow  
            g.FillPath(br1, path1); //draw main  
            g.FillPath(br3, path3); //draw top bubble  

            ///  
            ///Create a backup of the button image to a bitmap so we can manipulate it's pulsing action  
            ///  
            buttonBitmapRectangle = new Rectangle(rc.Location, rc.Size);
            buttonBitmap = new Bitmap(buttonBitmapRectangle.Width,
            buttonBitmapRectangle.Height);
            Graphics g_bmp = Graphics.FromImage(buttonBitmap);
            g_bmp.SmoothingMode = SmoothingMode.AntiAlias;
            g_bmp.FillPath(br1, path1);
            g_bmp.FillPath(br3, path3);

            ///  
            ///Set the region for the button  
            Region rgn = new Region(path1);
            rgn.Union(path2);
            this.Region = rgn;

            ///  
            /// Create a Path to draw the text to give the button a nice outline  
            ///   
            GraphicsPath path4 = new GraphicsPath();

            RectangleF path1bounds = path1.GetBounds();
            Rectangle rcText = new Rectangle((int)path1bounds.X, (int)path1bounds.Y,
            (int)path1bounds.Width, (int)path1bounds.Height);

            StringFormat strformat = new StringFormat();
            strformat.Alignment = StringAlignment.Center;
            strformat.LineAlignment = StringAlignment.Center;
            path4.AddString(this.Text, this.Font.FontFamily, (int)this.Font.Style,
            this.Font.Size, rcText, strformat);

            Pen txtPen = new Pen(this.ForeColor, 1);
            g.DrawPath(txtPen, path4);
            g_bmp.DrawPath(txtPen, path4);
        }
        private GraphicsPath GetPath(Rectangle rc, int r)
        {
            int x = rc.X, y = rc.Y, w = rc.Width, h = rc.Height;
            GraphicsPath path = new GraphicsPath();
            path.AddArc(x, y, r, r, 180, 90);               //Upper left corner  
            path.AddArc(x + w - r, y, r, r, 270, 90);         //Upper right corner  
            path.AddArc(x + w - r, y + h - r, r, r, 0, 90);     //Lower right corner  
            path.AddArc(x, y + h - r, r, r, 90, 90);          //Lower left corner  
            path.CloseFigure();
            return path;
        }

        protected override void OnMouseDown(MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                this.mouseAction = MouseActionType.Click;
                this.Invalidate();
            }
            base.OnMouseDown(e);
        }

        protected override void OnMouseUp(MouseEventArgs e)
        {
            if (this.Bounds.Contains(e.X, e.Y))
                this.mouseAction = MouseActionType.Hover;
            else
                this.mouseAction = MouseActionType.None;
            this.Invalidate();
            base.OnMouseUp(e);
        }


        protected override void OnMouseEnter(EventArgs e)
        {
            this.mouseAction = MouseActionType.Hover;
            this.Invalidate();
            base.OnMouseEnter(e);
        }

        protected override void OnMouseLeave(EventArgs e)
        {
            this.mouseAction = MouseActionType.None;
            this.Invalidate();
            base.OnMouseLeave(e);
        }

        //-----------------------------------------------------------------  
        // METHODS TO HANDLE PULSING  
        //-----------------------------------------------------------------  

        protected override void OnGotFocus(EventArgs e)
        {
            base.OnGotFocus(e);
            if (this.pulseOnFocus)
                pulseTimer.Start();
        }

        protected override void OnLostFocus(EventArgs e)
        {
            base.OnLostFocus(e);
            pulseTimer.Stop();
            this.Invalidate();  //redraw to get back it's original picture  
        }

        private void pulseTimer_Tick(object sender, EventArgs e)
        {
            if (this.Focused && pulseOnFocus && buttonBitmap != null)
            {
                gamma += gammaStep;
                if (gamma > this.maxGamma) gammaStep = -gammaStep;
                if (gamma < this.minGamma) gammaStep = Math.Abs(gammaStep);
                imgAttr.SetGamma(gamma);
                this.CreateGraphics().DrawImage(buttonBitmap,
                buttonBitmapRectangle, 0, 0,
                buttonBitmap.Width, buttonBitmap.Height, GraphicsUnit.Pixel, imgAttr);
            }
        }
    }

    //自定義Button SP

}
