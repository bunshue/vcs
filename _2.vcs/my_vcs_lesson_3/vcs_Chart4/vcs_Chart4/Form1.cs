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
            // 清除圖表
            chart1.Series.Clear();
            chart1.Titles.Clear();

            chart1.Size = new Size(W, H);  // 設定chart大小

            // 畫標題的方法1
            Title chart_title = new Title();
            chart_title.Text = title;
            chart_title.Alignment = ContentAlignment.MiddleCenter;
            chart_title.Font = new Font("Trebuchet MS", 14F, FontStyle.Bold);
            chart1.Titles.Add(chart_title);  // 標題

            // 畫標題的方法2
            Title chart_title2 = new Title
            {
                Text = title,
                Alignment = ContentAlignment.MiddleCenter,
                Font = new Font("Trebuchet MS", 14F, FontStyle.Bold)
            };
            //chart1.Titles.Add(chart_title2);
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

//1515
//---------------  # 15個


/*  可搬出

*/

