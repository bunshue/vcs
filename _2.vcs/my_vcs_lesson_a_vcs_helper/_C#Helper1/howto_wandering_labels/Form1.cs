using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace howto_wandering_labels
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The Label controls we will animate and their properties.
        private List<Label> AnimateLabels = new List<Label>();
        private List<int> AnimateStartXs = new List<int>();
        private List<int> AnimateStartYs = new List<int>();
        private List<float> AnimateDxs = new List<float>();
        private List<float> AnimateDys = new List<float>();
        private List<float> AnimateXs = new List<float>();
        private List<float> AnimateYs = new List<float>();
        private List<int> AnimateTotalTicks = new List<int>();
        private List<int> AnimateTicksToGo = new List<int>();

        // Make lists of the controls to move.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Move down 20 pixels in 1 second.
            StoreAnimationInfo(lblTitle1, 0, 20, 500);

            // Move right 40 pixels in 2 seconds.
            StoreAnimationInfo(lblTitle2, 40, 0, 1000);

            // Move left 40 pixels in 2 seconds.
            StoreAnimationInfo(lblTitle3, -40, 0, 1000);

            // Move up 20 pixels in 1 second.
            StoreAnimationInfo(lblTitle4, 0, -20, 500);
        }

        // Store information to move a label.
        private void StoreAnimationInfo(Label lbl, float dx, float dy, float milliseconds)
        {
            // Calculate the number of times the Timer will tick.
            int ticks = (int)(milliseconds / tmrMoveLabels.Interval);

            // Add the values.
            AnimateLabels.Add(lbl);
            AnimateStartXs.Add((int)(lbl.Location.X - dx));
            AnimateStartYs.Add((int)(lbl.Location.Y - dy));
            AnimateDxs.Add(dx / ticks);
            AnimateDys.Add(dy / ticks);
            AnimateTotalTicks.Add(ticks);
        }

        // Move the labels to the start positions and start animating them.
        private void btnAnimate_Click(object sender, EventArgs e)
        {
            btnAnimate.Enabled = false;
            AnimateTicksToGo = new List<int>();
            AnimateXs = new List<float>();
            AnimateYs = new List<float>();

            for (int i = 0; i < AnimateLabels.Count; i++)
            {
                AnimateXs.Add(AnimateStartXs[i]);
                AnimateYs.Add(AnimateStartYs[i]);
                AnimateLabels[i].Location =
                    new Point((int)AnimateXs[i], (int)AnimateYs[i]);
                AnimateLabels[i].Visible = true;
                AnimateTicksToGo.Add(AnimateTotalTicks[i]);
            }

            tmrMoveLabels.Enabled = true;
        }

        // Move the labels.
        private void tmrMoveLabels_Tick(object sender, EventArgs e)
        {
            bool done_moving = true;
            DateTime now = DateTime.Now;
            for (int i = 0; i < AnimateLabels.Count; i++)
            {
                if (AnimateTicksToGo[i]-- > 0)
                {
                    done_moving = false;
                    AnimateXs[i] += AnimateDxs[i];
                    AnimateYs[i] += AnimateDys[i];
                    AnimateLabels[i].Location =
                        new Point((int)AnimateXs[i], (int)AnimateYs[i]);
                }
            }

            // If all labels are done moving, disable the Timer.
            if (done_moving)
            {
                tmrMoveLabels.Enabled = false;
                tmrHideLabels.Enabled = true;
            }
        }

        // Hide the controls.
        private void tmrHideLabels_Tick(object sender, EventArgs e)
        {
            foreach (Label lbl in AnimateLabels) lbl.Visible = false;
            tmrHideLabels.Enabled = false;
            btnAnimate.Enabled = true;
        }
    }
}
