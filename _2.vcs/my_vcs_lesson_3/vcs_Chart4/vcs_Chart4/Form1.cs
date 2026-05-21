using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Windows.Forms.DataVisualization;
using System.Windows.Forms.DataVisualization.Charting;

namespace vcs_Chart4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            draw_chart0();
            draw_chart1();
            draw_chart2();
            draw_chart3();
            draw_chart4();
            draw_chart5();
        }

        void show_item_location()
        {
            int W = 500;
            int H = 400;
            int x_st = 10;
            int y_st = 10;
            int dx = W + 10;
            int dy = H + 10;

            chart0.Size = new Size(W, H);
            chart1.Size = new Size(W, H);
            chart2.Size = new Size(W, H);
            chart3.Size = new Size(W, H);
            chart4.Size = new Size(W, H);
            chart5.Size = new Size(W, H);
            chart0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            chart1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            chart2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            chart3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            chart4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            chart5.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            richTextBox1.Size = new Size(275, 810);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1840, 870);
            this.Text = "vcs_Chart4";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        void draw_chart0()
        {
            // 長條圖, 自定義座標軸刻度標籤

            // 清除圖表
            chart0.Series.Clear();
            chart0.Titles.Clear();
            chart0.ChartAreas[0].AxisX.CustomLabels.Clear();

            //不知道如何自動邊界

            // 設定數列1
            Series s1 = new Series();
            // 設定數列2
            Series s2 = new Series();

            Random r = new Random();
            for (int i = 1; i < 13; i++)
            {
                s1.Points.AddXY(i, r.Next(20, 30));
                s2.Points.AddXY(i, r.Next(10, 30));
            }

            // 將數列新增到chart上
            chart0.Series.Add(s1);
            chart0.Series.Add(s2);

            chart0.ChartAreas[0].AxisX.MajorGrid.LineColor = Color.Green;
            DateTime dt = DateTime.Parse("8:30");
            for (int i = 1; i < 26; i++)
            {
                if (i % 2 == 1)
                {
                    CustomLabel label = new CustomLabel();
                    label.Text = dt.ToShortTimeString();
                    label.ToPosition = i;
                    chart0.ChartAreas[0].AxisX.CustomLabels.Add(label);
                    label.GridTicks = GridTickTypes.Gridline;
                    dt = dt.AddHours(1);
                }
            }
        }

        //------------------------------------------------------------  # 60個

        void draw_chart1()
        {
            //雷達圖1

            //清除圖表
            chart1.Series.Clear();
            chart1.Titles.Clear();
            chart1.ChartAreas.Clear();

            chart1.Titles.Add("雷達圖1");
            chart1.Size = new Size(400, 400);

            ChartArea area = chart1.ChartAreas.Add("NewArea");

            // 設定數列1 的 大小與外觀
            Series series1 = chart1.Series.Add("雷達資料");
            series1.ChartArea = "NewArea";
            series1.ChartType = SeriesChartType.Radar;  // 圖表種類 : 雷達圖
            area.AxisY.LineColor = Color.Red;
            area.AxisY.LineWidth = 1;

            Random r = new Random();
            for (int index = 1; index <= 4; index++)
            {
                //第n個點, 數值
                series1.Points.AddXY(index, r.Next(10) * 50);

                //點的名稱
                series1.Points[index - 1].Label = index.ToString();
            }
        }

        //------------------------------------------------------------  # 60個

        void draw_chart2()
        {
            //雷達圖2

            //清除圖表
            chart2.Series.Clear();
            chart2.Titles.Clear();
            chart2.ChartAreas.Clear();

            chart2.Titles.Add("雷達圖2");
            chart2.Size = new Size(400, 400);

            ChartArea area = chart2.ChartAreas.Add("NewArea");

            // 設定數列1 的 大小與外觀
            Series series1 = chart2.Series.Add("雷達資料");
            series1.ChartArea = "NewArea";
            series1.ChartType = SeriesChartType.Radar;  // 圖表種類 : 雷達圖
            area.AxisY.LineColor = Color.Red;
            area.AxisY.LineWidth = 1;

            for (Int32 j = 0; j <= 72; j++)
            {
                series1.Points.AddXY(5 * j, 5 + j % 9);
            }
        }

        //------------------------------------------------------------  # 60個

        void draw_chart3()
        {
            int draw_mode = 1;  //0:畫chart, 固定邊界 1:畫chart, 變動邊界

            //折線圖, 固定邊界 / 變動邊界

            drawChart(draw_mode);
        }

        private void drawChart(int mode)    //畫Chart
        {
            //清除圖表
            chart3.Series.Clear();
            chart3.Titles.Clear();

            //------------------------------------------------------------  # 60個

            int N = 10;
            Random r = new Random();
            int[] number = new int[N];
            for (int i = 0; i < N; i++)
            {
                number[i] = r.Next(350);
            }

            // 設定數列1 的 大小與外觀
            Series series1 = new Series("Di0", 500); //初始畫線條(名稱，最大值)
            series1.Color = Color.Blue; //設定線條顏色
            series1.Font = new Font("新細明體", 10); //設定字型
            series1.ChartType = SeriesChartType.Line;  // 圖表種類 : 折線圖
            //chart3.ChartAreas[0].AxisY.Enabled= AxisEnabled.False; //隱藏Y 軸標示
            //chart3.ChartAreas[0].AxisY.MajorGrid.Enabled= true;  //隱藏Y軸標線
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
            series1.LegendText = "折線圖";  // 圖例文字

            // 將數列新增到chart上
            chart3.Series.Add(series1);

            if (mode == 0)
            {
                //固定邊界
                richTextBox1.Text += "固定邊界\n";
                chart3.ChartAreas[0].AxisY.Minimum = 0;//設定Y軸最小值
                chart3.ChartAreas[0].AxisY.Maximum = 500;//設定Y軸最大值
            }
            else if (mode == 1)
            {
                //變動邊界
                richTextBox1.Text += "變動邊界\n";
                chart3.ChartAreas[0].AxisY.Minimum = number.Min() - 10;//設定Y軸最小值
                chart3.ChartAreas[0].AxisY.Maximum = number.Max() + 10;//設定Y軸最大值
            }
            else
            {
                richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXX\n";
            }
        }

        //------------------------------------------------------------  # 60個

        void draw_chart4()
        {
            string[] xValues = { "一月", "二月", "三月", "四月", "五月", "六月", "七月" };
            int[] yValues = { 25, 18, 30, 24, 35, 50, 40 };
            var objSeries = chart4.Series.First();
            chart4.Series[0].ChartType = SeriesChartType.Point;
            objSeries.Points.DataBindXY(xValues, yValues);

            //設定邊界
            //chart4.ChartAreas[0].AxisX.Minimum = 0;//設定Y軸最小值
            //chart4.ChartAreas[0].AxisX.Maximum = 8;//設定Y軸最大值
            chart4.ChartAreas[0].AxisY.Minimum = 0;//設定Y軸最小值
            chart4.ChartAreas[0].AxisY.Maximum = 60;//設定Y軸最大值
        }

        //------------------------------------------------------------  # 60個

        void draw_chart5()
        {
            //清除圖表
            chart5.Series.Clear();
            chart5.Titles.Clear();

            // 設定數列1 的 大小與外觀
            Series series1 = new Series("Di0", 500); //初始畫線條(名稱，最大值)
            series1.Color = Color.Blue; //設定線條顏色
            series1.Font = new System.Drawing.Font("新細明體", 10); //設定字型
            series1.ChartType = SeriesChartType.Column; //設定線條種類
            //chart5.ChartAreas[0].AxisY.Minimum = 0;//設定Y軸最小值
            //chart5.ChartAreas[0].AxisY.Maximum = 500;//設定Y軸最大值
            //chart5.ChartAreas[0].AxisY.Enabled= AxisEnabled.False; //隱藏Y 軸標示
            //chart5.ChartAreas[0].AxisY.MajorGrid.Enabled= true;  //隱藏Y軸標線
            series1.IsValueShownAsLabel = true; //是否把數值顯示在線上
            //把值加入X 軸Y 軸
            series1.Points.AddXY("John", 200);
            series1.Points.AddXY("Carol", 100);
            series1.Points.AddXY("David", 100);
            series1.Points.AddXY("Tom", 30);
            series1.Points.AddXY("James", 300);
            series1.Points.AddXY("Larry", 70);

            int count = series1.Points.Count;
            richTextBox1.Text += "共有 " + count.ToString() + " 筆資料\n";
            for (int i = 0; i < count; i++)
            {
                richTextBox1.Text += "X[" + i.ToString() + "] = " + series1.Points[i].XValue.ToString() + "\t";
                richTextBox1.Text += "Y[" + i.ToString() + "] = " + series1.Points[i].YValues[0].ToString() + "\n";
            }

            //設定邊界
            chart5.ChartAreas[0].AxisX.Minimum = 0;//設定Y軸最小值
            chart5.ChartAreas[0].AxisX.Maximum = 8;//設定Y軸最大值
            chart5.ChartAreas[0].AxisY.Minimum = 0;//設定Y軸最小值
            chart5.ChartAreas[0].AxisY.Maximum = 400;//設定Y軸最大值

            // 將數列新增到chart上
            chart5.Series.Add(series1);
        }

        //------------------------------------------------------------  # 60個
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

*/


