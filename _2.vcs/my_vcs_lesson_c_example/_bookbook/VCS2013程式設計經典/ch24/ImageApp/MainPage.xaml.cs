using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Navigation;
using Microsoft.Phone.Controls;
using Microsoft.Phone.Shell;
using ImageApp.Resources;


using System.Windows.Media.Imaging; //使用BitmapImage，必須引用此命名空間

namespace ImageApp
{
    public partial class MainPage : PhoneApplicationPage
    {
        // 建構函式
        public MainPage()
        {
            InitializeComponent();

            Loaded += MainPage_Loaded;
            btn1.Click += btn1_Click;
            btn2.Click += btn1_Click;
            btn3.Click += btn1_Click;
        }

        void MainPage_Loaded(object sender, RoutedEventArgs e)
        {
            Uri uri = new Uri("images/小鴨1.jpg" , UriKind.Relative);
            img.Source = new BitmapImage(uri);
        }

        void btn1_Click(object sender, RoutedEventArgs e)
        {
            string imgName = (sender as Button).Content.ToString() + ".jpg";
            Uri uri = new Uri("images/" + imgName, UriKind.Relative);
            img.Source = new BitmapImage(uri);
        }
    }
}