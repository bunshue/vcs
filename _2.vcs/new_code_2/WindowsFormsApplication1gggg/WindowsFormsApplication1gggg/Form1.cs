using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1gggg
{
    public partial class Form1 : Form
    {
        public enum SwitchState
        {
            On,
            Off
        }

        private SwitchState _state;
        public SwitchState State
        {
            get
            {
                return _state;
            }
            set
            {
                if (_state == value)
                    return;
                _state = value;
                AdjustOnOffButton();
            }
        }


        private void AdjustOnOffButton()
        {
            switch (State)
            {
                case SwitchState.On:
                    OnOffButton.Dock = DockStyle.Top;
                    break;
                case SwitchState.Off:
                    OnOffButton.Dock = DockStyle.Bottom;
                    break;
                default:
                    break;
            }
        }


        public void Toggle()
        {
            State = State == SwitchState.On ? SwitchState.Off : SwitchState.On;
        }



        public Form1()
        {
            InitializeComponent();
            State = SwitchState.Off;
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void OnOffButton_Click(object sender, EventArgs e)
        {
            Toggle();
        }

        private void Form1_SizeChanged(object sender, EventArgs e)
        {
            OnOffButton.Height = this.Height / 2;
        }
    }
}
