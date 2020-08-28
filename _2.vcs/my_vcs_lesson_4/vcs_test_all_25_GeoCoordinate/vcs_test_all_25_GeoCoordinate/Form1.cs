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

        void find_angle(double x_st, double y_st, double x_sp, double y_sp)
        {
            double x_diff;
            double y_diff;
            double distance;

            x_diff = x_sp - x_st;
            y_diff = y_sp - y_st;

            //n_diff = 1;
            //e_diff = 1;

            double result;

            if ((y_diff > 0) && (x_diff > 0))
            {
                result = Math.Atan(x_diff / y_diff);
                //richTextBox1.Text += "result = " + result.ToString().ToString() + "\n";
                result = result * 180 / Math.PI;
                richTextBox1.Text += "1 result = " + result.ToString().ToString() + "\n";
                if (result <= 45)
                    richTextBox1.Text += "北偏東 " + result.ToString() + "度\n";
                else
                    richTextBox1.Text += "東偏北 " + (90 - result).ToString() + "度\n";
            }
            else if ((y_diff < 0) && (x_diff > 0))
            {
                result = Math.Atan(-y_diff / x_diff);
                //richTextBox1.Text += "result = " + result.ToString().ToString() + "\n";
                result = result * 180 / Math.PI + 90;
                richTextBox1.Text += "2 result = " + result.ToString().ToString() + "\n";
                if ((result - 90) <= 45)
                    richTextBox1.Text += "東偏南 " + (result - 90).ToString() + "度\n";
                else
                    richTextBox1.Text += "南偏東 " + (90 - (result - 90)).ToString() + "度\n";
            }
            else if ((y_diff < 0) && (x_diff < 0))
            {
                result = Math.Atan(x_diff / y_diff);
                //richTextBox1.Text += "result = " + result.ToString().ToString() + "\n";
                result = result * 180 / Math.PI + 180;
                richTextBox1.Text += "3 result = " + result.ToString().ToString() + "\n";
                if ((result - 180) <= 45)
                    richTextBox1.Text += "南偏西 " + (result - 180).ToString() + "度\n";
                else
                    richTextBox1.Text += "西偏南 " + (90 - (result - 180)).ToString() + "度\n";
            }
            else
            {
                result = Math.Atan(-y_diff / x_diff);
                //richTextBox1.Text += "result = " + result.ToString().ToString() + "\n";
                result = result * 180 / Math.PI + 270;
                richTextBox1.Text += "4 result = " + result.ToString().ToString() + "\n";
                if ((result - 270) <= 45)
                    richTextBox1.Text += "西偏北 " + (result - 270).ToString() + "度\n";
                else
                    richTextBox1.Text += "北偏西 " + (90 - (result - 270)).ToString() + "度\n";
            }

            //distance = Math.Sqrt(x_diff * x_diff + y_diff * y_diff);

            //richTextBox1.Text += "距離 " + distance.ToString() + " KM\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //南投縣魚池鄉東光村
            double e0 = 120.969543;
            double n0 = 23.861058;

            //花蓮縣秀林鄉富世村
            double e1 = 121.597506;
            double n1 = 24.166395;

            //台東縣台東市豐谷里
            double e2 = 121.123539;
            double n2 = 22.744382;

            //屏東縣崁頂鄉北勢村
            double e3 = 120.490360;
            double n3 = 22.507343;

            //台中市南屯區文山里
            double e4 = 120.601413;
            double n4 = 24.151991;

            //find_angle(e0, n0, e1, n1);
            //find_angle(e0, n0, e2, n2);
            //find_angle(e0, n0, e3, n3);
            //find_angle(e0, n0, e4, n4);


            find_angle(0, 0, 3, 4);
            find_angle(0, 0, 4, 3);

            find_angle(0, 0, 4, -3);
            find_angle(0, 0, 3, -4);

            find_angle(0, 0, -3, -4);
            find_angle(0, 0, -4, -3);

            find_angle(0, 0, -4, 3);
            find_angle(0, 0, -3, 4);


            find_angle(121.028837, 24.839819, 121.030778, 24.839649);

            find_angle(120.971655, 24.801604, 121.517033, 25.047778);
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
