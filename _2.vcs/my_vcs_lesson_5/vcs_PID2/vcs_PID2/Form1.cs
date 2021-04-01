using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Windows.Forms.DataVisualization.Charting;  //for Series

namespace vcs_PID2
{
    public partial class Form1 : Form
    {
        //定義Chart大小與外觀
        private const int CHART_WIDTH = 740;
        private const int CHART_HEIGHT = 370;
        private const int AXIS_X_MIN = 0;
        private const int AXIS_X_MAX = 200;
        private const int AXIS_Y_MIN = 0;
        private const int AXIS_Y_MAX = 100;
        private const string TITLE = "三角函數";
        private const string XLABLE = "Degree";
        private const string YLABLE = "Amplitude";

        int total_candles = 0;
        float J = 0;
        float target = 60;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            chart1_init();
            Series series1 = new Series();
            chart1.Series.Add(series1);
            chart1.Series[0].ChartType = SeriesChartType.Spline; //設定線條種類;
            //series1.ChartType = SeriesChartType.Point; //設定線條種類
            timer1.Enabled = true;
            lb_total_candles.Text = "N = " + total_candles.ToString();
            lb_total_energy.Text = "E = " + J.ToString();
            lb_target.Text = target.ToString();
            lb_temperature.Text = "0";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void chart1_init()
        {
            chart1.Series.Clear();  //每次使用此function前先清除圖表

            //設定Chart大小與外觀
            //全圖
            chart1.Size = new Size(CHART_WIDTH, CHART_HEIGHT);      //改變Cahrt大小
            //chart1.Titles.Add(TITLE);                               //標題

            //X軸
            chart1.ChartAreas[0].AxisX.Minimum = AXIS_X_MIN;        //設定X軸最小值
            chart1.ChartAreas[0].AxisX.Maximum = AXIS_X_MAX;        //設定X軸最大值
            //chart1.ChartAreas[0].AxisX.Title = XLABLE;              //設定X軸名稱
            chart1.ChartAreas[0].AxisX.TitleForeColor = Color.Blue; //設定X軸名稱的字體顏色
            chart1.ChartAreas[0].AxisX.Enabled = AxisEnabled.True;  //顯示 或 隱藏 X 軸標示
            chart1.ChartAreas[0].AxisX.MajorGrid.Enabled = true;    //顯示 或 隱藏 X 軸標線
            chart1.ChartAreas[0].AxisX.LabelStyle.Font = new System.Drawing.Font("Trebuchet MS", 15, System.Drawing.FontStyle.Bold);   //設定X軸刻度的字型
            chart1.ChartAreas[0].AxisX.LabelStyle.Interval = 10;    //設置X軸刻度間隔的大小
            chart1.ChartAreas[0].AxisX.LabelStyle.IntervalType = DateTimeIntervalType.Number;//設置間隔大小的度量單位
            chart1.ChartAreas[0].AxisX.LineColor = System.Drawing.Color.White;//設置X軸的線條顏色
            chart1.ChartAreas[0].AxisX.MajorGrid.Interval = 10;//設置主網格線與次要網格線的間隔
            chart1.ChartAreas[0].AxisX.MajorGrid.IntervalType = DateTimeIntervalType.Number;//設置主網格線與次網格線的間隔的度量單位
            chart1.ChartAreas[0].AxisX.MajorGrid.LineColor = System.Drawing.Color.Snow;//設置網格線的顏色
            chart1.ChartAreas[0].AxisX.MajorTickMark.Interval = 5;//設置刻度線的間隔
            chart1.ChartAreas[0].AxisX.MajorTickMark.IntervalType = DateTimeIntervalType.Number;//設置刻度線的間隔的度量單位

            //Y軸
            chart1.ChartAreas[0].AxisY.Minimum = AXIS_Y_MIN;        //設定Y軸最小值
            chart1.ChartAreas[0].AxisY.Maximum = AXIS_Y_MAX;        //設定Y軸最大值
            //chart1.ChartAreas[0].AxisY.Title = YLABLE;              //設定Y軸名稱
            chart1.ChartAreas[0].AxisY.TitleForeColor = Color.Blue; //設定Y軸名稱的字體顏色
            chart1.ChartAreas[0].AxisY.Enabled = AxisEnabled.True;  //顯示 或 隱藏 Y 軸標示
            chart1.ChartAreas[0].AxisY.MajorGrid.Enabled = true;    //顯示 或 隱藏 Y 軸標線

            chart1.ChartAreas[0].AxisY.LabelStyle.Font = new System.Drawing.Font("Trebuchet MS", 8.25F, System.Drawing.FontStyle.Bold);//設置Y軸左側的提示信息的字體屬性
            chart1.ChartAreas[0].AxisY.LineColor = System.Drawing.Color.DarkBlue;//設置軸的線條顏色
            chart1.ChartAreas[0].AxisY.MajorGrid.LineColor = System.Drawing.Color.White;//設置網格線顏色

            #region 圖表樣式
            chart1.BackGradientStyle = System.Windows.Forms.DataVisualization.Charting.GradientStyle.TopBottom;//指定圖表元素的漸變樣式(中心向外，從左到右，從上到下等等)
            chart1.BackSecondaryColor = System.Drawing.Color.Yellow;//設置背景的輔助顏色
            chart1.BorderlineColor = System.Drawing.Color.Yellow;//設置圖像邊框的顏色
            chart1.BorderlineDashStyle = System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.Solid;//設置圖像邊框線的樣式(實線、虛線、點線)
            chart1.BorderlineWidth = 2;//設置圖像的邊框寬度
            chart1.BorderSkin.SkinStyle = System.Windows.Forms.DataVisualization.Charting.BorderSkinStyle.Emboss;//設置圖像的邊框外觀樣式
            chart1.BackColor = System.Drawing.Color.Yellow;//設置圖表的背景顏色
            #endregion
            //chart1.Titles[0].Font = new System.Drawing.Font("標楷體", 30f);//设置图表标题字体样式和大小
            //chart1.Legends["Legend1"].Docking = System.Windows.Forms.DataVisualization.Charting.Docking.Right;  //設定圖標顯示停靠的位置
        }

        void update_energy()
        {
            J += total_candles * 1;     //一支蠟燭1W，每一秒產出熱量要加起來

            J = J * 8 / 10;     //熱量剩下8成

            if (J > 100)
                J -= 10;        //若是熱量太大，再減10

            if (J < 0.05)
                J = 0;
            total_candles = total_candles * 9 / 10; //蠟燭數目打9折，且取整數

            lb_total_candles.Text = "N = " + total_candles.ToString();
            lb_total_energy.Text = "E = " + J.ToString();
        }

        float check_current_temperature()
        {
            update_energy();

            float current_temperature = 0;

            int T0 = 10;

            current_temperature = (T0 + J / 10.0f);
            if (current_temperature > 100)
                current_temperature = 100;

            return current_temperature;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            float kp = 3.2f;
            float ki = 0.4f;
            float kd = 0.6f;

            float real = 0;
            float error = 0;

            float pp = 0;
            float ii = 0;
            float dd = 0;
            float ii_old = 0;
            float error_old = 0;
            float pid = 0;

            string result = String.Format("{0,-15}{1,-15}{2,-15}{3,-15}{4,-15}{5,-15}{6,-15}{7,-15}", "step", "target", "real", "error", "pp", "ii", "dd", "pid");
            richTextBox1.Text += result + "\n";

            int i;
            for (i = 0; i < 300; i++)
            {
                //update_energy();

                real = check_current_temperature();

                error = target - real;

                pp = error;
                ii = error + ii_old;
                dd = error - error_old;

                pid = kp * pp + ki * ii + kd * dd;

                result = String.Format("{0,-15}{1,-15}{2,-15}{3,-15}{4,-15}{5,-15}{6,-15}{7,-15}", i.ToString(), target.ToString(), real.ToString(), error.ToString(),
                    pp.ToString(), ii.ToString(), dd.ToString(), pid.ToString());

                richTextBox1.Text += result + "\n";

                //richTextBox1.Text += i.ToString() + "\t\t" + ((int)target).ToString() + "\t" + ((int)real).ToString() + "\t" + ((int)error).ToString() + "\t";
                //richTextBox1.Text += ((int)pp).ToString() + "\t" + ((int)ii).ToString() + "\t" + ((int)dd).ToString() + "\t" + ((int)pid).ToString() + "\n";


                /*
                richTextBox1.Text += "t = " + i.ToString() + "\t" +
                    "T = " + target.ToString() + "\t" +
                    "N = " + total_candles.ToString() + "\t" +
                    "J = " + J.ToString() + "\t" +
                    "R = " + real.ToString() + "\t" +
                    "E = " + error.ToString() + "\n";
                */


                //處置方案
                if (i < 50)
                {
                    //total_candles += 25;
                }

                if (Math.Abs(pid) < 10)
                {
                    richTextBox1.Text += "OK\n";
                }
                else
                {
                    int add = (int)(pid / 30);

                    total_candles += add;
                    richTextBox1.Text += "add " + add.ToString() + "\n";


                }



                error_old = error;
                ii_old = ii;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            add_candles(100);
        }

        double x = 0;
        private const int POINTS_IN_AXIS = 36;      //製作動畫時X軸要保留的點數

        private void timer1_Tick(object sender, EventArgs e)
        {
            float real = check_current_temperature();
            lb_temperature.Text = real.ToString();
            //richTextBox1.Text += real.ToString() + "  ";

            double y;
            //y = 110 * sind(x);

            chart1.Series[0].Points.AddXY(x, real);

            if (chart1.Series[0].Points.Count > POINTS_IN_AXIS)
                chart1.Series[0].Points.RemoveAt(0);

            //製作動畫
            chart1.ChartAreas[0].AxisX.Minimum = chart1.Series[0].Points[0].XValue;
            chart1.ChartAreas[0].AxisX.Maximum = x;

            x++;


            float kp = float.Parse(tb_kp.Text);
            float ki = float.Parse(tb_ki.Text);
            float kd = float.Parse(tb_kd.Text);

            float target = 80;
            //float real = 0;
            float error = 0;

            float pp = 0;
            float ii = 0;
            float dd = 0;
            float ii_old = 0;
            float error_old = 0;
            float pid = 0;

            //string result = String.Format("{0,-15}{1,-15}{2,-15}{3,-15}{4,-15}{5,-15}{6,-15}{7,-15}", "step", "target", "real", "error", "pp", "ii", "dd", "pid");
            //richTextBox1.Text += result + "\n";

            error = target - real;

            pp = error;
            ii = error + ii_old;
            dd = error - error_old;

            pid = kp * pp + ki * ii + kd * dd;

            string result = String.Format("{0,-15}{1,-15}{2,-15}{3,-15}{4,-15}{5,-15}{6,-15}{7,-15}", target.ToString(), target.ToString(), real.ToString(), error.ToString(),
                pp.ToString(), ii.ToString(), dd.ToString(), pid.ToString());

            //richTextBox1.Text += result + "\n";

            lb_pid.Text = pid.ToString();


            //處置方案
            if (Math.Abs(pid) < 10)
            {
                richTextBox1.Text += "OK\n";
            }
            else
            {
                int add = (int)(pid / 2);

                if (add > 0)
                {
                    richTextBox1.Text += "增加 " + add.ToString() + "   ";
                    add_candles(add);
                }
                else
                {
                    richTextBox1.Text += "移除 " + (-add).ToString() + "   ";
                    remove_candles(-add);
                }

                //total_candles += add;
                //richTextBox1.Text += "add " + add.ToString() + "\n";
            }


            error_old = error;
            ii_old = ii;


        }

        int set_candles()
        {
            return total_candles;
        }

        void set_candles(int n)
        {
            total_candles = n;
            lb_total_candles.Text = total_candles.ToString();
            lb_total_candles.Text = "N = " + total_candles.ToString();
        }

        void add_candles(int n)
        {
            total_candles += n;
            lb_total_candles.Text = total_candles.ToString();
            lb_total_candles.Text = "N = " + total_candles.ToString();
        }

        void remove_candles(int n)
        {
            if (total_candles > n)
                total_candles -= n;
            else
                total_candles = 0;
            //total_candles -= n;

            lb_total_candles.Text = total_candles.ToString();
            lb_total_candles.Text = "N = " + total_candles.ToString();
        }

    }
}
