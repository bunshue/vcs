using vcs_MidiPlayer.HtMidi;
using System;
using System.Windows.Forms;

namespace vcs_MidiPlayer
{
    public partial class Form1 : Form
    {
        HewenqiMidi _hoverTreeMidi;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            _hoverTreeMidi = new HewenqiMidi();
            _hoverTreeMidi.Open();
        }

        private void button_shortPlay_Click(object sender, EventArgs e)
        {
            _hoverTreeMidi.ShortPlay(Convert.ToUInt32(numericUpDown_key.Value), Convert.ToUInt32(numericUpDown_volumn.Value), Convert.ToUInt32(numericUpDown_chenel.Value));
        }
    }
}

