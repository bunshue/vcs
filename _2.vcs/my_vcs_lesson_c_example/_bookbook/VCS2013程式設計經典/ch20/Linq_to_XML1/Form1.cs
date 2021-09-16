using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;

using System.Text;
using System.Windows.Forms;

using System.Linq;
using System.Xml.Linq;  // 含入System.Xml.Linq命名空間

namespace Linq_to_XML1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        XElement xmlFile = XElement.Load("person.xml");
        // 表單載入時執行此事件處理函式
        private void Form1_Load(object sender, EventArgs e)
        {
            var stu = from s in xmlFile.Elements() select new { 學生學號 = (string)s.Element("學號"), 學生姓名 = (string)s.Element("姓名"), 學生電話 = (string)s.Element("電話"), 學生信箱 = (string)s.Element("信箱") };
            dataGridView1.DataSource = stu.ToList();
            lblCount.Text = "學生共 " + stu.Count().ToString() + "人";
        }
        // 按 [搜尋] 鈕執行此事件處理函式
        private void btnSearch_Click(object sender, EventArgs e)
        {
            var stu = from s in xmlFile.Elements() where (string)s.Element("學號") == txtId.Text select new { 學生學號 = (string)s.Element("學號"), 學生姓名 = (string)s.Element("姓名"), 學生電話 = (string)s.Element("電話"), 學生信箱 = (string)s.Element("信箱") };
            if (stu.Count() == 0)
            {
                MessageBox.Show("沒有學號 " + txtId.Text + "這位學生");
            }
            else
            {
                foreach (var s in stu)
                {
                    MessageBox.Show("學生學號：" + s.學生學號 + "\n學生姓名：" + s.學生姓名 + "\n學生電話：" + s.學生電話 + "\n學生信箱：" + s.學生信箱, "\n搜尋結果", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
            }
        }
    }
}