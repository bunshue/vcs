using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_RandomColor
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
            pictureBox1.BackColor = GetRandomColor();

        }

        //隨機顏色如下
        public static Color GetRandomColor()
        {
            Random randomFirst = new Random((int)DateTime.Now.Ticks);
            System.Threading.Thread.Sleep(300);
            Random randomSencond = new Random((int)DateTime.Now.Ticks);
            System.Threading.Thread.Sleep(300);
            Random randomThird = new Random((int)DateTime.Now.Ticks);
            int intRed = randomFirst.Next(256);
            int intGreen = randomSencond.Next(256);
            int intBlue = randomThird.Next(256);
            return Color.FromArgb(intRed, intGreen, intBlue);
        }
    }
}
