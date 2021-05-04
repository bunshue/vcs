using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace RelationDB
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void 產品類別BindingNavigatorSaveItem_Click(object sender, EventArgs e)
        {
            this.Validate();
            this.產品類別BindingSource.EndEdit();
            this.tableAdapterManager.UpdateAll(this.dataSetNorthwind);

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // TODO:  這行程式碼會將資料載入 'dataSetNorthwind.產品資料' 資料表。您可以視需要進行移動或移除。
            this.產品資料TableAdapter.Fill(this.dataSetNorthwind.產品資料);
            // TODO:  這行程式碼會將資料載入 'dataSetNorthwind.產品類別' 資料表。您可以視需要進行移動或移除。
            this.產品類別TableAdapter.Fill(this.dataSetNorthwind.產品類別);
            // 產品類別DataGridView停駐表單上方
            this.產品類別DataGridView.Dock = DockStyle.Top;
            // 產品資料DataGridView填滿整個表單
            this.產品資料DataGridView.Dock = DockStyle.Fill;
        }
    }
}
