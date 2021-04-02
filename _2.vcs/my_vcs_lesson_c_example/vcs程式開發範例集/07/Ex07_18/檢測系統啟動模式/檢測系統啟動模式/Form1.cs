using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 檢測系統啟動模式
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string mode = SystemInformation.BootMode.ToString();
            string str = "目前系統的啟動模式是：";
            switch (mode)
            {
                case "FailSafe":
                    MessageBox.Show(str + "不具有網絡支援的安全模式");
                    break;
                case "FailSafeWithNetwork":
                    MessageBox.Show(str + "具有網絡支援的安全模式");
                    break;
                case "Normal":
                    MessageBox.Show(str + "標準模式");
                    break;
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}