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

    // �w�q�A�ȦW��
    string servicename = "IrDAServer";

    public Form1()
    {
      InitializeComponent();
    }

    private void Form1_Load(object sender, EventArgs e)
    {
      btnConnect.Enabled = false;

      // �إ߬��~�u�Τ��
      irdaClient = new IrDAClient();
    }

    private void btnDevice_Click(object sender, EventArgs e)
    {
      // ���oPocket PC�BSmart Phone��WinCE�Ҹ˳]�����~�u�˸m
      irdaDevice = irdaClient.DiscoverDevices(3);

      // �Y�L���~�u�˸m
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

        // ��ܬ��~�u�˸m
        foreach (IrDADeviceInfo device in irdaDevice)
        {
          // ���o���~�u�˸m���ѧOID
          deviceID = BitConverter.ToInt32(device.DeviceID, 0);
          // ���o���~�u�˸m���W��
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

        // �]�w���~�u�q�T�˸m�Ψ�A�ȦW��
        remoteEP = new IrDAEndPoint(irdaDevice[i].DeviceID, servicename);

        // �s���ܬ��~�u���A��
        irdaClient.Connect(remoteEP);

        // ���o���A�ݪ��q�T�˸m�W��
        StatusBar.Text = "Remote: " + irdaClient.RemoteMachineName;
      }
      catch (Exception ex)
      {
        Console.WriteLine(ex.StackTrace.ToString());

        MessageBox.Show("Can not connect to the IrDA Listener.", "Infrared Client", MessageBoxButtons.OK, MessageBoxIcon.Hand, MessageBoxDefaultButton.Button1);
      }

      try
      {
        // ���o�Τ�ݪ���X�J��y
        iostream = irdaClient.GetStream();

        // �P�_��y�O�_�䴩�g�J�\��
        if (iostream.CanWrite)
        {
          byte[] msg = Encoding.ASCII.GetBytes("Message from Infrared Client");

          iostream.Write(msg, 0, msg.Length);
        }

        // �P�_��y�O�_�䴩Ū���\��
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