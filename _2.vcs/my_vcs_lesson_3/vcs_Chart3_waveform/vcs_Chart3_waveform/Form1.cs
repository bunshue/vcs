using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Windows.Forms.DataVisualization.Charting;

namespace vcs_Chart3_waveform
{
    public partial class Form1 : Form
    {
        private Queue<double> ecgBuffer = new Queue<double>();
        private int fs = 500;  // 取樣率
        private int hr = 60;  // 心率
        private double t = 0.0;  // 時間軸
        private int total_seconds = 3;  // 顯示時間

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            chart1.ChartAreas.Clear();  // 清除所有圖表區
            chart1.Series.Clear();  // 清除所有數列

            //圖表區設定
            ChartArea chartarea = new ChartArea("ChartArea1");
            chart1.ChartAreas.Add(chartarea);  // 將圖表區新增到圖表上

            // 設定邊界, 設定 X 軸顯示範圍 (例如 total_seconds 秒, 畫面保持最後 total_seconds 秒)
            chartarea.AxisX.Minimum = 0;  // 設定X軸最小值
            chartarea.AxisX.Maximum = total_seconds;  // 設定X軸最大值(秒)
            chartarea.AxisY.Minimum = -1.5;  // 設定Y軸最小值
            chartarea.AxisY.Maximum = 1.5;  // 設定Y軸最大值

            Series series1 = new Series("心電圖", 500);  // 初始化數列1(名稱, 最大值)
            series1.ChartType = SeriesChartType.Line;
            chart1.Series.Add(series1);  // 將數列1新增到chart上

            // 設定 TrackBar
            trackBar1.Minimum = 40;
            trackBar1.Maximum = 120;
            trackBar1.Value = hr;
            label1.Text = "心率 : " + hr + " bpm";

            trackBar2.Minimum = 100;
            trackBar2.Maximum = 1000;
            trackBar2.Value = fs;
            label2.Text = "取樣率 : " + fs + " Hz";


            label3.Text = "更新率 : " + fs + " Hz";

            // 啟動 Timer
            timer1.Interval = 20; // 每 20ms 更新一次
            //timer1.Tick += Timer1_Tick;
            timer1.Start();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            chart1.Size = new Size(600, 480);
            chart1.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            groupBox1.Size = new Size(110, 200);
            groupBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            trackBar1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            trackBar2.Location = new Point(x_st + dx * 4, y_st + dy * 0 + 40);
            trackBar3.Location = new Point(x_st + dx * 4, y_st + dy * 0 + 80);
            numericUpDown_time.Location = new Point(x_st + dx * 4, y_st + dy * 0 + 120);
            label1.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 0);
            label2.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 0 + 50);
            label3.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 0 + 100);
            label4.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 0 + 150);

            richTextBox1.Size = new Size(720, 480);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            y_st = 25;
            dy = 25;
            radioButton0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            radioButton1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            radioButton2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            radioButton3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            radioButton4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            btn_play.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            btn_pause.Location = new Point(x_st + dx * 0+50, y_st + dy * 5);

            this.Size = new Size(1400, 750);
            this.Text = "vcs_Chart3_waveform";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            hr = trackBar1.Value;
            label1.Text = "心率 : " + hr + " bpm";
        }

        private void trackBar2_Scroll(object sender, EventArgs e)
        {
            fs = trackBar2.Value;
            label2.Text = "取樣率 : " + fs + " Hz";
        }

        //------------------------------------------------------------  # 60個

        int index = 0;

        private void timer1_Tick(object sender, EventArgs e)
        {
            // 每次更新加入一些新點
            int samplesPerTick = fs / (1000 / timer1.Interval); // 每次更新的點數            

            for (int i = 0; i < samplesPerTick; i++)
            {
                double value = GenerateSignal(t, hr);
                ecgBuffer.Enqueue(value);
                t += 1.0 / fs;  // 每一格的時間 為 1/fs

                // 保持 buffer 長度在 total_seconds 秒內
                if (ecgBuffer.Count > total_seconds * fs)
                {
                    ecgBuffer.Dequeue();
                }
            }

            label4.Text = samplesPerTick.ToString() + "   " + ecgBuffer.Count.ToString();

            // 更新 Chart
            chart1.Series[0].Points.Clear();

            double xx = 0;
            foreach (var v in ecgBuffer)
            {
                xx = index / (double)fs;
                chart1.Series[0].Points.AddXY(xx, v);  // AddXY 二維加入
                index++;
            }
            chart1.ChartAreas[0].AxisX.Minimum = xx - total_seconds;  // 畫面保持最後 total_seconds 秒
            chart1.ChartAreas[0].AxisX.Maximum = xx;
        }

        private double GenerateSignal(double time, int hr)
        {
            double Period = 60.0 / hr;  // 一次心跳的時間, 一個週期
            double beatTime = time % Period;  // 測試時間
            double value = 0.0;

            if (radioButton0.Checked == true)
            {
                //心電圖
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
            }
            else if (radioButton1.Checked == true)
            {
                //正弦波
                value = Math.Sin(2 * Math.PI * beatTime / Period);
            }
            else if (radioButton2.Checked == true)
            {
                //三角波
                if (beatTime < Period / 2)
                {
                    value = beatTime;
                }
                else
                {
                    value = 1.0 - beatTime;
                }
            }
            else if (radioButton3.Checked == true)
            {
                //方波
                if (beatTime < Period / 2)
                {
                    value = 1.0;
                }
                else
                {
                    value = -1.0;
                }

            }
            else if (radioButton4.Checked == true)
            {
                //市電
            }
            return value;
        }

        private void numericUpDown_time_ValueChanged(object sender, EventArgs e)
        {
            total_seconds = (int)numericUpDown_time.Value;
        }

        private void radioButton_CheckedChanged(object sender, EventArgs e)
        {
            //調整Y邊界

            if (radioButton0.Checked == true)
            {
                richTextBox1.Text += "心電圖\n";
            }
            else if (radioButton1.Checked == true)
            {
                richTextBox1.Text += "正弦波\n";
            }
            else if (radioButton2.Checked == true)
            {
                richTextBox1.Text += "三角波\n";
            }
            else if (radioButton3.Checked == true)
            {
                richTextBox1.Text += "方波\n";
            }
            else if (radioButton4.Checked == true)
            {
                richTextBox1.Text += "市電\n";
            }
            else
            {
                richTextBox1.Text += "XXXXXX\n";
            }
        }

        private void btn_play_Click(object sender, EventArgs e)
        {
            timer1.Enabled = true;
        }

        private void btn_pause_Click(object sender, EventArgs e)
        {
            timer1.Enabled = false;
        }
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


