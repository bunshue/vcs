using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Windows.Forms.DataVisualization.Charting;

namespace vcs_test_all_11_Chart5
{
    public partial class Form1 : Form
    {
        private Series[] _series = new Series[] { new Series(), new Series() };

        public Form1()
        {
            InitializeComponent();
            foreach (Series s in _series)
            {
                s.ChartType = SeriesChartType.FastLine;
                chart1.Series.Add(s);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            foreach (Series s in _series)
            {
                s.ChartType = SeriesChartType.FastLine;
                chart1.Series.Add(s);
            }

            int i;
            int j;

            for (i = 0; i < 300; i++)
            {
                _series[0].Points.AddXY(i, i * 2.3);
                _series[1].Points.AddXY(i, i * 5);
            }

         

        }

        double x = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            /*
            x++;
            int y = DateTime.Now.Millisecond;
            //richTextBox1.Text += DateTime.Now.Millisecond.ToString() + " ";
            _series[0].Points.AddXY(x, y);

            //double aaa = chart1.Series[0].Points[0].XValue;
            //richTextBox1.Text += aaa.ToString() + " ";

            richTextBox1.Text += chart1.Series[0].Points.Count.ToString() + " ";
            if (chart1.Series[0].Points.Count > 20)
                chart1.Series[0].Points.RemoveAt(0);

            //chart1.ChartAreas[0].AxisX.Minimum = chart1.Series[0].Points[1].XValue;
            //chart1.ChartAreas[0].AxisX.Minimum = 0;
            //chart1.ChartAreas[0].AxisX.Minimum = chart1.Series[0].Points[0].XValue;
            //chart1.ChartAreas[0].AxisX.Maximum = x;
            */

            double y;
            //y = 3 * Math.Sin(5 * x) + 5 * Math.Cos(3 * x);
            y = 110 * Math.Sin(Math.PI * x / 180);
            chart1.Series[0].Points.AddXY(x, y);

            if (chart1.Series[0].Points.Count > 100)
                chart1.Series[0].Points.RemoveAt(0);

            chart1.ChartAreas[0].AxisX.Minimum = chart1.Series[0].Points[0].XValue;
            chart1.ChartAreas[0].AxisX.Maximum = x;

            x += 0.1;

            /*
            chart1.Series[0].Points.AddXY(x, 3 * Math.Sin(5 * x) + 5 * Math.Cos(3 * x));

            if (chart1.Series[0].Points.Count > 100)
            {
                richTextBox1.Text += "R";
                chart1.Series[0].Points.RemoveAt(0);
            }

            chart1.ChartAreas[0].AxisX.Minimum = chart1.Series[0].Points[0].XValue;
            chart1.ChartAreas[0].AxisX.Maximum = x;

            x += 0.1;
            */
        }
    }
}
