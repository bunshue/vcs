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

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 12;
            y_st = 12;
            dx = 110;
            dy = 48;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            bt_clear.Location = new Point(x_st + dx * 0, y_st + dy * 11);
        }

        private void button0_Click(object sender, EventArgs e)
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

            richTextBox1.Text += "兩點距離 " + distanceInKm.ToString() + " KM.\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //台北車站	25.047778, 121.517033 
            //新竹車站	24.801604, 120.971655

            //計算距離
            MapDistanceServices _distanceServices = new MapDistanceServices();

            //double distanceInKm = _distanceServices.GetDistance(緯度1, 經度1, 緯度2, 經度2);
            double distanceInKm = _distanceServices.GetDistance(25.047778, 121.517033, 24.801604, 120.971655);
            richTextBox1.Text += "兩點距離 " + distanceInKm.ToString() + " KM.\n";
        }

        void find_angle(double x_st, double y_st, double x_sp, double y_sp)
        {
            double x_diff;
            double y_diff;
            //double distance;

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

        private void button2_Click(object sender, EventArgs e)
        {
            // Get the entered latitudes and longitudes.
            double lat_from = 25.0;
            if (lat_from < 0) lat_from += 360;

            double lon_from = 240.0;
            if (lon_from < 0) lon_from += 360;

            double lat_to = 26.0;
            if (lat_to < 0) lat_to += 360;

            double lon_to = 241.0;
            if (lon_to < 0) lon_to += 360;

            // Calculate the differences in latitude and longitude.
            double dlat = Math.Abs(lat_from - lat_to);
            if (dlat > 180) dlat = 360 - dlat;

            double dlon = Math.Abs(lon_from - lon_to);
            if (dlon > 180) dlon = 360 - dlon;

            // Flat Earth.
            //txtMethod1.Text = FlatEarth(lat_from, lon_from, lat_to, lon_to).ToString("0.0000");
            FlatEarth(lat_from, lon_from, lat_to, lon_to);

            // Haversine.
            //txtMethod2.Text = Haversine(lat_from, lon_from, lat_to, lon_to).ToString("0.0000");
            Haversine(lat_from, lon_from, lat_to, lon_to);


            //台北車站	25.047778, 121.517033 
            //新竹車站	24.801604, 120.971655
            lat_from = 25.047778;
            if (lat_from < 0) lat_from += 360;

            lon_from = 121.517033;
            if (lon_from < 0) lon_from += 360;
            lat_to = 24.801604;
            if (lat_to < 0) lat_to += 360;
            lon_to = 120.971655;
            if (lon_to < 0) lon_to += 360;

            // Calculate the differences in latitude and longitude.
            dlat = Math.Abs(lat_from - lat_to);
            if (dlat > 180) dlat = 360 - dlat;

            dlon = Math.Abs(lon_from - lon_to);
            if (dlon > 180) dlon = 360 - dlon;

            // Flat Earth.
            //txtMethod1.Text = FlatEarth(lat_from, lon_from, lat_to, lon_to).ToString("0.0000");
            FlatEarth(lat_from, lon_from, lat_to, lon_to);

            // Haversine.
            //txtMethod2.Text = Haversine(lat_from, lon_from, lat_to, lon_to).ToString("0.0000");
            Haversine(lat_from, lon_from, lat_to, lon_to);

        }

        // Methods for calculating distances.
        private const double EarthRadius = 3958.756;  //mi
        //private const double EarthRadius = 6367.5;  //KM    //R表示地球的平均半徑，為6371km

        private double FlatEarth(double lat1, double lon1, double lat2, double lon2)
        {
            richTextBox1.Text += "量測距離\tFlatEarth\n";
            richTextBox1.Text += "從 東經 " + lon1.ToString() + " 度, 北緯 " + lat1.ToString() + " 度\n";
            richTextBox1.Text += "到 東經 " + lon2.ToString() + " 度, 北緯 " + lat2.ToString() + " 度\n";

            //                              緯度          經度
            // Calculate the differences in latitude and longitude.
            double dlat = Math.Abs(lat1 - lat2);
            if (dlat > 180) dlat = 360 - dlat;

            double dlon = Math.Abs(lon1 - lon2);
            if (dlon > 180) dlon = 360 - dlon;

            double x = 69.1 * dlat;     //緯度差 一度球心角所對應的子午線弧長為111.2km
            double y = 53.0 * dlon;     //經度差   同一緯度約等於111km乘緯度的餘弦
            double distance = Math.Sqrt(x * x + y * y);
            richTextBox1.Text += "距離\t" + distance.ToString() + " 公里\n";
            return distance;
        }

        private double Haversine(double lat1, double lon1, double lat2, double lon2)
        {
            richTextBox1.Text += "量測距離\tHaversine\n";
            richTextBox1.Text += "從 東經 " + lon1.ToString() + " 度, 北緯 " + lat1.ToString() + " 度\n";
            richTextBox1.Text += "到 東經 " + lon2.ToString() + " 度, 北緯 " + lat2.ToString() + " 度\n";

            double dlat = DegreesToRadians(lat2 - lat1);
            double dlon = DegreesToRadians(lon2 - lon1);
            double a = Math.Sin(dlat / 2) * Math.Sin(dlat / 2) + Math.Cos(DegreesToRadians(lat1)) * Math.Cos(DegreesToRadians(lat2)) * Math.Sin(dlon / 2) * Math.Sin(dlon / 2);
            double distance = 2 * Math.Atan2(Math.Sqrt(a), Math.Sqrt(1 - a)) * EarthRadius;
            richTextBox1.Text += "距離\t" + distance.ToString() + " 公里\n";
            return distance;
        }

        private double rad(double d)
        {
            return d * Math.PI / 180.0;
        }

        private double sind(double d)
        {
            return Math.Sin(d * Math.PI / 180.0);
        }

        private double cosd(double d)
        {
            return Math.Cos(d * Math.PI / 180.0);
        }

        // Convert degrees into radians.
        private double DegreesToRadians(double d)
        {
            return d / 180 * Math.PI;
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
            // The coordinate watcher.
            GeoCoordinateWatcher Watcher = null;

            // Create and start the watcher.
            // Create the watcher.
            Watcher = new GeoCoordinateWatcher();

            // Catch the StatusChanged event.
            //Watcher.StatusChanged += Watcher_StatusChanged;

            // Start the watcher.
            Watcher.Start();

            int i;
            for (i = 0; i < 10; i++)
            {
                //richTextBox1.Text += "IsUnknown\t" + Watcher.Position.Location.IsUnknown.ToString() + "\n";
                delay(5);
                if (Watcher.Position.Location.IsUnknown == false)
                    break;
            }
            richTextBox1.Text += "Latitude\t" + Watcher.Position.Location.Latitude.ToString() + "\n";
            richTextBox1.Text += "Longitude\t" + Watcher.Position.Location.Longitude.ToString() + "\n";
            richTextBox1.Text += "Altitude\t" + Watcher.Position.Location.Altitude.ToString() + "\n";
            richTextBox1.Text += "Course\t" + Watcher.Position.Location.Course.ToString() + "\n";
            richTextBox1.Text += "Speed\t" + Watcher.Position.Location.Speed.ToString() + "\n";
        }

        //delay 10000 約 10秒
        //C# 不lag的延遲時間
        private void delay(int delay_milliseconds)
        {
            delay_milliseconds *= 2;
            DateTime time_before = DateTime.Now;
            while (((TimeSpan)(DateTime.Now - time_before)).TotalMilliseconds < delay_milliseconds)
            {
                Application.DoEvents();
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

    }

    public class MapDistanceServices
    {
        public MapDistanceServices()
        {
        }
        private const double EARTH_RADIUS = 6378.137;
        private double rad(double d)
        {
            return d * Math.PI / 180.0;
        }

        /// <summary>
        /// 
        /// </summary>
        /// <param name="lat1">緯度1</param>
        /// <param name="lng1">經度1</param>
        /// <param name="lat2">緯度2</param>
        /// <param name="lng2">經度2</param>
        /// <returns></returns>
        public double GetDistance(double lat1, double lng1, double lat2, double lng2)
        {
            double dblResult = 0;
            double radLat1 = rad(lat1);
            double radLat2 = rad(lat2);
            double distLat = radLat1 - radLat2;
            double distLng = rad(lng1) - rad(lng2);
            dblResult = 2 * Math.Asin(Math.Sqrt(Math.Pow(Math.Sin(distLat / 2), 2) +
                            Math.Cos(radLat1) * Math.Cos(radLat2) * Math.Pow(Math.Sin(distLng / 2), 2)));
            dblResult = dblResult * EARTH_RADIUS;

            dblResult = Math.Round(dblResult * 10000) /10000;  //這回傳變成公里,少3個0變公尺
            //dblResult = Math.Round(dblResult * 10000) / 10; //公尺

            return dblResult;
        }
    }

}
