using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Bottom_Control
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

        private void timer1_Tick(object sender, EventArgs e)
        {
            if(daProcessEllipse1.Value<100)
            {
                daProcessEllipse1.Value++;
            }
            else
            {
                daProcessEllipse1.Value -= 100;
            }
            if(daProcessWave1.Value<100)
            {
                daProcessWave1.Value++;
            }
            else
            {
                daProcessWave1.Value = 0;
            }

            if(daMeter1.Value<100)
            {
                daMeter1.Value++;
            }
            else
            {
                daMeter1.Value = 0;

            }
            if(daThermometer1.Value<100)
            {
                daThermometer1.Value++;
            }
            else
            {
                daThermometer1.Value = 0;
            }

            if (daAnalogMeter1.Value < 100)
            {
                daAnalogMeter1.Value++;
            }
            else
            {
                daAnalogMeter1.Value = 0;
            }

        }

    }
}
