using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Navigation;
using Microsoft.Phone.Controls;
using Microsoft.Phone.Shell;

//使用PhoneCallTask和BingMapsDirectionsTask類別必須引用此命名空間
using Microsoft.Phone.Tasks;
//使用GeoCoordinate類別必須引用此命名空間
using System.Device.Location;

namespace TaipeiSPAApp
{
    public partial class DetailsPage : PhoneApplicationPage
    {
        public DetailsPage()
        {
            InitializeComponent();
            Loaded += DetailsPage_Loaded;
            btnPhone.Click += btnPhone_Click;
            btnMap.Click += btnMap_Click;
        }

        int index = 0;

        void DetailsPage_Loaded(object sender, RoutedEventArgs e)
        {
            string selectedIndex ="";
            if (NavigationContext.QueryString.TryGetValue("selectedItem", out selectedIndex))
            {
                index = int.Parse(selectedIndex);
                tbPlaceName.Text = App.ViewModel.Items[index].PlaceName;
                tbAddress.Text =  App.ViewModel.Items[index].Address ;
                tbTel.Text = "02-" + App.ViewModel.Items[index].Tel;
            }
        }

        void btnPhone_Click(object sender, RoutedEventArgs e)
        {
            PhoneCallTask pct = new PhoneCallTask();
            pct.PhoneNumber = tbTel.Text.Replace("-", "");
            pct.Show();
        }

        void btnMap_Click(object sender, RoutedEventArgs e)
        {
            double lat, lng;
            lng = App.ViewModel.Items[index].Lng;
            lat = App.ViewModel.Items[index].Lat;
           
            //終點名稱(即店名)
            string EndName = App.ViewModel.Items[index].PlaceName;

            BingMapsDirectionsTask bingMap = new BingMapsDirectionsTask();
            bingMap.End = new LabeledMapLocation(EndName, new GeoCoordinate(lat, lng));
            bingMap.Show();
        }
    }
}