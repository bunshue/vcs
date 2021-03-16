using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_FormSendData
{
    public partial class Form4 : Form
    {
        int[] data;

        public Form4(int[] histData)
        {
            InitializeComponent();

            data = histData;
        }

        void Draw_Hist(int[] data)
        {
            Graphics g = panel1.CreateGraphics();

            Pen pen = new Pen(Brushes.Black, 1);

            int N = data.Length;

            // get the max value
            int max = 0;
            for (int i = 0; i < N; i++)
            {
                max = Math.Max(max, data[i]);
            }
            // draw
            for (int i = 0; i < N; i += 2)
            {
                g.DrawLine(pen, i, 260, i, 260 - 256 * data[i] / max);
            }
        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {
            Draw_Hist(data);
        }
    }
}