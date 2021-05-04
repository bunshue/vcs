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

        // ���ջP�l����A���إ߳s��
        smtpClient.Connect(strHost, Int32.Parse(strPort));

        // �إ߿�X�J��Ƭy
        networkStream = smtpClient.GetStream();

        // �l����A���^�� 220 Ready �T��
        if (!SMTPResponse("220"))
          return;
      }
      catch (Exception ex)
      {
        lstLog.Items.Add("Socket: " + ex.ToString());
      }

      try
      {
        // Client�ݵo�X HELO <Mail Server> �T���H�^���l����A��
        msg = "HELO " + strHost + "\r\n";
        if (!SMTPSend(msg))
        {
          return;
        }
        // �l����A���^�� 250 OK �T��
        if (!SMTPResponse("250"))
        {
          return;
        }

        // Client�ݵo�X MAIL FROM�G<�H���E-Mail Address> �T��
        // �D�n�@�Φb��@����������~�o�ͩζl��^�����ͮ�
        // �|�ǩ���E-Mail Address
        msg = "MAIL FROM: " + strFrom + "\r\n";
        if (!SMTPSend(msg))
        {
          return;
        }
        // �Y�H��� E-Mail Address ���T�A�l����A���|�^�� 250 OK �T��
        // �_�h�|�^�� 550 No such user ���T��
        if (!SMTPResponse("250"))
        {
          return;
        }

        string[] strArray = strTo.Split(",".ToCharArray());

        for (int i = 0; i < strArray.Length; i++)
        {
          if (strArray[i].Trim().ToString() != "")
          {
            // Client�ݵo�X RCPT TO�G<�����E-Mail Address> ���O
            // �H�N����̤�E-Mail Address
            msg = "RCPT TO: " + strArray[i].Trim().ToString() + "\r\n";

            if (!SMTPSend(msg))
            {
              return;
            }
            // �Y�����E-Mail Address���T�A�l����A���|�^��250 OK�T��
            // �_�h�|�^��550 No such user���T��
            if (!SMTPResponse("250"))
            {
              return;
            }
          }
        }

        // �}�l�B�z�l����D�Τ��e�AClient�ݶǰe DATA ���O
        // �H�i���l����A�����ۭn�}�l�ǰe�l����D�Τ��e
        msg = "DATA" + "\r\n";

        if (!SMTPSend(msg))
        {
          return;
        }
        // �Y���T�h�l����A���|�^��354 Start mail input���T��
        if (!SMTPResponse("354"))
        {
          return;
        }

        // �ǰe�l����D (Date) �A�C�@�涷�H<CR><LF>�]�����k��\r\n�^����
        string strDate = DateTime.Now.ToShortDateString() + " " + DateTime.Now.ToLongTimeString();
        msg = "Date: " + strDate + "\r\n";
        if (!SMTPSend(msg))
        {
          return;
        }

        // �ǰe�l����D (From) 
        msg = "From: " + strFrom + "\r\n";
        if (!SMTPSend(msg))
        {
          return;
        }

        // �ǰe�l����D (To) 
        msg = "To: " + strTo + "\r\n";
        if (!SMTPSend(msg))
        {
          return;
        }

        // �ǰe�l����D (Subject) 
        msg = "Subject: " + strSubject + "\r\n" + "\r\n";
        if (!SMTPSend(msg))
        {
          return;
        }

        // �ǰe�l�󤺮e
        msg = strMsg + "\r\n";
        if (!SMTPSend(msg))
        {
          return;
        }

        // �ǰe�k��B����B�y�I�B�k��B����r��A�h<CR><LF>.<CR><LF>
        // �H�N��l�󤺮e�ǰe����
        msg = "\r\n" + "." + "\r\n";
        if (!SMTPSend(msg))
        {
          return;
        }
        // �l����A���|�^��250 OK�T���A�N���\�ǰe
        if (!SMTPResponse("250"))
        {
          return;
        }

        // Client�ݵo�X QUIT ���O�A�H�n�D�����q�T�s��
        msg = "QUIT" + "\r\n";
        if (!SMTPSend(msg))
        {
          return;
        }
        // �l����A���^�� 221 Service closing transmission channel �T��
        // �H��ܵ���
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

    // �B�z�Τ�ݶǰe�T���ܶl����A��
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

    // �B�z�l����A���^�ǰT���ܥΤ��
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