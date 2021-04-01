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
    PeerNameRegistration peerNameRegistration;
    
    public Window1()
    {
      InitializeComponent();
    }

    private void btnRegister_Click(object sender, RoutedEventArgs e)
    {
      if (txtPeerName.Text.Length > 0 && txtPort.Text.Length > 0)
      {
        // 建立PeerName物件
        // 設定PNRP Peer Name為未受保護的名稱
        PeerName peerName = new PeerName(txtPeerName.Text, PeerNameType.Unsecured);

        // 以PNRP Peer Name與通訊埠建立PeerNameRegistration物件
        peerNameRegistration = new PeerNameRegistration(peerName, Int32.Parse(txtPort.Text));

        // 設定PNRP Peer Name的其他資訊
        peerNameRegistration.Comment = "PNRP Peer Name的其他資訊";
        // 設定PeerNameRegistration物件之二進位資料
        peerNameRegistration.Data = System.Text.Encoding.UTF8.GetBytes("二進位資料");

        // 設定用戶端或Peer端點目前參與的所有連結本機之PNRP Cloud
        peerNameRegistration.Cloud = Cloud.AllLinkLocal;
        // 設定是否自動選取IP位址和通訊埠
        peerNameRegistration.UseAutoEndPointSelection = true;
        // 將PNRP Peer Name註冊至PNRP Cloud中
        peerNameRegistration.Start();
      }
      else
        MessageBox.Show("Please enter Peer Name and Port.", "P2P", MessageBoxButton.OK, MessageBoxImage.Error);
    }

    private void btnCloud_Click(object sender, RoutedEventArgs e)
    {
      // 取得目前所有有效的PNRP Cloud
      CloudCollection clouds = Cloud.GetAvailableClouds();

      if (clouds.Count > 0)
        lstCloud.Items.Clear();
      else
        MessageBox.Show("No Clouds Found", "P2P", MessageBoxButton.OK, MessageBoxImage.Error);

      foreach (Cloud cloud in clouds)
      {
        // 取得PNRP Cloud的名稱與網路範圍
        lstCloud.Items.Add(cloud.Name + ", " + cloud.Scope);
      }
    }

    private void Window_Closing(object sender, System.ComponentModel.CancelEventArgs e)
    {
      // 自PNRP Cloud中移除PNRP Peer Name之註冊
      peerNameRegistration.Stop();
    }
  }
}
