using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;     // for Thread
using System.Media;         // for SystemSounds     SystemSounds類別、SoundPlayer類別

namespace vcs_AudioVideoTest2
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

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 12;
            y_st = 12;
            dx = 190 + 10;
            dy = 40 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);

            button7.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button8.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 6);

            groupBox3.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 8 + 20);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Console.Beep(); //蜂鳴器發聲 262Hz, 500ms
            //Console.Beep(262, 500); //蜂鳴器發聲 262Hz, 500ms
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        //參考https://msdn.microsoft.com/zh-tw/library/4fe3hdb1(v=vs.110).aspx
        private void button3_Click(object sender, EventArgs e)
        {
            // Declare the first few notes of the song, "Mary Had A Little Lamb".
            Note[] Mary = 
            {
            new Note(Tone.B, Duration.QUARTER),
            new Note(Tone.A, Duration.QUARTER),
            new Note(Tone.GbelowC, Duration.QUARTER),
            new Note(Tone.A, Duration.QUARTER),
            new Note(Tone.B, Duration.QUARTER),
            new Note(Tone.B, Duration.QUARTER),
            new Note(Tone.B, Duration.HALF),
            new Note(Tone.A, Duration.QUARTER),
            new Note(Tone.A, Duration.QUARTER),
            new Note(Tone.A, Duration.HALF),
            new Note(Tone.B, Duration.QUARTER),
            new Note(Tone.D, Duration.QUARTER),
            new Note(Tone.D, Duration.HALF)
            };
            // Play the song
            Play(Mary);
        }

        // Play the notes in a song.
        //protected static void Play(Note[] tune)
        void Play(Note[] tune)
        {
            foreach (Note n in tune)
            {
                if (n.NoteTone == Tone.REST)
                    Thread.Sleep((int)n.NoteDuration);
                else
                {
                    richTextBox1.Text += "freq=" + ((int)n.NoteTone).ToString() + ", time=" + ((int)n.NoteDuration).ToString() + "\n";
                    Console.Beep((int)n.NoteTone, (int)n.NoteDuration);
                }
            }
        }

        // Define the frequencies of notes in an octave, as well as 
        // silence (rest).
        protected enum Tone
        {
            REST = 0,
            GbelowC = 196,
            A = 220,        //DO    261.63Hz
            Asharp = 233,
            B = 247,        //RE    293.66Hz
            C = 262,        //MI    329.63Hz
            Csharp = 277,
            D = 294,        //FA    349.23Hz
            Dsharp = 311,
            E = 330,        //SO    392.00Hz
            F = 349,        //LA    440.00Hz
            Fsharp = 370,
            G = 392,        //SI    493.88Hz
            Gsharp = 415,
            A2 = 220,       //DO2   523.26Hz
        }

        // Define the duration of a note in units of milliseconds.
        protected enum Duration
        {
            WHOLE = 1200,
            HALF = WHOLE / 2,
            QUARTER = HALF / 2,
            EIGHTH = QUARTER / 2,
            SIXTEENTH = EIGHTH / 2,
        }

        // Define a note as a frequency (tone) and the amount of 
        // time (duration) the note plays.
        protected struct Note
        {
            Tone toneVal;
            Duration durVal;

            // Define a constructor to create a specific note.
            public Note(Tone frequency, Duration time)
            {
                toneVal = frequency;
                durVal = time;
            }

            // Define properties to return the note's tone and duration.
            public Tone NoteTone
            {
                get
                {
                    return toneVal;
                }
                set
                {
                    toneVal = value;
                }
            }
            public Duration NoteDuration
            {
                get
                {
                    return durVal;
                }
                set
                {
                    durVal = value;
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            // Declare the first few notes of the song, "Do Re Mi".
            Note[] DoReMi = 
            {
            new Note(Tone.A, Duration.EIGHTH),
            new Note(Tone.B, Duration.EIGHTH),
            new Note(Tone.C, Duration.EIGHTH),
            new Note(Tone.D, Duration.EIGHTH),
            new Note(Tone.E, Duration.EIGHTH),
            new Note(Tone.F, Duration.EIGHTH),
            new Note(Tone.G, Duration.EIGHTH)
            };
            // Play the song
            Play(DoReMi);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            SystemSounds.Asterisk.Play();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            SystemSounds.Beep.Play();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            SystemSounds.Exclamation.Play();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            SystemSounds.Hand.Play();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            SystemSounds.Question.Play();
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //C# 演奏月亮代表我的心

            //racket 定義節拍
            const int one = 600;//一拍
            const int half = 300;//半拍
            const int four_one = 150;//1/4拍
            const int onedot = 450;//附點音符
            ////note   定義音符
            //const int mnote1 = 440;//do
            //const int mnote2 = 495;//re
            //const int mnote3 = 550;//mi
            //const int mnote4 = 587;//fa
            //const int mnote5 = 660;//so
            //const int mnote6 = 733;//la
            //const int mnote7 = 825;//si

            //const int lnote5 = 325;

            #region
            //low note   低音區
            const int lnote1 = 262;
            const int lnote2 = 294;
            const int lnote3 = 330;
            const int lnote4 = 349;
            const int lnote5 = 392;
            const int lnote6 = 440;
            const int lnote7 = 494;
            //mid note   中音區
            const int mnote1 = 523;
            const int mnote2 = 578;
            const int mnote3 = 659;
            const int mnote4 = 698;
            const int mnote5 = 784;
            const int mnote6 = 880;
            const int mnote7 = 988;
            //hight note   高音區
            const int hnote1 = 1046;
            const int hnote2 = 1175;
            const int hnote3 = 1318;
            const int hnote4 = 1397;
            const int hnote5 = 1568;
            const int hnote6 = 1760;
            const int hnote7 = 1976;
            #endregion

            //月亮代表我的心
            Console.Beep(lnote5, half);

            Console.Beep(mnote1, onedot);
            Console.Beep(mnote3, half);
            Console.Beep(mnote5, onedot);
            Console.Beep(mnote1, half);

            Console.Beep(lnote7, onedot);
            Console.Beep(mnote3, half);
            Console.Beep(mnote5, onedot);
            Console.Beep(mnote5, half);


            Console.Beep(mnote6, onedot);
            Console.Beep(mnote7, half);
            Console.Beep(hnote1, onedot);
            Console.Beep(mnote6, half);

            Console.Beep(mnote5, one);
            System.Threading.Thread.Sleep(one);
            System.Threading.Thread.Sleep(one);
            Console.Beep(mnote3, half);
            Console.Beep(mnote2, half);

            Console.Beep(mnote1, onedot);
            Console.Beep(mnote1, half);
            Console.Beep(mnote1, half);
            Console.Beep(mnote1, one);
            Console.Beep(mnote3, half);
            Console.Beep(mnote2, half);

            Console.Beep(mnote1, onedot);
            Console.Beep(mnote1, half);
            Console.Beep(mnote1, half);
            Console.Beep(mnote1, one);
            Console.Beep(mnote2, half);
            Console.Beep(mnote3, half);


            Console.Beep(mnote2, onedot);
            Console.Beep(mnote1, half);
            Console.Beep(lnote6, one);
            Console.Beep(mnote2, half);
            Console.Beep(mnote3, half);

            Console.Beep(mnote2, one);
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void bt_play_tone_Click(object sender, EventArgs e)
        {
            int freq = int.Parse(txtFrequency.Text);
            int duration = int.Parse(txtDuration.Text);

            System.Console.Beep(freq, duration);
        }

        //PC喇叭音效 ST
        protected void Play(Note tune)
        {
            if (tune.NoteTone == Tone.REST)
                Thread.Sleep((int)tune.NoteDuration);
            else
                Console.Beep((int)tune.NoteTone, (int)tune.NoteDuration);
        }

        private void PlayMic(int a)
        {
            Note note = new Note();
            switch (a)
            {
                case 1:
                    note.NoteTone = Tone.A;
                    break;
                case 2:
                    note.NoteTone = Tone.B;
                    break;
                case 3:
                    note.NoteTone = Tone.C;
                    break;
                case 4:
                    note.NoteTone = Tone.D;
                    break;
                case 5:
                    note.NoteTone = Tone.E;
                    break;
                case 6:
                    note.NoteTone = Tone.F;
                    break;
                case 7:
                    note.NoteTone = Tone.G;
                    break;
                default:
                    break;
            }
            if (this.radioButton1.Checked)
            {
                note.NoteDuration = Duration.WHOLE;
            }
            else if (this.radioButton2.Checked)
            {
                note.NoteDuration = Duration.HALF;
            }
            else if (this.radioButton3.Checked)
            {
                note.NoteDuration = Duration.QUARTER;
            }
            else if (this.radioButton4.Checked)
            {
                note.NoteDuration = Duration.EIGHTH;
            }
            else if (this.radioButton5.Checked)
            {
                note.NoteDuration = Duration.SIXTEENTH;
            }
            Play(note);
        }

        private void bt1_Click(object sender, EventArgs e)
        {
            PlayMic(1);
        }

        private void bt2_Click(object sender, EventArgs e)
        {
            PlayMic(2);
        }

        private void bt3_Click(object sender, EventArgs e)
        {
            PlayMic(3);
        }

        private void bt4_Click(object sender, EventArgs e)
        {
            PlayMic(4);
        }

        private void bt5_Click(object sender, EventArgs e)
        {
            PlayMic(5);
        }

        private void bt6_Click(object sender, EventArgs e)
        {
            PlayMic(6);
        }

        private void bt7_Click(object sender, EventArgs e)
        {
            PlayMic(7);
        }
        //PC喇叭音效 SP

        private void bt_system_sound0_Click(object sender, EventArgs e)
        {
            SystemSounds.Asterisk.Play();
        }

        private void bt_system_sound1_Click(object sender, EventArgs e)
        {
            SystemSounds.Beep.Play();
        }

        private void bt_system_sound2_Click(object sender, EventArgs e)
        {
            SystemSounds.Exclamation.Play();
        }

        private void bt_system_sound3_Click(object sender, EventArgs e)
        {
            SystemSounds.Hand.Play();
        }

        private void bt_system_sound4_Click(object sender, EventArgs e)
        {
            SystemSounds.Question.Play();
        }
    }
}
