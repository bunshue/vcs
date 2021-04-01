using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

// 命名空間
using System.Net;
using System.Net.PeerToPeer;

namespace P2P
{
  /// <summary>
  /// Interaction logic for Window1.xaml
  /// </summary>
  public partial class Window1 : Window
  {
    public Window1()
    {
      InitializeComponent();
    }

    private void Window_Loaded(object sender, RoutedEventArgs e)
    {
      progressBar.Visibility = Visibility.Hidden;
    }

    private void btnResolve_Click(object sender, RoutedEventArgs e)
    {
      if (txtPeerName.Text.Length > 0)
      {
        // 建立PeerName物件
        PeerName peerName = new PeerName(txtPeerName.Text);

        // 建立PeerNameResolver物件
        PeerNameResolver resolver = new PeerNameResolver();

        // 宣告非同步解析作業正在執行中所觸發之事件
        // 並定義所呼叫的方法為ResolveProgressChangedCallback
        resolver.ResolveProgressChanged += new EventHandler<ResolveProgressChangedEventArgs>(ResolveProgressChangedCallback);

        // 宣告非同步解析作業完成時所觸發之事件
        // 並定義所呼叫的方法為ResolveCompletedCallback
        resolver.ResolveCompleted += new EventHandler<ResolveCompletedEventArgs>(ResolveCompletedCallback);

        lstPeerNameRecord.Items.Clear();
        progressBar.Visibility = Visibility.Visible;

        // 非同步將PNRP Peer Name解析為PNRP Peer Name記錄物件
        resolver.ResolveAsync(peerName, 1);
      }
      else
        MessageBox.Show("Please enter Peer Name.", "Peer Name Resolver", MessageBoxButton.OK, MessageBoxImage.Error);
    }

    // 自訂非同步解析作業正在執行中，所呼叫的方法
    private void ResolveProgressChangedCallback(object sender, ResolveProgressChangedEventArgs e)
    {
      // 取得非同步作業的進度百分比
      // 並藉此改變ProgressBar物件的顯示進度
      progressBar.Value = e.ProgressPercentage;

      // 取得PNRP Peer Name記錄物件
      PeerNameRecord pnr = e.PeerNameRecord;

      foreach (IPEndPoint endpoint in pnr.EndPointCollection)
      {
        lstPeerNameRecord.Items.Add(endpoint);
      }
    }

    // 自訂非同步解析作業完成時，所呼叫的方法
    private void ResolveCompletedCallback(object sender, ResolveCompletedEventArgs e)
    {
      progressBar.Visibility = Visibility.Hidden;

      if (lstPeerNameRecord.Items.Count == 0)
        MessageBox.Show("No Peer Name Record Found", "Peer Name Resolver", MessageBoxButton.OK, MessageBoxImage.Error);
    }
  }
}
