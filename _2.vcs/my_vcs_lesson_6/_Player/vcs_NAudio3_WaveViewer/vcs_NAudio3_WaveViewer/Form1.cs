using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//參考/加入參考/NAudio.dll

using NAudio.Wave;

namespace vcs_NAudio3_WaveViewer
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            /* 要先清掉 chart1的東西
            legend1.Name = "Legend1";
            this.chart1.Legends.Add(legend1);

            series1.ChartArea = "ChartArea1";
            series1.Legend = "Legend1";
            series1.Name = "Series1";
            this.chart1.Series.Add(series1);
            */
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
        }

        private void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            waveViewer1.Size = new Size(750, 160);
            waveViewer1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            chart1.Size = new Size(750, 160);
            chart1.Location = new Point(x_st + dx * 1, y_st + dy * 0+170);

            richTextBox1.Size = new Size(750, 340);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1000, 750);
            this.Text = "vcs_NAudio3_WaveViewer";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            string wav_filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_Player\vcs_NAudio\tutorial1.wav";

            waveViewer1.SamplesPerPixel = 450;
            waveViewer1.WaveStream = new NAudio.Wave.WaveFileReader(wav_filename);

            chart1.Series.Add("wave");
            chart1.Series["wave"].ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.FastLine;
            chart1.Series["wave"].ChartArea = "ChartArea1";

            NAudio.Wave.WaveChannel32 wave = new NAudio.Wave.WaveChannel32(new NAudio.Wave.WaveFileReader(wav_filename));

            byte[] buffer = new byte[16384];
            int read = 0;

            while (wave.Position < wave.Length)
            {
                read = wave.Read(buffer, 0, 16384);

                for (int i = 0; i < read / 4; i++)
                {
                    chart1.Series["wave"].Points.Add(BitConverter.ToSingle(buffer, i * 4));
                }
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            /*
            string wav_filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_Player\vcs_NAudio\tutorial1.wav";

            customWaveViewer1.WaveStream = new NAudio.Wave.WaveFileReader(wav_filename);
            customWaveViewer1.FitToScreen();
            */
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }
    }
}
