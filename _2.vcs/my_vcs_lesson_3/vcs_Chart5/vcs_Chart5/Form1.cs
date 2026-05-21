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

namespace vcs_Chart5
{
    public partial class Form1 : Form
    {
        bool flag_show_value = false;

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
            this.Text = "vcs_Chart5";

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
            // 直條圖

            // 清除圖表
            chart0.Series.Clear();
            chart0.Titles.Clear();

            chart0.Titles.Add("直條圖");

            //x軸只顯示一條，只要將資料都加入到一個序列內即可
            //而x軸顯示多條，則需要使用多個序列存放資料

            // 設定數列1 的 大小與外觀
            Series[] series1 = new Series[3];
            double[] _y = new double[] { 77, 35, 131 };
            Color[] _colors = new Color[] { Color.Peru, Color.PowderBlue, Color.RosyBrown };
            String[] _users = new String[] { "小王", "小風", "小明" };

            int _length = _users.Length;

            for (int index = 0; index < _length; index++)
            {
                series1[index] = new Series(_users[index]);
                series1[index].ChartType = SeriesChartType.Column;  // 圖表種類 : 直條圖
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
                chart0.Series.Add(s);
            }
        }

        //------------------------------------------------------------  # 60個

        void draw_chart1()
        {
            // 長條圖

            // 清除圖表
            chart1.Series.Clear();
            chart1.Titles.Clear();

            chart1.Titles.Add("長條圖");

            // 設定數列1 的 大小與外觀
            Series[] series1 = null;
            double[] _y = new double[] { 100, 57, 93, 26, 77, 88 };
            Color[] _colors = new Color[] { Color.Peru, Color.PowderBlue, Color.RosyBrown, Color.Salmon, Color.Sienna, Color.SlateBlue };
            String[] _users = new String[] { "小王", "小風", "小明", "小姿", "小玉", "小蟹" };

            int _length = _y.Length;
            series1 = new Series[_length];
            for (int index = 0; index < _length; index++)
            {
                series1[index] = new Series();
                series1[index].Color = _colors[index];
                series1[index].ChartType = SeriesChartType.Column;  // 圖表種類 : 直條圖
                series1[index].Name = _users[index];
                series1[index].IsValueShownAsLabel = true;
                series1[index].Points.Add(_y[index]);
                chart1.Series.Add(series1[index]);
            }
        }

        //------------------------------------------------------------  # 60個

        void draw_chart2()
        {
            //用滑鼠指線 顯示數值
            richTextBox1.Text += "用滑鼠指線 顯示數值\n";
            FillChart();
            flag_show_value = true;
            this.tooltip.AutomaticDelay = 5;
        }

        private void FillChart()
        {
            //清除圖表
            chart2.Series.Clear();
            chart2.Titles.Clear();

            var rand = new Random(123);
            var items = Enumerable.Range(0, 20).Select(x => new Item(x, rand.Next(1, 100) / 2.0)).ToList();

            var seriesLines = this.chart2.Series.Add("Line");
            seriesLines.ChartType = SeriesChartType.Line; //System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
            seriesLines.XValueMember = "X";
            seriesLines.YValueMembers = "Y";
            seriesLines.Color = Color.Red;

            var seriesPoints = this.chart2.Series.Add("Points");
            seriesPoints.ChartType = SeriesChartType.Point; //System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
            seriesPoints.XValueMember = "X";
            seriesPoints.YValueMembers = "Y";

            this.chart2.DataSource = items;
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

        Point? prevPosition = null;     //好奇怪的寫法?
        ToolTip tooltip = new ToolTip();

        private void chart2_MouseMove(object sender, MouseEventArgs e)
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
                var results = chart2.HitTest(pos.X, pos.Y, false, ChartElementType.DataPoint);
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
                                tooltip.Show("X=" + prop.XValue + ", Y=" + prop.YValues[0], this.chart2, pos.X, pos.Y - 15);
                            }
                        }
                    }
                }
            }
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
        private const int AXIS_X_MIN = 0;
        private const int AXIS_X_MAX = 360;
        private const int AXIS_Y_MIN = -200;
        private const int AXIS_Y_MAX = 200;
        private const string TITLE = "三角函數";
        private const string XLABLE = "Degree";
        private const string YLABLE = "Amplitude";

        void chart_init(Chart chart)
        {
            chart.Titles.Add(TITLE);  // 標題
            chart.Size = new Size(500, 400);  // 設定chart大小

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

        void draw_chart3()
        {
            // 清除圖表
            chart3.Series.Clear();
            chart3.Titles.Clear();

            //靜畫範例1
            chart_init(chart3);
            richTextBox1.Text += "靜畫範例1, 用獨立數組做\n\r";

            // 設定數列1 的 大小與外觀
            Series series1 = new Series("sin", 500); //初始畫線條(標題，最大數值)
            series1.Color = Color.Red; //設定線條顏色
            series1.BorderColor = Color.Navy;  //設置數據邊框的顏色
            series1.BorderWidth = 3;    //線寬
            series1.Font = new Font("新細明體", 10); //設定字型
            series1.ChartType = SeriesChartType.Point;  // 圖表種類 : 點狀圖
            series1.MarkerSize = 5;     //圖標大小
            series1.IsValueShownAsLabel = false;   //將數值顯示在線上 是否在Chart中顯示座標點值
            series1.LegendText = "sin";  // 圖例文字
            series1.Name = "sine";      //設置數據名稱
            series1.ShadowOffset = 10;   //設置陰影偏移量
            series1.ShadowColor = Color.Orange; //設置陰影顏色
            series1.ToolTip = "百分比" + "#PERCENT";//鼠标移动显示数据 //TBD
            series1.Label = "#VALY" + "/" + "#TOTAL" + "#LEGENDTEXT";//直接显示各项数据

            /*
            MsChart的Label的值的转义字符

            #VALX 显示当前图例的X轴的对应文本(或数据)
            #VAL, #VALY, 显示当前图例的Y轴的对应文本(或数据)
            #VALY2, #VALY3, 显示当前图例的辅助Y轴的对应文本(或数据)
            #SER: 显示当前图例的名称
            #LABEL 显示当前图例的标签文本
            #INDEX 显示当前图例的索引
            #PERCENT 显示当前图例的所占的百分比
            #TOTAL 总数量
            #LEGENDTEXT  圖例文字
            */

            // 設定數列2 的 大小與外觀
            Series series2 = new Series("cos", 500); //初始畫線條(標題，最大數值)
            series2.Color = Color.Green; //設定線條顏色
            series2.BorderColor = Color.Navy;  //設置數據邊框的顏色
            series2.BorderWidth = 3;    //線寬
            series2.Font = new Font("標楷體", 12); //設定字型
            series2.ChartType = SeriesChartType.Point;  // 圖表種類 : 點狀圖
            series2.MarkerSize = 5;     //圖標大小
            series2.IsValueShownAsLabel = false;   //將數值顯示在線上 是否在Chart中顯示座標點值
            series2.LegendText = "cos";  // 圖例文字
            series2.Name = "cos";      //設置數據名稱
            series2.ShadowOffset = 10;   //設置陰影偏移量
            series2.ShadowColor = Color.Orange; //設置陰影顏色

            // 設定數列3 的 大小與外觀
            Series series3 = new Series("sin + cos", 500); //初始畫線條(標題，最大數值)
            series3.Color = Color.Blue; //設定線條顏色
            series3.BorderColor = Color.Navy;  //設置數據邊框的顏色
            series3.BorderWidth = 3;    //線寬
            series3.Font = new Font("標楷體", 12); //設定字型
            series3.ChartType = SeriesChartType.Point;  // 圖表種類 : 點狀圖
            series3.MarkerSize = 5;     //圖標大小
            series3.IsValueShownAsLabel = false;   //將數值顯示在線上 是否在Chart中顯示座標點值
            series3.LegendText = "sin + cos";  // 圖例文字
            series3.Name = "sine + cos";      //設置數據名稱
            series3.ShadowOffset = 10;   //設置陰影偏移量
            series3.ShadowColor = Color.Orange; //設置陰影顏色

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
                //richTextBox1.Text += "len = " + chart3.Series[0].Points.Count.ToString() + "\n";
                //chart3.Series[0].Points.AddXY(array_x[i / 10], array_y1[i / 10]);
                series1.Points.AddXY(array_x[i / 10], array_y1[i / 10]);    //將數值1新增至序列1
                series2.Points.AddXY(array_x[i / 10], array_y2[i / 10]);    //將數值2新增至序列2
                series3.Points.AddXY(array_x[i / 10], array_y3[i / 10]);    //將數值3新增至序列3
            }

            //經過chart3.Series.Clear()後, chart3.Series.Count = 0
            chart3.Series.Add(series1);//將序列1新增到chart上
            //此時, chart3.Series.Count = 1
            chart3.Series.Add(series2);//將序列2新增到chart上
            //此時, chart3.Series.Count = 2
            chart3.Series.Add(series3);//將序列3新增到chart上
            //此時, chart3.Series.Count = 3

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

        //------------------------------------------------------------  # 60個

        void draw_chart4()
        {
            // 清除圖表
            chart4.Series.Clear();
            chart4.Titles.Clear();

            //靜畫範例2
            chart_init(chart4);
            richTextBox1.Text += "靜畫範例2, 用數組陣列做\n\r";

            // 設定數列1 的 大小與外觀
            Series[] series = new Series[3];       //預先建立3個數組
            double[] _y = new double[] { 77, 35, 131 };
            Color[] colors = new Color[] { Color.Red, Color.Green, Color.Blue };
            String[] curves = new String[] { "sin", "cos", "sin+cos" };

            int len = curves.Length;

            int i;
            for (i = 0; i < len; i++)
            {
                series[i] = new Series(curves[i]);
                series[i].Color = colors[i];
                series[i].Font = new Font("新細明體", 10); //設定字型
                series[i].ChartType = SeriesChartType.Point;  // 圖表種類 : 點狀圖
                series[i].MarkerSize = 5;     //圖標大小
                series[i].IsValueShownAsLabel = false;  //將數值顯示在線上
            }

            for (i = 0; i <= 360; i += 10)
            {
                series[0].Points.AddXY(i, (int)(110 * sind(i)));                        //將數值1新增至數組陣列0
                series[1].Points.AddXY(i, (int)(110 * cosd(i)));                        //將數值1新增至數組陣列1
                series[2].Points.AddXY(i, (int)(110 * sind(i)) + (int)(110 * cosd(i))); //將數值1新增至數組陣列2
            }

            foreach (Series s in series)
            {
                chart4.Series.Add(s);       //將序列1新增到chart上
            }
        }

        //------------------------------------------------------------  # 60個

        void draw_chart5()
        {

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



/*
            save_chart_image_to_drive();



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


// chart1.Series[0].ChartType = SeriesChartType.Point;

