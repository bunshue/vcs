using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;
using System.Text.RegularExpressions;
using QueryIPAndMPhone.CommonClass;

namespace QueryIPAndMPhone
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private string IPData = "IPData.dat";           //IP数据文件
        private string MPhoneData = "MPhoneData.dat";   //手机号码归属地数据文件

        private void btnQuery_Click(object sender, EventArgs e)
        {
            string strIP= txtIP.Text.Trim();
            string strMPhone = txtMPhone.Text.Trim();
            txtResult.Text = "";
            //查询IP
            if (strIP.Length > 0)
            {
                try
                {
                    IPStruct myIPStruct = IPClass.SearchIP(IPData, strIP);
                    txtResult.Text += "IP地址段: " + IPClass.IntToIP(myIPStruct.IPStart) + " - " + IPClass.IntToIP(myIPStruct.IPEnd) + "\r\n";
                    txtResult.Text += "IP所在地: " + myIPStruct.Country + " " + myIPStruct.City + "\r\n\r\n";
                }
                catch
                {
                    MessageBox.Show("IP数据库打开失败,请确认" + IPData + "文件是否存在！", "警告", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                }
            }
            //查询手机号码归属地
            if (strMPhone.Length > 0 && Regex.IsMatch(strMPhone, @"^-?\d+$"))
            {
                if (strMPhone.Length > 7)
                    strMPhone = strMPhone.Substring(0, 7);
                int intMPhone = Int32.Parse(strMPhone);
                try
                {
                    MPhoneStruct myMPhoneStruct = MPhoneClass.GetMPhonePlace(MPhoneData, intMPhone);
                    txtResult.Text += "号码段: " + myMPhoneStruct.MPhoneStart + " - " + myMPhoneStruct.MPhoneEnd + "\r\n";
                    txtResult.Text += "归属地: " + myMPhoneStruct.Place + "\r\n\r\n";
                }
                catch
                {
                    MessageBox.Show("手机号码数据库打开失败,请确认" + MPhoneData + "文件是否存在！", "警告", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                }
            }
        }
    }
}
