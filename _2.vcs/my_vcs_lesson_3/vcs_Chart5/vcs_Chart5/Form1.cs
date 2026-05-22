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

namespace vcs_Chart5
{
    public partial class Form1 : Form
    {
        int W = 500;
        int H = 400;

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
            string title = "chart0";
            chart_init(chart0, title);

        }

        //------------------------------------------------------------  # 60個

        void draw_chart1()
        {
            string title = "chart1";
            chart_init(chart1, title);

        }

        //------------------------------------------------------------  # 60個

        void draw_chart2()
        {
            string title = "chart2";
            chart_init(chart2, title);

        }

        //------------------------------------------------------------  # 60個

        void draw_chart3()
        {
            string title = "chart3";
            chart_init(chart3, title);

        }

        //------------------------------------------------------------  # 60個

        void draw_chart4()
        {
            string title = "chart4";
            chart_init(chart4, title);

        }

        //------------------------------------------------------------  # 60個

        void draw_chart5()
        {
            string title = "chart5";
            chart_init(chart5, title);

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
//應該效果不太好
            //Random rnd = new Random();  //亂數產生區塊顏色
            //foreach (DataPoint point in Chart1.Series[Series1].Points)
            //{
            //    //pie 顏色
            //    point.Color = Color.FromArgb(150, rnd.Next(0, 255), rnd.Next(0, 255), rnd.Next(0, 255)); 
            //}

//------------------------------------------------------------  # 60個

            // 繪製圓餅圖

            Series series1 = new Series();
            double[] _y = new double[] { 77, 35, 131, 55, 77, 66 };
            Color[] _colors = new Color[] { Color.Peru, Color.PowderBlue, Color.RosyBrown, Color.Salmon, Color.Sienna, Color.SlateBlue };
            String[] _users = new String[] { "小王", "小風", "小明", "小姿", "小玉", "小蟹" };

            series1.ChartType = SeriesChartType.Pie;
            series1.IsValueShownAsLabel = true;
            series1.Points.DataBindXY(_users, _y);  // xx, yy 皆為一維陣列
            chart1.Series.Add(series1);

//------------------------------------------------------------  # 60個

//C#chart之PieChart

                void CreateChart()
        {
            string[] xValues = { "0-20", "20-30", "30-40", "40-50", "50-60", "> 60", "unknow" };
            int[] yValues = {5, 18, 45, 17, 2, 1, 162 };

            //ChartAreas,Series,Legends 基本設定-------------------------------------------------
            Chart Chart1 = new Chart();
            Chart1.ChartAreas.Add(ChartArea1); //圖表區域集合
            Chart1.Legends.Add(Legends1); //圖例集合說明
            Chart1.Series.Add(Series1); //數據序列集合

            //設定 Chart
            Chart1.Width = 770;
            Chart1.Height = 400;
            Title title = new Title();
            title.Text = "titleStr";
            title.Alignment = ContentAlignment.MiddleCenter;
            title.Font = new System.Drawing.Font("Trebuchet MS", 14F, FontStyle.Bold);
            Chart1.Titles.Add(title);

            //設定 ChartArea1
            Chart1.ChartAreas[ChartArea1].Area3DStyle.Enable3D = is3D;
            Chart1.ChartAreas[0].AxisX.Interval = 1;

            //設定 Legends
            //Chart1.Legends[Legends1].DockedToChartArea = ChartArea1; //顯示在圖表內
            //Chart1.Legends[Legends1].Docking = Docking.Bottom; //自訂顯示位置
            //背景色
            Chart1.Legends[Legends1].BackColor = Color.FromArgb(235, 235, 235); 
            //斜線背景
            Chart1.Legends[Legends1].BackHatchStyle = ChartHatchStyle.DarkDownwardDiagonal; 
            Chart1.Legends[Legends1].BorderWidth = 1;
            Chart1.Legends[Legends1].BorderColor = Color.FromArgb(200, 200, 200);

            //設定 Series1
            Chart1.Series[Series1].ChartType = SeriesChartType.Pie;
            //Chart1.Series[Series1].ChartType = SeriesChartType.Doughnut;
            Chart1.Series[Series1].Points.DataBindXY(xValues, yValues);  // xx, yy 皆為一維陣列
            Chart1.Series[Series1].LegendText = "Aaaaaa";   //#VALX:    [ #PERCENT{P1} ]; //X軸 + 百分比
            Chart1.Series[Series1].Label = "bbbb";  //#VALX#PERCENT{P1}; //X軸 + 百分比
            //Chart1.Series[Series1].LabelForeColor = Color.FromArgb(0, 90, 255); //字體顏色
            //字體設定
            Chart1.Series[Series1].Font = new System.Drawing.Font("Trebuchet MS", 10, System.Drawing.FontStyle.Bold); 
            Chart1.Series[Series1].Points.FindMaxByValue().LabelForeColor = Color.Red;
            //Chart1.Series[Series1].Points.FindMaxByValue().Color = Color.Red;
            //Chart1.Series[Series1].Points.FindMaxByValue()[Exploded] = true;
            Chart1.Series[Series1].BorderColor = Color.FromArgb(255, 101, 101, 101);
            
            //Chart1.Series[Series1][DoughnutRadius] = 80; // ChartType為Doughnut時，Set Doughnut hole size
            //Chart1.Series[Series1][PieLabelStyle] = Inside; //數值顯示在圓餅內
            Chart1.Series[Series1][PieLabelStyle] = Outside; //數值顯示在圓餅外
            //Chart1.Series[Series1][PieLabelStyle] = Disabled; //不顯示數值
            //設定圓餅效果，除 Default 外其他效果3D不適用
            Chart1.Series[Series1][PieDrawingStyle] = Default; 
            //Chart1.Series[Series1][PieDrawingStyle] = SoftEdge;
            //Chart1.Series[Series1][PieDrawingStyle] = Concave;

            //Random rnd = new Random();  //亂數產生區塊顏色
            //foreach (DataPoint point in Chart1.Series[Series1].Points)
            //{
            //    //pie 顏色
            //    point.Color = Color.FromArgb(150, rnd.Next(0, 255), rnd.Next(0, 255), rnd.Next(0, 255)); 
            //}
            this.Controls.Add(Chart1);
        }
      
//------------------------------------------------------------  # 60個


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








