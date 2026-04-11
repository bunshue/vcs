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

namespace vcs_NAudio2
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
            if (output != null)
            {
                output.Dispose();
                output = null;
            }
            if (stream != null)
            {
                stream.Dispose();
                stream = null;
            }
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

            richTextBox1.Size = new Size(750, 340);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1000, 750);
            this.Text = "vcs_NAudio2";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private DirectSoundOut output = null;
        private BlockAlignReductionStream stream = null;

        private void button0_Click(object sender, EventArgs e)
        {
            WaveTone tone = new WaveTone(3000, 0.1);
            stream = new BlockAlignReductionStream(tone);

            output = new DirectSoundOut();
            output.Init(stream);
            output.Play();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (output != null)
            {
                output.Stop();
            }
        }

        //same
        //private DirectSoundOut output = null;
        //private BlockAlignReductionStream stream = null;

        private void button2_Click(object sender, EventArgs e)
        {
            //Play Wav 1

            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_Player\vcs_NAudio\tutorial1.wav";

            WaveChannel32 wave = new WaveChannel32(new WaveFileReader(filename));
            EffectStream effect = new EffectStream(wave);
            stream = new BlockAlignReductionStream(effect);

            output = new DirectSoundOut(200);
            output.Init(stream);
            output.Play();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //Play Wav 2
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

    public class WaveTone : WaveStream
    {
        private double frequency;
        private double amplitude;
        private double time;

        public WaveTone(double f, double a)
        {
            this.time = 0;
            this.frequency = f;
            this.amplitude = a;
        }

        public override long Position
        {
            get;
            set;
        }

        public override long Length
        {
            get { return long.MaxValue; }
        }

        public override WaveFormat WaveFormat
        {
            get { return new WaveFormat(44100, 16, 1); }
        }

        public override int Read(byte[] buffer, int offset, int count)
        {
            int samples = count / 2;
            for (int i = 0; i < samples; i++)
            {
                double sine = amplitude * Math.Sin(Math.PI * 2 * frequency * time);
                time += 1.0 / 44100;
                short truncated = (short)Math.Round(sine * (Math.Pow(2, 15) - 1));
                buffer[i * 2] = (byte)(truncated & 0x00ff);
                buffer[i * 2 + 1] = (byte)((truncated & 0xff00) >> 8);
            }

            return count;
        }
    }

}
