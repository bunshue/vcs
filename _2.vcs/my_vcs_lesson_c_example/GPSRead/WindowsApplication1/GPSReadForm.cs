using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using JH.CommBase;

namespace WinBaseTerm
{
    public partial class GPSReadForm : Form
    {
        public GPSReadForm()
        {
            InitializeComponent();
        }

        private void GPSReadForm_Load(object sender, EventArgs e)
        {
            FillPorts(cbDK);
        }

        /// <summary>
        /// 填充端口
        /// </summary>
        /// <param name="cb"></param>
        private void FillPorts(ComboBox cb)
        {
            string n;
            for (int i = 0; i < 10; i++)
            {
                n = "COM" + i.ToString();
                richTextBox1.Text += "n : " + n + "\t";
                if (MonitorTerm.term.IsPortAvailable(n) == CommBase.PortStatus.available)
                {
                    richTextBox1.Text += "符合\n";
                    cb.Items.Add(n);
                }
                else
                {
                    richTextBox1.Text += "不符合\n";
                }
            }
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void btClear_Click(object sender, EventArgs e)
        {
            this.rt.Text = "";

            richTextBox1.Clear();
        }

        /// <summary>
        /// 顯示信息委托
        /// </summary>
        /// <param name="mess"></param>
        /// <param name="count"></param>
        private delegate void InvokeDelegate(string mess, int count);

        /// <summary>
        /// 顯示信息
        /// </summary>
        /// <param name="mess"></param>
        /// <param name="count"></param>
        public void ShowRevMsg(string mess, int count)
        {
            richTextBox1.Text += "A ";
            if (this.InvokeRequired)
                this.BeginInvoke(new InvokeDelegate(InvokeFunction), mess, count);
            else
                InvokeFunction(mess, count);

        }

        /// <summary>
        ///信息顯示回調方示
        /// </summary>
        /// <param name="s"></param>
        /// <param name="t"></param> 
        private void InvokeFunction(string mess, int count)
        {
            richTextBox1.Text += "B ";
            this.rt.Text += mess.Replace("<CR><LF>", "") + "\n";
            this.lbM.Text = string.Format("收到{0}條信息", count);
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
                    this.bt.Text = "關閉";
                    this.Text = "GPS讀取(監聽狀態)";
                    richTextBox1.Text += "GPS讀取(監聽狀態)\n";

                }
                catch (Exception ex)
                {
                    MessageBox.Show(string.Format("打開端口錯誤：{0}。", ex.Message));
                }
            }
            else
            {
                try
                {
                    MonitorTerm.term.Close();
                    this.bt.Tag = 0;
                    this.bt.Text = "監聽";
                    this.Text = "GPS讀取(關閉狀態)";
                    richTextBox1.Text += "GPS讀取(關閉狀態)\n";
                }
                catch (Exception ex)
                {
                    MessageBox.Show(string.Format("關閉端口錯誤：{0}。", ex.Message));
                }
            }
        }
    }
}
