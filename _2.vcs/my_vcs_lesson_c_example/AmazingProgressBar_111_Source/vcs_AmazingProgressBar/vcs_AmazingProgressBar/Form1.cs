using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using GAW;

namespace vcs_AmazingProgressBar
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            AmazingProgressBar amaze = new AmazingProgressBar();
            amaze.Location = new System.Drawing.Point(20, 100);
            amaze.Size = new System.Drawing.Size(200, 50);
            this.Controls.Add(amaze);

            amaze.Style = ProgressBarStyle.Continuous;
            amaze.MazeStyle = AmazingProgressBar.MazeStyleType.SingleLeft;
            amaze.RowCount = 4;

            // Assumes "AmazingProgressBar amaze" already declared and initialized
            //amaze.Gradient = GradientType.Rows;
            amaze.Gradient = AmazingProgressBar.GradientType.Rows;
            amaze.GradientStartColor = Color.LightBlue;
            amaze.GradientEndColor = Color.DarkBlue;

            amaze.BorderSize = 2;
            amaze.BorderColor = Color.LightGreen;
            amaze.BorderGradient = false;
            amaze.BorderRoundCorners = true;

            amaze.BackColor = Color.White;

        }

    }
}
