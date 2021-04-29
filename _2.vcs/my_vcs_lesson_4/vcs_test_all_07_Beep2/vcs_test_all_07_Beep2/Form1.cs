using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Threading;
using System.Runtime.InteropServices;

namespace vcs_test_all_07_Beep2
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

            protected  void Play(Note tune)
            {
                if (tune.NoteTone == Tone.REST)
                  Thread.Sleep((int)tune.NoteDuration);
                    else
                  Console.Beep((int)tune.NoteTone, (int)tune.NoteDuration);   
            }
            protected enum Tone
            {
                REST   = 0,
                A      = 220,
                B      = 247,
                C      = 262,
                D      = 294,
                E      = 330,
                F      = 349,
                G      = 392,
            }
            protected enum Duration
            {
                WHOLE     = 1200,
                HALF      = WHOLE/2,
                QUARTER   = HALF/2,
                EIGHTH    = QUARTER/2,
                SIXTEENTH = EIGHTH/2,
            }

            protected struct Note
            {
                Tone     toneVal;
                Duration durVal;
                public Note(Tone frequency, Duration time)
                {
                    toneVal = frequency;
                    durVal  = time;
                }
                public Tone NoteTone { get { return toneVal; } set { toneVal = value; } }
                public Duration NoteDuration { get { return durVal; } set { durVal = value; } }
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

            private void button2_Click(object sender, EventArgs e)
            {
                PlayMic(2); 
            }

            private void button3_Click(object sender, EventArgs e)
            {
                PlayMic(3); 
            }

            private void button4_Click(object sender, EventArgs e)
            {
                PlayMic(4); 
            }

            private void button5_Click(object sender, EventArgs e)
            {
                PlayMic(5); 
            }

            private void button6_Click(object sender, EventArgs e)
            {
                PlayMic(6); 
            }

            private void button7_Click(object sender, EventArgs e)
            {
                PlayMic(7); 
            }
            private void button1_Click(object sender, EventArgs e)
            {
                PlayMic(1);
            }

    }
}
