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

/*
拉一個Chart控件
chart5屬性
ChartAreas 移除 ChartArea1
Series 移除 Series1
*/

// x軸只顯示一條，只要將資料都加入到一個序列內即可
// 而x軸顯示多條，則需要使用多個序列存放資料

namespace vcs_Chart1
{
    public partial class Form1 : Form
    {
        int W = 500;
        int H = 310;

        bool flag_show_value = true;
        int flag_show_radar_type = 0;

        Font titles_font = new Font("Trebuchet MS", 14F, FontStyle.Bold);  // 標題的字型
        Font xlabel_font = new Font("Trebuchet MS", 15, FontStyle.Bold);  // 設定X軸刻度的字型
        Font ylabel_font = new Font("Trebuchet MS", 8.25F, FontStyle.Bold);  // 設置Y軸左側的提示信息的字體屬性
        Font series_font = new Font("Trebuchet MS", 10, FontStyle.Bold);  // 數列series顯示數值的字型

        SeriesChartType chartType = SeriesChartType.Point;

        //定義Chart大小與外觀
        private const int AXIS_X_MIN = 0;
        private const int AXIS_X_MAX = 360;
        private const int AXIS_Y_MIN = -200;
        private const int AXIS_Y_MAX = 200;

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
            chart0.Size = new Size(W, H);  // 設定chart大小
            chart1.Size = new Size(W, H);  // 設定chart大小
            chart2.Size = new Size(W, H);  // 設定chart大小
            chart3.Size = new Size(W, H);  // 設定chart大小
            chart4.Size = new Size(W, H);  // 設定chart大小
            chart5.Size = new Size(W, H);  // 設定chart大小
            chart6.Size = new Size(W, H);  // 設定chart大小
            chart7.Size = new Size(W, H);  // 設定chart大小
            chart8.Size = new Size(W, H);  // 設定chart大小
            chart0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            chart1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            chart2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            chart3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            chart4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            chart5.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            chart6.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            chart7.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            chart8.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            bt_chart6.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_chart6.BringToFront();
            bt_chart7.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            bt_chart7.BringToFront();
            bt_chart_type.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_chart_type.BringToFront();
            groupBox1.Visible = false;

            richTextBox1.Size = new Size(275, 950);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            bt_chart_save.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y);

            x_st = 20;
            y_st = 40;
            dx = 190;
            dy = 36;
            radioButton0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            radioButton1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            radioButton2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            radioButton3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            radioButton4.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            radioButton5.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            radioButton6.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            radioButton7.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            radioButton8.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            radioButton9.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            radioButton10.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            radioButton11.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            radioButton12.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            radioButton13.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            radioButton14.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            radioButton15.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            radioButton16.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            radioButton17.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            radioButton18.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            radioButton19.Location = new Point(x_st + dx * 4, y_st + dy * 3);
            radioButton20.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            radioButton21.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            radioButton22.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            radioButton23.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            radioButton24.Location = new Point(x_st + dx * 4, y_st + dy * 4);
            radioButton25.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            radioButton26.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            radioButton27.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            radioButton28.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            radioButton29.Location = new Point(x_st + dx * 4, y_st + dy * 5);
            radioButton30.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            radioButton31.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            radioButton32.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            radioButton33.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            radioButton34.Location = new Point(x_st + dx * 4, y_st + dy * 6);
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

            this.Size = new Size(1840, 1010);
            this.Text = "vcs_Chart1";

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
            // 清除圖表內的元件, 清除後要先新增才能使用
            //C T L S
            chart1.ChartAreas.Clear();  // 清除所有圖表區
            chart1.Titles.Clear();  // 清除所有標題
            chart1.Legends.Clear();  // 清除所有圖例
            chart1.Series.Clear();  // 清除所有數列

            //------------------------------  # 30個

            chart1.Size = new Size(W, H);  // 設定chart大小

            // 圖表樣式
            chart1.BackGradientStyle = GradientStyle.TopBottom;//指定圖表元素的漸變樣式(中心向外，從左到右，從上到下等等)
            chart1.BackSecondaryColor = Color.Yellow;//設置背景的輔助顏色
            chart1.BorderlineColor = Color.Yellow;//設置圖像邊框的顏色
            chart1.BorderlineDashStyle = ChartDashStyle.Solid;//設置圖像邊框線的樣式(實線、虛線、點線)
            chart1.BorderlineWidth = 2;//設置圖像的邊框寬度
            chart1.BorderSkin.SkinStyle = BorderSkinStyle.Emboss;//設置圖像的邊框外觀樣式
            chart1.BackColor = Color.Yellow;//設置圖表的背景顏色

            //------------------------------  # 30個

            //圖表區設定
            ChartArea chartarea = new ChartArea("ChartArea1");
            chart1.ChartAreas.Add(chartarea);  // 將圖表區新增到圖表上

            chartarea.BackColor = Color.Pink;  // 圖表區背景色
            chartarea.BackColor = Color.FromArgb(240, 240, 240);  // 圖表區背景色

            //X軸設定
            //chartarea.AxisX.CustomLabels.Clear();
            chartarea.AxisX.Enabled = AxisEnabled.True;
            chartarea.AxisX2.Enabled = AxisEnabled.False; //隱藏 X2 標示
            chartarea.AxisX.MajorGrid.LineColor = Color.Red;  // X軸主格線顏色
            chartarea.AxisX.Title = "種類";  // 設定X軸的標題
            chartarea.AxisX.Interval = 1;  // 設定X軸坐標的間隔
            chartarea.AxisX.IntervalOffset = 1;  //設置X軸坐標偏移為1
            chartarea.AxisX.LabelStyle.IsStaggered = true;   //設置是否交錯顯示,比如數據多的時間分成兩行來顯示
            chartarea.AxisX.MajorGrid.LineColor = Color.FromArgb(150, 150, 150);//X 軸線顏色
            // 設定邊界
            //chartarea.AxisX.Minimum = 0;  // 設定X軸最小值
            //chartarea.AxisX.Maximum = 20;  // 設定X軸最大值

            /*
            //X軸 new
            chartarea.AxisX.Minimum = AXIS_X_MIN;        //設定X軸最小值
            chartarea.AxisX.Maximum = AXIS_X_MAX;        //設定X軸最大值
            chartarea.AxisX.Title = "X軸標題";              //設定X軸名稱
            chartarea.AxisX.TitleForeColor = Color.Blue; //設定X軸名稱的字體顏色
            chartarea.AxisX.Enabled = AxisEnabled.True;  //顯示 或 隱藏 X 軸標示
            chartarea.AxisX.MajorGrid.Enabled = true;    //顯示 或 隱藏 X 軸標線
            chartarea.AxisX.LabelStyle.Font = xlabel_font;
            chartarea.AxisX.LabelStyle.Interval = 60;    //設置X軸刻度間隔的大小
            chartarea.AxisX.LabelStyle.IntervalType = DateTimeIntervalType.Number;//設置間隔大小的度量單位
            chartarea.AxisX.LineColor = Color.White;//設置X軸的線條顏色
            chartarea.AxisX.MajorGrid.Interval = 100;//設置主網格線與次要網格線的間隔
            chartarea.AxisX.MajorGrid.IntervalType = DateTimeIntervalType.Number;//設置主網格線與次網格線的間隔的度量單位
            chartarea.AxisX.MajorGrid.LineColor = Color.Snow;//設置網格線的顏色
            chartarea.AxisX.MajorTickMark.Interval = 20;//設置刻度線的間隔
            chartarea.AxisX.MajorTickMark.IntervalType = DateTimeIntervalType.Number;//設置刻度線的間隔的度量單位
            */

            //Y軸設定
            chartarea.AxisY.MajorGrid.LineColor = Color.Green;  // Y軸主格線顏色
            chartarea.AxisY.MajorGrid.Enabled = true;  // 顯示Y軸主格線
            chartarea.AxisY.Enabled = AxisEnabled.True; // 啟動Y軸標示
            chartarea.AxisY.Title = "體重(公斤)";  //設定Y軸的標題
            chartarea.AxisY.LineColor = Color.Red;
            chartarea.AxisY.LineWidth = 1;
            chartarea.AxisY2.Enabled = AxisEnabled.False; //隱藏 Y2 標示
            chartarea.AxisY2.MajorGrid.Enabled = false;   //隱藏 Y2 軸線
            chartarea.AxisY.MajorGrid.LineColor = Color.FromArgb(150, 150, 150);//Y 軸線顏色
            chartarea.AxisY.LabelStyle.Format = "#.###";//設定小數點
            // 設定邊界
            //chartarea.AxisY.Minimum = 0;  // 設定Y軸最小值
            //chartarea.AxisY.Maximum = 100;  // 設定Y軸最大值

            /*
            //Y軸 new
            chartarea.AxisY.Minimum = AXIS_Y_MIN;        //設定Y軸最小值
            chartarea.AxisY.Maximum = AXIS_Y_MAX;        //設定Y軸最大值
            chartarea.AxisY.Title = "Y軸標題";              //設定Y軸名稱
            chartarea.AxisY.TitleForeColor = Color.Blue; //設定Y軸名稱的字體顏色
            chartarea.AxisY.Enabled = AxisEnabled.True;  //顯示 或 隱藏 Y 軸標示
            chartarea.AxisY.MajorGrid.Enabled = true;    //顯示 或 隱藏 Y 軸標線

            chartarea.AxisY.LabelStyle.Font = ylabel_font;
            chartarea.AxisY.LineColor = Color.DarkBlue;//設置軸的線條顏色
            chartarea.AxisY.MajorGrid.LineColor = Color.White;//設置網格線顏色
            */



            //設定3D
            /*
            chartarea.Area3DStyle.Enable3D = true;  // 設定圖表區3D顯示
            chartarea.Area3DStyle.IsClustered = true; //並排顯示
            chartarea.Area3DStyle.Rotation = 40; //垂直角度
            chartarea.Area3DStyle.Inclination = 50; //水平角度
            chartarea.Area3DStyle.PointDepth = 10; //數據條厚度
            chartarea.Area3DStyle.WallWidth = 0; //外牆寬度
            chartarea.Area3DStyle.LightStyle = LightStyle.Realistic; //光源
            */

            //------------------------------  # 30個

            // 畫標題的方法1
            Title chart_title = new Title();
            chart_title.Text = title;
            chart_title.Alignment = ContentAlignment.MiddleCenter;
            chart_title.Font = titles_font;
            chart1.Titles.Add(chart_title);  // 將標題新增到圖表上

            // 畫標題的方法2
            Title chart_title2 = new Title
            {
                Text = title,
                Alignment = ContentAlignment.MiddleCenter,
                Font = titles_font
            };
            //chart1.Titles.Add(chart_title2);  // 將標題新增到圖表上

            // 設定標題1, Title1, 設定要顯示在哪個圖表
            chart1.Titles["Title1"].DockedToChartArea = "ChartArea1";  // 設定標題要顯示在哪個圖表區
            chart1.Titles["Title1"].IsDockedInsideChartArea = false;  // 設定要顯示在圖表的內外部

            //------------------------------  # 30個

            // 設定圖例.Legends
            chart1.Legends.Add("Legends1");  // 將圖例新增到圖表上
            chart1.Legends["Legends1"].DockedToChartArea = "ChartArea1";  // 設定圖例要顯示在哪個圖表區
            chart1.Legends["Legends1"].Docking = Docking.Right;  // 設定圖例的顯示停靠的位置, 預設靠右
            chart1.Legends["Legends1"].BackColor = Color.FromArgb(235, 235, 235);  // 背景色
            chart1.Legends["Legends1"].BackHatchStyle = ChartHatchStyle.DarkDownwardDiagonal;  // 斜線背景
            chart1.Legends["Legends1"].BorderWidth = 1;
            chart1.Legends["Legends1"].BorderColor = Color.FromArgb(200, 200, 200);
            chart1.Legends["Legends1"].IsDockedInsideChartArea = false;  // 設定要顯示在圖表的內外部
        }

        void series_point_add_data(Series series1)
        {
            string[] name = new string[] { "鼠", "牛", "虎", "兔", "龍" };
            int[] weight = new int[] { 3, 48, 33, 8, 38 };

            //1. DataBindXY
            //series1.Points.DataBindXY(name, weight);  // xx, yy 皆為一維陣列, same

            //2. 一個一個加入 AddXY
            /*
            //把值加入X 軸Y 軸
            series1.Points.AddXY("鼠", 3);
            series1.Points.AddXY("牛", 48);
            series1.Points.AddXY("虎", 33);
            series1.Points.AddXY("兔", 8);
            series1.Points.AddXY("龍", 38);
            */
            for (int i = 0; i < name.Length; i++)
            {
                //series1.Points.Add(weight[i]);  // Add 一維加入
                series1.Points.AddXY(name[i], weight[i]);  // AddXY 二維加入
            }

            //為每個點加入顏色
            Random rnd = new Random();  //亂數產生區塊顏色
            int count = series1.Points.Count;  // 數列1內的資料個數
            //richTextBox1.Text += "共有 " + count.ToString() + " 筆資料\n";
            for (int i = 0; i < count; i++)
            {
                series1.Points[i].BorderColor = Color.Red;  // 邊框顏色 for 直條圖
                series1.Points[i].Color = Color.FromArgb(150, rnd.Next(0, 255), rnd.Next(0, 255), rnd.Next(0, 255));
                //richTextBox1.Text += "X[" + i.ToString() + "] = " + series1.Points[i].XValue.ToString() + "\t";
                //richTextBox1.Text += "Y[" + i.ToString() + "] = " + series1.Points[i].YValues[0].ToString() + "\n";
            }

        }

        void chart_add_series0a(Chart chart1)
        {
            // 設定數列1 的 大小與外觀
            Series series1 = new Series("體重1", 500);  // 初始化數列1(名稱, 最大值)
            series1.ChartType = SeriesChartType.Column;  // 直條圖
            series1.Color = Color.Red; // 設定線條顏色
            series1.BorderWidth = 3;  // 線寬
            series1.Name = "體重1";  // 數列名稱
            series1.Font = series_font;
            series1.IsValueShownAsLabel = true;  // 是否把數值顯示在線上

            series_point_add_data(series1);

            chart1.Series.Add(series1);  // 將數列1新增到chart上
        }

        //------------------------------------------------------------  # 60個

        void chart_add_series0b(Chart chart1)
        {
            // 設定數列1 的 大小與外觀
            Series series1 = new Series("體重2", 500);  // 初始化數列2(名稱, 最大值)
            series1.ChartType = SeriesChartType.Line;  // 折線圖
            series1.ChartType = SeriesChartType.Column;  // 直條圖
            series1.Color = Color.Red; // 設定線條顏色
            series1.BorderWidth = 3;  // 線寬
            series1.Name = "體重2";  // 數列名稱
            series1.Font = series_font;
            series1.IsValueShownAsLabel = true;  // 是否把數值顯示在線上

            series_point_add_data(series1);

            chart1.Series.Add(series1);  // 將數列1新增到chart上
        }

        void draw_chart0()
        {
            string title = "直條圖 + 折線圖";
            chart_init(chart0, title);

            chart_add_series0a(chart0);
            chart_add_series0b(chart0);
        }

        void draw_chart1()
        {
        }

        //------------------------------------------------------------  # 60個

        void chart_add_series2a(Chart chart1)
        {
            // 設定數列1 的 大小與外觀
            Series series1 = new Series("體重1", 500);  // 初始化數列1(名稱, 最大值)
            series1.ChartType = SeriesChartType.Pie;  // 圓形圖
            series1.ChartType = SeriesChartType.Column; //直條圖(Column),折線圖(Line),橫條圖(Bar)

            //設定 Series1
            series1.ChartArea = "ChartArea1";  // 設定要呈現的圖表區

            series_point_add_data(series1);

            series1.Legend = "Legends1";  // 設定要呈現哪個圖例
            series1.LegendText = "體重1";  // 設定圖例文字
            series1.LabelFormat = "#.###"; //小數點
            series1.MarkerSize = 8; //Label 範圍大小
            series1.LabelForeColor = Color.FromArgb(0, 90, 255); //字體顏色

            series1.Font = series_font;

            //Label 背景色
            series1.LabelBackColor = Color.FromArgb(150, 255, 255, 255);
            series1.Color = Color.FromArgb(240, 65, 140, 240); //背景色
            series1.IsValueShownAsLabel = true;  // 是否把數值顯示在線上

            chart1.Series.Add(series1);  // 將數列1新增到圖表上
        }

        void chart_add_series2b(Chart chart1)
        {
            // 設定數列1 的 大小與外觀
            Series series1 = new Series("體重2", 500);  // 初始化數列1(名稱, 最大值)
            series1.ChartType = SeriesChartType.Pie;  // 圓形圖
            series1.ChartType = SeriesChartType.Column; //直條圖(Column),折線圖(Line),橫條圖(Bar)

            series_point_add_data(series1);

            series1.Legend = "Legends1";
            series1.LegendText = "體重2";
            series1.LabelFormat = "#.###"; //小數點
            series1.MarkerSize = 8; //Label 範圍大小
            series1.LabelForeColor = Color.FromArgb(255, 103, 0);
            series1.Font = series_font;
            series1.LabelBackColor = Color.FromArgb(150, 255, 255, 255);
            series1.Color = Color.FromArgb(240, 252, 180, 65); //背景色
            series1.IsValueShownAsLabel = true;  // 是否把數值顯示在線上

            chart1.Series.Add(series1);  // 將數列2新增到圖表上
        }

        void draw_chart2()
        {
            string title = "直條圖";
            chart_init(chart2, title);

            //------------------------------  # 30個

            chart_add_series2a(chart2);
            chart_add_series2b(chart2);
        }

        //------------------------------------------------------------  # 60個

        void draw_chart3()
        {
            // 各種圖表類型

            string title = "各種圖表類型";
            //chart_init(chart3, title);

            //------------------------------  # 30個

            // 清除圖表
            chart3.Series.Clear();  // 清除所有數列
            chart3.Titles.Clear();  // 清除所有標題

            // 全圖設定
            chart3.Titles.Add("各種圖表類型, 3數列");  // 將標題新增到圖表上

            // X軸設定
            chart3.ChartAreas[0].AxisX.Minimum = AXIS_X_MIN;  // 設定X軸最小值
            chart3.ChartAreas[0].AxisX.Maximum = AXIS_X_MAX;  // 設定X軸最大值
            chart3.ChartAreas[0].AxisX.Title = "角度";
            chart3.ChartAreas[0].AxisX.Enabled = AxisEnabled.True;  // 顯示 或 隱藏 X 軸標示
            chart3.ChartAreas[0].AxisX.MajorGrid.Enabled = true;  // 顯示 或 隱藏 X 軸標線

            // Y軸設定
            chart3.ChartAreas[0].AxisY.Minimum = AXIS_Y_MIN;  // 設定Y軸最小值
            chart3.ChartAreas[0].AxisY.Maximum = AXIS_Y_MAX;  // 設定Y軸最大值
            chart3.ChartAreas[0].AxisY.Title = "高度";
            chart3.ChartAreas[0].AxisY.Enabled = AxisEnabled.True;  // 顯示 或 隱藏 Y 軸標示
            chart3.ChartAreas[0].AxisY.MajorGrid.Enabled = true;  // 顯示 或 隱藏 Y 軸標線

            // 設定數列1 的 大小與外觀
            Series series1 = new Series("sin", 500);  // 初始畫線條(標題，最大值)
            series1.Color = Color.Red;  // 設定線條顏色
            series1.Font = new Font("新細明體", 10);  // 設定顯示數值的字型
            series1.ChartType = chartType;  // 設定線條種類
            series1.MarkerSize = 5;  // 圖標大小
            series1.IsValueShownAsLabel = false;  // 將數值顯示在線上

            // 設定數列2 的 大小與外觀
            Series series2 = new Series("cos", 500);  // 初始畫線條(標題，最大值)
            series2.Color = Color.Green;  // 設定線條顏色
            series2.Font = new Font("標楷體", 12);  // 設定顯示數值的字型
            series2.ChartType = chartType;  // 設定線條種類
            series2.MarkerSize = 5;  // 圖標大小
            series2.IsValueShownAsLabel = false;  // 將數值顯示在線上

            // 設定數列3 的 大小與外觀
            Series series3 = new Series("sin + cos", 500);  // 初始畫線條(標題，最大值)
            series3.Color = Color.Blue;  // 設定線條顏色
            series3.Font = new Font("標楷體", 12);  // 設定顯示數值的字型
            series3.ChartType = chartType;  // 設定線條種類
            series3.MarkerSize = 5;  // 圖標大小
            series3.IsValueShownAsLabel = false;  // 將數值顯示在線上

            // 設定 數列1 數列2 數列3 的 數值

            int[] array_xx = new int[37];
            int[] array_y1 = new int[37];
            int[] array_y2 = new int[37];
            int[] array_y3 = new int[37];
            for (int i = 0; i <= 360; i += 10)
            {
                array_xx[i / 10] = i;
                array_y1[i / 10] = (int)(110 * sind(i));
                array_y2[i / 10] = (int)(110 * cosd(i));
                array_y3[i / 10] = (int)(110 * sind(i) + 110 * cosd(i));
                //chart1.Series[0].Points.AddXY(array_xx[i / 10], array_y1[i / 10]);
                series1.Points.AddXY(array_xx[i / 10], array_y1[i / 10]);  // 將數值1新增至數列1
                series2.Points.AddXY(array_xx[i / 10], array_y2[i / 10]);  // 將數值2新增至數列2
                series3.Points.AddXY(array_xx[i / 10], array_y3[i / 10]);  // 將數值3新增至數列3
            }

            // 將數列新增到chart上
            chart3.Series.Add(series1);
            chart3.Series.Add(series2);
            chart3.Series.Add(series3);

            show_series_data(chart3);
        }

        void show_series_data(Chart chart1)
        {
            richTextBox1.Text += "目前 chart1 上的數列數  : " + chart1.Series.Count.ToString() + "\n";
            richTextBox1.Text += "目前 Series[0] 上的點數 : " + chart1.Series[0].Points.Count.ToString() + "\n";
            richTextBox1.Text += "目前 Series[1] 上的點數 : " + chart1.Series[1].Points.Count.ToString() + "\n";
            richTextBox1.Text += "目前 Series[2] 上的點數 : " + chart1.Series[2].Points.Count.ToString() + "\n";

            richTextBox1.Text += "顯示資料\n";
            int count = chart1.Series[0].Points.Count;
            richTextBox1.Text += "共有 " + count.ToString() + " 筆資料\n";
            for (int i = 0; i < count; i++)
            {
                richTextBox1.Text += "x[" + i.ToString() + "] = " + chart1.Series[0].Points[i].XValue.ToString() + "\t";
                richTextBox1.Text += "sin[" + i.ToString() + "] = " + chart1.Series[0].Points[i].YValues[0].ToString() + "\t";
                richTextBox1.Text += "cos[" + i.ToString() + "] = " + chart1.Series[1].Points[i].YValues[0].ToString() + "\t";
                richTextBox1.Text += "sin[" + i.ToString() + "] + " + "cos[" + i.ToString() + "] = " + chart1.Series[2].Points[i].YValues[0].ToString() + "\n";
            }
        }

        //------------------------------------------------------------  # 60個

        void chart_add_series4(Chart chart1)
        {
            // 設定數列1 的 大小與外觀
            Series series1 = new Series("體重", 500);  // 初始化數列1
            series1.ChartType = SeriesChartType.Pie;  // 圓形圖
            //series1.ChartType = SeriesChartType.Doughnut;  // 環圈圖
            series1.IsValueShownAsLabel = true;  // 是否把數值顯示在線上

            series_point_add_data(series1);

            //series1.LegendText = "體重";   //#VALX:    [ #PERCENT{P1} ]; //X軸 + 百分比
            //series1.Label = "bbbb";  //#VALX#PERCENT{P1}; //X軸 + 百分比
            series1.LabelForeColor = Color.Red; //字體顏色
            //字體設定
            series1.Font = series_font;
            series1.Points.FindMaxByValue().LabelForeColor = Color.Red;
            //series1.Points.FindMaxByValue().Color = Color.Red;
            //series1.Points.FindMaxByValue()[Exploded] = true;
            series1.BorderColor = Color.FromArgb(255, 101, 101, 101);

            //series1[DoughnutRadius] = 80; // ChartType為Doughnut時，Set Doughnut hole size
            //series1[PieLabelStyle] = Inside; //數值顯示在圓餅內
            ////series1[PieLabelStyle] = Outside; //數值顯示在圓餅外
            //series1[PieLabelStyle] = Disabled; //不顯示數值
            //設定圓餅效果，除 Default 外其他效果3D不適用
            ////series1[PieDrawingStyle] = Default;
            //series1[PieDrawingStyle] = SoftEdge;
            //series1[PieDrawingStyle] = Concave;

            chart1.Series.Add(series1);  // 將數列1新增到圖表上
        }

        void draw_chart4()
        {
            string title = "圓形圖";
            chart_init(chart4, title);

            chart_add_series4(chart4);
        }

        //------------------------------------------------------------  # 60個

        void chart_add_series5(Chart chart1)
        {
            // 設定數列1 的 大小與外觀
            Series series1 = new Series("體重1", 500);  // 初始化數列1(名稱, 最大值)
            series1.ChartType = SeriesChartType.Pie;  // 圓形圖
            series1.ChartArea = "ChartArea1";  // 設定要呈現的ChartArea
            //series1.ChartType = SeriesChartType.Doughnut;  // 環圈圖

            series_point_add_data(series1);

            series1.Legend = "Legends1";  // 設定要呈現哪個圖例
            // series1.IsValueShownAsLabel = true;  // 是否把數值顯示在線上
            series1.XValueType = ChartValueType.String; //X軸的資料格式
            series1.LegendText = "#VALX :[ #PERCENT{P1} ]"; //X軸 + 百分比
            series1.Label = "#VALX\n#PERCENT{P1}"; //X軸 + 百分比
            //series1.LabelForeColor = Color.FromArgb(0, 90, 255); //字體顏色

            series1.Font = series_font;
            series1.Points.FindMaxByValue().LabelForeColor = Color.Red; //設定特定數字之字體
            //series1.Points.FindMaxByValue().Color = Color.Red; //設定數值最大的餅的顏色
            //series1.Points.FindMaxByValue()["Exploded"] = "true";  // 設定數值最大的餅是否分離出去
            series1.BorderColor = Color.FromArgb(255, 101, 101, 101);
            //series1["DoughnutRadius"] = "80"; // ChartType為Doughnut時，Set Doughnut hole size
            //series1["PieLabelStyle"] = "Inside"; //數值顯示在圓餅內
            series1["PieLabelStyle"] = "Outside"; //數值顯示在圓餅外
            //series1["PieLabelStyle"] = "Disabled"; //不顯示數值

            //設定圓餅效果，除 Default 外其他效果3D不適用
            //series1["PieDrawingStyle"] = "Default";
            //series1["PieDrawingStyle"] = "SoftEdge";
            //series1["PieDrawingStyle"] = "Concave";

            chart1.Series.Add(series1);  // 將數列1新增到圖表上
        }

        void draw_chart5()
        {
            string title = "各區比例";
            chart_init(chart5, title);

            // 設定標題2
            chart5.Titles.Add("Title1");  // 將標題新增到圖表上
            chart5.Titles["Title1"].DockedToChartArea = "ChartArea1";  // 設定標題要顯示在哪個圖表區
            chart5.Titles["Title1"].IsDockedInsideChartArea = false; //設定顯示在圖表的內外部
            chart5.Titles["Title1"].Text = "各區比例";

            chart_add_series5(chart5);
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

        void draw_chart6()
        {
            string title = "完整範例";

            // 清除圖表
            chart6.Series.Clear();  // 清除所有數列
            chart6.Titles.Clear();  // 清除所有標題

            // 畫標題的方法1
            Title chart_title = new Title();
            chart_title.Text = title;
            chart_title.Alignment = ContentAlignment.MiddleCenter;
            chart_title.Font = titles_font;
            chart6.Titles.Add(chart_title);  // 將標題新增到圖表上

            // 畫標題的方法2
            Title chart_title2 = new Title
            {
                Text = title,
                Alignment = ContentAlignment.MiddleCenter,
                Font = titles_font
            };
            //chart6.Titles.Add(chart_title2);  // 將標題新增到圖表上

            //圖表區設定, X軸
            chart6.ChartAreas[0].AxisX.Minimum = 0;  // 設定X軸最小值
            chart6.ChartAreas[0].AxisX.Maximum = 360;  // 設定X軸最大值
            chart6.ChartAreas[0].AxisX.Title = "角度";  // 設定X軸名稱
            chart6.ChartAreas[0].AxisX.TitleForeColor = Color.Blue;  // 設定X軸名稱的字體顏色
            chart6.ChartAreas[0].AxisX.Enabled = AxisEnabled.True;  // 顯示 或 隱藏 X 軸標示
            chart6.ChartAreas[0].AxisX.MajorGrid.Enabled = true;  // 顯示 或 隱藏 X 軸標線
            chart6.ChartAreas[0].AxisX.LabelStyle.Font = xlabel_font;
            chart6.ChartAreas[0].AxisX.LabelStyle.Interval = 60;  // 設置X軸刻度間隔的大小
            chart6.ChartAreas[0].AxisX.LabelStyle.IntervalType = DateTimeIntervalType.Number;  // 設置間隔大小的度量單位
            chart6.ChartAreas[0].AxisX.LineColor = Color.White;  // 設置X軸的線條顏色
            chart6.ChartAreas[0].AxisX.MajorGrid.Interval = 100;  // 設置主網格線與次要網格線的間隔
            chart6.ChartAreas[0].AxisX.MajorGrid.IntervalType = DateTimeIntervalType.Number;  // 設置主網格線與次網格線的間隔的度量單位
            chart6.ChartAreas[0].AxisX.MajorGrid.LineColor = Color.Snow;  // 設置網格線的顏色
            chart6.ChartAreas[0].AxisX.MajorTickMark.Interval = 20;  // 設置刻度線的間隔
            chart6.ChartAreas[0].AxisX.MajorTickMark.IntervalType = DateTimeIntervalType.Number;  // 設置刻度線的間隔的度量單位

            //圖表區設定, Y軸
            chart6.ChartAreas[0].AxisY.Minimum = -200;  // 設定Y軸最小值
            chart6.ChartAreas[0].AxisY.Maximum = 200;  // 設定Y軸最大值
            chart6.ChartAreas[0].AxisY.Title = "數值";  // 設定Y軸名稱
            chart6.ChartAreas[0].AxisY.TitleForeColor = Color.Blue;  // 設定Y軸名稱的字體顏色
            chart6.ChartAreas[0].AxisY.Enabled = AxisEnabled.True;  // 顯示 或 隱藏 Y 軸標示
            chart6.ChartAreas[0].AxisY.MajorGrid.Enabled = true;  // 顯示 或 隱藏 Y 軸標線
            chart6.ChartAreas[0].AxisY.LabelStyle.Font = ylabel_font;
            chart6.ChartAreas[0].AxisY.LineColor = Color.DarkBlue;  // 設置軸的線條顏色
            chart6.ChartAreas[0].AxisY.MajorGrid.LineColor = Color.White;  // 設置網格線顏色

            // 圖表樣式
            chart6.BackGradientStyle = GradientStyle.TopBottom;  // 指定圖表元素的漸變樣式(中心向外，從左到右，從上到下等等)
            chart6.BackSecondaryColor = Color.Yellow;  // 設置背景的輔助顏色
            chart6.BorderlineColor = Color.Yellow;  // 設置圖像邊框的顏色
            chart6.BorderlineDashStyle = ChartDashStyle.Solid;  // 設置圖像邊框線的樣式(實線、虛線、點線)
            chart6.BorderlineWidth = 2;  // 設置圖像的邊框寬度
            chart6.BorderSkin.SkinStyle = BorderSkinStyle.Emboss;  // 設置圖像的邊框外觀樣式
            chart6.BackColor = Color.Yellow;  // 設置圖表的背景顏色

            // 設定圖例.Legends
            chart6.Legends["Legend1"].Docking = Docking.Right;  // 設定圖例的顯示停靠的位置, 預設靠右

            //------------------------------  # 30個

            // 設定數列1 的 大小與外觀
            Series series1 = new Series("sin", 500);  // 初始化數列1(名稱, 最大值)
            series1.ChartType = SeriesChartType.Point;  // 點狀圖
            series1.Color = Color.Red; //設定線條顏色
            series1.BorderColor = Color.Navy;  //設置數據邊框的顏色
            series1.BorderWidth = 3;    //線寬
            series1.Font = series_font;
            series1.MarkerSize = 5;     //圖標大小
            series1.IsValueShownAsLabel = false;   //將數值顯示在線上 是否在Chart中顯示座標點值
            series1.LegendText = "sin";  // 圖例文字
            series1.Name = "sine";      //設置數據名稱
            //series1.ShadowOffset = 10;   //設置陰影偏移量
            //series1.ShadowColor = Color.Orange; //設置陰影顏色
            //series1.ToolTip = "百分比" + "#PERCENT";//鼠标移动显示数据 //TBD
            //series1.Label = "#VALY" + "/" + "#TOTAL" + "#LEGENDTEXT";//直接显示各项数据

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

            //------------------------------  # 30個

            // 設定數列2 的 大小與外觀
            Series series2 = new Series("cos", 500);  // 初始化數列2(名稱, 最大值)
            series2.ChartType = SeriesChartType.Point;  // 點狀圖
            series2.Color = Color.Green; //設定線條顏色
            series2.BorderColor = Color.Navy;  //設置數據邊框的顏色
            series2.BorderWidth = 3;    //線寬
            series2.Font = series_font;
            series2.MarkerSize = 5;     //圖標大小
            series2.IsValueShownAsLabel = false;   //將數值顯示在線上 是否在Chart中顯示座標點值
            series2.LegendText = "cos";  // 圖例文字
            series2.Name = "cos";      //設置數據名稱
            //series2.ShadowOffset = 10;   //設置陰影偏移量
            //series2.ShadowColor = Color.Orange; //設置陰影顏色

            // 設定數列3 的 大小與外觀
            Series series3 = new Series("sin + cos", 500);  // 初始化數列3(名稱, 最大值)
            series3.ChartType = SeriesChartType.Point;  // 點狀圖
            series3.Color = Color.Blue; //設定線條顏色
            series3.BorderColor = Color.Navy;  //設置數據邊框的顏色
            series3.BorderWidth = 3;    //線寬
            series3.Font = series_font;
            series3.MarkerSize = 5;     //圖標大小
            series3.IsValueShownAsLabel = false;   //將數值顯示在線上 是否在Chart中顯示座標點值
            series3.LegendText = "sin + cos";  // 圖例文字
            series3.Name = "sine + cos";      //設置數據名稱
            //series3.ShadowOffset = 10;   //設置陰影偏移量
            //series3.ShadowColor = Color.Orange; //設置陰影顏色

            int[] array_xx = new int[37];
            int[] array_y1 = new int[37];
            int[] array_y2 = new int[37];
            int[] array_y3 = new int[37];

            for (int i = 0; i <= 360; i += 10)
            {
                array_xx[i / 10] = i;
                array_y1[i / 10] = (int)(110 * sind(i));
                array_y2[i / 10] = (int)(110 * cosd(i));
                array_y3[i / 10] = (int)(110 * sind(i) + 110 * cosd(i));
                series1.Points.AddXY(array_xx[i / 10], array_y1[i / 10]);    //將數值1新增至數列1
                series2.Points.AddXY(array_xx[i / 10], array_y2[i / 10]);    //將數值2新增至數列2
                series3.Points.AddXY(array_xx[i / 10], array_y3[i / 10]);    //將數值3新增至數列3
            }

            chart6.Series.Add(series1);  // 將數列1新增到圖表上
            chart6.Series.Add(series2);  // 將數列2新增到圖表上
            chart6.Series.Add(series3);  // 將數列3新增到圖表上

            print_series_data(series1, series2, series3);
        }

        void print_series_data(Series series1, Series series2, Series series3)
        {
            richTextBox1.Text += "顯示資料\n";
            int count = series1.Points.Count;  // 數列1內的資料個數
            //richTextBox1.Text += "共有 " + count.ToString() + " 筆資料\n";
            for (int i = 0; i < count; i++)
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
            string title = "雷達圖";
            chart_init(chart7, title);

            chart7.Titles.Clear();  // 清除所有標題
            chart7.Legends.Clear();  // 清除所有圖例

            // 設定數列1 的 大小與外觀
            Series series1 = chart7.Series.Add("雷達資料");
            series1.ChartArea = "ChartArea1";  // 設定要呈現的圖表區

            series1.ChartType = SeriesChartType.Radar;  // 雷達圖

            if (flag_show_radar_type == 0)
            {
                // 點的數值
                series1.Points.AddXY(1, 248);
                series1.Points.AddXY(2, 234);
                series1.Points.AddXY(3, 438);
                series1.Points.AddXY(4, 345);
                series1.Points.AddXY(1, 222);

                // 點的名稱
                series1.Points[0].Label = "A";
                series1.Points[1].Label = "B";
                series1.Points[2].Label = "C";
                series1.Points[3].Label = "D";
                series1.Points[4].Label = "E";
            }
            else
            {
                for (Int32 j = 0; j <= 72; j++)
                {
                    series1.Points.AddXY(5 * j, 5 + j % 9);
                }
            }
        }

        //------------------------------------------------------------  # 60個

        void draw_chart8()
        {
            //用滑鼠指線 顯示數值
            richTextBox1.Text += "用滑鼠指線 顯示數值\n";
            FillChart();
            this.tooltip.AutomaticDelay = 5;
        }

        private void FillChart()
        {
            string title = "用滑鼠指線 顯示數值";
            chart_init(chart8, title);

            string[] name = new string[] { "鼠", "牛", "虎", "兔", "龍" };
            int[] xx = new int[] { 0, 1, 2, 3, 4 };
            int[] weight = new int[] { 3, 48, 33, 8, 38 };

            // 設定數列1 的 大小與外觀
            Series series1 = new Series("體重1", 500);  // 初始化數列1(名稱，最大值)
            series1.ChartType = SeriesChartType.Line;  // 折線圖
            series1.Color = Color.Red;
            series1.XValueMember = "X";
            series1.YValueMembers = "Y";

            //------------------------------  # 30個

            // 設定數列2 的 大小與外觀
            Series series2 = new Series("體重2", 500);  // 初始化數列2(名稱，最大值)
            //series2.ChartType = SeriesChartType.Column;  // 直條圖
            //series2.ChartType = SeriesChartType.Line;  // 折線圖
            series2.ChartType = SeriesChartType.Point;  // 點狀圖
            series2.XValueMember = "X";
            series2.YValueMembers = "Y";
            series2.MarkerSize = 10;
            series2.MarkerStyle = MarkerStyle.Star5;

            for (int i = 0; i < xx.Length; i++)
            {
                series1.Points.AddXY(xx[i], weight[i]);  // AddXY 二維加入
                series2.Points.AddXY(xx[i], weight[i]);  // AddXY 二維加入
            }

            chart8.Series.Add(series1);  // 將數列1新增到圖表上
            chart8.Series.Add(series2);  // 將數列2新增到圖表上
        }

        Point? prevPosition = null;     //好奇怪的寫法?
        ToolTip tooltip = new ToolTip();
        private void chart8_MouseMove(object sender, MouseEventArgs e)
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
                var results = chart8.HitTest(pos.X, pos.Y, false, ChartElementType.DataPoint);
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
                                tooltip.Show("X=" + prop.XValue + ", Y=" + prop.YValues[0], this.chart8, pos.X, pos.Y - 15);
                            }
                        }
                    }
                }
            }
        }

        //------------------------------------------------------------  # 60個

        private void bt_chart6_Click(object sender, EventArgs e)
        {
            int x_st = 10;
            int y_st = 10;
            int dx = W + 10;
            int dy = H + 10;
            chart6.Size = new Size(W * 2, H * 2);
            chart6.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            chart6.BringToFront();

            W = 500 * 2;
            H = 310 * 2;

            draw_chart6();
        }

        //------------------------------------------------------------  # 60個

        private void bt_chart7_Click(object sender, EventArgs e)
        {
            if (flag_show_radar_type == 0)
            {
                flag_show_radar_type = 1;
            }
            else
            {
                flag_show_radar_type = 0;
            }
            draw_chart7();
        }

        //------------------------------------------------------------  # 60個

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
            draw_chart3();
        }

        private void bt_chart_type_Click(object sender, EventArgs e)
        {
            int x_st = 10;
            int y_st = 10;
            int dx = W + 10;
            int dy = H + 10;

            chart3.Size = new Size(W * 2 + 10, H * 2 + 10);  // 設定chart大小
            chart3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            chart3.BringToFront();
            groupBox1.Size = new Size(W * 2 + 10, H * 1);
            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox1.BringToFront();
            groupBox1.Visible = true;

            W = 500 * 2;
            H = 310 * 2;

            draw_chart3();
        }

        //6060

        private void bt_chart_save_Click(object sender, EventArgs e)
        {
            save_chart_image_to_drive(chart0);
        }

        void save_chart_image_to_drive(Chart chart1)
        {
            if (chart1 != null)
            {
                string filename = Application.StartupPath + "\\CHART_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                //String filename1 = filename + ".jpg";
                //String filename2 = filename + ".bmp";
                String filename3 = filename + ".png";

                try
                {
                    //chart1.SaveImage(@filename1, ChartImageFormat.Jpeg);
                    //chart1.SaveImage(@filename2, ChartImageFormat.Bmp);
                    chart1.SaveImage(@filename3, ChartImageFormat.Png);

                    richTextBox1.Text += "存檔成功, ";
                    //richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                    //richTextBox1.Text += "已存檔 : " + filename2 + "\n";
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

        //------------------------------------------------------------  # 60個
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/


// 設定調色板, 看不出效果
// chart0.Palette = ChartColorPalette.EarthTones;

/*
建立數列 與 加入到 chart, 使用後者
1.
建立數列並加入到chart
Series series1 = chart0.Series.Add("體重1");
Series series2 = chart0.Series.Add("體重2");
2.
建立數列
Series series1 = new Series("體重", 500);
加入chart
chart1.Series.Add(series1);  // 將數列1新增到圖表上
*/

//chart1.ChartAreas.Clear();  // 清除所有圖表區
//chart1.ChartAreas.Add("ChartArea1");  // 將圖表區1新增到圖表上
//chart1.ChartAreas[0]  //內建的圖表區

//chart1.Titles.Clear();  // 清除所有標題
//chart1.Titles.Add(chart_title);  // 將標題新增到圖表上

//chart1.Legends.Clear();  // 清除所有圖例
//chart1.Legends.Add("Legends1");  // 將圖例新增到圖表上

//chart1.Series.Clear();  // 清除所有數列
//chart1.Series.Add(series1);  // 將數列1新增到圖表上

//series1.Points.Clear();  // 清除數列1內的所有資料
//series1.Points.AddXY(xx, yy);  // 將資料新增到數列1裏
//series1.Points.Count      // 數列1內的資料個數

/*
共通
Form        表單
Chart       圖表
ChartAreas  圖表區
Titles      標題
Legends     圖例
Series      數列
*/

//series1.LegendText = "體重";  // 圖例文字

/*
Chart
隨意建立3組數據(Sin,Cos,Sin+Cos)
Chart 的屬性 / Series / 打開Series集合編輯器 / 原本有Series 1, 加入Series 2 Series 3
點選Series 1 Series 2 Series 3 把ChartType改成Spline    亦可修改線的粗細顏色等

Chart 的屬性
Title是在圖表上方增加標題 或著也可以想說說明圖表的文字,從屬性裡的Text可以修改文字,也可以修改字型大小位置等..
Legend是圖表右邊說明每一條線代表的文字,若不想要可以從Enabled改成False即可
ChartAreas是可以在同一圖表裡建立2種以上圖
從Series裡可以選擇哪一組數據要放在哪個ChartAreas上

//------------------------------------------------------------  # 60個

chart

http://kgood9999.blogspot.com/2010/04/c-chart.html
https://wayhome23.pixnet.net/blog/post/124267643-%5Bc%23%5D-chart-%E5%9F%BA%E7%A4%8E%E7%AF%87

chart放在
通用Silverlight控制項內

//------------------------------------------------------------  # 60個

*/

//數列加入資料點的方法
//series1.Points.AddXY(i, r.Next(10) * 50);
//objSeries.Points.DataBindXY(xx, yy);  // xx, yy 皆為一維陣列

