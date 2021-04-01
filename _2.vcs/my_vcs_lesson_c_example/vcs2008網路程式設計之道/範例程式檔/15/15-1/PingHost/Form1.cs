using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Globalization;

using System.Net.NetworkInformation;

namespace PingHost
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    private void btnPing_Click(object sender, EventArgs e)
    {
      Ping ping = null;
      PingReply reply = null;

      txtResult.Text = "";
      txtError.Text = "";

      if (txtIP.Text.Length != 0)
      {
        int i = 0;
        int received = 0;

        for (i = 0; i <= 3; i++)
        {
          try
          {
            // �إ�Ping����
            ping = new Ping();

            // �P�B�B�z�ǰeICMP�T���ܻ��ݥD��
            // �Ǧ����եD���s�u���A
            reply = ping.Send(txtIP.Text);

            // �P�_�s�u���A
            if (reply.Status == IPStatus.Success)
            {
              txtResult.Text +=
                  "Reply from " + reply.Address.ToString() +
                  ": bytes=" + reply.Buffer.Length +
                  " time=" + reply.RoundtripTime.ToString(NumberFormatInfo.CurrentInfo) + "ms" +
                  " TTL=" + reply.Options.Ttl + "\r\n";

              received += 1;
            }
            else
              txtResult.Text += GetPingReplyStatus(reply.Status) + "\r\n";
          }
          catch (Exception ex)
          {
            txtError.Text = ex.StackTrace.ToString();
          }
        }

        int loss = 4 - received;

        txtResult.Text += "\r\nPing statistics for " + txtIP.Text + ":" + "\r\n";
        txtResult.Text += "Packets: Sent = 4, Received = " + received + ", Lost = " + loss;
      }
      else
      {
        MessageBox.Show("Please enter a host name or IP address.", "Ping", MessageBoxButtons.OK, MessageBoxIcon.Error);
      }
    }

    private string GetPingReplyStatus(IPStatus status)
    {
      // �P�_�ǰe�ʥ]�����A
      switch (status)
      {
        case IPStatus.Success:
          return "Success.";
        case IPStatus.DestinationHostUnreachable:
          return "Destination host unreachable.";
        case IPStatus.DestinationNetworkUnreachable:
          return "Destination network unreachable.";
        case IPStatus.DestinationPortUnreachable:
          return "Destination port unreachable.";
        case IPStatus.DestinationProtocolUnreachable:
          return "Destination protocol unreachable.";
        case IPStatus.PacketTooBig:
          return "Packet too big.";
        case IPStatus.TtlExpired:
          return "TTL expired.";
        case IPStatus.ParameterProblem:
          return "Parameter problem.";
        case IPStatus.SourceQuench:
          return "Source quench.";
        case IPStatus.TimedOut:
          return "Timed out.";
        default:
          return "Ping failed.";
      }
    }
  }
}