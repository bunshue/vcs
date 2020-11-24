using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace howto_stddev_extension
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Make some data.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Make the values.
            Random rand = new Random();
            const int num_values = 100;

            int rr = 0;
            //Array version.
            int[] values = new int[num_values];
            for (int i = 0; i < num_values; i++)
            {
                rr = rand.Next(1, 7) + rand.Next(1, 7);
                values[i] = rr;
                richTextBox1.Text += rr.ToString() + "  ";
            }
            richTextBox1.Text += "\n";

            // Display statistics.
            richTextBox1.Text += "Average\t" + values.Average().ToString("0.00") + "\n";
            richTextBox1.Text += "StdDev(true)\t" + values.StdDev(true).ToString("0.00") + "\n";
            richTextBox1.Text += "StdDev(false)\t" + values.StdDev(false).ToString("0.00") + "\n";

            // Make a simple histogram.
            Label[] labels = { lbl2, lbl3, lbl4, lbl5, lbl6, lbl7, lbl8, lbl9, lbl10, lbl11, lbl12 };
            int bottom = lbl2.Bottom;
            foreach (Label lbl in labels) lbl.Height = 1;
            const int pixel_scale = 10;
            for (int i = 0; i < num_values; i++)
            {
                int index = values[i] - 2;
                labels[index].Height += pixel_scale;
            }
            foreach (Label lbl in labels)
            {
                lbl.Top = bottom - lbl.Height;
            }
        }
    }
}
