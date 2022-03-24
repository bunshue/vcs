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

using GMap.NET;
using GMap.NET.WindowsForms;
using GMap.NET.MapProviders;
using GMap.NET.WindowsForms.Markers;

namespace vcs_GMap
{
    public partial class Form1 : Form
    {
        private GMapOverlay markersOverlay = new GMapOverlay("markers"); //放置marker的图层

        private GMapOverlay RouteMark = new GMapOverlay("RouteMark");//放置区域标记图层
        /// <summary>
        /// 路径轨迹
        /// </summary> 
        private List<PointLatLng> RoutePoints = new List<PointLatLng>();
        private GmapMarkerRoute Route = null;
        private Point RightBDPoint;
        private string CurrentDir = new DirectoryInfo(Environment.CurrentDirectory).Parent.Parent.FullName;
        private Timer blinkTimer = new Timer();
        private Point BeforeZoomChangeMousePoint = new Point();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            gMapControl1.Manager.ImportFromGMDB(CurrentDir + "\\GMapCache\\mapdata.gmdb");

            gMapControl1.MapProvider = GMapProviders.GoogleChinaMap; //簡中地圖
            //gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖

            gMapControl1.MinZoom = 2;  //最小比例
            gMapControl1.MaxZoom = 17; //最大比例
            gMapControl1.Zoom = 14;     //当前比例
            gMapControl1.Position = new PointLatLng(30.6658229803096, 104.0647315979); //地图中心位置
            gMapControl1.OnMapZoomChanged += new MapZoomChanged(mapControl_OnMapZoomChanged);
            gMapControl1.MouseDown += new MouseEventHandler(mapControl_MouseDown);
            gMapControl1.MouseMove += new MouseEventHandler(mapControl_MouseMove);
            gMapControl1.MouseUp += new MouseEventHandler(mapControl_MouseUp);
            gMapControl1.MouseClick += new MouseEventHandler(gMapControl1_MouseClick);
            gMapControl1.Overlays.Add(markersOverlay);
            gMapControl1.Overlays.Add(RouteMark);
            update_gMapControl1_info();
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
            button8.Location = new Point(x_st + dx * 7, y_st + dy * 1-10);
            button9.Location = new Point(x_st + dx * 7, y_st + dy * 2-20);
            button10.Location = new Point(x_st + dx * 7+60, y_st + dy * 1-10);
            tb_zoom.Location = new Point(x_st + dx * 7 + 60, y_st + dy * 0);

            x_st = 20;
            y_st = 150;
            gMapControl1.Location = new Point(x_st, y_st);
            richTextBox1.Location = new Point(x_st + 960 + 20, y_st);
            
        }

        void setup_gMapControl1()
        {
            //檢查網路狀態, 已設定gmap存取模式
            try
            {
                //IPHostEntry iphe = Dns.GetHostEntry("ditu.google.cn");
                //IPHostEntry iphe = Dns.GetHostEntry("www.google.com.hk");
                IPHostEntry iphe = Dns.GetHostEntry("maps.google.com.tw");
            }
            catch
            {
                //gMapControl1.Manager.Mode = AccessMode.ServerAndCache;
                gMapControl1.Manager.Mode = AccessMode.CacheOnly;
                MessageBox.Show("No internet connection avaible, going to CacheOnly mode.", "GMap.NET Demo", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }

            gMapControl1.CacheLocation = Environment.CurrentDirectory + "\\GMapCache\\"; //缓存位置
            //gMapControl1.MapProvider = GMapProviders.GoogleChinaMap; //簡中地圖
            gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖
            gMapControl1.ShowCenter = false; //不显示中心十字点
            gMapControl1.DragButton = MouseButtons.Left; //左键拖拽地图
        }

        void update_gMapControl1_info()
        {
            tb_zoom.Text = gMapControl1.Zoom.ToString();
        }

        private void button0_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            setup_gMapControl1();

            gMapControl1.MinZoom = 2;  //最小比例 >=1
            gMapControl1.MaxZoom = 24; //最大比例 <=24
            gMapControl1.Zoom = 16;     //当前比例
            gMapControl1.Position = new PointLatLng(24.838, 121.003); //地图中心位置：竹北

            update_gMapControl1_info();
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

        private void button2_Click(object sender, EventArgs e)
        {
            //添加Markers
            gMapControl1.Position = new PointLatLng(24.838, 121.003); //地图中心位置：江理工图书馆
            gMapControl1.Overlays.Add(markersOverlay);   //MapControl添加图markersOverlay_before,null);//图层再添加marker

            string[] studentName = new string[4] { "121.00410306376308, 24.83923062590916", "121.00929660194892, 24.83900079788313", "121.00903566227302, 24.835634744818194", "121.01120945267155, 24.836966817989957" };

            SetLableOnMap_fore(studentName, markersOverlay);
        }

        public void SetLableOnMap_fore(string[] LatLngInfo, GMapOverlay markers_Overlay)
        {
            //给每个坐标打点
            for (int i = 0; i < LatLngInfo.Length; i++)
            {
                string[] LatLng = LatLngInfo[i].Split(',');
                //在坐标点上绘制一绿色点并向图层中添加标签 
                markers_Overlay.Markers.Add(new GMarkerGoogle(new PointLatLng(double.Parse(LatLng[1]), double.Parse(LatLng[0])), GMarkerGoogleType.red));

                richTextBox1.Text += (double.Parse(LatLng[1])).ToString() + "\t" + (double.Parse(LatLng[0])).ToString() + "\n";
                //方便之后寻找到是第几个GMapMarker   
                markers_Overlay.Markers[i].Tag = i;
                markers_Overlay.Markers[i].Tag = "xxxx";
                markers_Overlay.Id = "markroad";
            }

        }

        private void button3_Click(object sender, EventArgs e)
        {
            setup_gMapControl1();

            gMapControl1.MapProvider = GoogleChinaMapProvider.Instance;

            GMap.NET.GMaps.Instance.Mode = GMap.NET.AccessMode.ServerOnly;
            //gMapControl1.SetPositionByKeywords("china,harbin");//设置初始中心为china harbin 

            GMapProvider.Language = LanguageType.ChineseSimplified; //设置地图默认语言
            //gMapControl1.MapProvider = GMapProvidersExt.AMapProvider.Instance;
            //设置控件显示的当前中心位置  
            gMapControl1.Position = new PointLatLng(39.9804435664783, 116.345880031586);
            //设置控件最大的缩放比例  
            gMapControl1.MaxZoom = 24;
            //设置控件最小的缩放比例  
            gMapControl1.MinZoom = 0;
            //设置控件当前的缩放比例  
            gMapControl1.Zoom = 12;
            //gMapControl1.MouseWheelZoomType = MouseWheelZoomType.MousePositionAndCenter;
            gMapControl1.IsAccessible = false;
            GMapProvider.TimeoutMs = 1000;//地图加载完成后设置timeoutms为1000（或者其他大于领零的数值自己尝试0）
            update_gMapControl1_info();
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
            setup_gMapControl1();

            gMapControl1.MapProvider = GMapProviders.GoogleChinaMap; //簡中地圖
            gMapControl1.MinZoom = 4;  //最小比例
            gMapControl1.MaxZoom = 22; //最大比例
            gMapControl1.Zoom = 4;

            gMapControl1.Position = new PointLatLng(32.064, 118.704); //地图中心位置：南京
            update_gMapControl1_info();
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

        private void button7_Click(object sender, EventArgs e)
        {
            //放大
            gMapControl1.Zoom += 1;
            update_gMapControl1_info();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //縮小
            gMapControl1.Zoom -= 1;
            update_gMapControl1_info();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //重新載入
            gMapControl1.ReloadMap();
            update_gMapControl1_info();
        }

        private void button10_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "W = " + gMapControl1.Width.ToString() + "\n";
            richTextBox1.Text += "H = " + gMapControl1.Height.ToString() + "\n";
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


