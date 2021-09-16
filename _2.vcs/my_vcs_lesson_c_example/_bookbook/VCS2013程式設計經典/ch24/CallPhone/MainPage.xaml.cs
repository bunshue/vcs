using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Navigation;
using Microsoft.Phone.Controls;
using Microsoft.Phone.Shell;
using CallPhone.Resources;

using Microsoft.Phone.Tasks;

namespace CallPhone
{
    public partial class MainPage : PhoneApplicationPage
    {
        // 建構函式
        public MainPage()
        {
            InitializeComponent();
            btnGoTop.Click += btnGoTop_Click;
            btnPhone.Click += btnPhone_Click;
        }

        void btnGoTop_Click(object sender, RoutedEventArgs e)
        {
            PhoneCallTask phone = new PhoneCallTask();
            phone.DisplayName = "碁峰資訊";
            phone.PhoneNumber = "0227882408";
            phone.Show();
        }

        void btnPhone_Click(object sender, RoutedEventArgs e)
        {
            PhoneCallTask phone = new PhoneCallTask();
            phone.PhoneNumber = "0911123456";
            phone.Show();
        }
    }
}