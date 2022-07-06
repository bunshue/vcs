using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

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

namespace vcs_DB_Access4
{
    public partial class Form1 : Form
    {
        string db_filename = @"C:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\__db\_access\tt04.mdb";
        string str_connection = string.Empty;
        OleDbConnection db_connection;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //Provider=Microsoft.ACE.OLEDB.12.0;Data Source=" + System.Windows.Forms.Application.StartupPath + "\\mydb.accdb;"  accdb
            //str_connection = @"Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + db_filename+ ";Uid=Admin;Pwd=jcvadmin;";              //有帳號密碼的
            //str_connection = @"Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + db_filename+ ";Jet OLEDB:Database Password=workbill"  //有帳號密碼的
            str_connection = @"Provider=Microsoft.Jet.OLEDB.4.0;" + "Data Source=" + db_filename;
            db_connection = new OleDbConnection(str_connection);

            // 打開數據庫連接
            db_connection.Open();
            MessageBox.Show("打開數據庫連接成功");

            /*
            //建立SQL查询
            OleDbCommand odCommand = db_connection.CreateCommand();

            //3、输入查询语句
            odCommand.CommandText = "select customerID,companyName from Customers";

            //建立读取
            OleDbDataReader odrReader = odCommand.ExecuteReader();

            //查询并显示数据
            while (odrReader.Read())
            {
                //显示取出值(具体显示方式可由自己定义)
                richTextBox1.Text += "\r\t";
                richTextBox1.Text += odrReader["CustomerID"].ToString().PadRight(10, ' ');
                richTextBox1.Text += odrReader["CustomerID"].ToString();
            }

            //关闭连接
            odrReader.Close();
            */


            //以下注释为从一张表中选择数据，然后加载到Listview中
            string str = "select * from TestTable";//加载表中所有数据
            OleDbCommand cmd = new OleDbCommand(str, db_connection);
            OleDbDataReader oldbRed = cmd.ExecuteReader();
            while (oldbRed.Read())  //不调用Read()，将会没有数据。 
            {
                ListViewItem lvi = new ListViewItem(oldbRed[0].ToString());
                lvi.SubItems.Add(oldbRed[1].ToString());
                lvi.SubItems.Add(oldbRed[2].ToString());
                lvi.SubItems.Add(oldbRed[3].ToString());
                lvi.SubItems.Add(oldbRed[4].ToString());
                lvi.SubItems.Add(oldbRed[5].ToString());
                listView1.Items.Add(lvi);
            }
            oldbRed.Close();
            db_connection.Close();  // 關閉數據庫連接
            db_connection.Dispose();
            MessageBox.Show("關閉數據庫連接成功");

        }
    }
}
