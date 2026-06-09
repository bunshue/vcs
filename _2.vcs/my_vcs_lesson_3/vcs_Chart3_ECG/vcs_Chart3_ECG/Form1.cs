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
            richTextBox1.Size = new Size(300, 500);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            chart1.ChartAreas.Clear();  // 清除所有圖表區
            chart1.Series.Clear();  // 清除所有數列

            //圖表區設定
            ChartArea chartarea = new ChartArea("ChartArea1");
            chart1.ChartAreas.Add(chartarea);  // 將圖表區新增到圖表上

            Series series1 = new Series("心電圖", 500);  // 初始化數列1(名稱, 最大值)
            series1.ChartType = SeriesChartType.Line;
            chart1.Series.Add(series1);  // 將數列1新增到chart上

            // 產生模擬心電圖資料
            List<double> ecgData = GenerateECG(3, 500, 75); // 10秒, 取樣率500Hz, 心率75 bpm

            // 畫出心電圖
            for (int i = 0; i < ecgData.Count; i++)
            {
                chart1.Series[0].Points.AddXY(i / 500.0, ecgData[i]);
            }
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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

