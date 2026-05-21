using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Windows.Forms.DataVisualization;
using System.Windows.Forms.DataVisualization.Charting;  // for Series, Chart

//參考： http://wahahastudynote.blogspot.com/2013/04/c-realtime.html
//用 C# 建立 Realtime 圖表 
//加入參考： 參考/加入參考/.NET/System.Windows.Forms.DataVisualization

namespace vcs_Chart2
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
        }

        void show_item_location()
        {
            int W = 700;
            int H = 400;
            int x_st = 10;
            int y_st = 10;
            int dx = W + 10;
            int dy = H + 10;

            chart0.Size = new Size(W, H);
            chart1.Size = new Size(W, H);
            chart0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            chart1.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            richTextBox1.Size = new Size(275, 810);
            richTextBox1.Location = new Point(x_st + dx * 2 + 110, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1840, 870);
            this.Text = "vcs_Chart2";

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
            chart_init(chart0);
            Series series1 = new Series();
            chart0.Series.Add(series1);
            chart0.Series[0].ChartType = SeriesChartType.Point;  // 圖表種類 : 點狀圖
            //chart0.Series[0].ChartType = chartType;
            //series1.ChartType = SeriesChartType.Point;  // 圖表種類 : 點狀圖
            timer0.Enabled = true;

        }

        //------------------------------------------------------------  # 60個

        void draw_chart1()
        {
            //清除圖表
            chart1.Series.Clear();
            chart1.Titles.Clear();

            Series series1 = new Series();
            chart1.Series.Add(series1);
            chart1.Series[0].ChartType = SeriesChartType.Point;
            timer1.Enabled = true;
        }

        //------------------------------------------------------------  # 60個

        //繪圖類別
        public class RealtimeChart
        {
            private Chart chart1 = null;
            private int chartWidth = 640;
            private int chartHeight = 480;
            private string nameAxisX = "X軸標題";
            private string nameAxisY = "Y軸標題";

            public RealtimeChart()
            {
                chart1 = new Chart();

                ChartArea ctArea = new ChartArea();
                Legend legend = new Legend();
                Series series = new Series();

                chart1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(243)))), ((int)(((byte)(223)))), ((int)(((byte)(193)))));
                chart1.BackGradientStyle = System.Windows.Forms.DataVisualization.Charting.GradientStyle.TopBottom;
                chart1.BorderlineColor = System.Drawing.Color.FromArgb(((int)(((byte)(181)))), ((int)(((byte)(64)))), ((int)(((byte)(1)))));
                chart1.BorderlineDashStyle = System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.Solid;
                chart1.BorderlineWidth = 2;
                chart1.BorderSkin.SkinStyle = System.Windows.Forms.DataVisualization.Charting.BorderSkinStyle.Emboss;
                chart1.Location = new System.Drawing.Point(20, 20);
                chart1.Name = "chart1";
                chart1.Size = new System.Drawing.Size(chartWidth, chartHeight);
                chart1.TabIndex = 1;
                chart1.Dock = System.Windows.Forms.DockStyle.None;

                ctArea.Area3DStyle.Inclination = 15;
                ctArea.Area3DStyle.IsClustered = true;
                ctArea.Area3DStyle.IsRightAngleAxes = false;
                ctArea.Area3DStyle.Perspective = 10;
                ctArea.Area3DStyle.Rotation = 10;
                ctArea.Area3DStyle.WallWidth = 0;
                ctArea.AxisX.IsLabelAutoFit = false;
                ctArea.AxisX.LabelStyle.Font = new System.Drawing.Font("Trebuchet MS", 8.25F, System.Drawing.FontStyle.Bold);
                ctArea.AxisX.LineColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
                ctArea.AxisX.MajorGrid.LineColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
                ctArea.AxisX.MinorGrid.LineDashStyle = System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.Dash;
                ctArea.AxisX.Title = nameAxisX;
                ctArea.AxisY.IsLabelAutoFit = false;
                ctArea.AxisY.LabelStyle.Font = new System.Drawing.Font("Trebuchet MS", 8.25F, System.Drawing.FontStyle.Bold);
                ctArea.AxisY.LineColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
                ctArea.AxisY.MajorGrid.LineColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
                ctArea.AxisY.Maximum = 5000D;
                ctArea.AxisY.Minimum = 0D;
                ctArea.AxisY.Title = nameAxisY;
                ctArea.BackColor = System.Drawing.Color.OldLace;
                ctArea.BackGradientStyle = System.Windows.Forms.DataVisualization.Charting.GradientStyle.TopBottom;
                ctArea.BackSecondaryColor = System.Drawing.Color.White;
                ctArea.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
                ctArea.BorderDashStyle = System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.Solid;
                ctArea.Name = "Default";
                ctArea.ShadowColor = System.Drawing.Color.Transparent;
                chart1.ChartAreas.Add(ctArea);

                legend.BackColor = System.Drawing.Color.Transparent;
                legend.Enabled = false;
                legend.Font = new System.Drawing.Font("Trebuchet MS", 8.25F, System.Drawing.FontStyle.Bold);
                legend.IsTextAutoFit = false;
                legend.Name = "Default";
                chart1.Legends.Add(legend);

                series.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(180)))), ((int)(((byte)(26)))), ((int)(((byte)(59)))), ((int)(((byte)(105)))));
                series.ChartArea = "Default";
                series.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
                series.Legend = "Default";
                series.Name = "Default";
                chart1.Series.Add(series);
            }

            public Chart GetChart
            {
                get { return chart1; }
            }
        }

        private int pointIndex = 0;
        Chart chart2 = new RealtimeChart().GetChart;

        bool flag_running = false;

        void draw_chart2()
        {
            chart2 = new RealtimeChart().GetChart;
            pointIndex = 0;
            chart2 = new RealtimeChart().GetChart;
            timer2.Enabled = true;
            this.Controls.Add(chart2);
            chart2.BringToFront();
            chart2.Location = new Point(900, 360);
        }

        //------------------------------------------------------------  # 60個

        private double rad(double d)
        {
            return d * Math.PI / 180.0;
        }

        private double sind(double d)
        {
            return Math.Sin(d * Math.PI / 180.0);
        }

        private double cosd(double d)
        {
            return Math.Cos(d * Math.PI / 180.0);
        }

        //定義Chart大小與外觀
        private const int CHART_WIDTH = 740;
        private const int CHART_HEIGHT = 370;
        private const int AXIS_X_MIN = 0;
        private const int AXIS_X_MAX = 360;
        private const int AXIS_Y_MIN = -200;
        private const int AXIS_Y_MAX = 200;
        private const string TITLE = "三角函數";
        private const string XLABLE = "Degree";
        private const string YLABLE = "Amplitude";

        void chart_init(Chart chart)
        {
            //清除圖表
            chart.Series.Clear();
            chart.Titles.Clear();

            //設定Chart大小與外觀
            //全圖
            chart.Size = new Size(CHART_WIDTH, CHART_HEIGHT);  // 設定chart大小
            chart.Titles.Add(TITLE);

            //X軸
            chart.ChartAreas[0].AxisX.Minimum = AXIS_X_MIN;        //設定X軸最小值
            chart.ChartAreas[0].AxisX.Maximum = AXIS_X_MAX;        //設定X軸最大值
            chart.ChartAreas[0].AxisX.Title = XLABLE;              //設定X軸名稱
            chart.ChartAreas[0].AxisX.TitleForeColor = Color.Blue; //設定X軸名稱的字體顏色
            chart.ChartAreas[0].AxisX.Enabled = AxisEnabled.True;  //顯示 或 隱藏 X 軸標示
            chart.ChartAreas[0].AxisX.MajorGrid.Enabled = true;    //顯示 或 隱藏 X 軸標線
            chart.ChartAreas[0].AxisX.LabelStyle.Font = new Font("Trebuchet MS", 15, FontStyle.Bold);   //設定X軸刻度的字型
            chart.ChartAreas[0].AxisX.LabelStyle.Interval = 60;    //設置X軸刻度間隔的大小
            chart.ChartAreas[0].AxisX.LabelStyle.IntervalType = DateTimeIntervalType.Number;//設置間隔大小的度量單位
            chart.ChartAreas[0].AxisX.LineColor = Color.White;//設置X軸的線條顏色
            chart.ChartAreas[0].AxisX.MajorGrid.Interval = 100;//設置主網格線與次要網格線的間隔
            chart.ChartAreas[0].AxisX.MajorGrid.IntervalType = DateTimeIntervalType.Number;//設置主網格線與次網格線的間隔的度量單位
            chart.ChartAreas[0].AxisX.MajorGrid.LineColor = Color.Snow;//設置網格線的顏色
            chart.ChartAreas[0].AxisX.MajorTickMark.Interval = 20;//設置刻度線的間隔
            chart.ChartAreas[0].AxisX.MajorTickMark.IntervalType = DateTimeIntervalType.Number;//設置刻度線的間隔的度量單位

            //Y軸
            chart.ChartAreas[0].AxisY.Minimum = AXIS_Y_MIN;        //設定Y軸最小值
            chart.ChartAreas[0].AxisY.Maximum = AXIS_Y_MAX;        //設定Y軸最大值
            chart.ChartAreas[0].AxisY.Title = YLABLE;              //設定Y軸名稱
            chart.ChartAreas[0].AxisY.TitleForeColor = Color.Blue; //設定Y軸名稱的字體顏色
            chart.ChartAreas[0].AxisY.Enabled = AxisEnabled.True;  //顯示 或 隱藏 Y 軸標示
            chart.ChartAreas[0].AxisY.MajorGrid.Enabled = true;    //顯示 或 隱藏 Y 軸標線

            chart.ChartAreas[0].AxisY.LabelStyle.Font = new Font("Trebuchet MS", 8.25F, FontStyle.Bold);//設置Y軸左側的提示信息的字體屬性
            chart.ChartAreas[0].AxisY.LineColor = Color.DarkBlue;//設置軸的線條顏色
            chart.ChartAreas[0].AxisY.MajorGrid.LineColor = Color.White;//設置網格線顏色

            //#region 圖表樣式
            chart.BackGradientStyle = System.Windows.Forms.DataVisualization.Charting.GradientStyle.TopBottom;//指定圖表元素的漸變樣式(中心向外，從左到右，從上到下等等)
            chart.BackSecondaryColor = Color.Yellow;//設置背景的輔助顏色
            chart.BorderlineColor = Color.Yellow;//設置圖像邊框的顏色
            chart.BorderlineDashStyle = System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.Solid;//設置圖像邊框線的樣式(實線、虛線、點線)
            chart.BorderlineWidth = 2;//設置圖像的邊框寬度
            chart.BorderSkin.SkinStyle = System.Windows.Forms.DataVisualization.Charting.BorderSkinStyle.Emboss;//設置圖像的邊框外觀樣式
            chart.BackColor = Color.Yellow;//設置圖表的背景顏色
            //#endregion
            chart.Titles[0].Font = new Font("標楷體", 30f);//设置图表标题字体样式和大小
            chart.Legends["Legend1"].Docking = System.Windows.Forms.DataVisualization.Charting.Docking.Right;  //設定圖標顯示停靠的位置
        }

        //------------------------------------------------------------  # 60個

        double x = 0;
        private const int POINTS_IN_AXIS0 = 36;      //製作動畫時X軸要保留的點數
        private void timer0_Tick(object sender, EventArgs e)
        {
            double y;
            y = 110 * sind(x);

            chart0.Series[0].Points.AddXY(x, y);

            if (chart0.Series[0].Points.Count > POINTS_IN_AXIS0)
                chart0.Series[0].Points.RemoveAt(0);

            //製作動畫
            chart0.ChartAreas[0].AxisX.Minimum = chart0.Series[0].Points[0].XValue;
            chart0.ChartAreas[0].AxisX.Maximum = x;

            x += 26;
        }

        //------------------------------------------------------------  # 60個

        double x1 = 0;
        private const int POINTS_IN_AXIS1 = 36;      //製作動畫時X軸要保留的點數
        private void timer1_Tick(object sender, EventArgs e)
        {
            double y;
            y = 110 * sind(x1);

            chart1.Series[0].Points.AddXY(x1, y);

            if (chart1.Series[0].Points.Count > POINTS_IN_AXIS1)
                chart1.Series[0].Points.RemoveAt(0);

            //製作動畫
            chart1.ChartAreas[0].AxisX.Minimum = chart1.Series[0].Points[0].XValue;
            chart1.ChartAreas[0].AxisX.Maximum = x1;

            x1 += 26;
        }

        //------------------------------------------------------------  # 60個

        private void timer2_Tick(object sender, EventArgs e)
        {
            // Define some variables
            int numberOfPointsInChart = 15;
            int numberOfPointsAfterRemoval = 15;

            // Simulate adding new data points
            int x = pointIndex + 1;
            int y = (int)(2500 * Math.Sin(Math.PI * x * 40 / 180) + 2500);

            chart2.Series[0].Points.AddXY(x, y);
            ++pointIndex;

            // Adjust Y & X axis scale
            chart2.ResetAutoValues();
            if (chart2.ChartAreas["Default"].AxisX.Maximum < pointIndex)
            {
                chart2.ChartAreas["Default"].AxisX.Maximum = pointIndex;
            }

            // Keep a constant number of points by removing them from the left
            while (chart2.Series[0].Points.Count > numberOfPointsInChart)
            {
                // Remove data points on the left side
                while (chart2.Series[0].Points.Count > numberOfPointsAfterRemoval)
                {
                    chart2.Series[0].Points.RemoveAt(0);
                }

                // Adjust X axis scale
                chart2.ChartAreas["Default"].AxisX.Minimum = pointIndex - numberOfPointsAfterRemoval;
                chart2.ChartAreas["Default"].AxisX.Maximum = chart2.ChartAreas["Default"].AxisX.Minimum + numberOfPointsInChart;
            }

            // Redraw chart
            chart2.Invalidate();

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



/*
        void save_chart_image_to_drive()
        {
            if (chart1 != null)
            {
                string filename = Application.StartupPath + "\\CHART_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                String filename1 = filename + ".jpg";
                String filename2 = filename + ".bmp";
                String filename3 = filename + ".png";

                try
                {
                    chart1.SaveImage(@filename1, ChartImageFormat.Jpeg);
                    chart1.SaveImage(@filename2, ChartImageFormat.Bmp);
                    chart1.SaveImage(@filename3, ChartImageFormat.Png);

                    richTextBox1.Text += "存檔成功\n";
                    richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename3 + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
            else
            {
                richTextBox1.Text += "無圖可存\n";
            }
        }

*/

            //清除圖表
            //chart1.Series.Clear();  //每次使用此function前先清除圖表
            //chart1.Titles.Clear();
            /*
            chart1.Series[0].Points.Clear();
            chart1.Series[1].Points.Clear();
            chart1.Series[2].Points.Clear();
            */
/*
            //same
            //chart1.Series.Clear();  //每次使用此function前先清除圖表

            chart1.ChartAreas.Clear();
            chart1.Series.Clear();

*/

