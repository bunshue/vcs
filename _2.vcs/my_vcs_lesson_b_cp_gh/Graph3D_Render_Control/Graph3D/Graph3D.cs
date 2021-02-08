
/*****************************************************************************

This class has been written by Elmü (elmue@gmx.de)
It is based on code from Michał Bryłka but has been completely rewritten from the ground.
His code had several issues, bugs, misdesignes and a bad performance.

*****************************************************************************/

using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Text;
using System.Windows.Forms;
using System.Diagnostics;

namespace Plot3D
{
    /// <summary>
    /// ATTENTION: This class is not thread safe.
    /// Call all functions only from the GUI thread or use Control.Invoke()
    /// </summary>
    public class Graph3D : UserControl
    {
        #region enums

        public enum eRaster
        {
            Off,      // draw no coordinate system
            MainAxis, // draw solid axis X,Y,Z
            Raster,   // draw axis and dotted raster lines
            Labels,   // draw axis and dotted raster lines and labels in quadrant 3
        }

        // X and Y values must always be normalized. This cannot be turned off.
        // Center set     --> rotation (phi) goes through the center of the X, Y pane.
        // Center not set --> rotation (phi) around coordinate system root point {X=0, Y=0}
        // AdaptZ set     --> resize Z values so the are in the same range as X, Y values
        // AdaptZ not set --> resize Z values the same way as X,Y values
        // Lables set     --> display labels at the end of each axis (only in quadrant 3 and only in top view)
        [FlagsAttribute]
        public enum eNormalize
        {
            Center       = 1,
            AdaptZ       = 2,
            CenterAdaptZ = Center | AdaptZ,
        }

        public enum eCoord
        {
            X = 0,
            Y = 1,
            Z = 2,
        }

        enum eMouseAction
        {
            None = 0,
            Move,
            Rho,
            Theta,
            Phi,
        }

        #endregion

        #region cMouse 

        class cMouse
        {
            public eMouseAction me_Action;     // left mouse button action
            public Point        mk_LastPos;    // last mouse location
            public Point        mk_Offset;     // Offset for painting in OnPaint()
            public TrackBar     mi_TrackRho;   // Rho trackbar (optional)
            public TrackBar     mi_TrackTheta; // Theta trackbar (optional)
            public TrackBar     mi_TrackPhi;   // Phi trackbar (optional)
            public double       md_Rho   = VALUES_RHO  [2]; // 2 = Default value
            public double       md_Theta = VALUES_THETA[2]; // 2 = Default value
            public double       md_Phi   = VALUES_PHI  [2]; // 2 = Default value

            public void AssignTrackbar(eMouseAction e_Trackbar, TrackBar i_Trackbar, EventHandler i_OnScroll)
            {
                if (i_Trackbar == null)
                    return;

                double[] d_Values = null;
                switch (e_Trackbar)
                {
                    case eMouseAction.Rho:
                        d_Values      = VALUES_RHO;
                        mi_TrackRho   = i_Trackbar;
                        break;
                    case eMouseAction.Theta:
                        d_Values      = VALUES_THETA;
                        mi_TrackTheta = i_Trackbar;
                        break;
                    case eMouseAction.Phi:
                        d_Values      = VALUES_PHI;
                        mi_TrackPhi   = i_Trackbar;
                        break;
                }

                i_Trackbar.Minimum = (int)d_Values[0]; // 0 = Minimum
                i_Trackbar.Maximum = (int)d_Values[1]; // 1 = Maximum
                i_Trackbar.Value   = (int)d_Values[2]; // 2 = Default value
                i_Trackbar.Scroll += i_OnScroll;
            }

            /// <summary>
            /// User has moved the TrackBar
            /// </summary>
            public void OnTrackBarScroll()
            {
                if (mi_TrackRho   != null) md_Rho   = mi_TrackRho  .Value;
                if (mi_TrackTheta != null) md_Theta = mi_TrackTheta.Value;
                if (mi_TrackPhi   != null) md_Phi   = mi_TrackPhi  .Value;
            }

            /// <summary>
            /// User has dragged the mouse over the 3D control
            /// </summary>
            public void OnMouseMove(int s32_DiffX, int s32_DiffY)
            {
                switch (me_Action)
                {
                    case eMouseAction.Rho:
                        md_Rho += s32_DiffY *     VALUES_RHO[3];  // 3 = Factor
                        md_Rho = Math.Max(md_Rho, VALUES_RHO[0]); // 0 = Minimum
                        md_Rho = Math.Min(md_Rho, VALUES_RHO[1]); // 1 = Maximum
                        if (mi_TrackRho != null)
                            mi_TrackRho.Value = (int)md_Rho;
                        break;

                    case eMouseAction.Theta:
                        md_Theta -= s32_DiffY *       VALUES_THETA[3];  // 3 = Factor
                        md_Theta = Math.Max(md_Theta, VALUES_THETA[0]); // 0 = Minimum
                        md_Theta = Math.Min(md_Theta, VALUES_THETA[1]); // 1 = Maximum
                        if (mi_TrackTheta != null)
                            mi_TrackTheta.Value = (int)md_Theta;
                        break;

                    case eMouseAction.Phi:
                        md_Phi -= s32_DiffX * VALUES_PHI[3]; // 3 = Factor
                        if (md_Phi > 360.0) md_Phi -= 360.0; // continuous rotation
                        if (md_Phi <   0.0) md_Phi += 360.0; // continuous rotation
                        if (mi_TrackPhi != null)
                            mi_TrackPhi.Value = (int)md_Phi;
                        break;
                }
            }
        }

        #endregion

        #region cPoint3D

        public class cPoint3D
        {
            public double md_X;
            public double md_Y;
            public double md_Z;

            public cPoint3D()
            {
            }

            public cPoint3D(double X, double Y, double Z)
            {
                md_X = X;
                md_Y = Y;
                md_Z = Z;
            }

            public double GetValue(eCoord e_Coord)
            {
                switch (e_Coord)
                {
                    case eCoord.X: return md_X;
                    case eCoord.Y: return md_Y;
                    case eCoord.Z: return md_Z;
                    default:       return 0;
                }
            }
            public void SetValue(eCoord e_Coord, double d_Value)
            {
                switch (e_Coord)
                {
                    case eCoord.X: md_X = d_Value; break;
                    case eCoord.Y: md_Y = d_Value; break;
                    case eCoord.Z: md_Z = d_Value; break;
                }
            }

            // For debugging in Visual Studio
            public override string ToString()
            {
                return String.Format("{0:0.00}, {1:0.00}, {2:0.00}", md_X, md_Y, md_Z);
            }
        }

        #endregion

        #region cPoint2D

        private class cPoint2D
        {
            public double md_X;
            public double md_Y;

            public PointF Coord
            {
                get { return new PointF((float)md_X, (float)md_Y); }
            }

            // For debugging in Visual Studio
            public override string ToString()
            {
                return String.Format("{0:0.00}, {1:0.00}", md_X, md_Y);
            }
        }

        #endregion

        #region cMinMax3D

        private class cMinMax3D
        {
            public double md_MinX = double.PositiveInfinity;
            public double md_MaxX = double.NegativeInfinity;
            public double md_MinY = double.PositiveInfinity;
            public double md_MaxY = double.NegativeInfinity;
            public double md_MinZ = double.PositiveInfinity;
            public double md_MaxZ = double.NegativeInfinity;

            // Center point is subtracted from 3D values before converting to 2D
            public cPoint3D mi_Center = new cPoint3D();

            // Constructor
            public cMinMax3D(cPoint3D[,] i_Points3D)
            {
                for (int X = 0; X < i_Points3D.GetLength(0); X++)
                {
                    for (int Y = 0; Y < i_Points3D.GetLength(1); Y++)
                    {
                        cPoint3D i_Point3D = i_Points3D[X,Y];

                        md_MinX = Math.Min(md_MinX, i_Point3D.md_X);
                        md_MaxX = Math.Max(md_MaxX, i_Point3D.md_X);
                        md_MinY = Math.Min(md_MinY, i_Point3D.md_Y);
                        md_MaxY = Math.Max(md_MaxY, i_Point3D.md_Y);
                        md_MinZ = Math.Min(md_MinZ, i_Point3D.md_Z);
                        md_MaxZ = Math.Max(md_MaxZ, i_Point3D.md_Z);
                    }
                }
            }
        }

        #endregion

        #region cLine

        private class cLine
        {
            public eCoord     me_Line;    // main coordinate
            public eCoord     me_Offset;  // secondary coordinate
            public double     md_Label;   // Label for axis
            public Pen        mi_Pen;
            public double     md_Sort;
            public double     md_Angle;
            public cPoint3D[] mi_Points3D = new cPoint3D[2] { new cPoint3D(), new cPoint3D() }; // start and end point of line
            public cPoint2D[] mi_Points2D = new cPoint2D[2] { new cPoint2D(), new cPoint2D() };

            // Graphics.DrawLine() with huge length may take several seconds and block the GUI thread --> hanging.
            public bool IsValid
            {
                get
                {
                    foreach (cPoint2D i_Point in mi_Points2D)
                    {
                        if (Math.Abs(i_Point.md_X) > 9999.9 || Math.Abs(i_Point.md_Y) > 9999.9)
                            return false;
                    }
                    return true;
                }
            }

            /// <summary>
            /// Calculate the angle of the 3 main axis on the screen in a range from 0 to 360.
            /// </summary>
            public void CalcAngle2D()
            {
                double d_DX = mi_Points2D[1].md_X - mi_Points2D[0].md_X;
                double d_DY = mi_Points2D[1].md_Y - mi_Points2D[0].md_Y;
                md_Angle = Math.Atan2(d_DY, d_DX) * 180.0 / Math.PI;
                if (md_Angle < 0.0) md_Angle += 360.0;
            }
        }

        #endregion

        #region cPoygon

        private class cPolygon
        {
            public PointF[] mk_Points;  // 4 polygon points
            public double   md_FactorZ; // used to determine color

            // Graphics.FillPolygon() with huge coordinates may result in an Overflow Exception
            public bool IsValid
            {
                get
                {
                    foreach (PointF k_Point in mk_Points)
                    {
                        if (Math.Abs(k_Point.X) > 9999 || Math.Abs(k_Point.Y) > 9999)
                            return false;
                    }
                    return true;
                }
            }
        }

        #endregion

        #region cDrawObj

        private class cDrawObj
        {
            public cPolygon mi_Polygon;
            public cLine    mi_Line;
            public double   md_Sort;    // sorting is important. Always draw from back to front.
        }

        #endregion

        #region cQuadrant

        private class cQuadrant
        {
            public double md_SortXY;   // Sort order of raster in area XY  (red)
            public double md_SortXZ;   // Sort order of X axis and raster in area XZ (blue)
            public double md_SortYZ;   // Sort order of Y axis and raster in area YZ (green)
            public int    ms32_Quadrant;
            public bool   mb_BottomView;

            public cQuadrant(double d_MousePhi, cLine i_AxisX, cLine i_AxisY, cLine i_AxisZ)
            {
                // Split rotation into 4 sections (0...3) which increment every 90° starting at 45°
                int s32_Section45 = (int)d_MousePhi + 45;
                if (s32_Section45 > 360) s32_Section45 -= 360;
                s32_Section45 = Math.Min(3, s32_Section45 / 90);

                // Theta elevation lets the camera watch the graph from the top or bottom
                switch (s32_Section45)
                {
                    case 0: mb_BottomView = i_AxisX.md_Angle < 180.0; break;
                    case 1: mb_BottomView = i_AxisY.md_Angle < 180.0; break;
                    case 2: mb_BottomView = i_AxisX.md_Angle > 180.0; break;
                    case 3: mb_BottomView = i_AxisY.md_Angle > 180.0; break;
                }

                // The quadrant changes when the 2D transformed Z axis is in line with the X or Y axis
                if (mb_BottomView)
                {
                    switch (s32_Section45)
                    {
                        case 0: ms32_Quadrant = i_AxisX.md_Angle + 180.0 < i_AxisZ.md_Angle ? 1 : 0; break;
                        case 1: ms32_Quadrant = i_AxisY.md_Angle + 180.0 < i_AxisZ.md_Angle ? 2 : 1; break;
                        case 2: ms32_Quadrant = i_AxisX.md_Angle         < i_AxisZ.md_Angle ? 3 : 2; break;
                        case 3: ms32_Quadrant = i_AxisY.md_Angle         < i_AxisZ.md_Angle ? 0 : 3; break;
                    }
                }
                else // Top View
                {
                    switch (s32_Section45)
                    {
                        case 0: ms32_Quadrant = i_AxisX.md_Angle         > i_AxisZ.md_Angle ? 1 : 0; break;
                        case 1: ms32_Quadrant = i_AxisY.md_Angle         > i_AxisZ.md_Angle ? 2 : 1; break;
                        case 2: ms32_Quadrant = i_AxisX.md_Angle + 180.0 > i_AxisZ.md_Angle ? 3 : 2; break;
                        case 3: ms32_Quadrant = i_AxisY.md_Angle + 180.0 > i_AxisZ.md_Angle ? 0 : 3; break;
                    }
                }

                md_SortXY = (mb_BottomView) ? 99999.9 : -99999.9;
                md_SortXZ = (ms32_Quadrant == 1 || ms32_Quadrant == 2) ? 99999.9 : -99999.9;
                md_SortYZ = (ms32_Quadrant == 0 || ms32_Quadrant == 1) ? 99999.9 : -99999.9;

                i_AxisX.md_Sort = md_SortXZ;
                i_AxisY.md_Sort = md_SortYZ;
                i_AxisZ.md_Sort = 0.0;

                // Debug.WriteLine(String.Format("Section: {0}  Quadrant: {1}", s32_Section45, ms32_Quadrant));
            }
        }

        #endregion

        #region cTransform

        private class cTransform
        {
            private double md_Dist; // Screen Distance
            private double md_sf;
            private double md_st;
            private double md_cf;
            private double md_ct;
            private double md_Rho;
            // ----------------
            private double md_FactX;
            private double md_OffsX;
            private double md_FactY;
            private double md_OffsY;
            // ----------------
            public double  md_NormalizeXY;
            public double  md_NormalizeZ;

            public void SetCoeficients(cMouse i_Mouse)
            {
                md_Rho         =  i_Mouse.md_Rho;                           // Distance of viewer (zoom)
                double d_Theta =  i_Mouse.md_Theta       * Math.PI / 180.0; // Height   of viewer (elevation)
                double d_Phi   = (i_Mouse.md_Phi -180.0) * Math.PI / 180.0; // Rotation around center (-pi ... +pi)

                md_sf   = Math.Sin(d_Phi);
                md_cf   = Math.Cos(d_Phi);
                md_st   = Math.Sin(d_Theta);
                md_ct   = Math.Cos(d_Theta);
                md_Dist = 0.5; // Camera distance. Smaller values result in ugly stretched egdes when rotating.
            }

            public void SetSize(Size k_Size) // Control.ClientSize
            {
                double d_Width  = k_Size.Width  * 0.0254 / 96.0; // 0.0254 m = 1 inch. Screen has 96 DPI
                double d_Height = k_Size.Height * 0.0254 / 96.0;

                // linear transformation coeficients
                md_FactX =  k_Size.Width  / d_Width;
                md_FactY = -k_Size.Height / d_Height;
                
                md_OffsX =  md_FactX * d_Width  / 2.0;
                md_OffsY = -md_FactY * d_Height / 2.0;
            }

            // Performs projection. Calculates screen coordinates for 3D point.
            // returns Point in 2D space of the screen.
            public cPoint2D Project(cPoint3D i_Point3D, cPoint3D i_Center)
            {
                double X = (i_Point3D.md_X - i_Center.md_X) * md_NormalizeXY;
                double Y = (i_Point3D.md_Y - i_Center.md_Y) * md_NormalizeXY;
                double Z = (i_Point3D.md_Z - i_Center.md_Z) * md_NormalizeZ;

                // 3D coordinates with center point in the middle of the screen
                // X positive to the right, X negative to the left
                // Y positive to the top,   Y negative to the bottom
                double xn = -md_sf *         X + md_cf         * Y;
                double yn = -md_cf * md_ct * X - md_sf * md_ct * Y + md_st * Z;
                double zn = -md_cf * md_st * X - md_sf * md_st * Y - md_ct * Z + md_Rho;

                if (zn <= 0) zn = 0.01;

                // Thales' theorem
                cPoint2D i_Point2D = new cPoint2D();
                i_Point2D.md_X = md_FactX * xn * md_Dist / zn + md_OffsX;
                i_Point2D.md_Y = md_FactY * yn * md_Dist / zn + md_OffsY;
                return i_Point2D;
            }

            // Required for correct painting order of polygons (always from back to front)
            public double ProjectXY(double X, double Y)
            {
                return X * md_cf + Y * md_sf;
            }
        }

        #endregion

        // Limits and default values for mouse actions and trackbars.
        // ATTENTION: It is strongly recommended not to change the MIN, MAX values.
        // The mouse factor defines how much mouse movement you need for a change.
        // A movement of mouse by approx 1000 pixels on the screen results in getting from Min to Max or vice versa.
        //
        //                                                      MIN     MAX   DEFAULT  MOUSE FACTOR
        static readonly double[] VALUES_RHO   = new double[] {  300,   1800,   900,    2    };
        static readonly double[] VALUES_THETA = new double[] {   10,    170,    45,    0.25 }; // degree
        static readonly double[] VALUES_PHI   = new double[] {    0,    360,   120,    0.4  }; // degree  (continuous rotation)

        // Border in pixels around the 3D Graph in AutoSize mode
        const int AUTOSIZE_BORDER = 10;

        // The axis are 10% longer than the highest X,Y,Z value
        const double AXIS_EXCESS = 1.1;

        // Calculate 3-dimensional Z value from X,Y values
        public delegate double delRendererFunction(double X, double Y);

        Pen            mi_LinePen     = new Pen(Color.Black, 1);
        Pen            mi_BorderPen   = new Pen(Color.FromArgb(255,180,180,180), 1); // bright gray
        Pen[]          mi_AxisPen     = new Pen[3];
        Pen[]          mi_RasterPen   = new Pen[3];
        cTransform     mi_Transform   = new cTransform();
        List<cDrawObj> mi_DrawObjects = new List<cDrawObj>(); // cPolygon or cLine
        eRaster        me_Raster      = eRaster.Off;
        cMouse         mi_Mouse       = new cMouse();
        SolidBrush[]   mi_Brushes;
        Brush          mi_LegendBrush;
        cPoint3D[,]    mi_Points3D;
        cMinMax3D      mi_MinMax;
        cQuadrant      mi_Quadrant;
        bool           mb_AutoFitScreen;
        int            ms32_PolygonCount;

        /// <summary>
        /// setting LineColor = Color.Black draws black lines between the polygons
        /// setting LineColor = Color.Empty turns off lines between the polygons
        /// </summary>
        public Color LineColor
        {
            set
            {
                Debug.Assert(!InvokeRequired); // Do not call from other threads or use Invoke()
                if (value.A == 0) mi_LinePen = null; // transparent color
                else              mi_LinePen = new Pen(value);
                Invalidate(); // repaint only
            }
        }

        /// <summary>
        /// setting BorderColor = Color.Gray draws a gray border around the control
        /// setting BorderColor = Color.Empty turns off the border
        /// </summary>
        public Color BorderColor
        {
            set
            {
                Debug.Assert(!InvokeRequired); // Do not call from other threads or use Invoke()
                if (value.A == 0) mi_BorderPen = null; // transparent color
                else              mi_BorderPen = new Pen(value);
                Invalidate(); // repaint only
            }
        }

        /// <summary>
        /// Here you can set any amount of colors which will be used to paint to the polygons.
        /// </summary>
        public Color[] ColorSchema
        {
            set
            {
                Debug.Assert(!InvokeRequired); // Do not call from other threads or use Invoke()
                mi_Brushes = new SolidBrush[value.Length];
                for (int i = 0; i < mi_Brushes.Length; i++)
                {
                    mi_Brushes[i] = new SolidBrush(value[i]);
                }
                Invalidate(); // repaint only
            }
        }

        public eRaster Raster
        {
            set
            {
                Debug.Assert(!InvokeRequired); // Do not call from other threads or use Invoke()
				if (me_Raster != value)
				{
                    me_Raster = value;
                    mi_DrawObjects.Clear(); // recalculate
                    Invalidate();           // repaint
				}
            }
        }

        /// <summary>
        /// Setting this true will always adapt the size of the 3D graph to the size of the window.
        /// ATTENTION: Rotation will not be anymore around the center point.
        /// </summary>
        public bool AutoFitScreen
        {
            set 
            {
                Debug.Assert(!InvokeRequired); // Do not call from other threads or use Invoke()
                if (mb_AutoFitScreen != value)
                {
                    mb_AutoFitScreen   = value; 
                    mi_Mouse.mk_Offset = Point.Empty;
                    mi_DrawObjects.Clear(); // recalculate
                    Invalidate();           // repaint
                }
            }
        }

        /// <summary>
        /// returns the count of polygons
        /// </summary>
        public int PolygonCount
        {
            get { return ms32_PolygonCount; }
        }

        /// <summary>
        /// Show a legend with Rotation, Elevation and Distance
        /// </summary>
        public void EnableLegend(Color c_FontColor)
        {
            Debug.Assert(!InvokeRequired); // Do not call from other threads or use Invoke()
            mi_LegendBrush = new SolidBrush(c_FontColor);
        }

        /// <summary>
        /// Trackbars are optional for user interaction.
        /// If this function is never called thetrackbars are not used.
        /// </summary>
        public void AssignTrackBars(TrackBar i_Rho, TrackBar i_Theta, TrackBar i_Phi)
        {
            Debug.Assert(!InvokeRequired); // Do not call from other threads or use Invoke()
            mi_Mouse.AssignTrackbar(eMouseAction.Rho,   i_Rho,   new EventHandler(OnTrackbarScroll));
            mi_Mouse.AssignTrackbar(eMouseAction.Theta, i_Theta, new EventHandler(OnTrackbarScroll));
            mi_Mouse.AssignTrackbar(eMouseAction.Phi,   i_Phi,   new EventHandler(OnTrackbarScroll));
        }

        // ============================================================================

        // Constructor
        public Graph3D()
        {
            Debug.Assert(!InvokeRequired); // Do not call from other threads or use Invoke()

            // avoid flicker
            SetStyle(ControlStyles.AllPaintingInWmPaint,  true);
            SetStyle(ControlStyles.OptimizedDoubleBuffer, true);

            BackColor = Color.White;

            // Colors of main coordinate axis
            mi_AxisPen[0] = new Pen(Color.DarkBlue,  3);
            mi_AxisPen[1] = new Pen(Color.DarkGreen, 3);
            mi_AxisPen[2] = new Pen(Color.DarkRed,   3);

            // Colors of secondary raster lines
            mi_RasterPen[0] = new Pen(Color.FromArgb(255, 180, 100, 100), 1);
            mi_RasterPen[1] = new Pen(Color.FromArgb(255, 100, 180, 100), 1);
            mi_RasterPen[2] = new Pen(Color.FromArgb(255, 100, 100, 180), 1);

            mi_Transform.SetCoeficients(mi_Mouse);
        }

        // ============================================================================
   
        /// <summary>
        /// Here you can set a callback function delegate which will be called to calculate the 3D values.
        /// Use either SetFunction() or SetValues()
        /// </summary>
        public void SetFunction(delRendererFunction f_Function, PointF k_Start, PointF k_End, double d_Density, eNormalize e_Normalize)
        {
            Debug.Assert(!InvokeRequired); // Do not call from other threads or use Invoke()

            int s32_CountX = (int)((k_End.X - k_Start.X) / d_Density + 1);
            int s32_CountY = (int)((k_End.Y - k_Start.Y) / d_Density + 1);

            mi_Points3D = new cPoint3D[s32_CountX, s32_CountY];

            for (int X = 0; X < s32_CountX; X++)
            {
                for (int Y = 0; Y < s32_CountY; Y++)
                {
                    cPoint3D i_Point = new cPoint3D();
                    i_Point.md_X = k_Start.X + d_Density * X;
                    i_Point.md_Y = k_Start.Y + d_Density * Y;
                    i_Point.md_Z = f_Function(i_Point.md_X, i_Point.md_Y);

                    mi_Points3D[X, Y] = i_Point;
                }
            }

            NormalizeValues(e_Normalize);

            mi_Mouse.mk_Offset = Point.Empty;
            mi_DrawObjects.Clear(); // recalculate
            Invalidate();           // repaint
        }

        /// <summary>
        /// Here you can assign an Array of 3d points.
        /// Use either SetFunction() or SetValues()
        /// </summary>
        public void SetValues(cPoint3D[,] i_Points3D, eNormalize e_Normalize)
        {
            Debug.Assert(!InvokeRequired); // Do not call from other threads or use Invoke()

            mi_Points3D = i_Points3D;
            NormalizeValues(e_Normalize);

            mi_Mouse.mk_Offset = Point.Empty;
            mi_DrawObjects.Clear(); // recalculate
            Invalidate();           // repaint
        }

        /// <summary>
        /// This function normalizes the 3D values.
        /// Otherwise a 3D range of X,Y from -10 to +10 will appear much smaller than a range from -100 to +100.
        /// eNormalize.Center set     --> rotation (phi) goes through the center of the X, Y pane.
        /// eNormalize.Center not set --> rotation (phi) around coordinate system root point {X=0, Y=0}
        /// eNormalize.AdaptZ set     --> resize Z values so the are in the same range as X, Y values
        /// eNormalize.AdaptZ not set --> resize Z values the same way as X,Y values
        /// X and Y values are always normalized.
        /// </summary>
        private void NormalizeValues(eNormalize e_Normalize)
        {
            mi_MinMax = new cMinMax3D(mi_Points3D);

            ms32_PolygonCount = (mi_Points3D.GetLength(0) - 1) * (mi_Points3D.GetLength(1) - 1);
            if (ms32_PolygonCount < 1)
                throw new Exception("Insufficient 3D points specified");

            // Normalize 3D X,Y,Z values to compensate different ranges of X min ... X max and Y min ... Y max
            double d_RangeXY = Math.Max(mi_MinMax.md_MaxX - mi_MinMax.md_MinX, mi_MinMax.md_MaxY - mi_MinMax.md_MinY);
            if (d_RangeXY == 0.0)
                throw new Exception("The 3D points cannot have all the same X,Y coordinates");

            double d_FactorXY = 250.0 / d_RangeXY;
            
            double d_FactorZ = d_FactorXY;
            if ((e_Normalize & eNormalize.AdaptZ) != 0)
            {
                double d_RangeZ;
                if (me_Raster == eRaster.Off)
                    d_RangeZ = mi_MinMax.md_MaxZ - mi_MinMax.md_MinZ;
                else
                    d_RangeZ = Math.Max(0, mi_MinMax.md_MaxZ) - Math.Min(0, mi_MinMax.md_MinZ);

                if (d_RangeZ > 0.0)
                    d_FactorZ = 250.0 / d_RangeZ;
            }

            mi_Transform.md_NormalizeXY = d_FactorXY;
            mi_Transform.md_NormalizeZ  = d_FactorZ;

            if ((e_Normalize & eNormalize.Center) != 0)
            {
                mi_MinMax.mi_Center.md_X = (mi_MinMax.md_MaxX + mi_MinMax.md_MinX) / 2.0;
                mi_MinMax.mi_Center.md_Y = (mi_MinMax.md_MaxY + mi_MinMax.md_MinY) / 2.0;

                if ((e_Normalize & eNormalize.AdaptZ) != 0)
                {
                    if (me_Raster == eRaster.Off)
                        mi_MinMax.mi_Center.md_Z = (mi_MinMax.md_MaxZ + mi_MinMax.md_MinZ) / 2.0;
                    else
                        mi_MinMax.mi_Center.md_Z = (Math.Max(0, mi_MinMax.md_MaxZ) + Math.Min(0, mi_MinMax.md_MinZ)) / 2.0;
                }
            }
        }

        // ============================================================================

        private void CalcPolygons()
        {
            ms32_PolygonCount = 0;
            mi_DrawObjects.Clear();

            if (mi_Points3D == null)
                return; // no 3D data present

            cPoint2D[,] i_Points2D = new cPoint2D[mi_Points3D.GetLength(0), mi_Points3D.GetLength(1)];
            List<cLine> i_Lines = new List<cLine>();

            double d_Min2X = double.PositiveInfinity;
            double d_Max2X = double.NegativeInfinity;
            double d_Min2Y = double.PositiveInfinity;
            double d_Max2Y = double.NegativeInfinity;
            for (int X = 0; X < mi_Points3D.GetLength(0); X++)
            {
                for (int Y = 0; Y < mi_Points3D.GetLength(1); Y++)
                {
                    cPoint3D i_Point3D = mi_Points3D[X,Y];
                    cPoint2D i_Point2D = mi_Transform.Project(i_Point3D, mi_MinMax.mi_Center);
                    i_Points2D[X,Y] = i_Point2D;

                    d_Min2X = Math.Min(d_Min2X, i_Point2D.md_X);
                    d_Max2X = Math.Max(d_Max2X, i_Point2D.md_X);
                    d_Min2Y = Math.Min(d_Min2Y, i_Point2D.md_Y);
                    d_Max2Y = Math.Max(d_Max2Y, i_Point2D.md_Y);
                }
            }

            if (me_Raster != eRaster.Off)
            {
                // Add coordinate system main lines
                for (int A=0; A<3; A++)
                {
                    cLine i_Axis  = new cLine();
                    i_Axis.mi_Pen = mi_AxisPen[A];

                    switch ((eCoord)A)
                    {
                        case eCoord.X: // Blue
                            i_Axis.mi_Points3D[0].md_X = Math.Min(0.0, mi_MinMax.md_MinX * AXIS_EXCESS);
                            i_Axis.mi_Points3D[1].md_X = Math.Max(0.0, mi_MinMax.md_MaxX * AXIS_EXCESS);
                            break;
                        case eCoord.Y: // Green
                            i_Axis.mi_Points3D[0].md_Y = Math.Min(0.0, mi_MinMax.md_MinY * AXIS_EXCESS);
                            i_Axis.mi_Points3D[1].md_Y = Math.Max(0.0, mi_MinMax.md_MaxY * AXIS_EXCESS);
                            break;
                        case eCoord.Z: // Red
                            i_Axis.mi_Points3D[0].md_Z = Math.Min(0.0, mi_MinMax.md_MinZ * AXIS_EXCESS);
                            i_Axis.mi_Points3D[1].md_Z = Math.Max(0.0, mi_MinMax.md_MaxZ * AXIS_EXCESS);
                            break;
                    }

                    i_Axis.mi_Points2D[0] = mi_Transform.Project(i_Axis.mi_Points3D[0], mi_MinMax.mi_Center);
                    i_Axis.mi_Points2D[1] = mi_Transform.Project(i_Axis.mi_Points3D[1], mi_MinMax.mi_Center);
                    i_Axis.CalcAngle2D();

                    i_Lines.Add(i_Axis);
                }

                mi_Quadrant = new cQuadrant(mi_Mouse.md_Phi, i_Lines[(int)eCoord.X], i_Lines[(int)eCoord.Y], i_Lines[(int)eCoord.Z]);

                // Add raster lines in 6 different directions
                if (me_Raster >= eRaster.Raster)
                {
                    for (int A=0; A<3; A++)
                    {
                        // Combine X+Y, Y+Z, Z+X
                        eCoord e_First  = (eCoord)(A);
                        eCoord e_Second = (eCoord)((A+1) % 3);

                        cLine i_FirstAxis  = i_Lines[(int)e_First];
                        cLine i_SecondAxis = i_Lines[(int)e_Second];

                        double d_FirstStart = i_FirstAxis.mi_Points3D[0].GetValue(e_First);
                        double d_FirstEnd   = i_FirstAxis.mi_Points3D[1].GetValue(e_First);

                        double d_SecndStart = i_SecondAxis.mi_Points3D[0].GetValue(e_Second);
                        double d_SecndEnd   = i_SecondAxis.mi_Points3D[1].GetValue(e_Second);

                        // Distance between raster lines
                        double d_Interval = CalculateInterval(d_SecndEnd - d_SecndStart);

                        double d_OffPos = 0.0;
                        double d_OffNeg = 0.0;
                        for (int L=1; L<=10; L++)
                        {
                            d_OffPos += d_Interval;
                            d_OffNeg -= d_Interval;

                            // Draw raster on positive side
                            if (d_OffPos <= d_SecndEnd) 
                                AddRasterLine(i_Lines, mi_RasterPen[A], e_First, d_FirstStart, d_FirstEnd, e_Second, d_OffPos);

                            // Draw raster on negative side (only if negative values exist)
                            if (d_OffNeg >= d_SecndStart) 
                                AddRasterLine(i_Lines, mi_RasterPen[A], e_First, d_FirstStart, d_FirstEnd, e_Second, d_OffNeg);
                        }

                        d_Interval = d_Interval = CalculateInterval(d_FirstEnd - d_FirstStart);

                        d_OffPos = 0.0;
                        d_OffNeg = 0.0;
                        for (int L=1; L<=10; L++)
                        {
                            d_OffPos += d_Interval;
                            d_OffNeg -= d_Interval;

                            // Draw raster on positive side
                            if (d_OffPos <= d_FirstEnd) 
                                AddRasterLine(i_Lines, mi_RasterPen[A], e_Second, d_SecndStart, d_SecndEnd, e_First, d_OffPos);

                            // Draw raster on negative side (only if negative values exist)
                            if (d_OffNeg >= d_FirstStart)
                                AddRasterLine(i_Lines, mi_RasterPen[A], e_Second, d_SecndStart, d_SecndEnd, e_First, d_OffNeg);
                        }
                    }
                }

                // Convert axis and raster lines 3D --> 2D
                foreach (cLine i_Line in i_Lines)
                {
                    for (int P=0; P<2; P++)
                    {
                        cPoint2D i_Point2D = mi_Transform.Project(i_Line.mi_Points3D[P], mi_MinMax.mi_Center);
                        i_Line.mi_Points2D[P] = i_Point2D;

                        d_Min2X = Math.Min(d_Min2X, i_Point2D.md_X);
                        d_Max2X = Math.Max(d_Max2X, i_Point2D.md_X);
                        d_Min2Y = Math.Min(d_Min2Y, i_Point2D.md_Y);
                        d_Max2Y = Math.Max(d_Max2Y, i_Point2D.md_Y);
                    }
                }
            }

            if (mb_AutoFitScreen)
            {
                Size k_Screen = ClientSize;
                k_Screen.Width  -= 2 * AUTOSIZE_BORDER;
                k_Screen.Height -= 2 * AUTOSIZE_BORDER;

                double d_FactorX = k_Screen.Width  / (d_Max2X - d_Min2X);
                double d_FactorY = k_Screen.Height / (d_Max2Y - d_Min2Y);
                double d_Factor  = Math.Min(d_FactorX, d_FactorY);

                double d_OffsetX = AUTOSIZE_BORDER - d_Min2X * d_Factor + (k_Screen.Width  - (d_Max2X - d_Min2X) * d_Factor) / 2.0;
                double d_OffsetY = AUTOSIZE_BORDER - d_Min2Y * d_Factor + (k_Screen.Height - (d_Max2Y - d_Min2Y) * d_Factor) / 2.0;

                for (int X = 0; X < i_Points2D.GetLength(0); X++)
                {
                    for (int Y = 0; Y < i_Points2D.GetLength(1); Y++)
                    {
                        cPoint2D i_Point2D = i_Points2D[X,Y];
                        i_Point2D.md_X = i_Point2D.md_X * d_Factor + d_OffsetX;
                        i_Point2D.md_Y = i_Point2D.md_Y * d_Factor + d_OffsetY;
                    }
                }

                foreach (cLine i_Line in i_Lines)
                {
                    for (int P=0; P<2; P++)
                    {
                        cPoint2D i_Point2D = i_Line.mi_Points2D[P];
                        i_Point2D.md_X = i_Point2D.md_X * d_Factor + d_OffsetX;
                        i_Point2D.md_Y = i_Point2D.md_Y * d_Factor + d_OffsetY;
                    }
                }
            }

            // Avoid division by zero crash if d_Max == d_Min
            double d_Range3Z = Math.Max(0.00001, mi_MinMax.md_MaxZ - mi_MinMax.md_MinZ); 

            // Create polygons
            for (int X = 0; X < mi_Points3D.GetLength(0) -1; X++)
            {
                for (int Y = 0; Y < mi_Points3D.GetLength(1) -1; Y++)
                {
                    cPolygon i_Poly  = new cPolygon();
                    i_Poly.mk_Points = new PointF[] { i_Points2D[X,   Y]  .Coord,
                                                      i_Points2D[X,   Y+1].Coord,
                                                      i_Points2D[X+1, Y+1].Coord,
                                                      i_Points2D[X+1, Y]  .Coord };
                    
                    double Z1 = mi_Points3D[X,   Y]  .md_Z;
                    double Z2 = mi_Points3D[X,   Y+1].md_Z;
                    double Z3 = mi_Points3D[X+1, Y+1].md_Z;
                    double Z4 = mi_Points3D[X+1, Y]  .md_Z;
                    double Zavrg = (Z1 + Z2 + Z3 + Z4) / 4.0;

                    i_Poly.md_FactorZ = (Zavrg - mi_MinMax.md_MinZ) / d_Range3Z;
                    i_Poly.md_FactorZ = Math.Min(1.0, i_Poly.md_FactorZ);
                    i_Poly.md_FactorZ = Math.Max(0.0, i_Poly.md_FactorZ);

                    // Polygons must be painted in correct order: from behind to front. Order depends on rotation angle.
                    double d_Sort = mi_Transform.ProjectXY(X+1, Y+1);

                    AddDrawObject(i_Poly, null, d_Sort);
                    ms32_PolygonCount ++;
                }
            }

            foreach (cLine i_Line in i_Lines)
            {
                AddDrawObject(null, i_Line, i_Line.md_Sort);
            }
        }

        // Create a line from {d_Start, d_Offset} to {d_End, d_Offset}
        // The coordinates may be X,Y,Z 
        private void AddRasterLine(List<cLine> i_Lines, Pen i_Pen,
                                   eCoord e_Line,   double d_Start, double d_End, 
                                   eCoord e_Offset, double d_Offset)
        {
            cLine i_Raster = new cLine();
            i_Raster.mi_Pen    = i_Pen;
            i_Raster.me_Line   = e_Line;
            i_Raster.me_Offset = e_Offset;
            i_Raster.md_Label  = d_Offset;

            i_Raster.mi_Points3D[0].SetValue(e_Line, d_Start);
            i_Raster.mi_Points3D[1].SetValue(e_Line, d_End);

            i_Raster.mi_Points3D[0].SetValue(e_Offset, d_Offset);
            i_Raster.mi_Points3D[1].SetValue(e_Offset, d_Offset);

            if ((e_Line == eCoord.X && e_Offset == eCoord.Z) || // Blue
                (e_Line == eCoord.Z && e_Offset == eCoord.X))
            {
                i_Raster.md_Sort = mi_Quadrant.md_SortXZ;
            }
            else if ((e_Line == eCoord.Z && e_Offset == eCoord.Y) || // Green
                     (e_Line == eCoord.Y && e_Offset == eCoord.Z))
            {
                i_Raster.md_Sort = mi_Quadrant.md_SortYZ;
            }
            else // X + Y Red
            {
                i_Raster.md_Sort = mi_Quadrant.md_SortXY;
            }

            i_Lines.Add(i_Raster);
        }

        /// <summary>
        /// returns intervals of  0.1, 0.2, 0.5,  1, 2, 5,  10, 20, 50,  etc...
        /// The count of intervals which fit into the range is always between 5 and 10
        /// </summary>
        static double CalculateInterval(double d_Range)
        {
            double d_Factor = Math.Pow(10.0, Math.Floor(Math.Log10(d_Range)));
            if (d_Range / d_Factor >= 5.0)
                return d_Factor;
            else if (d_Range / (d_Factor / 2.0) >= 5.0)
                return d_Factor / 2.0;
            else
                return d_Factor / 5.0;
        }

        /// <summary>
        /// Polygons and axis must be sorted for correct drawing order
        /// </summary>
        private void AddDrawObject(cPolygon i_Poly, cLine i_Line, double d_Sort)
        {
            cDrawObj i_DrawObj = new cDrawObj();
            i_DrawObj.mi_Polygon = i_Poly;
            i_DrawObj.mi_Line    = i_Line;
            i_DrawObj.md_Sort    = d_Sort;

            int P;
            for (P=0; P<mi_DrawObjects.Count; P++)
            {
                if (mi_DrawObjects[P].md_Sort > d_Sort)
                    break;
            }
            mi_DrawObjects.Insert(P, i_DrawObj);
        }

        // ============================================================================

        protected override void OnPaintBackground(PaintEventArgs e)
        {
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            if (mi_DrawObjects.Count == 0)
                CalcPolygons();

            e.Graphics.Clear(BackColor);

            if (mi_LegendBrush != null)
            {
                String[] s_Legend = new String[] { "Rotation:", "Elevation:", "Distance:" };
                String[] s_Value  = new String[] { String.Format("{0:+#;-#;0}°", (int)mi_Mouse.md_Phi),
                                                   String.Format("{0:+#;-#;0}°", (int)mi_Mouse.md_Theta),
                                                   String.Format("{0}",          (int)mi_Mouse.md_Rho) };

                SizeF k_Size = e.Graphics.MeasureString(s_Legend[1], Font); // measure the widest string
                int X = 4;
                int Y = 3;
                for (int i=0; i<3; i++)
                {
                    e.Graphics.DrawString(s_Legend[i], Font, mi_LegendBrush, X,  Y);
                    e.Graphics.DrawString(s_Value [i], Font, mi_LegendBrush, X + k_Size.Width, Y);
                    Y += Font.Height;
                }
            }

            // Set X, Y offset which user has set by mouse dragging with SHIFT key pressed
            e.Graphics.TranslateTransform(mi_Mouse.mk_Offset.X, mi_Mouse.mk_Offset.Y);

            SmoothingMode e_Smooth = SmoothingMode.Invalid;

            foreach (cDrawObj i_DrawObj in mi_DrawObjects)
            {
                if (i_DrawObj.mi_Polygon != null)
                {
                    cPolygon i_Poly = i_DrawObj.mi_Polygon;
                    if (!i_Poly.IsValid)
                        continue; // avoid overflow exception

                    Brush i_Brush = Brushes.Goldenrod;
                    if (mi_Brushes != null)
                    {
                        // md_FactorZ is a value between 0.0 and 1.0
                        int s32_Brush = (int)(i_Poly.md_FactorZ * (mi_Brushes.Length - 1));
                        i_Brush = mi_Brushes[s32_Brush];
                    }

                    if (e_Smooth != SmoothingMode.None) // avoid unneccessary calls into GDI+ (speed optimization)
                    {
                        e_Smooth = SmoothingMode.None;
                        e.Graphics.SmoothingMode = SmoothingMode.None;
                    }

                    e.Graphics.FillPolygon(i_Brush, i_Poly.mk_Points);

                    if (mi_LinePen != null)
                    {
                        e.Graphics.DrawPolygon(mi_LinePen, i_Poly.mk_Points);
                    }
                }
                else
                {
                    cLine i_Line = i_DrawObj.mi_Line;
                    if (!i_Line.IsValid)
                        continue; // avoid hanging

                    if (e_Smooth != SmoothingMode.AntiAlias) // avoid unneccessary calls into GDI+ (speed optimization)
                    {
                        e_Smooth = SmoothingMode.AntiAlias;
                        e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
                    }

                    e.Graphics.DrawLine(i_Line.mi_Pen, i_Line.mi_Points2D[0].Coord, i_Line.mi_Points2D[1].Coord);

                    // ------------ Label ------------

                    if (me_Raster == eRaster.Labels        && 
                        i_Line.md_Label           != 0.0   && // no label for main axis
                        mi_Quadrant.mb_BottomView == false && // no label in bottom view
                        mi_Quadrant.ms32_Quadrant == 3)       // only in quadrant 3 showing labels makes sense
                    {
                        PointF k_Pos = i_Line.mi_Points2D[1].Coord;
                        StringFormat i_Format = new StringFormat();
                        if (i_Line.me_Line == eCoord.Y && i_Line.me_Offset == eCoord.Z)
                        {
                            k_Pos.X += 5;
                            k_Pos.Y -= Font.Height / 2;
                        }
                        else if (i_Line.me_Line == eCoord.Y && i_Line.me_Offset == eCoord.X)
                        {
                            k_Pos.X += (float)mi_Transform.ProjectXY(5, -5);
                            k_Pos.Y += (float)mi_Transform.ProjectXY(-Font.Height / 2, 5);
                        }
                        else if (i_Line.me_Line == eCoord.X && i_Line.me_Offset == eCoord.Y)
                        {
                            k_Pos.X += (float)mi_Transform.ProjectXY(5, -5);
                            k_Pos.Y += (float)mi_Transform.ProjectXY(5, -Font.Height / 2);
                            i_Format.Alignment = StringAlignment.Far;
                        }
                        else continue;

                        String s_Label = ((int)i_Line.md_Label).ToString();
                        e.Graphics.DrawString(s_Label, Font, Brushes.Black, k_Pos, i_Format);
                    }
                }
            }

            if (mi_BorderPen != null)
            {
                e.Graphics.TranslateTransform(-mi_Mouse.mk_Offset.X, -mi_Mouse.mk_Offset.Y);
                Rectangle r_Border = ClientRectangle;
                e.Graphics.DrawRectangle(mi_BorderPen, r_Border.X, r_Border.Y, r_Border.Width - 1, r_Border.Height - 1);
            }
        }

        // ============================================================================

        protected override void OnMouseDown(MouseEventArgs e)
        {
            base.OnMouseDown(e);

            mi_Mouse.mk_LastPos = e.Location;

            if (mi_DrawObjects.Count == 0)
                return;
           
            switch (Control.ModifierKeys)
            {
                case Keys.None:
                    if (e.Button == MouseButtons.Left)
                    {
                        Cursor = Cursors.NoMoveVert;
                        mi_Mouse.me_Action = eMouseAction.Theta;
                    }

                    if (e.Button == MouseButtons.Right)
                    {
                        Cursor = Cursors.NoMoveHoriz;
                        mi_Mouse.me_Action = eMouseAction.Phi;
                    }
                    break;

                case Keys.Shift:
                    if (e.Button == MouseButtons.Left && !mb_AutoFitScreen)
                    {
                        Cursor = Cursors.NoMove2D;
                        mi_Mouse.me_Action = eMouseAction.Move;
                    }
                    break;

                case Keys.Control:
                    if (e.Button == MouseButtons.Left)
                    {
                        Cursor = Cursors.SizeNS;
                        mi_Mouse.me_Action = eMouseAction.Rho;
                    }
                    break;
            }
        }

        protected override void OnMouseUp(MouseEventArgs e)
        {
            base.OnMouseUp(e);
            mi_Mouse.me_Action = eMouseAction.None;
            Cursor = Cursors.Arrow;
        }

        protected override void OnMouseLeave(EventArgs e)
        {
            base.OnMouseLeave(e);
            mi_Mouse.me_Action = eMouseAction.None;
            Cursor = Cursors.Arrow;
        }

        protected override void OnMouseMove(MouseEventArgs e)
        {
            base.OnMouseMove(e);

            int s32_DiffX = e.X - mi_Mouse.mk_LastPos.X;
            int s32_DiffY = e.Y - mi_Mouse.mk_LastPos.Y;
            mi_Mouse.mk_LastPos = e.Location;

            switch (mi_Mouse.me_Action)
            {
                case eMouseAction.Move:
                    mi_Mouse.mk_Offset.X += s32_DiffX;
                    mi_Mouse.mk_Offset.Y += s32_DiffY;

                    Invalidate(); // repaint only
                    break;

                case eMouseAction.Rho:
                case eMouseAction.Theta:
                case eMouseAction.Phi:
                    mi_Mouse.OnMouseMove(s32_DiffX, s32_DiffY);
                    mi_Transform.SetCoeficients(mi_Mouse);

                    mi_DrawObjects.Clear(); // recalculate
                    Invalidate();           // repaint
                    break;
            }
        }

        // ============================================================================

        /// <summary>
        /// This is only called when the user moves the trackbar, not when TrackBar.Value is set programmatically.
        /// </summary>
        void OnTrackbarScroll(object sender, EventArgs e)
        {
            mi_Mouse.OnTrackBarScroll();
            mi_Transform.SetCoeficients(mi_Mouse);

            mi_DrawObjects.Clear(); // recalculate
            Invalidate();           // repaint
        }

        protected override void OnSizeChanged(EventArgs e)
        {
            base.OnSizeChanged(e);

            mi_Transform.SetSize(ClientSize);

            mi_DrawObjects.Clear(); // recalculate
            Invalidate();           // repaint
        }
    }
}