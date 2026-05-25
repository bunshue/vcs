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
        }

        //------------------------------------------------------------  # 60個

        void draw_chart1()
        {
        }

        //------------------------------------------------------------  # 60個

        void draw_chart2()
        {
        }

        //------------------------------------------------------------  # 60個

        void draw_chart3()
        {
        }

        //------------------------------------------------------------  # 60個

        void draw_chart4()
        {
        }

        //------------------------------------------------------------  # 60個

        void draw_chart5()
        {
        }

        //------------------------------------------------------------  # 60個

        void draw_chart6()
        {

        }

        //------------------------------------------------------------  # 60個

        void draw_chart7()
        {
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

/*  可搬出

*/

