using System;
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

            chart1.Series.Clear();  //每次使用此function前先清除圖表
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
    }
}

