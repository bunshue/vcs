using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Net.Sockets;
using System.IO;
using System.Threading;

namespace InfraServer
{
  public partial class Form1 : Form
  {
    System.Net.Sockets.IrDAListener irdaListener = null;
    System.Net.Sockets.IrDAClient irdaClient = null;
    System.Net.Sockets.IrDADeviceInfo[] irdaDevice = null;

    System.Net.IrDAEndPoint irdaEP = null;

    // 定義服務名稱
    string servicename = "IrDAServer";

    public Form1()
    {
      InitializeComponent();
    }

    private void Form1_Load(object sender, EventArgs e)
    {
      btnListen.Enabled = false;
    }

    private void btnDevice_Click(object sender, EventArgs e)
    {
      irdaClient = new IrDAClient();

      // 取得Pocket PC、Smart Phone或WinCE所裝設的紅外線裝置
      irdaDevice = irdaClient.DiscoverDevices(3);

      // 若無紅外線裝置
      if (irdaDevice.Length == 0)
      {
        btnListen.Enabled = false;

        MessageBox.Show("No infrared device found.", "Infrared Server", MessageBoxButtons.OK, MessageBoxIcon.Hand, MessageBoxDefaultButton.Button1);
        return;
      }
      else
      {
        btnListen.Enabled = true;

        int deviceID;
        string deviceName;
        string item;

        cboDevices.Items.Clear();

        // 顯示紅外線裝置
        foreach (IrDADeviceInfo device in irdaDevice)
        {
          // 取得紅外線裝置之識別ID
          deviceID = BitConverter.ToInt32(device.DeviceID, 0);
          // 取得紅外線裝置之名稱
          deviceName = device.DeviceName;
          // 取得紅外線伺服端所使用的字元編碼與裝置之描述
          item = deviceID.ToString() + " " + deviceName + " " + device.CharacterSet + " " + device.Hints;

          cboDevices.Items.Add(item);
        }

        cboDevices.SelectedIndex = 0;
      }
    }

    private void btnListen_Click(object sender, EventArgs e)
    {
      try
      {
        int i = cboDevices.SelectedIndex;

        // 設定紅外線伺服端之通訊裝置及其服務名稱
        irdaEP = new IrDAEndPoint(irdaDevice[i].DeviceID, servicename);

        // 建立紅外線伺服端
        irdaListener = new IrDAListener(irdaEP);

        // 開始接聽等候紅外線用戶端的連結請求
        irdaListener.Start();

        // 取得紅外線伺服端相關的資訊
        IrDAEndPoint serverInfo = irdaListener.LocalEndpoint;

        int deviceID = BitConverter.ToInt32(serverInfo.DeviceID, 0);

        StatusBar.Text = "IrDA Device: " + deviceID.ToString();

        ListenClient lc = new ListenClient(irdaListener, this);
        // 執行緒
        ThreadStart serverThreadStart = new ThreadStart(lc.ServerThreadProc);
        Thread serverthread = new Thread(serverThreadStart);

        serverthread.Start();
      }
      catch (Exception ex)
      {
        Console.WriteLine(ex.StackTrace.ToString());

        MessageBox.Show("Can not start the IrDA Listener.", "Infrared Server", MessageBoxButtons.OK, MessageBoxIcon.Hand, MessageBoxDefaultButton.Button1);
      }
    }

    private void mnuExit_Click(object sender, EventArgs e)
    {
      DialogResult result = MessageBox.Show("Are you sure to quit?", "Infrared Server", MessageBoxButtons.YesNo, MessageBoxIcon.Question, MessageBoxDefaultButton.Button1);

      if (result == DialogResult.Yes)
      {
        try
        {
          if (irdaListener != null)
            irdaListener.Stop();
        }
        catch (Exception ex)
        {
          Console.WriteLine(ex.StackTrace.ToString());
        }

        this.Close();
      }
    }
  }
}