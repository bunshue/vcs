using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DBAp2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // ShowRecord方法用來在tsmShow項目上顯示目前巡覽記錄的狀態
        private void ShowRecord()
        {
            tsmShow.Text = (產品資料BindingSource.Position + 1).ToString()
             + "/" + 產品資料BindingSource.Count.ToString();
        }
        // 表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            // TODO: 這行程式碼會將資料載入 'ch16DBDataSet.產品資料' 資料表。
            // 您可以視需要進行移動或移除。
            this.產品資料TableAdapter.Fill(this.ch16DBDataSet.產品資料);
            ShowRecord();// 呼叫ShowRecord方法顯示目前巡覽記錄的狀態
            txtId.MaxLength = 5; 	// 產品編號只能輸入五個字
            txtSpecial.ReadOnly = true;	// 特價欄位唯讀
        }
        // 按功能表的 [巡覽/第一筆] 執行 
        private void 第一筆ToolStripMenuItem_Click
         (object sender, EventArgs e)
        {
            產品資料BindingSource.MoveFirst();
            ShowRecord();
        }
        // 按功能表的 [巡覽/上一筆] 執行 
        private void 上一筆ToolStripMenuItem_Click
         (object sender, EventArgs e)
        {
            產品資料BindingSource.MovePrevious();
            ShowRecord();
        }
        // 按功能表的 [巡覽/下一筆] 執行 
        private void 下一筆ToolStripMenuItem_Click
         (object sender, EventArgs e)
        {
            產品資料BindingSource.MoveNext();
            ShowRecord();
        }
        // 按功能表的 [巡覽/最末筆] 執行 
        private void 最末筆ToolStripMenuItem_Click
         (object sender, EventArgs e)
        {
            產品資料BindingSource.MoveLast();
            ShowRecord();
        }
        // 按功能表的 [編輯/新增] 執行 
        private void 新增ToolStripMenuItem_Click
         (object sender, EventArgs e)
        {
            try
            {
                產品資料BindingSource.AddNew();//在DataSet內新增一筆空的記錄
                ShowRecord();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "錯誤",
                    MessageBoxButtons.OK, MessageBoxIcon.Error);
            }

        }
        // 按功能表的 [編輯/刪除] 執行 
        private void 刪除ToolStripMenuItem_Click
         (object sender, EventArgs e)
        {
            // ˊ刪除DataSet內目前所指的記錄
            產品資料BindingSource.RemoveAt(產品資料BindingSource.Position);
            ShowRecord();
        }
        // 按功能表的 [編輯/更新] 執行 
        private void 更新ToolStripMenuItem_Click
         (object sender, EventArgs e)
        {
            try
            {
                產品資料BindingSource.EndEdit();
                // 將DataSet記憶體編修後的所有記錄一次寫回產品資料表
                產品資料TableAdapter.Update(ch16DBDataSet.產品資料);
                ShowRecord();
                MessageBox.Show("更新成功");
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "錯誤",
                 MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }

}
