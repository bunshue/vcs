using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SQLite;

namespace vcs_SQLite
{
    public partial class Form1 : Form
    {
        //path of data base
        string path = "data_table.db";
        string cs = @"URI=file:"+Application.StartupPath+ "\\data_table.db"; //database creat debug folder

        SQLiteConnection con;
        SQLiteCommand cmd;
        SQLiteDataReader dr;

        public Form1()
        {
            InitializeComponent();
        }
        //show data in table
        private void data_show()
        {
            var con = new SQLiteConnection(cs);
            con.Open();

            string stm = "SELECT * FROM test";
            var cmd = new SQLiteCommand(stm,con);
            dr = cmd.ExecuteReader();

            while (dr.Read())
            {
                dataGridView1.Rows.Insert(0,dr.GetString(0),dr.GetString(1));
            }
        }

        //create database and table
        private void Create_db()
        {
            if (!System.IO.File.Exists(path))
            {
                SQLiteConnection.CreateFile(path);
                using (var sqlite = new SQLiteConnection(@"Data Source=" + path))
                {
                    sqlite.Open();
                    string sql = "create table test(name varchar(20),id varchar(12))";
                    SQLiteCommand command = new SQLiteCommand(sql,sqlite);
                    command.ExecuteNonQuery();
                }
            }
            else
            {
                Console.WriteLine("Database cannot create");
                return;
            }
        }

        //insert data
        private void Insert_btn_Click(object sender, EventArgs e)
        {
            var con = new SQLiteConnection(cs);
            con.Open();
            var cmd = new SQLiteCommand(con);

            try
            {
                cmd.CommandText = "INSERT INTO test(name,id) VALUES(@name,@id)";

                string NAME = name_txt.Text;
                string ID = id_txt.Text;

                cmd.Parameters.AddWithValue("@name", NAME);
                cmd.Parameters.AddWithValue("@id", ID);

                dataGridView1.ColumnCount = 2;
                dataGridView1.Columns[0].Name = "Name";
                dataGridView1.Columns[1].Name = "Id";
                string[] row = new string[] { NAME, ID };
                dataGridView1.Rows.Add(row);

                cmd.ExecuteNonQuery();

            }
            catch (Exception )
            {
                Console.WriteLine("cannot insert data");
                return;
            }

        }

        // update data
        private void update_btn_Click(object sender, EventArgs e)
        {
            var con = new SQLiteConnection(cs);
            con.Open();

            var cmd = new SQLiteCommand(con);

            try
            {
                cmd.CommandText = "UPDATE test Set id=@Id where name =@Name";
                cmd.Prepare();
                cmd.Parameters.AddWithValue("@Name", name_txt.Text);
                cmd.Parameters.AddWithValue("@Id", id_txt.Text);

                cmd.ExecuteNonQuery();
                dataGridView1.Rows.Clear();
                data_show();

            }
            catch(Exception)
            {
                Console.WriteLine("cannot update data");
                return;
            }
        }

        // delete data
        private void delete_btn_Click(object sender, EventArgs e)
        {
            var con = new SQLiteConnection(cs);
            con.Open();

            var cmd = new SQLiteCommand(con);

            try
            {
                cmd.CommandText = "DELETE FROM test where name =@Name";
                cmd.Prepare();
                cmd.Parameters.AddWithValue("@Name", name_txt.Text);

                cmd.ExecuteNonQuery();
                dataGridView1.Rows.Clear();
                data_show();
            }
            catch (Exception)
            {
                Console.WriteLine("cannot delete data");
                return;
            }
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            if (dataGridView1.Rows[e.RowIndex].Cells[e.ColumnIndex].Value !=null)
            {
                dataGridView1.CurrentRow.Selected = true;
                name_txt.Text = dataGridView1.Rows[e.RowIndex].Cells["Name"].FormattedValue.ToString();
                id_txt.Text = dataGridView1.Rows[e.RowIndex].Cells["Id"].FormattedValue.ToString();
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Create_db();
            data_show();
        }
    }
}
