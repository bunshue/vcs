using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using RunnerSpace;

namespace _14._6_s2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private Turtle turtle;
        private Rabbit rabbit;

        private void Form1_Load(object sender, EventArgs e)
        {
            reset();
        }

        private void reset() {
            this.turtle = new Turtle(4, 3);
            this.rabbit = new Rabbit(15, 5);
            turtleLabel.Left = 12;
            rabbitLabel.Left = 12;
            startButton.Enabled = true;
            timer1.Stop();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            turtleLabel.Left += this.turtle.step();
            rabbitLabel.Left += this.rabbit.step();

            if (turtleLabel.Left > 320) {
                reset();
                if (turtleButton.Checked == true)
                    MessageBox.Show("烏龜贏了! 恭喜您猜對了!");
                else
                    MessageBox.Show("烏龜贏了! 但您猜錯了");
            }
            else if (rabbitLabel.Left > 320) {
                reset();
                if (rabbitButton.Checked == true)
                    MessageBox.Show("兔子贏了! 恭喜您猜對了!");
                else
                    MessageBox.Show("兔子贏了! 但您猜錯了");
            }
        }

        private void startButton_Click(object sender, EventArgs e)
        {
            startButton.Enabled = false;
            timer1.Start();
        }


    }
}
