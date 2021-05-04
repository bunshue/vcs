using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Weight
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            txtHeight.Text = "160"; //預設身高為160公分
            rdbMan.Checked = true;  //預設為男性
        }

        private void btnOK_Click(object sender, EventArgs e)
        {
            int height = Convert.ToInt32(txtHeight.Text);  //取得輸入的身高
            double weight;  //紀錄標準體重
            if (rdbMan.Checked == true)    //若rdbMan的Checked屬性值=true
                weight = (height - 80) * 0.7; //計算男性標準體重
            else
                weight = (height - 70) * 0.6; //計算女性標準體重
            lblWeight.Text = "標準體重：" + weight.ToString("f1") + "公斤";
        }
    }
}
