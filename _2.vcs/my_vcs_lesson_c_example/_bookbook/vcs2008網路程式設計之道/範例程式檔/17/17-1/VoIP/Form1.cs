using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

// Openh323控制元件轉換為ATLH323Lib參考
using ATLH323Lib;

namespace VoIP
{
  public partial class Form1 : Form
  {
    H323Class h323;

    public Form1()
    {
      InitializeComponent();
    }

    private void Form1_Load(object sender, EventArgs e)
    {
      // 建立H323Class物件
      h323 = new H323Class();

      cboInput.Items.Add(h323.RxSound); // 語音輸入裝置
      cboInput.SelectedIndex = 0;

      cboOutput.Items.Add(h323.TxSound); // 語音輸出裝置
      cboOutput.SelectedIndex = 0;

      h323.EnumSoundRx(); // 檢查語音輸入裝置
      h323.EnumSoundTx(); // 檢查語音輸出裝置

      h323.AutoAnswer = true;  // 自動答話
      h323.SilenceDetection = true;  // 靜音偵測

      btnHangup.Enabled = false;
      btnAnswer.Enabled = false;
    }

    private void btnListen_Click(object sender, EventArgs e)
    {
      h323.Listen();

      btnListen.Enabled = false;
      btnCall.Enabled = false;
      btnHangup.Enabled = false;
      btnAnswer.Enabled = false;
    }

    private void btnCall_Click(object sender, EventArgs e)
    {
      // 是否透過H.323閘道器連結
      if (chkGateway.Checked)
      {
        h323.UseGateway = true;
        // 設定H.323閘道器
        h323.Gateway = txtGateway.Text;
      }
      else
        h323.UseGateway = false;

      h323.RemoteHost = txtHost.Text;

      h323.Connect();

      btnListen.Enabled = false;
      btnCall.Enabled = false;
      btnHangup.Enabled = true;
      btnAnswer.Enabled = true;
    }

    private void btnHangup_Click(object sender, EventArgs e)
    {
      h323.Hangup();  // 掛斷

      btnListen.Enabled = true;
      btnCall.Enabled = true;
      btnHangup.Enabled = false;
      btnAnswer.Enabled = false;
    }

    private void chkAuto_CheckedChanged(object sender, EventArgs e)
    {
      // 設定是否自動答話
      if (chkAuto.Checked)
        h323.AutoAnswer = true;
      else
        h323.AutoAnswer = false;
    }

    private void chkSilence_CheckedChanged(object sender, EventArgs e)
    {
      // 是否使用靜音偵測
      if (chkSilence.Checked)
        h323.SilenceDetection = true;
      else
        h323.SilenceDetection = false;
    }

    private void chkGateway_CheckedChanged(object sender, EventArgs e)
    {
      // 是否透過H.323閘道器連結
      if (chkGateway.Checked)
      {
        txtGateway.Enabled = true;
        h323.UseGateway = true;
        // 設定H.323閘道器
        h323.Gateway = txtGateway.Text;
      }
      else
      {
        h323.UseGateway = false;
        txtGateway.Enabled = false;
      }
    }

    private void btnAnswer_Click(object sender, EventArgs e)
    {
      h323.Answer();
    }

    private void cboInput_SelectedIndexChanged(object sender, EventArgs e)
    {
      if (cboInput.SelectedIndex >= 0) // 語音輸入裝置
        h323.RxSound = cboInput.SelectedItem.ToString();
    }

    private void cboOutput_SelectedIndexChanged(object sender, EventArgs e)
    {
      if (cboOutput.SelectedIndex >= 0) // 語音輸出裝置
        h323.TxSound = cboOutput.SelectedItem.ToString();
    }
  }
}
