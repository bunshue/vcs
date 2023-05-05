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
using System.Xml.Serialization;

using Newtonsoft.Json;

using GMap.NET;
using GMap.NET.WindowsForms;
using GMap.NET.MapProviders;
using GMap.NET.WindowsForms.Markers;
using GMapDrawTools;
using GMapChinaRegion;
using GMapDownload;
using GMapTools;

//需要GMap.NET.Core.dll 和 GMap.NET.WindowsForms.dll這兩個檔案。

namespace vcs_GMap
{
    public partial class Form1 : Form
    {
        private GMapOverlay markersOverlay = new GMapOverlay("markers"); //放置marker的圖層
        private GMapOverlay polygonsOverlay = new GMapOverlay("polygonsOverlay");

        //按滑鼠左鍵連線
        //需要繪制的經緯度點集
        private List<PointLatLng> line_point = new List<PointLatLng>();

        TrackBar trackBar1 = new TrackBar();

        string gMapCacheLocation = @"C:\_git\vcs\_1.data\______test_files1\GMapCache1"; //緩存位置

        double latitude = 24.838;   //緯度
        double longitude = 121.003; //經度

        //量測距離用
        int flag_measure_distance = 0;  //0 : 無量測, 1 : 量測距離 單程, 2 : 量測距離 連續
        bool flag_measure_first_point = false;
        PointLatLng pt1 = new PointLatLng(0, 0);
        PointLatLng pt2 = new PointLatLng(0, 0);
        PointLatLng pt1_tmp = new PointLatLng(0, 0);
        double total_distance = 0;

        //讀取座標資料
        bool flag_read_coordinate = false;

        bool flag_fullscreen = false;

        private const int ICON_LINEWDITH = 4; //設定按鈕畫線線寬
        private const int ICON_W = 50; //設定按鈕大小 W
        private const int ICON_H = 50; //設定按鈕大小 H

        Country china;
        private GMapOverlay regionOverlay = new GMapOverlay("region");
        private GMapAreaPolygon currentAreaPolygon;

        private Draw draw;
        private DrawDistance drawDistance;  // Draw distane tool

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

            draw = new Draw(this.gMapControl1);
            draw.DrawComplete += new EventHandler<DrawEventArgs>(draw_DrawComplete);

            drawDistance = new DrawDistance(this.gMapControl1);
            drawDistance.DrawComplete += new EventHandler<DrawDistanceEventArgs>(drawDistance_DrawComplete);

            rb_location0.Checked = true;
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

            x_st = 10;
            y_st = 10;

            gMapControl1.Size = new Size(1130, 1060);
            gMapControl1.Location = new Point(x_st, y_st);

            int W = 250;
            int H = 180;
            dx = W + 10;
            dy = H + 10;

            groupBox_map_control1.Size = new Size(W, H);
            groupBox_map_control2.Size = new Size(W, H);
            groupBox_map.Size = new Size(W, H);
            groupBox_map2.Size = new Size(W * 2 - 10, H + 60);
            groupBox_location.Size = new Size(W, H);

            x_st = 1210;
            groupBox_map_control1.Location = new Point(x_st, y_st + dy * 0);
            groupBox_map_control2.Location = new Point(x_st, y_st + dy * 1);
            groupBox_map.Location = new Point(x_st, y_st + dy * 2);
            groupBox_location.Location = new Point(x_st, y_st + dy * 3);
            groupBox_map2.Location = new Point(x_st, y_st + dy * 4);

            W = 120;
            H = 750;
            groupBox_basic.Size = new Size(W, H);
            groupBox_basic.Location = new Point(x_st + dx, y_st);

            groupBox_map_downloader.Size = new Size(W, H);
            groupBox_map_downloader.Location = new Point(x_st + dx + W, y_st);

            dx += W * 2;
            y_st = 0;
            W = 200;
            H = 500;
            treeView1.Size = new Size(W, H);
            treeView1.Location = new Point(x_st + dx, y_st);

            richTextBox1.Size = new Size(W, H);
            richTextBox1.Location = new Point(x_st + dx, y_st + H);

            int BTN_WIDTH = 50;
            int BTN_HEIGHT = 50;
            bt_clear.Width = BTN_WIDTH;
            bt_clear.Height = BTN_HEIGHT;
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            bt_open_folder.Width = BTN_WIDTH;
            bt_open_folder.Height = BTN_HEIGHT;
            bt_open_folder.Text = "";
            bt_open_folder.BackgroundImage = Properties.Resources.open_folder;
            bt_open_folder.BackgroundImageLayout = ImageLayout.Zoom;
            bt_open_folder.Location = new Point(bt_clear.Location.X - BTN_WIDTH, bt_clear.Location.Y);

            x_st = 20;
            y_st = 15;
            dx = 100;
            dy = 16;

            radioButton1.Location = new Point(x_st, y_st + dy * 0);
            radioButton2.Location = new Point(x_st, y_st + dy * 1);
            radioButton3.Location = new Point(x_st, y_st + dy * 2);
            radioButton4.Location = new Point(x_st, y_st + dy * 3);
            radioButton5.Location = new Point(x_st, y_st + dy * 4);
            radioButton6.Location = new Point(x_st, y_st + dy * 5);
            radioButton7.Location = new Point(x_st, y_st + dy * 6);
            radioButton8.Location = new Point(x_st, y_st + dy * 7);
            radioButton9.Location = new Point(x_st, y_st + dy * 8);
            radioButton10.Location = new Point(x_st, y_st + dy * 9);
            radioButton11.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            radioButton12.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            radioButton13.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            radioButton14.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            radioButton15.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            radioButton16.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            radioButton17.Location = new Point(x_st + dx * 1, y_st + dy * 6);


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
            radioButton15.Text = "中國衛星地圖";
            radioButton16.Text = "中國地形地圖";
            radioButton17.Text = "其他";
            lb_distance.Text = "";

            rb_location0.Location = new Point(x_st, y_st + dy * 0);
            rb_location1.Location = new Point(x_st, y_st + dy * 1);
            rb_location2.Location = new Point(x_st, y_st + dy * 2);
            rb_location3.Location = new Point(x_st, y_st + dy * 3);
            rb_location4.Location = new Point(x_st, y_st + dy * 4);
            rb_location5.Location = new Point(x_st, y_st + dy * 5);
            rb_location6.Location = new Point(x_st, y_st + dy * 6);
            rb_location7.Location = new Point(x_st, y_st + dy * 7);
            rb_location8.Location = new Point(x_st, y_st + dy * 8);
            rb_location9.Location = new Point(x_st, y_st + dy * 9);
            rb_location10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            rb_location11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            rb_location12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            rb_location13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            rb_location14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            rb_location15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            rb_location16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            rb_location17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            rb_location18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            rb_location19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            dx = 150;
            dy = 14;
            rb_map00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            rb_map01.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            rb_map02.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            rb_map03.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            rb_map04.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            rb_map05.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            rb_map06.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            rb_map07.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            rb_map08.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            rb_map09.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            rb_map10.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            rb_map11.Location = new Point(x_st + dx * 0, y_st + dy * 11);
            rb_map12.Location = new Point(x_st + dx * 0, y_st + dy * 12);
            rb_map13.Location = new Point(x_st + dx * 0, y_st + dy * 13);

            rb_map14.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            rb_map15.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            rb_map16.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            rb_map17.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            rb_map18.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            rb_map19.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            rb_map20.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            rb_map21.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            rb_map22.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            rb_map23.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            rb_map24.Location = new Point(x_st + dx * 1, y_st + dy * 10);
            rb_map25.Location = new Point(x_st + dx * 1, y_st + dy * 11);
            rb_map26.Location = new Point(x_st + dx * 1, y_st + dy * 12);
            rb_map27.Location = new Point(x_st + dx * 1, y_st + dy * 13);

            rb_map28.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            rb_map29.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            rb_map30.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            rb_map31.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            rb_map32.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            rb_map33.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            rb_map34.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            rb_map35.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            rb_map36.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            rb_map37.Location = new Point(x_st + dx * 2, y_st + dy * 9);
            rb_map38.Location = new Point(x_st + dx * 2, y_st + dy * 10);
            rb_map39.Location = new Point(x_st + dx * 2, y_st + dy * 11);
            rb_map40.Location = new Point(x_st + dx * 2, y_st + dy * 12);
            rb_map41.Location = new Point(x_st + dx * 2, y_st + dy * 13);

            rb_map00.Text = "Google普通地圖";
            rb_map01.Text = "Google衛星地圖";
            rb_map02.Text = "Google混合地圖";
            rb_map03.Text = "Google中國普通地圖";
            rb_map04.Text = "Google中國衛星地圖";
            rb_map05.Text = "Google中國混合地圖";
            rb_map06.Text = "Google中國地形地圖";
            rb_map07.Text = "百度地圖 普通";
            rb_map08.Text = "百度地圖 衛星";
            rb_map09.Text = "百度地圖 混合";
            rb_map10.Text = "高德地圖 普通地圖";
            rb_map11.Text = "高德地圖 衛星地圖";
            rb_map12.Text = "高德地圖 混合地圖";
            rb_map13.Text = "騰迅地圖 普通地圖";
            rb_map14.Text = "騰迅地圖 衛星地圖";
            rb_map15.Text = "騰迅地圖 混合地圖";
            rb_map16.Text = "騰迅地圖 地形地圖";
            rb_map17.Text = "Here地圖 普通地圖";
            rb_map18.Text = "Here地圖 衛星地圖";
            rb_map19.Text = "Here地圖 混合地圖";
            rb_map20.Text = "Bing地圖 普通地圖";
            rb_map21.Text = "Bing地圖 衛星地圖";
            rb_map22.Text = "Bing地圖 混合地圖";
            rb_map23.Text = "Bing地圖 普通地圖中文";
            rb_map24.Text = "天地圖 街道地圖(球面墨卡托)";
            rb_map25.Text = "天地圖 衛星地圖(球面墨卡托)";
            rb_map26.Text = "天地圖 混合地圖(球面墨卡托)";
            rb_map27.Text = "天地圖 街道地圖(WGS84)";
            rb_map28.Text = "天地圖 衛星地圖(WGS84)";
            rb_map29.Text = "天地圖 混合地圖(WGS84)";
            rb_map30.Text = "天地圖 福建街道地圖";
            rb_map31.Text = "天地圖 福建衛星地圖";
            rb_map32.Text = "天地圖 福建混合地圖";
            rb_map33.Text = "ArcGIS地圖 arcGIS街道地圖";
            rb_map34.Text = "ArcGIS地圖 arcGIS街道地圖(無POI)";
            rb_map35.Text = "ArcGIS地圖 arcGIS街道地圖(冷色版)";
            rb_map36.Text = "ArcGIS地圖 arcGIS街道地圖(灰色版)";
            rb_map37.Text = "ArcGIS地圖 arcGIS街道地圖(暖色版)";
            rb_map38.Text = "ArcGIS地圖 arcGIS衛星地圖(無偏移)";
            rb_map39.Text = "搜狗地圖 普通地圖";
            rb_map40.Text = "船舶地圖 船舶";
            rb_map41.Text = "";

            rb_map07.Enabled = false;
            rb_map08.Enabled = false;
            rb_map09.Enabled = false;
            rb_map10.Enabled = false;
            rb_map11.Enabled = false;
            rb_map12.Enabled = false;
            rb_map13.Enabled = false;
            rb_map14.Enabled = false;
            rb_map15.Enabled = false;
            rb_map16.Enabled = false;
            rb_map17.Enabled = false;
            rb_map18.Enabled = false;
            rb_map19.Enabled = false;
            rb_map23.Enabled = false;
            rb_map24.Enabled = false;
            rb_map25.Enabled = false;
            rb_map26.Enabled = false;
            rb_map27.Enabled = false;
            rb_map28.Enabled = false;
            rb_map29.Enabled = false;
            rb_map30.Enabled = false;
            rb_map31.Enabled = false;
            rb_map32.Enabled = false;
            rb_map33.Enabled = false;
            rb_map34.Enabled = false;
            rb_map35.Enabled = false;
            rb_map36.Enabled = false;
            rb_map37.Enabled = false;
            rb_map38.Enabled = false;
            rb_map39.Enabled = false;
            rb_map40.Enabled = false;

            rb_map00.CheckedChanged += radioButton_CheckedChanged2;
            rb_map01.CheckedChanged += radioButton_CheckedChanged2;
            rb_map02.CheckedChanged += radioButton_CheckedChanged2;
            rb_map03.CheckedChanged += radioButton_CheckedChanged2;
            rb_map04.CheckedChanged += radioButton_CheckedChanged2;
            rb_map05.CheckedChanged += radioButton_CheckedChanged2;
            rb_map06.CheckedChanged += radioButton_CheckedChanged2;
            rb_map07.CheckedChanged += radioButton_CheckedChanged2;
            rb_map08.CheckedChanged += radioButton_CheckedChanged2;
            rb_map09.CheckedChanged += radioButton_CheckedChanged2;
            rb_map10.CheckedChanged += radioButton_CheckedChanged2;
            rb_map11.CheckedChanged += radioButton_CheckedChanged2;
            rb_map12.CheckedChanged += radioButton_CheckedChanged2;
            rb_map13.CheckedChanged += radioButton_CheckedChanged2;
            rb_map14.CheckedChanged += radioButton_CheckedChanged2;
            rb_map15.CheckedChanged += radioButton_CheckedChanged2;
            rb_map16.CheckedChanged += radioButton_CheckedChanged2;
            rb_map17.CheckedChanged += radioButton_CheckedChanged2;
            rb_map18.CheckedChanged += radioButton_CheckedChanged2;
            rb_map19.CheckedChanged += radioButton_CheckedChanged2;
            rb_map20.CheckedChanged += radioButton_CheckedChanged2;
            rb_map21.CheckedChanged += radioButton_CheckedChanged2;
            rb_map22.CheckedChanged += radioButton_CheckedChanged2;
            rb_map23.CheckedChanged += radioButton_CheckedChanged2;
            rb_map24.CheckedChanged += radioButton_CheckedChanged2;
            rb_map25.CheckedChanged += radioButton_CheckedChanged2;
            rb_map26.CheckedChanged += radioButton_CheckedChanged2;
            rb_map27.CheckedChanged += radioButton_CheckedChanged2;
            rb_map28.CheckedChanged += radioButton_CheckedChanged2;
            rb_map29.CheckedChanged += radioButton_CheckedChanged2;
            rb_map30.CheckedChanged += radioButton_CheckedChanged2;
            rb_map31.CheckedChanged += radioButton_CheckedChanged2;
            rb_map32.CheckedChanged += radioButton_CheckedChanged2;
            rb_map33.CheckedChanged += radioButton_CheckedChanged2;
            rb_map34.CheckedChanged += radioButton_CheckedChanged2;
            rb_map35.CheckedChanged += radioButton_CheckedChanged2;
            rb_map36.CheckedChanged += radioButton_CheckedChanged2;
            rb_map37.CheckedChanged += radioButton_CheckedChanged2;
            rb_map38.CheckedChanged += radioButton_CheckedChanged2;
            rb_map39.CheckedChanged += radioButton_CheckedChanged2;
            rb_map40.CheckedChanged += radioButton_CheckedChanged2;
            rb_map41.CheckedChanged += radioButton_CheckedChanged2;

            x_st = 10;
            y_st = 20;
            dx = 100;
            dy = 45;

            bt_test00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_test01.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_test02.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_test03.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_test04.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            bt_test05.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            bt_test06.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            bt_test07.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            bt_test08.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            bt_test09.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            bt_test10.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            bt_test11.Location = new Point(x_st + dx * 0, y_st + dy * 11);
            bt_test12.Location = new Point(x_st + dx * 0, y_st + dy * 12);
            bt_test13.Location = new Point(x_st + dx * 0, y_st + dy * 13);
            bt_test14.Location = new Point(x_st + dx * 0, y_st + dy * 14);
            bt_test15.Location = new Point(x_st + dx * 0, y_st + dy * 15);

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
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 11);
            button12.Location = new Point(x_st + dx * 0, y_st + dy * 12);
            button13.Location = new Point(x_st + dx * 0, y_st + dy * 13);
            button14.Location = new Point(x_st + dx * 0, y_st + dy * 14);
            button15.Location = new Point(x_st + dx * 0, y_st + dy * 15);


            x_st = 50;
            y_st = 20;
            btn_north.Location = new Point(x_st, y_st);
            btn_east.Location = new Point(x_st + 32, y_st + 32);
            btn_west.Location = new Point(x_st - 32, y_st + 32);
            btn_south.Location = new Point(x_st, y_st + 64);

            tb_zoom.Location = new Point(x_st + 70, y_st - 10);
            bt_zoom_in.Location = new Point(x_st + 70, y_st + 30);
            bt_zoom_out.Location = new Point(x_st + 70, y_st + 65);

            dy = 33;
            bt_draw0.Location = new Point(x_st + 70 + 70, y_st - 10 + dy * 0);
            bt_draw1.Location = new Point(x_st + 70 + 70, y_st - 10 + dy * 1);
            bt_draw2.Location = new Point(x_st + 70 + 70, y_st - 10 + dy * 2);
            bt_draw3.Location = new Point(x_st + 70 + 70, y_st - 10 + dy * 3);
            bt_draw4.Location = new Point(x_st + 70 + 70, y_st - 10 + dy * 4);
            bt_draw5.Location = new Point(x_st + 70 + 0, y_st - 10 + dy * 4);
            bt_draw1.Enabled = false;
            bt_draw2.Enabled = false;
            //bt_draw5.Enabled = false;

            x_st = 20;
            y_st = 20;
            dy = 25;
            checkBox1.Location = new Point(x_st, y_st + dy * 0);
            checkBox2.Location = new Point(x_st, y_st + dy * 1);

            rb_km.Location = new Point(x_st, y_st + dy * 2);
            rb_m.Location = new Point(x_st + 50, y_st + dy * 2);
            lb_distance.Location = new Point(x_st + 100, y_st + dy * 2);

            comboBox1.Location = new Point(x_st, y_st + dy * 3);
            btn_draw_profile.Location = new Point(x_st, y_st + dy * 4);
            btn_draw_profile2.Location = new Point(x_st + 85, y_st + dy * 4);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;

            //離開按鈕的寫法
            bt_exit_setup();

            //最小化按鈕的寫法
            bt_minimize_setup();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        void bt_minimize_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_minimize = new Button();  // 實例化按鈕
            bt_minimize.Size = new Size(w, h);
            bt_minimize.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            //g.DrawLine(p, 0, 0, w - 1, h - 1);
            //g.DrawLine(p, w - 1, 0, 0, h - 1);
            g.DrawLine(p, w / 4, h / 2 - 1, w * 3 / 4, h / 2 - 1);
            bt_minimize.Image = bmp;

            bt_minimize.Location = new Point(this.ClientSize.Width - bt_minimize.Width * 2 - 2, 0);
            bt_minimize.Click += bt_minimize_Click;     // 加入按鈕事件

            this.Controls.Add(bt_minimize); // 將按鈕加入表單
            bt_minimize.BringToFront();     //移到最上層
        }

        private void bt_minimize_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;   //設定表單最小化
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_open_folder_Click(object sender, EventArgs e)
        {
            //取得目前所在路徑
            string currentPath = Directory.GetCurrentDirectory();
            richTextBox1.Text += "目前所在路徑: " + currentPath + "\n";
            //開啟檔案總管
            Process.Start(currentPath);
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
            gMapControl1.DragButton = MouseButtons.Left; //左鍵拖拽地圖

            gMapControl1.MinZoom = 1;  //設置控件最小縮放比例 >=1
            gMapControl1.MaxZoom = 24; //設置控件最大縮放比例 <=24
            gMapControl1.Zoom = 14;     //當前比例

            //各種地圖的事件
            gMapControl1.OnMapZoomChanged += new MapZoomChanged(gMapControl1_OnMapZoomChanged);
            gMapControl1.MouseDown += new MouseEventHandler(gMapControl1_MouseDown);
            gMapControl1.MouseMove += new MouseEventHandler(gMapControl1_MouseMove);
            gMapControl1.MouseUp += new MouseEventHandler(gMapControl1_MouseUp);
            gMapControl1.MouseClick += new MouseEventHandler(gMapControl1_MouseClick);
            gMapControl1.MouseDoubleClick += new MouseEventHandler(gMapControl1_MouseDoubleClick);
            gMapControl1.Paint += new PaintEventHandler(gMapControl1_Paint);
            //gMapControl1.MouseWheelZoomType = MouseWheelZoomType.MousePositionAndCenter;
            gMapControl1.KeyDown += new KeyEventHandler(gMapControl1_KeyDown);
            gMapControl1.OnMarkerClick += gMapControl1_OnMarkerClick;
            //gMapControl1.OnMarkerClick += new MarkerClick(gMapControl1_OnMarkerClick);
            //gMapControl1.OnPositionChanged += gMapControl1_OnPositionChanged;
            //gMapControl1.OnPositionChanged += new PositionChanged(gMapControl1_OnPositionChanged);
            //gMapControl1.OnTileLoadComplete += GMap_OnTileLoadComplete;
            //gMapControl1.OnTileLoadStart += GMap_OnTileLoadStart;

            gMapControl1.OnMarkerEnter += new MarkerEnter(gMapControl1_OnMarkerEnter);
            gMapControl1.OnMarkerLeave += new MarkerLeave(gMapControl1_OnMarkerLeave);
            gMapControl1.OnPolygonClick += new PolygonClick(gMapControl1_OnPolygonClick);
            gMapControl1.OnPolygonEnter += new PolygonEnter(gMapControl1_OnPolygonEnter);
            gMapControl1.OnPolygonLeave += new PolygonLeave(gMapControl1_OnPolygonLeave);
            //gMapControl1.OnPolygonDoubleClick += new PolygonDoubleClick(gMapControl1_OnPolygonDoubleClick);

            this.ActiveControl = this.gMapControl1;//選中pictureBox1，不然沒法觸發事件

            gMapControl1.Overlays.Add(markersOverlay);  //添加 圖標 Markers 的圖層
            gMapControl1.Overlays.Add(polygonsOverlay);

            //gMapControl1.Dock = DockStyle.Fill;   //將控件全屏顯示
            gMapControl1.CanDragMap = true; //滑鼠右鍵拖動地圖
            gMapControl1.MarkersEnabled = true; //顯示markers
            gMapControl1.PolygonsEnabled = true;    //顯示polygon
            gMapControl1.RoutesEnabled = true;
            //gMapControl1.ShowTileGridLines = true;  //顯示座標格網  常有問題 可能是timeout
            //gMapControl1.GrayScaleMode = true;    //黑白地圖

            //GMapProvider.Language = LanguageType.ChineseSimplified; //設置地圖默認語言
            GMapProvider.Language = LanguageType.ChineseTraditional; //設置地圖默認語言
            GMapProvider.TimeoutMs = 10000;//地圖加載完成后設置timeoutms為1000(或者其他大于領零的數值自己嘗試0)
        }

        void setup_trackBar()
        {
            trackBar1.Orientation = Orientation.Vertical;
            trackBar1.TickStyle = TickStyle.Both;
            trackBar1.TickFrequency = 1;
            trackBar1.SmallChange = 1;
            trackBar1.LargeChange = 1;
            trackBar1.Maximum = 100;
            trackBar1.Minimum = 1;
            trackBar1.Value = 10;
            trackBar1.Height = gMapControl1.Height * 9 / 10;
            trackBar1.Width = 10;
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


        void gMapControl1_OnMarkerEnter(GMapMarker item)
        {
        }

        void gMapControl1_OnMarkerLeave(GMapMarker item)
        {
        }


        //void gMapControl1_OnMarkerClick(GMapMarker item, MouseEventArgs e)
        //{
        //if (e.Button == MouseButtons.Left)
        //{
        /*
            GMapOverlay overlay = item.Overlay;
            if (overlay.Markers.Contains(item))
            {
                overlay.Markers.Remove(item);
            }

            if (gMapControl1.Overlays.Contains(overlay))
            {
                gMapControl1.Overlays.Remove(overlay);
            }
         */
        //}
        //}

        void gMapControl1_OnPolygonClick(GMapPolygon item, MouseEventArgs e)
        {
        }



        void gMapControl1_OnPolygonEnter(GMapPolygon item)
        {
            /*
            if (item is GMapAreaPolygon)
            {
                GMapAreaPolygon areaPolygon = item as GMapAreaPolygon;
                if (currentAreaPolygon != null && currentAreaPolygon == areaPolygon)
                {
                    currentAreaPolygon = item as GMapAreaPolygon;
                    currentAreaPolygon.Stroke.Color = Color.Red;
                }
            }
           */
        }

        void gMapControl1_OnPolygonLeave(GMapPolygon item)
        {
            /*
            if (item is GMapAreaPolygon)
            {
                GMapAreaPolygon areaPolygon = item as GMapAreaPolygon;
                if (currentAreaPolygon != null && currentAreaPolygon == areaPolygon)
                {
                    currentAreaPolygon = item as GMapAreaPolygon;
                    currentAreaPolygon.Stroke.Color = Color.Blue;
                }
            }
            */
        }

        void gMapControl1_OnPolygonDoubleClick(GMapPolygon item, MouseEventArgs e)
        {
            /*
            if (item is GMapAreaPolygon)
            {
                if (currentAreaPolygon != null)
                {
                    DownloadMap(currentAreaPolygon);
                }
                else
                {
                    MessageBox.Show("請先用畫圖工具畫下載的區域多邊形或選擇省市區域！");
                }
            }
            */
        }


        private void trackBar1_ValueChanged(object sender, EventArgs e)
        {
            gMapControl1.Zoom = trackBar1.Value;
            tb_zoom.Text = gMapControl1.Zoom.ToString();
            update_MapProvider_info();
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

            //竹北座標 義民中學 24.83907276107702, 121.00421169156141
            latitude = 24.839;   //緯度
            longitude = 121.004; //經度
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

                //在坐標點上繪制一綠色點并向圖層中添加標簽
                PointLatLng point = new PointLatLng(double.Parse(LatLng[0]), double.Parse(LatLng[1]));

                GMapMarker marker = new GMarkerGoogle(point, GMarkerGoogleType.green);

                gMapOverlay1.Markers.Add(marker);

                //richTextBox1.Text += (double.Parse(LatLng[0])).ToString() + "\t" + (double.Parse(LatLng[1])).ToString() + "\n";

                //方便之后尋找到是第幾個GMapMarker   
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

            //竹北座標 義民中學 24.83907276107702, 121.00421169156141
            latitude = 24.839;   //緯度
            longitude = 121.004; //經度

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
            GMapOverlay markersOverlay_stop = new GMapOverlay("Stop"); //放置marker的圖層
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

            GMapOverlay markers_polygon = new GMapOverlay("polygon"); //放置marker的圖層
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
            markersOverlay = new GMapOverlay("markersOverlay");

            GMapDrawCircle Circle = null;
            GMapDrawLine Line = null;
            GMapPolygon Polygon = null;
            GMapDrawRoute Route = null;
            GMapDrawRectangle myRectangle = null;

            //竹北座標 義民中學 24.83907276107702, 121.00421169156141
            latitude = 24.839;   //緯度
            longitude = 121.004; //經度
            Pen stroke = new Pen(Color.Red, 5);
            Brush fill = null;

            //畫圓
            //圓心
            PointLatLng center = new PointLatLng(latitude, longitude);

            //圓邊
            int edge_x_st = 480;
            int edge_y_st = 0;
            PointLatLng currentPos = gMapControl1.FromLocalToLatLng(edge_x_st, edge_y_st);
            //currentPos = new PointLatLng(latitude + 0.01, longitude + 0.01);

            //Circle = new GMapDrawCircle(center, currentPos);  //多載
            Circle = new GMapDrawCircle(center, currentPos, stroke, fill);  //多載, 使用畫筆色
            //                          圓心    圓邊
            markersOverlay.Markers.Add(Circle);

            //畫圓
            //圓心
            int cx = 100;
            int cy = 100;
            int r = 100;
            PointLatLng p1 = gMapControl1.FromLocalToLatLng(cx, cy);  //圓心
            PointLatLng p2 = gMapControl1.FromLocalToLatLng(cx, cx + r);      //圓邊
            Circle = new GMapDrawCircle(p1, p2, stroke, fill);  //多載, 使用畫筆色
            markersOverlay.Markers.Add(Circle);

            //畫線, 連線
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
            Line = new GMapDrawLine(points, "AAAAAAAA");
            markersOverlay.Routes.Add(Line);

            //畫多邊形
            latitude = 24.839;   //緯度
            longitude = 121.004; //經度

            double dd = 0.015;
            points = new List<PointLatLng>();
            points.Add(new PointLatLng(latitude + dd, longitude));
            points.Add(new PointLatLng(latitude, longitude + dd));
            points.Add(new PointLatLng(latitude - dd, longitude));
            points.Add(new PointLatLng(latitude, longitude - dd));
            Polygon = new GMapPolygon(points, "BBBB");
            markersOverlay.Polygons.Add(Polygon);

            //畫路線
            points = new List<PointLatLng>();
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

            Route = new GMapDrawRoute(points, "Route");
            markersOverlay.Routes.Add(Route);


            //畫長方形
            latitude = 24.839;   //緯度
            longitude = 121.004; //經度

            dd = 0.015;
            points = new List<PointLatLng>();
            points.Add(new PointLatLng(latitude + dd, longitude - dd));
            points.Add(new PointLatLng(latitude + dd, longitude + dd));
            points.Add(new PointLatLng(latitude - dd, longitude + dd));
            points.Add(new PointLatLng(latitude - dd, longitude - dd));
            myRectangle = new GMapDrawRectangle(points, "BBBB");
            markersOverlay.Polygons.Add(myRectangle);

            gMapControl1.Overlays.Add(markersOverlay);
            gMapControl1.Refresh();

            //寫字
            //在地圖上寫字, 寫在markersOverlay上
            latitude = 24.839;   //緯度
            longitude = 121.004; //經度
            PointLatLng position = new PointLatLng(latitude + 0.005, longitude - 0.005);
            GMapTextMarker textMarker = new GMapTextMarker(position, "竹北市中心");
            textMarker.TipFont = new Font("標楷體", 30);
            textMarker.TipBrush = new SolidBrush(Color.Blue);
            markersOverlay.Markers.Add(textMarker);
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

            //TBD

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

        void gMapControl1_MouseDown(object sender, MouseEventArgs e)
        {
            //richTextBox1.Text += "MouseDown\n";

            if (e.Button == MouseButtons.Right) //檢查滑鼠右鍵
            {
                pt1_tmp = gMapControl1.FromLocalToLatLng(e.X, e.Y);
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

                        //在地圖上寫字, 寫在markersOverlay上
                        PointLatLng point_middle = new PointLatLng((pt1.Lat + pt2.Lat) / 2, (pt1.Lng + pt2.Lng) / 2);
                        GMapTextMarker textMarker = new GMapTextMarker(point_middle, dist2);
                        textMarker.TipFont = new Font("標楷體", 20);
                        textMarker.TipBrush = new SolidBrush(Color.Navy);
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

        void gMapControl1_MouseMove(object sender, MouseEventArgs e)
        {
            //richTextBox1.Text += "MouseMove\n";
            PointLatLng point = gMapControl1.FromLocalToLatLng(e.X, e.Y);
        }

        void gMapControl1_MouseUp(object sender, MouseEventArgs e)
        {
        }

        void gMapControl1_OnMapZoomChanged()
        {
            //richTextBox1.Text += "OnMapZoomChanged\n";
            trackBar1.Value = (int)gMapControl1.Zoom;
            tb_zoom.Text = gMapControl1.Zoom.ToString();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            markersOverlay.Clear();
            polygonsOverlay.Clear();

            //量測距離
            flag_measure_first_point = false;
            total_distance = 0;
            line_point.Clear();
            draw_line_point();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //tmp
            gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖
            //竹北座標 義民中學 24.83907276107702, 121.00421169156141
            latitude = 24.839;   //緯度
            longitude = 121.004; //經度
            gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置
            gMapControl1.Zoom = 14; //當前比例

            update_controls_info();

            //畫方圓3公里

            double longitude_new = longitude;

            for (double dd = 0; dd < 0.04; dd += 0.002)
            {
                longitude_new = longitude + dd; //經度
                double distance = getDistance(new PointLatLng(latitude, longitude), new PointLatLng(latitude, longitude_new));
                //richTextBox1.Text += "方法一, 距離 : " + distance.ToString() + "\n";
                if (distance > 3)
                    break;
            }

            markersOverlay = new GMapOverlay("markersOverlay");

            GMapDrawCircle Circle = null;
            Pen stroke = new Pen(Color.Red, 5);
            Brush fill = null;

            //畫圓
            //圓心
            PointLatLng center = new PointLatLng(latitude, longitude);
            PointLatLng edge = new PointLatLng(latitude, longitude_new);

            //Circle = new GMapDrawCircle(center, edge);  //多載
            Circle = new GMapDrawCircle(center, edge, stroke, fill);  //多載, 使用畫筆色
            //                          圓心    圓邊
            markersOverlay.Markers.Add(Circle);

            gMapControl1.Overlays.Add(markersOverlay);

            //畫36平方公里, 6公里平方
            double longitude_west = 0;
            double longitude_east = 0;
            double latitude_north = 0;
            double latitude_south = 0;

            longitude_new = longitude;
            for (double dd = 0; dd < 0.04; dd += 0.0002)
            {
                longitude_new = longitude + dd; //經度
                double distance = getDistance(new PointLatLng(latitude, longitude), new PointLatLng(latitude, longitude_new));
                richTextBox1.Text += "右, 距離 : " + distance.ToString() + "\n";
                if (distance > 6 / 2)
                    break;
            }
            richTextBox1.Text += "取得右邊界 : " + longitude_new.ToString() + "\n";
            longitude_east = longitude_new;

            longitude_new = longitude;
            for (double dd = 0.04; dd > 0; dd -= 0.0002)
            {
                longitude_new = longitude - dd; //經度
                double distance = getDistance(new PointLatLng(latitude, longitude), new PointLatLng(latitude, longitude_new));
                richTextBox1.Text += "左, 距離 : " + distance.ToString() + "\n";
                if (distance < 6 / 2)
                    break;
            }
            richTextBox1.Text += "取得左邊界 : " + longitude_new.ToString() + "\n";
            longitude_west = longitude_new;


            //latitude
            double latitude_new = latitude;
            for (double dd = 0; dd < 0.04; dd += 0.0002)
            {
                latitude_new = latitude + dd; //緯度
                double distance = getDistance(new PointLatLng(latitude, longitude), new PointLatLng(latitude_new, longitude));
                richTextBox1.Text += "上, 距離 : " + distance.ToString() + "\n";
                if (distance > 6 / 2)
                    break;
            }
            richTextBox1.Text += "取得上邊界 : " + latitude_new.ToString() + "\n";
            latitude_north = latitude_new;

            latitude_new = latitude;
            for (double dd = 0.04; dd > 0; dd -= 0.0002)
            {
                latitude_new = latitude - dd; //緯度
                double distance = getDistance(new PointLatLng(latitude, longitude), new PointLatLng(latitude_new, longitude));
                richTextBox1.Text += "下, 距離 : " + distance.ToString() + "\n";
                if (distance < 6 / 2)
                    break;
            }
            richTextBox1.Text += "取得下邊界 : " + latitude_new.ToString() + "\n";
            latitude_south = latitude_new;

            GMapDrawRectangle myRectangle = null;

            List<PointLatLng> points = new List<PointLatLng>();
            points = new List<PointLatLng>();

            points.Add(new PointLatLng(latitude_north, longitude_west));    //左上
            points.Add(new PointLatLng(latitude_north, longitude_east));    //右上
            points.Add(new PointLatLng(latitude_south, longitude_east));    //右下
            points.Add(new PointLatLng(latitude_south, longitude_west));    //左下


            /*
            double ddd = 0.01;
            points.Add(new PointLatLng(latitude - ddd, longitude + ddd));    //左上
            points.Add(new PointLatLng(latitude + ddd, longitude + ddd));    //右上
            points.Add(new PointLatLng(latitude + ddd, longitude - ddd));    //右下
            points.Add(new PointLatLng(latitude - ddd, longitude - ddd));    //左下
            */

            myRectangle = new GMapDrawRectangle(points, "BBBB");
            markersOverlay.Polygons.Add(myRectangle);


            gMapControl1.Refresh();
        }



        private void button8_Click(object sender, EventArgs e)
        {
            //經緯度度分秒轉換
            //由X度Y分Z秒換成a.bcde度

            double lat_degrees = 0;
            double lat_minutes = 0;
            double lat_seconds = 0;
            double long_degrees = 0;
            double long_minutes = 0;
            double long_seconds = 0;

            //新竹火車站 24°48′7.38″N 120°58′18.54″E
            //新竹火車站 24.80205, 120.971817

            lat_degrees = 24;
            lat_minutes = 48;
            lat_seconds = 7.38;
            long_degrees = 120;
            long_minutes = 58;
            long_seconds = 18.54;

            double Latitude = lat_degrees + lat_minutes / 60 + lat_seconds / 3600;
            double Longitude = long_degrees + long_minutes / 60 + long_seconds / 3600;

            //小數點語法
            richTextBox1.Text += "北緯 : " + Latitude.ToString("0.0000") + "\t東經 : " + Longitude.ToString("0.0000") + "\n";


            //txtLatitudeFrom.Text = city.Latitude.ToString("0.0000");
            //txtLongitudeFrom.Text = city.Longitude.ToString("0.0000");

        }

        private void button9_Click(object sender, EventArgs e)
        {
            gMapControl1.ReloadMap();   //重新載入
            update_controls_info();

            //gMapControl1.Refresh();
            //gMapControl1.ShowTileGridLines = true;//顯示瓦片，也就是顯示方格
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


            richTextBox1.Text += "此時的地圖中心位置 :\t" + gMapControl1.Position.ToString() + "\n";
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
            else if (radioButton15.Checked == true)
            {
                gMapControl1.MapProvider = GMapProviders.GoogleChinaSatelliteMap; //中國衛星地圖
            }
            else if (radioButton16.Checked == true)
            {
                gMapControl1.MapProvider = GMapProviders.GoogleChinaTerrainMap; //中國地形地圖
            }
            else if (radioButton17.Checked == true)
            {
                //其他
                gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖
            }
            else
            {
                richTextBox1.Text += "XXXXX";

            }
        }

        //地圖切換
        private void radioButton_CheckedChanged2(object sender, EventArgs e)
        {
            if (rb_map00.Checked == true)
            {
                this.gMapControl1.MapProvider = GMapProviders.GoogleMap;
                richTextBox1.Text += "Google普通地圖\n";

            }
            else if (rb_map01.Checked == true)
            {
                this.gMapControl1.MapProvider = GMapProviders.GoogleSatelliteMap;
                richTextBox1.Text += "Google衛星地圖\n";

            }
            else if (rb_map02.Checked == true)
            {
                this.gMapControl1.MapProvider = GMapProviders.GoogleHybridMap;
                richTextBox1.Text += "Google混合地圖\n";

            }
            else if (rb_map03.Checked == true)
            {
                gMapControl1.MapProvider = GMapProviders.GoogleChinaMap;
                richTextBox1.Text += "Google中國普通地圖\n";

            }
            else if (rb_map04.Checked == true)
            {
                gMapControl1.MapProvider = GMapProviders.GoogleChinaSatelliteMap;
                richTextBox1.Text += "Google中國衛星地圖\n";

            }
            else if (rb_map05.Checked == true)
            {
                gMapControl1.MapProvider = GMapProviders.GoogleChinaHybridMap;
                richTextBox1.Text += "Google中國混合地圖\n";

            }
            else if (rb_map06.Checked == true)
            {
                this.gMapControl1.MapProvider = GMapProviders.GoogleChinaTerrainMap;
                richTextBox1.Text += "Google中國地形地圖\n";

            }
            else if (rb_map07.Checked == true)
            {
                //百度地圖 普通
                //this.gMapControl1.MapProvider = GMapProvidersExt.Baidu.BaiduMapProvider.Instance;
                richTextBox1.Text += "GMapProvidersExt.Baidu.BaiduMapProvider.Instance.CnName\n";

            }
            else if (rb_map08.Checked == true)
            {
                //百度地圖 衛星
                //this.gMapControl1.MapProvider = GMapProvidersExt.Baidu.BaiduSatelliteMapProvider.Instance;
                richTextBox1.Text += "GMapProvidersExt.Baidu.BaiduSatelliteMapProvider.Instance.CnName\n";

            }
            else if (rb_map09.Checked == true)
            {
                //百度地圖 混合
                //this.gMapControl1.MapProvider = GMapProvidersExt.Baidu.BaiduHybridMapProvider.Instance;
                richTextBox1.Text += "GMapProvidersExt.Baidu.BaiduHybridMapProvider.Instance.CnName\n";

            }
            else if (rb_map10.Checked == true)
            {
                //高德地圖 普通地圖
                //this.gMapControl1.MapProvider = GMapProvidersExt.AMap.AMapProvider.Instance;
                richTextBox1.Text += "GMapProvidersExt.AMap.AMapProvider.Instance.CnName\n";

            }
            else if (rb_map11.Checked == true)
            {
                //高德地圖 衛星地圖
                //this.gMapControl1.MapProvider = GMapProvidersExt.AMap.AMapSateliteProvider.Instance;
                richTextBox1.Text += "GMapProvidersExt.AMap.AMapSateliteProvider.Instance.CnName\n";

            }
            else if (rb_map12.Checked == true)
            {
                //高德地圖 混合地圖
                //this.gMapControl1.MapProvider = GMapProvidersExt.AMap.AMapHybirdProvider.Instance;
                richTextBox1.Text += "GMapProvidersExt.AMap.AMapHybirdProvider.Instance.CnName\n";

            }
            else if (rb_map13.Checked == true)
            {
                //騰迅地圖 普通地圖
                //this.gMapControl1.MapProvider = GMapProvidersExt.Tencent.TencentMapProvider.Instance;
                //this.mapControl.MapProvider = GMapProvidersExt.SoSo.SosoMapProvider.Instance;
                richTextBox1.Text += "GMapProvidersExt.Tencent.TencentMapProvider.Instance.CnName\n";

            }
            else if (rb_map14.Checked == true)
            {
                //騰迅地圖 衛星地圖
                //this.gMapControl1.MapProvider = GMapProvidersExt.Tencent.TencentMapSateliteProvider.Instance;
                //this.mapControl.MapProvider = GMapProvidersExt.SoSo.SosoMapSateliteProvider.Instance;
                richTextBox1.Text += "GMapProvidersExt.Tencent.TencentMapSateliteProvider.Instance.CnName\n";

            }
            else if (rb_map15.Checked == true)
            {
                //騰迅地圖 混合地圖
                //this.gMapControl1.MapProvider = GMapProvidersExt.Tencent.TencentMapHybridProvider.Instance;
                //this.mapControl.MapProvider = GMapProvidersExt.SoSo.SosoMapHybridProvider.Instance;
                richTextBox1.Text += "GMapProvidersExt.Tencent.TencentMapHybridProvider.Instance.CnName\n";

            }
            else if (rb_map16.Checked == true)
            {
                //騰迅地圖 地形地圖
                //this.gMapControl1.MapProvider = TencentTerrainMapAnnoProvider.Instance;
                richTextBox1.Text += "GMapProvidersExt.Tencent.TencentTerrainMapAnnoProvider.Instance.CnName\n";

            }
            else if (rb_map17.Checked == true)
            {
                //Here地圖 普通地圖
                //gMapControl1.MapProvider = GMapProvidersExt.Here.NokiaMapProvider.Instance;
                richTextBox1.Text += "GMapProvidersExt.Here.NokiaMapProvider.Instance.CnName\n";

            }
            else if (rb_map18.Checked == true)
            {
                //Here地圖 衛星地圖
                //gMapControl1.MapProvider = GMapProvidersExt.Here.NokiaSatelliteMapProvider.Instance;
                richTextBox1.Text += "GMapProvidersExt.Here.NokiaSatelliteMapProvider.Instance.CnName\n";

            }
            else if (rb_map19.Checked == true)
            {
                //Here地圖 混合地圖
                //gMapControl1.MapProvider = GMapProvidersExt.Here.NokiaHybridMapProvider.Instance;
                richTextBox1.Text += "GMapProvidersExt.Here.NokiaHybridMapProvider.Instance.CnName\n";

            }
            else if (rb_map20.Checked == true)
            {
                //Bing地圖 普通地圖
                this.gMapControl1.MapProvider = GMapProviders.BingMap;
                richTextBox1.Text += "Bing普通地圖\n";

            }
            else if (rb_map21.Checked == true)
            {
                //Bing地圖 衛星地圖
                this.gMapControl1.MapProvider = GMapProviders.BingSatelliteMap;
                richTextBox1.Text += "Bing衛星地圖\n";

            }
            else if (rb_map22.Checked == true)
            {
                //Bing地圖 混合地圖
                this.gMapControl1.MapProvider = GMapProviders.BingHybridMap;
                richTextBox1.Text += "Bing混合地圖\n";

            }
            else if (rb_map23.Checked == true)
            {
                //Bing地圖 普通地圖中文
                //this.gMapControl1.MapProvider = GMapProvidersExt.Bing.BingChinaMapProvider.Instance;
                richTextBox1.Text += "GMapProvidersExt.Bing.BingChinaMapProvider.Instance.CnName\n";

            }
            else if (rb_map24.Checked == true)
            {
                //天地圖 街道地圖(球面墨卡托)
                //this.gMapControl1.MapProvider = GMapProvidersExt.TianDitu.TiandituMapProviderWithAnno.Instance;
                richTextBox1.Text += "GMapProvidersExt.TianDitu.TiandituMapProviderWithAnno.Instance.CnName\n";

            }
            else if (rb_map25.Checked == true)
            {
                //天地圖 衛星地圖(球面墨卡托)
                //this.gMapControl1.MapProvider = GMapProvidersExt.TianDitu.TiandituSatelliteMapProvider.Instance;
                richTextBox1.Text += "GMapProvidersExt.TianDitu.TiandituSatelliteMapProvider.Instance.CnName\n";

            }
            else if (rb_map26.Checked == true)
            {
                //天地圖 混合地圖(球面墨卡托)
                //this.gMapControl1.MapProvider = GMapProvidersExt.TianDitu.TiandituSatelliteMapProviderWithAnno.Instance;
                richTextBox1.Text += "GMapProvidersExt.TianDitu.TiandituSatelliteMapProviderWithAnno.Instance.CnName\n";

            }
            else if (rb_map27.Checked == true)
            {
                //天地圖 街道地圖(WGS84)
                //this.gMapControl1.MapProvider = GMapProvidersExt.TianDitu.TiandituMapProviderWithAnno4326.Instance;
                richTextBox1.Text += "GMapProvidersExt.TianDitu.TiandituMapProviderWithAnno4326.Instance.CnName\n";

            }
            else if (rb_map28.Checked == true)
            {
                //天地圖 衛星地圖(WGS84)
                //this.gMapControl1.MapProvider = GMapProvidersExt.TianDitu.TiandituSatelliteMapProvider4326.Instance;
                richTextBox1.Text += "GMapProvidersExt.TianDitu.TiandituSatelliteMapProvider4326.Instance.CnName\n";

            }
            else if (rb_map29.Checked == true)
            {
                //天地圖 混合地圖(WGS84)
                //this.gMapControl1.MapProvider = GMapProvidersExt.TianDitu.TiandituSatelliteMapProviderWithAnno4326.Instance;
                richTextBox1.Text += "GMapProvidersExt.TianDitu.TiandituSatelliteMapProviderWithAnno4326.Instance.CnName\n";

            }
            else if (rb_map30.Checked == true)
            {
                //天地圖 福建街道地圖
                //this.gMapControl1.MapProvider = GMapProvidersExt.TianDitu.Fujian.TiandituFujianMapProviderWithAnno.Instance;
                richTextBox1.Text += "GMapProvidersExt.TianDitu.Fujian.TiandituFujianMapProviderWithAnno.Instance.CnName\n";
                this.gMapControl1.Position = new PointLatLng(26.0651, 119.2786);

            }
            else if (rb_map31.Checked == true)
            {

                //天地圖 福建衛星地圖
                //this.gMapControl1.MapProvider = GMapProvidersExt.TianDitu.Fujian.TiandituFujianSatelliteMapProvider.Instance;
                richTextBox1.Text += "GMapProvidersExt.TianDitu.Fujian.TiandituFujianSatelliteMapProvider.Instance.CnName\n";
                this.gMapControl1.Position = new PointLatLng(26.0651, 119.2786);
            }
            else if (rb_map32.Checked == true)
            {
                //天地圖 福建混合地圖
                //this.gMapControl1.MapProvider = GMapProvidersExt.TianDitu.Fujian.TiandituFujianSatelliteMapProviderWithAnno.Instance;
                richTextBox1.Text += "GMapProvidersExt.TianDitu.Fujian.TiandituFujianSatelliteMapProviderWithAnno.Instance.CnName\n";
                this.gMapControl1.Position = new PointLatLng(26.0651, 119.2786);
            }
            else if (rb_map33.Checked == true)
            {
                //ArcGIS地圖 arcGIS街道地圖
                //this.gMapControl1.MapProvider = GMapProvidersExt.ArcGIS.ArcGISMapProvider.Instance;
                richTextBox1.Text += "GMapProvidersExt.ArcGIS.ArcGISMapProvider.Instance.CnName\n";
            }
            else if (rb_map34.Checked == true)
            {
                //ArcGIS地圖 arcGIS街道地圖(無POI)
                //this.gMapControl1.MapProvider = GMapProvidersExt.ArcGIS.ArcGISMapProviderNoPoi.Instance;
                richTextBox1.Text += "GMapProvidersExt.ArcGIS.ArcGISMapProviderNoPoi.Instance.CnName\n";
            }
            else if (rb_map35.Checked == true)
            {
                //ArcGIS地圖 arcGIS街道地圖(冷色版)
                //this.gMapControl1.MapProvider = GMapProvidersExt.ArcGIS.ArcGISColdMapProvider.Instance;
                richTextBox1.Text += "GMapProvidersExt.ArcGIS.ArcGISColdMapProvider.Instance.CnName\n";
            }
            else if (rb_map36.Checked == true)
            {
                //ArcGIS地圖 arcGIS街道地圖(灰色版)
                //this.gMapControl1.MapProvider = GMapProvidersExt.ArcGIS.ArcGISGrayMapProvider.Instance;
                richTextBox1.Text += "GMapProvidersExt.ArcGIS.ArcGISGrayMapProvider.Instance.CnName\n";
            }
            else if (rb_map37.Checked == true)
            {
                //ArcGIS地圖 arcGIS街道地圖(暖色版)
                //this.gMapControl1.MapProvider = GMapProvidersExt.ArcGIS.ArcGISWarmMapProvider.Instance;
                richTextBox1.Text += "GMapProvidersExt.ArcGIS.ArcGISWarmMapProvider.Instance.CnName\n";
            }
            else if (rb_map38.Checked == true)
            {
                //ArcGIS地圖 arcGIS衛星地圖(無偏移)
                //this.gMapControl1.MapProvider = GMapProvidersExt.ArcGIS.ArcGISSatelliteMapProvider.Instance;
                richTextBox1.Text += "GMapProvidersExt.ArcGIS.ArcGISSatelliteMapProvider.Instance.CnName\n";
            }
            else if (rb_map39.Checked == true)
            {
                //搜狗地圖 普通地圖
                //this.gMapControl1.MapProvider = GMapProvidersExt.Sogou.SogouMapProvider.Instance;
                richTextBox1.Text += "GMapProvidersExt.Sogou.SogouMapProvider.Instance.CnName\n";
            }
            else if (rb_map40.Checked == true)
            {
                //船舶地圖 船舶
                //this.gMapControl1.MapProvider = GMapProvidersExt.Ship.ShipMapProvider.Instance;
                richTextBox1.Text += "GMapProvidersExt.Ship.ShipMapProvider.Instance.CnName\n";
            }
            else if (rb_map41.Checked == true)
            {

            }
            else
            {
                richTextBox1.Text += "XXXXX";
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
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_icon\face1.png";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            marker = new GMarkerGoogle(point, bitmap1);
            //直接寫
            //GMapMarker marker2 = new GMarkerGoogle(point, new Bitmap(filename));

            setup_marker_tooltip(marker, "12345");  //設置marker訊息

            markersOverlay.Markers.Add(marker);
        }

        private void button12_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "計算兩點之間的距離\n";

            //義民中學 24.83907276107702, 121.00421169156141
            double latitude1 = 24.839;   //緯度
            double longitude1 = 121.004; //經度

            //竹北大遠百 24.822075898681902, 121.02319618273027
            double latitude2 = 24.822075898681902;   //緯度
            double longitude2 = 121.02319618273027; //經度


            //方法一
            double distance1 = getDistance(new PointLatLng(latitude1, longitude1), new PointLatLng(latitude2, longitude2));
            richTextBox1.Text += "方法一, 距離 : " + distance1.ToString() + "\n";


            //方法二
            double distance2 = getDistance2(latitude1, longitude1, latitude2, longitude2);
            richTextBox1.Text += "方法二, 距離 : " + distance2.ToString() + "\n";
        }

        //計算地圖上兩點之間的距離--擴展功能
        private const double EARTH_RADIUS = 6378.137;//地球半徑
        private static double radius(double d)
        {
            return d * Math.PI / 180.0;
        }

        public double getDistance2(double lat1, double lng1, double lat2, double lng2)
        {
            double radLat1 = radius(lat1);
            double radLat2 = radius(lat2);
            double a = radLat1 - radLat2;
            double b = radius(lng1) - radius(lng2);

            double s = 2 * Math.Asin(Math.Sqrt(Math.Pow(Math.Sin(a / 2), 2) +
             Math.Cos(radLat1) * Math.Cos(radLat2) * Math.Pow(Math.Sin(b / 2), 2)));
            s = s * EARTH_RADIUS;
            s = Math.Round(s * 10000) / 10000;
            return s;
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
            //地圖存圖
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

        private void button15_Click(object sender, EventArgs e)
        {
            gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖
            //竹北座標 義民中學 24.83907276107702, 121.00421169156141
            latitude = 24.839;   //緯度
            longitude = 121.004; //經度
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
            //創建“lay”圖層
            GMapOverlay lay = new GMapOverlay("lay");
            //創建一條route
            GMapRoute route1 = new GMapRoute("route1");
            //設置route的顏色和粗細
            route1.Stroke = new Pen(Color.Red, 2);  //連線顏色與大小
            //向route中添加點
            int i;
            for (i = 0; i < len; i++)
            {
                route1.Points.Add(new PointLatLng(points[i].Lat, points[i].Lng));
            }
            //將route添加到圖層
            lay.Routes.Add(route1);
            //將圖層添加到地圖
            gMapControl1.Overlays.Add(lay);

            //更新顯示route
            gMapControl1.UpdateRouteLocalPosition(route1);
        }

        private void btn_draw_profile_Click(object sender, EventArgs e)
        {
            string location = comboBox1.Text;
            richTextBox1.Text += "location = " + location + "\n";

            if (location == "甘肅")
            {
                richTextBox1.Text += "無 甘肅 資料";
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

            if (location == "甘肅")
            {
                richTextBox1.Text += "無 甘肅 資料";
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

                //竹北座標 義民中學 24.83907276107702, 121.00421169156141
                latitude = 24.839;   //緯度
                longitude = 121.004; //經度
                gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置
                gMapControl1.Zoom = 14; //當前比例

                update_controls_info();
            }
            else if (rb_location1.Checked == true)
            {
                string[,] location = null;

                location = new string[,] {
            { "臺北", "25.047778", "121.517222"},
            { "新竹", "24.80205", "120.971817"},
            { "臺中", "24.136944", "120.684722"},
            { "臺南", "23.001389", "120.2175"},
            { "高雄", "22.64", "120.302778"},
            { "臺東", "22.791389", "121.118889"},
            { "花蓮", "23.992694", "121.600861"},
            { "宜蘭", "24.750278", "121.7625"},
            };

                int total_location = location.GetUpperBound(0) + 1;
                richTextBox1.Text += "total_location = " + total_location.ToString() + "\n";

                gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖

                latitude = double.Parse(location[0, 1]);
                longitude = double.Parse(location[0, 2]);

                gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置
                gMapControl1.Zoom = 10; //當前比例

                update_controls_info();

                int i;
                for (i = 0; i < total_location; i++)
                {
                    latitude = double.Parse(location[i, 1]);
                    longitude = double.Parse(location[i, 2]);

                    //AddMarker(latitude, longitude, GMarkerGoogleType.blue_dot, location[i, 0]);
                    draw_circle_text(latitude, longitude, location[i, 0]);
                }

                richTextBox1.Text += "畫範圍 GMapPolygon 1\n";
                List<PointLatLng> points = new List<PointLatLng>();

                for (i = 0; i < total_location; i++)
                {
                    latitude = double.Parse(location[i, 1]);
                    longitude = double.Parse(location[i, 2]);

                    points.Add(new PointLatLng(latitude, longitude));
                }
                GMapPolygon polygon = new GMapPolygon(points, "mypolygon");
                polygon.Fill = new SolidBrush(Color.FromArgb(50, Color.Red));   //有填滿 半透明, 若不寫.Fill, 即無填滿
                polygon.Stroke = new Pen(Color.Red, 1); //邊框顏色與大小

                GMapOverlay markers_polygon = new GMapOverlay("polygon"); //放置marker的圖層
                markers_polygon.Polygons.Add(polygon);
                gMapControl1.Overlays.Add(markers_polygon);  //添加 圖標 Markers 的圖層

                richTextBox1.Text += "畫範圍 GMapPolygon 2\n";
                //List<PointLatLng> points = new List<PointLatLng>();
                points.Clear();
                for (i = 0; i < total_location; i++)
                {
                    latitude = double.Parse(location[i, 1]);
                    longitude = double.Parse(location[i, 2]);

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

                for (i = 0; i < (total_location - 1); i++)
                {
                    latitude = double.Parse(location[i, 1]);
                    longitude = double.Parse(location[i, 2]);

                    pt1 = new PointLatLng(double.Parse(location[i, 1]), double.Parse(location[i, 2]));
                    pt2 = new PointLatLng(double.Parse(location[i + 1, 1]), double.Parse(location[i + 1, 2]));
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
                    richTextBox1.Text += location[i, 0] + " 到 " + location[i + 1, 0] + " 直線距離 : " + dist + "\n";
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
                //gMapControl1.Zoom = 15; //當前比例

                string[,] location = null;

                location = new string[,] {
            { "圓明園", "40.007222", "116.2925"},
            { "中華書局", "39.88244693415653", "116.31404671396393"},
            };
                show_locations(location);
                gMapControl1.Zoom = 12; //當前比例

                update_controls_info();
            }
            else if (rb_location3.Checked == true)
            {

            }
            else if (rb_location4.Checked == true)
            {
                //烏克蘭 俄羅斯
                string[,] location = null;

                location = new string[,] {
            { "基輔", "50.4513678157106", "30.55059860621383"},
            { "賽瓦斯托波爾", "44.60672245398692", "33.52507514600167"},
            { "雅爾達", "44.49163293411768", "34.154514168194616"},
            { "伏爾加格勒(史達林格勒)", "48.71041949593781", "44.51688003466866"},
            { "莫斯科", "55.75541452385479", "37.61935290354823"},
            { "聖彼得堡(列寧格勒)", "59.9250247131024", "30.332144315364747"},
            { "馬立波", "47.095833", "37.549444"},
            { "車諾比核電廠", "51.389167", "30.099444"},
            { "蛇島", "45.255", "30.204167"},
            };
                show_locations(location);
                gMapControl1.Zoom = 5; //當前比例
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
                gMapControl1.MapProvider = GMapProviders.GoogleChinaMap; //簡中地圖

                //北京中華書局
                //北京市豐臺區太平橋西里38號
                //39.88244693415653, 116.31404671396393
                latitude = 39.88244693415653;   //緯度
                longitude = 116.31404671396393; //經度
                gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置
                gMapControl1.Zoom = 12; //當前比例

                update_controls_info();

            }
            else if (rb_location7.Checked == true)
            {
                //阿拉曼

                string[,] location = null;

                location = new string[,] {
            { "阿拉曼", "30.833333", "28.95"},
            { "羅塞塔", "31.4014", "30.4194"},
            { "亞歷山卓", "31.1975", "29.8925"},
            };
                show_locations(location);
                gMapControl1.Zoom = 7; //當前比例

            }
            else if (rb_location8.Checked == true)
            {
                //國共
                string[,] location = null;

                location = new string[,] {
            { "徐州", "34.205", "117.283"},
            { "蚌埠", "32.917625", "117.382417"},
            { "海州", "34.597", "119.222"},
            { "新安鎮", "34.36775", "118.34638"},
            { "碾莊", "34.29887", "117.77576"},
            { "宿縣", "33.64242", "116.9721"},
            { "雙堆集", "33.42498", "116.89588"},
            { "臺兒莊", "34.5608", "117.7382"},
            { "運河鎮", "34.30807", "117.96176"},
            { "陳官莊", "34.00683", "116.57751"},
            { "西柏坡", "38.31762", "114.01269"},
            { "延安", "36.5855", "109.4897"},
            { "西安", "34.261111", "108.9425"},
            { "錦州", "41.0957", "121.1264"},
            { "四平", "43.166", "124.35"},
            { "長春", "43.884581", "125.318431"},
            { "瀋陽", "41.795556", "123.448056"},
            { "孟良崮", "35.54516", "118.15811"},
            { "濟南", "36.633333", "117.016667"},
            { "秦皇島", "39.936", "119.6"},

            };
                show_locations(location);
                gMapControl1.Zoom = 6; //當前比例

            }
            else if (rb_location9.Checked == true)
            {
                richTextBox1.Text += "盧溝橋\n";

                gMapControl1.MapProvider = GMapProviders.GoogleChinaMap; //簡中地圖

                //盧溝橋
                latitude = 39.85025;    //緯度
                longitude = 116.219066; //經度
                gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置
                gMapControl1.Zoom = 11; //當前比例

                update_controls_info();

                draw_circle_text(latitude, longitude, "盧溝橋");

                //中日戰爭
                string[,] location = null;

                location = new string[,] {
                { "棗陽", "32.12874", "112.7581"},
                { "宜昌市", "30.704444", "111.288611"},
                { "襄陽市", "32.009", "112.123"},
                { "長沙", "28.196111", "112.972222"},
                { "台兒莊", "34.5608", "117.7382"},
                { "武漢", "30.583333", "114.316667"},
                { "衡陽", "26.893", "112.572"},
                { "南京", "32.05", "118.766667"},
                { "上海", "31.17", "121.47"},
                { "延安", "36.5855", "109.4897"},
                { "西安", "34.261111", "108.9425"},
                { "重慶", "29.55", "106.5069"},
                };
                show_locations(location);
                gMapControl1.Zoom = 6; //當前比例
            }
            else if (rb_location10.Checked == true)
            {
                //烏龍派出所
                //勝鬨橋
                //勝鬨橋35.661944, 139.775
                //白鬚橋
                //東経 	139.0+48.0/60+45.6/3600
                //北緯 	35.0+43.0/60+29.4/3600

                //somewhere
                //35.72483333 139.81266667

                //警視庁	35.677028, 139.752306 


                richTextBox1.Text += "烏龍派出所\n";

                gMapControl1.MapProvider = GMapProviders.GoogleChinaMap; //簡中地圖

                //勝鬨橋35.661944, 139.775
                latitude = 35.661944;   //緯度
                longitude = 139.775;    //經度
                gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置
                gMapControl1.Zoom = 14; //當前比例

                update_controls_info();

            }
            else if (rb_location11.Checked == true)
            {
                //三國地圖

                string[,] location = null;

                location = new string[,] {
            { "街亭", "34.99874", "105.9806"},
            { "五丈原", "34.44482", "107.62093"},
            };
                show_locations(location);
                gMapControl1.Zoom = 7; //當前比例
            }
            else if (rb_location12.Checked == true)
            {
                //大清地圖
                string[,] location = null;

                location = new string[,] {
{ "北京", "39.905556", "116.391389"},
{ "盛京", "41.795556", "123.448056"},
{ "寧古塔", "44.416815360491", "129.1617512724705"},	//黑龍江省牡丹江市海林市長汀鎮古城村
{ "五國城", "46.333333", "129.566667"},
{ "皮島", "39.55684765902427", "124.65626476139558"},
{ "薩爾滸", "41.897516334666754", "124.2727564312876"},
{ "錦州", "41.11652825274596", "121.12778002674251"},
{ "承德避暑山莊", "40.99498842603812", "117.9344426275432"},
{ "揚州", "32.39351078912071", "119.43441495124323"},
{ "西安", "34.27346577864542", "108.93530578323285"},
{ "杭州", "30.16", "120.12"},
{ "長春", "43.884581", "125.318431"},
{ "嘉興", "30.754", "120.759"},
{ "蘭州", "36.061", "103.832"},
{ "揚州", "32.393", "119.415"},
{ "清東陵", "40.19", "117.965"},
{ "清西陵", "39.34991", "115.49596"},
{ "尼布楚", "51.983333", "116.583333"},
{ "西寧", "36.6169", "101.7781"},
{ "璦琿", "50.245", "127.528"},
            };

                show_locations(location);
                gMapControl1.Zoom = 5; //當前比例
            }
            else if (rb_location13.Checked == true)
            {
                //太平洋戰爭
                string[,] location = null;

                location = new string[,] {
{ "拉包爾", "-4.1981", "152.1681"},
{ "布因", "-6.746", "155.685"},
{ "瓜達爾卡納爾島", "-9.616667", "160.183333"},
{ "馬里亞納群島", "16.794022", "145.931389"},
{ "關島", "13.45", "144.783333"},
{ "塞班島", "15.209325", "145.763169"},
{ "天寧島", "15.00", "145.633333"},
            };

                show_locations(location);
                gMapControl1.Zoom = 5; //當前比例

            }
            else if (rb_location14.Checked == true)
            {
                //西藏
                string[,] location = null;

                location = new string[,] {
{ "布達拉宮", "29.657778", "91.116944"},
{ "扎什倫布寺", "29.268569", "88.8698"},
{ "達蘭薩拉", "32.2153", "76.3186"},
{ "昌都", "31.13749", "97.17767"},
{ "汶川", "31.483789", "103.588403"},
            };

                show_locations(location);
                gMapControl1.Zoom = 5; //當前比例

            }
            else if (rb_location15.Checked == true)
            {
                //印度
                string[,] location = null;

                location = new string[,] {
{ "新德里", "28.613895", "77.209006"},
{ "邦加羅爾", "12.97912", "77.5913"},
{ "孟買", "19.0758", "72.8775"},
{ "泰姬瑪哈陵", "27.1751", "78.0422"},
{ "瓦拉納西", "25.3189", "83.0128"},
{ "迦毘羅衛城", "27.5739916", "83.0520061"},
{ "達蘭薩拉", "32.2153", "76.3186"},
{ "阿薩姆", "26.00292287", "93.00745948"},
{ "哈里亞納邦", "29.193657", "76.324586"},
            };

                show_locations(location);
                gMapControl1.Zoom = 5; //當前比例

            }
            else if (rb_location16.Checked == true)
            {
                //金庸
                string[,] location = null;

                location = new string[,] {
{ "風陵渡", "34.6314", "110.30895"},
{ "黑木崖", "38.31762", "114.01269"},
            };

                show_locations(location);
                gMapControl1.Zoom = 5; //當前比例

            }
            else if (rb_location17.Checked == true)
            {
                //古都

                string[,] location = null;

                location = new string[,] {
{ "西安", "34.261111", "108.9425"},
{ "咸陽", "34.3296", "108.7091"},
{ "洛陽", "34.6195", "112.4543"},
{ "開封", "34.7975", "114.3079"},
{ "成都", "30.66", "104.0633"},
{ "南京", "32.05", "118.766667"},
{ "北京", "39.90403", "116.40753"},
{ "杭州", "30.16", "120.12"},
{ "瀋陽", "41.795556", "123.448056"},
{ "長春", "43.884581", "125.318431"},
};

                show_locations(location);
                gMapControl1.Zoom = 6; //當前比例

            }
            else if (rb_location18.Checked == true)
            {
                //西藏
                string[,] location = null;

                location = new string[,] {
{ "布達拉宮", "29.657778", "91.116944"},
{ "扎什倫布寺", "29.268569", "88.8698"},
{ "達蘭薩拉", "32.2153", "76.3186"},
{ "昌都", "31.13749", "97.17767"},
{ "汶川", "31.483789", "103.588403"},
            };

                show_locations(location);
                gMapControl1.Zoom = 5; //當前比例

            }
            else if (rb_location19.Checked == true)
            {
                //西藏
                string[,] location = null;

                location = new string[,] {
{ "布達拉宮", "29.657778", "91.116944"},
{ "扎什倫布寺", "29.268569", "88.8698"},
{ "達蘭薩拉", "32.2153", "76.3186"},
{ "昌都", "31.13749", "97.17767"},
{ "汶川", "31.483789", "103.588403"},
            };

                show_locations(location);
                gMapControl1.Zoom = 5; //當前比例

            }
            else
            {

            }
        }

        void draw_circle_text(double latitude, double longitude, string text)
        {
            markersOverlay = new GMapOverlay("markersOverlay");

            GMapDrawCircle Circle = null;
            Pen stroke = new Pen(Color.Red, 5);
            Brush fill = null;

            //畫圓
            PointLatLng center = new PointLatLng(latitude, longitude);
            int r = 30;

            GPoint gp = gMapControl1.FromLatLngToLocal(center); // markersOverlay.Control.FromLatLngToLocal(center);
            //richTextBox1.Text += "地理座標" + center.Lat.ToString() + "\t" + center.Lng.ToString() + "\t控件座標(" + gp.X.ToString() + ", " + gp.Y.ToString() + ")\n";

            PointLatLng p1 = gMapControl1.FromLocalToLatLng((int)gp.X, (int)gp.Y);      //圓心
            PointLatLng p2 = gMapControl1.FromLocalToLatLng((int)gp.X, (int)gp.Y + r);  //圓邊
            Circle = new GMapDrawCircle(p1, p2, stroke, fill);  //多載, 使用畫筆色
            //                        圓心    圓邊
            markersOverlay.Markers.Add(Circle);

            gMapControl1.Overlays.Add(markersOverlay);
            gMapControl1.Refresh();

            //寫字
            //在地圖上寫字, 寫在markersOverlay上
            PointLatLng position = new PointLatLng(latitude, longitude);
            GMapTextMarker textMarker = new GMapTextMarker(position, text);
            textMarker.TipFont = new Font("標楷體", 20);
            textMarker.TipBrush = new SolidBrush(Color.Blue);
            markersOverlay.Markers.Add(textMarker);

            GMapDrawLine Line = null;

            List<PointLatLng> points = new List<PointLatLng>();
            points.Add(new PointLatLng(latitude - 0.05, longitude));
            points.Add(new PointLatLng(latitude + 0.05, longitude));
            Line = new GMapDrawLine(points, "");
            markersOverlay.Routes.Add(Line);

            points.Clear();
            points.Add(new PointLatLng(latitude, longitude - 0.05));
            points.Add(new PointLatLng(latitude, longitude + 0.05));
            Line = new GMapDrawLine(points, "");
            markersOverlay.Routes.Add(Line);
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

            pt1 = pt1_tmp;
            if ((flag_measure_distance == 1) || (flag_measure_distance == 2))  //0 : 無量測, 1 : 量測距離 單程, 2 : 量測距離 連續
            {
                line_point.Add(pt1);
                draw_line_point();
                if (flag_measure_first_point == false)
                {
                    flag_measure_first_point = true;
                }
            }
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

            pt1 = pt1_tmp;
            if ((flag_measure_distance == 1) || (flag_measure_distance == 2))  //0 : 無量測, 1 : 量測距離 單程, 2 : 量測距離 連續
            {
                line_point.Add(pt1);
                draw_line_point();
                if (flag_measure_first_point == false)
                {
                    flag_measure_first_point = true;
                }
            }
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

        private void toolStripMenuItem8_Click(object sender, EventArgs e)
        {
            //地圖存圖
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
                //this.WindowState = FormWindowState.Normal;
                gMapControl1.Dock = DockStyle.None;

                int x_st = 10;
                int y_st = 10;

                gMapControl1.Size = new Size(1130, 1060);
                gMapControl1.Location = new Point(x_st, y_st);

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
                x_st = 1370;
                y_st = 12;
                int dy = 25;
                lb_distance.Location = new Point(x_st + 90, y_st + dy * 2);
            }
        }

        private void selectMapProvider(object sender, EventArgs e)
        {
            //richTextBox1.Text += "你選擇了 : " + ((ToolStripMenuItem)sender).Name + "\n";
            if (((ToolStripMenuItem)sender).Name == "selectMapProvider1")
            {
                gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖
            }
            else if (((ToolStripMenuItem)sender).Name == "selectMapProvider2")
            {
                gMapControl1.MapProvider = GMapProviders.GoogleChinaMap; //簡中地圖
            }
            else if (((ToolStripMenuItem)sender).Name == "selectMapProvider3")
            {
                gMapControl1.MapProvider = GMapProviders.GoogleTerrainMap; //地形圖
            }
            else if (((ToolStripMenuItem)sender).Name == "selectMapProvider4")
            {
                gMapControl1.MapProvider = GMapProviders.GoogleSatelliteMap;    //衛星地圖
            }
            else if (((ToolStripMenuItem)sender).Name == "selectMapProvider5")
            {
                gMapControl1.MapProvider = GMapProviders.GoogleChinaHybridMap;  //混合地圖
            }
            else if (((ToolStripMenuItem)sender).Name == "selectMapProvider6")
            {
                gMapControl1.MapProvider = OpenCycleMapProvider.Instance; //腳踏車專用地圖
            }
            else
            {
                gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖
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
            richTextBox1.Text += "座標轉換\n";
            //從地圖上的滑鼠座標畫標記
            int x_st;
            int y_st;
            PointLatLng point;

            x_st = 100;
            y_st = 100;
            point = gMapControl1.FromLocalToLatLng(x_st, y_st);
            richTextBox1.Text += "控件座標(" + x_st.ToString() + ", " + y_st.ToString() + ")\t地理座標" + point.Lat.ToString() + "\t" + point.Lng.ToString() + "\n";

            x_st = 200;
            y_st = 200;
            point = gMapControl1.FromLocalToLatLng(x_st, y_st);
            richTextBox1.Text += "控件座標(" + x_st.ToString() + ", " + y_st.ToString() + ")\t地理座標" + point.Lat.ToString() + "\t" + point.Lng.ToString() + "\n";

            x_st = 300;
            y_st = 300;
            point = gMapControl1.FromLocalToLatLng(x_st, y_st);
            richTextBox1.Text += "控件座標(" + x_st.ToString() + ", " + y_st.ToString() + ")\t地理座標" + point.Lat.ToString() + "\t" + point.Lng.ToString() + "\n";


            //竹北座標 義民中學 24.83907276107702, 121.00421169156141
            latitude = 24.839;   //緯度
            longitude = 121.004; //經度

            point = new PointLatLng(latitude, longitude);
            GPoint gp = this.markersOverlay.Control.FromLatLngToLocal(point);
            richTextBox1.Text += "地理座標" + point.Lat.ToString() + "\t" + point.Lng.ToString() + "\t控件座標(" + gp.X.ToString() + ", " + gp.Y.ToString() + ")\n";


        }

        /// <summary>
        /// gets position using geocoder
        /// </summary>
        /// <param name="keys"></param>
        /// <returns></returns>
        public PointLatLng GetPositionByKeywords(string keys)
        {
            GeoCoderStatusCode status = GeoCoderStatusCode.Unknow;

            GeocodingProvider gp = gMapControl1.MapProvider as GeocodingProvider;
            if (gp == null)
            {
                gp = GMapProviders.OpenStreetMap as GeocodingProvider;
                richTextBox1.Text += "1111";
            }

            if (gp != null)
            {
                richTextBox1.Text += "2222";
                var pt = gp.GetPoint(keys, out status);
                if (status == GeoCoderStatusCode.G_GEO_SUCCESS && pt.HasValue)
                {
                    richTextBox1.Text += "3333";
                    return pt.Value;
                }
            }

            return new PointLatLng();
        }


        private void bt_test03_Click(object sender, EventArgs e)
        {
            //test DownloadMap

            //TBD
        }

        private void DownloadMap(GMapPolygon polygon)
        {
            /*
            if (polygon != null)
            {
                RectLatLng area = GMapUtil.PolygonUtils.GetRegionMaxRect(polygon);
                try
                {
                    DownloadCfgForm downloadCfgForm = new DownloadCfgForm(area, this.gMapControl1.MapProvider);
                    if (downloadCfgForm.ShowDialog() == DialogResult.OK)
                    {
                        TileDownloaderArgs downloaderArgs = downloadCfgForm.GetDownloadTileGPoints();
                        ResetToServerAndCacheMode();

                        if (this.comboBoxStore.SelectedIndex == 2)
                        {
                            tileDownloader.TilePath = this.tilePath;
                        }
                        tileDownloader.Retry = retryNum;
                        tileDownloader.StartDownload(downloaderArgs);
                    }
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += ex.Message + "\n";
                }
            }
            else
            {
                //MessageBox.Show("請先用畫圖工具畫下載的區域多邊形或選擇省市區域！");
            }
            */
        }

        private void bt_test04_Click(object sender, EventArgs e)
        {
            //測試JSON 1

            Country china;
            try
            {
                string filename_json = @"C:\_git\vcs\_1.data\______test_files1\_json\ChinaBoundary";
                byte[] buffer = File.ReadAllBytes(filename_json);

                //byte[] buffer = Properties.Resources.ChinaBoundary_Province_City; //另種讀取資料的方式
                //byte[] buffer = Properties.Resources.ChinaBoundary;               //另種讀取資料的方式

                china = ChinaMapRegion.GetChinaRegionFromJsonBinaryBytes(buffer);

                if (china != null)
                {
                    foreach (var provice in china.Province)
                    {
                        //this.comboBoxProvince.Items.Add(provice);
                        //richTextBox1.Text += provice + "\n";
                        richTextBox1.Text += provice.name + "\n";
                    }
                    //this.comboBoxProvince.DisplayMember = "name";
                    //this.comboBoxProvince.SelectedIndex = 0;
                    //this.comboBoxProvince.SelectedValueChanged += ComboBoxProvince_SelectedValueChanged;

                    richTextBox1.Text += "\n\n";
                    Province province = china.Province[9];  //江蘇省
                    if (province != null)
                    {
                        richTextBox1.Text += province.name + " 有 " + province.City.Count.ToString() + " 個城市\n";
                        int i = 0;
                        foreach (var city in province.City)
                        {
                            richTextBox1.Text += "第 " + i.ToString() + " 個 : " + city.name + "\n";
                            i++;
                            if (city.name == "南京市")
                            {
                                int len = city.Piecearea.Count;
                                richTextBox1.Text += "共有 : " + len.ToString() + " 區\n";

                                int j;
                                for (j = 0; j < len; j++)
                                {
                                    richTextBox1.Text += "j = " + j.ToString() + "\t" + city.Piecearea[j].name + "\n";
                                    //區界座標
                                    //richTextBox1.Text += city.Piecearea[j].rings + "\n";

                                    if (j == 3)
                                    {
                                        gMapControl1.MapProvider = GMapProviders.GoogleChinaMap; //簡中地圖

                                        richTextBox1.Text += "AAAAAAAAAAAAAAAAAAAAAAA\n";
                                        string name = city.Piecearea[j].name;
                                        string rings = city.Piecearea[j].rings;

                                        if (rings != null && !string.IsNullOrEmpty(rings))
                                        {
                                            GMapPolygon polygon = GetRegionPolygon(name, rings);
                                            if (polygon != null)
                                            {
                                                GMapAreaPolygon areaPolygon = new GMapAreaPolygon(polygon.Points, name);
                                                RectLatLng rect = GMapChinaRegion.MapRegion.GetRegionMaxRect(polygon);
                                                GMapTextMarker textMarker = new GMapTextMarker(rect.LocationMiddle, name);
                                                markersOverlay.Clear();
                                                markersOverlay.Polygons.Add(areaPolygon);
                                                markersOverlay.Markers.Add(textMarker);
                                                this.gMapControl1.SetZoomToFitRect(rect);
                                            }
                                        }
                                    }
                                }
                            }
                        }
                        //this.comboBoxCity.DisplayMember = "name";
                        //this.comboBoxCity.SelectedIndex = 0;
                    }
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }
        }

        public static GMapPolygon GetRegionPolygon(string name, string rings)
        {
            if (string.IsNullOrEmpty(rings))
            {
                return null;
            }
            else
            {
                List<PointLatLng> pointList = new List<PointLatLng>();
                string[] pairPoints = rings.Split(',');
                foreach (var points in pairPoints)
                {
                    string[] point = points.Split(' ');
                    if (point.Length == 2)
                    {
                        PointLatLng p = new PointLatLng(double.Parse(point[1]), double.Parse(point[0]));
                        pointList.Add(p);
                    }
                }
                GMapPolygon polygon = new GMapPolygon(pointList, name);
                polygon.Fill = new SolidBrush(Color.FromArgb(0, Color.White));
                return polygon;
            }
        }


        private void bt_test05_Click(object sender, EventArgs e)
        {
            //測試JSON 2
            GenerateNewFile();
        }

        private static void GenerateNewFile()
        {
            string filename_json = @"C:\_git\vcs\_1.data\______test_files1\_json\ChinaBoundary_Province_City";
            Country china = JsonHelper.JsonDeserializeFromFile<Country>(filename_json, Encoding.UTF8);
            foreach (var provice in china.Province)
            {
                if (provice.name == "海南省")
                {
                    string newRings = GetMapRegionInfo();
                    provice.rings = newRings;
                    break;
                }
            }

            string filename_xml = @"ChinaBoundary_Province_City.xml";
            JsonHelper.JsonSerializeToBinaryFile(china, filename_xml);
        }

        static string GetMapRegionInfo()
        {
            string region = null;
            string newValue = "";
            bool success = MapRegion.regionDictionary.TryGetValue("海南", out region);
            if (success)
            {

                string[] points = region.Split(';');
                for (int i = 0; i < points.Length; ++i)
                {
                    string[] lnglat = points[i].Split(',');
                    newValue += lnglat[0];
                    newValue += " ";
                    newValue += lnglat[1];
                    if (i != points.Length - 1)
                    {
                        newValue += ",";
                    }
                }
                Console.WriteLine(newValue);
            }
            return newValue;
        }

        private void bt_test06_Click(object sender, EventArgs e)
        {
            gMapControl1.MapProvider = GMapProviders.GoogleChinaMap; //簡中地圖

            richTextBox1.Text += "call InitChinaRegion initial\n";
            InitChinaRegion();

            try
            {
                string filename_json = @"C:\_git\vcs\_1.data\______test_files1\_json\ChinaBoundary";
                byte[] buffer = File.ReadAllBytes(filename_json);

                //byte[] buffer = Properties.Resources.ChinaBoundary_Province_City; //另種讀取資料的方式
                //byte[] buffer = Properties.Resources.ChinaBoundary;               //另種讀取資料的方式

                china = ChinaMapRegion.GetChinaRegionFromJsonBinaryBytes(buffer);

                if (china == null)
                {
                    //log.Error("加載中國省市邊界失敗！");
                    return;
                }

                //InitPOICountrySearchCondition();

                if (china != null)
                {
                    foreach (var provice in china.Province)
                    {
                        //this.comboBoxProvince.Items.Add(provice);
                    }
                }


                richTextBox1.Text += "call InitCountryTree\n";
                InitCountryTree();
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.ToString() + "\n";
            }
        }

        private void InitChinaRegion()
        {
            TreeNode rootNode = new TreeNode("中國aaaaa");
            this.treeView1.Nodes.Add(rootNode);
            rootNode.Expand();

            //異步加載中國省市邊界
            //BackgroundWorker loadChinaWorker = new BackgroundWorker();
            //loadChinaWorker.DoWork += new DoWorkEventHandler(loadChinaWorker_DoWork);
            //loadChinaWorker.RunWorkerCompleted += new RunWorkerCompletedEventHandler(loadChinaWorker_RunWorkerCompleted);
            //loadChinaWorker.RunWorkerAsync();
        }

        private void InitCountryTree()
        {
            richTextBox1.Text += "InitCountryTree ST\n";
            try
            {
                if (china.Province != null)
                {
                    foreach (var provice in china.Province)
                    {
                        TreeNode pNode = new TreeNode(provice.name);
                        pNode.Tag = provice;
                        if (provice.City != null)
                        {
                            foreach (var city in provice.City)
                            {
                                TreeNode cNode = new TreeNode(city.name);
                                cNode.Tag = city;
                                if (city.Piecearea != null)
                                {
                                    foreach (var piecearea in city.Piecearea)
                                    {
                                        TreeNode areaNode = new TreeNode(piecearea.name);
                                        areaNode.Tag = piecearea;
                                        //richTextBox1.Text += "add cnode : " + areaNode.Tag + "\n";
                                        cNode.Nodes.Add(areaNode);
                                    }
                                }
                                pNode.Nodes.Add(cNode);
                            }
                        }

                        TreeNode rootNode = this.treeView1.Nodes[0];
                        //richTextBox1.Text += "add pNode : " + pNode + "\n";
                        richTextBox1.Text += "add pNode text : " + pNode.Text + "\n";
                        //richTextBox1.Text += "add pNode name : " + pNode.Name + "\n";
                        //richTextBox1.Text += "add pNode tag : " + pNode.Tag + "\n";
                        rootNode.Nodes.Add(pNode);
                    }
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.ToString() + "\n";
            }

            this.treeView1.NodeMouseClick += new TreeNodeMouseClickEventHandler(advTreeChina_NodeMouseClick);
        }

        void advTreeChina_NodeMouseClick(object sender, TreeNodeMouseClickEventArgs e)
        {
            //richTextBox1.Text += "advTreeChina_NodeMouseClick\n";
            this.treeView1.SelectedNode = sender as TreeNode;
            if (e.Button == MouseButtons.Left || e.Button == MouseButtons.Right)
            {
                string name = e.Node.Text;
                string rings = null;
                richTextBox1.Text += "name = " + name + ", level = " + e.Node.Level.ToString() + "\n";
                switch (e.Node.Level)
                {
                    case 0:
                        richTextBox1.Text += "XXXXXX, name = " + name + "\n";
                        break;
                    case 1:
                        Province province = e.Node.Tag as Province;
                        name = province.name;
                        rings = province.rings;
                        richTextBox1.Text += "Province, name = " + name + "\n";
                        break;
                    case 2:
                        City city = e.Node.Tag as City;
                        name = city.name;
                        rings = city.rings;
                        richTextBox1.Text += "City, name = " + name + "\n";
                        break;
                    case 3:
                        Piecearea piecearea = e.Node.Tag as Piecearea;
                        name = piecearea.name;
                        rings = piecearea.rings;
                        richTextBox1.Text += "Piecearea, name = " + name + "\n";
                        break;
                }
                if (rings != null && !string.IsNullOrEmpty(rings))
                {
                    GMapPolygon polygon = GetRegionPolygon(name, rings);
                    if (polygon != null)
                    {
                        richTextBox1.Text += "draw polygon\n";
                        GMapAreaPolygon areaPolygon = new GMapAreaPolygon(polygon.Points, name);
                        currentAreaPolygon = areaPolygon;
                        RectLatLng rect = GMapChinaRegion.MapRegion.GetRegionMaxRect(polygon);
                        GMapTextMarker textMarker = new GMapTextMarker(rect.LocationMiddle, "雙擊下載");
                        regionOverlay.Clear();
                        regionOverlay.Polygons.Add(areaPolygon);
                        regionOverlay.Markers.Add(textMarker);
                        this.gMapControl1.SetZoomToFitRect(rect);
                    }
                }
            }
        }


        private void bt_test07_Click(object sender, EventArgs e)
        {
            //測試地址解析查詢

            //尚待破解AMapProvider

            /*

            string address = "广东省深圳市福田区华强北路1002号";

            if (!string.IsNullOrEmpty(address))
            {
                richTextBox1.Text += "你按了 地址解析 之 查詢\t地址 : " + address + "\n";

                //this.routeOverlay.Markers.Clear();
                Placemark placemark = new Placemark(address);

                richTextBox1.Text += "初始化就給值 Text : " + placemark.Address + "\n";

                //placemark.CityName = currentCenterCityName;

                //richTextBox1.Text += "currentCenterCityName : " + currentCenterCityName + "\n";   尚未給值

                if (currentAreaPolygon != null)
                {
                    placemark.CityName = currentAreaPolygon.Name;
                }

                //richTextBox1.Text += "placemark.CityName : " + placemark.CityName + "\n"; 無資料

                List<PointLatLng> points = new List<PointLatLng>();
                //GeoCoderStatusCode statusCode = SoSoMapProvider.Instance.GetPoints(placemark, out points);
                GeoCoderStatusCode statusCode = AMapProvider.Instance.GetPoints(placemark, out points);

                //richTextBox1.Text += "Text : " + placemark.Address + "\n";

                if (statusCode == GeoCoderStatusCode.G_GEO_SUCCESS)
                {
                    richTextBox1.Text += "查詢資料成功, 共有" + points.Count.ToString() + " 筆資料\n";
                    foreach (PointLatLng point in points)
                    {
                        richTextBox1.Text += "取得地圖資料 地理座標 " + point.ToString() + "\n";
                        GMarkerGoogle marker = new GMarkerGoogle(point, GMarkerGoogleType.red_dot);

                        marker.ToolTipText = placemark.Address;
                        //this.routeOverlay.Markers.Add(marker);
                        this.gMapControl1.Position = point;

                        richTextBox1.Text += "Text1 : " + placemark.Address + "\n";
            */
            /*  除了第一項，全無資料
            richTextBox1.Text += "Text2 : " + placemark.AdministrativeAreaName + "\n";
            richTextBox1.Text += "Text3 : " + placemark.CityName.ToString() + "\n";
            richTextBox1.Text += "Text4 : " + placemark.CountryName + "\n";
            richTextBox1.Text += "Text5 : " + placemark.DistrictName + "\n";
            richTextBox1.Text += "Text6 : " + placemark.HouseNo.ToString() + "\n";
            richTextBox1.Text += "Text7 : " + placemark.LocalityName + "\n";
            richTextBox1.Text += "Text8 : " + placemark.Name.ToString() + "\n";
            richTextBox1.Text += "Text9 : " + placemark.Neighborhood + "\n";
            richTextBox1.Text += "Text10 : " + placemark.ProvinceName.ToString() + "\n";

            richTextBox1.Text += "Text9 : " + placemark.StreetNumber.ToString() + "\n";
            richTextBox1.Text += "Text9 : " + placemark.SubAdministrativeAreaName + "\n";
            richTextBox1.Text += "Text9 : " + placemark.Tel.ToString() + "\n";
            richTextBox1.Text += "Text9 : " + placemark.ThoroughfareName + "\n";
            */
            /*
                    }
                }
                else
                {
                    richTextBox1.Text += "查詢資料失敗\n";
                }
            }
            else
            {
                richTextBox1.Text += "地址無資料\n";
            }
            */
        }

        private void bt_test08_Click(object sender, EventArgs e)
        {
        }

        private void bt_test09_Click(object sender, EventArgs e)
        {
        }

        private void bt_test10_Click(object sender, EventArgs e)
        {
            //地址解析

            //TBD

            string currentCenterCityName = "南京市";
            //GMapAreaPolygon currentAreaPolygon;

            string address = "雨花台";

            if (!string.IsNullOrEmpty(address))
            {
                this.markersOverlay.Markers.Clear();
                Placemark placemark = new Placemark(address);
                placemark.CityName = currentCenterCityName;
                //if (currentAreaPolygon != null)
                {
                    placemark.CityName = "AAAAA";
                }
                List<PointLatLng> points = new List<PointLatLng>();
                //GeoCoderStatusCode statusCode = SoSoMapProvider.Instance.GetPoints(placemark, out points);

                /*
                GeoCoderStatusCode statusCode = AMapProvider.Instance.GetPoints(placemark, out points);

                if (statusCode == GeoCoderStatusCode.G_GEO_SUCCESS)
                {
                    foreach (PointLatLng p in points)
                    {
                        GMarkerGoogle marker = new GMarkerGoogle(p, GMarkerGoogleType.blue_dot);
                        marker.ToolTipText = placemark.Address;
                        this.markersOverlay.Markers.Add(marker);
                        this.gMapControl1.Position = p;
                    }
                }
                */

            }


            /*
            GMapPolygon polygon = ChinaMapRegion.GetRegionPolygon(name, rings);
            if (polygon != null)
            {
                GMapAreaPolygon areaPolygon = new GMapAreaPolygon(polygon.Points, name);
                currentAreaPolygon = areaPolygon;
                RectLatLng rect = GMapUtil.PolygonUtils.GetRegionMaxRect(polygon);
                GMapTextMarker textMarker = new GMapTextMarker(rect.LocationMiddle, "雙擊下載");
                regionOverlay.Clear();
                regionOverlay.Polygons.Add(areaPolygon);
                regionOverlay.Markers.Add(textMarker);
                this.mapControl.SetZoomToFitRect(rect);
            }
            */
            /*
            GMapAreaPolygon areaPolygon = new GMapAreaPolygon(drawPolygon.Points, "下載區域");
            currentAreaPolygon = areaPolygon;
            RectLatLng rect = GMapUtil.PolygonUtils.GetRegionMaxRect(currentAreaPolygon);
            GMapTextMarker textMarker = new GMapTextMarker(rect.LocationMiddle, "雙擊下載");
            regionOverlay.Clear();
            regionOverlay.Polygons.Add(areaPolygon);
            regionOverlay.Markers.Add(textMarker);
            this.mapControl.SetZoomToFitRect(rect);
*/

            /*
            if (currentAreaPolygon != null)
            {
                RectLatLng rect = GMapUtil.PolygonUtils.GetRegionMaxRect(currentAreaPolygon);
                argument.Rectangle = string.Format("{0},{1},{2},{3}",
                    new object[] { rect.LocationRightBottom.Lat, rect.LocationTopLeft.Lng, rect.LocationTopLeft.Lat, rect.LocationRightBottom.Lng });
            }
            */
        }

        private void bt_test11_Click(object sender, EventArgs e)
        {

        }

        private void bt_test12_Click(object sender, EventArgs e)
        {

        }

        private void bt_test13_Click(object sender, EventArgs e)
        {
            //讀取KML檔案

            gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖

            string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_xml\kml_mountain.kml";
            //string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_xml\kml_shangxi.kml"; //陝西省

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

            richTextBox1.Text += "cnt = " + playRoute.Points.Count.ToString() + "\n";

            //找中心
            List<PointLatLng> points = playRoute.Points;
            richTextBox1.Text += "cnt = " + points.Count.ToString() + "\n";

            int total_location = points.Count;
            richTextBox1.Text += "total_location = " + total_location.ToString() + "\n";

            double lat_north = -90;
            double lat_south = 90;
            double lng_east = -180;
            double lng_west = 180;

            int i;
            for (i = 0; i < total_location; i++)
            {
                double lat = points[i].Lat;
                double lng = points[i].Lng;

                if (lat > lat_north)
                    lat_north = lat;
                if (lat < lat_south)
                    lat_south = lat;
                if (lng > lng_east)
                    lng_east = lng;
                if (lng < lng_west)
                    lng_west = lng;
            }

            double lat_center = (lat_south + lat_north) / 2;
            double lng_center = (lng_east + lng_west) / 2;

            gMapControl1.MapProvider = GMapProviders.GoogleChinaMap; //簡中地圖

            latitude = lat_center;   //緯度
            longitude = lng_center; //經度

            gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置

            update_controls_info();

            gMapControl1.Zoom = 15; //當前比例
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
                MessageBox.Show("XXXXX " + ex.Message);
            }
            return null;
        }

        private void bt_test14_Click(object sender, EventArgs e)
        {
            //讀取GPX檔案

            gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖

            string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_xml\gps_bicycle.gpx";

            try
            {
                string objectXml = File.ReadAllText(filename);
                gpxType type = this.gMapControl1.Manager.DeserializeGPX(objectXml);
                if (type != null)
                {
                    if ((type.trk != null) && (type.trk.Length > 0))
                    {
                        List<PointLatLng> points = new List<PointLatLng>();
                        foreach (trkType trk in type.trk)
                        {
                            foreach (trksegType seg in trk.trkseg)
                            {
                                foreach (wptType p in seg.trkpt)
                                {
                                    points.Add(new PointLatLng((double)p.lat, (double)p.lon));
                                }
                            }
                            string name = string.IsNullOrEmpty(trk.name) ? string.Empty : trk.name;
                            GMapRoute item = new GMapRoute(points, name)
                            {
                                Stroke = new Pen(Color.FromArgb(0x90, Color.Red))
                            };
                            item.Stroke.Width = 5f;
                            item.Stroke.DashStyle = DashStyle.DashDot;
                            this.polygonsOverlay.Routes.Add(item);
                        }
                    }
                    if ((type.rte != null) && (type.rte.Length > 0))
                    {
                        List<PointLatLng> points = new List<PointLatLng>();
                        foreach (rteType rte in type.rte)
                        {
                            foreach (wptType p in rte.rtept)
                            {
                                points.Add(new PointLatLng((double)p.lat, (double)p.lon));
                            }
                            string str3 = string.IsNullOrEmpty(rte.name) ? string.Empty : rte.name;
                            GMapRoute route2 = new GMapRoute(points, str3)
                            {
                                Stroke = new Pen(Color.FromArgb(0x90, Color.Red))
                            };
                            route2.Stroke.Width = 5f;
                            route2.Stroke.DashStyle = DashStyle.DashDot;
                            this.polygonsOverlay.Routes.Add(route2);
                        }
                    }
                    if (type.wpt != null && type.wpt.Length > 0)
                    {
                        foreach (wptType p in type.wpt)
                        {
                            PointLatLng point = new PointLatLng((double)p.lat, (double)p.lon);
                            GMarkerGoogle marker = new GMarkerGoogle(point, GMarkerGoogleType.blue_dot);
                            this.polygonsOverlay.Markers.Add(marker);
                        }
                    }
                    this.gMapControl1.ZoomAndCenterRoutes(null);
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }
        }

        private void bt_test15_Click(object sender, EventArgs e)
        {
            //讀取KML檔案

            return;

            /*
            gMapControl1.MapProvider = GMapProviders.GoogleMap; //正中地圖

            string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_xml\kml_mountain.kml";

            try
            {
                this.polygonsOverlay.Clear();
                InitKMLPlaceMarks(KmlUtil.GetPlaceMarksFromKmlFile(filename));
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Error : " + ex.ToString() + "\n";
                MessageBox.Show("讀取KML文件時出現異常");
            }
            */
        }

        private void bt_zoom_in_Click(object sender, EventArgs e)
        {
            //放大
            gMapControl1.Zoom += 1; //當前比例
            update_controls_info();
        }

        private void bt_zoom_out_Click(object sender, EventArgs e)
        {
            //縮小
            gMapControl1.Zoom -= 1; //當前比例
            update_controls_info();
        }

        private void bt_draw0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了繪圖工具 圓形\n";
            draw.DrawingMode = DrawingMode.Circle;
            draw.IsEnable = true;
        }

        private void bt_draw1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了繪圖工具 矩形\n";
            draw.DrawingMode = DrawingMode.Rectangle;
            draw.IsEnable = true;
        }

        private void bt_draw2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了繪圖工具 多邊形\n";
            draw.DrawingMode = DrawingMode.Polygon;
            draw.IsEnable = true;
        }

        private void bt_draw3_Click(object sender, EventArgs e)
        {
            //線段, 一段線
            richTextBox1.Text += "你按了繪圖工具 線段\n";
            draw.DrawingMode = DrawingMode.Line;
            draw.IsEnable = true;
        }

        private void bt_draw4_Click(object sender, EventArgs e)
        {
            //折線段 = 線條, 多段連線
            richTextBox1.Text += "你按了繪圖工具 折線段\n";
            draw.DrawingMode = DrawingMode.Route;
            draw.IsEnable = true;
        }

        private void bt_draw5_Click(object sender, EventArgs e)
        {
            //測距
            drawDistance.IsEnable = true;
        }

        void show_locations(string[,] location)
        {

            int total_location = location.GetUpperBound(0) + 1;
            richTextBox1.Text += "total_location = " + total_location.ToString() + "\n";

            double lat_north = -90;
            double lat_south = 90;
            double lng_east = -180;
            double lng_west = 180;

            int i;
            for (i = 0; i < total_location; i++)
            {
                double lat = double.Parse(location[i, 1]);
                double lng = double.Parse(location[i, 2]);

                if (lat > lat_north)
                    lat_north = lat;
                if (lat < lat_south)
                    lat_south = lat;
                if (lng > lng_east)
                    lng_east = lng;
                if (lng < lng_west)
                    lng_west = lng;
            }

            double lat_center = (lat_south + lat_north) / 2;
            double lng_center = (lng_east + lng_west) / 2;

            gMapControl1.MapProvider = GMapProviders.GoogleChinaMap; //簡中地圖

            latitude = lat_center;   //緯度
            longitude = lng_center; //經度

            gMapControl1.Position = new PointLatLng(latitude, longitude); //地圖中心位置

            update_controls_info();

            for (i = 0; i < total_location; i++)
            {
                latitude = double.Parse(location[i, 1]);
                longitude = double.Parse(location[i, 2]);

                //AddMarker(latitude, longitude, GMarkerGoogleType.blue_dot, location[i, 0]);
                draw_circle_text(latitude, longitude, location[i, 0]);
            }
        }

        //畫圖完成函數
        void draw_DrawComplete(object sender, DrawEventArgs e)
        {
            try
            {
                if (e != null && (e.Polygon != null || e.Rectangle != null || e.Circle != null || e.Line != null || e.Route != null))
                {
                    GMapPolygon drawPolygon = null;
                    switch (e.DrawingMode)
                    {
                        case DrawingMode.Polygon:
                            drawPolygon = e.Polygon;
                            break;
                        case DrawingMode.Rectangle:
                            drawPolygon = e.Rectangle;
                            break;
                        case DrawingMode.Circle:
                            polygonsOverlay.Markers.Add(e.Circle);
                            break;
                        case DrawingMode.Line:
                            polygonsOverlay.Routes.Add(e.Line);
                            break;
                        case DrawingMode.Route:
                            polygonsOverlay.Routes.Add(e.Route);
                            break;
                        default:
                            draw.IsEnable = false;
                            break;
                    }

                    if (drawPolygon != null)
                    {
                        GMapAreaPolygon areaPolygon = new GMapAreaPolygon(drawPolygon.Points, "下載區域");
                        currentAreaPolygon = areaPolygon;
                        //RectLatLng rect = GMapUtil.PolygonUtils.GetRegionMaxRect(currentAreaPolygon);
                        RectLatLng rect = GMapChinaRegion.MapRegion.GetRegionMaxRect(currentAreaPolygon);

                        GMapTextMarker textMarker = new GMapTextMarker(rect.LocationMiddle, "雙擊下載");
                        regionOverlay.Clear();
                        regionOverlay.Polygons.Add(areaPolygon);
                        regionOverlay.Markers.Add(textMarker);
                        this.gMapControl1.SetZoomToFitRect(rect);
                    }
                }
            }
            finally
            {
                draw.IsEnable = false;
            }
        }

        void drawDistance_DrawComplete(object sender, DrawDistanceEventArgs e)
        {
            if (e != null)
            {
                GMapOverlay distanceOverlay = new GMapOverlay();
                this.gMapControl1.Overlays.Add(distanceOverlay);
                foreach (LineMarker line in e.LineMarkers)
                {
                    distanceOverlay.Markers.Add(line);
                }
                foreach (DrawDistanceMarker marker in e.DistanceMarkers)
                {
                    distanceOverlay.Markers.Add(marker);
                }
                distanceOverlay.Markers.Add(e.DistanceDeleteMarker);
            }
            drawDistance.IsEnable = false;
        }
    }

    public class Piecearea
    {
        [XmlAttribute]
        public string code { set; get; }

        [XmlAttribute]
        public string name { set; get; }

        [XmlAttribute]
        public string rings { set; get; }
    }

    public class City
    {
        [XmlAttribute]
        public string code { set; get; }

        [XmlAttribute]
        public string name { set; get; }

        [XmlAttribute]
        public string rings { set; get; }

        [XmlElement]
        public List<Piecearea> Piecearea { set; get; }
    }

    public class Province
    {
        [XmlAttribute]
        public string ID { set; get; }

        [XmlAttribute]
        public string code { set; get; }

        [XmlAttribute]
        public string name { set; get; }

        [XmlAttribute]
        public string rings { set; get; }

        [XmlElement]
        public List<City> City { set; get; }
    }

    public class Country
    {
        [XmlAttribute]
        public string ID { set; get; }

        [XmlAttribute]
        public string code { set; get; }

        [XmlAttribute]
        public string name { set; get; }

        [XmlElement]
        public List<Province> Province { set; get; }
    }

    public class GMapAreaPolygon : GMapPolygon
    {
        public GMapAreaPolygon(List<PointLatLng> points, string name)
            : base(points, name)
        {
            this.Stroke = new Pen(Color.Blue);
            this.Stroke.Width = 3f;
            this.Stroke.DashStyle = DashStyle.Dash;
            //this.Fill = new SolidBrush(Color.Azure);
            this.Fill = new SolidBrush(Color.FromArgb(100, 240, 255, 255));

            this.IsHitTestVisible = true;
        }
    }

    public static class ChinaMapRegion
    {
        public static Country GetChinaRegionFromJsonBinaryBytes(byte[] buffer)
        {
            Country china = JsonHelper.JsonDeserializeFromBinaryBytes<Country>(buffer);
            return china;
        }

        public static Country GetChinaRegionFromJsonFile(string filePath)
        {
            Country china = JsonHelper.JsonDeserializeFromFile<Country>(filePath, Encoding.UTF8);
            return china;
        }

        public static Country GetChinaRegionFromXmlFile(string filePath)
        {
            Country china = XmlHelper.XmlDeserializeFromFile<Country>(filePath, Encoding.UTF8);
            return china;
        }

        /*
        public static GMapPolygon GetRegionPolygon(string name, string rings)
        {
            if (string.IsNullOrEmpty(rings))
            {
                return null;
            }
            else
            {
                List<PointLatLng> pointList = new List<PointLatLng>();
                string[] pairPoints = rings.Split(',');
                foreach (var points in pairPoints)
                {
                    string[] point = points.Split(' ');
                    if (point.Length == 2)
                    {
                        PointLatLng p = new PointLatLng(double.Parse(point[1]), double.Parse(point[0]));
                        pointList.Add(p);
                    }
                }
                GMapPolygon polygon = new GMapPolygon(pointList, name);
                polygon.Fill = new SolidBrush(Color.FromArgb(0, Color.White));
                return polygon;
            }
        }
        */

    }

    /// <summary>
    /// represents place info
    /// </summary>
    public struct Placemark
    {
        public static readonly Placemark Empty = new Placemark();

        //string address;

        /// <summary>
        /// the address
        /// </summary>
        public string Address;
        //{
        //    get
        //    {
        //        return address;
        //    }
        //    internal set
        //    {
        //        address = value;
        //    }
        //}

        /// <summary>
        /// the accuracy of address
        /// </summary>
        public int Accuracy;

        // parsed values from address      
        public string ThoroughfareName;
        public string LocalityName;
        public string PostalCodeNumber;
        public string CountryName;
        public string AdministrativeAreaName;
        public string DistrictName;
        public string SubAdministrativeAreaName;
        public string Neighborhood;
        public string StreetNumber;

        public string CountryNameCode;
        public string HouseNo;

        //Added for Map
        public PointLatLng Point;
        public string Name;
        public string CountryCode;
        public string ProvinceName;
        public string CityName;
        public string Tel;
        public string Category;
        public RectLatLng LatLonBox;

        public Placemark(string address)
        {
            //this.address = address;
            Address = address;

            Accuracy = 0;
            HouseNo = string.Empty;
            ThoroughfareName = string.Empty;
            DistrictName = string.Empty;
            LocalityName = string.Empty;
            PostalCodeNumber = string.Empty;
            CountryName = string.Empty;
            CountryNameCode = string.Empty;
            AdministrativeAreaName = string.Empty;
            SubAdministrativeAreaName = string.Empty;
            Neighborhood = string.Empty;
            StreetNumber = string.Empty;

            Point = PointLatLng.Empty;
            LatLonBox = RectLatLng.Empty;
            Name = string.Empty;
            CountryCode = string.Empty;
            ProvinceName = string.Empty;
            CityName = string.Empty;
            Tel = string.Empty;
            Category = string.Empty;
        }

        public Placemark(Placemark oth)
        {
            this.Address = oth.Address;
            this.Category = oth.Category;
            this.ProvinceName = oth.ProvinceName;
            this.CityName = oth.CityName;
            this.CountryCode = oth.CountryCode;
            this.LatLonBox = oth.LatLonBox;
            this.Name = oth.Name;
            this.Tel = oth.Tel;
            this.Point = oth.Point;
            this.Accuracy = oth.Accuracy;
            this.HouseNo = oth.HouseNo;
            this.ThoroughfareName = oth.ThoroughfareName;
            this.DistrictName = oth.DistrictName;
            this.LocalityName = oth.LocalityName;
            this.PostalCodeNumber = oth.PostalCodeNumber;
            this.CountryName = oth.CountryName;
            this.CountryNameCode = oth.CountryNameCode;
            this.AdministrativeAreaName = oth.AdministrativeAreaName;
            this.SubAdministrativeAreaName = oth.SubAdministrativeAreaName;
            this.Neighborhood = oth.Neighborhood;
            this.StreetNumber = oth.StreetNumber;
        }
    }
}
