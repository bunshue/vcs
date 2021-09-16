using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh9_2_2_11
{
    public partial class Form1 : Form
    {
        DataTable table;
        DataColumn column;
        DataRow row;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            MakeDataTable();
            DemonstrateRowVersion();
        }

        private void MakeDataTable()
        {
            table = new DataTable("Table");
            column = new DataColumn("Column");
            table.Columns.Add(column);
            
            for (int i = 0; i < 10; i++)
            {
                row = table.NewRow();
                row["Column"] = "紀錄- " + i;
                table.Rows.Add(row);
            }

            table.AcceptChanges();
        }

        private void PrintView(DataView view, string label)
        {
            textBox1.AppendText(Environment.NewLine);
            textBox1.AppendText(Environment.NewLine + label);

            string result = "";
            for (int i = 0; i < view.Count; i++)
            {
                textBox1.AppendText(Environment.NewLine);
                textBox1.AppendText(view[i]["Column"].ToString());
                result = "DataViewRow.RowVersion值：" + view[i].RowVersion;
                textBox1.AppendText("，" + result);
            }
        }

        private void DemonstrateRowVersion()
        {
            DataView view = new DataView(table);

            table.Rows[1]["Column"] = "物件導向";

            row = table.NewRow();
            row["Column"] = "程式設計";
            table.Rows.Add(row);

            view.RowStateFilter = DataViewRowState.Added |
                DataViewRowState.ModifiedCurrent;
            PrintView(view, "**ModifiedCurrent及Added");

            view.RowStateFilter = DataViewRowState.ModifiedOriginal;
            PrintView(view, "**顯示已被變更的紀錄(ModifiedOriginal)");

            table.Rows[1].Delete();
            table.Rows[2].Delete();
            table.Rows[3].Delete();

            view.RowStateFilter = DataViewRowState.Deleted;
            PrintView(view, "**顯示已被刪除的紀錄(Deleted)");

            view.RowStateFilter = DataViewRowState.CurrentRows;
            PrintView(view, "**紀錄是目前的值(Current)");

            view.RowStateFilter = DataViewRowState.Unchanged;
            PrintView(view, "**紀錄未被變更者(Unchanged)");

            view.RowStateFilter = DataViewRowState.OriginalRows;
            PrintView(view, "**紀錄含有原始值(OriginalRows)");
        }

 
    }
}
