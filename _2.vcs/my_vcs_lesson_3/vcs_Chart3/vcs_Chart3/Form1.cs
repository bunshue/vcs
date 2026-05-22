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

/*
拉一個Chart控件

chart4屬性
Series 加 Series4a 和 Series4a
Titles 加 Title1 Title2
*/

/*
拉一個Chart控件

chart5屬性
ChartAreas 移除 ChartArea1
Series 移除 Series1
*/

namespace vcs_Chart3
{
    public partial class Form1 : Form
    {
        int W = 500;
        int H = 310;
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
            // 清除圖表
            chart1.Series.Clear();
            chart1.Titles.Clear();

            chart1.Titles.Add(title);  // 標題
            chart1.Size = new Size(W, H);  // 設定chart大小

        }

        void draw_chart0()
        {
            string title = "直條圖 Total Income";
            chart_init(chart0, title);

            // 設定數列1 的 大小與外觀
            Series series1 = chart0.Series.Add("平均高溫​℃");
            series1.ChartType = SeriesChartType.Column;  // 直條圖
            //series1.ChartType = SeriesChartType.Line;  // 折線圖

            // 設定數列2 的 大小與外觀
            Series series2 = chart0.Series.Add("平均低溫​℃");
            series2.ChartType = SeriesChartType.Column;  // 直條圖
            //series2.ChartType = SeriesChartType.Line;  // 折線圖

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

            for (int i = 0; i < 12; i++)
            {
                series1.Points.AddXY(month[i], temperature_average_high[i]);
                series2.Points.AddXY(month[i], temperature_average_low[i]);
            }
        }

        void draw_chart1()
        {
            // 直條圖

            string title = "直條圖 Animals";
            chart_init(chart1, title);

            // Data arrays
            string[] seriesArray = { "Cat", "Dog", "Bird", "Monkey" };
            int[] pointsArray = { 2, 1, 7, 5 };

            // Set palette
            chart1.Palette = ChartColorPalette.EarthTones;

            // Add series.
            for (int i = 0; i < seriesArray.Length; i++)
            {
                // 設定數列i 的 大小與外觀
                Series series = chart1.Series.Add(seriesArray[i]);
                series.Points.Add(pointsArray[i]);
            }
        }

        void draw_chart2()
        {
            string title = "長條圖, 自定義座標軸刻度標籤";
            chart_init(chart2, title);

            chart2.ChartAreas[0].AxisX.CustomLabels.Clear();

            //不知道如何自動邊界

            // 設定數列1
            Series series1 = new Series();
            // 設定數列2
            Series series2 = new Series();

            Random r = new Random();
            for (int i = 1; i < 13; i++)
            {
                series1.Points.AddXY(i, r.Next(20, 30));
                series2.Points.AddXY(i, r.Next(10, 30));
            }

            // 將數列新增到chart上
            chart2.Series.Add(series1);
            chart2.Series.Add(series2);

            chart2.ChartAreas[0].AxisX.MajorGrid.LineColor = Color.Green;

            DateTime dt = DateTime.Parse("8:30");
            for (int i = 1; i < 26; i++)
            {
                if (i % 2 == 1)
                {
                    CustomLabel label = new CustomLabel();
                    label.Text = dt.ToShortTimeString();
                    label.ToPosition = i;
                    chart2.ChartAreas[0].AxisX.CustomLabels.Add(label);
                    label.GridTicks = GridTickTypes.Gridline;
                    dt = dt.AddHours(1);
                }
            }
        }

        void draw_chart3()
        {
            string title = "";
            chart_init(chart3, title);

            // 設定數列1 的 大小與外觀
            Series series1 = new Series("Di0", 500); //初始畫線條(名稱，最大值)
            series1.Color = Color.Blue; //設定線條顏色
            series1.Font = new System.Drawing.Font("新細明體", 10); //設定字型
            series1.ChartType = SeriesChartType.Column;  // 直條圖
            //chart3.ChartAreas[0].AxisY.Minimum = 0;//設定Y軸最小值
            //chart3.ChartAreas[0].AxisY.Maximum = 500;//設定Y軸最大值
            //chart3.ChartAreas[0].AxisY.Enabled= AxisEnabled.False; //隱藏Y 軸標示
            //chart3.ChartAreas[0].AxisY.MajorGrid.Enabled= true;  //隱藏Y軸標線
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
            chart3.ChartAreas[0].AxisX.Minimum = 0;//設定Y軸最小值
            chart3.ChartAreas[0].AxisX.Maximum = 8;//設定Y軸最大值
            chart3.ChartAreas[0].AxisY.Minimum = 0;//設定Y軸最小值
            chart3.ChartAreas[0].AxisY.Maximum = 400;//設定Y軸最大值

            // 將數列新增到chart上
            chart3.Series.Add(series1);
        }

        void draw_chart4()
        {
            // 清除圖表
            //chart4.Series.Clear();
            //chart4.Titles.Clear();

            string[] xValues = { "北部", "中部", "南部", "東部", "離島" };
            int[] yValues = { 137, 163, 237, 48, 4 };

            //ChartAreas, Series, Legends 基本設定
            if (chart4.Legends.FindByName("Legends2") == null) //如果chart4沒有包含Legends2才將其Add
            {
                chart4.Legends.Add(new Legend("Legends2")); //圖例集合說明
            }
            chart4.ChartAreas.Add("ChartArea2");  // 圖表區域集合
            // chart4.Series.Add("Series3");  // 數據序列集合
            // chart4.Legends.Add("Legends2");  // 圖例集合

            //標題集合
            Title Title2 = new Title
            {
                Text = "各區域發生婦幼被害犯罪件數統計比例圖",
                Alignment = ContentAlignment.MiddleCenter,
                Font = new Font("Trebuchet MS", 14F, FontStyle.Bold)
            };
            chart4.Titles.Add(Title2);

            //設定 ChartArea2
            //設定3D
            chart4.ChartAreas["ChartArea2"].Area3DStyle.Enable3D = true; //3D效果
            chart4.ChartAreas["ChartArea2"].Area3DStyle.IsClustered = true; //並排顯示
            chart4.ChartAreas["ChartArea2"].Area3DStyle.Rotation = 40; //垂直角度
            chart4.ChartAreas["ChartArea2"].Area3DStyle.Inclination = 50; //水平角度
            chart4.ChartAreas["ChartArea2"].Area3DStyle.PointDepth = 10; //數據條厚度
            chart4.ChartAreas["ChartArea2"].Area3DStyle.WallWidth = 0; //外牆寬度
            chart4.ChartAreas["ChartArea2"].Area3DStyle.LightStyle = LightStyle.Realistic; //光源

            // 設定Title2
            chart4.Titles["Title2"].DockedToChartArea = "ChartArea2"; //設定標題停駐的ChartArea
            chart4.Titles["Title2"].IsDockedInsideChartArea = false; //設定顯示在圖表的內外部

            //設定 Legends2
            chart4.Legends["Legends2"].DockedToChartArea = "ChartArea2"; //設定要顯示在哪個圖表
            chart4.Legends["Legends2"].IsDockedInsideChartArea = false; //設定要顯示在圖表的內外部
            //chart4.Legends["Legends2"].Docking = Docking.Bottom; //自訂顯示位置

            //背景色
            chart4.Legends["Legends2"].BackColor = Color.FromArgb(235, 235, 235);

            //斜線背景
            chart4.Legends["Legends2"].BackHatchStyle = ChartHatchStyle.DarkDownwardDiagonal;
            chart4.Legends["Legends2"].BorderWidth = 1;
            chart4.Legends["Legends2"].BorderColor = Color.FromArgb(200, 200, 200);

            //設定 Series4b
            chart4.Series["Series4b"].ChartArea = "ChartArea2";  // 設定要呈現的ChartArea
            chart4.Series["Series4b"].ChartType = SeriesChartType.Pie;  // 圓形圖
            //chart4.Series["Series4b"].ChartType = SeriesChartType.Doughnut;  // 環圈圖
            chart4.Series["Series4b"].Points.DataBindXY(xValues, yValues);  // xx, yy 皆為一維陣列
            chart4.Series["Series4b"].Legend = "Legends2";  // 設定要呈現哪個圖例
            // chart4.Series["Series4b"].IsValueShownAsLabel = true; // Show data points labels
            chart4.Series["Series4b"].XValueType = ChartValueType.String; //X軸的資料格式
            chart4.Series["Series4b"].LegendText = "#VALX :[ #PERCENT{P1} ]"; //X軸 + 百分比
            chart4.Series["Series4b"].Label = "#VALX\n#PERCENT{P1}"; //X軸 + 百分比
            //chart4.Series["Series4b"].LabelForeColor = Color.FromArgb(0, 90, 255); //字體顏色

            //字體設定
            chart4.Series["Series4b"].Font = new Font("Trebuchet MS", 10, FontStyle.Bold);
            chart4.Series["Series4b"].Points.FindMaxByValue().LabelForeColor = Color.Red; //設定特定數字之字體
            //chart4.Series["Series4b"].Points.FindMaxByValue().Color = Color.Red; //設定數值最大的餅的顏色
            //chart4.Series["Series4b"].Points.FindMaxByValue()["Exploded"] = "true";  // 設定數值最大的餅是否分離出去
            chart4.Series["Series4b"].BorderColor = Color.FromArgb(255, 101, 101, 101);
            //chart4.Series["Series4b"]["DoughnutRadius"] = "80"; // ChartType為Doughnut時，Set Doughnut hole size
            //chart4.Series["Series4b"]["PieLabelStyle"] = "Inside"; //數值顯示在圓餅內
            chart4.Series["Series4b"]["PieLabelStyle"] = "Outside"; //數值顯示在圓餅外
            //chart4.Series["Series4b"]["PieLabelStyle"] = "Disabled"; //不顯示數值

            //設定圓餅效果，除 Default 外其他效果3D不適用
            //chart4.Series["Series4b"]["PieDrawingStyle"] = "Default";
            //chart4.Series["Series4b"]["PieDrawingStyle"] = "SoftEdge";
            //chart4.Series["Series4b"]["PieDrawingStyle"] = "Concave";

            //Random rnd = new Random();  //亂數產生區塊顏色
            //foreach (DataPoint point in chart4.Series["Series4b"].Points)
            //{
            //    //pie 顏色
            //    point.Color = Color.FromArgb(150, rnd.Next(0, 255), rnd.Next(0, 255), rnd.Next(0, 255)); 
            //}
        }

        void draw_chart5()
        {
            string title = "";
            chart_init(chart5, title);

            // 清除圖表
            chart5.ChartAreas.Clear();
            chart5.Legends.Clear();

            List<String> xValue = new List<string>
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
                "新竹縣",
                "嘉義市",
                "嘉義縣",
                "彰化縣",
                "臺中市",
                "臺北市",
                "臺東縣",
                "臺南市",
                "澎湖縣"
        };

            string[] titleArr = { "件數" };
            double[] yValues = { 20, 19, 64, 128, 8, 48, 58, 21, 18, 27, 17, 11, 4, 24, 23, 58, 5, 9, 23, 4 };

            chart5.ChartAreas.Add("ChartArea1");  // 圖表區域集合
            chart5.Series.Add("Series1");  // 數據序列集合
            chart5.Legends.Add("Legends1");  // 圖例集合

            // 標題集合
            Title Title1 = new Title
            {
                Text = "各縣市發生婦幼被害犯罪件數統計",
                Alignment = ContentAlignment.MiddleCenter,
                Font = new Font("Trebuchet MS", 14F, FontStyle.Bold)
            };
            chart5.Titles.Add(Title1);

            //設定 ChartArea1
            chart5.ChartAreas["ChartArea1"].AxisX.Interval = 1;   //設置X軸坐標的間隔為1
            chart5.ChartAreas["ChartArea1"].AxisX.IntervalOffset = 1;  //設置X軸坐標偏移為1
            chart5.ChartAreas["ChartArea1"].AxisX.LabelStyle.IsStaggered = true;   //設置是否交錯顯示,比如數據多的時間分成兩行來顯示
            chart5.ChartAreas["ChartArea1"].AxisX.Title = "縣市"; //設定X軸的標題
            chart5.ChartAreas["ChartArea1"].AxisY.Title = "人數"; //設定Y軸的標題
            chart5.ChartAreas["ChartArea1"].BackColor = Color.FromArgb(240, 240, 240); //背景色
            chart5.ChartAreas["ChartArea1"].AxisX.Enabled = AxisEnabled.True;
            chart5.ChartAreas["ChartArea1"].AxisX2.Enabled = AxisEnabled.False; //隱藏 X2 標示
            chart5.ChartAreas["ChartArea1"].AxisY2.Enabled = AxisEnabled.False; //隱藏 Y2 標示
            chart5.ChartAreas["ChartArea1"].AxisY2.MajorGrid.Enabled = false;   //隱藏 Y2 軸線
            chart5.ChartAreas["ChartArea1"].AxisX.MajorGrid.LineColor = Color.FromArgb(150, 150, 150);//X 軸線顏色
            chart5.ChartAreas["ChartArea1"].AxisY.MajorGrid.LineColor = Color.FromArgb(150, 150, 150);//Y 軸線顏色
            chart5.ChartAreas["ChartArea1"].AxisY.LabelStyle.Format = "#.###";//設定小數點

            //設定3D
            chart5.ChartAreas["ChartArea1"].Area3DStyle.Enable3D = true; //3D效果
            chart5.ChartAreas["ChartArea1"].Area3DStyle.IsClustered = true; //並排顯示
            chart5.ChartAreas["ChartArea1"].Area3DStyle.Rotation = 40; //垂直角度
            chart5.ChartAreas["ChartArea1"].Area3DStyle.Inclination = 50; //水平角度
            chart5.ChartAreas["ChartArea1"].Area3DStyle.PointDepth = 10; //數據條厚度
            chart5.ChartAreas["ChartArea1"].Area3DStyle.WallWidth = 0; //外牆寬度
            chart5.ChartAreas["ChartArea1"].Area3DStyle.LightStyle = LightStyle.Realistic; //光源

            // 設定Title1
            chart5.Titles["Title1"].DockedToChartArea = "ChartArea1";  // 設定要顯示在哪個圖表
            chart5.Titles["Title1"].IsDockedInsideChartArea = false;  // 設定要顯示在圖表的內外部

            //設定 Legends1
            chart5.Legends["Legends1"].DockedToChartArea = "ChartArea1"; //顯示在圖表內
            //chart5.Legends["Legends1"].Docking = Docking.Bottom; //自訂顯示位置
            chart5.Legends["Legends1"].BackColor = Color.FromArgb(235, 235, 235); //背景色

            //斜線背景
            chart5.Legends["Legends1"].BackHatchStyle = ChartHatchStyle.DarkDownwardDiagonal;
            chart5.Legends["Legends1"].BorderWidth = 1;
            chart5.Legends["Legends1"].BorderColor = Color.FromArgb(200, 200, 200);

            //設定 Series1
            chart5.Series["Series1"].ChartArea = "ChartArea1";  // 設定要呈現的ChartArea
            //chart5.Series["Series1"].ChartType = SeriesChartType.Line; //直條圖(Column),折線圖(Line),橫條圖(Bar)
            chart5.Series["Series1"].Points.DataBindXY(xValue, yValues);//Series1的XY數值放入圖中  // xx, yy 皆為一維陣列
            chart5.Series["Series1"].Legend = "Legends1";  // 設定要呈現哪個圖例
            chart5.Series["Series1"].LegendText = titleArr[0]; //設定圖例文字
            chart5.Series["Series1"].LabelFormat = "#.###"; //小數點
            chart5.Series["Series1"].MarkerSize = 8; //Label 範圍大小
            chart5.Series["Series1"].LabelForeColor = Color.FromArgb(0, 90, 255); //字體顏色

            //字體設定
            chart5.Series["Series1"].Font = new Font("Trebuchet MS", 10, System.Drawing.FontStyle.Bold);

            //Label 背景色
            chart5.Series["Series1"].LabelBackColor = Color.FromArgb(150, 255, 255, 255);
            chart5.Series["Series1"].Color = Color.FromArgb(240, 65, 140, 240); //背景色
            chart5.Series["Series1"].IsValueShownAsLabel = true; // Show data points labels

            /*  
            chart5.Series["Series2"].Points.DataBindXY(xValue, yValues);  // xx, yy 皆為一維陣列
            chart5.Series["Series2"].Legend = "Legends1";
            chart5.Series["Series2"].LegendText = titleArr[1];
            chart5.Series["Series2"].LabelFormat = "#.###"; //小數點
            chart5.Series["Series2"].MarkerSize = 8; //Label 範圍大小
            chart5.Series["Series2"].LabelForeColor = Color.FromArgb(255, 103, 0);
            chart5.Series["Series2"].Font = new System.Drawing.Font("Trebuchet MS", 10, FontStyle.Bold);
            chart5.Series["Series2"].LabelBackColor = Color.FromArgb(150, 255, 255, 255);
            chart5.Series["Series2"].Color = Color.FromArgb(240, 252, 180, 65); //背景色
            chart5.Series["Series2"].IsValueShownAsLabel = true; //顯示數據
            */
        }

        //------------------------------------------------------------  # 60個

        void draw_chart6()
        {
            // 直條圖

            string title = "直條圖";
            chart_init(chart6, title);

            //x軸只顯示一條，只要將資料都加入到一個序列內即可
            //而x軸顯示多條，則需要使用多個序列存放資料

            // 設定數列1 的 大小與外觀
            Series[] series1 = new Series[3];  // 預先建立3個數組   應該是不太好
            double[] _y = new double[] { 77, 35, 131 };
            Color[] colors = new Color[] { Color.Peru, Color.PowderBlue, Color.RosyBrown };
            String[] users = new String[] { "小王", "小風", "小明" };

            int len = users.Length;

            for (int index = 0; index < len; index++)
            {
                series1[index] = new Series(users[index]);
                series1[index].ChartType = SeriesChartType.Column;  // 直條圖
                series1[index].Color = colors[index];
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
                // 將數列新增到chart上
                chart6.Series.Add(s);
            }
        }

        //------------------------------------------------------------  # 60個

        void draw_chart7()
        {
            string title = "直條圖";
            chart_init(chart7, title);

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
                series1[index].ChartType = SeriesChartType.Column;  // 直條圖
                series1[index].Name = _users[index];
                series1[index].IsValueShownAsLabel = true;
                series1[index].Points.Add(_y[index]);
                // 將數列新增到chart上
                chart7.Series.Add(series1[index]);
            }

            /* print data TBD
            int i;
            int count = series1.Points.Count;
            richTextBox1.Text += "共有 " + count.ToString() + " 筆資料\n";
            for (i = 0; i < count; i++)
            {
                richTextBox1.Text += "X[" + i.ToString() + "] = " + series1.Points[i].XValue.ToString() + "\t";
                richTextBox1.Text += "Y[" + i.ToString() + "] = " + series1.Points[i].YValues[0].ToString() + "\n";
            }
            */
            /*
            //設定邊界
            chart2.ChartAreas[0].AxisX.Minimum = 0;//設定Y軸最小值
            chart2.ChartAreas[0].AxisX.Maximum = 8;//設定Y軸最大值
            chart2.ChartAreas[0].AxisY.Minimum = 0;//設定Y軸最小值
            chart2.ChartAreas[0].AxisY.Maximum = 120;//設定Y軸最大值
            */
        }

        //------------------------------------------------------------  # 60個

        void draw_chart8()
        {
            //用滑鼠指線 顯示數值
            richTextBox1.Text += "用滑鼠指線 顯示數值\n";
            FillChart();
            flag_show_value = true;
            this.tooltip.AutomaticDelay = 5;
        }

        private void FillChart()
        {
            string title = "";
            chart_init(chart8, title);

            var rand = new Random(123);
            var items = Enumerable.Range(0, 20).Select(x => new Item(x, rand.Next(1, 100) / 2.0)).ToList();

            var seriesLines = this.chart8.Series.Add("Line");
            seriesLines.ChartType = SeriesChartType.Line;  // 折線圖
            seriesLines.XValueMember = "X";
            seriesLines.YValueMembers = "Y";
            seriesLines.Color = Color.Red;

            var seriesPoints = this.chart8.Series.Add("Points");
            seriesPoints.ChartType = SeriesChartType.Point;  // 點狀圖
            seriesPoints.XValueMember = "X";
            seriesPoints.YValueMembers = "Y";

            this.chart8.DataSource = items;
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
