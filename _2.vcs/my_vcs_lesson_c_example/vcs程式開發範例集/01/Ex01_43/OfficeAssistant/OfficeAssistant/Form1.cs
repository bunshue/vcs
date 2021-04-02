using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using AgentObjects;

namespace OfficeAssistant
{
    public partial class Form1 : Form
    {
        IAgentCtlCharacterEx ICCE;
        IAgentCtlRequest ICR;
        string[] ws = new string[10] { "Acknowledge", "LookDown", "Sad", "Alert", "LookDownBlink", "Search", "Announce", "LookUp", "Think", "Blink"};
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            for (int i = 0; i < 10; i++)
            {
                listBox1.Items.Add(ws[i]);
            }
            ICR = axAgent1.Characters.Load("merlin", "merlin.acs");
            ICCE = axAgent1.Characters.Character("merlin");
            ICCE.Show(0);
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            ICCE.StopAll("");
            ICCE.Play(ws[listBox1.SelectedIndex]);
        }
    }
}