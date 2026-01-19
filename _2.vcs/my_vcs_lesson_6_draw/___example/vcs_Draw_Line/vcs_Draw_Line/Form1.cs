using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_Draw_Line
{
    public partial class Form1 : Form
    {
        // The grid spacing.
        const int grid_gap = 8;

        // The "size" of an object for mouse over purposes.
        private const int object_radius = 3;

        // We're over an object if the distance squared
        // between the mouse and the object is less than this.
        private const int over_dist_squared = object_radius * object_radius;

        // The points that make up the line segments.
        private List<Point> Pt1 = new List<Point>();
        private List<Point> Pt2 = new List<Point>();

        // Points for the new line.
        private bool IsDrawing = false;
        private Point NewPt1, NewPt2;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        // The mouse is up. See whether we're over an end point or segment.
        private void picCanvas_MouseMove_NotDown(object sender, MouseEventArgs e)
        {
            Cursor new_cursor = Cursors.Cross;

            // See what we're over.
            Point hit_point;
            int segment_number;

            if (MouseIsOverEndpoint(e.Location, out segment_number, out hit_point))
            {
                new_cursor = Cursors.Arrow;
            }
            else if (MouseIsOverSegment(e.Location, out segment_number))
            {
                new_cursor = Cursors.Hand;
            }

            // Set the new cursor.
            if (picCanvas.Cursor != new_cursor)
            {
                picCanvas.Cursor = new_cursor;
            }
        }

        // See what we're over and start doing whatever is appropriate.
        private void picCanvas_MouseDown(object sender, MouseEventArgs e)
        {
            // See what we're over.
            Point hit_point;
            int segment_number;

            if (MouseIsOverEndpoint(e.Location, out segment_number, out hit_point))
            {
                // Start moving this end point.
                picCanvas.MouseMove -= picCanvas_MouseMove_NotDown;
                picCanvas.MouseMove += picCanvas_MouseMove_MovingEndPoint;
                picCanvas.MouseUp += picCanvas_MouseUp_MovingEndPoint;

                // Remember the segment number.
                MovingSegment = segment_number;

                // See if we're moving the start end point.
                MovingStartEndPoint = (Pt1[segment_number].Equals(hit_point));

                // Remember the offset from the mouse to the point.
                OffsetX = hit_point.X - e.X;
                OffsetY = hit_point.Y - e.Y;
            }
            else if (MouseIsOverSegment(e.Location, out segment_number))
            {
                // Start moving this segment.
                picCanvas.MouseMove -= picCanvas_MouseMove_NotDown;
                picCanvas.MouseMove += picCanvas_MouseMove_MovingSegment;
                picCanvas.MouseUp += picCanvas_MouseUp_MovingSegment;

                // Remember the segment number.
                MovingSegment = segment_number;

                // Remember the offset from the mouse to the segment's first point.
                OffsetX = Pt1[segment_number].X - e.X;
                OffsetY = Pt1[segment_number].Y - e.Y;
            }
            else
            {
                // Start drawing a new segment.
                picCanvas.MouseMove -= picCanvas_MouseMove_NotDown;
                picCanvas.MouseMove += picCanvas_MouseMove_Drawing;
                picCanvas.MouseUp += picCanvas_MouseUp_Drawing;

                IsDrawing = true;

                int x = e.X;
                int y = e.Y;
                SnapToGrid(ref x, ref y);
                NewPt1 = new Point(x, y);
                NewPt2 = new Point(x, y);
            }
        }

        // Snap to the nearest grid point.
        private void SnapToGrid(ref int x, ref int y)
        {
            if (!chkSnapToGrid.Checked)
            {
                return;
            }
            x = grid_gap * (int)Math.Round((double)x / grid_gap);
            y = grid_gap * (int)Math.Round((double)y / grid_gap);
        }

        #region "Drawing"

        // We're drawing a new segment.
        private void picCanvas_MouseMove_Drawing(object sender, MouseEventArgs e)
        {
            // Save the new point.
            int x = e.X;
            int y = e.Y;
            SnapToGrid(ref x, ref y);
            NewPt2 = new Point(x, y);

            // Redraw.
            picCanvas.Invalidate();
        }

        // Stop drawing.
        private void picCanvas_MouseUp_Drawing(object sender, MouseEventArgs e)
        {
            IsDrawing = false;

            // Reset the event handlers.
            picCanvas.MouseMove -= picCanvas_MouseMove_Drawing;
            picCanvas.MouseMove += picCanvas_MouseMove_NotDown;
            picCanvas.MouseUp -= picCanvas_MouseUp_Drawing;

            // Create the new segment.
            Pt1.Add(NewPt1);
            Pt2.Add(NewPt2);

            // Redraw.
            picCanvas.Invalidate();
        }

        #endregion // Drawing

        #region "Moving End Point"

        // The segment we're moving or the segment whose end point we're moving.
        private int MovingSegment = -1;

        // The end point we're moving.
        private bool MovingStartEndPoint = false;

        // The offset from the mouse to the object being moved.
        private int OffsetX, OffsetY;

        // We're moving an end point.
        private void picCanvas_MouseMove_MovingEndPoint(object sender, MouseEventArgs e)
        {
            // Move the point to its new location.
            int x = e.X + OffsetX;
            int y = e.Y + OffsetY;
            SnapToGrid(ref x, ref y);

            if (MovingStartEndPoint)
                Pt1[MovingSegment] = new Point(x, y);
            else
                Pt2[MovingSegment] = new Point(x, y);

            // Redraw.
            picCanvas.Invalidate();
        }

        // Stop moving the end point.
        private void picCanvas_MouseUp_MovingEndPoint(object sender, MouseEventArgs e)
        {
            // Reset the event handlers.
            picCanvas.MouseMove += picCanvas_MouseMove_NotDown;
            picCanvas.MouseMove -= picCanvas_MouseMove_MovingEndPoint;
            picCanvas.MouseUp -= picCanvas_MouseUp_MovingEndPoint;

            // Redraw.
            picCanvas.Invalidate();
        }

        #endregion // Moving End Point

        #region "Moving Segment"

        // We're moving a segment.
        private void picCanvas_MouseMove_MovingSegment(object sender, MouseEventArgs e)
        {
            // See how far the first point will move.
            int x = e.X + OffsetX;
            int y = e.Y + OffsetY;
            SnapToGrid(ref x, ref y);

            int dx = x - Pt1[MovingSegment].X;
            int dy = y - Pt1[MovingSegment].Y;

            if (dx == 0 && dy == 0) return;

            // Move the segment to its new location.
            Pt1[MovingSegment] = new Point(x, y);
            Pt2[MovingSegment] = new Point(
                Pt2[MovingSegment].X + dx,
                Pt2[MovingSegment].Y + dy);

            // Redraw.
            picCanvas.Invalidate();
        }

        // Stop moving the segment.
        private void picCanvas_MouseUp_MovingSegment(object sender, MouseEventArgs e)
        {
            // Reset the event handlers.
            picCanvas.MouseMove += picCanvas_MouseMove_NotDown;
            picCanvas.MouseMove -= picCanvas_MouseMove_MovingSegment;
            picCanvas.MouseUp -= picCanvas_MouseUp_MovingSegment;

            // Redraw.
            picCanvas.Invalidate();
        }

        #endregion // Moving End Point

        // See if the mouse is over an end point.
        private bool MouseIsOverEndpoint(Point mouse_pt, out int segment_number, out Point hit_pt)
        {
            for (int i = 0; i < Pt1.Count; i++)
            {
                // Check the starting point.
                if (FindDistanceToPointSquared(mouse_pt, Pt1[i]) < over_dist_squared)
                {
                    // We're over this point.
                    segment_number = i;
                    hit_pt = Pt1[i];
                    return true;
                }

                // Check the end point.
                if (FindDistanceToPointSquared(mouse_pt, Pt2[i]) < over_dist_squared)
                {
                    // We're over this point.
                    segment_number = i;
                    hit_pt = Pt2[i];
                    return true;
                }
            }

            segment_number = -1;
            hit_pt = new Point(-1, -1);
            return false;
        }

        // See if the mouse is over a line segment.
        private bool MouseIsOverSegment(Point mouse_pt, out int segment_number)
        {
            for (int i = 0; i < Pt1.Count; i++)
            {
                // See if we're over the segment.
                PointF closest;
                if (FindDistanceToSegmentSquared(mouse_pt, Pt1[i], Pt2[i], out closest) < over_dist_squared)
                {
                    // We're over this segment.
                    segment_number = i;
                    return true;
                }
            }
            segment_number = -1;
            return false;
        }

        // Calculate the distance squared between two points.
        private int FindDistanceToPointSquared(Point pt1, Point pt2)
        {
            int dx = pt1.X - pt2.X;
            int dy = pt1.Y - pt2.Y;
            return dx * dx + dy * dy;
        }

        // Calculate the distance squared between
        // point pt and the segment p1 --> p2.
        private double FindDistanceToSegmentSquared(Point pt, Point p1, Point p2, out PointF closest)
        {
            float dx = p2.X - p1.X;
            float dy = p2.Y - p1.Y;
            if ((dx == 0) && (dy == 0))
            {
                // It's a point not a line segment.
                closest = p1;
                dx = pt.X - p1.X;
                dy = pt.Y - p1.Y;
                return dx * dx + dy * dy;
            }

            // Calculate the t that minimizes the distance.
            float t = ((pt.X - p1.X) * dx + (pt.Y - p1.Y) * dy) / (dx * dx + dy * dy);

            // See if this represents one of the segment's
            // end points or a point in the middle.
            if (t < 0)
            {
                closest = new PointF(p1.X, p1.Y);
                dx = pt.X - p1.X;
                dy = pt.Y - p1.Y;
            }
            else if (t > 1)
            {
                closest = new PointF(p2.X, p2.Y);
                dx = pt.X - p2.X;
                dy = pt.Y - p2.Y;
            }
            else
            {
                closest = new PointF(p1.X + t * dx, p1.Y + t * dy);
                dx = pt.X - closest.X;
                dy = pt.Y - closest.Y;
            }

            return dx * dx + dy * dy;
        }

        // Draw the lines.
        private void picCanvas_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the segments.
            for (int i = 0; i < Pt1.Count; i++)
            {
                // Draw the segment.
                e.Graphics.DrawLine(Pens.Blue, Pt1[i], Pt2[i]);
            }

            // Draw the end points.
            foreach (Point pt in Pt1)
            {
                Rectangle rect = new Rectangle(pt.X - object_radius, pt.Y - object_radius, 2 * object_radius + 1, 2 * object_radius + 1);
                e.Graphics.FillEllipse(Brushes.White, rect);
                e.Graphics.DrawEllipse(Pens.Black, rect);
            }
            foreach (Point pt in Pt2)
            {
                Rectangle rect = new Rectangle(pt.X - object_radius, pt.Y - object_radius, 2 * object_radius + 1, 2 * object_radius + 1);
                e.Graphics.FillEllipse(Brushes.White, rect);
                e.Graphics.DrawEllipse(Pens.Black, rect);
            }

            // If there's a new segment under constructions, draw it.
            if (IsDrawing)
            {
                e.Graphics.DrawLine(Pens.Red, NewPt1, NewPt2);
            }
        }

        // Give the PictureBox a grid background.
        private void picCanvas_Resize(object sender, EventArgs e)
        {
            MakeBackgroundGrid();
        }
        private void chkSnapToGrid_CheckedChanged(object sender, EventArgs e)
        {
            MakeBackgroundGrid();
        }
        private void MakeBackgroundGrid()
        {
            if (!chkSnapToGrid.Checked)
            {
                picCanvas.BackgroundImage = null;
            }
            else
            {
                Bitmap bm = new Bitmap(picCanvas.ClientSize.Width, picCanvas.ClientSize.Height);
                for (int x = 0; x < picCanvas.ClientSize.Width; x += grid_gap)
                {
                    for (int y = 0; y < picCanvas.ClientSize.Height; y += grid_gap)
                    {
                        bm.SetPixel(x, y, Color.Black);
                    }
                }
                picCanvas.BackgroundImage = bm;
            }
        }
    }
}
