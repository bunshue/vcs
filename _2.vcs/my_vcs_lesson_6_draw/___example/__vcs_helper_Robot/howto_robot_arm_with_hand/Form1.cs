using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_robot_arm_with_hand
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Redraw.
        private void scrJoint_Scroll(object sender, ScrollEventArgs e)
        {
            picCanvas.Refresh();
        }

        // Draw the arm.
        private void picCanvas_Paint(object sender, PaintEventArgs e)
        {
            DrawRobotArm(e.Graphics);
        }

        // Draw the robot arm.
        private void DrawRobotArm(Graphics gr)
        {
            const int UpperArmLength = 75;
            const int LowerArmLength = 50;
            const int WristLength = 20;
            const int HandWidth = 48;
            const int FingerLength = 30;

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
            gr.RotateTransform(-scrJoint3.Value, MatrixOrder.Prepend);

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

            // Rotate at the shoulder.
            // (Negative to make the angle increase counter-clockwise).
            gr.RotateTransform(-scrJoint1.Value, MatrixOrder.Prepend);

            // Translate to the end of the first arm.
            gr.TranslateTransform(UpperArmLength, 0, MatrixOrder.Prepend);

            // Draw the elbow.
            gr.FillEllipse(Brushes.Red, joint_rect);

            // Rotate at the elbow.
            gr.RotateTransform(-scrJoint2.Value, MatrixOrder.Prepend);

            // Translate to the end of the second arm.
            gr.TranslateTransform(LowerArmLength, 0, MatrixOrder.Prepend);

            // Draw the wrist.
            gr.FillEllipse(Brushes.Red, joint_rect);

            // **************
            // Draw the hand.

            // Rotate at the wrist.
            gr.RotateTransform(-scrJoint3.Value, MatrixOrder.Prepend);
            
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
    }
}
