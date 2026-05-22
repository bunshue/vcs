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

namespace vcs_Chart4
{
    public partial class Form1 : Form
    {
        int W = 500;
        int H = 310;

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
            draw_chart6();
            draw_chart7();
            draw_chart8();
        }

        void show_item_location()
        {
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
            chart6.Size = new Size(W, H);
            chart7.Size = new Size(W, H);
            chart8.Size = new Size(W, H);
            chart0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            chart1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            chart2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            chart3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            chart4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            chart5.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            chart6.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            chart7.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            chart8.Location = new Point(x_st + dx * 2, y_st + dy * 2);

            richTextBox1.Size = new Size(275, 950);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1840, 1010);
            this.Text = "vcs_Chart4";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);

            this.BackColor = Color.Pink;
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        void chart_init(Chart chart1, string title)
        {
            // 清除圖表
            chart1.Series.Clear();
            chart1.Titles.Clear();

            chart1.Titles.Add(title);  // 標題
            chart1.Size = new Size(W, H);  // 設定chart大小

        }

        void draw_chart0()
        {
        }

        //------------------------------------------------------------  # 60個

        void draw_chart1()
        {
            string title = "雷達圖";
            chart_init(chart1, title);

            chart1.ChartAreas.Clear();

            ChartArea area = chart1.ChartAreas.Add("NewArea");

            // 設定數列1 的 大小與外觀
            Series series1 = chart1.Series.Add("雷達資料");
            series1.ChartArea = "NewArea";
            series1.ChartType = SeriesChartType.Radar;  // 雷達圖
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
            string title = "雷達圖";
            chart_init(chart2, title);

            chart2.ChartAreas.Clear();

            ChartArea area = chart2.ChartAreas.Add("NewArea");

            // 設定數列1 的 大小與外觀
            Series series1 = chart2.Series.Add("雷達資料");
            series1.ChartArea = "NewArea";
            series1.ChartType = SeriesChartType.Radar;  // 雷達圖
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

            string title = "";
            chart_init(chart3, title);

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
            series1.ChartType = SeriesChartType.Line;  // 折線圖
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

            if (draw_mode == 0)
            {
                //固定邊界
                richTextBox1.Text += "固定邊界\n";
                chart3.ChartAreas[0].AxisY.Minimum = 0;//設定Y軸最小值
                chart3.ChartAreas[0].AxisY.Maximum = 500;//設定Y軸最大值
            }
            else if (draw_mode == 1)
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
            string[] xx = { "一月", "二月", "三月", "四月", "五月", "六月", "七月" };
            int[] yy = { 25, 18, 30, 24, 35, 50, 40 };
            // NG Series objSeries = chart4.Series.Add("月溫度​℃");
            var objSeries = chart4.Series.First();
            chart4.Series[0].ChartType = SeriesChartType.Point;  // 點狀圖
            objSeries.Points.DataBindXY(xx, yy);  // xx, yy 皆為一維陣列

            //設定邊界
            //chart4.ChartAreas[0].AxisX.Minimum = 0;//設定Y軸最小值
            //chart4.ChartAreas[0].AxisX.Maximum = 8;//設定Y軸最大值
            chart4.ChartAreas[0].AxisY.Minimum = 0;//設定Y軸最小值
            chart4.ChartAreas[0].AxisY.Maximum = 60;//設定Y軸最大值
        }

        //------------------------------------------------------------  # 60個

        void draw_chart5()
        {
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

        void chart_init2(Chart chart)
        {
            chart.Titles.Add("三角函數");  // 標題
            chart.Size = new Size(500, 400);  // 設定chart大小

            //X軸
            chart.ChartAreas[0].AxisX.Minimum = AXIS_X_MIN;        //設定X軸最小值
            chart.ChartAreas[0].AxisX.Maximum = AXIS_X_MAX;        //設定X軸最大值
            chart.ChartAreas[0].AxisX.Title = "角度";              //設定X軸名稱
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
            chart.ChartAreas[0].AxisY.Title = "數值";              //設定Y軸名稱
            chart.ChartAreas[0].AxisY.TitleForeColor = Color.Blue; //設定Y軸名稱的字體顏色
            chart.ChartAreas[0].AxisY.Enabled = AxisEnabled.True;  //顯示 或 隱藏 Y 軸標示
            chart.ChartAreas[0].AxisY.MajorGrid.Enabled = true;    //顯示 或 隱藏 Y 軸標線

            chart.ChartAreas[0].AxisY.LabelStyle.Font = new Font("Trebuchet MS", 8.25F, FontStyle.Bold);//設置Y軸左側的提示信息的字體屬性
            chart.ChartAreas[0].AxisY.LineColor = Color.DarkBlue;//設置軸的線條顏色
            chart.ChartAreas[0].AxisY.MajorGrid.LineColor = Color.White;//設置網格線顏色

            // 圖表樣式
            chart.BackGradientStyle = GradientStyle.TopBottom;//指定圖表元素的漸變樣式(中心向外，從左到右，從上到下等等)
            chart.BackSecondaryColor = Color.Yellow;//設置背景的輔助顏色
            chart.BorderlineColor = Color.Yellow;//設置圖像邊框的顏色
            chart.BorderlineDashStyle = ChartDashStyle.Solid;//設置圖像邊框線的樣式(實線、虛線、點線)
            chart.BorderlineWidth = 2;//設置圖像的邊框寬度
            chart.BorderSkin.SkinStyle = BorderSkinStyle.Emboss;//設置圖像的邊框外觀樣式
            chart.BackColor = Color.Yellow;//設置圖表的背景顏色

            chart.Titles[0].Font = new Font("標楷體", 30f);//设置图表标题字体样式和大小
            chart.Legends["Legend1"].Docking = Docking.Right;  //設定圖標顯示停靠的位置
        }

        void draw_chart6()
        {
            // 清除圖表
            chart6.Series.Clear();
            chart6.Titles.Clear();

            //靜畫範例1
            chart_init2(chart6);
            richTextBox1.Text += "靜畫範例1, 用獨立數組做\n";

            // 設定數列1 的 大小與外觀
            Series series1 = new Series("sin", 500); //初始畫線條(標題，最大數值)
            series1.Color = Color.Red; //設定線條顏色
            series1.BorderColor = Color.Navy;  //設置數據邊框的顏色
            series1.BorderWidth = 3;    //線寬
            series1.Font = new Font("新細明體", 10); //設定字型
            series1.ChartType = SeriesChartType.Point;  // 點狀圖
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
            series2.ChartType = SeriesChartType.Point;  // 點狀圖
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
            series3.ChartType = SeriesChartType.Point;  // 點狀圖
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
                //richTextBox1.Text += "len = " + chart6.Series[0].Points.Count.ToString() + "\n";
                //chart6.Series[0].Points.AddXY(array_x[i / 10], array_y1[i / 10]);
                series1.Points.AddXY(array_x[i / 10], array_y1[i / 10]);    //將數值1新增至序列1
                series2.Points.AddXY(array_x[i / 10], array_y2[i / 10]);    //將數值2新增至序列2
                series3.Points.AddXY(array_x[i / 10], array_y3[i / 10]);    //將數值3新增至序列3
            }

            //經過chart6.Series.Clear()後, chart6.Series.Count = 0
            chart6.Series.Add(series1);//將序列1新增到chart上
            //此時, chart6.Series.Count = 1
            chart6.Series.Add(series2);//將序列2新增到chart上
            //此時, chart6.Series.Count = 2
            chart6.Series.Add(series3);//將序列3新增到chart上
            //此時, chart6.Series.Count = 3

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

        void draw_chart7()
        {
            // 清除圖表
            chart7.Series.Clear();
            chart7.Titles.Clear();

            //靜畫範例2
            chart_init2(chart7);
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
                series[i].ChartType = SeriesChartType.Point;  // 點狀圖
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
                chart7.Series.Add(s);       //將序列1新增到chart上
            }
        }

        //------------------------------------------------------------  # 60個

        void draw_chart8()
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


//數列加入資料點的方法
//series1.Points.AddXY(index, r.Next(10) * 50);
//objSeries.Points.DataBindXY(xx, yy);  // xx, yy 皆為一維陣列




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


/*
chart1.Series[0].Points.Clear();
chart1.Series[1].Points.Clear();
chart1.Series[2].Points.Clear();
*/
/*
            chart1.ChartAreas.Clear();

*/


