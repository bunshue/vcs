using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Reflection;    //for Assembly

namespace vcs_Class5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

            List<Student> students = Data.GetStudents();

            //List to DataTable conversion
            DataTable studentTbl = students.ToDataTable();

            //DataTable to List conversion
            List<Student> newStudents = studentTbl.ToList<Student>();//ExtensionUtility.ToList<Student>(newStudents);
            this.dataGridView1.DataSource = newStudents;

            //List to DataTable conversion
            DataTable teacherTbl = Data.DbNullInt();
            //DataTable to List conversion
            List<Teacher> newTeachers = teacherTbl.ToList<Teacher>();


            this.dataGridView2.DataSource = newTeachers;


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

    public static class ExtensionUtility
    {

        /// <summary>
        /// Converts List To DataTable
        /// </summary>
        /// <typeparam name="TSource"></typeparam>
        /// <param name="data"></param>
        /// <returns></returns>
        public static DataTable ToDataTable<TSource>(this IList<TSource> data)
        {
            DataTable dataTable = new DataTable(typeof(TSource).Name);
            PropertyInfo[] props = typeof(TSource).GetProperties(BindingFlags.Public | BindingFlags.Instance);
            foreach (PropertyInfo prop in props)
            {
                dataTable.Columns.Add(prop.Name, Nullable.GetUnderlyingType(prop.PropertyType) ?? prop.PropertyType);
            }

            foreach (TSource item in data)
            {
                var values = new object[props.Length];
                for (int i = 0; i < props.Length; i++)
                {
                    values[i] = props[i].GetValue(item, null);
                }
                dataTable.Rows.Add(values);
            }
            return dataTable;
        }


        /// <summary>
        /// Converts DataTable To List
        /// </summary>
        /// <typeparam name="TSource"></typeparam>
        /// <param name="dataTable"></param>
        /// <returns></returns>
        public static List<TSource> ToList<TSource>(this DataTable dataTable) where TSource : new()
        {
            var dataList = new List<TSource>();

            const BindingFlags flags = BindingFlags.Public | BindingFlags.Instance | BindingFlags.NonPublic;
            var objFieldNames = (from PropertyInfo aProp in typeof(TSource).GetProperties(flags)
                                 select new { Name = aProp.Name, Type = Nullable.GetUnderlyingType(aProp.PropertyType) ?? aProp.PropertyType }).ToList();
            var dataTblFieldNames = (from DataColumn aHeader in dataTable.Columns
                                     select new { Name = aHeader.ColumnName, Type = aHeader.DataType }).ToList();
            var commonFields = objFieldNames.Intersect(dataTblFieldNames).ToList();

            foreach (DataRow dataRow in dataTable.AsEnumerable().ToList())
            {
                var aTSource = new TSource();
                foreach (var aField in commonFields)
                {
                    PropertyInfo propertyInfos = aTSource.GetType().GetProperty(aField.Name);
                    var value = (dataRow[aField.Name] == DBNull.Value) ? null : dataRow[aField.Name]; //if database field is nullable
                    propertyInfos.SetValue(aTSource, value, null);
                }
                dataList.Add(aTSource);
            }
            return dataList;
        }
    }

}
