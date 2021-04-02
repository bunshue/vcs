using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace ByteConversion
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        const int GB = 1024 * 1024 * 1024;//定義GB的計算常量
        const int MB = 1024 * 1024;//定義MB的計算常量
        const int KB = 1024;//定義KB的計算常量
        public string ByteConversionGBMBKB(Int64 KSize)
        {
            if (KSize / GB >= 1)//如果目前Byte的值大於等於1GB
                return (Math.Round(KSize / (float)GB, 2)).ToString() + "GB";//將其轉換成GB
            else if (KSize / MB >= 1)//如果目前Byte的值大於等於1MB
                return (Math.Round(KSize / (float)MB, 2)).ToString() + "MB";//將其轉換成MB
            else if (KSize / KB >= 1)//如果目前Byte的值大於等於1KB
                return (Math.Round(KSize / (float)KB, 2)).ToString() + "KB";//將其轉換成KGB
            else
                return KSize.ToString() + "Byte";//顯示Byte值
        }

        private void button1_Click(object sender, EventArgs e)
        {
            textBox2.Text = ByteConversionGBMBKB(Convert.ToInt64(textBox1.Text));
        }
    }
}
