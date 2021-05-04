using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace 產品管理
{
    public partial class frmRelation : Form
    {
        public frmRelation()
        {
            InitializeComponent();
        }

        //建立MyDBClass類別物件db，來管理Database1.mdf資料庫
        MyDBClass db = new MyDBClass();

        //表單載入時執行
        private void frmRelation_Load(object sender, EventArgs e)
        {
            dgvCategory.DataSource = db.GetCategory();
            dgvCategory.Dock = DockStyle.Top;
            dgvProduct.Dock = DockStyle.Fill;
            //取得目前產品類別dgvCategory所選取記錄的第一欄資料，即類別編號
            //並指定給CategoryId整數變數
            int CategoryId = int.Parse(dgvCategory.CurrentRow.Cells[0].Value.ToString());
            //呼叫GetProduct()方法並傳入類別編號CategoryId來取得該類別相對應的產品資料
            //接著將產品資料顯示在dgvProduct上
            dgvProduct.DataSource = db.GetProduct(CategoryId);
        }
        //產品類別dgvCategory上按一下執行
        private void dgvCategory_Click(object sender, EventArgs e)
        {
            try
            {
                int CategoryId = int.Parse(dgvCategory.CurrentRow.Cells[0].Value.ToString());
                dgvProduct.DataSource = db.GetProduct(CategoryId);
            }
            catch (Exception ex)
            { }
        }
    }
}
