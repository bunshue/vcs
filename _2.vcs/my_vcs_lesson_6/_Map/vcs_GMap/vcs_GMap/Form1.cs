using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

using System.IO;
using System.Net;
using System.Diagnostics;
using System.Threading;

using System.Xml;
using System.Xml.Linq;

using GMap.NET;
using GMap.NET.WindowsForms;
using GMap.NET.MapProviders;
using GMap.NET.WindowsForms.Markers;

using GMapChinaRegion;

using GMapDownload;

//需要GMap.NET.Core.dll 和 GMap.NET.WindowsForms.dll這兩個檔案。

namespace vcs_GMap
{
    public partial class Form1 : Form
    {
        GMapOverlay markersOverlay = new GMapOverlay("markers"); //放置marker的图层

        //按滑鼠左鍵連線
        //需要绘制的经纬度点集
        private List<PointLatLng> line_point = new List<PointLatLng>();

        TrackBar trackBar1 = new TrackBar();

        string gMapCacheLocation = "GMapCache"; //緩存位置

        double latitude = 24.838;   //緯度
        double longitude = 121.003; //經度

        //量測距離用
        int flag_measure_distance = 0;  //0 : 無量測, 1 : 量測距離 單程, 2 : 量測距離 連續
        bool flag_measure_first_point = false;
        PointLatLng pt1 = new PointLatLng(0, 0);
        PointLatLng pt2 = new PointLatLng(0, 0);
        double total_distance = 0;

        //讀取座標資料
        bool flag_read_coordinate = false;

        bool flag_fullscreen = false;

        private const int ICON_LINEWDITH = 4; //設定按鈕畫線線寬
        private const int ICON_W = 50; //設定按鈕大小 W
        private const int ICON_H = 50; //設定按鈕大小 H

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            setup_controls();
            update_controls_info();

            update_region_info();
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //C# 強制關閉 Process
            Process.GetCurrentProcess().Kill();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 100;
            dy = 50;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button4.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            button5.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            button6.Location = new Point(x_st + dx * 6, y_st + dy * 0);

            button11.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button13.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button14.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button15.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            button16.Location = new Point(x_st + dx * 5, y_st + dy * 1);
            button17.Location = new Point(x_st + dx * 6, y_st + dy * 1);

            button7.Location = new Point(x_st + dx * 7, y_st + dy * 0);
            button8.Location = new Point(x_st + dx * 7, y_st + dy * 1 - 10);
            button9.Location = new Point(x_st + dx * 7, y_st + dy * 2 - 20);
            button10.Location = new Point(x_st + dx * 7 + 60, y_st + dy * 1 - 10);
            tb_zoom.Location = new Point(x_st + dx * 7 + 60, y_st + dy * 0);
            bt_save.Location = new Point(x_st + dx * 7 + 60, y_st + dy * 2 - 20);

            x_st = 10;
            y_st = 150;
            gMapControl1.Location = new Point(x_st, y_st);
            richTextBox1.Location = new Point(x_st + 960 + 70, y_st);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            x_st = 940;
            y_st = 30;
            btn_north.Location = new Point(x_st, y_st);
            btn_east.Location = new Point(x_st + 32, y_st + 32);
            btn_west.Location = new Point(x_st - 32, y_st + 32);
            btn_south.Location = new Point(x_st, y_st + 64);

            x_st = 1010;
            y_st = 10;
            groupBox1.Location = new Point(x_st, y_st);
            groupBox2.Location = new Point(x_st + 240, y_st);

            x_st = 1370;
            y_st = 12;
            dy = 25;
            checkBox1.Location = new Point(x_st, y_st + dy * 0);
            checkBox2.Location = new Point(x_st, y_st + dy * 1);

            rb_km.Location = new Point(x_st, y_st + dy * 2);
            rb_m.Location = new Point(x_st + 45, y_st + dy * 2);
            lb_distance.Location = new Point(x_st + 90, y_st + dy * 2);

            comboBox1.Location = new Point(x_st, y_st + dy * 3);
            btn_draw_profile.Location = new Point(x_st, y_st + dy * 4);
            btn_draw_profile2.Location = new Point(x_st + 85, y_st + dy * 4);
            groupBox3.Location = new Point(x_st, y_st + dy * 5+20);

            x_st = 20;
            y_st = 15;
            dy = 16;

            radioButton1.Location = new Point(x_st, y_st + dy * 0);
            radioButton2.Location = new Point(x_st, y_st + dy * 1);
            radioButton3.Location = new Point(x_st, y_st + dy * 2);
            radioButton4.Location = new Point(x_st, y_st + dy * 3);
            radioButton5.Location = new Point(x_st, y_st + dy * 4);
            radioButton6.Location = new Point(x_st, y_st + dy * 5);
            radioButton7.Location = new Point(x_st, y_st + dy * 6);

            radioButton1.Text = "正中地圖";
            radioButton2.Text = "簡中地圖";
            radioButton3.Text = "地形圖";
            radioButton4.Text = "衛星地圖";
            radioButton5.Text = "混合地圖";
            radioButton6.Text = "腳踏車";
            radioButton7.Text = "英文";
            radioButton8.Text = "Bing混和地圖";
            radioButton9.Text = "Bing衛星地圖";
            radioButton10.Text = "Bing混合地圖";
            radioButton11.Text = "Google";
            radioButton12.Text = "WikiMapia";
            radioButton13.Text = "Google混合地圖";
            radioButton14.Text = "簡中地圖";
            lb_distance.Text = "";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void setup_controls()
        {
            setup_gMapControl();
            setup_trackBar();
        }

        void setup_gMapControl()
        {
            //檢查網路狀態, 以設定gmap存取模式
            try
            {
                //IPHostEntry iphe = Dns.GetHostEntry("ditu.google.cn");
                //IPHostEntry iphe = Dns.GetHostEntry("www.google.com.hk");
                IPHostEntry iphe = Dns.GetHostEntry("maps.google.com.tw");
            }
            catch
            {
                //設置控件的管理模式
                //gMapControl1.Manager.Mode = AccessMode.ServerOnly;
                //gMapControl1.Manager.Mode = AccessMode.ServerAndCache;
                gMapControl1.Manager.Mode = AccessMode.CacheOnly;
                //MessageBox.Show("No internet connection avaible, going to CacheOnly mode.", "GMap.NET Demo", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                richTextBox1.Text += "無網路, 使用記憶體快取\n";
                this.BackColor = Color.Yellow;
            }

            gMapControl1.EmptyTileColor = Color.Pink;  //設置沒有數據的切片所顯示的顏色
            gMapControl1.CacheLocation = gMapCacheLocation; //緩存位置
            gMapControl1.Manager.ImportFromGMDB(@"gMapCacheLocation\mapdata.gmdb");

            //設定MapProvider
            //gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖

            gMapControl1.MapScaleInfoEnabled = true;    //比例尺
            gMapControl1.ShowCenter = true; //隱藏/顯示地圖中間的紅十字
            gMapControl1.IsAccessible = false;  //??
            gMapControl1.DragButton = MouseButtons.Left; //左键拖拽地图

            gMapControl1.MinZoom = 1;  //設置控件最小縮放比例 >=1
            gMapControl1.MaxZoom = 24; //設置控件最大縮放比例 <=24
            gMapControl1.Zoom = 14;     //當前比例

            gMapControl1.OnMapZoomChanged += new MapZoomChanged(mapControl_OnMapZoomChanged);
            gMapControl1.MouseDown += new MouseEventHandler(mapControl_MouseDown);
            gMapControl1.MouseMove += new MouseEventHandler(mapControl_MouseMove);
            gMapControl1.MouseUp += new MouseEventHandler(mapControl_MouseUp);
            gMapControl1.MouseClick += new MouseEventHandler(gMapControl1_MouseClick);
            gMapControl1.MouseDoubleClick += new MouseEventHandler(gMapControl1_MouseDoubleClick);
            gMapControl1.Paint += new PaintEventHandler(gMapControl1_Paint);
            //gMapControl1.MouseWheelZoomType = MouseWheelZoomType.MousePositionAndCenter;
            gMapControl1.KeyDown += new KeyEventHandler(gMapControl1_KeyDown);
            this.ActiveControl = this.gMapControl1;//选中pictureBox1，不然没法触发事件

            gMapControl1.Overlays.Add(markersOverlay);  //添加 圖標 Markers 的圖層

            //gMapControl1.Dock = DockStyle.Fill;   //將控件全屏顯示
            gMapControl1.CanDragMap = true; //滑鼠右鍵拖動地圖
            gMapControl1.MarkersEnabled = true; //顯示markers
            gMapControl1.PolygonsEnabled = true;    //顯示polygon
            gMapControl1.RoutesEnabled = true;
            //gMapControl1.ShowTileGridLines = true;  //顯示座標格網  常有問題 可能是timeout
            //gMapControl1.GrayScaleMode = true;    //黑白地圖

            //gMapControl1.OnMarkerClick += gMapControl1_OnMarkerClick;
            //gMapControl1.OnPositionChanged += gMapControl1_OnPositionChanged;
            //gMapControl1.OnTileLoadComplete += GMap_OnTileLoadComplete;
            //gMapControl1.OnTileLoadStart += GMap_OnTileLoadStart;

            //GMapProvider.Language = LanguageType.ChineseSimplified; //设置地图默认语言
            GMapProvider.Language = LanguageType.ChineseTraditional; //设置地图默认语言
            GMapProvider.TimeoutMs = 10000;//地图加载完成后设置timeoutms为1000(或者其他大于领零的数值自己尝试0)
        }

        void setup_trackBar()
        {
            trackBar1.Orientation = Orientation.Vertical;
            trackBar1.TickStyle = TickStyle.Both;
            trackBar1.TickFrequency = 10;
            trackBar1.Maximum = 100;
            trackBar1.Minimum = 1;
            trackBar1.Value = 10;
            trackBar1.Height = gMapControl1.Height * 9 / 10;
            trackBar1.Width = 30;
            trackBar1.Location = new Point(gMapControl1.Location.X + gMapControl1.Width + 10, gMapControl1.Location.Y + gMapControl1.Height / 20);
            trackBar1.ValueChanged += trackBar1_ValueChanged;
            Controls.Add(trackBar1);
            trackBar1.BringToFront();
        }

        int cnt = 0;
        void gMapControl1_MouseClick(object sender, MouseEventArgs e)
        {
            if ((e.Location.X > (gMapControl1.Size.Width - ICON_W)) && (e.Location.Y < ICON_H))
            {
                Application.Exit();
            }

            if (e.Button == MouseButtons.Right)
            {
                if (checkBox2.Checked == true)   //滑鼠右鍵畫標記
                {
                    //從地圖上的滑鼠座標畫標記
                    PointLatLng point = gMapControl1.FromLocalToLatLng(e.X, e.Y);
                    richTextBox1.Text += "控件座標(" + e.X.ToString() + ", " + e.Y.ToString() + ")\t地理座標" + point.Lat.ToString() + "\t" + point.Lng.ToString() + "\n";

                    GMapMarker marker = new GMarkerGoogle(point, GMarkerGoogleType.green);
                    setup_marker_tooltip(marker, (cnt++).ToString());   //設置marker訊息
                    markersOverlay.Markers.Add(marker);
                }
                //PointLatLng pts = gMapControl1.FromLocalToLatLng(e.X, e.Y);
                //richTextBox1.Text += "points.Add(new PointLatLng(" + pts.Lat.ToString() + ", " + pts.Lng.ToString() + "));\n";

            }

            if (flag_read_coordinate == true)
            {
                PointLatLng pts = gMapControl1.FromLocalToLatLng(e.X, e.Y);
                richTextBox1.Text += "points.Add(new PointLatLng(" + pts.Lat.ToString() + ", " + pts.Lng.ToString() + "));\n";
            }
        }

        void gMapControl1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            if ((e.Location.X > (gMapControl1.Size.Width - ICON_W)) && (e.Location.Y < ICON_H))
            {
                Application.Exit();
            }

            if (e.Button == MouseButtons.Left)
            {
                do_toggle_fullscreen();
            }
        }

        void gMapControl1_Paint(object sender, PaintEventArgs e)
        {
            int width = ICON_LINEWDITH; //設定按鈕畫線線寬
            int w = ICON_W; //設定按鈕大小 W
            int h = ICON_H; //設定按鈕大小 H

            Pen p = new Pen(Color.Red, width);
            int x_st = gMapControl1.Size.Width - ICON_W;
            int y_st = 0;
            e.Graphics.DrawRectangle(p, x_st - width, y_st, w, h);
            e.Graphics.DrawLine(p, x_st - width, y_st, x_st + w - width, y_st + h);
            e.Graphics.DrawLine(p, x_st + w - width, y_st, x_st - width, y_st + h);
        }

        void gMapControl1_KeyDown(object sender, KeyEventArgs e)
        {
            if ((e.KeyCode == Keys.Return) || (e.KeyCode == Keys.Escape))
            {
                //richTextBox1.Text += "你按了" + e.KeyCode.ToString() + "\n";

                flag_measure_distance = 0;  //0 : 無量測, 1 : 量測距離 單程, 2 : 量測距離 連續
                flag_measure_first_point = false;
            }
            else
            {
                richTextBox1.Text += "你按了" + e.KeyCode.ToString() + "\n";
            }
        }

        //標記點擊事件
        private void gMapControl1_OnMarkerClick(GMapMarker item, MouseEventArgs e)
        {
            richTextBox1.Text += "你按了圖標 " + item.ToolTipText + "\n";

            //試者將此點設為地圖中心
            //map.Position = new PointLatLng(coords.Latitude, coords.Longitude);


            if (flag_measure_distance == 3) //0 : 無量測, 1 : 量測距離 單程, 2 : 量測距離 連續
            {

                PointLatLng point = gMapControl1.FromLocalToLatLng(e.X, e.Y);
                //richTextBox1.Text += "控件座標(" + e.X.ToString() + ", " + e.Y.ToString() + ")\t地理座標" + point.Lat.ToString() + "\t" + point.Lng.ToString() + "\n";

                richTextBox1.Text += "a " + point.ToString() + "\n";
                richTextBox1.Text += "b " + pt1.ToString() + "\n";
                richTextBox1.Text += "c " + pt2.ToString() + "\n";

                if (point == pt1)
                {
                    richTextBox1.Text += "AAA\n";
                }
                else if (point == pt2)
                {
                    richTextBox1.Text += "BBB\n";
                }
                else
                {
                    richTextBox1.Text += "XXX\n";

                }


            }
        }

        /*
        //標記點擊事件
        private void gMapControl1_OnPositionChanged(GMapMarker item, MouseEventArgs e)
        {
            richTextBox1.Text += "你按了圖標 " + item.ToolTipText + "\n";

            //試者將此點設為地圖中心
        }
        */

        private void trackBar1_ValueChanged(object sender, EventArgs e)
        {
            //richTextBox1.Text += trackBar1.Value.ToString() + "  ";
        }

        void update_controls_info()
        {
            trackBar1.Maximum = gMapControl1.MaxZoom;
            trackBar1.Minimum = gMapControl1.MinZoom;
            trackBar1.Value = (int)gMapControl1.Zoom;
            tb_zoom.Text = gMapControl1.Zoom.ToString();
            update_MapProvider_info();
        }

        void update_MapProvider_info()
        {
            if (gMapControl1.MapProvider == GMapProviders.GoogleMap)    //正中地圖
            {
                if (radioButton1.Checked != true)
                {
                    radioButton1.Checked = true;
                }
            }
            else if (gMapControl1.MapProvider == GMapProviders.GoogleChinaMap)  //簡中地圖
            {
                if (radioButton2.Checked != true)
                {
                    radioButton2.Checked = true;
                }
            }
            else if (gMapControl1.MapProvider == GMapProviders.GoogleTerrainMap)    //地形圖
            {
                if (radioButton3.Checked != true)
                {
                    radioButton3.Checked = true;
                }
            }
            else if (gMapControl1.MapProvider == GMapProviders.GoogleSatelliteMap)  //衛星地圖
            {
                if (radioButton4.Checked != true)
                {
                    radioButton4.Checked = true;
                }
            }
            else if (gMapControl1.MapProvider == GMapProviders.GoogleChinaHybridMap)    //混合地圖
            {
                if (radioButton5.Checked != true)
                {
                    radioButton5.Checked = true;
                }
            }
            else if (gMapControl1.MapProvider == OpenCycleMapProvider.Instance) //腳踏車專用地圖
            {
                if (radioButton6.Checked != true)
                {
                    radioButton6.Checked = true;
                }
            }
            else
            {

            }
        }

        private void button0_Click(object sender, EventArgs e)
        {
            gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖

            //竹北座標
            latitude = 24.838;   //緯度
            longitude = 121.003; //經度
            gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置
            gMapControl1.Zoom = 14; //當前比例

            update_controls_info();
        }

        public void DrawMarker(string[] LatLngInfo, GMapOverlay gMapOverlay1)
        {
            int len = LatLngInfo.Length;
            for (int i = 0; i < len; i++)
            {
                string[] LatLng = LatLngInfo[i].Split(',');

                //在坐标点上绘制一绿色点并向图层中添加标签
                PointLatLng point = new PointLatLng(double.Parse(LatLng[0]), double.Parse(LatLng[1]));

                GMapMarker marker = new GMarkerGoogle(point, GMarkerGoogleType.green);

                gMapOverlay1.Markers.Add(marker);

                //richTextBox1.Text += (double.Parse(LatLng[0])).ToString() + "\t" + (double.Parse(LatLng[1])).ToString() + "\n";

                //方便之后寻找到是第几个GMapMarker   
                gMapOverlay1.Markers[i].Tag = i;
                gMapOverlay1.Markers[i].Tag = "xxxx";
                gMapOverlay1.Id = "markroad";

                setup_marker_tooltip(marker, "顯示訊息"); //設置marker訊息
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double R = 0.015;
            double angle = 0;
            double cx = latitude;
            double cy = longitude;

            //製作 marker_position 資料
            string[] marker_position = new string[12];
            for (angle = 0; angle < 360; angle += 30)
            {
                marker_position[(int)(angle / 30)] = (cx + R * cosd(angle)).ToString() + ", " + (cy + R * sind(angle)).ToString();

                richTextBox1.Text += angle.ToString() + "\t" + (cx + R * cosd(angle)).ToString() + "\t" + (cy + R * sind(angle)).ToString() + "\n";
            }

            /* marker_position 語法
            //string[] marker_position = new string[4] { "24.83923062590916, 121.00410306376308", "24.83900079788313, 121.00929660194892", "24.835634744818194, 121.00903566227302", "24.836966817989957, 121.01120945267155" };

            string[] marker_position = new string[10];

            marker_position[0] = "31.420147, 121.488286";
            marker_position[1] = "31.294828, 121.702154";
            marker_position[2] = "31.141157, 121.780918";
            marker_position[3] = "30.941157, 121.782068";
            marker_position[4] = "30.909931, 121.492885";
            marker_position[5] = "30.890099, 121.22325";
            marker_position[6] = "31.015526, 121.161482";
            marker_position[7] = "31.226239, 121.076395";
            marker_position[8] = "31.339688, 121.189873";
            marker_position[9] = "31.41368, 121.459509";
            */

            DrawMarker(marker_position, markersOverlay);

            /* under test
            double lat = 24.836494165650475 + 10;
            double lon = 121.01959461339993 + 10;

            //DrawPoint(gMapControl1, lat, lon);

            //竹北座標
            latitude = 24.838;   //緯度
            longitude = (121.003+0.02); //經度

            //DrawPoint(gMapControl1, latitude, longitude);
            */

            PointLatLng point = gMapControl1.FromLocalToLatLng(1920 / 2 / 2, 1080 / 2 / 2);

            //richTextBox1.Text += "控件座標(" + e.X.ToString() + ", " + e.Y.ToString() + ")\t地理座標" + point.Lat.ToString() + "\t" + point.Lng.ToString() + "\n";

            GMapMarker marker = new GMarkerGoogle(point, GMarkerGoogleType.red);
            markersOverlay.Markers.Add(marker);
            setup_marker_tooltip(marker, "地圖正中央圖示");    //設置marker訊息

            string lngstr, latstr;
            if (point.Lng > 0)
                lngstr = point.Lng.ToString("F06") + " E";
            else
                lngstr = (-point.Lng).ToString("F06") + " W";
            if (point.Lat > 0)
                latstr = point.Lat.ToString("F06") + " N";
            else
                latstr = (-point.Lat).ToString("F06") + " S";

            setup_marker_tooltip(marker, "GPS\r\n經度=" + lngstr + "\r\n緯度=" + latstr);   //設置marker訊息

            //畫Route ST
            List<PointLatLng> points = new List<PointLatLng>();

            points.Add(new PointLatLng(24.8493692081609, 120.996723175049));
            points.Add(new PointLatLng(24.8489019025833, 121.003332138062));
            points.Add(new PointLatLng(24.8492134398311, 121.005306243896));
            points.Add(new PointLatLng(24.8505374643828, 121.009511947632));
            points.Add(new PointLatLng(24.8509268806719, 121.010885238647));
            points.Add(new PointLatLng(24.8498365119735, 121.013631820679));
            points.Add(new PointLatLng(24.8483567105118, 121.017322540283));
            points.Add(new PointLatLng(24.8449297339118, 121.02032661438));
            points.Add(new PointLatLng(24.8403343208788, 121.021013259888));
            points.Add(new PointLatLng(24.83690712212, 121.020669937134));
            points.Add(new PointLatLng(24.8326229902382, 121.018524169922));
            points.Add(new PointLatLng(24.8283387101149, 121.016464233398));
            points.Add(new PointLatLng(24.824287981682, 121.014575958252));
            points.Add(new PointLatLng(24.8268586516249, 121.01019859314));
            points.Add(new PointLatLng(24.8304419206983, 121.004705429077));
            points.Add(new PointLatLng(24.8322335163524, 121.001529693604));
            points.Add(new PointLatLng(24.8334798284745, 120.99835395813));

            /*
             * points.Add(new PointLatLng(24.8361282000777, 120.99723815918));
            points.Add(new PointLatLng(24.83425876718, 120.99268913269));
            points.Add(new PointLatLng(24.8313766694912, 120.987539291382));
            points.Add(new PointLatLng(24.8322335163524, 120.982732772827));
            points.Add(new PointLatLng(24.8379197134477, 120.984363555908));
            points.Add(new PointLatLng(24.8416584404391, 120.98539352417));
            points.Add(new PointLatLng(24.8465653482197, 120.987367630005));
            points.Add(new PointLatLng(24.84640957636, 120.988655090332));
            points.Add(new PointLatLng(24.8461759182027, 120.989942550659));
            points.Add(new PointLatLng(24.8453191678509, 120.99157333374));
            points.Add(new PointLatLng(24.8437614247412, 120.993976593018));
            points.Add(new PointLatLng(24.8460201458526, 120.995092391968));
            points.Add(new PointLatLng(24.8475778605281, 120.995864868164));
            points.Add(new PointLatLng(24.8492913240205, 120.99663734436));
            */
            DrawRoute(points);
        }

        public void DrawRoute(List<PointLatLng> points)
        {
            GMapRoute playRoute = new GMapRoute(points, "my route");
            //playRoute.Stroke.Color = Color.Red;
            //playRoute.Stroke = new Pen(Color.FromArgb(144, Color.Red)); //半透明

            playRoute.Stroke = new Pen(Color.FromArgb(127, Color.Blue), 10);    //連線顏色與大小

            //playRoute.Stroke.Width = 5;
            playRoute.Stroke.DashStyle = DashStyle.Solid;

            markersOverlay.Routes.Clear();
            markersOverlay.Routes.Add(playRoute);

            gMapControl1.ZoomAndCenterRoute(playRoute); //將playRoute這條路初始為檢視中心，顯示時以playRoute為中心顯示

            //算距離
            string dist = "";
            if (rb_km.Checked == true)  //公里
            {
                dist = ((float)playRoute.Distance * 1f).ToString("0.##") + " 公里";
            }
            else
            {
                dist = ((float)playRoute.Distance * 1000f).ToString("0.##") + " 公尺";
            }
            richTextBox1.Text += "總距離 : " + dist + "\n";
            lb_distance.Text = dist;

            /*
            richTextBox1.Text += "畫起點\n";
            PointLatLng point = new PointLatLng(points.First().Lat, points.First().Lng);
            GMapMarker marker = new GMarkerGoogle(point, GMarkerGoogleType.green_big_go);
            markersOverlay.Markers.Add(marker);

            richTextBox1.Text += "畫終點\n";
            point = new PointLatLng(points.Last().Lat, points.Last().Lng);
            marker = new GMarkerGoogle(point, GMarkerGoogleType.red_big_stop);
            markersOverlay.Markers.Add(marker);
            */

            richTextBox1.Text += "畫範圍 GMapPolygon\n";
            GMapPolygon polygon = new GMapPolygon(points, "polygon");
            polygon.Stroke.Color = Color.Purple;    //邊框顏色
            polygon.Fill = new SolidBrush(Color.FromArgb(30, Color.Blue));  //有填滿 半透明, 若不寫.Fill, 即無填滿
            markersOverlay.Polygons.Add(polygon);
        }

        public void DrawPoint(GMapControl map, double latitude, double longitude)   //緯 經
        {
            PointLatLng point = new PointLatLng(latitude, longitude);
            GMapMarker marker = new GMarkerGoogle(point, GMarkerGoogleType.red);
            GMapOverlay markersOverlay_stop = new GMapOverlay("Stop"); //放置marker的图层
            markersOverlay_stop.Markers.Add(marker);
            map.Overlays.Add(markersOverlay_stop);

            richTextBox1.Text += "北緯 " + latitude.ToString() + "\t東經 " + longitude.ToString() + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "畫範圍 GMapPolygon 1\n";
            List<PointLatLng> points = new List<PointLatLng>();
            points.Add(new PointLatLng(24.8516278269032, 121.004190444946));
            points.Add(new PointLatLng(24.8357387372186, 121.020069122314));
            points.Add(new PointLatLng(24.8316103555869, 121.002731323242));
            points.Add(new PointLatLng(24.8438393123624, 120.994234085083));
            GMapPolygon polygon = new GMapPolygon(points, "mypolygon");
            polygon.Fill = new SolidBrush(Color.FromArgb(50, Color.Red));   //有填滿 半透明, 若不寫.Fill, 即無填滿
            polygon.Stroke = new Pen(Color.Red, 1); //邊框顏色與大小

            GMapOverlay markers_polygon = new GMapOverlay("polygon"); //放置marker的图层
            markers_polygon.Polygons.Add(polygon);
            gMapControl1.Overlays.Add(markers_polygon);  //添加 圖標 Markers 的圖層

            richTextBox1.Text += "畫範圍 GMapPolygon 2\n";
            //List<PointLatLng> points = new List<PointLatLng>();
            points.Clear();
            points.Add(new PointLatLng(24.8493692081609, 120.996723175049));
            points.Add(new PointLatLng(24.8489019025833, 121.003332138062));
            points.Add(new PointLatLng(24.8509268806719, 121.010885238647));

            points.Add(new PointLatLng(24.8498365119735, 121.013631820679));
            points.Add(new PointLatLng(24.8483567105118, 121.017322540283));
            points.Add(new PointLatLng(24.8326229902382, 121.018524169922));
            points.Add(new PointLatLng(24.8283387101149, 121.016464233398));
            points.Add(new PointLatLng(24.8268586516249, 121.01019859314));

            polygon = new GMapPolygon(points, "畫範圍");
            polygon.Stroke = new Pen(Color.Red, 1); //邊框顏色與大小
            polygon.Fill = new SolidBrush(Color.FromArgb(40, Color.Purple));    //有填滿 半透明, 若不寫.Fill, 即無填滿
            markersOverlay.Polygons.Add(polygon);
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Graphics g = gMapControl1.CreateGraphics();
            g.DrawRectangle(Pens.Red, 100, 100, 100, 100);

            List<Point> Point = new List<Point>();
            Point.Clear();
            Point.Add(new Point(500, 113));
            Point.Add(new Point(686, 160));
            Point.Add(new Point(655, 437));
            Point.Add(new Point(475, 351));
            Point.Add(new Point(500, 113));
            g.DrawLines(Pens.Red, Point.ToArray());

            g.DrawString("用GDI+在gMap上畫圖", new Font("標楷體", 30), new SolidBrush(Color.Red), new PointF(60, 20));
            //david: 但無法長久留在畫面
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //拼接地圖


            int x = 0;
            int y = 0;
            PointLatLng point = new PointLatLng(x, y);

            //從地圖上的滑鼠座標畫標記

            x = 0;
            y = 0;
            point = gMapControl1.FromLocalToLatLng(x, y);
            richTextBox1.Text += "控件座標(" + x.ToString() + ", " + y.ToString() + ")\t地理座標" + point.Lat.ToString() + "\t" + point.Lng.ToString() + "\n";

            x = 960 / 2;
            y = 540 / 2;
            point = gMapControl1.FromLocalToLatLng(x, y);
            richTextBox1.Text += "控件座標(" + x.ToString() + ", " + y.ToString() + ")\t地理座標" + point.Lat.ToString() + "\t" + point.Lng.ToString() + "\n";

            x = 960 - 1;
            y = 540 - 1;
            point = gMapControl1.FromLocalToLatLng(x, y);
            richTextBox1.Text += "控件座標(" + x.ToString() + ", " + y.ToString() + ")\t地理座標" + point.Lat.ToString() + "\t" + point.Lng.ToString() + "\n";

            x = 960 + 100;
            y = 540 + 100;
            point = gMapControl1.FromLocalToLatLng(x, y);
            richTextBox1.Text += "控件座標(" + x.ToString() + ", " + y.ToString() + ")\t地理座標" + point.Lat.ToString() + "\t" + point.Lng.ToString() + "\n";
        }

        void mapControl_MouseDown(object sender, MouseEventArgs e)
        {
            //richTextBox1.Text += "MouseDown\n";

            if (e.Button == MouseButtons.Right) //檢查滑鼠右鍵
            {
                contextMenuStrip1.Show(gMapControl1, e.Location);   //顯示ContextMenu
                return;
            }
            else if (e.Button == MouseButtons.Left)
            {
                PointLatLng point = gMapControl1.FromLocalToLatLng(e.X, e.Y);
                //richTextBox1.Text += "控件座標(" + e.X.ToString() + ", " + e.Y.ToString() + ")\t地理座標" + point.Lat.ToString() + "\t" + point.Lng.ToString() + "\n";
                if (checkBox1.Checked == true)   //滑鼠左鍵連線
                {
                    line_point.Add(point);
                    draw_line_point();
                }

                if ((flag_measure_distance == 1) || (flag_measure_distance == 2))  //0 : 無量測, 1 : 量測距離 單程, 2 : 量測距離 連續
                {
                    line_point.Add(point);
                    draw_line_point();
                    if (flag_measure_first_point == false)
                    {
                        pt1 = point;
                        flag_measure_first_point = true;
                    }
                    else
                    {
                        pt2 = point;
                        double distance = getDistance(pt1, pt2);
                        total_distance += distance;

                        //算直線距離
                        string dist1 = "";
                        string dist2 = "";

                        if (rb_km.Checked == true)  //公里
                        {
                            dist1 = ((float)distance * 1f).ToString("0.##") + " 公里";
                            dist2 = ((float)total_distance * 1f).ToString("0.##") + " 公里";
                        }
                        else
                        {
                            dist1 = ((float)distance * 1000f).ToString("0.##") + " 公尺";
                            dist2 = ((float)total_distance * 1000f).ToString("0.##") + " 公尺";
                        }

                        richTextBox1.Text += "量測距離 直線 : " + dist1 + "\t總距離 : " + dist2 + "\n";
                        lb_distance.Text = dist2;

                        //在地圖上寫字
                        PointLatLng point_middle = new PointLatLng((pt1.Lat + pt2.Lat) / 2, (pt1.Lng + pt2.Lng) / 2);
                        GMapTextMarker textMarker = new GMapTextMarker(point_middle, dist2);
                        markersOverlay.Markers.Add(textMarker);

                        pt1 = point;

                        if (flag_measure_distance == 1) //0 : 無量測, 1 : 量測距離 單程, 2 : 量測距離 連續
                        {
                            flag_measure_distance = 3;
                            flag_measure_first_point = false;
                        }
                    }
                }
            }
        }

        void mapControl_MouseMove(object sender, MouseEventArgs e)
        {
            //richTextBox1.Text += "MouseMove\n";
            PointLatLng point = gMapControl1.FromLocalToLatLng(e.X, e.Y);
        }

        void mapControl_MouseUp(object sender, MouseEventArgs e)
        {
        }

        void mapControl_OnMapZoomChanged()
        {
            //richTextBox1.Text += "OnMapZoomChanged\n";
            trackBar1.Value = (int)gMapControl1.Zoom;
            tb_zoom.Text = gMapControl1.Zoom.ToString();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            markersOverlay.Clear();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //放大
            gMapControl1.Zoom += 1; //當前比例
            update_controls_info();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //縮小
            gMapControl1.Zoom -= 1; //當前比例
            update_controls_info();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            gMapControl1.ReloadMap();   //重新載入
            update_controls_info();

            //gMapControl1.Refresh();
            //gMapControl1.ShowTileGridLines = true;//显示瓦片，也就是显示方格
        }

        //info
        private void button10_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "地圖大小 W = " + gMapControl1.Width.ToString() + ", H = " + gMapControl1.Height.ToString() + "\n";

            richTextBox1.Text += "滑鼠左鍵連線點數 : " + line_point.Count.ToString() + "\n";
            richTextBox1.Text += "滑鼠右鍵標記個數 : " + markersOverlay.Markers.Count.ToString() + "\n";
            richTextBox1.Text += "內容 : ";
            int len = markersOverlay.Markers.Count;
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += i.ToString() + "\t" + markersOverlay.Markers[i].Position.ToString() + "\n";


            }


            richTextBox1.Text += "目前 GMapOverlay 有 " + gMapControl1.Overlays.Count.ToString() + "層\n";
            foreach (GMapOverlay overlay in gMapControl1.Overlays)
            {
                richTextBox1.Text += "get overlay " + overlay.Control.Name + "\n";

                foreach (var route in overlay.Routes)
                {
                    richTextBox1.Text += "這一層有 Routes\t名稱 :\t" + route.Name + "\n";
                    //其點數 route.Points
                    //其畫筆 route.Stroke
                }
            }
            richTextBox1.Text += "Zoom :\t" + gMapControl1.Zoom.ToString() + "\n";
        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            try
            {
                string filename = Application.StartupPath + "\\map_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".png";

                Image image = gMapControl1.ToImage();
                if (image != null)
                {
                    image.Save(filename);
                    richTextBox1.Text += "已存檔 : " + filename + "\n";
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }
        }

        private void btn_north_Click(object sender, EventArgs e)
        {
            //往北移動
            latitude += 0.005;
            gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置
        }

        private void btn_south_Click(object sender, EventArgs e)
        {
            //往南移動
            latitude -= 0.005;
            gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置
        }

        private void btn_east_Click(object sender, EventArgs e)
        {
            //往東移動
            longitude += 0.005;
            gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置
        }

        private void btn_west_Click(object sender, EventArgs e)
        {
            //往西移動
            longitude -= 0.005;
            gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置
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

        private void radioButton_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton1.Checked == true)
            {
                gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖
            }
            else if (radioButton2.Checked == true)
            {
                gMapControl1.MapProvider = GMapProviders.GoogleChinaMap; //簡中地圖
            }
            else if (radioButton3.Checked == true)
            {
                gMapControl1.MapProvider = GMapProviders.GoogleTerrainMap; //地形圖
            }
            else if (radioButton4.Checked == true)
            {
                gMapControl1.MapProvider = GMapProviders.GoogleSatelliteMap;    //衛星地圖
            }
            else if (radioButton5.Checked == true)
            {
                gMapControl1.MapProvider = GMapProviders.GoogleChinaHybridMap;  //混合地圖
            }
            else if (radioButton6.Checked == true)
            {
                gMapControl1.MapProvider = OpenCycleMapProvider.Instance; //腳踏車專用地圖
            }
            else if (radioButton7.Checked == true)
            {
                gMapControl1.MapProvider = BingMapProvider.Instance;    //英文
            }
            else if (radioButton8.Checked == true)
            {
                gMapControl1.MapProvider = BingHybridMapProvider.Instance;	//Bing混和地圖
            }
            else if (radioButton9.Checked == true)
            {
                gMapControl1.MapProvider = GMapProviders.BingSatelliteMap;  //Bing衛星地圖
            }
            else if (radioButton10.Checked == true)
            {
                gMapControl1.MapProvider = GMapProviders.BingHybridMap;       //Bing混合地圖
            }
            else if (radioButton11.Checked == true)
            {
                gMapControl1.MapProvider = GoogleMapProvider.Instance;
            }
            else if (radioButton12.Checked == true)
            {
                gMapControl1.MapProvider = WikiMapiaMapProvider.Instance;
            }
            else if (radioButton13.Checked == true)
            {
                gMapControl1.MapProvider = GMapProviders.GoogleHybridMap;     //Google混合地圖
            }
            else if (radioButton14.Checked == true)
            {
                gMapControl1.MapProvider = GoogleChinaMapProvider.Instance; //簡中地圖
            }
        }

        void AddMarker(double lat, double lng, GMarkerGoogleType type, string message)
        {
            GMapMarker marker = new GMarkerGoogle(new PointLatLng(lat, lng), type);
            setup_marker_tooltip(marker, message);  //設置marker訊息
            markersOverlay.Markers.Add(marker);
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //各種marker
            latitude = gMapControl1.Position.Lat;   //緯度
            longitude = gMapControl1.Position.Lng; //經度

            double dd = 0.008;

            longitude -= dd * 2;

            AddMarker(latitude + dd * 1, longitude - dd, GMarkerGoogleType.red, "red");
            AddMarker(latitude + dd * 1, longitude + dd * 0, GMarkerGoogleType.green, "green");
            AddMarker(latitude + dd * 1, longitude + dd * 1, GMarkerGoogleType.blue, "blue");

            AddMarker(latitude + dd * 0, longitude - dd, GMarkerGoogleType.green_big_go, "green_big_go");
            AddMarker(latitude + dd * 0, longitude + dd * 0, GMarkerGoogleType.red_big_stop, "red_big_stop");
            AddMarker(latitude + dd * 0, longitude + dd * 1, GMarkerGoogleType.blue_pushpin, "blue_pushpin");
            AddMarker(latitude + dd * 0, longitude + dd * 2, GMarkerGoogleType.arrow, "arrow");

            AddMarker(latitude - dd * 1, longitude - dd, GMarkerGoogleType.red_dot, "red_dot");
            AddMarker(latitude - dd * 1, longitude + dd * 0, GMarkerGoogleType.green_dot, "green_dot");
            AddMarker(latitude - dd * 1, longitude + dd * 1, GMarkerGoogleType.blue_dot, "blue_dot");
            AddMarker(latitude - dd * 1, longitude + dd * 2, GMarkerGoogleType.pink_dot, "pink_dot");

            AddMarker(latitude - dd * 2, longitude - dd, GMarkerGoogleType.red_small, "red_small");
            AddMarker(latitude - dd * 2, longitude + dd * 0, GMarkerGoogleType.gray_small, "gray_small");
            AddMarker(latitude - dd * 2, longitude + dd * 1, GMarkerGoogleType.orange_small, "orange_small");

            PointLatLng point = new PointLatLng(latitude, longitude);
            GMapMarker marker = new GMarkerGoogle(point, GMarkerGoogleType.green);
            point = new PointLatLng(latitude, longitude - dd - dd);
            string filename = @"C:\______test_files\__pic\_icon\face1.png";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            marker = new GMarkerGoogle(point, bitmap1);
            //直接寫
            //GMapMarker marker2 = new GMarkerGoogle(point, new Bitmap(filename));

            setup_marker_tooltip(marker, "12345");  //設置marker訊息

            markersOverlay.Markers.Add(marker);





        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //量測距離 直線
            PointLatLng pt1 = new PointLatLng(24.839008233119472, 121.00927283881413);
            PointLatLng pt2 = new PointLatLng(24.840091217715898, 120.99410979639839);
            double distance = getDistance(pt1, pt2);

            //算直線距離
            string dist1 = "";
            if (rb_km.Checked == true)  //公里
            {
                dist1 = ((float)distance * 1f).ToString("0.##") + " 公里";
            }
            else
            {
                dist1 = ((float)distance * 1000f).ToString("0.##") + " 公尺";
            }
            richTextBox1.Text += "量測距離 直線 : " + dist1 + "\n";
            lb_distance.Text = dist1;

            //量測距離 曲線
            List<PointLatLng> points = new List<PointLatLng>();
            points.Add(new PointLatLng(24.8493692081609, 120.996723175049));
            points.Add(new PointLatLng(24.8489019025833, 121.003332138062));
            points.Add(new PointLatLng(24.8492134398311, 121.005306243896));
            points.Add(new PointLatLng(24.8505374643828, 121.009511947632));
            points.Add(new PointLatLng(24.8509268806719, 121.010885238647));
            points.Add(new PointLatLng(24.8498365119735, 121.013631820679));
            points.Add(new PointLatLng(24.8483567105118, 121.017322540283));
            points.Add(new PointLatLng(24.8449297339118, 121.02032661438));
            points.Add(new PointLatLng(24.8403343208788, 121.021013259888));
            points.Add(new PointLatLng(24.83690712212, 121.020669937134));
            points.Add(new PointLatLng(24.8326229902382, 121.018524169922));
            points.Add(new PointLatLng(24.8283387101149, 121.016464233398));
            points.Add(new PointLatLng(24.824287981682, 121.014575958252));
            points.Add(new PointLatLng(24.8268586516249, 121.01019859314));
            points.Add(new PointLatLng(24.8304419206983, 121.004705429077));
            points.Add(new PointLatLng(24.8322335163524, 121.001529693604));
            points.Add(new PointLatLng(24.8334798284745, 120.99835395813));
            points.Add(new PointLatLng(24.8361282000777, 120.99723815918));
            points.Add(new PointLatLng(24.83425876718, 120.99268913269));
            points.Add(new PointLatLng(24.8313766694912, 120.987539291382));
            points.Add(new PointLatLng(24.8322335163524, 120.982732772827));
            points.Add(new PointLatLng(24.8379197134477, 120.984363555908));
            points.Add(new PointLatLng(24.8416584404391, 120.98539352417));
            points.Add(new PointLatLng(24.8465653482197, 120.987367630005));
            points.Add(new PointLatLng(24.84640957636, 120.988655090332));
            points.Add(new PointLatLng(24.8461759182027, 120.989942550659));
            points.Add(new PointLatLng(24.8453191678509, 120.99157333374));
            points.Add(new PointLatLng(24.8437614247412, 120.993976593018));
            points.Add(new PointLatLng(24.8460201458526, 120.995092391968));
            points.Add(new PointLatLng(24.8475778605281, 120.995864868164));
            points.Add(new PointLatLng(24.8492913240205, 120.99663734436));
            GMapRoute playRoute = new GMapRoute(points, "my route");

            //算曲線距離
            string dist2 = "";
            if (rb_km.Checked == true)  //公里
            {
                dist2 = ((float)playRoute.Distance * 1f).ToString("0.##") + " 公里";
            }
            else
            {
                dist2 = ((float)playRoute.Distance * 1000f).ToString("0.##") + " 公尺";
            }
            richTextBox1.Text += "量測距離 直線 : " + dist2 + "\n";
            lb_distance.Text = dist2;
        }

        public double getDistance(PointLatLng p1, PointLatLng p2)
        {
            //算直線距離
            GMapRoute route = new GMapRoute("getDistance");
            route.Points.Add(p1);
            route.Points.Add(p2);
            double distance = route.Distance;
            route.Clear();
            route = null;
            return distance;
        }

        private void button14_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\__RW\_xml\gps_test.gpx";

            GMapRoute playRoute = GetRouteFromKml(filename);

            if (playRoute == null)
            {
                richTextBox1.Text += "無法開啟檔案\n";
                return;

            }
            //playRoute.Stroke.Color = Color.Red;
            playRoute.Stroke = new Pen(Color.FromArgb(144, Color.Red)); //半透明
            playRoute.Stroke.Width = 5;
            playRoute.Stroke.DashStyle = DashStyle.Solid;
            //playRoute.Stroke.DashStyle = DashStyle.Dash;

            markersOverlay.Routes.Add(playRoute);
        }

        public static GMapRoute GetRouteFromKml(string fileName)
        {
            try
            {
                //XDocument root = XDocument.Load(new StreamReader(fileName));
                XElement root = XElement.Load(new StreamReader(fileName));
                IEnumerable<string> coordinates = from c in root.Descendants(XName.Get("coordinates", root.Name.NamespaceName))
                                                  select (string)c;
                foreach (string c in coordinates)
                {
                    List<PointLatLng> points = new List<PointLatLng>();
                    string[] ss = c.Split(new char[] { ' ', '\n', '\t' }, StringSplitOptions.RemoveEmptyEntries);
                    foreach (string sss in ss)
                    {
                        string[] ss2 = sss.Split(new char[] { ',' }, StringSplitOptions.RemoveEmptyEntries);
                        points.Add(new PointLatLng(Convert.ToDouble(ss2[1]), Convert.ToDouble(ss2[0])));
                    }

                    GMapRoute rt = new GMapRoute(points, string.Empty);
                    {
                        rt.Stroke = new Pen(Color.FromArgb(144, Color.Red));
                        rt.Stroke.Width = 5;
                        rt.Stroke.DashStyle = DashStyle.Solid;
                    }
                    return rt;
                }
            }
            catch (Exception ex)
            {
                System.Windows.Forms.MessageBox.Show(ex.Message);
            }
            return null;
        }

        private void button15_Click(object sender, EventArgs e)
        {
            gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖
            //竹北座標
            latitude = 24.838;   //緯度
            longitude = 121.003; //經度
            gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置
            gMapControl1.Zoom = 14; //當前比例

            update_controls_info();

            //畫Route ST
            List<PointLatLng> points = new List<PointLatLng>();

            points.Add(new PointLatLng(24.8493692081609, 120.996723175049));
            points.Add(new PointLatLng(24.8489019025833, 121.003332138062));
            points.Add(new PointLatLng(24.8492134398311, 121.005306243896));
            points.Add(new PointLatLng(24.8505374643828, 121.009511947632));
            points.Add(new PointLatLng(24.8509268806719, 121.010885238647));
            points.Add(new PointLatLng(24.8498365119735, 121.013631820679));
            points.Add(new PointLatLng(24.8483567105118, 121.017322540283));
            points.Add(new PointLatLng(24.8449297339118, 121.02032661438));
            points.Add(new PointLatLng(24.8403343208788, 121.021013259888));
            points.Add(new PointLatLng(24.83690712212, 121.020669937134));
            points.Add(new PointLatLng(24.8326229902382, 121.018524169922));
            points.Add(new PointLatLng(24.8283387101149, 121.016464233398));
            points.Add(new PointLatLng(24.824287981682, 121.014575958252));
            points.Add(new PointLatLng(24.8268586516249, 121.01019859314));
            points.Add(new PointLatLng(24.8304419206983, 121.004705429077));
            points.Add(new PointLatLng(24.8322335163524, 121.001529693604));
            points.Add(new PointLatLng(24.8334798284745, 120.99835395813));
            points.Add(new PointLatLng(24.8361282000777, 120.99723815918));
            points.Add(new PointLatLng(24.83425876718, 120.99268913269));
            points.Add(new PointLatLng(24.8313766694912, 120.987539291382));
            points.Add(new PointLatLng(24.8322335163524, 120.982732772827));
            points.Add(new PointLatLng(24.8379197134477, 120.984363555908));
            points.Add(new PointLatLng(24.8416584404391, 120.98539352417));
            points.Add(new PointLatLng(24.8465653482197, 120.987367630005));
            points.Add(new PointLatLng(24.84640957636, 120.988655090332));
            points.Add(new PointLatLng(24.8461759182027, 120.989942550659));
            points.Add(new PointLatLng(24.8453191678509, 120.99157333374));
            points.Add(new PointLatLng(24.8437614247412, 120.993976593018));
            points.Add(new PointLatLng(24.8460201458526, 120.995092391968));
            points.Add(new PointLatLng(24.8475778605281, 120.995864868164));
            points.Add(new PointLatLng(24.8492913240205, 120.99663734436));

            int len = points.Count;
            richTextBox1.Text += "共有 " + len.ToString() + " 點\n";

            List<PointLatLng> points2 = new List<PointLatLng>();

            int i;
            for (i = 0; i < len; i++)
            {
                points2.Add(points[i]);

                draw_route(points2);
                Application.DoEvents();
                Thread.Sleep(300);
            }
        }

        public void draw_route(List<PointLatLng> points)
        {
            int len = points.Count;

            if (len < 2)
                return;

            //添加線
            //创建“lay”图层
            GMapOverlay lay = new GMapOverlay("lay");
            //创建一条route
            GMapRoute route1 = new GMapRoute("route1");
            //设置route的颜色和粗细
            route1.Stroke = new Pen(Color.Red, 2);  //連線顏色與大小
            //向route中添加点
            int i;
            for (i = 0; i < len; i++)
            {
                route1.Points.Add(new PointLatLng(points[i].Lat, points[i].Lng));
            }
            //将route添加到图层
            lay.Routes.Add(route1);
            //将图层添加到地图
            gMapControl1.Overlays.Add(lay);

            //更新显示route
            gMapControl1.UpdateRouteLocalPosition(route1);
        }

        private void button16_Click(object sender, EventArgs e)
        {
            gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖
            //竹北座標
            latitude = 24.838;   //緯度
            longitude = 121.003; //經度
            gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置
            gMapControl1.Zoom = 14; //當前比例

            update_controls_info();
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void btn_draw_profile_Click(object sender, EventArgs e)
        {
            string location = comboBox1.Text;
            richTextBox1.Text += "location = " + location + "\n";

            if (location == "甘肃")
            {
                richTextBox1.Text += "無 甘肃 資料";
                return;
            }

            string pts = GMapChinaRegion.MapRegion.regionDictionary[location];
            List<PointLatLng> points = new List<PointLatLng>();

            string[] ss = pts.Split(new char[] { ';', '\n', '\t' }, StringSplitOptions.RemoveEmptyEntries);
            double lat_north = -90;
            double lat_south = 90;
            double lng_east = -180;
            double lng_west = 180;
            foreach (string sss in ss)
            {
                string[] ss2 = sss.Split(new char[] { ',' }, StringSplitOptions.RemoveEmptyEntries);
                double lat = Convert.ToDouble(ss2[1]);
                double lng = Convert.ToDouble(ss2[0]);
                if (lat > lat_north)
                    lat_north = lat;
                if (lat < lat_south)
                    lat_south = lat;
                if (lng > lng_east)
                    lng_east = lng;
                if (lng < lng_west)
                    lng_west = lng;
                points.Add(new PointLatLng(lat, lng));
            }

            /*
            //把最東最西最南最北框出來 ST
            richTextBox1.Text += "畫範圍 GMapPolygon\n";
            List<PointLatLng> points2 = new List<PointLatLng>();
            points2.Clear();
            points2.Add(new PointLatLng(lat_south, lng_east));
            points2.Add(new PointLatLng(lat_south, lng_west));
            points2.Add(new PointLatLng(lat_north, lng_west));
            points2.Add(new PointLatLng(lat_north, lng_east));
            points2.Add(new PointLatLng(lat_south, lng_east));
            GMapPolygon polygon = new GMapPolygon(points2, "畫範圍");
            polygon.Stroke = new Pen(Color.Red, 1); //邊框顏色與大小
            polygon.Fill = new SolidBrush(Color.FromArgb(40, Color.Purple));    //有填滿 半透明, 若不寫.Fill, 即無填滿
            markersOverlay.Polygons.Add(polygon);
            //把最東最西最南最北框出來 SP
            */

            int len = points.Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            double lat_center = (lat_south + lat_north) / 2;
            double lng_center = (lng_east + lng_west) / 2;

            int i;
            for (i = 0; i < len / 10; i++)
            {
                //richTextBox1.Text += "i = " + i.ToString() + "\t" + points[i].Lat.ToString() + "\t" + points[i].Lng.ToString() + "\n";
            }

            gMapControl1.MapProvider = GMapProviders.GoogleChinaMap; //簡中地圖

            latitude = lat_center;   //緯度
            longitude = lng_center; //經度

            gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置
            gMapControl1.Zoom = 8; //當前比例

            update_controls_info();

            DrawRoute(points);
        }

        void update_region_info()
        {

            //richTextBox1.Text += "len = " + regionDictionary.Count.ToString() + "\n";
            comboBox1.Items.Clear();

            foreach (string name in GMapChinaRegion.MapRegion.regionDictionary.Keys)  //使用Keys和values屬性迭代集合中的鍵和值, 也可從Values找回Keys
            {
                //richTextBox1.Text += "找到 省份 " + name + "\n";
                comboBox1.Items.Add(name);
            }
            comboBox1.SelectedIndex = 0;
        }

        private void btn_draw_profile2_Click(object sender, EventArgs e)
        {
            string location = comboBox1.Text;
            richTextBox1.Text += "location = " + location + "\n";

            if (location == "甘肃")
            {
                richTextBox1.Text += "無 甘肃 資料";
                return;
            }

            gMapControl1.MapProvider = GMapProviders.GoogleChinaMap; //簡中地圖
            GMapPolygon p = GMapChinaRegion.MapRegion.CreateMapPolygon(location);
            if (p != null)
            {
                markersOverlay.Polygons.Clear();
                markersOverlay.Polygons.Add(p);
                RectLatLng rect = GMapChinaRegion.MapRegion.GetRegionMaxRect(p);
                this.gMapControl1.SetZoomToFitRect(rect);
            }
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            //滑鼠左鍵連線
            line_point.Clear();
            draw_line_point();
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {
            //滑鼠右鍵畫標記
            markersOverlay.Markers.Clear();
        }

        void draw_line_point()
        {
            GMapRoute playRoute = new GMapRoute(line_point, "my route");
            //playRoute.Stroke.Color = Color.Red;   //連線顏色
            //playRoute.Stroke = new Pen(Color.FromArgb(144, Color.Red)); //半透明

            playRoute.Stroke = new Pen(Color.FromArgb(127, Color.Blue), 10);    //連寬度一起寫

            //playRoute.Stroke.Width = 5;
            playRoute.Stroke.DashStyle = DashStyle.Solid;

            markersOverlay.Routes.Clear();
            markersOverlay.Routes.Add(playRoute);

            //只畫起始點
            if (line_point.Count > 0)
            {
                GMapMarker marker = new GMarkerGoogle(line_point[line_point.Count - 1], GMarkerGoogleType.gray_small);

                if (line_point.Count == 1)
                {
                    marker = new GMarkerGoogle(line_point[line_point.Count - 1], GMarkerGoogleType.green);
                }
                else if ((line_point.Count == 2) && (flag_measure_distance == 1))
                {
                    marker = new GMarkerGoogle(line_point[line_point.Count - 1], GMarkerGoogleType.red);
                }
                markersOverlay.Markers.Add(marker);
            }
        }

        void setup_marker_tooltip(GMapMarker marker, string text)
        {
            //設置marker訊息
            marker.ToolTip = new GMapToolTip(marker);
            marker.ToolTipText = text;
            //marker.ToolTip.Fill = Brushes.Blue;   //有填滿 全色, 若不寫.Fill, 即無填滿
            marker.ToolTip.Fill = new SolidBrush(Color.FromArgb(100, Color.Black)); //有填滿 半透明, 若不寫.Fill, 即無填滿
            marker.ToolTip.Foreground = Brushes.White;
            marker.ToolTip.Stroke = Pens.Black;
            marker.ToolTip.TextPadding = new Size(20, 20);
            marker.ToolTipMode = MarkerTooltipMode.OnMouseOver;   //滑鼠靠近才顯示
            //marker.ToolTipMode = MarkerTooltipMode.Always;  //總是顯示
            marker.ToolTip.Format.Alignment = StringAlignment.Near;
        }

        private void radioButton_location_CheckedChanged(object sender, EventArgs e)
        {
            if (rb_location0.Checked == true)
            {
                gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖

                //竹北座標
                latitude = 24.838;   //緯度
                longitude = 121.003; //經度
                gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置
                gMapControl1.Zoom = 14; //當前比例

                update_controls_info();
            }
            else if (rb_location1.Checked == true)
            {
                string[,] station = null;

                station = new string[,] { 
            { "台北", "25.047778", "121.517222"},
            { "新竹", "24.80205", "120.971817"},
            { "台中", "24.136944", "120.684722"},
            { "台南", "23.001389", "120.2175"},
            { "高雄", "22.64", "120.302778"},
            { "台東", "22.791389", "121.118889"},
            { "花蓮", "23.992694", "121.600861"},
            { "宜蘭", "24.750278", "121.7625"},
            };

                int total_station = station.GetUpperBound(0) + 1;
                richTextBox1.Text += "total_station = " + total_station.ToString() + "\n";

                gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖

                latitude = double.Parse(station[0, 1]);
                longitude = double.Parse(station[0, 2]);

                gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置
                gMapControl1.Zoom = 10; //當前比例

                update_controls_info();

                int i;
                for (i = 0; i < total_station; i++)
                {
                    latitude = double.Parse(station[i, 1]);
                    longitude = double.Parse(station[i, 2]);

                    AddMarker(latitude, longitude, GMarkerGoogleType.blue_dot, station[i, 0]);
                }

                richTextBox1.Text += "畫範圍 GMapPolygon 1\n";
                List<PointLatLng> points = new List<PointLatLng>();

                for (i = 0; i < total_station; i++)
                {
                    latitude = double.Parse(station[i, 1]);
                    longitude = double.Parse(station[i, 2]);

                    points.Add(new PointLatLng(latitude, longitude));
                }
                GMapPolygon polygon = new GMapPolygon(points, "mypolygon");
                polygon.Fill = new SolidBrush(Color.FromArgb(50, Color.Red));   //有填滿 半透明, 若不寫.Fill, 即無填滿
                polygon.Stroke = new Pen(Color.Red, 1); //邊框顏色與大小

                GMapOverlay markers_polygon = new GMapOverlay("polygon"); //放置marker的图层
                markers_polygon.Polygons.Add(polygon);
                gMapControl1.Overlays.Add(markers_polygon);  //添加 圖標 Markers 的圖層

                richTextBox1.Text += "畫範圍 GMapPolygon 2\n";
                //List<PointLatLng> points = new List<PointLatLng>();
                points.Clear();
                for (i = 0; i < total_station; i++)
                {
                    latitude = double.Parse(station[i, 1]);
                    longitude = double.Parse(station[i, 2]);

                    points.Add(new PointLatLng(latitude, longitude));
                }

                polygon = new GMapPolygon(points, "畫範圍");
                polygon.Stroke = new Pen(Color.Red, 1); //邊框顏色與大小
                polygon.Fill = new SolidBrush(Color.FromArgb(40, Color.Purple));    //有填滿 半透明, 若不寫.Fill, 即無填滿
                markersOverlay.Polygons.Add(polygon);

                //量測距離 直線
                PointLatLng pt1;
                PointLatLng pt2;
                double distance;
                string dist;

                for (i = 0; i < (total_station - 1); i++)
                {
                    latitude = double.Parse(station[i, 1]);
                    longitude = double.Parse(station[i, 2]);

                    pt1 = new PointLatLng(double.Parse(station[i, 1]), double.Parse(station[i, 2]));
                    pt2 = new PointLatLng(double.Parse(station[i + 1, 1]), double.Parse(station[i + 1, 2]));
                    distance = getDistance(pt1, pt2);

                    //算距離
                    if (rb_km.Checked == true)  //公里
                    {
                        dist = ((float)distance * 1f).ToString("0.##") + " 公里";
                    }
                    else
                    {
                        dist = ((float)distance * 1000f).ToString("0.##") + " 公尺";
                    }
                    richTextBox1.Text += station[i, 0] + " 到 " + station[i + 1, 0] + " 直線距離 : " + dist + "\n";
                    lb_distance.Text = dist;
                }
            }
            else if (rb_location2.Checked == true)
            {
                richTextBox1.Text += "畫範圍 GMapPolygon 北京故宮\n";

                gMapControl1.MapProvider = GMapProviders.GoogleChinaMap; //簡中地圖

                GMapOverlay polygons = new GMapOverlay("polygons");
                List<PointLatLng> points = new List<PointLatLng>();
                points.Add(new PointLatLng(39.92244, 116.3922));
                points.Add(new PointLatLng(39.92280, 116.4015));
                points.Add(new PointLatLng(39.91378, 116.4019));
                points.Add(new PointLatLng(39.91346, 116.3926));
                GMapPolygon polygon = new GMapPolygon(points, "故宮");
                polygon.Fill = new SolidBrush(Color.FromArgb(50, Color.Red));   //有填滿 半透明, 若不寫.Fill, 即無填滿
                polygon.Stroke = new Pen(Color.Red, 1); //邊框顏色與大小
                polygons.Polygons.Add(polygon);
                gMapControl1.Overlays.Add(polygons);

                //故宮中心座標
                latitude = (39.92244 + 39.92280 + 39.91378 + 39.91346) / 4;     //緯度
                longitude = (116.3922 + 116.4015 + 116.4019 + 116.3926) / 4;    //經度
                gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置
                gMapControl1.Zoom = 15; //當前比例

                update_controls_info();
            }
            else if (rb_location3.Checked == true)
            {

            }
            else if (rb_location4.Checked == true)
            {
                gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖

                //馬立波
                latitude = 47.095833;   //緯度
                longitude = 37.549444; //經度
                gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置
                gMapControl1.Zoom = 6; //當前比例

                update_controls_info();
            }
            else if (rb_location5.Checked == true)
            {
                gMapControl1.MapProvider = BingHybridMapProvider.Instance;

                //巴黎
                latitude = 48.866383;   //緯度
                longitude = 2.323575; //經度

                gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置
                gMapControl1.Zoom = 15; //當前比例
            }
            else if (rb_location6.Checked == true)
            {

            }
        }

        private void toolStripMenuItem1_Click(object sender, EventArgs e)
        {
            do_toggle_fullscreen();
        }

        private void toolStripMenuItem2_Click(object sender, EventArgs e)
        {
            //量測距離 單程
            flag_measure_distance = 1;  //0 : 無量測, 1 : 量測距離 單程, 2 : 量測距離 連續
            flag_measure_first_point = false;
            total_distance = 0;
            line_point.Clear();
            draw_line_point();
            markersOverlay.Clear();
        }

        private void toolStripMenuItem3_Click(object sender, EventArgs e)
        {
            //量測距離 連續
            flag_measure_distance = 2;  //0 : 無量測, 1 : 量測距離 單程, 2 : 量測距離 連續
            flag_measure_first_point = false;
            total_distance = 0;
            line_point.Clear();
            draw_line_point();
            markersOverlay.Clear();
        }

        private void toolStripMenuItem4_Click(object sender, EventArgs e)
        {
            if (flag_read_coordinate == false)
            {
                flag_read_coordinate = true;
                toolStripMenuItem4.Text = "停止讀取座標";
            }
            else
            {
                flag_read_coordinate = false;
                toolStripMenuItem4.Text = "讀取座標";
            }
        }

        private void toolStripMenuItem5_Click(object sender, EventArgs e)
        {

        }

        private void toolStripMenuItem6_Click(object sender, EventArgs e)
        {

        }

        private void toolStripMenuItem7_Click(object sender, EventArgs e)
        {
            //離開
            this.Close();
        }

        void do_toggle_fullscreen()
        {
            if (flag_fullscreen == false)
            {
                flag_fullscreen = true;
                toolStripMenuItem1.Text = "離開全螢幕";

                //全螢幕
                //按Alt+F4關閉程式

                //隱藏 除 gMapControl1 外所有控件  全螢幕顯示

                //最大化螢幕
                this.FormBorderStyle = FormBorderStyle.None;
                this.WindowState = FormWindowState.Maximized;

                gMapControl1.Dock = DockStyle.Fill;   //將控件全屏顯示

                for (int i = 0; i < this.Controls.Count; i++)
                {
                    //richTextBox1.Text += "Name: " + this.Controls[i].Name + "\t";
                    //richTextBox1.Text += "Text: " + this.Controls[i].Text + "\t";
                    //richTextBox1.Text += "這項是：" + this.Controls[i].GetType() + "\n";
                    if (this.Controls[i].Name != "gMapControl1")
                    {
                        this.Controls[i].Visible = false;
                    }
                }
                lb_distance.Visible = true;
                lb_distance.Location = new Point(30, 30);

            }
            else if (flag_fullscreen == true)
            {
                flag_fullscreen = false;
                toolStripMenuItem1.Text = "全螢幕";

                //離開全螢幕
                this.FormBorderStyle = FormBorderStyle.Sizable;
                this.WindowState = FormWindowState.Normal;
                gMapControl1.Dock = DockStyle.None;
                for (int i = 0; i < this.Controls.Count; i++)
                {
                    //richTextBox1.Text += "Name: " + this.Controls[i].Name + "\t";
                    //richTextBox1.Text += "Text: " + this.Controls[i].Text + "\t";
                    //richTextBox1.Text += "這項是：" + this.Controls[i].GetType() + "\n";
                    if (this.Controls[i].Name != "gMapControl1")
                    {
                        this.Controls[i].Visible = true;
                    }
                }
                int x_st = 1370;
                int y_st = 12;
                int dy = 25;
                lb_distance.Location = new Point(x_st + 90, y_st + dy * 2);
            }
        }

        private void bt_test00_Click(object sender, EventArgs e)
        {
            //列出省市界資料

            List<string> regionNames = GMapChinaRegion.MapRegion.GetAllRegionName();
            foreach (var regionName in regionNames)
            {
                richTextBox1.Text += "get " + regionName + "\n";
            }
        }

        private void bt_test01_Click(object sender, EventArgs e)
        {

        }


        private void bt_test02_Click(object sender, EventArgs e)
        {

        }

        private void bt_test03_Click(object sender, EventArgs e)
        {

        }

        private void bt_test04_Click(object sender, EventArgs e)
        {

        }

        private void bt_test05_Click(object sender, EventArgs e)
        {

        }

        private void bt_test06_Click(object sender, EventArgs e)
        {

        }

        private void bt_test07_Click(object sender, EventArgs e)
        {

        }

        private void bt_test08_Click(object sender, EventArgs e)
        {

        }

        private void bt_test09_Click(object sender, EventArgs e)
        {

        }
    }
}

