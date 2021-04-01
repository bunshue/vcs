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

    // �w�q�A�ȦW��
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

      // ���oPocket PC�BSmart Phone��WinCE�Ҹ˳]�����~�u�˸m
      irdaDevice = irdaClient.DiscoverDevices(3);

      // �Y�L���~�u�˸m
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

        // ��ܬ��~�u�˸m
        foreach (IrDADeviceInfo device in irdaDevice)
        {
          // ���o���~�u�˸m���ѧOID
          deviceID = BitConverter.ToInt32(device.DeviceID, 0);
          // ���o���~�u�˸m���W��
          deviceName = device.DeviceName;
          // ���o���~�u���A�ݩҨϥΪ��r���s�X�P�˸m���y�z
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

        // �]�w���~�u���A�ݤ��q�T�˸m�Ψ�A�ȦW��
        irdaEP = new IrDAEndPoint(irdaDevice[i].DeviceID, servicename);

        // �إ߬��~�u���A��
        irdaListener = new IrDAListener(irdaEP);

        // �}�l��ť���Ԭ��~�u�Τ�ݪ��s���ШD
        irdaListener.Start();

        // ���o���~�u���A�ݬ�������T
        IrDAEndPoint serverInfo = irdaListener.LocalEndpoint;

        int deviceID = BitConverter.ToInt32(serverInfo.DeviceID, 0);

        StatusBar.Text = "IrDA Device: " + deviceID.ToString();

        ListenClient lc = new ListenClient(irdaListener, this);
        // �����
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