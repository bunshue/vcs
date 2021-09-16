using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh11_4_1_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // DataContext的名稱是以「*.dbml」的檔名，
            // 再加上DataContext組合而成
            // 因此，本例的DataContext即為
            // NorthwindDataContext
            NorthwindDataContext db = new NorthwindDataContext();

            var myQuery =
                from emplolyee in db.Employees
                select emplolyee;

            dataGridView1.DataSource = myQuery;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            NorthwindDataContext db = new NorthwindDataContext();

            var myQuery =
                from emplolyee in db.Employees
                where emplolyee.Title.StartsWith("業務")
                select emplolyee;

            dataGridView1.DataSource = myQuery;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            NorthwindDataContext db = new NorthwindDataContext();

            var myQuery =
                from emplolyee in db.Employees
                where emplolyee.Title.StartsWith("業務")
                select new { 姓名 = emplolyee.EmployeeName, 頭銜 = emplolyee.Title };

            dataGridView1.DataSource = myQuery;
        }
    }
}
