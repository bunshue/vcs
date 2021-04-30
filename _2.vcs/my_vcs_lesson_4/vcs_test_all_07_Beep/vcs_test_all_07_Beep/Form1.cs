using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Threading;     //for Thread

namespace vcs_test_all_07_Beep
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {


        }
        
        private void button1_Click(object sender, EventArgs e)
        {
            Console.Beep(); //蜂鳴器發聲 262Hz, 500ms
            //Console.Beep(262, 500); //蜂鳴器發聲 262Hz, 500ms
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
            System.Media.SystemSounds.Asterisk.Play();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            System.Media.SystemSounds.Beep.Play();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            System.Media.SystemSounds.Exclamation.Play();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            System.Media.SystemSounds.Hand.Play();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            System.Media.SystemSounds.Question.Play();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button11_Click(object sender, EventArgs e)
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

    
    
    }
}
