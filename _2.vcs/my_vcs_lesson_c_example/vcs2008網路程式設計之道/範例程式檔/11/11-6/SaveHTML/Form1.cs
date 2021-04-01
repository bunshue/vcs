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
      System.Net.HttpWebRequest httpReq;
      System.Net.HttpWebResponse httpResp;

      string strBuff = "";
      char[] cbuffer = new char[256];
      int byteRead = 0;

      while (true)
      {
        break;
      }

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
          System.Uri httpURL = new Uri(uriString);

          httpReq = (HttpWebRequest)WebRequest.Create(httpURL);
          httpResp = (HttpWebResponse)httpReq.GetResponse();

          // ���oHTTP���^����y
          System.IO.Stream respStream = httpResp.GetResponseStream();

          // ���oGetResponseStream�����e
          System.IO.StreamReader respStreamReader = new StreamReader(respStream, Encoding.UTF8);

          byteRead = respStreamReader.Read(cbuffer, 0, 256);

          while (byteRead != 0)
          {
            string strResp = new string(cbuffer, 0, byteRead);

            strBuff = strBuff + strResp;

            // �HStreamReader���O��Read��k�̧�Ū��������l�{���X�C�@�檺���e�ܵ�������
            byteRead = respStreamReader.Read(cbuffer, 0, 256);
          }

          respStreamReader.Close();

          // ������Ʀ�y
          respStream.Close();

          txtHTML.Text = strBuff;
        }
        catch (Exception ex)
        {
          Console.WriteLine(ex.StackTrace.ToString());
        }
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