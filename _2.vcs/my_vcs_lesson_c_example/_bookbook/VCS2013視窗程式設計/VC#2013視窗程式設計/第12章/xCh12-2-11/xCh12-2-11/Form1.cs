using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh12_2_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            button1.Text = "新增";
            button2.Text = "刪除";
            button3.Text = "查詢";
            button4.Text = "修改";

            using (NorthwindChineseEntities context = new NorthwindChineseEntities())
            {
                dataGridView1.DataSource = context.Employees.ToList();
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            using (NorthwindChineseEntities context = new NorthwindChineseEntities())
            {
                try
                {
                    context.Employees.Add(new Employees()
                    {
                        EmployeeName = textBox1.Text,
                        EmployeeAddress = "嘉義市北港路",
                        Title = "產品測試經理"
                    });
                    context.SaveChanges();
                    dataGridView1.DataSource = context.Employees.ToList();
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.InnerException.Message);
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            using (NorthwindChineseEntities context = new NorthwindChineseEntities())
            {
                context.Employees.Remove(
                    context.Employees.Where(
                    r => r.EmployeeName == textBox1.Text)
                    .FirstOrDefault());
                context.SaveChanges();
                dataGridView1.DataSource = context.Employees.ToList();
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            using (NorthwindChineseEntities context = new NorthwindChineseEntities())
            {
                var qry = from emp in context.Employees
                          where emp.EmployeeName == textBox1.Text
                          select new
                          {
                              編號 = emp.EmployeeID,
                              姓名 = emp.EmployeeName,
                              地址 = emp.EmployeeAddress
                          };
                dataGridView1.DataSource = qry.ToList();
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            using (NorthwindChineseEntities context = new NorthwindChineseEntities())
            {
                var qry = context.Employees.First(r => r.EmployeeName == textBox1.Text);
                qry.EmployeeName = textBox1.Text + qry.TitleOfCourtesy;
                context.SaveChanges();
                dataGridView1.DataSource = context.Employees.ToList();
            }
        }
    }
}
