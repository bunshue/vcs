using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

// �R�W�Ŷ�
using System.IO;
using System.Net;
using System.Net.Cache;

namespace Response
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    private void Button1_Click(object sender, EventArgs e)
    {
      System.Net.WebRequest request = null;
      System.Net.WebResponse response = null;

      string result = "";

      if (txtURL.Text != "")
      {
        string uriString = "";

        if (!txtURL.Text.StartsWith("http://"))
        {
          uriString = "http://" + txtURL.Text;
          txtURL.Text = uriString;
        }
        else
          uriString = txtURL.Text;

        try
        {
          // �HWebRequest��H���O��Create��k�إ�WebRequest����
          request = WebRequest.Create(new Uri(uriString));

          // �ϥ�WebRequest���O��GetResponse��k�إ�WebResponse����
          response = request.GetResponse();

          // WebResponse���O���ݩ�

          // �Τ�ݩұ�����Ƥ��e���j�p�]byte�^
          result = result + "ContentLength: " + response.ContentLength.ToString() + "\r\n";

          // �Τ�ݩұ�����Ƥ��e��MIME�榡
          result = result + "ContentType: " + response.ContentType.ToString() + "\r\n";

          // �Τ�ݩұ�����URI
          result = result + "ResponseUri: " + response.ResponseUri.ToString() + "\r\n";

          // �Τ�ݩұ������^�����e�O�_�q�֨������o
          result = result + "���A�ݦ^���O�_����Cache? " + response.IsFromCache;

          // �����^����y
          response.Close();

          txtResponse.Text = result;
        }
        catch (Exception ex)
        {
          txtResponse.Text = ex.StackTrace.ToString();
        }
      }
    }
  }
}