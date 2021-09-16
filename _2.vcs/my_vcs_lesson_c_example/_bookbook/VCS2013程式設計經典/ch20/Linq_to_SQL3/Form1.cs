using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Linq_to_SQL3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // 表單載入時執行此事件處理函式
        private void Form1_Load(object sender, EventArgs e)
        {
            ch20DBDataContext dc = new ch20DBDataContext();
            var result = from p in dc.員工
                         select new { p.編號, p.姓名, p.職稱, p.電話, p.薪資 };
            dataGridView1.DataSource = result;
        }

    }
}
