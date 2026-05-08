using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Data.OleDb;    //讀取Access需使用OLEDB

//"Provider=Microsoft.Jet.OleDb.4.0;"是指數據提供者,這裡使用的是Microsoft Jet引擎,也就是Access中的數據引擎,asp.net就是靠這個和Access的數據庫連接的.
//"Data Source=C:BegASPNETNorthwind.mdb"是指明數據源的位置,他的標准形式是"Data Source=MyDrive:MyPathMyFile.MDB".

/*
以将其分为两类，即：关系型数据库（SQL）和非关系型数据库（NoSQL，Not Only SQL）。
关系型数据库：
    大型：Oracle、DB2 等
    中型：SQL Server、MySQL 等
    小型：Access 等

非关系型数据库：
    Memcached、MongoDB 和 Redis 等
*/

namespace vcs_OleDb3_Access
{
    public partial class Form1 : Form
    {
        // 資料庫檔案
        string db_filename = string.Empty;
        // 連接字串
        string cnstr = string.Empty;
        // 查詢字串
        string sqlstr = string.Empty;
        // 連接字串
        // string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\{0};Integrated Security=True;Connect Timeout=30";
        // 工作表名稱
        string sheetName = "Sheet1";
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        private void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            int dd = 26;
            dataGridView1.Size = new Size(510, 380);
            dataGridView2.Size = new Size(510, 380);
            dataGridView3.Size = new Size(420, 380);
            dataGridView4.Size = new Size(420, 380);

            lb_dgv1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            dataGridView1.Location = new Point(x_st + dx * 3, y_st + dy * 0 + dd);
            lb_dgv2.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            dataGridView2.Location = new Point(x_st + dx * 3, y_st + dy * 6 + dd);
            lb_dgv3.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 0);
            dataGridView3.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 0 + dd);
            lb_dgv4.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 6);
            dataGridView4.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 6 + dd);
            lb_dgv1.Text = "";
            lb_dgv2.Text = "";
            lb_dgv3.Text = "";
            lb_dgv4.Text = "";

            richTextBox1.Size = new Size(300, 820);
            richTextBox1.Location = new Point(x_st + dx * 7 + 110, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1920, 890);
            this.Text = "vcs_OleDb3_Access";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            dataGridView1.DataSource = null;  // 設定DGV的資料來源為無, 即清除
            dataGridView2.DataSource = null;  // 設定DGV的資料來源為無, 即清除
            dataGridView3.DataSource = null;  // 設定DGV的資料來源為無, 即清除
            dataGridView4.DataSource = null;  // 設定DGV的資料來源為無, 即清除
            lb_dgv1.Text = "";
            lb_dgv2.Text = "";
            lb_dgv3.Text = "";
            lb_dgv4.Text = "";
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\__db\_access\Books.accdb";

            test(filename, "BookInfo");
        }

        private void test(string db_name, string table_name)
        {
            //TableName = table_name;

            string cnstr = "Provider=Microsoft.ACE.OLEDB.12.0;" + "Data Source=" + db_name + ";" + "Mode=Share Deny None";

            string sqlstr = "SELECT * FROM " + table_name;

            OleDbConnection cn = new OleDbConnection(cnstr);

            richTextBox1.Text += cnstr + "\n\n";

            richTextBox1.Text += "\n\n";

            OleDbCommand cmd = new OleDbCommand();
            cmd.Connection = cn;
            cmd.CommandText = sqlstr;

            cn.Open();

            // 建構DataSet及其組成分子
            DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
            OleDbDataAdapter da = new OleDbDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
            // da.Fill(ds, "table");  // da將查詢的結果填充至數據集ds, 指定TableName為"table"
            da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
            //dataGridView1.DataSource = ds.Tables["table"];  // DGV設置數據源, same
            dataGridView1.DataSource = ds.Tables[0];  // DGV設置數據源
            richTextBox1.Text += "取得資料 : " + ds.Tables[0].Rows.Count.ToString() + " 筆\n";
        }


        //------------------------------------------------------------  # 60個

        // The connection object.
        private OleDbConnection Conn;

        // The table's column names.
        private List<string> ColumnNames = new List<string>();
        private string TableName = "";

        // The query controls.
        private ComboBox[] CboField, CboOperator;
        private TextBox[] TxtValue;
        private List<Type> DataTypes = new List<Type>();

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\__db\_access\Books.accdb";

            PrepareForm(filename, "BookInfo");
        }


        // Make a list of the table's field names and prepare the first ComboBox.
        private void PrepareForm(string db_name, string table_name)
        {
            TableName = table_name;

            // Make the connection object.
            Conn = new OleDbConnection("Provider=Microsoft.ACE.OLEDB.12.0;" + "Data Source=" + db_name + ";" + "Mode=Share Deny None");

            richTextBox1.Text += "Provider=Microsoft.ACE.OLEDB.12.0;" + "Data Source=" + db_name + ";" + "Mode=Share Deny None" + "\n";

            richTextBox1.Text += "\n\n";

            // Get the fields in the BookInfo table.
            // Make a command object to represent the command.
            OleDbCommand cmd = new OleDbCommand();
            cmd.Connection = Conn;
            cmd.CommandText = "SELECT TOP 1 * FROM " + table_name;

            // Open the connection and execute the command.
            try
            {
                // Open the connection.
                Conn.Open();

                // Execute the query. The reader gives access to the results.
                OleDbDataReader reader = cmd.ExecuteReader();

                // Get field information.
                DataTable schema = reader.GetSchemaTable();
                foreach (DataRow schema_row in schema.Rows)
                {
                    ColumnNames.Add(schema_row.Field<string>("ColumnName"));
                    DataTypes.Add(schema_row.Field<Type>("DataType"));
                    // Console.WriteLine(schema_row.Field<Type>("DataType").ToString());
                }

                // Initialize the field name ComboBoxes.
                CboField = new ComboBox[] { cboField0, cboField1, cboField2, cboField3 };
                CboOperator = new ComboBox[] { cboOperator0, cboOperator1, cboOperator2, cboOperator3 };
                TxtValue = new TextBox[] { txtValue0, txtValue1, txtValue2, txtValue3 };

                for (int i = 0; i < CboField.Length; i++)
                {
                    CboField[i].Items.Add("");          // Allow a blank field choice.
                    foreach (string field_name in ColumnNames)
                    {
                        CboField[i].Items.Add(field_name);
                    }
                    CboField[i].SelectedIndex = 0;      // Select the blank choice.
                    CboOperator[i].SelectedIndex = 0;   // Select the blank choice.
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error reading " + table_name + " column names.\n" + ex.Message);
            }
            finally
            {
                // Close the connection whether we succeed or fail.
                Conn.Close();
            }
        }

        //------------------------------------------------------------  # 60個

        private void button2_Click(object sender, EventArgs e)
        {
            string where_clause = "";
            for (int i = 0; i < CboField.Length; i++)
            {
                // See if the field and operator are non-blank.
                if ((CboField[i].SelectedIndex <= 0) || (CboOperator[i].SelectedIndex <= 0))
                {
                    // Don't use this row. Clear it to prevent confusion.
                    CboField[i].SelectedIndex = 0;
                    CboOperator[i].SelectedIndex = 0;
                    TxtValue[i].Clear();
                }
                else
                {
                    // See what delimiter we need for this type of field.
                    string delimiter = "";
                    string value = TxtValue[i].Text;
                    int column_num = CboField[i].SelectedIndex - 1;
                    if (DataTypes[column_num] == typeof(System.String))
                    {
                        delimiter = "'";
                        value = value.Replace("'", "''");
                    }
                    else if (DataTypes[column_num] == typeof(System.DateTime))
                    {
                        // Use # for Access, ' for SQL Server.
                        delimiter = "#";
                    }

                    // Add the constraint to the WHERE clause.
                    where_clause += " AND " + CboField[i].SelectedItem.ToString() + " " + CboOperator[i].SelectedItem.ToString() + " " + delimiter + value + delimiter;
                }   // if field and operator are selected.
            }   // for (int i = 0; i < CboField.Length; i++)

            // If where_clause is non-blank, remove the initial " AND ".
            if (where_clause.Length > 0)
            {
                where_clause = where_clause.Substring(5);
            }

            // Compose the query.
            string query = "SELECT * FROM " + TableName;
            if (where_clause.Length > 0)
            {
                query += " WHERE " + where_clause;
            }
            // Console.WriteLine("Query: " + query);

            // Create a DataAdapter to load the data.
            OleDbDataAdapter data_adapter = new OleDbDataAdapter(query, Conn);

            // Create a DataTable.
            DataTable data_table = new DataTable();
            try
            {
                data_adapter.Fill(data_table);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error executing query " + query + "\n" + ex.Message);
            }

            // Bind the DataGridView to the DataTable.
            dataGridView1.DataSource = data_table;
        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button9_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button10_Click(object sender, EventArgs e)
        {
            //创建数据库连接字符串
            string P_Connection = string.Format("Provider=Microsoft.ACE.OLEDB.12.0;Data Source=..//..//test.mdb;User Id=Admin");    //sugar
            //string P_Connection = string.Format("Provider=Microsoft.Jet.OLEDB.4.0;Data Source=..//..//test.mdb;User Id=Admin");    //kilo
            OleDbDataAdapter P_OLeDbDataAdapter = new OleDbDataAdapter("select au_id as 用户编号,au_lname as 用户名,phone as 联系电话  from authors", P_Connection);
            DataSet ds = new DataSet();
            P_OLeDbDataAdapter.Fill(ds, "UserInfo");
            dataGridView1.DataSource = ds.Tables["UserInfo"].DefaultView;   //將所有資料都匯出到dataGridView上

        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button21_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button22_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button23_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button24_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
        }

        private void button27_Click(object sender, EventArgs e)
        {
        }

        private void button28_Click(object sender, EventArgs e)
        {
        }

        private void button29_Click(object sender, EventArgs e)
        {
            //簡易測試
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

 */


//cmd.CommandText = "SELECT TOP 1 * FROM " + table_name;

