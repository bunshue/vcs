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
    }

    private void btnSignOut_Click(object sender, RoutedEventArgs e)
    {
      // 登出近端分享
      PeerCollaboration.SignOut(PeerScope.NearMe);
    }
  }
}
