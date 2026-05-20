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
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

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
            this.Text = "vcs_Chart3";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void draw_chart0()
        {
        }

        void draw_chart1()
        {
        }

        void draw_chart2()
        {
        }

        void draw_chart3()
        {
        }

        void draw_chart4()
        {
            string[] xValues = { "北部", "中部", "南部", "東部", "離島" };
            int[] yValues = { 137, 163, 237, 48, 4 };
            //ChartAreas,Series,Legends 基本設定-------------------------------------------------
            if (chart4.Legends.FindByName("Legends2") == null) //如果chart4沒有包含Legends2才將其Add
            {
                chart4.Legends.Add(new Legend("Legends2")); //圖例集合說明
            }
            chart4.ChartAreas.Add("ChartArea2"); ////圖表區域集合
            //chart4.Series.Add("Series3"); ////數據序列集合
            // chart4.Legends.Add("Legends2"); ////圖例集合
            ////標題集合
            Title Title2 = new Title
            {
                Text = "各區域發生婦幼被害犯罪件數統計比例圖",
                Alignment = ContentAlignment.MiddleCenter,
                Font = new Font("Trebuchet MS", 14F, FontStyle.Bold)
            };
            chart4.Titles.Add(Title2);
            //設定 ChartArea2--------------------------------------------------------------------
            //設定3D
            chart4.ChartAreas["ChartArea2"].Area3DStyle.Enable3D = true; //3D效果
            chart4.ChartAreas["ChartArea2"].Area3DStyle.IsClustered = true; //並排顯示
            chart4.ChartAreas["ChartArea2"].Area3DStyle.Rotation = 40; //垂直角度
            chart4.ChartAreas["ChartArea2"].Area3DStyle.Inclination = 50; //水平角度
            chart4.ChartAreas["ChartArea2"].Area3DStyle.PointDepth = 10; //數據條厚度
            chart4.ChartAreas["ChartArea2"].Area3DStyle.WallWidth = 0; //外牆寬度
            chart4.ChartAreas["ChartArea2"].Area3DStyle.LightStyle = LightStyle.Realistic; //光源
            ////設定Title2---------------------------------------------------------------------------
            chart4.Titles["Title2"].DockedToChartArea = "ChartArea2"; //設定標題停駐的ChartArea
            chart4.Titles["Title2"].IsDockedInsideChartArea = false; //設定顯示在圖表的內外部
            //設定 Legends2-------------------------------------------------------------------------                
            chart4.Legends["Legends2"].DockedToChartArea = "ChartArea2"; //設定要顯示在哪個圖表
            chart4.Legends["Legends2"].IsDockedInsideChartArea = false; //設定要顯示在圖表的內外部
            //chart4.Legends["Legends2"].Docking = Docking.Bottom; //自訂顯示位置
            //背景色
            chart4.Legends["Legends2"].BackColor = Color.FromArgb(235, 235, 235);
            //斜線背景
            chart4.Legends["Legends2"].BackHatchStyle = ChartHatchStyle.DarkDownwardDiagonal;
            chart4.Legends["Legends2"].BorderWidth = 1;
            chart4.Legends["Legends2"].BorderColor = Color.FromArgb(200, 200, 200);
            //設定 Series4b-----------------------------------------------------------------------
            chart4.Series["Series4b"].ChartArea = "ChartArea2"; ////設定要呈現的ChartArea
            chart4.Series["Series4b"].ChartType = SeriesChartType.Pie; //設定圖表類型
            //chart4.Series["Series4b"].ChartType = SeriesChartType.Doughnut; //中空圓餅圖
            chart4.Series["Series4b"].Points.DataBindXY(xValues, yValues);
            chart4.Series["Series4b"].Legend = "Legends2"; ////設定要呈現哪個圖例
            // chart4.Series["Series4b"].IsValueShownAsLabel = true; // Show data points labels
            chart4.Series["Series4b"].XValueType = ChartValueType.String; //X軸的資料格式
            chart4.Series["Series4b"].LegendText = "#VALX :[ #PERCENT{P1} ]"; //X軸 + 百分比
            chart4.Series["Series4b"].Label = "#VALX\n#PERCENT{P1}"; //X軸 + 百分比
            //chart4.Series["Series4b"].LabelForeColor = Color.FromArgb(0, 90, 255); //字體顏色
            //字體設定
            chart4.Series["Series4b"].Font = new Font("Trebuchet MS", 10, FontStyle.Bold);
            chart4.Series["Series4b"].Points.FindMaxByValue().LabelForeColor = Color.Red; //設定特定數字之字體
            //chart4.Series["Series4b"].Points.FindMaxByValue().Color = Color.Red; //設定數值最大的餅的顏色
            //chart4.Series["Series4b"].Points.FindMaxByValue()["Exploded"] = "true"; ////設定數值最大的餅是否分離出去
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
            chart5.Series.Clear();
            chart5.ChartAreas.Clear();
            chart5.Legends.Clear();
            chart5.Titles.Clear();

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
            chart5.ChartAreas.Add("ChartArea1"); ////圖表區域集合
            chart5.Series.Add("Series1"); ////數據序列集合
            chart5.Legends.Add("Legends1"); ////圖例集合
            ////標題集合
            Title Title1 = new Title
            {
                Text = "各縣市發生婦幼被害犯罪件數統計",
                Alignment = ContentAlignment.MiddleCenter,
                Font = new Font("Trebuchet MS", 14F, FontStyle.Bold)
            };
            chart5.Titles.Add(Title1);
            //設定 ChartArea1----------------------------------------------------------------------
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
            ////設定Title1---------------------------------------------------------------------------
            chart5.Titles["Title1"].DockedToChartArea = "ChartArea1"; ////設定要顯示在哪個圖表
            chart5.Titles["Title1"].IsDockedInsideChartArea = false; ////設定要顯示在圖表的內外部
            //設定 Legends1------------------------------------------------------------------------         
            chart5.Legends["Legends1"].DockedToChartArea = "ChartArea1"; //顯示在圖表內
            //chart5.Legends["Legends1"].Docking = Docking.Bottom; //自訂顯示位置
            chart5.Legends["Legends1"].BackColor = Color.FromArgb(235, 235, 235); //背景色
            //斜線背景
            chart5.Legends["Legends1"].BackHatchStyle = ChartHatchStyle.DarkDownwardDiagonal;
            chart5.Legends["Legends1"].BorderWidth = 1;
            chart5.Legends["Legends1"].BorderColor = Color.FromArgb(200, 200, 200);
            //設定 Series1-----------------------------------------------------------------------
            chart5.Series["Series1"].ChartArea = "ChartArea1"; ////設定要呈現的ChartArea
            //chart5.Series["Series1"].ChartType = SeriesChartType.Line; //直條圖(Column),折線圖(Line),橫條圖(Bar)
            chart5.Series["Series1"].Points.DataBindXY(xValue, yValues);//Series1的XY數值放入圖中
            chart5.Series["Series1"].Legend = "Legends1"; ////設定要呈現哪個圖例
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

            /*  chart5.Series["Series2"].Points.DataBindXY(xValue, yValues);

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


