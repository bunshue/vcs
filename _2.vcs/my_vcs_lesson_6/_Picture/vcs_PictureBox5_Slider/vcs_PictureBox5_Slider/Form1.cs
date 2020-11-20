using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureBox5_Slider
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "";

        }

        // The current value.
        private float SliderValue = 0.3f;

        // The minimum and maximum allowed values.
        private const float MinimumValue = 0.0f;
        private const float MaximumValue = 1.0f;

        // Move the needle to this position.
        private bool MouseIsDown = false;
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            MouseIsDown = true;
            SetValue(XtoValue(e.X));


        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (!MouseIsDown) return;
            SetValue(XtoValue(e.X));

        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            MouseIsDown = false;
            toolTip1.Hide(this);

            // Take action here if desired.
            label1.Text = SliderValue.ToString("0.00");

        }

        // Draw the needle.
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            // Calculate the needle's X coordinate.
            float x = ValueToX(SliderValue);

            if (rb1.Checked == true)
            {
                // Draw it.
                using (Pen pen = new Pen(Color.Blue, 2))
                {
                    e.Graphics.DrawLine(pen, x, 0, x, pictureBox1.ClientSize.Height);
                }
            }
            else
            {
                int y = (int)(pictureBox1.ClientSize.Height * 0.25);
                int hgt = pictureBox1.ClientSize.Height - 2 * y;

                // Draw it.
                e.Graphics.FillRectangle(Brushes.Blue, 0, y, x, hgt);
                using (Pen pen = new Pen(Color.Blue, 3))
                {
                    e.Graphics.DrawLine(pen, x, 0, x, pictureBox1.ClientSize.Height);
                }
            }
        }

        // Convert an X coordinate to a value.
        private float XtoValue(int x)
        {
            return MinimumValue + (MaximumValue - MinimumValue) *
                x / (float)(pictureBox1.ClientSize.Width - 1);
        }

        // Convert value to an X coordinate.
        private float ValueToX(float value)
        {
            return (pictureBox1.ClientSize.Width - 1) *
                (value - MinimumValue) / (float)(MaximumValue - MinimumValue);
        }

        // Set the slider's value. If the value has changed,
        // display the value tooltip.
        private void SetValue(float value)
        {
            // Make sure the new value is within bounds.
            if (value < MinimumValue) value = MinimumValue;
            if (value > MaximumValue) value = MaximumValue;

            // See if the value has changed.
            if (SliderValue == value) return;

            // Save the new value.
            SliderValue = value;

            // Redraw to show the new value.
            pictureBox1.Refresh();

            // Display the value tooltip.
            int tip_x = pictureBox1.Left + (int)ValueToX(SliderValue);
            int tip_y = pictureBox1.Top;
            toolTip1.Show(SliderValue.ToString("0.00"), this, tip_x, tip_y, 3000);

            // Take action here if desired.
            label1.Text = SliderValue.ToString("0.00");
        }



    }
}
