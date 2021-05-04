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
using System.Net.PeerToPeer.Collaboration; 

namespace PeopleNearMe
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

    private void btnSignIn_Click(object sender, RoutedEventArgs e)
    {
      // 登入至Internet之範圍
      PeerCollaboration.SignIn(PeerScope.NearMe);

      // 宣告當Peer端點登入或登出時所觸發之事件
      // 並定義所呼叫的方法為PeerNearMeChangedCallback
      PeerNearMe.PeerNearMeChanged += new EventHandler<PeerNearMeChangedEventArgs>(PeerNearMeChangedCallback);
    }

    private void btnSignOut_Click(object sender, RoutedEventArgs e)
    {
      // 登出近端分享
      PeerCollaboration.SignOut(PeerScope.NearMe);
    }

    private void btnGet_Click(object sender, RoutedEventArgs e)
    {
      // 取得目前所有登入的Peer端點
      PeerNearMeCollection pnmc = PeerCollaboration.GetPeersNearMe();

      String str = "";

      foreach (PeerNearMe pnm in pnmc)
      {
        // 取得Peer端點的暱稱
        str = pnm.Nickname;

        // 取得Peer端點的位置
        PeerEndPointCollection pepc = pnm.PeerEndPoints;

        foreach (PeerEndPoint pep in pepc)
        {
          // 回傳System.Net.IPEndPoint物件
          IPEndPoint ipEndPoint = pep.EndPoint;

          // 取得Peer端點的IP位址
          str = str + ", " + ipEndPoint.Address.ToString() + ":";
          // 取得Peer端點的通訊埠
          str = str + ipEndPoint.Port.ToString();
        }

        lstPeer.Items.Add(str);
      }
    }

    // 自訂當Peer端點登入或登出時所呼叫的方法
    private void PeerNearMeChangedCallback(Object sender, PeerNearMeChangedEventArgs e)
    {
      String str = "";
      
      PeerNearMe pnm = e.PeerNearMe as PeerNearMe;

      // 取得Peer端點的位置
      PeerEndPointCollection pepc = pnm.PeerEndPoints;

      foreach (PeerEndPoint pep in pepc)
      {
        // 回傳System.Net.IPEndPoint物件
        IPEndPoint ipEndPoint = pep.EndPoint;

        // 取得Peer端點的IP位址
        str = str + ", " + ipEndPoint.Address.ToString() + ":";
        // 取得Peer端點的通訊埠
        str = str + ipEndPoint.Port.ToString();
      }

      // 取得PeerNearMe物件所發生的變更類型
      switch (e.PeerChangeType)
      {
        // 當有新的Peer端點登入時
        case PeerChangeType.Added:
          lstPeer.Items.Add(str);
          break;
        // 當Peer端點登出時
        case PeerChangeType.Deleted:
          break;
        // 當Peer端點因相關資訊更新時
        case PeerChangeType.Updated:
          lstPeer.Items.Add(str);
          break;
        default:
          break;
      }
    }
  }
}
