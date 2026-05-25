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

namespace vcs_Chart3
{
    public partial class Form1 : Form
    {
        int W = 500;
        int H = 310;

        bool flag_show_value = true;
        int flag_show_radar_type = 0;

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
            bt_chart6.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_chart6.BringToFront();
            bt_chart7.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            bt_chart7.BringToFront();

            richTextBox1.Size = new Size(275, 950);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1840, 1010);
            this.Text = "vcs_Chart3";

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

            chart1.Size = new Size(W, H);  // 設定chart大小
            chart1.Titles.Clear();  // 清除所有標題
            chart1.Legends.Clear();  // 清除所有圖例
            chart1.ChartAreas.Clear();  // 清除所有圖表區
            chart1.Series.Clear();  // 清除所有數列

           //------------------------------  # 30個

            // 畫標題的方法1
            Title chart_title = new Title();
            chart_title.Text = title;
            chart_title.Alignment = ContentAlignment.MiddleCenter;
            chart_title.Font = new Font("Trebuchet MS", 14F, FontStyle.Bold);
            chart1.Titles.Add(chart_title);  // 將標題新增到圖表上

            // 畫標題的方法2
            Title chart_title2 = new Title
            {
                Text = title,
                Alignment = ContentAlignment.MiddleCenter,
                Font = new Font("Trebuchet MS", 14F, FontStyle.Bold)
            };
            //chart1.Titles.Add(chart_title2);  // 將標題新增到圖表上

            //------------------------------  # 30個

            // 設定圖例.Legends
            chart1.Legends.Add("Legends1");  // 將圖例新增到圖表上

            //設定 Legends
            //chart1.Legends["Legends1"].DockedToChartArea = ChartArea1;  // 設定圖例要顯示在哪個圖表區
            chart1.Legends["Legends1"].Docking = Docking.Right;  // 設定圖例的顯示位置, 預設靠右
            //背景色
            chart1.Legends["Legends1"].BackColor = Color.FromArgb(235, 235, 235);
            //斜線背景
            chart1.Legends["Legends1"].BackHatchStyle = ChartHatchStyle.DarkDownwardDiagonal;
            chart1.Legends["Legends1"].BorderWidth = 1;
            chart1.Legends["Legends1"].BorderColor = Color.FromArgb(200, 200, 200);

            //------------------------------  # 30個
            //圖表區設定
            ChartArea chartarea = new ChartArea("ChartArea1");
            chart1.ChartAreas.Add(chartarea);  // 將圖表區新增到圖表上

            chartarea.BackColor = Color.Pink;  // 圖表區背景色
            chartarea.AxisX.MajorGrid.LineColor = Color.Red;  // X軸主格線顏色

            chartarea.AxisY.MajorGrid.LineColor = Color.Green;  // Y軸主格線顏色
            chartarea.AxisY.MajorGrid.Enabled = true;  // 顯示Y軸主格線
            chartarea.AxisY.Enabled = AxisEnabled.True; // 啟動Y軸標示

            chartarea.AxisX.Title = "種類";  // 設定X軸的標題
            chartarea.AxisY.Title = "體重(公斤)";  //設定Y軸的標題

            /*
            // 設定邊界
            chartarea.AxisX.Minimum = 0;  // 設定X軸最小值
            chartarea.AxisX.Maximum = 20;  // 設定X軸最大值
            chartarea.AxisY.Minimum = 0;  // 設定Y軸最小值
            chartarea.AxisY.Maximum = 100;  // 設定Y軸最大值
            */

            //chartarea.AxisX.CustomLabels.Clear();

            //chartarea.AxisX.Interval = 1;  // 設定X軸坐標的間隔

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
        }

        void draw_chart0()
        {
            string title = "直條圖 + 折線圖";
            chart_init(chart0, title);

            //------------------------------  # 30個

            // 設定數列1 的 大小與外觀
            Series series1 = new Series("體重1");
            series1.ChartType = SeriesChartType.Column;  // 直條圖

            series1.Points.AddXY("鼠", 3);
            series1.Points.AddXY("牛", 48);
            series1.Points.AddXY("虎", 33);
            series1.Points.AddXY("兔", 8);
            series1.Points.AddXY("龍", 38);
            series1.Points.AddXY("蛇", 16);
            series1.Points.AddXY("馬", 31);
            series1.Points.AddXY("羊", 29);
            series1.Points.AddXY("猴", 22);
            series1.Points.AddXY("雞", 5);
            series1.Points.AddXY("狗", 17);
            series1.Points.AddXY("豬", 42);

            Random rnd = new Random();  //亂數產生區塊顏色
            int count = series1.Points.Count;  // 數列1內的資料個數
            richTextBox1.Text += "共有 " + count.ToString() + " 筆資料\n";
            for (int i = 0; i < count; i++)
            {
                series1.Points[i].BorderColor = Color.Red;  // 邊框顏色 for 直條圖
                series1.Points[i].Color = Color.FromArgb(150, rnd.Next(0, 255), rnd.Next(0, 255), rnd.Next(0, 255));
                //richTextBox1.Text += "X[" + i.ToString() + "] = " + series1.Points[i].XValue.ToString() + "\t";
                //richTextBox1.Text += "Y[" + i.ToString() + "] = " + series1.Points[i].YValues[0].ToString() + "\n";
            }

            chart0.Series.Add(series1);  // 將數列1新增到chart0上

            //------------------------------  # 30個

            // 設定數列2 的 大小與外觀
            Series series2 = new Series("體重2", 500);  // 初始化數列2(名稱，最大值)
            series2.ChartType = SeriesChartType.Line;  // 折線圖
            series2.Color = Color.Red; // 設定線條顏色
            series2.BorderWidth = 5;  // 折線圖線寬
            //series2.Name = "體重";  // 數列名稱
            //series2.Font = new Font("新細明體", 10); //設定字型
            //series2.IsValueShownAsLabel = true;  // 是否把數值顯示在線上

            string[] name = new string[] { "鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬" };
            int[] weight = new int[] { 3, 48, 33, 8, 38, 16, 31, 29, 22, 5, 17, 42 };

            for (int i = 0; i < name.Length; i++)
            {
                //series2.Points.Add(weight[i]);  // Add 一維加入
                series2.Points.AddXY(name[i], weight[i]);  // AddXY 二維加入
            }

            chart0.Series.Add(series2);  // 將數列2新增到chart0上
        }

        void draw_chart1()
        {
            string title = "直條圖";
            chart_init(chart1, title);

            //------------------------------  # 30個

            // 設定數列1 的 大小與外觀
            Series series1 = new Series("體重", 500);  // 初始化數列1(名稱, 最大值)
            series1.ChartType = SeriesChartType.Column;  // 直條圖
            series1.Color = Color.Blue; // 設定線條顏色
            series1.Font = new Font("新細明體", 10); //設定字型            
            series1.IsValueShownAsLabel = true;  // 是否把數值顯示在線上

            //把值加入X 軸Y 軸
            series1.Points.AddXY("鼠", 3);
            series1.Points.AddXY("牛", 48);
            series1.Points.AddXY("虎", 33);
            series1.Points.AddXY("兔", 8);
            series1.Points.AddXY("龍", 38);
            series1.Points.AddXY("蛇", 16);
            series1.Points.AddXY("馬", 31);
            series1.Points.AddXY("羊", 29);
            series1.Points.AddXY("猴", 22);
            series1.Points.AddXY("雞", 5);
            series1.Points.AddXY("狗", 17);
            series1.Points.AddXY("豬", 42);

            chart1.Series.Add(series1);  // 將數列1新增到圖表上
        }

        void draw_chart2()
        {
            string title = "長條圖, 自定義座標軸刻度標籤";
            chart_init(chart2, title);

            // 設定數列1
            Series series1 = new Series("體重1");  // 初始化數列1
            series1.Points.AddXY("鼠", 3);
            series1.Points.AddXY("牛", 48);
            series1.Points.AddXY("虎", 33);
            series1.Points.AddXY("兔", 8);
            series1.Points.AddXY("龍", 38);
            series1.Points.AddXY("蛇", 16);
            series1.Points.AddXY("馬", 31);
            series1.Points.AddXY("羊", 29);
            series1.Points.AddXY("猴", 22);
            series1.Points.AddXY("雞", 5);
            series1.Points.AddXY("狗", 17);
            series1.Points.AddXY("豬", 42);

            chart2.Series.Add(series1);  // 將數列1新增到圖表上

            //------------------------------  # 30個

            // 設定數列2
            Series series2 = new Series("體重2");  // 初始化數列2
            series2.Points.AddXY("鼠", 3);
            series2.Points.AddXY("牛", 48);
            series2.Points.AddXY("虎", 33);
            series2.Points.AddXY("兔", 8);
            series2.Points.AddXY("龍", 38);
            series2.Points.AddXY("蛇", 16);
            series2.Points.AddXY("馬", 31);
            series2.Points.AddXY("羊", 29);
            series2.Points.AddXY("猴", 22);
            series2.Points.AddXY("雞", 5);
            series2.Points.AddXY("狗", 17);
            series2.Points.AddXY("豬", 42);

            chart2.Series.Add(series2);  // 將數列2新增到圖表上
        }

        void draw_chart3()
        {
            string title = "圓形圖";
            chart_init(chart3, title);

            string[] name = new string[] { "鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬" };
            int[] weight = new int[] { 3, 48, 33, 8, 38, 16, 31, 29, 22, 5, 17, 42 };

            Series series1 = new Series("體重", 500);  // 初始化數列1
            series1.ChartType = SeriesChartType.Pie;  // 圓形圖
            //series1.ChartType = SeriesChartType.Doughnut;  // 環圈圖
            series1.IsValueShownAsLabel = true;  // 是否把數值顯示在線上

            series1.Points.DataBindXY(name, weight);  // xx, yy 皆為一維陣列

            //series1.LegendText = "體重";   //#VALX:    [ #PERCENT{P1} ]; //X軸 + 百分比
            //series1.Label = "bbbb";  //#VALX#PERCENT{P1}; //X軸 + 百分比
            series1.LabelForeColor = Color.Red; //字體顏色
            //字體設定
            series1.Font = new System.Drawing.Font("Trebuchet MS", 10, System.Drawing.FontStyle.Bold);
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

            chart3.Series.Add(series1);  // 將數列1新增到圖表上
        }

        void draw_chart4()
        {
            string title = "各區比例";
            chart_init(chart4, title);

            string[] name = { "AAA", "BBB", "CCC", "DDD", "EEE" };
            int[] weight = { 137, 63, 87, 98, 74 };

            //ChartAreas, Legends 基本設定
            if (chart4.Legends.FindByName("Legends1") == null) //如果chart4沒有包含Legends2才將其Add
            {
                // 設定圖例.Legends
                chart4.Legends.Add(new Legend("Legends1"));  // 將圖例新增到圖表上
            }
            //chart4.ChartAreas.Add("ChartArea1");  // 將圖表區2新增到圖表上

            //設定 ChartArea1
            //設定3D
            chart4.ChartAreas["ChartArea1"].Area3DStyle.Enable3D = true;  // 設定圖表區3D顯示
            chart4.ChartAreas["ChartArea1"].Area3DStyle.IsClustered = true; //並排顯示
            chart4.ChartAreas["ChartArea1"].Area3DStyle.Rotation = 40; //垂直角度
            chart4.ChartAreas["ChartArea1"].Area3DStyle.Inclination = 50; //水平角度
            chart4.ChartAreas["ChartArea1"].Area3DStyle.PointDepth = 10; //數據條厚度
            chart4.ChartAreas["ChartArea1"].Area3DStyle.WallWidth = 0; //外牆寬度
            chart4.ChartAreas["ChartArea1"].Area3DStyle.LightStyle = LightStyle.Realistic; //光源

            // 設定標題2
            chart4.Titles.Add("Title1");  // 將標題新增到圖表上
            chart4.Titles["Title1"].DockedToChartArea = "ChartArea1";  // 設定標題要顯示在哪個圖表區
            chart4.Titles["Title1"].IsDockedInsideChartArea = false; //設定顯示在圖表的內外部
            chart4.Titles["Title1"].Text = "各區比例";

            // 設定圖例.Legends
            chart4.Legends["Legends1"].DockedToChartArea = "ChartArea1";  // 設定圖例要顯示在哪個圖表區
            chart4.Legends["Legends1"].IsDockedInsideChartArea = false; //設定要顯示在圖表的內外部
            chart4.Legends["Legends1"].Docking = Docking.Right;  // 設定圖例的顯示位置, 預設靠右
            chart4.Legends["Legends1"].BackColor = Color.FromArgb(235, 235, 235);
            chart4.Legends["Legends1"].BackHatchStyle = ChartHatchStyle.DarkDownwardDiagonal;
            chart4.Legends["Legends1"].BorderWidth = 1;
            chart4.Legends["Legends1"].BorderColor = Color.FromArgb(200, 200, 200);

            // 設定數列1 的 大小與外觀
            Series series1 = new Series("體重1");
            series1.ChartType = SeriesChartType.Pie;  // 圓形圖
            series1.ChartArea = "ChartArea1";  // 設定要呈現的ChartArea
            //series1.ChartType = SeriesChartType.Doughnut;  // 環圈圖
            series1.Points.DataBindXY(name, weight);  // xx, yy 皆為一維陣列
            series1.Legend = "Legends1";  // 設定要呈現哪個圖例
            // series1.IsValueShownAsLabel = true;  // 是否把數值顯示在線上
            series1.XValueType = ChartValueType.String; //X軸的資料格式
            series1.LegendText = "#VALX :[ #PERCENT{P1} ]"; //X軸 + 百分比
            series1.Label = "#VALX\n#PERCENT{P1}"; //X軸 + 百分比
            //series1.LabelForeColor = Color.FromArgb(0, 90, 255); //字體顏色

            //字體設定
            series1.Font = new Font("Trebuchet MS", 10, FontStyle.Bold);
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

            chart4.Series.Add(series1);  // 將數列1新增到圖表上
        }

        void draw_chart5()
        {
            string title = "各縣市統計";
            chart_init(chart5, title);

            List<String> name = new List<string>
            {
                "宜蘭縣",
                "花蓮縣",
                "南投縣",
                "屏東縣",
                "苗栗縣",
                "桃園市",
                "高雄市",
                "基隆市",
                "雲林縣",
                "新北市",
                "新竹市",
                "澎湖縣"
        };

            double[] weight = { 20, 19, 64, 128, 8, 48, 58, 21, 18, 27, 17, 11 };

            //設定 ChartArea1
            chart5.ChartAreas["ChartArea1"].AxisX.Interval = 1;  // 設定X軸坐標的間隔
            chart5.ChartAreas["ChartArea1"].AxisX.IntervalOffset = 1;  //設置X軸坐標偏移為1
            chart5.ChartAreas["ChartArea1"].AxisX.LabelStyle.IsStaggered = true;   //設置是否交錯顯示,比如數據多的時間分成兩行來顯示
            chart5.ChartAreas["ChartArea1"].AxisX.Title = "縣市";  // 設定X軸的標題
            chart5.ChartAreas["ChartArea1"].AxisY.Title = "人數";  //設定Y軸的標題
            chart5.ChartAreas["ChartArea1"].BackColor = Color.FromArgb(240, 240, 240); //背景色
            chart5.ChartAreas["ChartArea1"].AxisX.Enabled = AxisEnabled.True;
            chart5.ChartAreas["ChartArea1"].AxisX2.Enabled = AxisEnabled.False; //隱藏 X2 標示
            chart5.ChartAreas["ChartArea1"].AxisY2.Enabled = AxisEnabled.False; //隱藏 Y2 標示
            chart5.ChartAreas["ChartArea1"].AxisY2.MajorGrid.Enabled = false;   //隱藏 Y2 軸線
            chart5.ChartAreas["ChartArea1"].AxisX.MajorGrid.LineColor = Color.FromArgb(150, 150, 150);//X 軸線顏色
            chart5.ChartAreas["ChartArea1"].AxisY.MajorGrid.LineColor = Color.FromArgb(150, 150, 150);//Y 軸線顏色
            chart5.ChartAreas["ChartArea1"].AxisY.LabelStyle.Format = "#.###";//設定小數點

            //設定3D
            chart5.ChartAreas["ChartArea1"].Area3DStyle.Enable3D = true;  // 設定圖表區3D顯示
            chart5.ChartAreas["ChartArea1"].Area3DStyle.IsClustered = true; //並排顯示
            chart5.ChartAreas["ChartArea1"].Area3DStyle.Rotation = 40; //垂直角度
            chart5.ChartAreas["ChartArea1"].Area3DStyle.Inclination = 50; //水平角度
            chart5.ChartAreas["ChartArea1"].Area3DStyle.PointDepth = 10; //數據條厚度
            chart5.ChartAreas["ChartArea1"].Area3DStyle.WallWidth = 0; //外牆寬度
            chart5.ChartAreas["ChartArea1"].Area3DStyle.LightStyle = LightStyle.Realistic; //光源

            // 設定標題1, Title1, 設定要顯示在哪個圖表
            chart5.Titles["Title1"].DockedToChartArea = "ChartArea1";  // 設定標題要顯示在哪個圖表區
            chart5.Titles["Title1"].IsDockedInsideChartArea = false;  // 設定要顯示在圖表的內外部

            // 設定圖例.Legends
            chart5.Legends["Legends1"].DockedToChartArea = "ChartArea1";  // 設定圖例要顯示在哪個圖表區
            chart5.Legends["Legends1"].Docking = Docking.Right;  // 設定圖例的顯示位置, 預設靠右
            chart5.Legends["Legends1"].BackColor = Color.FromArgb(235, 235, 235); //背景色
            chart5.Legends["Legends1"].BackHatchStyle = ChartHatchStyle.DarkDownwardDiagonal;
            chart5.Legends["Legends1"].BorderWidth = 1;
            chart5.Legends["Legends1"].BorderColor = Color.FromArgb(200, 200, 200);

            // 設定數列1 的 大小與外觀
            Series series1 = new Series("體重1");
            series1.ChartType = SeriesChartType.Pie;  // 圓形圖
            series1.ChartType = SeriesChartType.Column; //直條圖(Column),折線圖(Line),橫條圖(Bar)

            //設定 Series1
            series1.ChartArea = "ChartArea1";  // 設定要呈現的圖表區
            series1.Points.DataBindXY(name, weight);//Series1的XY數值放入圖中  // xx, yy 皆為一維陣列
            series1.Legend = "Legends1";  // 設定要呈現哪個圖例
            series1.LegendText = "體重1";  // 設定圖例文字
            series1.LabelFormat = "#.###"; //小數點
            series1.MarkerSize = 8; //Label 範圍大小
            series1.LabelForeColor = Color.FromArgb(0, 90, 255); //字體顏色

            //字體設定
            series1.Font = new Font("Trebuchet MS", 10, FontStyle.Bold);

            //Label 背景色
            series1.LabelBackColor = Color.FromArgb(150, 255, 255, 255);
            series1.Color = Color.FromArgb(240, 65, 140, 240); //背景色
            series1.IsValueShownAsLabel = true;  // 是否把數值顯示在線上

            chart5.Series.Add(series1);  // 將數列1新增到圖表上

            //------------------------------  # 30個

            // 設定數列2 的 大小與外觀
            Series series2 = new Series("體重2");
            series2.ChartType = SeriesChartType.Pie;  // 圓形圖
            series2.ChartType = SeriesChartType.Column; //直條圖(Column),折線圖(Line),橫條圖(Bar)

            series2.Points.DataBindXY(name, weight);  // xx, yy 皆為一維陣列
            series2.Legend = "Legends1";
            series2.LegendText = "體重2";
            series2.LabelFormat = "#.###"; //小數點
            series2.MarkerSize = 8; //Label 範圍大小
            series2.LabelForeColor = Color.FromArgb(255, 103, 0);
            series2.Font = new Font("Trebuchet MS", 10, FontStyle.Bold);
            series2.LabelBackColor = Color.FromArgb(150, 255, 255, 255);
            series2.Color = Color.FromArgb(240, 252, 180, 65); //背景色
            series2.IsValueShownAsLabel = true;  // 是否把數值顯示在線上

            chart5.Series.Add(series2);  // 將數列2新增到圖表上
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

            chart6.Size = new Size(W, H);  // 設定chart大小

            // 畫標題的方法1
            Title chart_title = new Title();
            chart_title.Text = title;
            chart_title.Alignment = ContentAlignment.MiddleCenter;
            chart_title.Font = new Font("標楷體", 24F, FontStyle.Bold);
            chart6.Titles.Add(chart_title);  // 將標題新增到圖表上

            // 畫標題的方法2
            Title chart_title2 = new Title
            {
                Text = title,
                Alignment = ContentAlignment.MiddleCenter,
                Font = new Font("Trebuchet MS", 14F, FontStyle.Bold)
            };
            //chart6.Titles.Add(chart_title2);  // 將標題新增到圖表上

            //圖表區設定, X軸
            chart6.ChartAreas[0].AxisX.Minimum = 0;  // 設定X軸最小值
            chart6.ChartAreas[0].AxisX.Maximum = 360;  // 設定X軸最大值
            chart6.ChartAreas[0].AxisX.Title = "角度";  // 設定X軸名稱
            chart6.ChartAreas[0].AxisX.TitleForeColor = Color.Blue;  // 設定X軸名稱的字體顏色
            chart6.ChartAreas[0].AxisX.Enabled = AxisEnabled.True;  // 顯示 或 隱藏 X 軸標示
            chart6.ChartAreas[0].AxisX.MajorGrid.Enabled = true;  // 顯示 或 隱藏 X 軸標線
            chart6.ChartAreas[0].AxisX.LabelStyle.Font = new Font("Trebuchet MS", 15, FontStyle.Bold);  // 設定X軸刻度的字型
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
            chart6.ChartAreas[0].AxisY.LabelStyle.Font = new Font("Trebuchet MS", 8.25F, FontStyle.Bold);  // 設置Y軸左側的提示信息的字體屬性
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
            chart6.Legends["Legend1"].Docking = Docking.Right;  // 設定圖例的顯示位置, 預設靠右

            //------------------------------  # 30個

            // 設定數列1 的 大小與外觀
            Series series1 = new Series("sin", 500);  // 初始化數列1(名稱, 最大值)
            series1.ChartType = SeriesChartType.Point;  // 點狀圖
            series1.Color = Color.Red; //設定線條顏色
            series1.BorderColor = Color.Navy;  //設置數據邊框的顏色
            series1.BorderWidth = 3;    //線寬
            series1.Font = new Font("新細明體", 10); //設定字型
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
            Series series2 = new Series("cos", 500);  // 初始化數列1(名稱, 最大值)
            series2.ChartType = SeriesChartType.Point;  // 點狀圖
            series2.Color = Color.Green; //設定線條顏色
            series2.BorderColor = Color.Navy;  //設置數據邊框的顏色
            series2.BorderWidth = 3;    //線寬
            series2.Font = new Font("標楷體", 12); //設定字型
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
            series3.Font = new Font("標楷體", 12); //設定字型
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

            richTextBox1.Text += "顯示資料\n";
            int count = series1.Points.Count;  // 數列1內的資料個數
            richTextBox1.Text += "共有 " + count.ToString() + " 筆資料\n";
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

            chart7.ChartAreas.Clear();

            ChartArea area = chart7.ChartAreas.Add("NewArea");

            // 設定數列1 的 大小與外觀
            Series series1 = chart7.Series.Add("雷達資料");
            series1.ChartArea = "NewArea";
            series1.ChartType = SeriesChartType.Radar;  // 雷達圖
            area.AxisY.LineColor = Color.Red;
            area.AxisY.LineWidth = 1;

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

            string[] name = new string[] { "鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬" };
            int[] xx = new int[] { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 };
            int[] weight = new int[] { 3, 48, 33, 8, 38, 16, 31, 29, 22, 5, 17, 42 };

            // 設定數列1 的 大小與外觀
            Series series1 = new Series("體重1", 500);  // 初始化數列2(名稱，最大值)
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
            {
                richTextBox1.Text += "無圖可存\n";
            }
        }
*/



//chart5.ChartAreas.Add("ChartArea1");  // 將圖表區1新增到圖表上
//chart5.ChartAreas.Add("ChartArea1");  // 將圖表區1新增到圖表上

