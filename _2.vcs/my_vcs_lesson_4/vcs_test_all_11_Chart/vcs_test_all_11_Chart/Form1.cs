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
            plotChart1();

        }

        private void plotChart1() //繪圖
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
            series1.ChartType = SeriesChartType.Line; //設定線條種類
            chart1.ChartAreas[0].AxisY.Minimum = 0;//設定Y軸最小值
            chart1.ChartAreas[0].AxisY.Maximum = 500;//設定Y軸最大值
            //chart1.ChartAreas[0].AxisY.Enabled= AxisEnabled.False; //隱藏Y 軸標示
            //chart1.ChartAreas[0].AxisY.MajorGrid.Enabled= true;  //隱藏Y軸標線
            series1.IsValueShownAsLabel = true; //是否把數值顯示在線上
            //把值加入X 軸Y 軸
            series1.Points.AddXY("A", 200);
            series1.Points.AddXY("B", 100);
            series1.Points.AddXY("C", 100);
            series1.Points.AddXY("D", 30);
            series1.Points.AddXY("E", 300);
            series1.Points.AddXY("F", 70);
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

            Series series = this.chart1.Series.Add("Total Income");
            series.ChartType = SeriesChartType.Spline;
            series.Points.AddXY("September", 100);
            series.Points.AddXY("Obtober", 300);
            series.Points.AddXY("November", 800);
            series.Points.AddXY("December", 200);
            series.Points.AddXY("January", 600);
            series.Points.AddXY("February", 400);

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //clear

        }


        Timer timer;
        double x;
        bool isRunning = false;
        private void button7_Click(object sender, EventArgs e)
        {
            if (isRunning == false)
            {
                isRunning = true;
                timer = new Timer();
                timer.Tick += Timer_Tick;
                timer.Interval = 50;
                timer.Start();
            }
            else
            {
                isRunning = false;
                timer.Stop();

            }
        }

        private void Timer_Tick(object sender, EventArgs e)
        {
            chart1.Series[0].Points.AddXY(x, 3 * Math.Sin(5 * x) + 5 * Math.Cos(3 * x));

            if (chart1.Series[0].Points.Count > 100)
                chart1.Series[0].Points.RemoveAt(0);

            chart1.ChartAreas[0].AxisX.Minimum = chart1.Series[0].Points[0].XValue;
            chart1.ChartAreas[0].AxisX.Maximum = x;

            x += 0.1;
        }


    }
}
