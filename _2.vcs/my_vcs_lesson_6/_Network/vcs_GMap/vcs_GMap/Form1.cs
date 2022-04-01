using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Net;
using System.Diagnostics;

using GMap.NET;
using GMap.NET.WindowsForms;
using GMap.NET.MapProviders;
using GMap.NET.WindowsForms.Markers;

namespace vcs_GMap
{
    public partial class Form1 : Form
    {
        GMapOverlay markersOverlay = new GMapOverlay("markers"); //放置marker的图层
        GMapOverlay RouteMark = new GMapOverlay("RouteMark");//放置区域标记图层
        GMapOverlay markersOverlay_stop = new GMapOverlay("Stop"); //放置marker的图层

        /// <summary>
        /// 路径轨迹
        /// </summary> 
        private List<PointLatLng> RoutePoints = new List<PointLatLng>();
        private GmapMarkerRoute Route = null;
        private Point RightBDPoint;
        private string CurrentDir = new DirectoryInfo(Environment.CurrentDirectory).Parent.Parent.FullName;
        private Point BeforeZoomChangeMousePoint = new Point();

        TrackBar trackBar1 = new TrackBar();

        string gMapCacheLocation = "GMapCache"; //緩存位置

        double latitude = 24.838;   //緯度
        double longitude = 121.003; //經度

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            richTextBox1.Text += "CurrentDir1 = " + Environment.CurrentDirectory + "\n";
            richTextBox1.Text += "CurrentDir2 = " + new DirectoryInfo(Environment.CurrentDirectory).Parent + "\n";
            richTextBox1.Text += "CurrentDir3 = " + new DirectoryInfo(Environment.CurrentDirectory).Parent.Parent + "\n";
            richTextBox1.Text += "CurrentDir4 = " + new DirectoryInfo(Environment.CurrentDirectory).Parent.Parent.FullName + "\n";
            richTextBox1.Text += "CurrentDir5 = " + CurrentDir + "\n";

            /*
            CurrentDir1 = C:\_git\vcs\_2.vcs\my_vcs_lesson_6\_Network\vcs_GMap\vcs_GMap\bin\Debug
            CurrentDir2 = bin
            CurrentDir3 = vcs_GMap
            CurrentDir4 = C:\_git\vcs\_2.vcs\my_vcs_lesson_6\_Network\vcs_GMap\vcs_GMap
            CurrentDir5 = C:\_git\vcs\_2.vcs\my_vcs_lesson_6\_Network\vcs_GMap\vcs_GMap

            //private string CurrentDir = new DirectoryInfo(Environment.CurrentDirectory).Parent.Parent.FullName;
            */

            setup_controls();
            update_controls_info();
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
            x_st = 20;
            y_st = 20;
            dx = 110;
            dy = 50;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button4.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            button5.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            button6.Location = new Point(x_st + dx * 6, y_st + dy * 0);

            button7.Location = new Point(x_st + dx * 7, y_st + dy * 0);
            button8.Location = new Point(x_st + dx * 7, y_st + dy * 1 - 10);
            button9.Location = new Point(x_st + dx * 7, y_st + dy * 2 - 20);
            button10.Location = new Point(x_st + dx * 7 + 60, y_st + dy * 1 - 10);
            tb_zoom.Location = new Point(x_st + dx * 7 + 60, y_st + dy * 0);
            bt_save.Location = new Point(x_st + dx * 7 + 60, y_st + dy * 2 - 20);

            x_st = 20;
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

            x_st = 1150;
            y_st = 15;
            checkBox1.Location = new Point(x_st, y_st);
            checkBox2.Location = new Point(x_st, y_st + 30);
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
                //gMapControl1.Manager.Mode = AccessMode.ServerOnly;
                //gMapControl1.Manager.Mode = AccessMode.ServerAndCache;
                gMapControl1.Manager.Mode = AccessMode.CacheOnly;
                MessageBox.Show("No internet connection avaible, going to CacheOnly mode.", "GMap.NET Demo", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }

            //gMapControl1.CacheLocation = Environment.CurrentDirectory + "\\GMapCache\\"; //缓存位置
            gMapControl1.CacheLocation = gMapCacheLocation; //緩存位置
            gMapControl1.Manager.ImportFromGMDB(@"gMapCacheLocation\mapdata.gmdb");

            //設定MapProvider
            //gMapControl1.MapProvider = GMapProviders.GoogleChinaMap; //簡中地圖
            //gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖

            gMapControl1.ShowCenter = false; //不显示中心十字点
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
            //gMapControl1.MouseWheelZoomType = MouseWheelZoomType.MousePositionAndCenter;

            gMapControl1.Overlays.Add(markersOverlay);  //添加 圖標 Markers 的圖層
            gMapControl1.Overlays.Add(RouteMark);

            //gMapControl1.Dock = DockStyle.Fill;
            gMapControl1.MarkersEnabled = true;
            gMapControl1.PolygonsEnabled = true;
            gMapControl1.RoutesEnabled = true;
            //gMapControl1.OnMarkerClick += gMapControl1_OnMarkerClick;
            //gMapControl1.OnPositionChanged += gMapControl1_OnPositionChanged;
            //gMapControl1.OnTileLoadComplete += GMap_OnTileLoadComplete;
            //gMapControl1.OnTileLoadStart += GMap_OnTileLoadStart;

            //GMapProvider.Language = LanguageType.ChineseSimplified; //设置地图默认语言
            GMapProvider.Language = LanguageType.ChineseTraditional; //设置地图默认语言
            GMapProvider.TimeoutMs = 1000;//地图加载完成后设置timeoutms为1000(或者其他大于领零的数值自己尝试0)
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
            this.Controls.Add(trackBar1);
            trackBar1.BringToFront();
        }

        void gMapControl1_MouseClick(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Right)
            {
                if (checkBox2.Checked == true)   //滑鼠右鍵畫標記
                {
                    PointLatLng point = gMapControl1.FromLocalToLatLng(e.X, e.Y);

                    richTextBox1.Text += "控件座標(" + e.X.ToString() + ", " + e.Y.ToString() + ")\t地理座標" + point.Lat.ToString() + "\t" + point.Lng.ToString() + "\n";

                    GMapMarker marker = new GMarkerGoogle(point, GMarkerGoogleType.green);
                    markersOverlay.Markers.Add(marker);
                }
            }
        }

        private void trackBar1_ValueChanged(object sender, EventArgs e)
        {
            richTextBox1.Text += trackBar1.Value.ToString() + "  ";
        }

        void update_controls_info()
        {
            tb_zoom.Text = gMapControl1.Zoom.ToString();

            trackBar1.Maximum = gMapControl1.MaxZoom;
            trackBar1.Minimum = gMapControl1.MinZoom;
            trackBar1.Value = (int)gMapControl1.Zoom;
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //gMapControl1.MapProvider = GMapProviders.OpenStreetMap;    //不能用
            //gMapControl1.MapProvider = GMapProviders.GoogleChinaMap; //簡中地圖
            //gMapControl1.MapProvider = GoogleChinaMapProvider.Instance;
            gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖
            //gMapControl1.MapProvider = GMapProviders.GoogleSatelliteMap;    //衛星地圖

            //竹北座標
            latitude = 24.838;   //緯度
            longitude = 121.003; //經度
            gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置
            gMapControl1.Zoom = 14; //當前比例

            update_controls_info();
        }

        public void SetLableOnMap_fore(string[] LatLngInfo, GMapOverlay markers_Overlay)
        {
            //给每个坐标打点
            for (int i = 0; i < LatLngInfo.Length; i++)
            {
                string[] LatLng = LatLngInfo[i].Split(',');
                //在坐标点上绘制一绿色点并向图层中添加标签 
                markers_Overlay.Markers.Add(new GMarkerGoogle(new PointLatLng(double.Parse(LatLng[0]), double.Parse(LatLng[1])), GMarkerGoogleType.green));

                richTextBox1.Text += (double.Parse(LatLng[0])).ToString() + "\t" + (double.Parse(LatLng[1])).ToString() + "\n";
                //方便之后寻找到是第几个GMapMarker   
                markers_Overlay.Markers[i].Tag = i;
                markers_Overlay.Markers[i].Tag = "xxxx";
                markers_Overlay.Id = "markroad";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double R = 0.015;
            double angle = 0;
            double cx = latitude;
            double cy = longitude;
            string[] marker_position = new string[12];
            for (angle = 0; angle < 360; angle += 30)
            {
                marker_position[(int)(angle / 30)] = (cx + R * cosd(angle)).ToString() + ", " + (cy + R * sind(angle)).ToString();

                richTextBox1.Text += angle.ToString() + "\t" + (cx + R * cosd(angle)).ToString() + "\t" + (cy + R * sind(angle)).ToString() + "\n";
            }

            //string[] marker_position = new string[4] { "24.83923062590916, 121.00410306376308", "24.83900079788313, 121.00929660194892", "24.835634744818194, 121.00903566227302", "24.836966817989957, 121.01120945267155" };

            SetLableOnMap_fore(marker_position, markersOverlay);

            /* under test
            double lat = 24.836494165650475 + 10;
            double lon = 121.01959461339993 + 10;

            //DrawPoint(gMapControl1, lat, lon);

            //竹北座標
            latitude = 24.838;   //緯度
            longitude = (121.003+0.02); //經度

            //DrawPoint(gMapControl1, latitude, longitude);
            */
        }

        public void DrawPoint(GMapControl map, double latitude, double longitude)   //緯 經
        {
            markersOverlay_stop.Markers.Add(new GMarkerGoogle(new PointLatLng(latitude, longitude), GMarkerGoogleType.red));

            map.Overlays.Add(markersOverlay_stop);
            richTextBox1.Text += "北緯 " + latitude.ToString() + "\t東經 " + longitude.ToString() + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //gMapControl1.MapProvider = GMapProviders.OpenStreetMap;    //不能用
            //gMapControl1.MapProvider = GMapProviders.GoogleChinaMap; //簡中地圖
            //gMapControl1.MapProvider = GoogleChinaMapProvider.Instance;
            gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖

            //竹北座標
            latitude = 24.838;   //緯度
            longitude = 121.003; //經度
            gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置

            gMapControl1.Zoom = 14; //當前比例

            gMapControl1.EmptyTileColor = System.Drawing.Color.Aquamarine;
            //gMapControl1.GrayScaleMode = true;    //黑白地圖
            gMapControl1.Manager.UsePlacemarkCache = false;
            gMapControl1.Manager.UseMemoryCache = true;
            //gMapControl1.Manager.CancelTileCaching();

            foreach (GMapOverlay overlay in gMapControl1.Overlays)
            {
                foreach (var route in overlay.Routes)
                {
                    var r = new GMapRoute(route.Name);
                    r.Points.AddRange(route.Points);
                    r.Stroke = route.Stroke;
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //gMapControl1.MapProvider = GMapProviders.OpenStreetMap;    //不能用
            //gMapControl1.MapProvider = GMapProviders.GoogleChinaMap; //簡中地圖
            //gMapControl1.MapProvider = GoogleChinaMapProvider.Instance;
            gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖
            //gMapControl1.MapProvider = GMapProviders.GoogleSatelliteMap;    //衛星地圖

            //上海座標
            latitude = 31.128199299112;   //緯度
            longitude = 121.489562988281; //經度
            gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置
            gMapControl1.Zoom = 10; //當前比例

            update_controls_info();

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


            SetLableOnMap_fore(marker_position, markersOverlay);



        }

        private void button4_Click(object sender, EventArgs e)
        {
            /*
            GMapRoute route_1 = new GMapRoute(list1, "route_1");
            route_1.Stroke = (Pen)route_1.Stroke.Clone();
            route_1.Stroke.Color = Color.AliceBlue; 
            */
        }

        private void button5_Click(object sender, EventArgs e)
        {
            /*
            List<PointLatLng> PointLL = new List<PointLatLng>();
            PointLL.Add(double.Parse("121.00410306376308"), double.Parse("24.83923062590916"));


            Point.Add(new Point((int)gp.X - Origin.X - OriginOffset.X, (int)gp.Y - Origin.Y - OriginOffset.Y));
            PointLL.Add(NewPointLatLng);
            */
        }

        public static void DrawMap(GMapControl map, List<Point> points, Color color, bool includeMarkers)
        {
            Pen pen = new Pen(color, 3.0f);

            List<PointLatLng> allMapPoints = points.Select(point => new PointLatLng(point.X, point.Y)).ToList();

            GMapRoute route = new GMapRoute(allMapPoints, "Route");
            route.Stroke = pen;
            map.ZoomAndCenterRoute(route);

            GMapOverlay overlay = new GMapOverlay("Overlay");
            if (includeMarkers)
            {
                //overlay.Markers.Add(new GMap.NET.WindowsForms.Markers.GMapMarkerGoogleGreen(new PointLatLng(allMapPoints.First().Lat, allMapPoints.First().Lng)));
                //overlay.Markers.Add(new GMap.NET.WindowsForms.Markers.GMarkerGoogleType.GMapMarkerGoogleGreen(new PointLatLng(allMapPoints.First().Lat, allMapPoints.First().Lng)));
                //overlay.Markers.Add(new GMap.NET.WindowsForms.Markers.GMapMarkerGoogleRed(new PointLatLng(allMapPoints.Last().Lat, allMapPoints.Last().Lng)));
            }
            overlay.Routes.Add(route);
            map.Overlays.Add(overlay);
        }

        /// <summary>
        /// 地图拖拽向量
        /// 在进行地图的缩放后需要将该偏移量清零
        /// </summary>
        private int DragOffsetX = 0, DragOffsetY = 0;

        void mapControl_MouseDown(object sender, MouseEventArgs e)
        {
            //richTextBox1.Text += "MouseDown\n";
            if (e.Button == MouseButtons.Left)
            {
                if (checkBox1.Checked == true)   //滑鼠左鍵連線
                {
                    PointLatLng point = gMapControl1.FromLocalToLatLng(e.X, e.Y);
                    if (Route == null)
                    {
                        Route = new GmapMarkerRoute(point);
                        Route.Origin.X = gMapControl1.Size.Width / 2;
                        Route.Origin.Y = gMapControl1.Size.Height / 2;
                        Route.OriginOffset.X = DragOffsetX;
                        Route.OriginOffset.Y = DragOffsetY;
                        RouteMark.Markers.Add(Route as GMapMarker);
                    }
                    Route.AddPoint(point);
                }
            }
            else if (e.Button == MouseButtons.Right)
            {
                //记录鼠标按下位置
                RightBDPoint.X = e.X;
                RightBDPoint.Y = e.Y;
            }
        }

        void mapControl_MouseMove(object sender, MouseEventArgs e)
        {
            //richTextBox1.Text += "MouseMove\n";
            PointLatLng point = gMapControl1.FromLocalToLatLng(e.X, e.Y);

            BeforeZoomChangeMousePoint.X = e.X;
            BeforeZoomChangeMousePoint.Y = e.Y;
        }

        void mapControl_MouseUp(object sender, MouseEventArgs e)
        {
            //richTextBox1.Text += "MouseUp\n";
            if (e.Button == MouseButtons.Right)
            {
                //在拖拽地图后地图原点和视窗原点的偏移量
                DragOffsetX = DragOffsetX + e.X - RightBDPoint.X;
                DragOffsetY = DragOffsetY + e.Y - RightBDPoint.Y;
                if (Route != null)
                {
                    //设置Route的中心偏移
                    Route.OriginOffset.X = DragOffsetX;
                    Route.OriginOffset.Y = DragOffsetY;
                }
            }
        }

        void mapControl_OnMapZoomChanged()
        {
            //richTextBox1.Text += "OnMapZoomChanged\n";
            //在进行地图的缩放后，视图的原点会重新回到MapControl控件的中心点
            DragOffsetX = 0;
            DragOffsetY = 0;

            if (Route != null)
            {
                Route.IsZoomChanged = true;
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "test 6\n";
            gMapControl1.SetPositionByKeywords("竹東鎮");  //設置初始中心, 看似無效

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
            //重新載入
            gMapControl1.ReloadMap();
            update_controls_info();
        }

        private void button10_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "W = " + gMapControl1.Width.ToString() + "\n";
            richTextBox1.Text += "H = " + gMapControl1.Height.ToString() + "\n";
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
                //gMapControl1.MapProvider = GMapProviders.OpenStreetMap;    //不能用
                //gMapControl1.MapProvider = GoogleChinaMapProvider.Instance;
            }
        }
    }

    class GmapMarkerRoute : GMapMarker
    {
        //用户绘制在视窗中的点，是将经纬度转换成GPoint再加上偏移处理后的点
        private List<Point> Point = new List<Point>();
        //需要绘制的经纬度点集
        private List<PointLatLng> PointLL = new List<PointLatLng>();


        // 是否有新的点加入
        private bool HasNewPoint = false;
        //新加入点的经纬度
        private PointLatLng NewPointLatLng;
        /// <summary>
        /// 图层缩放比例是否变化
        /// </summary>
        public bool IsZoomChanged = false;
        /// <summary>
        /// 拖拽地图后图层原点与视窗原点的偏差向量
        /// </summary>
        public Point OriginOffset = new Point();
        /// <summary>
        /// 视窗原点相对于图层原点的像素偏差向量
        /// 视窗原点默认是视窗中心点
        /// 图层原点默认是视窗左上角的点
        /// </summary>
        public Point Origin = new Point();
        /// <summary>
        /// 绘制点集的pen
        /// </summary>
        public Pen pen = new Pen(Color.Red, 1);


        public GmapMarkerRoute(GMap.NET.PointLatLng p)
            : base(p)
        {

        }

        public override void OnRender(Graphics g)
        {
            GPoint gp = new GPoint();

            //地图拖拽
            if (Overlay.Control.IsDragging)
            {
                pen.Color = Color.Green;
            }
            //地图缩放比例改变后需要重新计算Point    
            else if (IsZoomChanged)
            {
                pen.Color = Color.Black;
                OriginOffset.X = 0;
                OriginOffset.Y = 0;
                if (PointLL.Count > 1)
                {
                    Point.Clear();
                    {
                        foreach (PointLatLng p in PointLL)
                        {
                            gp = Overlay.Control.FromLatLngToLocal(p);
                            Point.Add(new Point((int)(gp.X - Origin.X), (int)(gp.Y - Origin.Y)));
                        }
                    }
                }
                IsZoomChanged = false;
            }
            //其他事件
            else
            {
                pen.Color = Color.Red;
            }
            //判断是否有新的点加入,如果有将其添加进Point点集
            //同时也添加相应的经纬度到相关点集
            if (HasNewPoint)
            {
                gp = Overlay.Control.FromLatLngToLocal(NewPointLatLng);
                Point.Add(new Point((int)gp.X - Origin.X - OriginOffset.X, (int)gp.Y - Origin.Y - OriginOffset.Y));
                PointLL.Add(NewPointLatLng);
                HasNewPoint = false;
            }
            if (Point.Count > 1)
            {
                g.DrawLines(pen, Point.ToArray());
            }
        }

        public void AddPoint(PointLatLng p)
        {
            NewPointLatLng = p;
            HasNewPoint = true;
        }
    }
}

