using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Net.Sockets;
using System.Threading;
using System.IO;
using System.Net;
namespace 點對點聊天室
{
    public partial class frmMain : Form
    {
        public frmMain()
        {
            InitializeComponent();
        }
        private Thread td;
        private TcpListener tcpListener;
        private void frmMain_Load(object sender, EventArgs e)
        {
            td = new Thread(new ThreadStart(this.StartListen));
            td.Start();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            try
            {
                IPAddress[] ip = Dns.GetHostAddresses(Dns.GetHostName());
                string message = " "+txtName.Text + "("+ip[0].ToString()+") "+DateTime.Now.ToLongTimeString()+"\n" +"  "+ this.rtbSend.Text + "\n";
                TcpClient client = new TcpClient(txtIP.Text, 888);
                NetworkStream netstream = client.GetStream();
                StreamWriter wstream = new StreamWriter(netstream, Encoding.Default);
                wstream.Write(message);
                wstream.Flush();
                wstream.Close();
                client.Close();
                rtbContent.AppendText(message);
                rtbContent.ScrollToCaret();
                rtbSend.Clear();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void StartListen()
        {
            tcpListener = new TcpListener(888);
            tcpListener.Start();
            while (true)
            {
                TcpClient tclient = tcpListener.AcceptTcpClient();//接受連接請求
                NetworkStream nstream = tclient.GetStream();       //取得數據流
                byte[] mbyte = new byte[1024];                      //建立快取
                int i = nstream.Read(mbyte, 0, mbyte.Length);       //將數據流寫入快取
                string message = Encoding.Default.GetString(mbyte, 0, i);
                rtbContent.AppendText(message);
                rtbContent.ScrollToCaret();
            }
        }

        private void frmMain_FormClosed(object sender, FormClosedEventArgs e)
        {
            if (this.tcpListener != null)
            {
                tcpListener.Stop();
            }
            if (td != null)
            {
                if (td.ThreadState == ThreadState.Running)
                {
                    td.Abort();
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            rtbContent.Clear();
        }

        private void rtbSend_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == '\r')
            {
                button2_Click(sender,e);
            }
        }
    }
}
