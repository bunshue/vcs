using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using NAudio.Wave;

namespace vcs_AudioRecording2
{
    public partial class Form1 : Form
    {
        private WaveIn waveIn;
        private WaveFileWriter writer;
        private DateTime recordStartTime;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //啟動時列出所有麥克風
            comboBox1.Items.Clear();

            for (int i = 0; i < WaveIn.DeviceCount; i++)
            {
                WaveInCapabilities cap = WaveIn.GetCapabilities(i);
                comboBox1.Items.Add(cap.ProductName);
            }

            if (comboBox1.Items.Count > 0)
            {
                comboBox1.SelectedIndex = 0;
            }

            timer1.Interval = 1000;
        }

        //------------------------------------------------------------  # 60個

        //接收錄音資料
        private void waveIn_DataAvailable(object sender, WaveInEventArgs e)
        {
            if (writer != null)
            {
                writer.WriteData(e.Buffer, 0, e.BytesRecorded);

                writer.Flush();
            }

            int max = 0;

            for (int i = 0; i < e.BytesRecorded; i += 2)
            {
                short sample = BitConverter.ToInt16(e.Buffer, i);

                if (Math.Abs(sample) > max)
                {
                    max = Math.Abs(sample);
                }
            }

            int level = max * 100 / 32767;

            BeginInvoke(new MethodInvoker(delegate
            {
                if (level > 100)
                {
                    level = 100;
                }

                progressBar1.Value = level;
            }));
        }

        //錄音結束事件
        private void waveIn_RecordingStopped(object sender, EventArgs e)
        {
            timer1.Stop();

            if (waveIn != null)
            {
                waveIn.Dispose();
                waveIn = null;
            }

            if (writer != null)
            {
                writer.Dispose();
                writer = null;
            }

            progressBar1.Value = 0;

            MessageBox.Show("錄音完成");
        }

        //開始錄音
        private void button1_Click(object sender, EventArgs e)
        {
            if (waveIn != null)
            {
                return;
            }

            string filename = "tmp_Record" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".wav";

            waveIn = new WaveIn();

            waveIn.DeviceNumber = comboBox1.SelectedIndex;

            waveIn.WaveFormat = new WaveFormat(44100, 1);

            waveIn.DataAvailable += waveIn_DataAvailable;

            waveIn.RecordingStopped += waveIn_RecordingStopped;

            writer = new WaveFileWriter(filename, waveIn.WaveFormat);

            recordStartTime = DateTime.Now;

            timer1.Start();

            waveIn.StartRecording();

        }

        //停止錄音
        private void button2_Click(object sender, EventArgs e)
        {
            if (waveIn != null)
            {
                waveIn.StopRecording();
            }
        }

        //顯示錄音時間
        private void timer1_Tick(object sender, EventArgs e)
        {
            TimeSpan ts = DateTime.Now - recordStartTime;

            label1.Text = ts.ToString(@"hh\:mm\:ss");
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個



