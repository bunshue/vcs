using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ColorDialog2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Initialize the dialog.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Use light custom colors for the background dialog.
            int[] bg_colors = {
                0xFFFFFF, 0xFFC0C0, 0xFFE0C0, 0xFFFFC0, 0xC0FFC0,
                0xC0FFFF, 0xC0C0FF, 0xFFC0FF, 0xE0E0E0, 0xFF8080,
                0xFFC080, 0xFFFF80, 0x80FF80, 0x80FFFF, 0x8080FF,
                0xFF80FF
            };
            dlgBgColor.CustomColors = bg_colors;

            // Use dark custom colors for the foreground dialog.
            int[] fg_colors = {
                0x808080, 0xFF0000, 0xFF8000, 0xFFFF00, 0x00FF00,
                0x00FFFF, 0x0000FF, 0xFF00FF, 0x000000, 0xC00000,
                0x804000, 0xC0C000, 0x008000, 0x00C0C0, 0x0000C0,
                0x800080 };
            dlgFgColor.CustomColors = fg_colors;

            // Make the background dialog open with the custom colors displayed.
            dlgBgColor.FullOpen = true;
            dlgFgColor.FullOpen = false;
        }

        // Let the user select a foreground color.
        private void btnFgColor_Click(object sender, EventArgs e)
        {
            // Initialize the dialog's selected color.
            dlgFgColor.Color = this.ForeColor;

            // Display the dialog and check the result.
            if (dlgFgColor.ShowDialog() == DialogResult.OK)
            {
                this.ForeColor = dlgFgColor.Color;
            }
        }

        // Let the user select a background color.
        private void btnBgColor_Click(object sender, EventArgs e)
        {
            // Initialize the dialog's selected color.
            dlgBgColor.Color = this.BackColor;

            // Display the dialog and check the result.
            if (dlgBgColor.ShowDialog() == DialogResult.OK)
            {
                this.BackColor = dlgBgColor.Color;
                btnBgColor.BackColor = dlgBgColor.Color;
                btnFgColor.BackColor = dlgBgColor.Color;
            }
        }
    }
}
