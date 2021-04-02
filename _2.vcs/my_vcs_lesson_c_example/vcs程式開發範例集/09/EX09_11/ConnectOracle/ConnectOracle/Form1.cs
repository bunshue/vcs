using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.OracleClient;

namespace ConnectOracle
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

      
       protected void button1_Click(object sender, EventArgs e)
        {
            string OrlCon = "Data Source=Oracle9i;Integrated Securite=yes";
            OracleConnection con = new OracleConnection(OrlCon);
            try
            {
                con.Open();
                MessageBox.Show("已成功連接Oracle資料庫");
            }
            catch (Exception ex)
            {
                MessageBox.Show("連接Oracle資料庫失敗");
            }
            finally
            {
                con.Close();
            }
        }


    }
}