using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double length, width; // 長度  寬度

            length = Convert.ToDouble(textBox1.Text);
            width = Convert.ToDouble(textBox2.Text);

            double pin; // 坪數
            pin = length * width * 0.3025;

            label3.Text = "坪數：" + pin.ToString();
        }
    }
}
