using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace PlayBeepVoice
{
    public partial class PlayVoice : Form
    {
        public PlayVoice()
        {
            InitializeComponent();
        }

        private void playHand_Click(object sender,EventArgs e)
        {
            System.Media.SystemSounds.Hand.Play();
        }

        private void playBeep_Click(object sender,EventArgs e)
        {
            System.Media.SystemSounds.Beep.Play();
        }

        private void playExclamation_Click(object sender,EventArgs e)
        {
            System.Media.SystemSounds.Exclamation.Play();
        }

        private void playAsterisk_Click(object sender,EventArgs e)
        {
            System.Media.SystemSounds.Asterisk.Play();
        }

        private void playQuestion_Click(object sender,EventArgs e)
        {
            System.Media.SystemSounds.Question.Play();
        }
    }
}
