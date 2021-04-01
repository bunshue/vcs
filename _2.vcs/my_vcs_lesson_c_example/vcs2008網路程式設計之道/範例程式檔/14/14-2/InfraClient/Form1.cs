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

namespace InfraClient
{
  public partial class Form1 : Form
  {
    System.Net.Sockets.IrDAClient irdaClient = null;
    System.Net.Sockets.IrDADeviceInfo[] irdaDevice = null;

    System.Net.IrDAEndPoint remoteEP = null;

    // 定義服務名稱
    string servicename = "IrDAServer";

    public Form1()
    {
      InitializeComponent();
    }

    private void Form1_Load(object sender, EventArgs e)
    {
      btnConnect.Enabled = false;

      // 建立紅外線用戶端
      irdaClient = new IrDAClient();
    }

    private void btnDevice_Click(object sender, EventArgs e)
    {
      // 取得Pocket PC、Smart Phone或WinCE所裝設的紅外線裝置
      irdaDevice = irdaClient.DiscoverDevices(3);

      // 若無紅外線裝置
      if (irdaDevice.Length == 0)
      {
        btnConnect.Enabled = false;

        MessageBox.Show("No infrared device found.", "Infrared Client", MessageBoxButtons.OK, MessageBoxIcon.Hand, MessageBoxDefaultButton.Button1);
        return;
      }
      else
      {
        btnConnect.Enabled = true;

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

          item = deviceID.ToString() + " " + deviceName + " " + device.CharacterSet + " " + device.Hints;

          cboDevices.Items.Add(item);
        }

        cboDevices.SelectedIndex = 0;
      }
    }

    private void btnConnect_Click(object sender, EventArgs e)
    {
      Stream iostream = null;

      try
      {
        int i = cboDevices.SelectedIndex;

        // 設定紅外線通訊裝置及其服務名稱
        remoteEP = new IrDAEndPoint(irdaDevice[i].DeviceID, servicename);

        // 連結至紅外線伺服端
        irdaClient.Connect(remoteEP);

        // 取得伺服端的通訊裝置名稱
        StatusBar.Text = "Remote: " + irdaClient.RemoteMachineName;
      }
      catch (Exception ex)
      {
        Console.WriteLine(ex.StackTrace.ToString());

        MessageBox.Show("Can not connect to the IrDA Listener.", "Infrared Client", MessageBoxButtons.OK, MessageBoxIcon.Hand, MessageBoxDefaultButton.Button1);
      }

      try
      {
        // 取得用戶端的輸出入串流
        iostream = irdaClient.GetStream();

        // 判斷串流是否支援寫入功能
        if (iostream.CanWrite)
        {
          byte[] msg = Encoding.ASCII.GetBytes("Message from Infrared Client");

          iostream.Write(msg, 0, msg.Length);
        }

        // 判斷串流是否支援讀取功能
        if (iostream.CanRead)
        {
          byte[] bytes = new byte[iostream.Length];

          iostream.Read(bytes, 0, (int)iostream.Length);

          txtMessage.Text = txtMessage.Text + Encoding.ASCII.GetString(bytes, 0, bytes.Length) + "\r\n";
        }

        iostream.Close();
      }
      catch (Exception ex)
      {
        Console.WriteLine(ex.StackTrace.ToString());

        if (iostream != null)
          iostream.Close();

        if (irdaClient != null)
          irdaClient.Close();
      }

      try
      {
        if (irdaClient != null)
          irdaClient.Close();
      }
      catch (Exception ex)
      {
        Console.WriteLine(ex.StackTrace.ToString());
      }
    }

    private void mnuExit_Click(object sender, EventArgs e)
    {
      DialogResult result = MessageBox.Show("Are you sure to quit?", "Infrared Client", MessageBoxButtons.YesNo, MessageBoxIcon.Question, MessageBoxDefaultButton.Button1);

      if (result == DialogResult.Yes)
      {
        try
        {
          if (irdaClient != null)
            irdaClient.Close();
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