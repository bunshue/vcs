using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;
namespace 远程控制计算机
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
        //首先添加对 System.Management的引用 
        private void CloseComputer(string strname,string strpwd,string ip,string doinfo)
        {
            ConnectionOptions op = new ConnectionOptions ( ) ; 
            op.Username =strname;//''或者你的帐号（注意要有管理员的权限） 
            op.Password = strpwd; //''你的密码 
            ManagementScope scope = new ManagementScope("\\\\" + ip + "\\root\\cimv2:Win32_Service", op); 
            try 
            { 
                scope.Connect ( ) ; 
                System.Management.ObjectQuery oq = new System.Management.ObjectQuery ( "SELECT * FROM Win32_OperatingSystem" ) ; 
                ManagementObjectSearcher query1 = new ManagementObjectSearcher (scope,oq) ; 
                //得到WMI控制 
                ManagementObjectCollection queryCollection1 = query1.Get ( ) ; 
                foreach ( ManagementObject mobj in queryCollection1 ) 
                { 
                    string [ ] str= {""} ;
                    mobj.InvokeMethod(doinfo, str); 
                }
                MessageBox.Show("操作成功");
            } 
            catch(Exception ey)
            {
                MessageBox.Show(ey.Message);
                this.button1.PerformClick();
            } 
        }

        private void button1_Click(object sender, EventArgs e)
        {
            CloseComputer(this.textBox2.Text, this.textBox3.Text, this.textBox1.Text, "Reboot");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            CloseComputer(this.textBox2.Text, this.textBox3.Text, this.textBox1.Text, "Shutdown");
        }
    }
}