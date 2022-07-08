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
using System.Text.RegularExpressions;
using System.Threading;

using System.Xml;

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

        private void button3_Click(object sender, EventArgs e)
        {
            //read_xml.xml

            string filename = @"../../read_xml.xml";


            //XDocument doc = XDocument.Load(Server.MapPath("html5Reader/ReaderData.xml")); 
            StringBuilder sb = new StringBuilder();
            XmlDocument dc = new XmlDocument();
            dc.Load(filename);

            XmlNodeList xnl = dc.SelectNodes("chapter");
            sb.Append("<ul>");
            readxml(xnl, sb);
            sb.Append("</ul>");


            richTextBox1.Text += sb.ToString() + "\n";
            //this.html.InnerHtml = sb.ToString(); 

        }

        private void readxml(XmlNodeList xmlnl, StringBuilder sb_)
        {
            richTextBox1.Text += "rrrrrr len = " + xmlnl.Count.ToString() + "\n";
            foreach (XmlNode xl in xmlnl)
            {
                if (xl.ChildNodes.Count == 0)
                {
                    sb_.Append("<li><a>" + xl.Attributes["value"].Value + "</a></li>");
                    richTextBox1.Text += "11111";
                }
                else
                {
                    sb_.Append("<li><a>" + xl.Attributes["value"].Value + "</a><ul>");
                    readxml(xl.ChildNodes, sb_);
                    sb_.Append("</ul></li>");
                    richTextBox1.Text += "22222";
                }
            }
        }







        public class Student
        {
            public long Id { get; set; }
            public string Name { get; set; }
            public short Age { get; set; }
            public DateTime DateOfCreation { get; set; }
            public bool? IsActive { get; set; }
        }

        public class Teacher
        {
            public long Id { get; set; }
            public string Name { get; set; }
            public Nullable<int> DepartmentId { get; set; }
        }


        public class Data
        {
            public static List<Student> GetStudents()
            {
                var list = new List<Student>
        {
            new Student {Id = 1, Name = "Smith", Age = 18, DateOfCreation = DateTime.Now, IsActive = true},
            new Student {Id = 2, Name = "Hook", Age = 16, DateOfCreation = DateTime.Now.AddDays(-1), IsActive = true},
            new Student {Id = 3, Name = "Jhon", Age = 15, DateOfCreation = DateTime.Now.AddDays(-2), IsActive = true},
            new Student {Id = 4, Name = "Alan", Age = 21, DateOfCreation = DateTime.Now.AddDays(-3), IsActive = true}
        };
                return list;
            }

            public static List<Teacher> GetTeachers()
            {
                var list = new List<Teacher>
        {
            new Teacher {Id = 1, Name = "Smith", DepartmentId = 18 },
            new Teacher {Id = 2, Name = "Hook", DepartmentId = 16 },
            new Teacher {Id = 3, Name = "Jhon", DepartmentId = 15 },
            new Teacher {Id = 4, Name = "Alan", DepartmentId = 21 }
        };
                return list;
            }

            public static DataTable DbNullInt()
            {
                DataTable table = new DataTable();
                table.Columns.Add("Id", typeof(long));
                table.Columns.Add("Name", typeof(string));

                DataColumn column;
                column = new DataColumn("DepartmentId", System.Type.GetType("System.Int32"));
                column.AllowDBNull = true;
                table.Columns.Add(column);

                table.Rows.Add(1, "Smith", DBNull.Value);
                table.Rows.Add(2, "Hook", 1);


                return table;
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            /*
            List<Student> students = Data.GetStudents();
            
           //List to DataTable conversion
            DataTable studentTbl = students.ToDataTable();
            
             * //DataTable to List conversion
            List<Student> newStudents = studentTbl.ToList<Student>();//ExtensionUtility.ToList<Student>(newStudents);
            this.dataGridView1.DataSource = newStudents;

            //List to DataTable conversion
            DataTable teacherTbl = Data.DbNullInt();
            //DataTable to List conversion
            List<Teacher> newTeachers = teacherTbl.ToList<Teacher>();


            this.dataGridView2.DataSource = newTeachers;
            */

        }


    }
}

