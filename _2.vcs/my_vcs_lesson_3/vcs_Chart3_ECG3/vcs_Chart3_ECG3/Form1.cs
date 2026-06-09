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
            // 初始化 Chart
            chart1.ChartAreas.Add(new ChartArea("ECG"));
            chart1.Series.Add("ECGWave");
            chart1.Series["ECGWave"].ChartType = SeriesChartType.Line;

            chart1.ChartAreas["ECG"].AxisX.Minimum = 0;
            chart1.ChartAreas["ECG"].AxisX.Maximum = 2;
            chart1.ChartAreas["ECG"].AxisY.Minimum = -1.5;
            chart1.ChartAreas["ECG"].AxisY.Maximum = 1.5;

            // 設定 TrackBar
            trackBar1.Minimum = 40;
            trackBar1.Maximum = 120;
            trackBar1.Value = hr;
            //trackBar1.Scroll += TrackBar1_Scroll;
            label1.Text = "心率 : " + hr + " bpm";

            // 啟動 Timer
            timer1.Interval = 20;
            //timer1.Tick += Timer1_Tick;
            timer1.Start();
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            hr = trackBar1.Value;
            label1.Text = "心率 : " + hr + " bpm";
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            int samplesPerTick = fs / (1000 / timer1.Interval);
            for (int i = 0; i < samplesPerTick; i++)
            {
                double value = GenerateECGPoint(t, hr);
                ecgBuffer.Enqueue(value);
                t += 1.0 / fs;

                if (ecgBuffer.Count > 2 * fs)
                    ecgBuffer.Dequeue();
            }

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

            value += Math.Exp(-Math.Pow((beatTime - 0.1) / 0.01, 2)) * 0.1;   // P 波
            value += -Math.Exp(-Math.Pow((beatTime - 0.2) / 0.002, 2)) * 0.15; // Q 波
            value += Math.Exp(-Math.Pow((beatTime - 0.22) / 0.002, 2)) * 1.0;  // R 波
            value += -Math.Exp(-Math.Pow((beatTime - 0.25) / 0.002, 2)) * 0.25; // S 波
            value += Math.Exp(-Math.Pow((beatTime - 0.4) / 0.02, 2)) * 0.35;   // T 波

            return value;
        }
    }
}
