using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Linq_to_SQL_EditDB
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        ch20DBDataContext dc = new ch20DBDataContext();
        // 表單載入時執行此事件處理函式
        private void Form1_Load(object sender, EventArgs e)
        {
            var result = from p in dc.員工
                         orderby p.編號 descending
                         select new
                         {
                             p.姓名,
                             p.職稱,
                             p.電話,
                             p.薪資
                         };
            dataGridView1.DataSource = result;
        }
        // 按下 [新增] 鈕執行此事件處理函式 
        private void btnAdd_Click(object sender, EventArgs e)
        {
            try
            {
                員工 emp = new 員工();
                emp.姓名 = txtName.Text;
                emp.電話 = txtTel.Text;
                emp.職稱 = txtPosition.Text;
                emp.薪資 = int.Parse(txtSalary.Text);
                dc.員工.InsertOnSubmit(emp);
                dc.SubmitChanges();
                Form1_Load(sender, e);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
        // 按下 [修改] 鈕執行此事件處理函式 
        private void btnUpdate_Click(object sender, EventArgs e)
        {
            try
            {
                var emp = (from p in dc.員工
                           where p.姓名 == txtName.Text
                           select p).Single();
                emp.電話 = txtTel.Text;
                emp.職稱 = txtPosition.Text;
                emp.薪資 = int.Parse(txtSalary.Text);
                dc.SubmitChanges();
                Form1_Load(sender, e);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
        // 按 [刪除] 鈕執行此事件處理函式 
        private void btnDel_Click(object sender, EventArgs e)
        {
            try
            {
                var emp = (from p in dc.員工
                           where p.姓名 == txtName.Text
                           select p).Single();
                dc.員工.DeleteOnSubmit(emp);
                dc.SubmitChanges();
                Form1_Load(sender, e);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
    }
}
