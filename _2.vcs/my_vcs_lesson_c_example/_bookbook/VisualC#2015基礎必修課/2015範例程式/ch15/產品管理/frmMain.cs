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
    public partial class frmMain : Form
    {
        public frmMain()
        {
            InitializeComponent();
        }

        private void 產品類別管理ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //建立frmCategory子表單物件ChildForm
            frmCategory ChildForm = new frmCategory();
            //將ChildForm變成這個MDI表單的子表單，接著才顯示
            ChildForm.MdiParent = this;
            ChildForm.Show();
        }

        private void 產品資料管理ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            frmProduct ChildForm = new frmProduct();
            ChildForm.MdiParent = this;
            ChildForm.Show();
        }

        private void 產品關聯查詢ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            frmRelation ChildForm = new frmRelation();
            ChildForm.MdiParent = this;
            ChildForm.Show();
        }
    }
}
