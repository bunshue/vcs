using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PID2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int total_candles = 0;
        float J = 0;


        void update_energy()
        {
            J += total_candles * 2 / 2;
            //richTextBox1.Text += "J1 = " + J.ToString() + "\t";
            J = J * 8 / 10;
            if (J > 100)
                J -= 10;
            //richTextBox1.Text += "J2 = " + J.ToString() + "\n";

            total_candles = total_candles * 9 / 10;
        }

        float check_current_temperature()
        {
            float current_temperature = 0;

            int T0 = 10;

            current_temperature = (T0 + J / 10);
            if (current_temperature > 100)
                current_temperature = 100;

            return current_temperature;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            float kp = 3.2f;
            float ki = 0.4f;
            float kd = 0.6f;

            float target = 80;
            float real = 0;
            float error = 0;

            float pp = 0;
            float ii = 0;
            float dd = 0;
            float ii_old = 0;
            float error_old = 0;
            float pid = 0;

            string result = String.Format("{0,-15}{1,-15}{2,-15}{3,-15}{4,-15}{5,-15}{6,-15}{7,-15}", "step", "target", "real", "error", "pp", "ii", "dd", "pid");
            richTextBox1.Text += result + "\n";

            int i;
            for (i = 0; i < 300; i++)
            {
                update_energy();

                real = check_current_temperature();

                error = target - real;

                pp = error;
                ii = error + ii_old;
                dd = error - error_old;

                pid = kp * pp + ki * ii + kd * dd;

                result = String.Format("{0,-15}{1,-15}{2,-15}{3,-15}{4,-15}{5,-15}{6,-15}{7,-15}", i.ToString(), target.ToString(), real.ToString(), error.ToString(),
                    pp.ToString(), ii.ToString(), dd.ToString(), pid.ToString());

                richTextBox1.Text += result + "\n";

                //richTextBox1.Text += i.ToString() + "\t\t" + ((int)target).ToString() + "\t" + ((int)real).ToString() + "\t" + ((int)error).ToString() + "\t";
                //richTextBox1.Text += ((int)pp).ToString() + "\t" + ((int)ii).ToString() + "\t" + ((int)dd).ToString() + "\t" + ((int)pid).ToString() + "\n";


                /*
                richTextBox1.Text += "t = " + i.ToString() + "\t" +
                    "T = " + target.ToString() + "\t" +
                    "N = " + total_candles.ToString() + "\t" +
                    "J = " + J.ToString() + "\t" +
                    "R = " + real.ToString() + "\t" +
                    "E = " + error.ToString() + "\n";
                */


                //處置方案
                if (i < 50)
                {
                    //total_candles += 25;
                }

                if (Math.Abs(pid) < 10)
                {
                    richTextBox1.Text += "OK\n";
                }
                else
                {
                    int add = (int)(pid / 30);

                    total_candles += add;
                    richTextBox1.Text += "add " + add.ToString() + "\n";


                }



                error_old = error;
                ii_old = ii;
            }
        }
    }
}
