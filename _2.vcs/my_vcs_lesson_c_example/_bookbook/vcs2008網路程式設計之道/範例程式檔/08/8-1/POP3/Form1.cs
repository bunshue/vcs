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
using System.Collections;

namespace POP3
{
  public partial class Form1 : Form
  {
    private Socket pop3Socket = new System.Net.Sockets.Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);

    private int totalMail, currentMail, mailSize;

    public Form1()
    {
      InitializeComponent();
    }

    private void Form1_Load(object sender, EventArgs e)
    {
      txtMessage.Clear();
      lstLog.Items.Clear();

      btnPrevious.Enabled = false;
      btnNext.Enabled = false;
    }

    private void mnuExit_Click(object sender, EventArgs e)
    {
      DialogResult result = MessageBox.Show("Are you sure to quit?", "POP3 Client", MessageBoxButtons.YesNo, MessageBoxIcon.Question, MessageBoxDefaultButton.Button1);

      if (result == DialogResult.Yes)
      {
        try
        {
          if (pop3Socket.Connected)
          {
            pop3Socket.Shutdown(SocketShutdown.Both);
            pop3Socket.Close();
          }
        }
        catch (Exception) { }

        this.Close();
      }
    }

    private void ToolBar1_ButtonClick(object sender, ToolBarButtonClickEventArgs e)
    {
      bool flag;

      switch (ToolBar1.Buttons.IndexOf(e.Button))
      {
        case 0:
          // Receive
          try
          {
            if (receiveMail())
            {
              if (totalMail > 0)
              {
                currentMail = 1;

                flag = showMail(currentMail);
                showObject(true);
              }
              else
                MessageBox.Show("There is no mail.", "POP3", MessageBoxButtons.OK, MessageBoxIcon.Warning, MessageBoxDefaultButton.Button1);
            }
            else
              showObject(false);
          }
          catch (Exception ex)
          {
            lstLog.Items.Add("Socket: " + ex.ToString());
          }

          break;

        case 1:
          // Previous Mail
          currentMail = currentMail - 1;

          if (currentMail <= 1)
            currentMail = 1;

          if (!showMail(currentMail))
            currentMail = currentMail + 1;

          showObject(true);

          break;

        case 2:
          // Next Mail
          currentMail = currentMail + 1;

          if (currentMail >= totalMail)
            currentMail = totalMail;

          if (!showMail(currentMail))
            currentMail = currentMail - 1;

          showObject(true);

          break;

        case 3:
          // Clear
          txtMessage.Clear();
          lstLog.Items.Clear();
          break;
      }
    }
    private void showObject(bool flag)
    {
      if (flag)
      {
        btnReceive.Enabled = false;

        if ((totalMail > 1) && (currentMail == 1))
        {
          btnPrevious.Enabled = false;
          btnNext.Enabled = true;
        }
        else if ((currentMail < totalMail) && (currentMail > 1))
        {
          btnPrevious.Enabled = true;
          btnNext.Enabled = true;
        }
        else if ((currentMail == totalMail) && (currentMail > 1))
        {
          btnPrevious.Enabled = true;
          btnNext.Enabled = false;
        }
      }
      else
      {
        btnPrevious.Enabled = false;
        btnNext.Enabled = false;
        btnReceive.Enabled = true;

        txtMessage.Clear();
        lstLog.Items.Clear();
      }
    }

    private bool receiveMail()
    {
      IPAddress IPAdd;
      IPEndPoint IPEndAdd;
      string strHost, strPort, strUser, strPass, strMsg;
      string strResponse = "";
      byte[] RecvBytes = new byte[256];
      int bytes;

      strHost = txtHost.Text;
      strPort = txtPort.Text;
      strUser = txtLogin.Text;
      strPass = txtPass.Text;

      lstLog.Items.Clear();

      try
      {
        lstLog.Items.Add("C: Trying to connect to host " + strHost + ", port: " + strPort);

        IPAdd = Dns.Resolve(strHost).AddressList[0];
        IPEndAdd = new System.Net.IPEndPoint(IPAdd, Int32.Parse(strPort));

        // 嘗試與郵件伺服器建立連結
        pop3Socket.Connect(IPEndAdd);

        if (!pop3Socket.Connected)
        {
          lstLog.Items.Add("Unable to connect to " + strHost + ":" + strPort);
          return (false);
        }

        // 郵件伺服器回傳 +OK hello from popgate 訊息?
        if (!POP3Response())
          return (false);

        // USER
        strMsg = "USER " + strUser;
        if (!POP3Request(strMsg))
          return (false);

        // 郵件伺服器回傳 +OK password required 訊息?
        if (!POP3Response())
          return (false);

        // PASS
        strMsg = "PASS " + strPass;
        if (!POP3Request(strMsg))
          return (false);

        // 郵件伺服器回傳 +OK maildrop ready, .. messages 訊息?
        if (!POP3Response())
          return (false);

        // STAT
        strMsg = "STAT";
        if (!POP3Request(strMsg))
          return (false);

        // 郵件伺服器回傳 +OK <# of Mail> <Mail Size>
        bytes = pop3Socket.Receive(RecvBytes, RecvBytes.Length, 0);
        strResponse = Encoding.ASCII.GetString(RecvBytes, 0, bytes);
        lstLog.Items.Add("S: " + strResponse.ToString());

        if (!strResponse.StartsWith("+OK"))
        {
          MessageBox.Show(strResponse.ToString(), "POP3 Error", MessageBoxButtons.OK, MessageBoxIcon.Warning, MessageBoxDefaultButton.Button1);
          return (false);
        }

        // +OK <#> <Size>
        string[] strTemp = strResponse.Split(" ".ToCharArray());

        totalMail = Int32.Parse(strTemp[1].Trim().ToString());
        mailSize = Int32.Parse(strTemp[2].Trim().ToString());

        return (true);
      }
      catch (Exception ex)
      {
        lstLog.Items.Add(ex.ToString());
        pop3Socket.Shutdown(SocketShutdown.Both);
        pop3Socket.Close();
        return (false);
      }
    }

    private bool showMail(int mailNo)
    {
      string strResponse, strMsg;
      string strContent = "";
      byte[] RecvBytes = new byte[256];
      int bytes;
      bool blnFlag = true;

      try
      {
        strMsg = "RETR " + mailNo;

        if (!POP3Request(strMsg))
          return (false);

        do
        {
          bytes = pop3Socket.Receive(RecvBytes, RecvBytes.Length, 0);

          if (bytes > 0)
          {
            strResponse = Encoding.ASCII.GetString(RecvBytes, 0, bytes);

            if (blnFlag)
            {
              if (!strResponse.StartsWith("+OK"))
              {
                MessageBox.Show(strResponse.ToString(), "POP3 Error", MessageBoxButtons.OK, MessageBoxIcon.Warning, MessageBoxDefaultButton.Button1);
                return (false);
                //break;
              }
              blnFlag = false;
            }

            strContent = strContent + strResponse;

            if (strContent.Trim().EndsWith("."))
              break;
          }
          else
            break;
        }
        while (true);

        txtMessage.Text = strContent;

        Label1.Text = "Total: " + totalMail + " (Size: " + mailSize + ") Current: " + mailNo;

        return (true);
      }
      catch (Exception ex)
      {
        lstLog.Items.Add(ex.ToString());
        return (false);
      }
    }

    private bool POP3Response()
    {
      byte[] RecvBytes = new byte[256];
      string strResponse = "";
      int bytes;

      try
      {
        bytes = pop3Socket.Receive(RecvBytes, RecvBytes.Length, 0);
        strResponse = Encoding.ASCII.GetString(RecvBytes, 0, bytes);
        lstLog.Items.Add("S: " + strResponse.ToString());

        if (!strResponse.StartsWith("+OK"))
        {
          lstLog.Items.Add("POP3Response Error.");
          pop3Socket.Shutdown(SocketShutdown.Both);
          pop3Socket.Close();
          return (false);
        }
        else
          return (true);
      }
      catch (Exception ex)
      {
        lstLog.Items.Add("POP3Response Error: " + ex.ToString());
        pop3Socket.Shutdown(SocketShutdown.Both);
        pop3Socket.Close();
        return (false);
      }
    }

    private bool POP3Request(string strMsg)
    {
      byte[] byteMsg;

      strMsg = strMsg + "\r\n";

      try
      {
        byteMsg = Encoding.ASCII.GetBytes(strMsg.ToCharArray());
        pop3Socket.Send(byteMsg, byteMsg.Length, SocketFlags.None);
        lstLog.Items.Add("C: " + strMsg.ToString());
        return (true);
      }
      catch (Exception ex)
      {
        lstLog.Items.Add("POP3Request Error: " + ex.ToString());
        pop3Socket.Shutdown(SocketShutdown.Both);
        pop3Socket.Close();
        return (false);
      }
    }
  }
}