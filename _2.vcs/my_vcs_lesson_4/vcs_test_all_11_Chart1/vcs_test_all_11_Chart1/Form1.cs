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

        bool flag_show_value = false;

        public Form1()
        {
            InitializeComponent();
            show_item_location();
            comboBox1.SelectedIndex = 0;
            chart1.Size = new Size(CHART_WIDTH, CHART_HEIGHT);       //改變Cahrt大小
            chart1.Series[0].ChartType = chartType;
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 110;
            dy = 50;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);


            bt_start.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            bt_save.Location = new Point(x_st + dx * 0, y_st + dy * 11);
            bt_clear.Location = new Point(x_st + dx * 0, y_st + dy * 12);
        
        
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

        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "靜畫範例1, 用獨立數組做\n\r";
                 
            chart1.Series.Clear();  //每次使用此function前先清除圖表

            //設定Chart大小與外觀
            //全圖
            chart1.Size = new Size(CHART_WIDTH, CHART_HEIGHT);      //改變Cahrt大小
            chart1.Titles.Add(TITLE + " 用獨立數組做");                               //標題

            //X軸
            chart1.ChartAreas[0].AxisX.Minimum = AXIS_X_MIN;        //設定X軸最小值
            chart1.ChartAreas[0].AxisX.Maximum = AXIS_X_MAX;        //設定X軸最大值
            chart1.ChartAreas[0].AxisX.Title = XLABLE;
            chart1.ChartAreas[0].AxisX.Enabled = AxisEnabled.True;  //顯示 或 隱藏 X 軸標示
            chart1.ChartAreas[0].AxisX.MajorGrid.Enabled = true;    //顯示 或 隱藏 X 軸標線

            //Y軸
            chart1.ChartAreas[0].AxisY.Minimum = AXIS_Y_MIN;        //設定Y軸最小值
            chart1.ChartAreas[0].AxisY.Maximum = AXIS_Y_MAX;        //設定Y軸最大值
            chart1.ChartAreas[0].AxisY.Title = YLABLE;
            chart1.ChartAreas[0].AxisY.Enabled = AxisEnabled.True;   //顯示 或 隱藏 Y 軸標示
            chart1.ChartAreas[0].AxisY.MajorGrid.Enabled = true;    //顯示 或 隱藏 Y 軸標線

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
                //richTextBox1.Text += "len = " + chart1.Series[0].Points.Count.ToString() + "\n";
                //chart1.Series[0].Points.AddXY(array_x[i / 10], array_y1[i / 10]);
                series1.Points.AddXY(array_x[i / 10], array_y1[i / 10]);    //將數值1新增至序列1
                series2.Points.AddXY(array_x[i / 10], array_y2[i / 10]);    //將數值2新增至序列2
                series3.Points.AddXY(array_x[i / 10], array_y3[i / 10]);    //將數值3新增至序列3
            }

            //經過chart1.Series.Clear()後, chart1.Series.Count = 0
            chart1.Series.Add(series1);//將序列1新增到chart上
            //此時, chart1.Series.Count = 1
            chart1.Series.Add(series2);//將序列2新增到chart上
            //此時, chart1.Series.Count = 2
            chart1.Series.Add(series3);//將序列3新增到chart上
            //此時, chart1.Series.Count = 3

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
        }

        private void button1_Click(object sender, EventArgs e)
        {
            plotChart1();
        }

        private void plotChart1() //繪圖
        {
            string[] xValues = { "一月", "二月", "三月", "四月", "五月", "六月", "七月" };
            int[] yValues = { 25, 18, 30, 24, 35, 50, 40 };
            var objSeries = chart1.Series.First();
            objSeries.Points.DataBindXY(xValues, yValues);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            plotChart2();
        }

        private void plotChart2() //繪圖
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

        private void button3_Click(object sender, EventArgs e)
        {
            plotChart3();
        }

        private void plotChart3() //繪圖
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

        private void button4_Click(object sender, EventArgs e)
        {
            plotChart4();
        }

        private void plotChart4() //繪圖
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

        private void button5_Click(object sender, EventArgs e)
        {
            //C#.Net 透過Chart繪製直線圖

            chart1.Titles.Add("直線圖");
            Series[] series = new Series[3];       //預先建立3個數組   應該是不太好
            double[] _y = new double[] { 77, 35, 131 };
            Color[] colors = new Color[] { Color.Peru, Color.PowderBlue, Color.RosyBrown };
            String[] users = new String[] { "小王", "小風", "小明" };

            int len = users.Length;

            for (int index = 0; index < len; index++)
            {
                series[index] = new Series(users[index]);
                series[index].ChartType = SeriesChartType.Column;
                series[index].Color = colors[index];
                series[index].IsValueShownAsLabel = true;
            }

            for (int index = 0; index < 6; index++)
            {
                series[0].Points.AddXY(index, _y[0] - index);
                series[1].Points.AddXY(index, _y[1] - index);
                series[2].Points.AddXY(index, _y[2] - index);
            }

            foreach (Series s in series)
                chart1.Series.Add(s);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //C#.Net 透過Chart繪製圓餅圖

            /*  TBD
            Series _series = new Series();
            double[] _y = new double[] { 77, 35, 131, 55, 77, 66 };
            Color[] _colors = new Color[] { Color.Peru, Color.PowderBlue, Color.RosyBrown, Color.Salmon, Color.Sienna, Color.SlateBlue };
            String[] _users = new String[] { "小王", "小風", "小明", "小姿", "小玉", "小蟹" };



            _series.ChartType = SeriesChartType.Pie;
            _series.IsValueShownAsLabel = true;
            _series.Points.DataBindXY(_users, _y);
            chart1.Series.Add(_series);
            */
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //C#.Net 使用Chart繪製長條圖

            Series[] _series = null;
            double[] _y = new double[] { 100, 57, 93, 26, 77, 88 };
            Color[] _colors = new Color[] { Color.Peru, Color.PowderBlue, Color.RosyBrown, Color.Salmon, Color.Sienna, Color.SlateBlue };
            String[] _users = new String[] { "小王", "小風", "小明", "小姿", "小玉", "小蟹" };

            int _length = _y.Length;
            _series = new Series[_length];
            for (int index = 0; index < _length; index++)
            {
                _series[index] = new Series();
                _series[index].Color = _colors[index];
                _series[index].ChartType = SeriesChartType.Column;
                _series[index].Name = _users[index];
                _series[index].IsValueShownAsLabel = true;
                _series[index].Points.Add(_y[index]);
                chart1.Series.Add(_series[index]);
            }

        }

        double x = 0;
        private const int POINTS_IN_AXIS = 36;      //製作動畫時X軸要保留的點數
        private void timer1_Tick(object sender, EventArgs e)
        {
            double y;
            y = 110 * sind(x);

            chart1.Series[0].Points.AddXY(x, y);

            if (chart1.Series[0].Points.Count > POINTS_IN_AXIS)
                chart1.Series[0].Points.RemoveAt(0);

            //製作動畫
            chart1.ChartAreas[0].AxisX.Minimum = chart1.Series[0].Points[0].XValue;
            chart1.ChartAreas[0].AxisX.Maximum = x;

            x += 26;
        }

        private void bt_start_Click(object sender, EventArgs e)
        {
            if (bt_start.Text == "動畫 ST")
            {
                Series series1 = new Series();
                chart1.Series.Add(series1);
                chart1.Series[0].ChartType = chartType;
                bt_start.Text = "動畫 SP";
                timer1.Enabled = true;
            }
            else
            {
                bt_start.Text = "動畫 ST";
                timer1.Enabled = false;
            }
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            if (timer1.Enabled == false)
                chart1.Series.Clear();  //每次使用此function前先清除圖表
            richTextBox1.Clear();
        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            save_chart_image_to_drive();
        }

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
                richTextBox1.Text += "無圖可存\n";
        }


        internal class Item
        {
            public double X { get; private set; }
            public double Y { get; private set; }
            public Item(double x, double y)
            {
                this.X = x;
                this.Y = y;
            }
        }

        //用滑鼠指 顯示數值
        private void button8_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "用滑鼠指線 顯示數值\n";
            FillChart();
            flag_show_value = true;
            this.tooltip.AutomaticDelay = 5;
        }

        private void FillChart()
        {
            var rand = new Random(123);
            var items = Enumerable.Range(0, 20).Select(x => new Item(x, rand.Next(1, 100) / 2.0)).ToList();

            this.chart1.Series.Clear();

            var seriesLines = this.chart1.Series.Add("Line");
            seriesLines.ChartType = SeriesChartType.Line; //System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
            seriesLines.XValueMember = "X";
            seriesLines.YValueMembers = "Y";
            seriesLines.Color = Color.Red;

            var seriesPoints = this.chart1.Series.Add("Points");
            seriesPoints.ChartType = SeriesChartType.Point; //System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
            seriesPoints.XValueMember = "X";
            seriesPoints.YValueMembers = "Y";

            this.chart1.DataSource = items;
        }

        Point? prevPosition = null;
        ToolTip tooltip = new ToolTip();
        private void chart1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_show_value == true)
            {
                var pos = e.Location;
                if (prevPosition.HasValue && pos == prevPosition.Value)
                    return;
                tooltip.RemoveAll();
                prevPosition = pos;
                var results = chart1.HitTest(pos.X, pos.Y, false,
                                                ChartElementType.DataPoint);
                foreach (var result in results)
                {
                    if (result.ChartElementType == ChartElementType.DataPoint)
                    {
                        var prop = result.Object as DataPoint;
                        if (prop != null)
                        {
                            var pointXPixel = result.ChartArea.AxisX.ValueToPixelPosition(prop.XValue);
                            var pointYPixel = result.ChartArea.AxisY.ValueToPixelPosition(prop.YValues[0]);

                            // check if the cursor is really close to the point (2 pixels around)
                            if (Math.Abs(pos.X - pointXPixel) < 2 &&
                                Math.Abs(pos.Y - pointYPixel) < 2)
                            {
                                tooltip.Show("X=" + prop.XValue + ", Y=" + prop.YValues[0], this.chart1,
                                                pos.X, pos.Y - 15);
                            }
                        }
                    }
                }
            }
        }



    }
}
