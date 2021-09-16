using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.OleDb;

namespace xCh10_2_3_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            comboBox1.Items.AddRange(new object[] {
            "宜蘭",
            "台北",
            "桃園",
            "新竹",
            "苗栗",
            "台中",
            "南投",
            "高雄",
            "屏東",
            "花蓮"}
            );
        }

        private void button1_Click(object sender, EventArgs e)
        {
            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = @"C:\Northwind.mdb";
            builder["User Id"] = "Admin";
            string queryString = 
                "SELECT * FROM 供應商 WHERE 供應商=@supplier OR 行政區=@district";

            using (OleDbConnection connection = new OleDbConnection(builder.ConnectionString))
            {
                connection.Open();

                OleDbCommand command = new OleDbCommand(queryString, connection);
                OleDbParameter supplierParam = command.Parameters.Add(
                    "@supplier", OleDbType.Char
                    );
                supplierParam.Value = "一心";
                // 以上二道敘述的寫法，可縮寫如下：
                // command.Parameters.Add("@supplier", OleDbType.Char).Value = "一心";

                // 如果有從ComboBox中挑選行政區，則將該值設定給做為篩選條件的distric
                // 否則就提示使用者，並中斷事件這個事件處理程序
                if (comboBox1.SelectedIndex != -1)
                {
                    string district = comboBox1.Items[comboBox1.SelectedIndex].ToString();
                    command.Parameters.AddWithValue("@district", district);
                }
                else
                {
                    MessageBox.Show("請點選行政區");
                    return;
                }

                OleDbDataReader reader = command.ExecuteReader();

                // 建構DataSet及其組成分子
                DataSet NorthwindDataSet = new DataSet();
                DataTable 供應商Table = new DataTable("供應商Table");
                DataColumn aColumn;
                for (int i = 0; i < reader.FieldCount; i++)
                {
                    aColumn = new DataColumn(reader.GetName(i), reader.GetFieldType(i));
                    供應商Table.Columns.Add(aColumn);
                }
                // 加入記錄
                DataRow newRow = null;
                while (reader.Read())
                {
                    newRow = 供應商Table.NewRow();
                    for (int i = 0; i < reader.FieldCount; i++)
                    {
                        newRow[i] = reader.GetValue(i);// 相當於reader[i];
                    }
                    供應商Table.Rows.Add(newRow);
                }
                NorthwindDataSet.Tables.Add(供應商Table);

                // 秀出剛動態建構出來的DataSet 
                dataGridView1.DataSource = NorthwindDataSet.Tables["供應商Table"];
                reader.Close();
            }
        }
    }
}
