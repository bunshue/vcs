using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Windows.Forms.DataVisualization.Charting;

/*
拉一個Chart控件

chart1屬性
ChartAreas 移除 ChartArea1
Series 移除 Series1
*/

namespace vcs_Chart7
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            draw_chart_bar();
        }

        void draw_chart_bar()
        {

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
            chart1.ChartAreas.Add("ChartArea1"); ////圖表區域集合
            chart1.Series.Add("Series1"); ////數據序列集合
            chart1.Legends.Add("Legends1"); ////圖例集合
            ////標題集合
            Title Title1 = new Title
            {
                Text = "各縣市發生婦幼被害犯罪件數統計",
                Alignment = ContentAlignment.MiddleCenter,
                Font = new Font("Trebuchet MS", 14F, FontStyle.Bold)
            };
            chart1.Titles.Add(Title1);
            //設定 ChartArea1----------------------------------------------------------------------
            chart1.ChartAreas["ChartArea1"].AxisX.Interval = 1;   //設置X軸坐標的間隔為1
            chart1.ChartAreas["ChartArea1"].AxisX.IntervalOffset = 1;  //設置X軸坐標偏移為1
            chart1.ChartAreas["ChartArea1"].AxisX.LabelStyle.IsStaggered = true;   //設置是否交錯顯示,比如數據多的時間分成兩行來顯示
            chart1.ChartAreas["ChartArea1"].AxisX.Title = "縣市"; //設定X軸的標題
            chart1.ChartAreas["ChartArea1"].AxisY.Title = "人數"; //設定Y軸的標題
            chart1.ChartAreas["ChartArea1"].BackColor = Color.FromArgb(240, 240, 240); //背景色
            chart1.ChartAreas["ChartArea1"].AxisX.Enabled = AxisEnabled.True;
            chart1.ChartAreas["ChartArea1"].AxisX2.Enabled = AxisEnabled.False; //隱藏 X2 標示
            chart1.ChartAreas["ChartArea1"].AxisY2.Enabled = AxisEnabled.False; //隱藏 Y2 標示
            chart1.ChartAreas["ChartArea1"].AxisY2.MajorGrid.Enabled = false;   //隱藏 Y2 軸線
            chart1.ChartAreas["ChartArea1"].AxisX.MajorGrid.LineColor = Color.FromArgb(150, 150, 150);//X 軸線顏色
            chart1.ChartAreas["ChartArea1"].AxisY.MajorGrid.LineColor = Color.FromArgb(150, 150, 150);//Y 軸線顏色
            chart1.ChartAreas["ChartArea1"].AxisY.LabelStyle.Format = "#.###";//設定小數點
            //設定3D
            chart1.ChartAreas["ChartArea1"].Area3DStyle.Enable3D = true; //3D效果
            chart1.ChartAreas["ChartArea1"].Area3DStyle.IsClustered = true; //並排顯示
            chart1.ChartAreas["ChartArea1"].Area3DStyle.Rotation = 40; //垂直角度
            chart1.ChartAreas["ChartArea1"].Area3DStyle.Inclination = 50; //水平角度
            chart1.ChartAreas["ChartArea1"].Area3DStyle.PointDepth = 10; //數據條厚度
            chart1.ChartAreas["ChartArea1"].Area3DStyle.WallWidth = 0; //外牆寬度
            chart1.ChartAreas["ChartArea1"].Area3DStyle.LightStyle = LightStyle.Realistic; //光源
            ////設定Title1---------------------------------------------------------------------------
            chart1.Titles["Title1"].DockedToChartArea = "ChartArea1"; ////設定要顯示在哪個圖表
            chart1.Titles["Title1"].IsDockedInsideChartArea = false; ////設定要顯示在圖表的內外部
            //設定 Legends1------------------------------------------------------------------------         
            chart1.Legends["Legends1"].DockedToChartArea = "ChartArea1"; //顯示在圖表內
            //chart1.Legends["Legends1"].Docking = Docking.Bottom; //自訂顯示位置
            chart1.Legends["Legends1"].BackColor = Color.FromArgb(235, 235, 235); //背景色
            //斜線背景
            chart1.Legends["Legends1"].BackHatchStyle = ChartHatchStyle.DarkDownwardDiagonal;
            chart1.Legends["Legends1"].BorderWidth = 1;
            chart1.Legends["Legends1"].BorderColor = Color.FromArgb(200, 200, 200);
            //設定 Series1-----------------------------------------------------------------------
            chart1.Series["Series1"].ChartArea = "ChartArea1"; ////設定要呈現的ChartArea
            //chart1.Series["Series1"].ChartType = SeriesChartType.Line; //直條圖(Column),折線圖(Line),橫條圖(Bar)
            chart1.Series["Series1"].Points.DataBindXY(xValue, yValues);//Series1的XY數值放入圖中
            chart1.Series["Series1"].Legend = "Legends1"; ////設定要呈現哪個圖例
            chart1.Series["Series1"].LegendText = titleArr[0]; //設定圖例文字
            chart1.Series["Series1"].LabelFormat = "#.###"; //小數點
            chart1.Series["Series1"].MarkerSize = 8; //Label 範圍大小
            chart1.Series["Series1"].LabelForeColor = Color.FromArgb(0, 90, 255); //字體顏色
            //字體設定
            chart1.Series["Series1"].Font = new Font("Trebuchet MS", 10, System.Drawing.FontStyle.Bold);
            //Label 背景色
            chart1.Series["Series1"].LabelBackColor = Color.FromArgb(150, 255, 255, 255);
            chart1.Series["Series1"].Color = Color.FromArgb(240, 65, 140, 240); //背景色
            chart1.Series["Series1"].IsValueShownAsLabel = true; // Show data points labels

            /*  chart1.Series["Series2"].Points.DataBindXY(xValue, yValues);

              chart1.Series["Series2"].Legend = "Legends1";
              chart1.Series["Series2"].LegendText = titleArr[1];
              chart1.Series["Series2"].LabelFormat = "#.###"; //小數點
              chart1.Series["Series2"].MarkerSize = 8; //Label 範圍大小
              chart1.Series["Series2"].LabelForeColor = Color.FromArgb(255, 103, 0);
              chart1.Series["Series2"].Font = new System.Drawing.Font("Trebuchet MS", 10, FontStyle.Bold);
              chart1.Series["Series2"].LabelBackColor = Color.FromArgb(150, 255, 255, 255);
              chart1.Series["Series2"].Color = Color.FromArgb(240, 252, 180, 65); //背景色
              chart1.Series["Series2"].IsValueShownAsLabel = true; //顯示數據*/
        }
    }
}
