using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh9_1_1_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void 員工BindingNavigatorSaveItem_Click(object sender, EventArgs e)
        {
            this.Validate();
            this.員工BindingSource.EndEdit();
            this.tableAdapterManager.UpdateAll(this.dataSet1);

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // TODO: 這行程式碼會將資料載入 'dataSet1.員工' 資料表。您可以視需要進行移動或移除。
            this.員工TableAdapter.Fill(this.dataSet1.員工);

        }

        private void bindingNavigatorDeleteItem_Click(object sender, EventArgs e)
        {
            if (MessageBox.Show("是否要刪除？", 
                "小心", MessageBoxButtons.YesNo,
                MessageBoxIcon.Question,
                MessageBoxDefaultButton.Button2) == DialogResult.Yes)
            {
                員工BindingSource.RemoveCurrent();
            }
        }

        private void 員工DataGridView_CellValueChanged(
            object sender, DataGridViewCellEventArgs e)
        {
            if (e.RowIndex == -1)
                return;

            if (e.ColumnIndex == 5)
            {
                string position = (string)
                    員工DataGridView.Rows[e.RowIndex].
                    Cells[e.ColumnIndex].Value;
                switch (position)
                {
                    case "業務代表": break;
                    case "業務協調員": break;
                    case "業務經理": break;
                    case "資深工程師": break;
                    case "副總裁，銷售部門": break;
                    default: MessageBox.Show("職稱不正確，請再確認！"); break;
                }
            }
        }
    }
}
