using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MyProgressBar3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        ToolTip toolTip1 = new ToolTip();

        // The current value.
        private int CurrentValue = 234;

        // The minimum and maximum allowed values.
        private const int MinimumValue = 0;
        private const int MaximumValue = 1000;

        // Move the needle to this position.
        private bool flag_pbx_mouse_down = false;
        private void pbx_MouseDown(object sender, MouseEventArgs e)
        {
            flag_pbx_mouse_down = true;
            SetValue(sender, XtoValue(sender, e.X));
        }

        private void pbx_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_pbx_mouse_down == false)
            {
                return;
            }
            SetValue(sender, XtoValue(sender, e.X));
        }

        private void pbx_MouseUp(object sender, MouseEventArgs e)
        {
            flag_pbx_mouse_down = false;
            toolTip1.Hide(this);
        }

        // Draw the needle.
        private void pbx_Paint(object sender, PaintEventArgs e)
        {
            // Calculate the needle's X coordinate.
            int x = ValueToX(sender, CurrentValue);

            //case 1
            using (Pen pen = new Pen(Color.Blue, 2))
            {
                e.Graphics.DrawLine(pen, x, 0, x, ((PictureBox)sender).ClientSize.Height);
            }

            /*
            //case 2
            int y = (int)(pbx.ClientSize.Height * 0.25);
            int hgt = pbx.ClientSize.Height - 2 * y;

            // Draw it.
            e.Graphics.FillRectangle(Brushes.Blue, 0, y, x, hgt);
            using (Pen pen = new Pen(Color.Blue, 3))
            {
                e.Graphics.DrawLine(pen, x, 0, x, pbx.ClientSize.Height);
            }
            */
        }

        // Convert an X coordinate to a value.
        private int XtoValue(object sender, int x)
        {
            return MinimumValue + (MaximumValue - MinimumValue) * x / (int)(((PictureBox)sender).ClientSize.Width - 1);
        }

        // Convert value to an X coordinate.
        private int ValueToX(object sender, int value)
        {
            return (((PictureBox)sender).ClientSize.Width - 1) * (value - MinimumValue) / (int)(MaximumValue - MinimumValue);
        }

        // Set the slider's value. If the value has changed,
        // display the value tooltip.
        private void SetValue(object sender, int value)
        {
            // Make sure the new value is within bounds.
            if (value < MinimumValue)
            {
                value = MinimumValue;
            }
            if (value > MaximumValue)
            {
                value = MaximumValue;
            }

            // See if the value has changed.
            if (CurrentValue == value)
            {
                return;
            }

            // Save the new value.
            CurrentValue = value;

            // Redraw to show the new value.
            ((PictureBox)sender).Refresh();

            // Display the value tooltip.
            int tip_x = ((PictureBox)sender).Left + (int)ValueToX(sender, CurrentValue);
            int tip_y = ((PictureBox)sender).Top;
            toolTip1.Show(CurrentValue.ToString(), this, tip_x, tip_y, 3000);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            PictureBox pbx = new PictureBox();
            //pbx.Parent = this;  //相當於 this.Controls.Add(pbx)
            //pbx.SizeMode = PictureBoxSizeMode.Zoom;
            //pbx.Image = bitmap1;
            pbx.BackColor = Color.Pink;
            pbx.Size = new Size(600, 100);
            pbx.Location = new Point(50, 50);

            pbx.MouseDown += new MouseEventHandler(pbx_MouseDown);
            pbx.MouseMove += new MouseEventHandler(pbx_MouseMove);
            pbx.MouseUp += new MouseEventHandler(pbx_MouseUp);
            pbx.Paint += new PaintEventHandler(pbx_Paint);

            this.Controls.Add(pbx);

        }
    }
}


