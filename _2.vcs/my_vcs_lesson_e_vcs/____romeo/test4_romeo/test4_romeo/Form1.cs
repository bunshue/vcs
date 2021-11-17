using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Microsoft.Win32;

using System.IO;
using System.Net;
using System.Web;

using System.Data.OleDb;    //for OleDbConnection


using System.Runtime.InteropServices;
using System.Resources;

using System.Diagnostics;   //for FileVersionInfo

namespace test4_romeo
{
    public partial class Form1 : Form
    {
        //定義OleDb======================================================
        //1.檔案位置    注意絕對路徑 -> 非 \  是 \\
        //private const string FileName = "C:\\Users\\user\\documents\\visual studio 2010\\Projects\\WindowsFormsApplication1\\WindowsFormsApplication1\\Data\\Book1.xlsx";
        private const string FileName = @"C:\______test_files\__RW\_excel\excel_20210602_131921.xls";
        //2.提供者名稱  Microsoft.Jet.OLEDB.4.0適用於2003以前版本，Microsoft.ACE.OLEDB.12.0 適用於2007以後的版本處理 xlsx 檔案
        //private const string ProviderName = "Microsoft.ACE.OLEDB.12.0;";
        private const string ProviderName = "Microsoft.Jet.OLEDB.4.0;";
        //3.Excel版本，Excel 8.0 針對Excel2000及以上版本，Excel5.0 針對Excel97。
        private const string ExtendedString = "'Excel 8.0;";
        //4.第一行是否為標題
        private const string Hdr = "Yes;";
        //5.IMEX=1 通知驅動程序始終將「互混」數據列作為文本讀取
        private const string IMEX = "0';";
        //=============================================================

        //連線字串
        string cs =
                "Data Source=" + FileName + ";" +
                "Provider=" + ProviderName +
                "Extended Properties=" + ExtendedString +
                "HDR=" + Hdr +
                "IMEX=" + IMEX;
        //Excel 的工作表名稱 (Excel左下角有的分頁名稱)
        string SheetName = "Sheet1";

        
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 15;
            y_st = 15;
            dx = 180;
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            button8.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 4);

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            using (OleDbConnection cn = new OleDbConnection(cs))
            {
                cn.Open();
                string qs = "select * from[" + SheetName + "$]";
                try
                {
                    using (OleDbDataAdapter dr = new OleDbDataAdapter(qs, cn))
                    {
                        DataTable dt = new DataTable();
                        dr.Fill(dt);
                        this.dataGridView1.DataSource = dt;
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
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

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {

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
    }
}

