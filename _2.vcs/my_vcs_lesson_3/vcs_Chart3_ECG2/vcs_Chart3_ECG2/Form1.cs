using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Windows.Forms.DataVisualization.Charting;

namespace vcs_Chart3_ECG2
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
            // 初始化 Chart
            chart1.ChartAreas.Add(new ChartArea("ECG"));
            chart1.Series.Add("ECGWave");
            chart1.Series["ECGWave"].ChartType = SeriesChartType.Line;

            // 設定 X 軸顯示範圍 (例如 2 秒)
            chart1.ChartAreas["ECG"].AxisX.Minimum = 0;
            chart1.ChartAreas["ECG"].AxisX.Maximum = 2;
            chart1.ChartAreas["ECG"].AxisY.Minimum = -1.5;
            chart1.ChartAreas["ECG"].AxisY.Maximum = 1.5;

            // 啟動 Timer
            timer1.Interval = 20; // 每 20ms 更新一次
            timer1.Start();
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

            // 更新 Chart
            chart1.Series["ECGWave"].Points.Clear();
            int index = 0;
            foreach (var v in ecgBuffer)
            {
                chart1.Series["ECGWave"].Points.AddXY(index / (double)fs, v);
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
