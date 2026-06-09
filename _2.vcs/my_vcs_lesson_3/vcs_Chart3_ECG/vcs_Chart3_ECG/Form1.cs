using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Windows.Forms.DataVisualization.Charting;

namespace vcs_Chart3_ECG
{
    public partial class Form1 : Form
    {
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

            // 產生模擬心電圖資料
            List<double> ecgData = GenerateECG(3, 500, 75); // 10秒, 取樣率500Hz, 心率75 bpm

            // 畫出心電圖
            for (int i = 0; i < ecgData.Count; i++)
            {
                chart1.Series["ECGWave"].Points.AddXY(i / 500.0, ecgData[i]);
            }
        }

        private List<double> GenerateECG(double durationSec, int fs, int hr)
        {
            List<double> signal = new List<double>();
            double rrInterval = 60.0 / hr; // 心跳週期 (秒)
            int totalSamples = (int)(durationSec * fs);

            for (int i = 0; i < totalSamples; i++)
            {
                double t = i / (double)fs;
                double value = 0.0;

                // 每個心跳週期的波形
                double beatTime = t % rrInterval;

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

                signal.Add(value);
            }
            return signal;
        }
    }
}

