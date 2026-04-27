using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using AForge;
using AForge.Controls;

/*
AForge.Controls.Chart 測試
*/

namespace vcs_AForgeTest2
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

        private void button1_Click(object sender, EventArgs e)
        {
            chart4.RemoveAllDataSeries();

            chart4.AddDataSeries("map", Color.Red, Chart.SeriesType.Dots, 10, false);
            chart4.RangeX = new Range(0, 1000);
            chart4.RangeY = new Range(0, 1000);

            Random rand = new Random((int)DateTime.Now.Ticks);

            int citiesCount = 10;  // 個數
            double[,] map4 = new double[citiesCount, 2];

            for (int i = 0; i < citiesCount; i++)
            {
                map4[i, 0] = rand.Next(1001);
                map4[i, 1] = rand.Next(1001);
            }

            chart4.UpdateDataSeries("map", map4);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            chart4.UpdateDataSeries("map", null);
        }
    }
}

//chart4.AddDataSeries("path", Color.Blue, Chart.SeriesType.Line, 1, false);
//chart4.AddDataSeries("path", Color.Blue, Chart.SeriesType.Line, 1, false);

