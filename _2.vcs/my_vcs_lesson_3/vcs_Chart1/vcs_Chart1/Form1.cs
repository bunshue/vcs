using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Windows.Forms.DataVisualization.Charting;  //for Series

namespace vcs_Chart1
{
    public partial class Form1 : Form
    {
        SeriesChartType chartType = SeriesChartType.Point;

        //定義Chart大小與外觀
        private const int CHART_WIDTH = 1000;
        private const int CHART_HEIGHT = 500;
        private const int AXIS_X_MIN = 0;
        private const int AXIS_X_MAX = 360;
        private const int AXIS_Y_MIN = -200;
        private const int AXIS_Y_MAX = 200;
        private const string TITLE = "三角函數";
        private const string XLABLE = "Degree";
        private const string YLABLE = "Amplitude";

        //bool flag_show_value = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            show_chart();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200;
            int dy = 30;
            groupBox1.Size = new Size(1200, 220);
            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            x_st = 20;
            y_st = 30;
            radioButton0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            radioButton1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            radioButton2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            radioButton3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            radioButton4.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            radioButton5.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            radioButton6.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            radioButton7.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            radioButton8.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            radioButton9.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            radioButton10.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            radioButton11.Location = new Point(x_st + dx * 5, y_st + dy * 1);
            radioButton12.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            radioButton13.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            radioButton14.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            radioButton15.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            radioButton16.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            radioButton17.Location = new Point(x_st + dx * 5, y_st + dy * 2);
            radioButton18.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            radioButton19.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            radioButton20.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            radioButton21.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            radioButton22.Location = new Point(x_st + dx * 4, y_st + dy * 3);
            radioButton23.Location = new Point(x_st + dx * 5, y_st + dy * 3);
            radioButton24.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            radioButton25.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            radioButton26.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            radioButton27.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            radioButton28.Location = new Point(x_st + dx * 4, y_st + dy * 4);
            radioButton29.Location = new Point(x_st + dx * 5, y_st + dy * 4);
            radioButton30.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            radioButton31.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            radioButton32.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            radioButton33.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            radioButton34.Location = new Point(x_st + dx * 4, y_st + dy * 5);
            radioButton0.Text = "點狀圖";
            radioButton1.Text = "FastPoint 圖表";
            radioButton2.Text = "泡泡圖";
            radioButton3.Text = "折線圖";
            radioButton4.Text = "曲線圖";
            radioButton5.Text = "StepLine 圖表";
            radioButton6.Text = "FastLine 圖表";
            radioButton7.Text = "橫條圖";
            radioButton8.Text = "堆疊橫條圖";
            radioButton9.Text = "100% 堆疊橫條圖";
            radioButton10.Text = "直條圖";
            radioButton11.Text = "堆疊直條圖";
            radioButton12.Text = "100% 堆疊直條圖";
            radioButton13.Text = "區域圖表";
            radioButton14.Text = "曲線區域圖";
            radioButton15.Text = "堆疊區域圖";
            radioButton16.Text = "100% 堆疊區域圖";
            radioButton18.Text = "環圈圖";
            radioButton19.Text = "股票圖";
            radioButton20.Text = "K 線圖";
            radioButton21.Text = "範圍圖";
            radioButton22.Text = "曲線範圍圖";
            radioButton23.Text = "範圍橫條圖";
            radioButton24.Text = "範圍直條圖";
            radioButton25.Text = "雷達圖";
            radioButton26.Text = "極座標圖";
            radioButton27.Text = "誤差長條圖";
            radioButton28.Text = "盒狀圖";
            radioButton29.Text = "磚形圖";
            radioButton30.Text = "ThreeLineBreak 圖表";
            radioButton31.Text = "Kagi 圖表";
            radioButton32.Text = "PointAndFigure 圖表";
            radioButton33.Text = "漏斗圖";
            radioButton34.Text = "金字塔圖";
            radioButton0.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton1.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton2.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton3.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton4.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton5.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton6.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton7.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton8.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton9.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton10.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton11.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton12.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton13.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton14.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton15.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton16.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton17.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton18.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton19.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton20.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton21.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton22.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton23.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton24.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton25.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton26.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton27.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton28.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton29.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton30.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton31.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton32.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton33.CheckedChanged += new EventHandler(radioButton_CheckedChanged);
            radioButton34.CheckedChanged += new EventHandler(radioButton_CheckedChanged);

            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

            chart_type.Size = new Size(1000, 500);
            chart_type.Location = new Point(x_st + dx * 0, y_st + dy * 4 - 50);

            richTextBox1.Size = new Size(300, 500);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 4 - 50);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1400, 790);
            this.Text = "vcs_Chart1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        void radioButton_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton0.Checked == true)
            {
                chartType = SeriesChartType.Point;
                richTextBox1.Text += "點狀圖類型\n";
            }
            else if (radioButton1.Checked == true)
            {
                chartType = SeriesChartType.FastPoint;
                richTextBox1.Text += "FastPoint 圖表類型\n";
            }
            else if (radioButton2.Checked == true)
            {
                chartType = SeriesChartType.Bubble;
                richTextBox1.Text += "泡泡圖類型\n";
            }
            else if (radioButton3.Checked == true)
            {
                chartType = SeriesChartType.Line;
                richTextBox1.Text += "折線圖類型\n";
            }
            else if (radioButton4.Checked == true)
            {
                chartType = SeriesChartType.Spline;
                richTextBox1.Text += "曲線圖類型\n";
            }
            else if (radioButton5.Checked == true)
            {
                chartType = SeriesChartType.StepLine;
                richTextBox1.Text += "StepLine 圖表類型\n";
            }
            else if (radioButton6.Checked == true)
            {
                chartType = SeriesChartType.FastLine;
                richTextBox1.Text += "FastLine 圖表類型\n";
            }
            else if (radioButton7.Checked == true)
            {
                chartType = SeriesChartType.Bar;
                richTextBox1.Text += "橫條圖類型\n";
            }
            else if (radioButton8.Checked == true)
            {
                chartType = SeriesChartType.StackedBar;
                richTextBox1.Text += "堆疊橫條圖類型\n";
            }
            else if (radioButton9.Checked == true)
            {
                chartType = SeriesChartType.StackedBar100;
                richTextBox1.Text += "100% 堆疊橫條圖類型\n";
            }
            else if (radioButton10.Checked == true)
            {
                chartType = SeriesChartType.Column;
                richTextBox1.Text += "直條圖類型\n";
            }
            else if (radioButton11.Checked == true)
            {
                chartType = SeriesChartType.StackedColumn;
                richTextBox1.Text += "堆疊直條圖類型\n";
            }
            else if (radioButton12.Checked == true)
            {
                chartType = SeriesChartType.StackedColumn100;
                richTextBox1.Text += "100% 堆疊直條圖類型\n";
            }
            else if (radioButton13.Checked == true)
            {
                chartType = SeriesChartType.Area;
                richTextBox1.Text += "區域圖表類型\n";
            }
            else if (radioButton14.Checked == true)
            {
                chartType = SeriesChartType.SplineArea;
                richTextBox1.Text += "曲線區域圖類型\n";
            }
            else if (radioButton15.Checked == true)
            {
                chartType = SeriesChartType.StackedArea;
                richTextBox1.Text += "堆疊區域圖類型\n";
            }
            else if (radioButton16.Checked == true)
            {
                chartType = SeriesChartType.StackedArea100;
                richTextBox1.Text += "100% 堆疊區域圖類型\n";
            }
            else if (radioButton17.Checked == true)
            {
                chartType = SeriesChartType.Pie;
                richTextBox1.Text += "圓形圖類型\n";
            }
            else if (radioButton18.Checked == true)
            {
                chartType = SeriesChartType.Doughnut;
                richTextBox1.Text += "環圈圖類型\n";
            }
            else if (radioButton19.Checked == true)
            {
                chartType = SeriesChartType.Stock;
                richTextBox1.Text += "股票圖類型\n";
            }
            else if (radioButton20.Checked == true)
            {
                chartType = SeriesChartType.Candlestick;
                richTextBox1.Text += "K 線圖類型\n";
            }
            else if (radioButton21.Checked == true)
            {
                chartType = SeriesChartType.Range;
                richTextBox1.Text += "範圍圖類型\n";
            }
            else if (radioButton22.Checked == true)
            {
                chartType = SeriesChartType.SplineRange;
                richTextBox1.Text += "曲線範圍圖類型\n";
            }
            else if (radioButton23.Checked == true)
            {
                chartType = SeriesChartType.RangeBar;
                richTextBox1.Text += "範圍橫條圖類型\n";
            }
            else if (radioButton24.Checked == true)
            {
                chartType = SeriesChartType.RangeColumn;
                richTextBox1.Text += "範圍直條圖類型\n";
            }
            else if (radioButton25.Checked == true)
            {
                chartType = SeriesChartType.Radar;
                richTextBox1.Text += "雷達圖類型\n";
            }
            else if (radioButton26.Checked == true)
            {
                chartType = SeriesChartType.Polar;
                richTextBox1.Text += "極座標圖類型\n";
            }
            else if (radioButton27.Checked == true)
            {
                chartType = SeriesChartType.ErrorBar;
                richTextBox1.Text += "誤差長條圖類型\n";
            }
            else if (radioButton28.Checked == true)
            {
                chartType = SeriesChartType.BoxPlot;
                richTextBox1.Text += "盒狀圖類型\n";
            }
            else if (radioButton29.Checked == true)
            {
                chartType = SeriesChartType.Renko;
                richTextBox1.Text += "磚形圖類型\n";
            }
            else if (radioButton30.Checked == true)
            {
                chartType = SeriesChartType.ThreeLineBreak;
                richTextBox1.Text += "ThreeLineBreak 圖表類型\n";
            }
            else if (radioButton31.Checked == true)
            {
                chartType = SeriesChartType.Kagi;
                richTextBox1.Text += "Kagi 圖表類型\n";
            }
            else if (radioButton32.Checked == true)
            {
                chartType = SeriesChartType.PointAndFigure;
                richTextBox1.Text += "PointAndFigure 圖表類型\n";
            }
            else if (radioButton33.Checked == true)
            {
                chartType = SeriesChartType.Funnel;
                richTextBox1.Text += "漏斗圖類型\n";
            }
            else if (radioButton34.Checked == true)
            {
                chartType = SeriesChartType.Pyramid;
                richTextBox1.Text += "金字塔圖類型\n";
            }
            show_chart();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private double sind(double d)
        {
            return Math.Sin(d * Math.PI / 180.0);
        }

        private double cosd(double d)
        {
            return Math.Cos(d * Math.PI / 180.0);
        }

        void show_chart()
        {
            //richTextBox1.Text += "靜畫範例1, 用獨立數組做\n\r";

            //清除圖表
            chart_type.Series.Clear();
            chart_type.Titles.Clear();

            //設定Chart大小與外觀
            //全圖
            chart_type.Size = new Size(CHART_WIDTH, CHART_HEIGHT);      //改變Cahrt大小
            chart_type.Titles.Add(TITLE + " 用獨立數組做");                               //標題

            //X軸
            chart_type.ChartAreas[0].AxisX.Minimum = AXIS_X_MIN;        //設定X軸最小值
            chart_type.ChartAreas[0].AxisX.Maximum = AXIS_X_MAX;        //設定X軸最大值
            chart_type.ChartAreas[0].AxisX.Title = XLABLE;
            chart_type.ChartAreas[0].AxisX.Enabled = AxisEnabled.True;  //顯示 或 隱藏 X 軸標示
            chart_type.ChartAreas[0].AxisX.MajorGrid.Enabled = true;    //顯示 或 隱藏 X 軸標線

            //Y軸
            chart_type.ChartAreas[0].AxisY.Minimum = AXIS_Y_MIN;        //設定Y軸最小值
            chart_type.ChartAreas[0].AxisY.Maximum = AXIS_Y_MAX;        //設定Y軸最大值
            chart_type.ChartAreas[0].AxisY.Title = YLABLE;
            chart_type.ChartAreas[0].AxisY.Enabled = AxisEnabled.True;   //顯示 或 隱藏 Y 軸標示
            chart_type.ChartAreas[0].AxisY.MajorGrid.Enabled = true;    //顯示 或 隱藏 Y 軸標線

            //設定數列大小與外觀
            //series 1
            Series series1 = new Series("sin", 500); //初始畫線條(標題，最大值)
            series1.Color = Color.Red; //設定線條顏色
            series1.Font = new System.Drawing.Font("新細明體", 10); //設定字型
            series1.ChartType = chartType; //設定線條種類
            series1.MarkerSize = 5;     //圖標大小
            series1.IsValueShownAsLabel = false;   //將數值顯示在線上

            //series 2
            Series series2 = new Series("cos", 500); //初始畫線條(標題，最大值)
            series2.Color = Color.Green; //設定線條顏色
            series2.Font = new System.Drawing.Font("標楷體", 12); //設定字型

            series2.ChartType = chartType; //設定線條種類
            series2.MarkerSize = 5;     //圖標大小
            series2.IsValueShownAsLabel = false;   //將數值顯示在線上

            //series 3
            Series series3 = new Series("sin + cos", 500); //初始畫線條(標題，最大值)
            series3.Color = Color.Blue; //設定線條顏色
            series3.Font = new System.Drawing.Font("標楷體", 12); //設定字型
            series3.ChartType = chartType; //設定線條種類
            series3.MarkerSize = 5;     //圖標大小
            series3.IsValueShownAsLabel = false;   //將數值顯示在線上

            int[] array_x = new int[37];
            int[] array_y1 = new int[37];
            int[] array_y2 = new int[37];
            int[] array_y3 = new int[37];

            int i;
            for (i = 0; i <= 360; i += 10)
            {
                array_x[i / 10] = i;
                array_y1[i / 10] = (int)(110 * sind(i));
                array_y2[i / 10] = (int)(110 * cosd(i));
                array_y3[i / 10] = (int)(110 * sind(i) + 110 * cosd(i));
                //richTextBox1.Text += "len = " + chart_type.Series[0].Points.Count.ToString() + "\n";
                //chart_type.Series[0].Points.AddXY(array_x[i / 10], array_y1[i / 10]);
                series1.Points.AddXY(array_x[i / 10], array_y1[i / 10]);    //將數值1新增至序列1
                series2.Points.AddXY(array_x[i / 10], array_y2[i / 10]);    //將數值2新增至序列2
                series3.Points.AddXY(array_x[i / 10], array_y3[i / 10]);    //將數值3新增至序列3
            }

            //經過chart_type.Series.Clear()後, chart_type.Series.Count = 0
            chart_type.Series.Add(series1);//將序列1新增到chart上
            //此時, chart_type.Series.Count = 1
            chart_type.Series.Add(series2);//將序列2新增到chart上
            //此時, chart_type.Series.Count = 2
            chart_type.Series.Add(series3);//將序列3新增到chart上
            //此時, chart_type.Series.Count = 3
            /*
            if (cb_show_data.Checked == true)
            {
                richTextBox1.Text += "顯示資料\n";
                int count = series1.Points.Count;
                richTextBox1.Text += "共有 " + count.ToString() + " 筆資料\n";
                for (i = 0; i < count; i++)
                {
                    richTextBox1.Text += "x[" + i.ToString() + "] = " + series1.Points[i].XValue.ToString() + "\t";
                    richTextBox1.Text += "sin[" + i.ToString() + "] = " + series1.Points[i].YValues[0].ToString() + "\t";
                    richTextBox1.Text += "cos[" + i.ToString() + "] = " + series2.Points[i].YValues[0].ToString() + "\t";
                    richTextBox1.Text += "sin[" + i.ToString() + "] + " + "cos[" + i.ToString() + "] = " + series3.Points[i].YValues[0].ToString() + "\n";
                }
            }
            */
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

*/


