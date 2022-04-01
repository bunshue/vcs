using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using JH.CommBase;
/*
 作者:旋风
 时间:2010-4-8
 主页:http://xuanfeng.cnblogs.com/
 */
namespace WinBaseTerm
{
    public partial class GPSReadForm : Form
    {
        public GPSReadForm()
        {
            InitializeComponent();
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void btClear_Click(object sender, EventArgs e)
        {
            this.rt.Text = "";
        }
        /// <summary>
        /// 显示信息委托
        /// </summary>
        /// <param name="mess"></param>
        /// <param name="count"></param>
        private delegate void InvokeDelegate(string mess,int count);
        /// <summary>
        /// 显示信息
        /// </summary>
        /// <param name="mess"></param>
        /// <param name="count"></param>
        public void ShowRevMsg(string mess,int count)
        {
            if (this.InvokeRequired)
                this.BeginInvoke(new InvokeDelegate(InvokeFunction), mess,count);
            else
                InvokeFunction(mess,count);

        }
        /// <summary>
        ///信息显示回调方示
        /// </summary>
        /// <param name="s"></param>
        /// <param name="t"></param> 
        private void InvokeFunction(string mess,int count)
        {
            this.rt.Text += mess.Replace("<CR><LF>","") + "\n";
            this.lbM.Text = string.Format("收到{0}条信息",count);
            
        }
        private void bt_Click(object sender, EventArgs e)
        {
            if (this.bt.Tag.ToString() == "0")
            {
               

                try
                {
                    MonitorTerm.settings.port = this.cbDK.Text;
                    MonitorTerm.term.Open();

                    this.bt.Tag = 1;
                    this.bt.Text = "关闭";
                    this.Text = "GPS读取(监听状态)";
                    
                }
                catch (Exception ex)
                {

                    MessageBox.Show(string.Format("打开端口错误：{0}。", ex.Message));
                }
            }
            else
            {
              
                try
                {
                    MonitorTerm.term.Close();
                    this.bt.Tag = 0;
                    this.bt.Text = "监听";
                    this.Text = "GPS读取(关闭状态)";

                }
                catch (Exception ex)
                {
                    MessageBox.Show(string.Format("关闭端口错误：{0}。", ex.Message));
                }
            }
        }
        /// <summary>
        /// 填冲端口
        /// </summary>
        /// <param name="cb"></param>
        private void FillPorts(ComboBox cb)
        {
            string n;
            for (int i = 0; (i < 99); i++)
            {
                n = "COM" + i.ToString();
                if (MonitorTerm.term.IsPortAvailable(n) == CommBase.PortStatus.available)
                {
                    cb.Items.Add(n);
                }
            }
        }

        private void GPSReadForm_Load(object sender, EventArgs e)
        {
            FillPorts(cbDK);
        }
    }
}