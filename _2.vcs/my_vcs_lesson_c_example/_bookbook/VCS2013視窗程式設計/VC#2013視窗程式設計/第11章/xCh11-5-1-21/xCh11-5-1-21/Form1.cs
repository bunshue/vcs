using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh11_5_1_21
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            xCh11_5_1_21.Northwind ds = new Northwind();

            xCh11_5_1_21.NorthwindTableAdapters.產品資料TableAdapter da =     
                new xCh11_5_1_21.NorthwindTableAdapters.產品資料TableAdapter();

            da.Fill(ds.產品資料);

            var myQuery =
                from product in ds.產品資料.AsEnumerable()
                where product.不再銷售 == true
                select
                    new
                    {
                        產品編號 = product.產品編號,
                        產品 = product.產品,
                        庫存量 = product.庫存量
                    };

            // 秀出LINQ查詢出來的資料 
            dataGridView1.DataSource = myQuery.ToList();
        }
    }
}
