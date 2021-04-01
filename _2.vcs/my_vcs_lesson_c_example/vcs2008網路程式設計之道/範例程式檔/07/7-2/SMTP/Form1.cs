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

namespace SMTP
{
  public partial class Form1 : Form
  {
    private TcpClient smtpClient = new System.Net.Sockets.TcpClient();

    private Stream networkStream;

    public Form1()
    {
      InitializeComponent();
    }

    private void ToolBar1_ButtonClick(object sender, ToolBarButtonClickEventArgs e)
    {
      switch (ToolBar1.Buttons.IndexOf(e.Button))
      {
        case 0:
          // Send
          Thread mailThread = new Thread(new ThreadStart(ProcessMail));
          mailThread.Start();

          break;

        case 1:
          // Clear
          txtTo.Clear();
          txtSubject.Clear();
          txtMessage.Clear();
          lstLog.Items.Clear();
          break;
      }
    }

    private void ProcessMail()
    {
      string strHost, strPort, strFrom, strTo, strSubject, strMsg;
      string msg;

      strHost = txtHost.Text;
      strPort = txtPort.Text;
      strFrom = txtFrom.Text;
      strTo = txtTo.Text;
      strSubject = txtSubject.Text;
      strMsg = txtMessage.Text;

      lstLog.Items.Clear();

      try
      {
        // Connect to SMTP server
        lstLog.Items.Add("C: Trying to connect to host " + strHost + ", port: " + strPort);

        // 嘗試與郵件伺服器建立連結
        smtpClient.Connect(strHost, Int32.Parse(strPort));

        // 建立輸出入資料流
        networkStream = smtpClient.GetStream();

        // 郵件伺服器回傳 220 Ready 訊息
        if (!SMTPResponse("220"))
          return;
      }
      catch (Exception ex)
      {
        lstLog.Items.Add("Socket: " + ex.ToString());
      }

      try
      {
        // Client端發出 HELO <Mail Server> 訊息以回應郵件伺服器
        msg = "HELO " + strHost + "\r\n";
        if (!SMTPSend(msg))
        {
          return;
        }
        // 郵件伺服器回傳 250 OK 訊息
        if (!SMTPResponse("250"))
        {
          return;
        }

        // Client端發出 MAIL FROM：<寄件者E-Mail Address> 訊息
        // 主要作用在於一旦有任何錯誤發生或郵件回應產生時
        // 會傳往此E-Mail Address
        msg = "MAIL FROM: " + strFrom + "\r\n";
        if (!SMTPSend(msg))
        {
          return;
        }
        // 若寄件者 E-Mail Address 正確，郵件伺服器會回傳 250 OK 訊息
        // 否則會回傳 550 No such user 之訊息
        if (!SMTPResponse("250"))
        {
          return;
        }

        string[] strArray = strTo.Split(",".ToCharArray());

        for (int i = 0; i < strArray.Length; i++)
        {
          if (strArray[i].Trim().ToString() != "")
          {
            // Client端發出 RCPT TO：<收件者E-Mail Address> 指令
            // 以代表收件者之E-Mail Address
            msg = "RCPT TO: " + strArray[i].Trim().ToString() + "\r\n";

            if (!SMTPSend(msg))
            {
              return;
            }
            // 若收件者E-Mail Address正確，郵件伺服器會回傳250 OK訊息
            // 否則會回傳550 No such user之訊息
            if (!SMTPResponse("250"))
            {
              return;
            }
          }
        }

        // 開始處理郵件標題及內容，Client端傳送 DATA 指令
        // 以告知郵件伺服器接著要開始傳送郵件標題及內容
        msg = "DATA" + "\r\n";

        if (!SMTPSend(msg))
        {
          return;
        }
        // 若正確則郵件伺服器會回應354 Start mail input之訊息
        if (!SMTPResponse("354"))
        {
          return;
        }

        // 傳送郵件標題 (Date) ，每一行須以<CR><LF>（換行歸位\r\n）結尾
        string strDate = DateTime.Now.ToShortDateString() + " " + DateTime.Now.ToLongTimeString();
        msg = "Date: " + strDate + "\r\n";
        if (!SMTPSend(msg))
        {
          return;
        }

        // 傳送郵件標題 (From) 
        msg = "From: " + strFrom + "\r\n";
        if (!SMTPSend(msg))
        {
          return;
        }

        // 傳送郵件標題 (To) 
        msg = "To: " + strTo + "\r\n";
        if (!SMTPSend(msg))
        {
          return;
        }

        // 傳送郵件標題 (Subject) 
        msg = "Subject: " + strSubject + "\r\n" + "\r\n";
        if (!SMTPSend(msg))
        {
          return;
        }

        // 傳送郵件內容
        msg = strMsg + "\r\n";
        if (!SMTPSend(msg))
        {
          return;
        }

        // 傳送歸位、換行、句點、歸位、換行字串，則<CR><LF>.<CR><LF>
        // 以代表郵件內容傳送結束
        msg = "\r\n" + "." + "\r\n";
        if (!SMTPSend(msg))
        {
          return;
        }
        // 郵件伺服器會回傳250 OK訊息，代表成功傳送
        if (!SMTPResponse("250"))
        {
          return;
        }

        // Client端發出 QUIT 指令，以要求結束通訊連結
        msg = "QUIT" + "\r\n";
        if (!SMTPSend(msg))
        {
          return;
        }
        // 郵件伺服器回應 221 Service closing transmission channel 訊息
        // 以表示結束
        if (!SMTPResponse("221"))
        {
          return;
        }

        smtpClient.Close();
      }
      catch (Exception ex)
      {
        lstLog.Items.Add(ex.ToString());
      }
    }

    private void Form1_Load(object sender, System.EventArgs e)
    {
      txtTo.Clear();
      txtSubject.Clear();
      txtMessage.Clear();
      lstLog.Items.Clear();
    }

    private void mnuExit_Click(object sender, System.EventArgs e)
    {
      DialogResult result = MessageBox.Show("Are you sure to quit?", "SMTP Client", MessageBoxButtons.YesNo, MessageBoxIcon.Question, MessageBoxDefaultButton.Button1);

      if (result == DialogResult.Yes)
      {
        try
        {
          smtpClient.Close();
        }
        catch (Exception) { }

        this.Close();
      }
    }

    // 處理用戶端傳送訊息至郵件伺服器
    private bool SMTPSend(string strMsg)
    {
      byte[] byteMsg;

      try
      {
        lstLog.Items.Add("C: " + strMsg.ToString());

        byteMsg = Encoding.ASCII.GetBytes(strMsg.ToCharArray());

        networkStream.Write(byteMsg, 0, byteMsg.Length);

        return (true);
      }
      catch (Exception ex)
      {
        lstLog.Items.Add("SMTPSend Error: " + ex.ToString());

        smtpClient.Close();

        return (false);
      }
    }

    // 處理郵件伺服器回傳訊息至用戶端
    private bool SMTPResponse(string strEcho)
    {
      byte[] bytes = new byte[smtpClient.ReceiveBufferSize];
      string strResponse = "";

      try
      {
        networkStream.Read(bytes, 0, (int)smtpClient.ReceiveBufferSize);
        strResponse = Encoding.ASCII.GetString(bytes);

        lstLog.Items.Add("S: " + strResponse.ToString());

        if (!strResponse.StartsWith(strEcho))
        {
          lstLog.Items.Add("SMTPResponse Error.");

          smtpClient.Close();

          return (false);
        }
        else
        {
          return (true);
        }
      }
      catch (Exception ex)
      {
        lstLog.Items.Add("SMTPResponse Error: " + ex.ToString());

        smtpClient.Close();

        return (false);
      }
    }

    private void Form1_Resize(object sender, EventArgs e)
    {
      Control control = (Control)sender;

      txtTo.Location = new System.Drawing.Point(53, 7);
      txtTo.Size = new System.Drawing.Size(control.Size.Width - 72, 22);
      txtSubject.Location = new System.Drawing.Point(53, 35);
      txtSubject.Size = new System.Drawing.Size(control.Size.Width - 72, 22);
    }
  }
}