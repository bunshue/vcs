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

namespace xCh10_3_21
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            comboBox1.Items.AddRange(
                new object[] {
                    "宜蘭市",
                    "台北市",
                    "台北縣",
                    "桃園縣",
                    "新竹市",
                    "苗栗縣",
                    "台中市",
                     "南投縣市",
                     "高雄市",
                     "屏東縣",
                     "屏東市",
                     "花蓮市"}
                     );
        }

        private void button1_Click(object sender, EventArgs e)
        {
            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = @"C:\Northwind.mdb";
            builder["User Id"] = "Admin";

            using (OleDbConnection connection = new OleDbConnection(builder.ConnectionString))
            {
                connection.Open();

                OleDbCommand command;
                command = new OleDbCommand(
                    "SELECT * FROM 客戶 " + "WHERE 城市 = ?", connection);
                command.Parameters.Add("城市", OleDbType.VarChar, 6);

                string cityParam = comboBox1.Items[comboBox1.SelectedIndex].ToString();
                command.Parameters["城市"].Value = cityParam;

                OleDbDataAdapter myAdapter = new OleDbDataAdapter();
                myAdapter.SelectCommand = command;

                // 建構DataSet及其組成分子
                DataSet NorthwindDataSet = new DataSet();
                myAdapter.Fill(NorthwindDataSet, "客戶Table");

                // 秀出剛動態建構出來的DataSet 
                dataGridView1.DataSource = NorthwindDataSet.Tables["客戶Table"];
            }
        }
    }
}
