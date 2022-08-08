using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Windows.Forms.DataVisualization.Charting;

//C#.Net 透過Chart繪製FastLine      做不出來
//C#.Net 透過Chart繪製圓餅圖        做不出來

namespace vcs_Chart5_FollowFang
{
    public partial class Form1 : Form
    {

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            chart1.Series.Clear();
            chart1.Titles.Clear();

            //C#.Net 透過Chart繪製直線圖

            //x軸只顯示一條，只要將資料都加入到一個序列內即可
            //而x軸顯示多條，則需要使用多個序列存放資料

            Series[] series1 = new Series[3];
            double[] _y = new double[] { 77, 35, 131 };
            Color[] _colors = new Color[] { Color.Peru, Color.PowderBlue, Color.RosyBrown };
            String[] _users = new String[] { "小王", "小風", "小明" };

            chart1.Titles.Add("直線圖");

            int _length = _users.Length;

            for (int index = 0; index < _length; index++)
            {
                series1[index] = new Series(_users[index]);
                series1[index].ChartType = SeriesChartType.Column;
                series1[index].Color = _colors[index];
                series1[index].IsValueShownAsLabel = true;
            }

            for (int index = 0; index < 6; index++)
            {
                series1[0].Points.AddXY(index, _y[0] - index);
                series1[1].Points.AddXY(index, _y[1] - index);
                series1[2].Points.AddXY(index, _y[2] - index);
            }

            foreach (Series s in series1)
            {
                chart1.Series.Add(s);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            chart1.Series.Clear();
            chart1.Titles.Clear();

            //C#.Net 使用Chart繪製長條圖

            Series[] series1 = null;
            double[] _y = new double[] { 100, 57, 93, 26, 77, 88 };
            Color[] _colors = new Color[] { Color.Peru, Color.PowderBlue, Color.RosyBrown, Color.Salmon, Color.Sienna, Color.SlateBlue };
            String[] _users = new String[] { "小王", "小風", "小明", "小姿", "小玉", "小蟹" };

            chart1.Titles.Add("長條圖");
            int _length = _y.Length;
            series1 = new Series[_length];
            for (int index = 0; index < _length; index++)
            {
                series1[index] = new Series();
                series1[index].Color = _colors[index];
                series1[index].ChartType = SeriesChartType.Column;
                series1[index].Name = _users[index];
                series1[index].IsValueShownAsLabel = true;
                series1[index].Points.Add(_y[index]);
                chart1.Series.Add(series1[index]);
            }
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            //same
            //chart1.Series.Clear();  //每次使用此function前先清除圖表

            chart1.ChartAreas.Clear();
            chart1.Series.Clear();
        }

    }
}
