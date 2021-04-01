using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;

// Remoting Channel
using System.Runtime.Remoting;
using System.Runtime.Remoting.Channels;
using System.Runtime.Remoting.Channels.Http;

namespace RemoteDesktop
{
  public partial class MainForm : Form
  {
    System.Runtime.Remoting.Channels.Http.HttpChannel httpchannel;

    // 自定類別
    RemoteControl remotecontrol = null;

    public bool connected = false;

    public MainForm()
    {
      InitializeComponent();
    }

    private void mnuSlaveStart_Click(object sender, EventArgs e)
    {
      try
      {
        // 以指定連接埠的伺服器Channel建立HttpChannel物件
        httpchannel = new System.Runtime.Remoting.Channels.Http.HttpChannel(8080);

        // 註冊Channel服務的Channel通道
        System.Runtime.Remoting.Channels.ChannelServices.RegisterChannel(httpchannel, false);

        // 設定Channel組態
        System.Runtime.Remoting.WellKnownServiceTypeEntry entry =
            new WellKnownServiceTypeEntry(typeof(RemoteControl), "RemoteSlave", WellKnownObjectMode.SingleCall);

        // 在服務端登錄提供服務之物件
        System.Runtime.Remoting.RemotingConfiguration.RegisterWellKnownServiceType(entry);

        timer1.Enabled = false;
        this.notifyIcon1.ContextMenu = this.contextMenu1;
        this.notifyIcon1.Visible = true;
        this.Visible = false;

        this.mnuSlaveStart.Enabled = false;
        this.mnuSlaveStop.Enabled = true;
      }
      catch (Exception ex)
      {
        stop();
        this.mnuSlaveStart.Enabled = true;
        this.mnuSlaveStop.Enabled = false;
        Console.WriteLine(ex.StackTrace.ToString());
      }
    }

    private void mnuSlaveStop_Click(object sender, EventArgs e)
    {
      stop();
      this.mnuView.Visible = false;
      this.mnuView.Enabled = false;
      this.mnuSlaveStart.Enabled = true;
      this.mnuSlaveStop.Enabled = false;
      this.FormBorderStyle = FormBorderStyle.Sizable;
      this.WindowState = FormWindowState.Normal;
      this.Width = 640;
      this.Height = 480;
    }

    private void mnuSlaveStop1_Click(object sender, EventArgs e)
    {
      stop();

      this.mnuView.Visible = false;
      this.mnuView.Enabled = false;
      this.mnuSlaveStart.Enabled = true;
      this.mnuSlaveStop.Enabled = false;
      this.WindowState = FormWindowState.Normal;
      this.Width = 640;
      this.Height = 480;
      this.notifyIcon1.Visible = false;
      this.Visible = true;
    }
    
    private void mnuMasterStart_Click(object sender, EventArgs e)
    {
      start();
    }

    private void mnuMasterStop_Click(object sender, EventArgs e)
    {
      stop();

      desktopPicture.Image = null;

      this.mnuView.Visible = false;
      this.mnuView.Enabled = false;
      this.mnuMasterStart.Enabled = true;
      this.mnuMasterStop.Enabled = false;
      this.FormBorderStyle = FormBorderStyle.Sizable;
      this.WindowState = FormWindowState.Normal;
      this.Width = 640;
      this.Height = 480;
    }

    private void mnuNormal_Click(object sender, EventArgs e)
    {
      this.FormBorderStyle = FormBorderStyle.Sizable;
      this.WindowState = FormWindowState.Normal;
      this.Width = 640;
      this.Height = 480;
    }

    private void mnuFull_Click(object sender, EventArgs e)
    {
      this.FormBorderStyle = FormBorderStyle.None;
      this.WindowState = FormWindowState.Maximized;
    }

    private void mnuExit_Click(object sender, EventArgs e)
    {
      DialogResult result = MessageBox.Show("Are you sure to quit?", "Remote Desktop", MessageBoxButtons.YesNo, MessageBoxIcon.Question, MessageBoxDefaultButton.Button1);

      if (result == DialogResult.Yes)
      {
        stop();
        this.Close();
      }
    }

    private void start()
    {
      frmHost form = new frmHost();

      if (form.ShowDialog(this) == DialogResult.OK)
      {
        string remotehost = form.Host;

        if (remotehost.Length != 0)
        {
          try
          {
            string url = "http://" + remotehost + ":8080/RemoteSlave";

            // 建立HttpChannel物件
            httpchannel = new System.Runtime.Remoting.Channels.Http.HttpChannel();

            // 註冊Channel服務的Channel通道
            System.Runtime.Remoting.Channels.ChannelServices.RegisterChannel(httpchannel, false);

            // 以指定物件和URL建立Proxy
            remotecontrol = (RemoteControl)System.Activator.GetObject(typeof(RemoteControl), url);

            this.connected = true;
            timer1.Enabled = true;

            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;

            this.mnuView.Visible = true;
            this.mnuView.Enabled = true;

            this.mnuMasterStart.Enabled = false;
            this.mnuMasterStop.Enabled = true;
          }
          catch (Exception ex)
          {
            stop();
            this.mnuMasterStart.Enabled = true;
            this.mnuMasterStop.Enabled = false;
            Console.WriteLine(ex.StackTrace.ToString());
          }
        }
        else
          MessageBox.Show("請輸入被控端之IP位址或DNS主機名稱.", "Remote Desktop", MessageBoxButtons.OK, MessageBoxIcon.Error);
      }
    }

    private void stop()
    {
      try
      {
        timer1.Enabled = false;
        connected = false;

        this.WindowState = FormWindowState.Normal;
        this.Width = 640;
        this.Height = 480;

        // 移除登錄之Channel
        ChannelServices.UnregisterChannel(httpchannel);
      }
      catch (Exception ex)
      {
        Console.WriteLine(ex.StackTrace.ToString());
      }
    }

    private void MainForm_FormClosing(object sender, FormClosingEventArgs e)
    {
      stop();
    }

    private void timer1_Tick(object sender, EventArgs e)
    {
      try
      {
        // 取得螢幕之位元組陣列
        byte[] buffer = remotecontrol.GetDesktopBuffer();

        // 建立記憶體的資料流
        System.IO.MemoryStream memStream = new MemoryStream(buffer);

        // 從指定的資料流建立Image物件
        desktopPicture.Image = System.Drawing.Image.FromStream(memStream);
      }
      catch (Exception ex)
      {
        stop();
        Console.WriteLine(ex.StackTrace.ToString());
      }
    }

    private void desktopPicture_MouseDown(object sender, MouseEventArgs e)
    {
      if (connected == true)
        remotecontrol.MouseButtonCall(true, e.Button == MouseButtons.Left, e.X, e.Y);
    }

    private void desktopPicture_MouseUp(object sender, MouseEventArgs e)
    {
      if (connected == true)
        remotecontrol.MouseButtonCall(false, e.Button == MouseButtons.Left, e.X, e.Y);
    }

    private void desktopPicture_MouseMove(object sender, MouseEventArgs e)
    {
      if (connected == true)
        remotecontrol.MoveMouse(e.X, e.Y);
    }
  }
}