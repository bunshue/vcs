using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.IO;
using System.Linq;
using System.Data.SqlClient;

namespace RemotingClass
{
    public partial class FarClass : Form
    {
        public static int i;
        SqlConnection conn;
        public FarClass()
        {
            InitializeComponent();
            conn = new SqlConnection();
            conn.ConnectionString = "Data Source=localhost;Database=test;User ID=sa;Password=";
        }
        public int GetTime()
        {
            StreamWriter sw = new StreamWriter("hb.txt", true);
            sw.WriteLine("遠程類對像被第" + i + "次呼叫" + DateTime.Now.ToString());
            sw.Close();
            i++;
            MessageBox.Show("遠程類在服務器端對像被"+i+"次呼叫"+DateTime.Now.ToString());
            return i;
        }
        public DataTable GetDataTable(string TableName)
        {
            SqlDataAdapter sda = new SqlDataAdapter("select * from  " + TableName, conn);
            DataSet ds = new DataSet();
            sda.Fill(ds,TableName);
            return ds.Tables[TableName];
        }
        public void UpdateDataTable(DataTable table ,string TableName)
        {
            SqlDataAdapter sda = new SqlDataAdapter("select * from  " + TableName, conn);
            SqlCommandBuilder sqlcb = new SqlCommandBuilder(sda);
            sda.Update(table);
        }
    }
}