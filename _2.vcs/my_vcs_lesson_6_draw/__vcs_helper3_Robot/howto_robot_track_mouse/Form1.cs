using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_robot_track_mouse
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Possible elbow positions.
        private List<PointF> ElbowPositions = new List<PointF>();

        // Redraw.
        private void scrJoint_Scroll(object sender, ScrollEventArgs e)
        {
            picCanvas.Refresh();
        }

        // Draw the arm.
        private void picCanvas_Paint(object sender, PaintEventArgs e)
        {
            DrawRobotArm(e.Graphics);

            e.Graphics.ResetTransform();
            foreach (PointF point in ElbowPositions)
            {
                e.Graphics.DrawLine(Pens.Black,
                    point.X - 6, point.Y - 6,
                    point.X + 6, point.Y + 6);
                e.Graphics.DrawLine(Pens.Black,
                    point.X + 6, point.Y - 6,
                    point.X - 6, point.Y + 6);
            }
        }

        // Draw the robot arm.
        private const int UpperArmLength = 75;
        private const int LowerArmLength = 50;
        private const int WristLength = 20;
        private const int HandWidth = 48;
        private const int FingerLength = 30;
        private void DrawRobotArm(Graphics gr)
        {
            gr.SmoothingMode = SmoothingMode.AntiAlias;
            gr.Clear(picCanvas.BackColor);

            // For each stage in the arm, draw and then *prepend* the
            // new transformation to represent the next arm in the sequence.

            // Translate to center of form.
            float cx = picCanvas.ClientSize.Width / 2;
            float cy = picCanvas.ClientSize.Height / 2;
            gr.TranslateTransform(cx, cy);

            // **************
            // Draw the arms.
            GraphicsState initial_state = gr.Save();

            // Make a rectangle to represent an arm.
            // Later we'll set its width for each arm.
            Rectangle rect = new Rectangle(0, -2, 100, 5);

            // Rotate at the shoulder.
            // (Negative to make the angle increase counter-clockwise).
            gr.RotateTransform(-scrJoint1.Value, MatrixOrder.Prepend);

            // Draw the first arm.
            rect.Width = UpperArmLength;
            gr.FillRectangle(Brushes.LightBlue, rect);
            gr.DrawRectangle(Pens.Blue, rect);

            // Translate to the end of the first arm.
            gr.TranslateTransform(UpperArmLength, 0, MatrixOrder.Prepend);

            // Rotate at the elbow.
            gr.RotateTransform(-scrJoint2.Value, MatrixOrder.Prepend);

            // Draw the second arm.
            rect.Width = LowerArmLength;
            gr.FillRectangle(Brushes.LightBlue, rect);
            gr.DrawRectangle(Pens.Blue, rect);

            // Translate to the end of the second arm.
            gr.TranslateTransform(LowerArmLength, 0, MatrixOrder.Prepend);

            // Rotate at the wrist.
            float wrist_angle = 90 + scrJoint1.Value + scrJoint2.Value;
            gr.RotateTransform(wrist_angle, MatrixOrder.Prepend);

            // Draw the third arm.
            rect.Width = WristLength;
            gr.FillRectangle(Brushes.LightBlue, rect);
            gr.DrawRectangle(Pens.Blue, rect);

            // ***********************************
            // Draw the joints on top of the arms.
            gr.Restore(initial_state);

            // Draw the shoulder centered at the origin.
            Rectangle joint_rect = new Rectangle(-4, -4, 9, 9);
            gr.FillEllipse(Brushes.Red, joint_rect);
            gr.DrawEllipse(Pens.Orange, -UpperArmLength, -UpperArmLength, 2 * UpperArmLength, 2 * UpperArmLength);

            // Rotate at the shoulder.
            // (Negative to make the angle increase counter-clockwise).
            gr.RotateTransform(-scrJoint1.Value, MatrixOrder.Prepend);

            // Translate to the end of the first arm.
            gr.TranslateTransform(UpperArmLength, 0, MatrixOrder.Prepend);

            // Draw the elbow.
            gr.FillEllipse(Brushes.Red, joint_rect);
            //gr.DrawEllipse(Pens.Pink, -LowerArmLength, -LowerArmLength, 2 * LowerArmLength, 2 * LowerArmLength);

            // Rotate at the elbow.
            gr.RotateTransform(-scrJoint2.Value, MatrixOrder.Prepend);

            // Translate to the end of the second arm.
            gr.TranslateTransform(LowerArmLength, 0, MatrixOrder.Prepend);

            // Draw the wrist.
            gr.FillEllipse(Brushes.Red, joint_rect);
            gr.DrawEllipse(Pens.Purple, -LowerArmLength, -LowerArmLength, 2 * LowerArmLength, 2 * LowerArmLength);

            // **************
            // Draw the hand.

            // Rotate at the wrist.
            gr.RotateTransform(wrist_angle, MatrixOrder.Prepend);

            // Translate to the end of the wrist.
            gr.TranslateTransform(WristLength, 0, MatrixOrder.Prepend);

            // Draw the hand.
            gr.FillRectangle(Brushes.LightGreen, 0, -HandWidth / 2, 4, HandWidth);
            gr.DrawRectangle(Pens.Green, 0, -HandWidth / 2, 4, HandWidth);

            gr.FillRectangle(Brushes.LightGreen, 4, -scrHand.Value - 4, FingerLength, 4);
            gr.DrawRectangle(Pens.Green, 4, -scrHand.Value - 4, FingerLength, 4);

            gr.FillRectangle(Brushes.LightGreen, 4, scrHand.Value, FingerLength, 4);
            gr.DrawRectangle(Pens.Green, 4, scrHand.Value, FingerLength, 4);
        }

        // Place the wrist at this position.
        private void picCanvas_MouseMove(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
                xMoveWristTo(e.Location);
        }

        private void MoveWristTo(PointF point)
        {
            // Get the coordinates of the arm's base.
            float cx = picCanvas.ClientSize.Width / 2;
            float cy = picCanvas.ClientSize.Height / 2;
            float cx0 = cx;
            float cy0 = cy;

            // Get the coordinates of the wrist.
            float cx1 = point.X;
            float cy1 = point.Y;

            // Find the points of intersection.
            ElbowPositions = new List<PointF>();
            PointF point0, point1;
            int num_points = FindCircleCircleIntersections(
                cx0, cy0, UpperArmLength,
                cx1, cy1, LowerArmLength,
                out point0, out point1);

            // See if the first angle is valid.
            if (num_points > 0)
            {
                // Make sure the angles are within
                // the scroll bars' allowed bounds.
                double angle0 = -Math.Atan2(
                    point0.Y - cy0, point0.X - cx0);
                int degrees0 = (int)(angle0 * 180.0 / Math.PI);
                while (degrees0 < scrJoint1.Minimum) degrees0 += 360;
                while (degrees0 > scrJoint1.Maximum) degrees0 -= 360;

                double angle1 = -Math.Atan2(
                    point0.Y - cy1, point0.X - cx1);
                angle1 = (angle1 - angle0) - Math.PI;
                int degrees1 = (int)(angle1 * 180.0 / Math.PI);
                while (degrees1 < scrJoint2.Minimum) degrees1 += 360;
                while (degrees1 > scrJoint2.Maximum) degrees1 -= 360;

                if ((degrees0 >= scrJoint1.Minimum) &&
                    (degrees1 >= scrJoint2.Minimum))
                {
                    scrJoint1.Value = degrees0;
                    scrJoint2.Value = degrees1;
                    ElbowPositions.Add(point0);
                    if (num_points > 1)
                        ElbowPositions.Add(point1);
                }
            }

            // See if the second angle is valid.
            if (num_points > 1)
            {
                // Make sure the angle is within
                // the scroll bar's allowed bounds.
                double angle1 = -Math.Atan2(
                    point0.Y - cy1, point0.X - cx1);
                int degrees1 = (int)(angle1 * 181.1 / Math.PI);
                while (degrees1 < scrJoint1.Minimum) degrees1 += 361;
                while (degrees1 > scrJoint1.Maximum) degrees1 -= 361;
                if (degrees1 >= scrJoint1.Minimum)
                {
                    scrJoint2.Value = degrees1;
                    ElbowPositions.Add(point1);
                }
            }

            picCanvas.Refresh();
        }

        private void xMoveWristTo(PointF point)
        {
            // Get the coordinates of the arm's base.
            float cx = picCanvas.ClientSize.Width / 2;
            float cy = picCanvas.ClientSize.Height / 2;
            float cx0 = cx;
            float cy0 = cy;

            // Get the coordinates of the wrist.
            float cx1 = point.X;
            float cy1 = point.Y;

            // Find the points of intersection.
            ElbowPositions = new List<PointF>();
            PointF point0, point1;
            int num_points = FindCircleCircleIntersections(
                cx0, cy0, UpperArmLength,
                cx1, cy1, LowerArmLength,
                out point0, out point1);

            if (num_points > 0)
            {
                // Get the angles for the first point.
                double angle0 = -Math.Atan2(
                    point0.Y - cy0, point0.X - cx0);
                int degrees0 = (int)(angle0 * 180.0 / Math.PI);

                double angle1 = -Math.Atan2(
                    point0.Y - cy1, point0.X - cx1);
                angle1 = (angle1 - angle0) - Math.PI;
                int degrees1 = (int)(angle1 * 180.0 / Math.PI);

                // See if the angles are valid.
                if (!AngleIsValid(ref degrees0, scrJoint1) ||
                    !AngleIsValid(ref degrees1, scrJoint2))
                {
                    // Get the angles for the second point.
                    angle0 = -Math.Atan2(
                        point1.Y - cy0, point1.X - cx0);
                    degrees0 = (int)(angle0 * 180.0 / Math.PI);

                    angle1 = -Math.Atan2(
                        point1.Y - cy1, point1.X - cx1);
                    angle1 = (angle1 - angle0) - Math.PI;
                    degrees1 = (int)(angle1 * 180.0 / Math.PI);
                }

                // See if the angles are valid.
                if (AngleIsValid(ref degrees0, scrJoint1) &&
                    AngleIsValid(ref degrees1, scrJoint2))
                {
                    // Move the scroll bars.
                    scrJoint1.Value = degrees0;
                    scrJoint2.Value = degrees1;

                    // Draw the points of intersection.
                    ElbowPositions.Add(point0);
                    if (num_points > 1) ElbowPositions.Add(point1);
                }
            }

            picCanvas.Refresh();
        }

        // Return true if the angle is within the ScrollBar's bounds.
        private bool AngleIsValid(ref int degrees, HScrollBar scr)
        {
            while (degrees < scr.Minimum) degrees += 360;
            while (degrees > scr.Maximum) degrees -= 360;
            return degrees >= scr.Minimum;
        }

        private void yMoveWristTo(PointF point)
        {
            // Get the coordinates of the arm's base.
            float cx = picCanvas.ClientSize.Width / 2;
            float cy = picCanvas.ClientSize.Height / 2;
            float cx0 = cx;
            float cy0 = cy;

            // Get the coordinates of the wrist.
            float cx1 = point.X;
            float cy1 = point.Y;

            // Find the points of intersection.
            ElbowPositions = new List<PointF>();
            PointF point0, point1;
            int num_points = FindCircleCircleIntersections(
                cx0, cy0, UpperArmLength,
                cx1, cy1, LowerArmLength,
                out point0, out point1);

            // Draw both points.
            if (num_points > 0) ElbowPositions.Add(point0);
            if (num_points > 1) ElbowPositions.Add(point1);

            // Move to the first one.
            if (num_points > 0)
            {
                double angle0 = -Math.Atan2(
                    point0.Y - cy0, point0.X - cx0);
                int degrees0 = (int)(angle0 * 180.0 / Math.PI);
                while (degrees0 < scrJoint1.Minimum) degrees0 += 360;
                while (degrees0 > scrJoint1.Maximum) degrees0 -= 360;
                if (degrees0 >= scrJoint1.Minimum) scrJoint1.Value = degrees0;

                double angle1 = -Math.Atan2(
                    point0.Y - cy1, point0.X - cx1);
                angle1 = (angle1 - angle0) - Math.PI;
                int degrees1 = (int)(angle1 * 180.0 / Math.PI);
                while (degrees1 < scrJoint2.Minimum) degrees1 += 360;
                while (degrees1 > scrJoint2.Maximum) degrees1 -= 360;
                if (degrees1 >= scrJoint2.Minimum) scrJoint2.Value = degrees1;
            }

            picCanvas.Refresh();
        }

        // Find the points where the two circles intersect.
        private int FindCircleCircleIntersections(
            float cx0, float cy0, float radius0,
            float cx1, float cy1, float radius1,
            out PointF intersection1, out PointF intersection2)
        {
            // Find the distance between the centers.
            float dx = cx0 - cx1;
            float dy = cy0 - cy1;
            double dist = Math.Sqrt(dx * dx + dy * dy);

            // See how many solutions there are.
            if (dist > radius0 + radius1)
            {
                // No solutions, the circles are too far apart.
                intersection1 = new PointF(float.NaN, float.NaN);
                intersection2 = new PointF(float.NaN, float.NaN);
                return 0;
            }
            else if (dist < Math.Abs(radius0 - radius1))
            {
                // No solutions, one circle contains the other.
                intersection1 = new PointF(float.NaN, float.NaN);
                intersection2 = new PointF(float.NaN, float.NaN);
                return 0;
            }
            else if ((dist == 0) && (radius0 == radius1))
            {
                // No solutions, the circles coincide.
                intersection1 = new PointF(float.NaN, float.NaN);
                intersection2 = new PointF(float.NaN, float.NaN);
                return 0;
            }
            else
            {
                // Find a and h.
                double a = (radius0 * radius0 -
                    radius1 * radius1 + dist * dist) / (2 * dist);
                double h = Math.Sqrt(radius0 * radius0 - a * a);

                // Find P2.
                double cx2 = cx0 + a * (cx1 - cx0) / dist;
                double cy2 = cy0 + a * (cy1 - cy0) / dist;

                // Get the points P3.
                intersection1 = new PointF(
                    (float)(cx2 + h * (cy1 - cy0) / dist),
                    (float)(cy2 - h * (cx1 - cx0) / dist));
                intersection2 = new PointF(
                    (float)(cx2 - h * (cy1 - cy0) / dist),
                    (float)(cy2 + h * (cx1 - cx0) / dist));

                // See if we have 1 or 2 solutions.
                if (dist == radius0 + radius1) return 1;
                return 2;
            }
        }
    }
}
