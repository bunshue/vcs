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
    Ping ping = new Ping();

    public Form1()
    {
      InitializeComponent();
    }

    private void Form1_Load(object sender, EventArgs e)
    {
      // ��ǰeICMP�T��������
      // �éw�q�ҩI�s��Callback��k
      ping.PingCompleted += new PingCompletedEventHandler(this.PingCompletedCallback);
    }

    private void btnPing_Click(object sender, EventArgs e)
    {
      txtResult.Text = "";
      txtError.Text = "";
      StatusBar.Text = "";

      if (txtIP.Text.Length != 0)
      {
        btnPing.Enabled = false;

        StatusBar.Text = "Pinging " + txtIP.Text + " ...";

        try
        {
          // ����D�P�B�ǰeICMP�T��
          ping.SendAsync(txtIP.Text, null);
        }
        catch (Exception ex)
        {
          txtError.Text = ex.StackTrace.ToString();
        }
      }
      else
      {
        MessageBox.Show("Please enter a host name or IP address.", "Ping", MessageBoxButtons.OK, MessageBoxIcon.Error);
      }
    }

    private void btnCancel_Click(object sender, EventArgs e)
    {
      // �����D�P�B�ǰeICMP�T��
      ping.SendAsyncCancel();
    }

    // �ۭqCallback��k
    private void PingCompletedCallback(object sender, PingCompletedEventArgs e)
    {
      // �P�_�D�P�B�@�~�O�_�o�Ϳ��~
      if (e.Error == null)
      {
        // �P�_�D�P�B�@�~�O�_�w�Q����
        if (e.Cancelled)
          StatusBar.Text = "Ping cancelled.";
        else
        {
          if (e.Reply.Status == IPStatus.Success)
          {
            txtResult.Text +=
                "Reply from " + e.Reply.Address.ToString() +
                ": bytes=" + e.Reply.Buffer.Length +
                " time=" + e.Reply.RoundtripTime.ToString(NumberFormatInfo.CurrentInfo) + "ms" +
                " TTL=" + e.Reply.Options.Ttl + "\r\n";

            StatusBar.Text = "Ping complete.";
          }
          else
            txtResult.Text += GetPingReplyStatus(e.Reply.Status) + "\r\n";
        }
      }
      else
      {
        // �@�~�o�Ϳ��~
        StatusBar.Text = "Ping error.";

        MessageBox.Show("Ping error: " + e.Error.InnerException.Message, "Ping", MessageBoxButtons.OK, MessageBoxIcon.Error);
      }

      btnPing.Enabled = true;
    }

    private string GetPingReplyStatus(IPStatus status)
    {
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