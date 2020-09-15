using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Windows.Forms.DataVisualization.Charting;  //for Series

namespace vcs_test_all_11_Chart1
{
    public partial class Form1 : Form
    {
        SeriesChartType chartType = SeriesChartType.Point;

        public Form1()
        {
            InitializeComponent();
            comboBox1.SelectedIndex = 0;
            chart1.Series[0].ChartType = chartType;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            chart1.Series.Clear();  //每次使用此function前先清除圖表
            Series series1 = new Series("Sine", 500); //初始畫線條(標題，最大值)
            Series series2 = new Series("Cosine", 500); //初始畫線條(標題，最大值)

            series1.Color = Color.Red; //設定線條顏色
            series2.Color = Color.Green; //設定線條顏色
            series1.Font = new System.Drawing.Font("新細明體", 10); //設定字型
            series2.Font = new System.Drawing.Font("標楷體", 12); //設定字型

            series1.ChartType = chartType; //設定線條種類
            series2.ChartType = chartType; //設定線條種類

            chart1.ChartAreas[0].AxisX.Minimum = 0;//設定X軸最小值
            chart1.ChartAreas[0].AxisX.Maximum = 360;//設定X軸最大值
            chart1.ChartAreas[0].AxisY.Minimum = -200;//設定Y軸最小值
            chart1.ChartAreas[0].AxisY.Maximum = 200;//設定Y軸最大值

            chart1.ChartAreas[0].AxisX.Title = "Degree";
            chart1.ChartAreas[0].AxisY.Title = "Amplitude";

            //將數值顯示在線上
            //series1.IsValueShownAsLabel = true;
            //series2.IsValueShownAsLabel = true;

            //chart1.ChartAreas[0].AxisY.Enabled= AxisEnabled.False; //隱藏Y 軸標示
            //chart1.ChartAreas[0].AxisY.MajorGrid.Enabled= true;  //隱藏Y軸標線
            //series1.IsValueShownAsLabel = true; //是否把數值顯示在線上

            int[] array_x = new int[37];
            int[] array_y1 = new int[37];
            int[] array_y2 = new int[37];

            int i;
            for (i = 0; i <= 360; i+=10)
            {
                array_x[i / 10] = i;
                array_y1[i / 10] = (int)(110 * Math.Sin(Math.PI * i / 180));
                array_y2[i / 10] = (int)(110 * Math.Cos(Math.PI * i / 180));
                //richTextBox1.Text += "len = " + chart1.Series[0].Points.Count.ToString() + "\n";
                //chart1.Series[0].Points.AddXY(array_x[i / 10], array_y1[i / 10]);
                series1.Points.AddXY(array_x[i / 10], array_y1[i / 10]);    //將數值新增至序列
                series2.Points.AddXY(array_x[i / 10], array_y2[i / 10]);    //將數值新增至序列
            }

            chart1.Series.Add(series1);//將序列新增到圖上
            chart1.Series.Add(series2);//將序列新增到圖上

            chart1.Titles.Add("三角函數");      //標題

            /*
            //Point[] pt = new Point[360];    //一維陣列內有360個Point
            */

        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (button2.Text == "動畫 ST")
            {
                button2.Text = "動畫 SP";
                timer1.Enabled = true;
            }
            else
            {
                button2.Text = "動畫 ST";
                timer1.Enabled = false;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            chart1.Series.Clear();  //每次使用此function前先清除圖表
            richTextBox1.Clear();
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            switch (comboBox1.SelectedIndex)
            {
                case 0:
                    chartType = SeriesChartType.Point;
                    richTextBox1.Text += "點狀圖類型\n"; break;
                case 1:
                    chartType = SeriesChartType.FastPoint;
                    richTextBox1.Text += "FastPoint 圖表類型\n"; break;
                case 2:
                    chartType = SeriesChartType.Bubble;
                    richTextBox1.Text += "泡泡圖類型\n"; break;
                case 3:
                    chartType = SeriesChartType.Line;
                    richTextBox1.Text += "折線圖類型\n"; break;
                case 4:
                    chartType = SeriesChartType.Spline;
                    richTextBox1.Text += "曲線圖類型\n"; break;
                case 5:
                    chartType = SeriesChartType.StepLine;
                    richTextBox1.Text += "StepLine 圖表類型\n"; break;
                case 6:
                    chartType = SeriesChartType.FastLine;
                    richTextBox1.Text += "FastLine 圖表類型\n"; break;
                case 7:
                    chartType = SeriesChartType.Bar;
                    richTextBox1.Text += "橫條圖類型\n"; break;
                case 8:
                    chartType = SeriesChartType.StackedBar;
                    richTextBox1.Text += "堆疊橫條圖類型\n"; break;
                case 9:
                    chartType = SeriesChartType.StackedBar100;
                    richTextBox1.Text += "100% 堆疊橫條圖類型\n"; break;
                case 10:
                    chartType = SeriesChartType.Column;
                    richTextBox1.Text += "直條圖類型\n"; break;
                case 11:
                    chartType = SeriesChartType.StackedColumn;
                    richTextBox1.Text += "堆疊直條圖類型\n"; break;
                case 12:
                    chartType = SeriesChartType.StackedColumn100;
                    richTextBox1.Text += "100% 堆疊直條圖類型\n"; break;
                case 13:
                    chartType = SeriesChartType.Area;
                    richTextBox1.Text += "區域圖表類型\n"; break;
                case 14:
                    chartType = SeriesChartType.SplineArea;
                    richTextBox1.Text += "曲線區域圖類型\n"; break;
                case 15:
                    chartType = SeriesChartType.StackedArea;
                    richTextBox1.Text += "堆疊區域圖類型\n"; break;
                case 16:
                    chartType = SeriesChartType.StackedArea100;
                    richTextBox1.Text += "100% 堆疊區域圖類型\n"; break;
                case 17:
                    chartType = SeriesChartType.Pie;
                    richTextBox1.Text += "圓形圖類型\n"; break;
                case 18:
                    chartType = SeriesChartType.Doughnut;
                    richTextBox1.Text += "環圈圖類型\n"; break;
                case 19:
                    chartType = SeriesChartType.Stock;
                    richTextBox1.Text += "股票圖類型\n"; break;
                case 20:
                    chartType = SeriesChartType.Candlestick;
                    richTextBox1.Text += "K 線圖類型\n"; break;
                case 21:
                    chartType = SeriesChartType.Range;
                    richTextBox1.Text += "範圍圖類型\n"; break;
                case 22:
                    chartType = SeriesChartType.SplineRange;
                    richTextBox1.Text += "曲線範圍圖類型\n"; break;
                case 23:
                    chartType = SeriesChartType.RangeBar;
                    richTextBox1.Text += "範圍橫條圖類型\n"; break;
                case 24:
                    chartType = SeriesChartType.RangeColumn;
                    richTextBox1.Text += "範圍直條圖類型\n"; break;
                case 25:
                    chartType = SeriesChartType.Radar;
                    richTextBox1.Text += "雷達圖類型\n"; break;
                case 26:
                    chartType = SeriesChartType.Polar;
                    richTextBox1.Text += "極座標圖類型\n"; break;
                case 27:
                    chartType = SeriesChartType.ErrorBar;
                    richTextBox1.Text += "誤差長條圖類型\n"; break;
                case 28:
                    chartType = SeriesChartType.BoxPlot;
                    richTextBox1.Text += "盒狀圖類型\n"; break;
                case 29:
                    chartType = SeriesChartType.Renko;
                    richTextBox1.Text += "磚形圖類型\n"; break;
                case 30:
                    chartType = SeriesChartType.ThreeLineBreak;
                    richTextBox1.Text += "ThreeLineBreak 圖表類型\n"; break;
                case 31:
                    chartType = SeriesChartType.Kagi;
                    richTextBox1.Text += "Kagi 圖表類型\n"; break;
                case 32:
                    chartType = SeriesChartType.PointAndFigure;
                    richTextBox1.Text += "PointAndFigure 圖表類型\n"; break;
                case 33:
                    chartType = SeriesChartType.Funnel;
                    richTextBox1.Text += "漏斗圖類型\n"; break;
                case 34:
                    chartType = SeriesChartType.Pyramid;
                    richTextBox1.Text += "金字塔圖類型\n"; break;
                default:
                    chartType = SeriesChartType.Point;
                    richTextBox1.Text += "點狀圖類型\n"; break;
            }

        }

        double x = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            double y;
            y = 110 * Math.Sin(Math.PI * x / 180);

            chart1.Series[0].Points.AddXY(x, y);

            if (chart1.Series[0].Points.Count > 30)
                chart1.Series[0].Points.RemoveAt(0);

            chart1.ChartAreas[0].AxisX.Minimum = chart1.Series[0].Points[0].XValue;
            chart1.ChartAreas[0].AxisX.Maximum = x;

            x += 16;


        }

    }
}
