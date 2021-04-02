using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Net.NetworkInformation;
using System.Net.Sockets;
using System.Net;
using System.Runtime.InteropServices;
namespace 監測目前網絡連接狀態
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        [DllImport("wininet.dll", EntryPoint = "InternetGetConnectedState")]
        public extern static bool InternetGetConnectedState(out int conState, int reder);
        //參數說明 constate 連接說明 ，reder保留值
        public bool IsConnectedToInternet()
        {
            int Desc=0;
            return InternetGetConnectedState(out  Desc, 0);
        }
    

        private void button2_Click(object sender, EventArgs e)
        {
            if (IsConnectedToInternet())
                MessageBox.Show("已連接在網上!","提示");
            else
                MessageBox.Show("未連接在網上!!","提示"); 
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
     
    }
}