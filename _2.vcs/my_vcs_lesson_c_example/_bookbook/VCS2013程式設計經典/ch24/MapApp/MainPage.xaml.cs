using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Navigation;
using Microsoft.Phone.Controls;
using Microsoft.Phone.Shell;
using MapApp.Resources;


using Microsoft.Phone.Tasks; //使用BingMapsDirectionsTask必須引用此命名空間
using System.Device.Location;  //使用GeoCoordinate必須引用此命名空間

namespace MapApp
{
    public partial class MainPage : PhoneApplicationPage
    {
        // 建構函式
        public MainPage()
        {
            InitializeComponent();

            btn1.Click += btn1_Click;
            btn2.Click += btn2_Click;
        }
        //美術館->台中新光三越
        void btn1_Click(object sender, RoutedEventArgs e)
        {
            BingMapsDirectionsTask bingMap = new BingMapsDirectionsTask();
            bingMap.Start = new LabeledMapLocation("台中美術館", new GeoCoordinate(24.152018, 120.66374059999998));
            bingMap.End = new LabeledMapLocation("台中新光三越", new GeoCoordinate(24.165832, 120.644271));
            bingMap.Show();
        }
        //目前位置->海生館
        void btn2_Click(object sender, RoutedEventArgs e)
        {
            BingMapsDirectionsTask bingMap = new BingMapsDirectionsTask();
            bingMap.End = new LabeledMapLocation("海生館", new GeoCoordinate(22.04594, 120.69875200000001));
            bingMap.Show();
        }
    }
}