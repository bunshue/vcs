using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Media;

namespace vcs_Clock8_Countdown
{
    public partial class Form1 : Form
    {
        // Initialize information about the event.
        private const string EventName = "End of the World";
        private DateTime EventDate = DateTime.Now + new TimeSpan(1, 13, 42, 59);

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            lblEvent.Text = EventName;
            this.Text = EventName + " at " + EventDate.ToString();
            tmrCheckTime.Enabled = true;
        }

        // Update the countdown.
        private void tmrCheckTime_Tick(object sender, EventArgs e)
        {
            TimeSpan remaining = EventDate - DateTime.Now;
            if (remaining.TotalSeconds < 1)
            {
                tmrCheckTime.Enabled = false;
                this.WindowState = FormWindowState.Maximized;
                this.TopMost = true;

                foreach (Control ctl in this.Controls)
                {
                    if (ctl == lblEvent)
                    {
                        ctl.Location = new Point(
                            (this.ClientSize.Width - ctl.Width) / 2,
                            (this.ClientSize.Height - ctl.Height) / 2);
                    }
                    else
                    {
                        ctl.Visible = false;
                    }
                }

                using (SoundPlayer player = new SoundPlayer(
                    Properties.Resources.tada))
                {
                    player.Play();
                }
            }
            else 
            {
                lblDays.Text = remaining.Days + " days";
                lblHours.Text = remaining.Hours + " hours";
                lblMinutes.Text = remaining.Minutes + " minutes";
                lblSeconds.Text = remaining.Seconds + " seconds";
            }
        }
    }
}
