﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Windows.Forms.DataVisualization.Charting;  //for Series

namespace vcs_Chart0
{
    public partial class Form1 : Form
    {
        int draw_mode = 0;  //0:畫chart, 固定邊界 1:畫chart, 變動邊界

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            chart1.Series.Clear();  //每次使用此function前先清除圖表
        }

        private void button0_Click(object sender, EventArgs e)
        {

        }

        private void drawChart(int mode)    //畫Chart
        {
            int i;
            int N = 10;
            Random r = new Random();
            int[] number = new int[N];
            for (i = 0; i < N; i++)
            {
                number[i] = r.Next(350);
            }

            //清除圖表
            chart1.Series.Clear();
            chart1.Titles.Clear();

            Series series1 = new Series("Di0", 500); //初始畫線條(名稱，最大值)
            series1.Color = Color.Blue; //設定線條顏色
            series1.Font = new System.Drawing.Font("新細明體", 10); //設定字型
            series1.ChartType = SeriesChartType.Line; //設定線條種類
            //chart1.ChartAreas[0].AxisY.Enabled= AxisEnabled.False; //隱藏Y 軸標示
            //chart1.ChartAreas[0].AxisY.MajorGrid.Enabled= true;  //隱藏Y軸標線
            series1.IsValueShownAsLabel = true; //是否把數值顯示在線上
            //把值加入X 軸Y 軸
            series1.Points.AddXY("A", number[0]);
            series1.Points.AddXY("B", number[1]);
            series1.Points.AddXY("C", number[2]);
            series1.Points.AddXY("D", number[3]);
            series1.Points.AddXY("E", number[4]);
            series1.Points.AddXY("F", number[5]);
            series1.Points.AddXY("G", number[6]);
            series1.Points.AddXY("H", number[7]);
            series1.Points.AddXY("I", number[8]);
            series1.Points.AddXY("J", number[9]);
            chart1.Series.Add(series1);//將線畫在圖上

            //大小位置
            chart1.Size = new Size(600, 600);
            chart1.Location = new Point(200, 20);

            if (mode == 0)
            {
                //固定邊界
                richTextBox1.Text += "固定邊界\n";
                chart1.ChartAreas[0].AxisY.Minimum = 0;//設定Y軸最小值
                chart1.ChartAreas[0].AxisY.Maximum = 500;//設定Y軸最大值
            }
            else if (mode == 1)
            {
                //變動邊界
                richTextBox1.Text += "變動邊界\n";
                chart1.ChartAreas[0].AxisY.Minimum = number.Min() - 10;//設定Y軸最小值
                chart1.ChartAreas[0].AxisY.Maximum = number.Max() + 10;//設定Y軸最大值
            }
            else
            {
                richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXX\n";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            draw_mode = 0;
            drawChart(draw_mode);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            draw_mode = 1;
            drawChart(draw_mode);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //畫chart, 自定義座標軸刻度標籤

            //清空chart
            chart1.Series.Clear();
            chart1.ChartAreas[0].AxisX.CustomLabels.Clear();

            //不知道如何自動邊界

            Series s1 = new Series();
            Series s2 = new Series();
            Random r = new Random();
            for (int i = 1; i < 13; i++)
            {
                s1.Points.AddXY(i, r.Next(20, 30));
                s2.Points.AddXY(i, r.Next(10, 30));
            }

            chart1.Series.Add(s1);
            chart1.Series.Add(s2);
            chart1.ChartAreas[0].AxisX.MajorGrid.LineColor = Color.Green;
            DateTime t = DateTime.Parse("8:30");
            for (int i = 1; i < 26; i++)
            {
                if (i % 2 == 1)
                {
                    CustomLabel label = new CustomLabel();
                    label.Text = t.ToShortTimeString();
                    label.ToPosition = i;
                    chart1.ChartAreas[0].AxisX.CustomLabels.Add(label);
                    label.GridTicks = GridTickTypes.Gridline;
                    t = t.AddHours(1);
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //Chart繪製直線圖
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

        private void button5_Click(object sender, EventArgs e)
        {
            //Chart繪製長條圖
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

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }




    }
}

