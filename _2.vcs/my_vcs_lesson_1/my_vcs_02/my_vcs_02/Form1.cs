using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;        //for Directory

using System.Net.NetworkInformation;    //for network test
using System.Net.Sockets;               //for network test
using System.Net;                       //for network test
using System.Runtime.InteropServices;   //for network test

namespace my_vcs_02
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            folderBrowserDialog1.ShowDialog();
            textBox1.Text = folderBrowserDialog1.SelectedPath;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //if (textBox1.Text != 0)   ??
            {
                string[] files = Directory.GetFiles(textBox1.Text);
                //MessageBox.Show("file numbers = " + files.Length);
                //MessageBox.Show("files = " + files);
                for (int i = 0; i < files.Length; i++)
                {
                    //MessageBox.Show("i = " + i + ", filename = " + files);
                    //MessageBox.Show("i = " + i);
                    
                    textBox2.Lines = files;
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (DialogResult.Yes == MessageBox.Show("是否要建立文件夾"+textBox3.Text.ToString(), "提示", MessageBoxButtons.YesNo))
            {
                Directory.CreateDirectory(textBox3.Text);
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (DialogResult.Yes == MessageBox.Show("是否要刪除文件夾" + textBox3.Text.ToString(), "提示", MessageBoxButtons.YesNo))
            {
                Directory.Delete(textBox3.Text);
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            MessageBox.Show("CruuentSystemDir : " + System.Environment.CurrentDirectory);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            MessageBox.Show("CurrentDirectory : " + Application.StartupPath);
        }

        int IsComPortOpen = 0;
        private void OpenComPortButton_Click(object sender, EventArgs e)
        {
            if (IsComPortOpen == 1)
            {
                //OPEN => CLOSE
                this.OpenComPortButton.Text = "COM Close";
                //this.OpenComPortButton.ForeColor = Color.OrangeRed;
                this.OpenComPortButton.BackColor = Color.OrangeRed;
                //this.OpenComPortButton.Image = Resource1.green_ball_icon;
                IsComPortOpen = 0;
            }
            else
            {
                //CLOSE => OPEN
                this.OpenComPortButton.Text = "COM Open";
                //this.OpenComPortButton.ForeColor = Color.MediumSpringGreen;
                this.OpenComPortButton.BackColor = Color.MediumSpringGreen;
                //this.OpenComPortButton.Image = Resource1.red_ball_icon;
                IsComPortOpen = 1;
            }
        }

        [DllImport("wininet.dll", EntryPoint = "InternetGetConnectedState")]
        public extern static bool InternetGetConnectedState(out int conState, int reder);
        //參數說明 constate 連接說明 ，reder保留值
        public bool IsConnectedToInternet()
        {
            int Desc = 0;
            return InternetGetConnectedState(out  Desc, 0);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            if (IsConnectedToInternet())
                MessageBox.Show("已連接在網上!", "提示");
            else
                MessageBox.Show("未連接在網上!!", "提示"); 
        }

        private void SelectFile_Click(object sender, EventArgs e)
        {
            if(openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                label2.Text = "Select : " + openFileDialog1.FileName;
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            System.Diagnostics.Process.Start(textBox1.Text);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            MessageBox.Show("一些按鈕功能。");
        }
    }
}
