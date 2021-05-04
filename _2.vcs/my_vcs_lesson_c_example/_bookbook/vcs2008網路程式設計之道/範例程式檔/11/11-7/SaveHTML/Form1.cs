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

namespace SaveHTML
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    private void btnHTML_Click(object sender, EventArgs e)
    {
      IPAddress serverIP = Dns.GetHostEntry(txtURL.Text).AddressList[0];

      // Default Web Server Port = 80
      string Port = "80";
      IPEndPoint serverhost = new IPEndPoint(serverIP, Int32.Parse(Port));

      Socket clientSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);

      try
      {
        clientSocket.Connect(serverhost);

        if (!clientSocket.Connected)
        {
          MessageBox.Show("Connect Error.", "HTTP", MessageBoxButtons.OK, MessageBoxIcon.Error, MessageBoxDefaultButton.Button1);
          return;
        }

        string httpReq = "GET / HTTP/1.0" + "\r\n" + "\r\n";

        // �ǰeHTTP���D��T��Web Server
        clientSocket.Send(Encoding.ASCII.GetBytes(httpReq));

        byte[] buffer = new byte[1024];

        // �����^�Ǥ�HTML���D�κ������e�ܥΤ��
        int byteCount = clientSocket.Receive(buffer, buffer.Length, 0);

        txtHTML.Text = Encoding.ASCII.GetString(buffer, 0, byteCount);

        while (byteCount > 0)
        {
          byteCount = clientSocket.Receive(buffer, buffer.Length, 0);
          txtHTML.Text = txtHTML.Text + Encoding.ASCII.GetString(buffer, 0, byteCount);
        }
      }
      catch (Exception ex)
      {
        Console.WriteLine(ex.StackTrace.ToString());
      }
    }

    private void btnSave_Click(object sender, EventArgs e)
    {
      string filename = "";

      SaveFileDialog1.Title = "Save HTML";
      SaveFileDialog1.Filter = "All files (*.*)|*.*";

      if (SaveFileDialog1.ShowDialog() == DialogResult.OK)
      {
        filename = SaveFileDialog1.FileName;

        try
        {
          // �إ��ɮצ�y
          System.IO.FileStream fileStream = new FileStream(filename, FileMode.OpenOrCreate, FileAccess.Write);
          byte[] byteSave = Encoding.ASCII.GetBytes(txtHTML.Text.ToString());

          // �HFileStream���O��Write��k�NHTML���e�g�J�ɮפ�
          fileStream.Write(byteSave, 0, byteSave.Length);

          // �����ɮצ�y
          fileStream.Close();

          MessageBox.Show(filename + " has been save.", "HTTP Response", MessageBoxButtons.OK, MessageBoxIcon.Information, MessageBoxDefaultButton.Button1);
        }
        catch (Exception ex)
        {
          Console.WriteLine(ex.StackTrace.ToString());
        }
      }
    }
  }
}