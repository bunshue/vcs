using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;
using System.Runtime.InteropServices;

//參考/加入參考/NAudio.dll

using NAudio.Wave;
using NAudio.CoreAudioApi;

using DirectShowLib;

namespace vcs_AudioRecording
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
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            richTextBox1.Size = new Size(400, 690);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //針對某控件的邊緣 設定表單大小
            this.ClientSize = new Size(richTextBox1.Right + 10, richTextBox1.Bottom + 10);
            this.Text = "vcs_AudioRecording";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        class WinMM
        {
            [DllImport("winmm.dll")]
            public static extern uint waveInGetNumDevs();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //查找音效裝置

            richTextBox1.Text += "查找音效裝置------------------------------------------------------------\n";  // 60個

            ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_SoundDevice");

            foreach (ManagementObject obj in searcher.Get())
            {
                richTextBox1.Text += "找到 : " + obj["Name"] + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            // 使用 WinMM (舊 API)

            uint count = WinMM.waveInGetNumDevs();
            richTextBox1.Text += "錄音裝置數量：" + count.ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //使用 NAudio

            MMDeviceEnumerator enumerator = new MMDeviceEnumerator();

            MMDeviceCollection devices =
                enumerator.EnumerateAudioEndPoints(
                    DataFlow.Capture,
                    DeviceState.Active);

            richTextBox1.Text += "麥克風數量：" + devices.Count + "\n";

            foreach (MMDevice device in devices)
            {
                richTextBox1.Text += device.FriendlyName + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //使用 DirectShowLib;

            DsDevice[] devices2 =
                DsDevice.GetDevicesOfCat(FilterCategory.AudioInputDevice);

            Console.WriteLine(devices2.Length);
            richTextBox1.Text += "麥克風數量：" + devices2.Length + "\n";

            foreach (DsDevice d in devices2)
            {
                Console.WriteLine(d.Name);
                richTextBox1.Text += d.Name + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



        }

        private void button1_Click(object sender, EventArgs e)
        {
            waveSource = new WaveIn();
            for (int i = 0; i < WaveIn.DeviceCount; i++)
            {
                WaveInCapabilities cap = WaveIn.GetCapabilities(i);

                Console.WriteLine(i + " : " + cap.ProductName);
            }

            //錄音前指定裝置：
            waveSource.DeviceNumber = 1;  // 即可使用第 2 支麥克風。
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

        //------------------------------------------------------------  # 60個

        private WaveIn waveSource;
        private WaveFileWriter waveFile;

        //接收錄音資料
        private void waveSource_DataAvailable(object sender, WaveInEventArgs e)
        {
            if (waveFile != null)
            {
                waveFile.WriteData(e.Buffer, 0, e.BytesRecorded);
                waveFile.Flush();
            }
        }

        //錄音結束事件
        private void waveSource_RecordingStopped(object sender, EventArgs e)
        {
            if (waveSource != null)
            {
                waveSource.Dispose();
                waveSource = null;
            }

            if (waveFile != null)
            {
                waveFile.Dispose();
                waveFile = null;
            }

            MessageBox.Show("錄音完成");
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //st
            if (waveSource != null)
            {
                MessageBox.Show("已經在錄音中");
                return;
            }

            string filename = @"tmp_Record.wav";

            waveSource = new WaveIn();

            waveSource.WaveFormat = new WaveFormat(44100, 1);

            waveSource.DataAvailable += waveSource_DataAvailable;
            waveSource.RecordingStopped += new EventHandler(waveSource_RecordingStopped);

            waveFile = new WaveFileWriter(filename, waveSource.WaveFormat);

            waveSource.StartRecording();

        }

        private void button11_Click(object sender, EventArgs e)
        {
            //sp

            if (waveSource != null)
            {
                waveSource.StopRecording();
            }
        }

        //------------------------------------------------------------  # 60個

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
        {
        }

        private void button21_Click(object sender, EventArgs e)
        {
        }

        private void button22_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {
        }

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
        }

        private void button27_Click(object sender, EventArgs e)
        {
        }

        private void button28_Click(object sender, EventArgs e)
        {
        }

        private void button29_Click(object sender, EventArgs e)
        {
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

