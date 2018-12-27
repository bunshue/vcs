using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Device.Location;

namespace vcs_test_all_25_GeoCoordinate
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //台北車站	25.047778, 121.517033 
            //新竹車站	24.801604, 120.971655
            GeoCoordinate station_tpe = new GeoCoordinate(25.047778, 121.517033);
            GeoCoordinate station_hsc = new GeoCoordinate(24.801604, 120.971655);
            double distanceInKm = station_tpe.GetDistanceTo(station_hsc) / 1000;

            richTextBox1.Text += "\n";
            richTextBox1.Text += "台北車站：\n";
            richTextBox1.Text += "東經：" + station_tpe.Longitude.ToString() + "度\n";
            richTextBox1.Text += "北緯：" + station_tpe.Latitude.ToString() + "度\n";
            richTextBox1.Text += "有無其他資訊：" + station_tpe.IsUnknown.ToString() + "\n\n";

            richTextBox1.Text += "新竹車站：\n";
            richTextBox1.Text += "東經：" + station_hsc.Longitude.ToString() + "度\n";
            richTextBox1.Text += "北緯：" + station_hsc.Latitude.ToString() + "度\n";
            richTextBox1.Text += "有無其他資訊：" + station_hsc.IsUnknown.ToString() + "\n\n";

            richTextBox1.Text += "兩站距離 " + distanceInKm.ToString() + " KM.\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }


    }
}
