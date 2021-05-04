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

    private void btnResolve_Click(object sender, RoutedEventArgs e)
    {
      if (txtPeerName.Text.Length > 0)
      {
        // 建立PeerName物件
        PeerName peerName = new PeerName(txtPeerName.Text);

        // 建立PeerNameResolver物件
        PeerNameResolver resolver = new PeerNameResolver();

        // 將PNRP Peer Name解析為PNRP Peer Name記錄物件
        PeerNameRecordCollection pmrcs = resolver.Resolve(peerName);

        if (pmrcs.Count > 0)
          lstPeerNameRecord.Items.Clear();
        else
          MessageBox.Show("No Peer Name Record Found", "Peer Name Resolver", MessageBoxButton.OK, MessageBoxImage.Error);

        foreach (PeerNameRecord pmrc in pmrcs)
        {
          foreach (IPEndPoint endpoint in pmrc.EndPointCollection)
          {
            lstPeerNameRecord.Items.Add(endpoint);
          }
        }
      }
      else
        MessageBox.Show("Please enter Peer Name.", "Peer Name Resolver", MessageBoxButton.OK, MessageBoxImage.Error);
    }
  }
}
