using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.Objects;

namespace xCh12_1_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            NorthwindChineseEntities currContext = new NorthwindChineseEntities();

            foreach (var cr in currContext.Employees)
            {
                textBox1.AppendText(cr.EmployeeName.ToString());
                textBox1.AppendText("\t");
                textBox1.AppendText(cr.Address.ToString());
                textBox1.AppendText("\n");
            }

            var employees = from emp in currContext.Employees
                            select new { emp.Address,  emp.EmployeeName };
            foreach (var recs in employees)
            {
                listBox1.Items.Add(string.Format("{0}\t{1}", recs.EmployeeName,recs.Address));
            }

            var nemployees = from emp in currContext.Employees
                            select new 
                            { 
                                地址=emp.Address, 
                                姓名=emp.EmployeeName
                            };
            dataGridView1.DataSource = nemployees.ToList();
            dataGridView1.Columns[0].Width =250;
            dataGridView1.Columns[1].Width = 100;
        }
    }
}
