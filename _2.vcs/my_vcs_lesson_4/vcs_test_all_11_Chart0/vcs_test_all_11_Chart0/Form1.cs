using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Windows.Forms.DataVisualization.Charting;  //for Series

namespace vcs_test_all_11_Chart0
{
    public partial class Form1 : Form
    {
        //定義Chart大小與外觀
        private const int CHART_WIDTH = 740;
        private const int CHART_HEIGHT = 370;
        private const int AXIS_X_MIN = 0;
        private const int AXIS_X_MAX = 360;
        private const int AXIS_Y_MIN = -200;
        private const int AXIS_Y_MAX = 200;
        private const string TITLE = "三角函數";
        private const string XLABLE = "Degree";
        private const string YLABLE = "Amplitude";

        public Form1()
        {
            InitializeComponent();
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            chart1_init();
        }

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

        void chart1_init()
        {
            chart1.Series.Clear();  //每次使用此function前先清除圖表

            //設定Chart大小與外觀
            //全圖
            chart1.Size = new Size(CHART_WIDTH, CHART_HEIGHT);      //改變Cahrt大小
            chart1.Titles.Add(TITLE);                               //標題

            //X軸
            chart1.ChartAreas[0].AxisX.Minimum = AXIS_X_MIN;        //設定X軸最小值
            chart1.ChartAreas[0].AxisX.Maximum = AXIS_X_MAX;        //設定X軸最大值
            chart1.ChartAreas[0].AxisX.Title = XLABLE;
            chart1.ChartAreas[0].AxisX.Enabled = AxisEnabled.True;  //顯示 或 隱藏 X 軸標示
            chart1.ChartAreas[0].AxisX.MajorGrid.Enabled = true;    //顯示 或 隱藏 X 軸標線

            //Y軸
            chart1.ChartAreas[0].AxisY.Minimum = AXIS_Y_MIN;        //設定Y軸最小值
            chart1.ChartAreas[0].AxisY.Maximum = AXIS_Y_MAX;        //設定Y軸最大值
            chart1.ChartAreas[0].AxisY.Title = YLABLE;
            chart1.ChartAreas[0].AxisY.Enabled = AxisEnabled.True;   //顯示 或 隱藏 Y 軸標示
            chart1.ChartAreas[0].AxisY.MajorGrid.Enabled = true;    //顯示 或 隱藏 Y 軸標線

        }

        private void button1_Click(object sender, EventArgs e)
        {
            chart1_init();
            richTextBox1.Text += "靜畫範例1, 用獨立數組做\n\r";
                 
            //設定數列大小與外觀
            //series 1
            Series series1 = new Series("sin", 500); //初始畫線條(標題，最大值)
            series1.Color = Color.Red; //設定線條顏色
            series1.Font = new System.Drawing.Font("新細明體", 10); //設定字型
            series1.ChartType = SeriesChartType.Point; //設定線條種類
            series1.MarkerSize = 5;     //圖標大小
            series1.IsValueShownAsLabel = false;   //將數值顯示在線上

            //series 2
            Series series2 = new Series("cos", 500); //初始畫線條(標題，最大值)
            series2.Color = Color.Green; //設定線條顏色
            series2.Font = new System.Drawing.Font("標楷體", 12); //設定字型
            series2.ChartType = SeriesChartType.Point; //設定線條種類
            series2.MarkerSize = 5;     //圖標大小
            series2.IsValueShownAsLabel = false;   //將數值顯示在線上

            //series 3
            Series series3 = new Series("sin + cos", 500); //初始畫線條(標題，最大值)
            series3.Color = Color.Blue; //設定線條顏色
            series3.Font = new System.Drawing.Font("標楷體", 12); //設定字型
            series3.ChartType = SeriesChartType.Point; //設定線條種類
            series3.MarkerSize = 5;     //圖標大小
            series3.IsValueShownAsLabel = false;   //將數值顯示在線上

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
                //richTextBox1.Text += "len = " + chart1.Series[0].Points.Count.ToString() + "\n";
                //chart1.Series[0].Points.AddXY(array_x[i / 10], array_y1[i / 10]);
                series1.Points.AddXY(array_x[i / 10], array_y1[i / 10]);    //將數值1新增至序列1
                series2.Points.AddXY(array_x[i / 10], array_y2[i / 10]);    //將數值2新增至序列2
                series3.Points.AddXY(array_x[i / 10], array_y3[i / 10]);    //將數值3新增至序列3
            }

            //經過chart1.Series.Clear()後, chart1.Series.Count = 0
            chart1.Series.Add(series1);//將序列1新增到chart上
            //此時, chart1.Series.Count = 1
            chart1.Series.Add(series2);//將序列2新增到chart上
            //此時, chart1.Series.Count = 2
            chart1.Series.Add(series3);//將序列3新增到chart上
            //此時, chart1.Series.Count = 3

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

        private void button2_Click(object sender, EventArgs e)
        {
            chart1_init();
            richTextBox1.Text += "靜畫範例2, 用數組陣列做\n\r";

            //設定數列大小與外觀
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
                series[i].Font = new System.Drawing.Font("新細明體", 10); //設定字型
                series[i].ChartType = SeriesChartType.Point; //設定線條種類
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
                chart1.Series.Add(s);       //將序列1新增到chart上
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (button3.Text == "動畫 ST")
            {
                button3.Text = "動畫 SP";
                chart1_init();
                Series series1 = new Series();
                chart1.Series.Add(series1);
                chart1.Series[0].ChartType = SeriesChartType.Point; //設定線條種類;
                //chart1.Series[0].ChartType = chartType;
                //series1.ChartType = SeriesChartType.Point; //設定線條種類
                timer1.Enabled = true;
            }
            else
            {
                button3.Text = "動畫 ST";
                timer1.Enabled = false;
            }
        }

        double x = 0;
        private const int POINTS_IN_AXIS = 36;      //製作動畫時X軸要保留的點數
        private void timer1_Tick(object sender, EventArgs e)
        {
            double y;
            y = 110 * sind(x);

            chart1.Series[0].Points.AddXY(x, y);

            if (chart1.Series[0].Points.Count > POINTS_IN_AXIS)
                chart1.Series[0].Points.RemoveAt(0);

            //製作動畫
            chart1.ChartAreas[0].AxisX.Minimum = chart1.Series[0].Points[0].XValue;
            chart1.ChartAreas[0].AxisX.Maximum = x;

            x += 26;
        }

        private void bt_clear_chart_Click(object sender, EventArgs e)
        {
            if(timer1.Enabled == false)
                chart1.Series.Clear();  //每次使用此function前先清除圖表
            /*
            chart1.Series[0].Points.Clear();
            chart1.Series[1].Points.Clear();
            chart1.Series[2].Points.Clear();
            */
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            save_chart_image_to_drive();
        }

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


    }
}
