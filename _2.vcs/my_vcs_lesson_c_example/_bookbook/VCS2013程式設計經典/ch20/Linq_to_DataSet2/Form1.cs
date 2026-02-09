using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;

using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.Linq;

namespace Linq_to_DataSet2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        EmployeeDataSet ds = new EmployeeDataSet();

        // 表單載入時執行此事件處理函式
        private void Form1_Load(object sender, EventArgs e)
        {
            EmployeeDataSetTableAdapters.員工TableAdapter da =
            new EmployeeDataSetTableAdapters.員工TableAdapter();
            da.Fill(ds.員工);
            dataGridView1.DataSource = ds.員工;
        }

        // 按下 [確定] 鈕執行此事件處理函式 
        private void btnOk_Click(object sender, EventArgs e)
        {
            try
            {
                var emp = from p in ds.員工
                          orderby p.薪資
                          where p.薪資 >= int.Parse(txtInput.Text)
                          select new
                          {
                              員工編號 = p.編號,
                              員工姓名 = p.姓名,
                              員工電話 = p.電話,
                              員工職稱 = p.職稱,
                              員工薪資 = p.薪資
                          };
                dataGridView1.DataSource = emp.ToList();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
    }
}
