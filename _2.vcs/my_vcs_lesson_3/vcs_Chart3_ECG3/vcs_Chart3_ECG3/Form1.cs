using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Windows.Forms.DataVisualization.Charting;

namespace vcs_Chart3_ECG3
{
    public partial class Form1 : Form
    {
        private Queue<double> ecgBuffer = new Queue<double>();
        private int fs = 500;   // 取樣率
        private int hr = 75;    // 心率
        private double t = 0.0; // 時間軸

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            richTextBox1.Size = new Size(300, 500);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            chart1.ChartAreas.Clear();  // 清除所有圖表區
            chart1.Series.Clear();  // 清除所有數列

            //圖表區設定
            ChartArea chartarea = new ChartArea("ChartArea1");
            chart1.ChartAreas.Add(chartarea);  // 將圖表區新增到圖表上

            // 設定邊界, 設定 X 軸顯示範圍 (例如 2 秒)
            chartarea.AxisX.Minimum = 0;  // 設定X軸最小值
            chartarea.AxisX.Maximum = 2;  // 設定X軸最大值
            chartarea.AxisY.Minimum = -1.5;  // 設定Y軸最小值
            chartarea.AxisY.Maximum = 1.5;  // 設定Y軸最大值

            Series series1 = new Series("心電圖", 500);  // 初始化數列1(名稱, 最大值)
            series1.ChartType = SeriesChartType.Line;
            chart1.Series.Add(series1);  // 將數列1新增到chart上

            // 設定 TrackBar
            trackBar1.Minimum = 40;
            trackBar1.Maximum = 120;
            trackBar1.Value = hr;
            //trackBar1.Scroll += TrackBar1_Scroll;
            label1.Text = "心率 : " + hr + " bpm";

            // 啟動 Timer
            timer1.Interval = 20; // 每 20ms 更新一次
            //timer1.Tick += Timer1_Tick;
            timer1.Start();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            hr = trackBar1.Value;
            label1.Text = "心率 : " + hr + " bpm";
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            // 每次更新加入一些新點
            int samplesPerTick = fs / (1000 / timer1.Interval); // 每次更新的點數            

            for (int i = 0; i < samplesPerTick; i++)
            {
                double value = GenerateECGPoint(t, hr);
                ecgBuffer.Enqueue(value);
                t += 1.0 / fs;

                // 保持 buffer 長度在 2 秒內
                if (ecgBuffer.Count > 2 * fs)
                    ecgBuffer.Dequeue();
            }

            label2.Text = samplesPerTick.ToString() + "   " + ecgBuffer.Count.ToString();

            // 更新 Chart
            chart1.Series[0].Points.Clear();

            int index = 0;
            foreach (var v in ecgBuffer)
            {
                chart1.Series[0].Points.AddXY(index / (double)fs, v);  // AddXY 二維加入
                index++;
            }
        }

        private double GenerateECGPoint(double time, int hr)
        {
            double rrInterval = 60.0 / hr;
            double beatTime = time % rrInterval;
            double value = 0.0;

            // P 波
            value += Math.Exp(-Math.Pow((beatTime - 0.1) / 0.01, 2)) * 0.1;
            // Q 波
            value += -Math.Exp(-Math.Pow((beatTime - 0.2) / 0.002, 2)) * 0.15;
            // R 波
            value += Math.Exp(-Math.Pow((beatTime - 0.22) / 0.002, 2)) * 1.0;
            // S 波
            value += -Math.Exp(-Math.Pow((beatTime - 0.25) / 0.002, 2)) * 0.25;
            // T 波
            value += Math.Exp(-Math.Pow((beatTime - 0.4) / 0.02, 2)) * 0.35;

            return value;
        }
    }
}
