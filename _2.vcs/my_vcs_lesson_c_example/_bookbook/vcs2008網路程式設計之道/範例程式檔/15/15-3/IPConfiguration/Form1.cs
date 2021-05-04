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
      // ���o�����q���W�Ҧ����������d����T
      interfaces = NetworkInterface.GetAllNetworkInterfaces();

      // �P�_�����q�������������d�O�_�������s�u
      if (NetworkInterface.GetIsNetworkAvailable())
        StatusBar.Text = "Network interface is up.";
      else
        StatusBar.Text = "The network is not available.";

      ShowNetworkInterfaces();
    }

    private void cboInterfaces_SelectedIndexChanged(object sender, EventArgs e)
    {
      selectedInterface = interfaces[cboInterfaces.SelectedIndex];
      UpdateNetworkInformation();
      UpdateNetworkStatistics();
    }

    private void ShowNetworkInterfaces()
    {
      cboInterfaces.Items.Clear();

      // ���o�����q���W�Ҧ����������d����T
      interfaces = NetworkInterface.GetAllNetworkInterfaces();

      if (interfaces.Length == 0)
        cboInterfaces.Items.Add("No network interface is found.");
      else
      {
        foreach (NetworkInterface adapter in interfaces)
          // ���o���������d���y�z�]�A�t�ӡB�����B�ӼФΫ���
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

      // ���o�����q���䴩IPv4�q�T��w�����������d���έp���
      IPv4InterfaceStatistics ipv4Statistics = selectedInterface.GetIPv4Statistics();

      // ���o�䴩IP�q�T��w�����������d��������T
      IPInterfaceProperties ipProperties = selectedInterface.GetIPProperties();

      NumberFormatInfo numberFormat = NumberFormatInfo.CurrentInfo;

      // DNS���X
      listItem[0] = "DNS���X";
      listItem[1] = ipProperties.DnsSuffix.ToString();
      item = new ListViewItem(listItem);
      lstInformation.Items.Add(item);

      // ���o���������d�ұ������줸�ռƥ�
      long received = ipv4Statistics.BytesReceived / 1024;
      listItem[0] = "�����d�ұ������줸�ռƥ�";
      listItem[1] = received.ToString("N0", numberFormat) + " KB";
      item = new ListViewItem(listItem);
      lstInformation.Items.Add(item);

      // ���o���������d�Ҷǰe���줸�ռƥ�
      long sent = ipv4Statistics.BytesSent / 1024;
      listItem[0] = "�����d�Ҷǰe���줸�ռƥ�";
      listItem[1] = sent.ToString("N0", numberFormat) + " KB";
      item = new ListViewItem(listItem);
      lstInformation.Items.Add(item);

      // ���o���������d���t��
      listItem[0] = "�����d���t��";
      listItem[1] = ConvertSpeedtoString(selectedInterface.Speed);
      item = new ListViewItem(listItem);
      lstInformation.Items.Add(item);

      // ���o���������d�ثe�����A�A��OperationalStatus���C�|��
      listItem[0] = "�����d�ثe�����A";
      listItem[1] = selectedInterface.OperationalStatus.ToString();
      item = new ListViewItem(listItem);
      lstInformation.Items.Add(item);

      // �P�_���������d�O�_�����h�I���e�ʥ]
      listItem[0] = "�O�_�����h�I���e�ʥ]";
      listItem[1] = selectedInterface.SupportsMulticast.ToString();
      item = new ListViewItem(listItem);
      lstInformation.Items.Add(item);
    }

    private void UpdateNetworkInformation()
    {
      lstAddress.Items.Clear();

      // ���o�䴩IP�q�T��w�����������d��������T
      IPInterfaceProperties ipProperties = selectedInterface.GetIPProperties();

      // ���oDHCP���A����}
      IPAddressCollection ipAddresses = ipProperties.DhcpServerAddresses;
      foreach (IPAddress ipAddress in ipAddresses)
        addIPAddress("DHCP���A��", ipAddress);

      // ���o���������d�ҳ]�w��DNS���A����}
      ipAddresses = ipProperties.DnsAddresses;
      foreach (IPAddress ipAddress in ipAddresses)
        addIPAddress("DNS���A��", ipAddress);

      // ���oWINS���A������}
      ipAddresses = ipProperties.WinsServersAddresses;
      foreach (IPAddress ipAddress in ipAddresses)
        addIPAddress("WINS���A��", ipAddress);

      // ���o���������d�������h�D��}
      GatewayIPAddressInformationCollection gatewayInfo = ipProperties.GatewayAddresses;
      foreach (GatewayIPAddressInformation info in gatewayInfo)
        addIPAddress("�����h�D", info.Address);

      // ���o���������d��Anycast IP��}
      IPAddressInformationCollection anycastInfo = ipProperties.AnycastAddresses;
      foreach (IPAddressInformation info in anycastInfo)
        addIPAddress("Anycast", info.Address);

      // ���o���������d���h�I���e��}
      MulticastIPAddressInformationCollection multicastInfo = ipProperties.MulticastAddresses;
      foreach (MulticastIPAddressInformation info in multicastInfo)
        addIPAddress("�h�I���e", info.Address);

      // ���o���������d�����I�ǰe��}
      UnicastIPAddressInformationCollection unicastInfo = ipProperties.UnicastAddresses;
      foreach (UnicastIPAddressInformation info in unicastInfo)
        addIPAddress("���I�ǰe", info.Address);
    }

    private void addIPAddress(string type, IPAddress ipAddress)
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
  }
}