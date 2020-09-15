using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Windows.Forms.DataVisualization.Charting;

namespace vcs_test_all_11_Chart4
{
    public partial class Form1 : Form
    {


        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Series[] _series = new Series[3];
            double[] _y = new double[] { 77, 35, 131 };
            Color[] _colors = new Color[] { Color.Peru, Color.PowderBlue, Color.RosyBrown };
            String[] _users = new String[] { "小王", "小風", "小明" };
            
            int _length = _users.Length;

            for (int index = 0; index < _length; index++)
            {
                _series[index] = new Series(_users[index]);
                _series[index].ChartType = SeriesChartType.Column;
                _series[index].Color = _colors[index];
                _series[index].IsValueShownAsLabel = true;
            }


            for (int index = 0; index < 6; index++)
            {
                _series[0].Points.AddXY(index, _y[0] - index);
                _series[1].Points.AddXY(index, _y[1] - index);
                _series[2].Points.AddXY(index, _y[2] - index);
            }

            foreach (Series s in _series)
                chart1.Series.Add(s);
        
        }

        private void button2_Click(object sender, EventArgs e)
        {
            /*  TBD
            Series _series = new Series();
            double[] _y = new double[] { 77, 35, 131, 55, 77, 66 };
            Color[] _colors = new Color[] { Color.Peru, Color.PowderBlue, Color.RosyBrown, Color.Salmon, Color.Sienna, Color.SlateBlue };
            String[] _users = new String[] { "小王", "小風", "小明", "小姿", "小玉", "小蟹" };



            _series.ChartType = SeriesChartType.Pie;
            _series.IsValueShownAsLabel = true;
            _series.Points.DataBindXY(_users, _y);
            chart1.Series.Add(_series);
            */
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Series[] _series = null;
            double[] _y = new double[] { 100, 57, 93, 26, 77, 88 };
            Color[] _colors = new Color[] { Color.Peru, Color.PowderBlue, Color.RosyBrown, Color.Salmon, Color.Sienna, Color.SlateBlue };
            String[] _users = new String[] { "小王", "小風", "小明", "小姿", "小玉", "小蟹" };

            int _length = _y.Length;
            _series = new Series[_length];
            for (int index = 0; index < _length; index++)
            {
                _series[index] = new Series();
                _series[index].Color = _colors[index];
                _series[index].ChartType = SeriesChartType.Column;
                _series[index].Name = _users[index];
                _series[index].IsValueShownAsLabel = true;
                _series[index].Points.Add(_y[index]);
                chart1.Series.Add(_series[index]);
            }

        }

        private void button5_Click(object sender, EventArgs e)
        {
            chart1.Series.Clear();  //每次使用此function前先清除圖表
        }
    }
}
