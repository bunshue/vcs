using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;     //for GraphicsPath

namespace vcs_Button
{
    public partial class Form1 : Form
    {
        public enum SwitchState
        {
            On,
            Off
        }

        private SwitchState _state;
        public SwitchState State
        {
            get
            {
                return _state;
            }
            set
            {
                if (_state == value)
                    return;
                _state = value;
                AdjustOnOffButton();
            }
        }


        private void AdjustOnOffButton()
        {
            switch (State)
            {
                case SwitchState.On:
                    OnOffButton.Dock = DockStyle.Top;
                    break;
                case SwitchState.Off:
                    OnOffButton.Dock = DockStyle.Bottom;
                    break;
                default:
                    break;
            }
        }


        public void Toggle()
        {
            State = State == SwitchState.On ? SwitchState.Off : SwitchState.On;
        }



        public Form1()
        {
            InitializeComponent();
            State = SwitchState.Off;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //加選
            //this.button1.UseVisualStyleBackColor = true;

            // Shape the button.  Button1
            // Define the points in the polygonal path.
            Point[] pts = {
                new Point( 20,  60),
                new Point(140,  60),
                new Point(140,  20),
                new Point(220, 100),
                new Point(140, 180),
                new Point(140, 140),
                new Point( 20, 140)
            };

            // Make the GraphicsPath.
            GraphicsPath polygon_path = new GraphicsPath(FillMode.Winding);
            polygon_path.AddPolygon(pts);

            // Convert the GraphicsPath into a Region.
            Region polygon_region = new Region(polygon_path);

            // Constrain the button to the region.
            button1.Region = polygon_region;

            // Make the button big enough to hold the whole region.
            button1.SetBounds(
                button1.Location.X,
                button1.Location.Y,
                pts[3].X + 5, pts[4].Y + 5);

        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "向右\n";
        }

        private void OnOffButton_Click(object sender, EventArgs e)
        {
            Toggle();
        }

        private void Form1_SizeChanged(object sender, EventArgs e)
        {
            OnOffButton.Height = this.Height / 2;
        }

    }
}
