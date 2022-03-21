using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

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

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                //IPHostEntry iphe = Dns.GetHostEntry("ditu.google.cn");
                IPHostEntry iphe = Dns.GetHostEntry("maps.google.com.tw");
            }
            catch
            {
                gMapControl1.Manager.Mode = AccessMode.CacheOnly;
                MessageBox.Show("No internet connection avaible, going to CacheOnly mode.", "GMap.NET Demo", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }

            gMapControl1.CacheLocation = Environment.CurrentDirectory + "\\GMapCache\\"; //缓存位置
            //gMapControl1.MapProvider = GMapProviders.GoogleChinaMap; //簡中地圖
            gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖
            gMapControl1.MinZoom = 2;  //最小比例 >=1
            gMapControl1.MaxZoom = 24; //最大比例 <=24
            gMapControl1.Zoom = 17;     //当前比例
            gMapControl1.ShowCenter = false; //不显示中心十字点
            gMapControl1.DragButton = MouseButtons.Left; //左键拖拽地图
            //gMapControl1.Position = new PointLatLng(32.064, 118.704); //地图中心位置：南京
            gMapControl1.Position = new PointLatLng(24.838, 121.003); //地图中心位置：竹北

            gMapControl1.Overlays.Add(markersOverlay);

            gMapControl1.MouseClick += new MouseEventHandler(gMapControl1_MouseClick);

        }

        void gMapControl1_MouseClick(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Right)
            {
                PointLatLng point = gMapControl1.FromLocalToLatLng(e.X, e.Y);
                GMapMarker marker = new GMarkerGoogle(point, GMarkerGoogleType.green);
                markersOverlay.Markers.Add(marker);
            }
        }





    }
}

