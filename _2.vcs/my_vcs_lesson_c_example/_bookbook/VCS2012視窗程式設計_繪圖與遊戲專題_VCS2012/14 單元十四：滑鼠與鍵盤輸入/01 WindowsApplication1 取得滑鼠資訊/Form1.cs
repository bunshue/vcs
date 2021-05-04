/* 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2009-09 */
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace WindowsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            if (SystemInformation.MousePresent)  // 是否安裝滑鼠
                label1.Text = label1.Text + "是";
            else
                label1.Text = label1.Text + "否";

            // 滑鼠按鈕的數目
            label2.Text = label2.Text + SystemInformation.MouseButtons.ToString();

            if (SystemInformation.MouseWheelPresent) // 滑鼠是否有滾輪
                label3.Text = label3.Text + "是";
            else
                label3.Text = label3.Text + "否";

            // 滑鼠速度 (1 ~ 20)
            label4.Text = label4.Text + SystemInformation.MouseSpeed.ToString();
        }
    }
}