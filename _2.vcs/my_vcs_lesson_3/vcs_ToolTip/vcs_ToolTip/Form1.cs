using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ToolTip
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            toolTip1.InitialDelay = 300;
            toolTip1.ReshowDelay = 300;
            toolTip1.ShowAlways = true;
            toolTip1.SetToolTip(this.button1, "button1 的提示");
            toolTip1.SetToolTip(this.button2, "button2 的提示");
            toolTip1.SetToolTip(this.button3, "button3 的提示");

            toolTip1.InitialDelay = 300;
            toolTip1.ReshowDelay = 300;
            toolTip1.ShowAlways = true;
            toolTip1.SetToolTip(this.richTextBox1, "richTextBox1 的提示");

            toolTip1.InitialDelay = 300;
            toolTip1.ReshowDelay = 300;
            toolTip1.ShowAlways = true;
            toolTip1.SetToolTip(this.pictureBox1, "pictureBox1 的提示");
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            this.Text = e.Location.ToString();
            SetTooltip(e.Location);
        }

        private void SetTooltip(PointF point)
        {
            if (pictureBox1.Image == null)
            {
                //return;
            }

            string mesg = "";

            mesg = "目前座標 " + point.ToString();

            if (toolTip1.GetToolTip(pictureBox1) != mesg)
            {
                toolTip1.SetToolTip(pictureBox1, mesg);
            }
            pictureBox1.Refresh();
        }

    }
}
