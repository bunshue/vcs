using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ComboBox3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Make a font for the item text.
            Font font = new Font("Times New Roman", 14);

            // Make image and text data.
            ImageAndText[] planets =
            {
                new ImageAndText(Properties.Resources.Mercury,
                    "Name: Mercury" + '\n' +
                    "Distance: 0.31-0.47" + '\n' +
                    "Distance: 0.31-0.47" + '\n' +
                    "Mass: 0.06" + '\n' +
                    "Diameter: 0.382" + '\n' +
                    "Year: 0.24" + '\n' +
                    "Day: 58.64",
                    font),
                new ImageAndText(Properties.Resources.Venus,
                    "Name: Venus" + '\n' +
                    "Distance: 0.72" + '\n' +
                    "Mass: 0.82" + '\n' +
                    "Diameter: 0.949" + '\n' +
                    "Year: 0.62" + '\n' +
                    "Day: -243.02",
                    font),
                new ImageAndText(Properties.Resources.Earth,
                    "Name: Earth" + '\n' +
                    "Distance: 1" + '\n' +
                    "Mass: 1" + '\n' +
                    "Diameter: 1" + '\n' +
                    "Year: 1" + '\n' +
                    "Day: 1",
                    font),
                new ImageAndText(Properties.Resources.Mars,
                    "Name: Mars" + '\n' +
                    "Distance: 1.52" + '\n' +
                    "Mass: 0.11" + '\n' +
                    "Diameter: 0.532" + '\n' +
                    "Year: 1.88" + '\n' +
                    "Day: 1.03",
                    font),
                new ImageAndText(Properties.Resources.Jupiter,
                    "Name: Jupiter" + '\n' +
                    "Distance: 5.2" + '\n' +
                    "Mass: 317.8" + '\n' +
                    "Diameter: 11.209" + '\n' +
                    "Year: 11.86" + '\n' +
                    "Day: 0.41",
                    font),
                new ImageAndText(Properties.Resources.Saturn,
                    "Name: Saturn" + '\n' +
                    "Distance: 9.54" + '\n' +
                    "Mass: 95.2" + '\n' +
                    "Diameter: 9.449" + '\n' +
                    "Year: 29.46" + '\n' +
                    "Day: 0.43",
                    font),
                new ImageAndText(Properties.Resources.Uranus,
                    "Name: Uranus" + '\n' +
                    "Distance: 19.22" + '\n' +
                    "Mass: 14.6" + '\n' +
                    "Diameter: 4.007" + '\n' +
                    "Year: 84.01" + '\n' +
                    "Day: −0.72",
                    font),
                new ImageAndText(Properties.Resources.Neptune,
                    "Name: Neptune" + '\n' +
                    "Distance: 30.06" + '\n' +
                    "Mass: 17.2" + '\n' +
                    "Diameter: 3.883" + '\n' +
                    "Year: 164.8" + '\n' +
                    "Day: 0.67",
                    font),
            };

            comboBox1.DisplayImagesAndText(planets);
            comboBox1.SelectedIndex = 0;
        }
    }
}
