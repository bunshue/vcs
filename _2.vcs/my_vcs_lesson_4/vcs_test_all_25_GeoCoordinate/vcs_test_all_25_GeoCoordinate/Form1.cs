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
        private const string Deg = "°";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label3.Text = "";
            show_item_location();

            LoadCities();

            // Pick some random cities.
            Random rand = new Random();
            cboCity1.SelectedIndex = 0;
            cboCity2.SelectedIndex = 4;

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
        private double DegreesToRadians(double degrees)
        {
            return degrees * Math.PI / 180.0;
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
            //Sugar可用
            //Kilo不可用
            //Romeo不可用

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


        // for 量測距離 ST

        // Calculate the distance.
        private void bt_measure_Click(object sender, EventArgs e)
        {
            // Parse the latitudes and longitudes.
            double lat1 = ParseLatLon(txtLat1.Text);
            double lon1 = ParseLatLon(txtLon1.Text);
            double lat2 = ParseLatLon(txtLat2.Text);
            double lon2 = ParseLatLon(txtLon2.Text);

            // Display the distance.
            double distance = GreatCircleDistance(lat1, lon1, lat2, lon2);

            richTextBox1.Text += "起點\t" + cboCity1.Text + "\n";
            if (lat1 > 0)
                richTextBox1.Text += "北緯\t" + lat1.ToString() + "\n";
            else
                richTextBox1.Text += "南緯\t" + (-lat1).ToString() + "\n";
            if (lon1 > 0)
                richTextBox1.Text += "東經\t" + lon1.ToString() + "\n";
            else
                richTextBox1.Text += "西經\t" + (-lon1).ToString() + "\n";

            richTextBox1.Text += "\n終點\t" + cboCity2.Text + "\n";
            if (lat2 > 0)
                richTextBox1.Text += "北緯\t" + lat2.ToString() + "\n";
            else
                richTextBox1.Text += "南緯\t" + (-lat2).ToString() + "\n";
            if (lon2 > 0)
                richTextBox1.Text += "東經\t" + lon2.ToString() + "\n";
            else
                richTextBox1.Text += "西經\t" + (-lon2).ToString() + "\n";

            label3.Text = "距離    " + Math.Round(distance).ToString() + " 公里\n";
            richTextBox1.Text += "距離\t" + Math.Round(distance).ToString() + " 公里\n";
        }

        // Parse a latitude or longitude.
        private double ParseLatLon(string str)
        {
            str = str.ToUpper().Replace(Deg, " ").Replace("'", " ").Replace("\"", " ");
            str = str.Replace("S", " S").Replace("N", " N");
            str = str.Replace("E", " E").Replace("W", " W");
            char[] separators = { ' ' };
            string[] fields = str.Split(separators,
                StringSplitOptions.RemoveEmptyEntries);

            double result =             // Degrees.
                double.Parse(fields[0]);
            if (fields.Length > 2)      // Minutes.
                result += double.Parse(fields[1]) / 60;
            if (fields.Length > 3)      // Seconds.
                result += double.Parse(fields[2]) / 3600;
            if (str.Contains('S') || str.Contains('W')) result *= -1;
            return result;
        }

        // Calculate the great circle distance between two points.
        private double GreatCircleDistance(
            double lat1, double lon1, double lat2, double lon2)
        {
            const double radius = 6371; // Radius of the Earth in km.
            lat1 = DegreesToRadians(lat1);
            lon1 = DegreesToRadians(lon1);
            lat2 = DegreesToRadians(lat2);
            lon2 = DegreesToRadians(lon2);
            double d_lat = lat2 - lat1;
            double d_lon = lon2 - lon1;
            double h = Math.Sin(d_lat / 2) * Math.Sin(d_lat / 2) +
                Math.Cos(lat1) * Math.Cos(lat2) *
                Math.Sin(d_lon / 2) * Math.Sin(d_lon / 2);
            return 2 * radius * Math.Asin(Math.Sqrt(h));
        }

        // Load latitude and longitude data for major cities. Data from:
        // https://www.infoplease.com/world/world-geography/major-cities-latitude-longitude-and-corresponding-time-zones
        private void LoadCities()
        {
            string[] city_data = {
                "Beijing, China;39;55 N;116;25 E",
                "Tokyo, Japan;35;40 N;139;45 E",
                "Mexico City, Mexico;19;26 N;99;7 W",
                "Buenos Aires, Argentina;34;35 S;58;22 W",
                "Wellington, New Zealand;41;17 S;174;47 E",
                "Aberdeen, Scotland;57;9 N;2;9 W",
                "Adelaide, Australia;34;55 S;138;36 E",
                "Algiers, Algeria;36;50 N;3;0 E",
                "Amsterdam, Netherlands;52;22 N;4;53 E",
                "Ankara, Turkey;39;55 N;32;55 E",
                "Asunción, Paraguay;25;15 S;57;40 W",
                "Athens, Greece;37;58 N;23;43 E",
                "Auckland, New Zealand;36;52 S;174;45 E",
                "Bangkok, Thailand;13;45 N;100;30 E",
                "Barcelona, Spain;41;23 N;2;9 E",
                "Beijing, China;39;55 N;116;25 E",
                "Belém, Brazil;1;28 S;48;29 W",
                "Belfast, Northern Ireland;54;37 N;5;56 W",
                "Belgrade, Serbia;44;52 N;20;32 E",
                "Berlin, Germany;52;30 N;13;25 E",
                "Birmingham, England;52;25 N;1;55 W",
                "Bogotá, Colombia;4;32 N;74;15 W",
                "Bombay, India;19;0 N;72;48 E",
                "Bordeaux, France;44;50 N;0;31 W",
                "Bremen, Germany;53;5 N;8;49 E",
                "Brisbane, Australia;27;29 S;153;8 E",
                "Bristol, England;51;28 N;2;35 W",
                "Brussels, Belgium;50;52 N;4;22 E",
                "Bucharest, Romania;44;25 N;26;7 E",
                "Budapest, Hungary;47;30 N;19;5 E",
                "Buenos Aires, Argentina;34;35 S;58;22 W",
                "Cairo, Egypt;30;2 N;31;21 E",
                "Calcutta, India;22;34 N;88;24 E",
                "Canton, China;23;7 N;113;15 E",
                "Cape Town, South Africa;33;55 S;18;22 E",
                "Caracas, Venezuela;10;28 N;67;2 W",
                "Cayenne, French Guiana;4;49 N;52;18 W",
                "Chihuahua, Mexico;28;37 N;106;5 W",
                "Chongqing, China;29;46 N;106;34 E",
                "Copenhagen, Denmark;55;40 N;12;34 E",
                "Córdoba, Argentina;31;28 S;64;10 W",
                "Dakar, Senegal;14;40 N;17;28 W",
                "Darwin, Australia;12;28 S;130;51 E",
                "Djibouti, Djibouti;11;30 N;43;3 E",
                "Dublin, Ireland;53;20 N;6;15 W",
                "Durban, South Africa;29;53 S;30;53 E",
                "Edinburgh, Scotland;55;55 N;3;10 W",
                "Frankfurt, Germany;50;7 N;8;41 E",
                "Georgetown, Guyana;6;45 N;58;15 W",
                "Glasgow, Scotland;55;50 N;4;15 W",
                "Guatemala City, Guatemala;14;37 N;90;31 W",
                "Guayaquil, Ecuador;2;10 S;79;56 W",
                "Hamburg, Germany;53;33 N;10;2 E",
                "Hammerfest, Norway;70;38 N;23;38 E",
                "Havana, Cuba;23;8 N;82;23 W",
                "Helsinki, Finland;60;10 N;25;0 E",
                "Hobart, Tasmania;42;52 S;147;19 E",
                "Hong Kong, China;22;20 N;114;11 E",
                "Iquique, Chile;20;10 S;70;7 W",
                "Irkutsk, Russia;52;30 N;104;20 E",
                "Jakarta, Indonesia;6;16 S;106;48 E",
                "Johannesburg, South Africa;26;12 S;28;4 E",
                "Kingston, Jamaica;17;59 N;76;49 W",
                "Kinshasa, Congo;4;18 S;15;17 E",
                "Kuala Lumpur, Malaysia;3;8 N;101;42 E",
                "La Paz, Bolivia;16;27 S;68;22 W",
                "Leeds, England;53;45 N;1;30 W",
                "Lima, Peru;12;0 S;77;2 W",
                "Lisbon, Portugal;38;44 N;9;9 W",
                "Liverpool, England;53;25 N;3;0 W",
                "London, England;51;32 N;0;5 W",
                "Lyons, France;45;45 N;4;50 E",
                "Madrid, Spain;40;26 N;3;42 W",
                "Manchester, England;53;30 N;2;15 W",
                "Manila, Philippines;14;35 N;120;57 E",
                "Marseilles, France;43;20 N;5;20 E",
                "Mazatlán, Mexico;23;12 N;106;25 W",
                "Mecca, Saudi Arabia;21;29 N;39;45 E",
                "Melbourne, Australia;37;47 S;144;58 E",
                "Mexico City, Mexico;19;26 N;99;7 W",
                "Milan, Italy;45;27 N;9;10 E",
                "Montevideo, Uruguay;34;53 S;56;10 W",
                "Moscow, Russia;55;45 N;37;36 E",
                "Munich, Germany;48;8 N;11;35 E",
                "Nagasaki, Japan;32;48 N;129;57 E",
                "Nagoya, Japan;35;7 N;136;56 E",
                "Nairobi, Kenya;1;25 S;36;55 E",
                "Nanjing (Nanking), China;32;3 N;118;53 E",
                "Naples, Italy;40;50 N;14;15 E",
                "New Delhi, India;28;35 N;77;12 E",
                "Newcastle-on-Tyne, England;54;58 N;1;37 W",
                "Odessa, Ukraine;46;27 N;30;48 E",
                "Osaka, Japan;34;32 N;135;30 E",
                "Oslo, Norway;59;57 N;10;42 E",
                "Panama City, Panama;8;58 N;79;32 W",
                "Paramaribo, Suriname;5;45 N;55;15 W",
                "Paris, France;48;48 N;2;20 E",
                "Perth, Australia;31;57 S;115;52 E",
                "Plymouth, England;50;25 N;4;5 W",
                "Port Moresby, Papua New Guinea;9;25 S;147;8 E",
                "Prague, Czech Republic;50;5 N;14;26 E",
                "Rangoon, Myanmar;16;50 N;96;0 E",
                "Reykjavík, Iceland;64;4 N;21;58 W",
                "Rio de Janeiro, Brazil;22;57 S;43;12 W",
                "Rome, Italy;41;54 N;12;27 E",
                "Salvador, Brazil;12;56 S;38;27 W",
                "Santiago, Chile;33;28 S;70;45 W",
                "St. Petersburg, Russia;59;56 N;30;18 E",
                "São Paulo, Brazil;23;31 S;46;31 W",
                "Shanghai, China;31;10 N;121;28 E",
                "Singapore, Singapore;1;14 N;103;55 E",
                "Sofia, Bulgaria;42;40 N;23;20 E",
                "Stockholm, Sweden;59;17 N;18;3 E",
                "Sydney, Australia;34;0 S;151;0 E",
                "Tananarive, Madagascar;18;50 S;47;33 E",
                "Teheran, Iran;35;45 N;51;45 E",
                "Tokyo, Japan;35;40 N;139;45 E",
                "Tripoli, Libya;32;57 N;13;12 E",
                "Venice, Italy;45;26 N;12;20 E",
                "Veracruz, Mexico;19;10 N;96;10 W",
                "Vienna, Austria;48;14 N;16;20 E",
                "Vladivostok, Russia;43;10 N;132;0 E",
                "Warsaw, Poland;52;14 N;21;0 E",
                "Wellington, New Zealand;41;17 S;174;47 E",
                "Zürich, Switzerland;47;21 N;8;31 E",
            };
            foreach (string line in city_data)
            {
                string[] fields = line.Split(';');

                fields[2] = fields[2].Replace(" ", "' ");
                string lat = fields[1] + " " + fields[2];
                fields[4] = fields[4].Replace(" ", "' ");
                string lon = fields[3] + " " + fields[4];

                cboCity1.Items.Add(new LatLon(fields[0], lat, lon));
                cboCity2.Items.Add(new LatLon(fields[0], lat, lon));
            }
        }

        // Fill in the latitude and longitude for this city.
        private void cboCity1_SelectedIndexChanged(object sender, EventArgs e)
        {
            LatLon latlon = (LatLon)cboCity1.SelectedItem;
            txtLat1.Text = latlon.Lat;
            txtLon1.Text = latlon.Lon;
            lblDistance.Text = "";
        }
        private void cboCity2_SelectedIndexChanged(object sender, EventArgs e)
        {
            LatLon latlon = (LatLon)cboCity2.SelectedItem;
            txtLat2.Text = latlon.Lat;
            txtLon2.Text = latlon.Lon;
            lblDistance.Text = "";
        }


        // for 量測距離 SP
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
