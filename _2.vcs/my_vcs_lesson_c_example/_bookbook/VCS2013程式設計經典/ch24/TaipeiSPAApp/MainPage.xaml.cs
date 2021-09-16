using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Navigation;
using Microsoft.Phone.Controls;
using Microsoft.Phone.Shell;
using TaipeiSPAApp.Resources;

namespace TaipeiSPAApp
{
    public partial class MainPage : PhoneApplicationPage
    {
        // 建構函式
        public MainPage()
        {
            InitializeComponent();

            Loaded += MainPage_Loaded;
            MainLongListSelector.SelectionChanged += MainLongListSelector_SelectionChanged;
        }

        void MainPage_Loaded(object sender, RoutedEventArgs e)
        {
            if (!App.ViewModel.IsDataLoaded)
            {
                App.ViewModel.LoadData();
                MainLongListSelector.ItemsSource = App.ViewModel.Items;
            }
        }

        void MainLongListSelector_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            // 如果選取的項目是 null (沒有選取項目)，不執行任何動作
            if (MainLongListSelector.SelectedItem == null)
                return;

            // 巡覽到新頁面
            NavigationService.Navigate(new Uri("/DetailsPage.xaml?selectedItem=" + ((SPAPlace)MainLongListSelector.SelectedItem ).ID, UriKind.Relative));

            // 將選取的項目重設為 null (沒有選取項目)
            MainLongListSelector.SelectedItem = null;
        }
    }
}