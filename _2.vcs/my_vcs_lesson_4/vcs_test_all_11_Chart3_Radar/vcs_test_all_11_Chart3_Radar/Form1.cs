using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Windows.Forms.DataVisualization.Charting;

namespace vcs_test_all_11_Chart3_Radar
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //雷達圖
            chart1.ChartAreas.Clear();
            chart1.Series.Clear();
            chart1.Size = new System.Drawing.Size(500, 500);
            ChartArea area = chart1.ChartAreas.Add("NewArea");
            Series series1 = chart1.Series.Add("雷達資料");
            series1.ChartArea = "NewArea";
            series1.ChartType = SeriesChartType.Radar;
            area.AxisY.LineColor = Color.Red;
            area.AxisY.LineWidth = 1;

            for (int index = 1; index <= 4; index++)
            {
                //第n個點, 數值
                series1.Points.AddXY(index, index * 100);

                //點的名稱
                series1.Points[index - 1].Label = index.ToString();
            }


        }

        private void button2_Click(object sender, EventArgs e)
        {
            chart1.ChartAreas.Clear();
            chart1.Series.Clear();
            chart1.Size = new System.Drawing.Size(500, 500);
            ChartArea area = chart1.ChartAreas.Add("NewArea");
            Series series1 = chart1.Series.Add("雷達資料");
            series1.ChartArea = "NewArea";
            series1.ChartType = SeriesChartType.Radar;
            area.AxisY.LineColor = Color.Red;
            area.AxisY.LineWidth = 1;

            for (Int32 j = 0; j <= 72; j++)
            {
                series1.Points.AddXY(5 * j, 5 + j % 9);
            }

        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            //same
            //chart1.Series.Clear();  //每次使用此function前先清除圖表
            
            chart1.ChartAreas.Clear();
            chart1.Series.Clear();
        }

        private void button3_Click(object sender, EventArgs e)
        {

        }
    }
}
