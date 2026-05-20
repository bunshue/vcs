using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Windows.Forms.DataVisualization.Charting;  //for Series

namespace vcs_Chart2
{
    public partial class Form1 : Form
    {
        //定義Chart大小與外觀
        private const int CHART_WIDTH = 800;
        private const int CHART_HEIGHT = 330;
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
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            chart1.Size = new Size(CHART_WIDTH, CHART_HEIGHT);       //改變Cahrt大小
            chart1.Series[0].ChartType = SeriesChartType.Point;
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);

            cb_show_data.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            bt_start.Location = new Point(x_st + dx * 0, y_st + dy * 9 + 20);
            bt_save.Location = new Point(x_st + dx * 0, y_st + dy * 9 + 70);

            chart1.Size = new Size(800, 330);
            chart1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            chart0.Size = new Size(800, 330);
            chart0.Location = new Point(x_st + dx * 1, y_st + dy * 5);

            richTextBox1.Size = new Size(800, 320/2);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 10);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1060, 920);
            this.Text = "vcs_Chart2";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            if (timer1.Enabled == false)
            {
                //清除圖表
                chart1.Series.Clear();
                chart1.Titles.Clear();
            }
            richTextBox1.Clear();
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
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string[] xValues = { "一月", "二月", "三月", "四月", "五月", "六月", "七月" };
            int[] yValues = { 25, 18, 30, 24, 35, 50, 40 };
            var objSeries = chart1.Series.First();
            chart1.Series[0].ChartType = SeriesChartType.Point;
            objSeries.Points.DataBindXY(xValues, yValues);

            //設定邊界
            //chart1.ChartAreas[0].AxisX.Minimum = 0;//設定Y軸最小值
            //chart1.ChartAreas[0].AxisX.Maximum = 8;//設定Y軸最大值
            chart1.ChartAreas[0].AxisY.Minimum = 0;//設定Y軸最小值
            chart1.ChartAreas[0].AxisY.Maximum = 60;//設定Y軸最大值
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //清除圖表
            chart1.Series.Clear();
            chart1.Titles.Clear();

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

            int i;
            int count = series1.Points.Count;
            richTextBox1.Text += "共有 " + count.ToString() + " 筆資料\n";
            for (i = 0; i < count; i++)
            {
                richTextBox1.Text += "X[" + i.ToString() + "] = " + series1.Points[i].XValue.ToString() + "\t";
                richTextBox1.Text += "Y[" + i.ToString() + "] = " + series1.Points[i].YValues[0].ToString() + "\n";
            }

            //設定邊界
            chart1.ChartAreas[0].AxisX.Minimum = 0;//設定Y軸最小值
            chart1.ChartAreas[0].AxisX.Maximum = 8;//設定Y軸最大值
            chart1.ChartAreas[0].AxisY.Minimum = 0;//設定Y軸最小值
            chart1.ChartAreas[0].AxisY.Maximum = 400;//設定Y軸最大值

            this.chart1.Series.Add(series1);//將線畫在圖上
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {
            // 繪製圓餅圖,  fail

            /*  TBD
            Series series1 = new Series();
            double[] _y = new double[] { 77, 35, 131, 55, 77, 66 };
            Color[] _colors = new Color[] { Color.Peru, Color.PowderBlue, Color.RosyBrown, Color.Salmon, Color.Sienna, Color.SlateBlue };
            String[] _users = new String[] { "小王", "小風", "小明", "小姿", "小玉", "小蟹" };

            series1.ChartType = SeriesChartType.Pie;
            series1.IsValueShownAsLabel = true;
            series1.Points.DataBindXY(_users, _y);
            chart1.Series.Add(series1);
            */
        }

        private void button7_Click(object sender, EventArgs e)
        {
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
                //清除圖表
                chart1.Series.Clear();
                chart1.Titles.Clear();

                Series series1 = new Series();
                chart1.Series.Add(series1);
                chart1.Series[0].ChartType = SeriesChartType.Point;
                bt_start.Text = "動畫 SP";
                timer1.Enabled = true;
            }
            else
            {
                bt_start.Text = "動畫 ST";
                timer1.Enabled = false;
            }
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

            //清除圖表
            chart1.Series.Clear();
            chart1.Titles.Clear();

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

        Point? prevPosition = null;     //好奇怪的寫法?
        ToolTip tooltip = new ToolTip();
        private void chart1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_show_value == true)
            {
                var pos = e.Location;
                if (prevPosition.HasValue && pos == prevPosition.Value)
                {
                    return;
                }
                tooltip.RemoveAll();
                prevPosition = pos;
                var results = chart1.HitTest(pos.X, pos.Y, false, ChartElementType.DataPoint);
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
                            if (Math.Abs(pos.X - pointXPixel) < 2 && Math.Abs(pos.Y - pointYPixel) < 2)
                            {
                                tooltip.Show("X=" + prop.XValue + ", Y=" + prop.YValues[0], this.chart1, pos.X, pos.Y - 15);
                            }
                        }
                    }
                }
            }
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
