using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Collections;
using System.Globalization;

using System.Net;
using System.Net.NetworkInformation;

namespace IPConfiguration
{
  public partial class Form1 : Form
  {
    private NetworkInterface[] interfaces = null;
    private NetworkInterface selectedInterface = null;

    public Form1()
    {
      InitializeComponent();
    }

    private void Form1_Load(object sender, EventArgs e)
    {
      // 宣告當網路介面卡的IP位址變更時所觸發之事件
      // 並定義所呼叫的方法為NetworkAddressChangedCallback
      NetworkChange.NetworkAddressChanged += new NetworkAddressChangedEventHandler(NetworkAddressChangedCallback);

      // 宣告當網路的有效性變更時所觸發之事件
      // 並定義所呼叫的方法為NetworkAvailabilityChangedCallback
      NetworkChange.NetworkAvailabilityChanged += new NetworkAvailabilityChangedEventHandler(NetworkAvailabilityChangedCallback);

      // 取得本機電腦上所有網路介面卡的資訊
      interfaces = NetworkInterface.GetAllNetworkInterfaces();

      // 判斷本機電腦之網路介面卡是否有網路連線
      if (NetworkInterface.GetIsNetworkAvailable())
        StatusBar.Text = "Network interface is up.";
      else
        StatusBar.Text = "The network is not available.";

      ShowNetworkInterfaces();
    }

    private void ShowNetworkInterfaces()
    {
      cboInterfaces.Items.Clear();

      // 取得本機電腦上所有網路介面卡的資訊
      interfaces = NetworkInterface.GetAllNetworkInterfaces();

      if (interfaces.Length == 0)
        cboInterfaces.Items.Add("No network interface is found.");
      else
      {
        foreach (NetworkInterface adapter in interfaces)
          // 取得網路介面卡的描述包括廠商、類型、商標及型號
          cboInterfaces.Items.Add(adapter.Description);

        cboInterfaces.SelectedIndex = 0;

        selectedInterface = interfaces[cboInterfaces.SelectedIndex];

        UpdateNetworkInformation();
      }
    }

    private void UpdateNetworkStatistics()
    {
      ListViewItem item = null;
      string[] listItem = new string[2];

      lstInformation.Items.Clear();

      // 取得本機電腦支援IPv4通訊協定之網路介面卡的統計資料
      IPv4InterfaceStatistics ipv4Statistics = selectedInterface.GetIPv4Statistics();

      // 取得支援IP通訊協定之網路介面卡的相關資訊
      IPInterfaceProperties ipProperties = selectedInterface.GetIPProperties();

      NumberFormatInfo numberFormat = NumberFormatInfo.CurrentInfo;

      // DNS尾碼
      listItem[0] = "DNS尾碼";
      listItem[1] = ipProperties.DnsSuffix.ToString();
      item = new ListViewItem(listItem);
      lstInformation.Items.Add(item);

      // 取得網路介面卡所接收的位元組數目
      long received = ipv4Statistics.BytesReceived / 1024;
      listItem[0] = "介面卡所接收的位元組數目";
      listItem[1] = received.ToString("N0", numberFormat) + " KB";
      item = new ListViewItem(listItem);
      lstInformation.Items.Add(item);

      // 取得網路介面卡所傳送的位元組數目
      long sent = ipv4Statistics.BytesSent / 1024;
      listItem[0] = "介面卡所傳送的位元組數目";
      listItem[1] = sent.ToString("N0", numberFormat) + " KB";
      item = new ListViewItem(listItem);
      lstInformation.Items.Add(item);

      // 取得網路介面卡的速度
      listItem[0] = "介面卡的速度";
      listItem[1] = ConvertSpeedtoString(selectedInterface.Speed);
      item = new ListViewItem(listItem);
      lstInformation.Items.Add(item);

      // 取得網路介面卡目前的狀態，為OperationalStatus之列舉值
      listItem[0] = "介面卡目前的狀態";
      listItem[1] = selectedInterface.OperationalStatus.ToString();
      item = new ListViewItem(listItem);
      lstInformation.Items.Add(item);

      // 判斷網路介面卡是否接收多點播送封包
      listItem[0] = "是否接收多點播送封包";
      listItem[1] = selectedInterface.SupportsMulticast.ToString();
      item = new ListViewItem(listItem);
      lstInformation.Items.Add(item);
    }

    private void UpdateNetworkInformation()
    {
      lstAddress.Items.Clear();

      // 取得支援IP通訊協定之網路介面卡的相關資訊
      IPInterfaceProperties ipProperties = selectedInterface.GetIPProperties();

      // 取得DHCP伺服器位址
      IPAddressCollection ipAddresses = ipProperties.DhcpServerAddresses;
      foreach (IPAddress ipAddress in ipAddresses)
        InsertAddress("DHCP伺服器", ipAddress);

      // 取得網路介面卡所設定之DNS伺服器位址
      ipAddresses = ipProperties.DnsAddresses;
      foreach (IPAddress ipAddress in ipAddresses)
        InsertAddress("DNS伺服器", ipAddress);

      // 取得WINS伺服器的位址
      ipAddresses = ipProperties.WinsServersAddresses;
      foreach (IPAddress ipAddress in ipAddresses)
        InsertAddress("WINS伺服器", ipAddress);

      // 取得網路介面卡的網路閘道位址
      GatewayIPAddressInformationCollection gatewayInfo = ipProperties.GatewayAddresses;
      foreach (GatewayIPAddressInformation info in gatewayInfo)
        InsertAddress("網路閘道", info.Address);

      // 取得網路介面卡的Anycast IP位址
      IPAddressInformationCollection anycastInfo = ipProperties.AnycastAddresses;
      foreach (IPAddressInformation info in anycastInfo)
        InsertAddress("Anycast", info.Address);

      // 取得網路介面卡的多點播送位址
      MulticastIPAddressInformationCollection multicastInfo = ipProperties.MulticastAddresses;
      foreach (MulticastIPAddressInformation info in multicastInfo)
        InsertAddress("多點播送", info.Address);

      // 取得網路介面卡的單點傳送位址
      UnicastIPAddressInformationCollection unicastInfo = ipProperties.UnicastAddresses;
      foreach (UnicastIPAddressInformation info in unicastInfo)
        InsertAddress("單點傳送", info.Address);
    }

    private void InsertAddress(string type, IPAddress ipAddress)
    {
      string[] listItem = new string[2];

      listItem[0] = type;
      listItem[1] = ipAddress.ToString();

      ListViewItem item = new ListViewItem(listItem);
      lstAddress.Items.Add(item);
    }

    private string ConvertSpeedtoString(long speed)
    {
      switch (speed)
      {
        case 10000000:
          return "10 MB";
        case 11000000:
          return "11 MB";
        case 54000000:
          return "54 MB";
        case 100000000:
          return "100 MB";
        case 1000000000:
          return "1 GB";
        default:
          return speed.ToString(NumberFormatInfo.CurrentInfo);
      }
    }

    private void cboInterfaces_SelectedIndexChanged(object sender, EventArgs e)
    {
      selectedInterface = interfaces[cboInterfaces.SelectedIndex];
      UpdateNetworkInformation();
    }

    private void timer1_Tick(object sender, EventArgs e)
    {
      UpdateNetworkStatistics();
    }

    // 自訂當網路介面卡的IP位址變更時所呼叫的方法
    private void NetworkAddressChangedCallback(object sender, EventArgs e)
    {
      ShowNetworkInterfaces();
    }

    // 自訂當網路的有效性變更時所呼叫的方法
    private void NetworkAvailabilityChangedCallback(object sender, NetworkAvailabilityEventArgs e)
    {
      // 取得目前網路的連線狀態
      if (e.IsAvailable)
        StatusBar.Text = "Network interface is up.";
      else
        StatusBar.Text = "The network is not available.";
    }
  }
}