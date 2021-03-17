using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_ToolStrip_MenuStrip
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The currently selected drawing parameters.
        private Color DrawingColor = Color.Black;
        private int DrawingThickness = 1;
        private DashStyle DrawingDashStyle = DashStyle.Solid;

        // Select the appropriate color.
        private void ColorTool_Click(object sender, EventArgs e)
        {
            ToolStripMenuItem tool = sender as ToolStripMenuItem;
            toolColor.Image = tool.Image;
            DrawingColor = tool.ForeColor;
            richTextBox1.Text += "你選擇了 DrawingColor:\t" + DrawingColor.ToString() + "\n";
        }

        // Select the line thickness.
        private void ThicknessTool_Click(object sender, EventArgs e)
        {
            ToolStripMenuItem tool = sender as ToolStripMenuItem;
            toolThick.Image = tool.Image;
            DrawingThickness = int.Parse(tool.Text);
            richTextBox1.Text += "你選擇了 DrawingThickness:\t" + DrawingThickness.ToString() + "\n";
        }

        // Select the dash style.
        private void StyleTool_Click(object sender, EventArgs e)
        {
            ToolStripMenuItem tool = sender as ToolStripMenuItem;
            toolStyle.Image = tool.Image;
            switch (tool.Text)
            {
                case "Solid":
                    DrawingDashStyle = DashStyle.Solid;
                    break;
                case "Dash":
                    DrawingDashStyle = DashStyle.Dash;
                    break;
                case "Dot":
                    DrawingDashStyle = DashStyle.Dot;
                    break;
                case "Custom":
                    DrawingDashStyle = DashStyle.Custom;
                    break;
            }
            richTextBox1.Text += "你選擇了 DrawingDashStyle:\t" + DrawingDashStyle.ToString() + "\n";
        }

        private void mnuFileExit_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "File/Exit\n";
            this.Close();
        }

        private void mnuFileNew_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "File/New\n";
        }
    }
}
