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

chart1屬性
Series 加 Series2
Titles 加 Title1 Title2
*/

namespace vcs_Chart6
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
            draw_chart_pie();
        }

        void draw_chart_pie()
        {
            string[] xValues = { "北部", "中部", "南部", "東部", "離島" };
            int[] yValues = { 137, 163, 237, 48, 4 };
            //ChartAreas,Series,Legends 基本設定-------------------------------------------------
            if (chart1.Legends.FindByName("Legends2") == null) //如果Chart1沒有包含Legends2才將其Add
            {
                chart1.Legends.Add(new Legend("Legends2")); //圖例集合說明
            }
            chart1.ChartAreas.Add("ChartArea2"); ////圖表區域集合
            chart1.Series.Add("Series3"); ////數據序列集合
            // chart1.Legends.Add("Legends2"); ////圖例集合
            ////標題集合
            Title Title2 = new Title
            {
                Text = "各區域發生婦幼被害犯罪件數統計比例圖",
                Alignment = ContentAlignment.MiddleCenter,
                Font = new Font("Trebuchet MS", 14F, FontStyle.Bold)
            };
            chart1.Titles.Add(Title2);
            //設定 ChartArea2--------------------------------------------------------------------
            //設定3D
            chart1.ChartAreas["ChartArea2"].Area3DStyle.Enable3D = true; //3D效果
            chart1.ChartAreas["ChartArea2"].Area3DStyle.IsClustered = true; //並排顯示
            chart1.ChartAreas["ChartArea2"].Area3DStyle.Rotation = 40; //垂直角度
            chart1.ChartAreas["ChartArea2"].Area3DStyle.Inclination = 50; //水平角度
            chart1.ChartAreas["ChartArea2"].Area3DStyle.PointDepth = 10; //數據條厚度
            chart1.ChartAreas["ChartArea2"].Area3DStyle.WallWidth = 0; //外牆寬度
            chart1.ChartAreas["ChartArea2"].Area3DStyle.LightStyle = LightStyle.Realistic; //光源
            ////設定Title2---------------------------------------------------------------------------
            chart1.Titles["Title2"].DockedToChartArea = "ChartArea2"; //設定標題停駐的ChartArea
            chart1.Titles["Title2"].IsDockedInsideChartArea = false; //設定顯示在圖表的內外部
            //設定 Legends2-------------------------------------------------------------------------                
            chart1.Legends["Legends2"].DockedToChartArea = "ChartArea2"; //設定要顯示在哪個圖表
            chart1.Legends["Legends2"].IsDockedInsideChartArea = false; //設定要顯示在圖表的內外部
            //chart1.Legends["Legends2"].Docking = Docking.Bottom; //自訂顯示位置
            //背景色
            chart1.Legends["Legends2"].BackColor = Color.FromArgb(235, 235, 235);
            //斜線背景
            chart1.Legends["Legends2"].BackHatchStyle = ChartHatchStyle.DarkDownwardDiagonal;
            chart1.Legends["Legends2"].BorderWidth = 1;
            chart1.Legends["Legends2"].BorderColor = Color.FromArgb(200, 200, 200);
            //設定 Series2-----------------------------------------------------------------------
            chart1.Series["Series2"].ChartArea = "ChartArea2"; ////設定要呈現的ChartArea
            chart1.Series["Series2"].ChartType = SeriesChartType.Pie; //設定圖表類型
            //chart1.Series["Series2"].ChartType = SeriesChartType.Doughnut; //中空圓餅圖
            chart1.Series["Series2"].Points.DataBindXY(xValues, yValues);
            chart1.Series["Series2"].Legend = "Legends2"; ////設定要呈現哪個圖例
            // chart1.Series["Series2"].IsValueShownAsLabel = true; // Show data points labels
            chart1.Series["Series2"].XValueType = ChartValueType.String; //X軸的資料格式
            chart1.Series["Series2"].LegendText = "#VALX :[ #PERCENT{P1} ]"; //X軸 + 百分比
            chart1.Series["Series2"].Label = "#VALX\n#PERCENT{P1}"; //X軸 + 百分比
            //chart1.Series["Series2"].LabelForeColor = Color.FromArgb(0, 90, 255); //字體顏色
            //字體設定
            chart1.Series["Series2"].Font = new Font("Trebuchet MS", 10, FontStyle.Bold);
            chart1.Series["Series2"].Points.FindMaxByValue().LabelForeColor = Color.Red; //設定特定數字之字體
            //chart1.Series["Series2"].Points.FindMaxByValue().Color = Color.Red; //設定數值最大的餅的顏色
            //chart1.Series["Series2"].Points.FindMaxByValue()["Exploded"] = "true"; ////設定數值最大的餅是否分離出去
            chart1.Series["Series2"].BorderColor = Color.FromArgb(255, 101, 101, 101);
            //chart1.Series["Series2"]["DoughnutRadius"] = "80"; // ChartType為Doughnut時，Set Doughnut hole size
            //chart1.Series["Series2"]["PieLabelStyle"] = "Inside"; //數值顯示在圓餅內
            chart1.Series["Series2"]["PieLabelStyle"] = "Outside"; //數值顯示在圓餅外
            //chart1.Series["Series2"]["PieLabelStyle"] = "Disabled"; //不顯示數值
            //設定圓餅效果，除 Default 外其他效果3D不適用
            //chart1.Series["Series2"]["PieDrawingStyle"] = "Default";
            //chart1.Series["Series2"]["PieDrawingStyle"] = "SoftEdge";
            //chart1.Series["Series2"]["PieDrawingStyle"] = "Concave";

            //Random rnd = new Random();  //亂數產生區塊顏色
            //foreach (DataPoint point in chart1.Series["Series2"].Points)
            //{
            //    //pie 顏色
            //    point.Color = Color.FromArgb(150, rnd.Next(0, 255), rnd.Next(0, 255), rnd.Next(0, 255)); 
            //}
        }
    }
}
