using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinTabControl
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        // 定義Employee員工類別
        class Employee
        {
            public string EmpID { get; set; }   	// 編號屬性
            public string EmpName { get; set; } 	// 姓名屬性
            public string EmpSex { get; set; }     	// 性別屬性
            public bool EmpIsMarry { get; set; }  	// 婚姻屬性
        }

        List<Employee> emp = new List<Employee>();

        // 表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            txtShow.Dock = DockStyle.Fill; // txtShow文字方塊填滿整個標籤頁
            // txtShow 字型大小11
            txtShow.Font = new Font(txtShow.Font.FontFamily, 11, FontStyle.Regular);
            txtShow.ReadOnly = true;
            txtShow.Multiline = true;
            rdbF.Checked = true;    // 男選項鈕，預設選取
        }

        private void btnAdd_Click(object sender, EventArgs e)
        {
                string sex="";
                if (rdbM.Checked)
                {
                    sex = "先生";
                }
                else
                {
                    sex = "小姐";
                }
                emp.Add(new Employee() { EmpID = txtEmpId.Text, EmpName = txtName.Text, EmpSex = sex, EmpIsMarry = chkIsMarry.Checked  });
                MessageBox.Show("員工新增成功");

                // 還原預設值
                txtEmpId.Text = "";
                txtName.Text = "";
                rdbF.Checked = true;
                chkIsMarry.Checked = false;
        }

        private void tabControl1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if(tabControl1.SelectedIndex==1)// 判斷是否切換到「會員列表」標籤頁
            {
                // 在txtShow文字方塊內顯示已新增的員工資料
                txtShow.Text = "編號\t姓名\t性別\t是否已婚" + Environment.NewLine;
                txtShow.Text += "============================" + Environment.NewLine;
                for (int i = 0; i < emp.Count; i++)
                {
                    txtShow.Text +=	emp[i].EmpID + "\t" + emp[i].EmpName + " \t" +
 						emp[i].EmpSex + "\t" + emp[i].EmpIsMarry.ToString() +
 						Environment.NewLine;
                }
            }
        }
    }
}
