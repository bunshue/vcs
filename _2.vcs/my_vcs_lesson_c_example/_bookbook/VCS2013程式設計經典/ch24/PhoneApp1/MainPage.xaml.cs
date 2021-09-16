using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Navigation;
using Microsoft.Phone.Controls;
using Microsoft.Phone.Shell;
using PhoneApp1.Resources;

namespace PhoneApp1
{
    public partial class MainPage : PhoneApplicationPage
    {
        // 建構函式
        public MainPage()
        {
            InitializeComponent();
            // 指定 [確定] 鈕Click事件觸發時執行btnOk_Click事件處理函式
            btnOk.Click += btnOk_Click;
        }

        void btnOk_Click(object sender, RoutedEventArgs e)
        {
            MessageBox.Show(txtName.Text + "你好");
        }
    }
}