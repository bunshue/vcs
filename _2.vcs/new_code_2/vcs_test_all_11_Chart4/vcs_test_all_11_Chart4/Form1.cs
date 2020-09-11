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
            
            chart1.Titles.Add("直線圖");

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



            chart1.Titles.Add("圓餅圖");
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



            chart1.Titles.Add("長條圖");
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

        private void button4_Click(object sender, EventArgs e)
        {
            int[,] array = new int[,] {
            {1,8,9,7,105,11,50,999,500,1},
            {12,15,11,18,733,5,4,3,2,500} };


            //標題 最大數值
            Series series1 = new Series("第一條線", 1000);
            Series series2 = new Series("第二條線", 1000);

            //設定線條顏色
            series1.Color = Color.Blue;
            series2.Color = Color.Red;

            //設定字型
            series1.Font = new System.Drawing.Font("新細明體", 14);
            series2.Font = new System.Drawing.Font("標楷體", 12);

            //折線圖
            series1.ChartType = SeriesChartType.Line;
            series2.ChartType = SeriesChartType.Line;

            //將數值顯示在線上
            series1.IsValueShownAsLabel = true;
            series2.IsValueShownAsLabel = true;


            //將數值新增至序列
            for (int index = 0; index < 10; index++)
            {
                series1.Points.AddXY(index, array[0, index]);
                series2.Points.AddXY(index, array[1, index]);
            }

            //將序列新增到圖上
            this.chart1.Series.Add(series1);
            this.chart1.Series.Add(series2);

            //標題
            this.chart1.Titles.Add("標題");
        }
    }
}
