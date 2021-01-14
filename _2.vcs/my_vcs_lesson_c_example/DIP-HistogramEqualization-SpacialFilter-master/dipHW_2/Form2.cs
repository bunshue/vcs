using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace dipHW_2
{
    public partial class Form2 : Form
    {
        int[] data;
        void Draw_Hist(int[] data) {
            Graphics g = panel1.CreateGraphics();
           
            Pen pen = new Pen(Brushes.Black, 1);
            // get the max value
            int max = 0;
            for (int i = 0; i < 256; ++i) {
                max = Math.Max(max, data[i]);
            }
            // draw
            for (int i = 0; i < 256; ++i) {
                g.DrawLine(pen, i, 260, i, 260 - 256 * data[i] / max);
            }
        }
        public Form2(int[] histData)
        {   InitializeComponent();
            data = histData;
           /* for (int i = 0; i < 256; ++i)
            {
                Console.WriteLine(i + ":" + data[i]);
            }*/
        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {
            Draw_Hist(data);
        }
    }
}
