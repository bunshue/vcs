using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
方案總管/方案... 右鍵/專案相依性,
專案 選 vcs_UseLibrary
相依於 CommonTools 打勾

vcs_UseLibrary 方案總管/參考/加入參考 選 CommonTools
*/

namespace vcs_UseLibrary
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

        private void button1_Click(object sender, EventArgs e)
        {
            CommonTools.MessageBox.ShowTipMessage("请先用画图工具画下载的区域多边形或选择省市区域！");
        }
    }
}
