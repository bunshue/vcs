using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Net.Mail;
using System.Net.Mime;
using System.IO;
using System.Threading;

namespace NetMail
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    private void Form1_Load(object sender, EventArgs e)
    {
      cboPriority.SelectedIndex = 0;
      lstAttachment.Items.Clear();
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
          // �B�z����
          OpenFileDialog1.Filter = "All files (*.*)|*.*";
          OpenFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();
          OpenFileDialog1.Title = "Select Attachment";

          if (OpenFileDialog1.ShowDialog() == DialogResult.OK)
            lstAttachment.Items.Add(OpenFileDialog1.FileName);

          break;

        case 2:
          // Clear
          txtTo.Clear();
          txtCc.Clear();
          txtBcc.Clear();
          txtSubject.Clear();
          txtMessage.Clear();
          lstAttachment.Items.Clear();
          chkHTML.Checked = false;
          cboPriority.SelectedIndex = 0;
          break;
      }
    }

    private void mnuExit_Click(object sender, EventArgs e)
    {
      DialogResult result = MessageBox.Show("Are you sure to quit?", "Net Mail", MessageBoxButtons.YesNo, MessageBoxIcon.Question, MessageBoxDefaultButton.Button1);

      if (result == DialogResult.Yes)
      {
        this.Close();
      }
    }

    private void ProcessMail()
    {
      System.Net.Mail.SmtpClient mailClient = null;
      System.Net.Mail.MailMessage mailmsg = null;
      System.Net.Mail.MailAddress fromAddress = null;
      System.Net.Mail.MailAddress toAddress = null;
      System.Net.Mail.MailAddress ccAddress = null;
      System.Net.Mail.MailAddress bccAddress = null;
      System.Net.Mail.Attachment mailAttach = null;

      try
      {
        // �]�wSMTP�l����A����DNS�W�٩�IP��}�γq�T��
        mailClient = new SmtpClient(txtHost.Text, 25);

        // �]�w�ϥΪ̵n�JSMTP�l����A���ݨϥαb���P�K�X���{��
        NetworkCredential credentials = new NetworkCredential(txtLogin.Text, txtPassword.Text, txtHost.Text);

        // �]�wSmtpClient����Credentials�ݩ�
        mailClient.Credentials = credentials;

        // �]�w�H��̶l��a�}
        fromAddress = new MailAddress(txtFrom.Text);

        // �]�w����̶l��a�}�]To�^
        if (txtTo.Text != "")
          toAddress = new MailAddress(txtTo.Text);

        // �]�w�ƥ�����̶l��a�}�]CC�^
        if (txtCc.Text != "")
          ccAddress = new MailAddress(txtCc.Text);

        // �]�w�K��ƥ�����̶l��a�}�]BCC�^
        if (txtBcc.Text != "")
          bccAddress = new MailAddress(txtBcc.Text);

        mailmsg = new MailMessage(fromAddress, toAddress);
        mailmsg.CC.Add(ccAddress);
        mailmsg.Bcc.Add(bccAddress);

        // �]�w�l��D��
        mailmsg.Subject = txtSubject.Text;

        // �]�w�l�󤺤媺�r���s�X�榡
        mailmsg.BodyEncoding = System.Text.Encoding.UTF8;

        // �]�w�l�󤺤�
        mailmsg.Body = txtMessage.Text;

        // �]�w�l�󤺤�O�_��HTML�榡
        if (chkHTML.Checked)
          mailmsg.IsBodyHtml = true;
        else
          mailmsg.IsBodyHtml = false;

        // �B�z����
        for (int i = 0; i <= lstAttachment.Items.Count - 1; i++)
        {
          mailAttach = new Attachment(lstAttachment.Items[i].ToString());
          mailmsg.Attachments.Add(mailAttach);
        }

        // �u���B�z����
        switch (cboPriority.SelectedIndex)
        {
          case 0:
            mailmsg.Priority = System.Net.Mail.MailPriority.Normal;
            break;

          case 1:
            mailmsg.Priority = System.Net.Mail.MailPriority.Low;
            break;

          case 2:
            mailmsg.Priority = System.Net.Mail.MailPriority.High;
            break;
        }

        // �l��ǰe
        mailClient.Send(mailmsg);

        mailmsg = null;

        MessageBox.Show("Send Mail Successfully.", "Net Mail", MessageBoxButtons.OK, MessageBoxIcon.Information, MessageBoxDefaultButton.Button1);
      }
      catch (Exception ex)
      {
        MessageBox.Show("Send Mail Error: " + ex.ToString(), "Net Mail", MessageBoxButtons.OK, MessageBoxIcon.Information, MessageBoxDefaultButton.Button1);
      }
    }

    private void Form1_Resize(object sender, EventArgs e)
    {
      Control control = (Control)sender;

      txtTo.Location = new System.Drawing.Point(72, 5);
      txtTo.Size = new System.Drawing.Size(control.Size.Width - 95, 22);
      txtCc.Location = new System.Drawing.Point(72, 31);
      txtCc.Size = new System.Drawing.Size(control.Size.Width - 95, 22);
      txtBcc.Location = new System.Drawing.Point(72, 57);
      txtBcc.Size = new System.Drawing.Size(control.Size.Width - 95, 22);
      txtSubject.Location = new System.Drawing.Point(72, 83);
      txtSubject.Size = new System.Drawing.Size(control.Size.Width - 95, 22);
      lstAttachment.Location = new System.Drawing.Point(72, 109);
      lstAttachment.Size = new System.Drawing.Size(control.Size.Width - 95, 28);
    }
  }
}