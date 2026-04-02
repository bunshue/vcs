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

namespace vcs_NAudio
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

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            DisposeWave();
        }

        private void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

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

            richTextBox1.Size = new Size(750, 340);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1000, 750);
            this.Text = "vcs_NAudio";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private NAudio.Wave.WaveFileReader wave = null;
        private NAudio.Wave.DirectSoundOut output = null;
        private NAudio.Wave.BlockAlignReductionStream stream = null;

        private void button0_Click(object sender, EventArgs e)
        {
            //使用 NAudio 播放 wave檔, 使用 WaveFileReader

            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_Player\vcs_NAudio\tutorial1.wav";

            wave = new NAudio.Wave.WaveFileReader(filename);
            output = new NAudio.Wave.DirectSoundOut();
            output.Init(new NAudio.Wave.WaveChannel32(wave));
            output.Play();
        }

        private void DisposeWave()
        {
            if (output != null)
            {
                if (output.PlaybackState == NAudio.Wave.PlaybackState.Playing)
                {
                    output.Stop();
                }
                output.Dispose();
                output = null;
            }
            if (wave != null)
            {
                wave.Dispose();
                wave = null;
            }
            if (stream != null)
            {
                stream.Dispose();
                stream = null;
            }
        }


        private void button1_Click(object sender, EventArgs e)
        {
            //使用 NAudio 播放 wave檔, 使用 BlockAlignReductionStream

            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_Player\vcs_NAudio\tutorial1.wav";

            NAudio.Wave.WaveStream pcm = new NAudio.Wave.WaveChannel32(new NAudio.Wave.WaveFileReader(filename));
            stream = new NAudio.Wave.BlockAlignReductionStream(pcm);

            output = new NAudio.Wave.DirectSoundOut();
            output.Init(stream);
            output.Play();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //使用 NAudio 播放 mp3檔

            string filename = @"D:\_git\vcs\_1.data\______test_files1\_mp3\02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3";

            DisposeWave();

            NAudio.Wave.WaveStream pcm = NAudio.Wave.WaveFormatConversionStream.CreatePcmStream(new NAudio.Wave.Mp3FileReader(filename));
            stream = new NAudio.Wave.BlockAlignReductionStream(pcm);

            output = new NAudio.Wave.DirectSoundOut();
            output.Init(stream);
            output.Play();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //mp3轉wave

            string mp3_filename = @"D:\_git\vcs\_1.data\______test_files1\_mp3\02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3";
            string wave_filename = "tmp_aaaaa.wav";

            using (Mp3FileReader mp3 = new Mp3FileReader(mp3_filename))
            {
                using (WaveStream pcm = WaveFormatConversionStream.CreatePcmStream(mp3))
                {
                    WaveFileWriter.CreateWaveFile(wave_filename, pcm);
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //停止
            output.Stop();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //播放
            output.Play();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //暫停
            output.Pause();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            if (output == null)
                return;

            //狀態
            if (output.PlaybackState == NAudio.Wave.PlaybackState.Playing)
                richTextBox1.Text += "播放中\n";
            else if (output.PlaybackState == NAudio.Wave.PlaybackState.Paused)
                richTextBox1.Text += "暫停中\n";
            else if (output.PlaybackState == NAudio.Wave.PlaybackState.Stopped)
                richTextBox1.Text += "停止\n";
            else
                richTextBox1.Text += "XXXXXX\n";
        }
    }
}
