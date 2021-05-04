using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 使用LINQ技術查詢SQL數據庫中的數據
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        #region 定義公共變數及Linq連接對像
        //定義數據庫連接字串
        string strCon = "Data Source=(local);Database=db_11;Uid=sa;Pwd=;";
        linqtosqlDataContext linq;          //宣告Linq連接對像
        #endregion
        private void Form1_Load(object sender, EventArgs e)
        {
            comboBox1.SelectedIndex = 0;
        }

        private void Form1_Activated(object sender, EventArgs e)
        {
            txtKey.Focus();
        }

        private void SearchInfo()
        {
            linq = new linqtosqlDataContext(strCon);    //實例化Linq連接對像
            if (txtKey.Text == "")
            {
                var result = from info in linq.tb_User
                             select new
                             {
                                 編號 = info.ID,
                                 姓名 = info.User_Name.Trim(),
                                 性別 = info.User_Sex.Trim(),
                                 年齡 = info.User_Age.Trim(),
                                 婚姻狀況 = info.User_Marriage.Trim(),
                                 職位 = info.User_Duty.Trim(),
                                 聯繫電話 = info.User_Phone.Trim(),
                                 聯繫地址 = info.User_Address.Trim()
                             };
                dataGridView1.DataSource = result;
            }
            else
            {
                int i = comboBox1.SelectedIndex;
                switch (i)
                {
                    case 0://根據姓名尋找
                        var resultName = from info in linq.tb_User
                                     where info.User_Name.IndexOf(txtKey.Text)>=0
                                     select new
                                     {
                                         編號 = info.ID,
                                         姓名 = info.User_Name,
                                         性別 = info.User_Sex,
                                         年齡 = info.User_Age,
                                         婚姻狀況 = info.User_Marriage,
                                         職位 = info.User_Duty,
                                         聯繫電話 = info.User_Phone,
                                         聯繫地址 = info.User_Address
                                     };
                        dataGridView1.DataSource = resultName;
                        break;
                    case 1:////根據性別尋找
                        var resultSex = from info in linq.tb_User
                                     where info.User_Sex==txtKey.Text.Trim()
                                     select new 
                                     {
                                         編號 = info.ID,
                                         姓名 = info.User_Name,
                                         性別 = info.User_Sex,
                                         年齡 = info.User_Age,
                                         婚姻狀況 = info.User_Marriage,
                                         職位 = info.User_Duty,
                                         聯繫電話 = info.User_Phone,
                                         聯繫地址 = info.User_Address
                                     };
                        dataGridView1.DataSource = resultSex;
                        break;
                    case 2:////根據年齡尋找
                        var resultAge = from info in linq.tb_User
                                        where info.User_Age.StartsWith(txtKey.Text)
                                        select new 
                                        {
                                            編號 = info.ID,
                                            姓名 = info.User_Name,
                                            性別 = info.User_Sex,
                                            年齡 = info.User_Age,
                                            婚姻狀況 = info.User_Marriage,
                                            職位 = info.User_Duty,
                                            聯繫電話 = info.User_Phone,
                                            聯繫地址 = info.User_Address
                                        };
                        dataGridView1.DataSource = resultAge;
                        break;
                    case 3:////根據職位尋找
                        var resultDuty = from info in linq.tb_User
                                         where info.User_Duty == txtKey.Text.Trim()
                                         select new 
                                         { 
                                            編號 = info.ID,
                                            姓名 = info.User_Name,
                                            性別 = info.User_Sex,
                                            年齡 = info.User_Age,
                                            婚姻狀況 = info.User_Marriage,
                                            職位 = info.User_Duty,
                                            聯繫電話 = info.User_Phone,
                                            聯繫地址 = info.User_Address
                                         };
                        dataGridView1.DataSource = resultDuty;
                        break;
                }
            }
        }
        private void button1_Click(object sender, EventArgs e)
        {
            SearchInfo();
        }
    }
}
