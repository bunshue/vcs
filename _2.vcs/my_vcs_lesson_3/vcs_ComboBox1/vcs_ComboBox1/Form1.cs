using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ComboBox1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Add colors and pictures to the ComboBoxes.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Colors.
            Color[] colors =
            {
                Color.Red,
                Color.Orange,
                Color.Yellow,
                Color.Green,
                Color.Blue,
                Color.Indigo,
                Color.Purple,
            };
            cboColor.DisplayColorSamples(colors);
            cboColor.SelectedIndex = 0;

            // Faces.
            Image[] images = 
            {
                Properties.Resources.face1,
                Properties.Resources.face2,
                Properties.Resources.face3,
                Properties.Resources.face4,
            };
            cboFace.DisplayImages(images);
            cboFace.SelectedIndex = 0;
            cboFace.DropDownHeight = 200;
        }

    }
}
