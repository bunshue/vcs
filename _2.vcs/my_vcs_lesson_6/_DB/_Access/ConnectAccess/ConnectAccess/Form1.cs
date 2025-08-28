using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Linq;
using System.Data.OleDb;

namespace ConnectAccess
{
    public partial class Form1 : Form
    {
        string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\__db\_access\db_09.mdb";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        //顯示資料庫的內容 ST
        void show_dataset_content(DataSet ds)
        {
            richTextBox1.Text += "顯示資料庫的內容\n";

            richTextBox1.Text += "Tables.Count = " + ds.Tables.Count.ToString() + "\n";
            richTextBox1.Text += "Columns = " + ds.Tables[0].Columns.Count.ToString() + "\n";
            richTextBox1.Text += "Rows = " + ds.Tables[0].Rows.Count.ToString() + "\n";
            richTextBox1.Text += "TableName = " + ds.Tables[0].TableName + "\n\n";

            richTextBox1.Text += "標題\n";
            int i;
            int j;
            int C = ds.Tables[0].Columns.Count;
            int R = ds.Tables[0].Rows.Count;
            for (i = 0; i < C; i++)
            {
                richTextBox1.Text += ds.Tables[0].Columns[i] + "\t";
            }
            richTextBox1.Text += "\n\n";

            richTextBox1.Text += "內容\n";
            for (j = 0; j < R; j++)
            {
                for (i = 0; i < C; i++)
                {
                    richTextBox1.Text += ds.Tables[0].Rows[j].ItemArray[i] + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
        }
        //顯示資料庫的內容 SP

        private void button1_Click(object sender, EventArgs e)
        {
            //"Provider=Microsoft.Jet.OleDb.4.0;"是指數據提供者,這裡使用的是Microsoft Jet引擎,也就是Access中的數據引擎,asp.net就是靠這個和Access的數據庫連接的.
            //"Data Source=XXXXX.mdb"是指明數據源的位置

            string connection_string = "Provider=Microsoft.ACE.OLEDB.12.0;Data source=" + filename;  //sugar
            //string connection_string = "Provider=Microsoft.Jet.OLEDB.4.0;Data source=" + filename;     //kilo

            OleDbConnection connection = new OleDbConnection(connection_string);

            connection.Open();  // 打開數據庫連接

            OleDbDataAdapter OleDat = new OleDbDataAdapter("select * from 帳目", connection);
            DataSet ds = new DataSet();
            OleDat.Fill(ds, "帳目");
            this.dataGridView1.DataSource = ds.Tables[0].DefaultView;   //將所有資料都匯出到dataGridView上

            show_dataset_content(ds);   //顯示資料庫的內容

            connection.Close(); // 關閉數據庫連接

            connection.Dispose();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            return; //TBD

            string connection_string = "Provider=Microsoft.ACE.OLEDB.12.0;Data source=" + filename;  //sugar
            //string connection_string = "Provider=Microsoft.Jet.OLEDB.4.0;Data source=" + filename;     //kilo

            OleDbConnection connection = new OleDbConnection(connection_string);

            OleDbDataReader reader;

            // 獲得Person裡面的所以數據記錄

            string strCommand = "SELECT * FROM Persons";

            connection.Open();  // 打開數據連接

            OleDbCommand cmd = new OleDbCommand(strCommand, connection);

            reader = cmd.ExecuteReader();   //獲得數據集

            //（2）.對列表進行初始化，並使得列表的顯示條件符合數據記錄的條件。需要說明的是在下面源代碼中，lv是在Class中定義的一個ListView的一個實例

            // 初始化ListView

            listView1.Left = 0;

            listView1.Top = 0;

            listView1.Width = 700;

            //listView1.Height = this.ClientRectangle.Height ;

            listView1.GridLines = true;	//顯示各個記錄的分隔線

            listView1.FullRowSelect = true;	//要選擇就是一行

            listView1.View = View.Details;	//定義列表顯示的方式

            listView1.Scrollable = true;	//需要時候顯示滾動條

            listView1.MultiSelect = false; // 不可以多行選擇

            listView1.HeaderStyle = ColumnHeaderStyle.Nonclickable;

            // 針對數據庫的字段名稱，建立與之適應顯示表頭

            listView1.Columns.Add("姓名", 60, HorizontalAlignment.Right);

            listView1.Columns.Add("住宅電話", 100, HorizontalAlignment.Left);


            listView1.Columns.Add("辦公電話", 100, HorizontalAlignment.Left);

            listView1.Columns.Add("移動電話", 100, HorizontalAlignment.Left);

            listView1.Columns.Add("居住地點", 100, HorizontalAlignment.Left);

            listView1.Columns.Add("工作單位", 100, HorizontalAlignment.Left);

            listView1.Columns.Add("電子郵件", 100, HorizontalAlignment.Left);

            listView1.Visible = true;

            while (reader.Read())
            {

                ListViewItem li = new ListViewItem();

                li.SubItems.Clear();

                li.SubItems[0].Text = reader["name"].ToString();

                li.SubItems.Add(reader["HomePhone"].ToString());


                li.SubItems.Add(reader["WorkPhone"].ToString());

                li.SubItems.Add(reader["MobilePhone"].ToString());

                li.SubItems.Add(reader["City"].ToString());

                li.SubItems.Add(reader["Address"].ToString());

                li.SubItems.Add(reader["Email"].ToString());

                listView1.Items.Add(li);

            }


            reader.Close();	//關閉數據集

            connection.Close();	//關閉數據連接

  /*          
如果訪問的數據庫是SQL Server 7.0，只需要把上面源代碼中的一條語句：
private static string strConnect = "Provider = Microsoft.Jet.OLEDB.4.0 ; Data Source = " + Application.StartupPath + "\\MY.MDB" ;
改變成：
private static string strConnect = "Provider=SQLOLEDB.1 ; Persist Security Info=False ; User ID = sa ; Initial Catalog=數據庫名稱; Data Source = 服務器名稱 " ;
即可。
*/

        }
    }
}



