using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;  //for Series

namespace vcs_test_all_11_Chart
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            plotChart2();

        }

        private void plotChart2() //繪圖
        {
            string[] xValues = { "一月", "二月", "三月", "四月", "五月", "六月", "七月" };
            int[] yValues = { 25, 18, 30, 24, 35, 50, 40 };
            var objSeries = chart1.Series.First();
            objSeries.Points.DataBindXY(xValues, yValues);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            plotChart3();

        }

        private void plotChart3() //繪圖
        {
            //---------------------
            chart1.Series.Clear();  //每次使用此function前先清除圖表
            Series series1 = new Series("Di0", 500); //初始畫線條(名稱，最大值)
            series1.Color = Color.Blue; //設定線條顏色
            series1.Font = new System.Drawing.Font("新細明體", 10); //設定字型
            series1.ChartType = SeriesChartType.Column; //設定線條種類
            //chart1.ChartAreas[0].AxisY.Minimum = 0;//設定Y軸最小值
            //chart1.ChartAreas[0].AxisY.Maximum = 500;//設定Y軸最大值
            //chart1.ChartAreas[0].AxisY.Enabled= AxisEnabled.False; //隱藏Y 軸標示
            //chart1.ChartAreas[0].AxisY.MajorGrid.Enabled= true;  //隱藏Y軸標線
            series1.IsValueShownAsLabel = true; //是否把數值顯示在線上
            //把值加入X 軸Y 軸
            series1.Points.AddXY("John", 200);
            series1.Points.AddXY("Carol", 100);
            series1.Points.AddXY("David", 100);
            series1.Points.AddXY("Tom", 30);
            series1.Points.AddXY("James", 300);
            series1.Points.AddXY("Larry", 70);
            this.chart1.Series.Add(series1);//將線畫在圖上
        }

        private void button4_Click(object sender, EventArgs e)
        {
            plotChart4();

        }

        private void plotChart4() //繪圖
        {
            //Bar example
            this.chart1.Series.Clear();

            // Data arrays
            string[] seriesArray = { "Cat", "Dog", "Bird", "Monkey" };
            int[] pointsArray = { 2, 1, 7, 5 };

            // Set palette
            this.chart1.Palette = ChartColorPalette.EarthTones;

            // Set title
            this.chart1.Titles.Add("Animals");

            // Add series.
            for (int i = 0; i < seriesArray.Length; i++)
            {
                Series series = this.chart1.Series.Add(seriesArray[i]);
                series.Points.Add(pointsArray[i]);
            }

        }

        private void button5_Click(object sender, EventArgs e)
        {
            plotChart5();

        }

        private void plotChart5() //繪圖
        {
            //SplineChartExample
            this.chart1.Series.Clear();

            this.chart1.Titles.Add("Total Income");

            Series series1 = this.chart1.Series.Add("平均高溫​℃");
            Series series2 = this.chart1.Series.Add("平均低溫​℃");
            series1.ChartType = SeriesChartType.Column;
            series1.ChartType = SeriesChartType.Column;
            /*
            series.Points.AddXY("September", 100);
            series.Points.AddXY("Obtober", 300);
            series.Points.AddXY("November", 800);
            series.Points.AddXY("December", 200);
            series.Points.AddXY("January", 600);
            series.Points.AddXY("February", 400);
            */

            string[] month = new string[] { "1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月" };
            double[] temperature_average_high = new double[] { 18.9, 19.4, 21.4, 25.2, 28.6, 31.0, 32.9, 32.6, 31.0, 27.8, 24.9, 21.2 };
            double[] temperature_average_low = new double[] { 12.9, 13.4, 15.2, 18.8, 21.8, 24.4, 25.7, 25.6, 24.1, 21.6, 18.5, 15.0 };
            int i;
            for (i = 0; i < 12; i++)
            {
                series1.Points.AddXY(month[i], temperature_average_high[i]);
                series2.Points.AddXY(month[i], temperature_average_low[i]);



            }

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //clear

        }


    }
}
