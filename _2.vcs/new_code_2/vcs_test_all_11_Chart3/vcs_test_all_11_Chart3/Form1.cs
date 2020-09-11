using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Windows.Forms.DataVisualization.Charting;

namespace vcs_test_all_11_Chart3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            drawChart();
        }

        void drawChart()
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

        private void button2_Click(object sender, EventArgs e)
        {

        }

    }
}
