using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.OleDb;

namespace vcs_DB_Access1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The connection object.
        private OleDbConnection Conn;

        // The table's column names.
        private List<string> ColumnNames = new List<string>();
        private string TableName = "";

        // The query controls.
        private ComboBox[] CboField, CboOperator;
        private TextBox[] TxtValue;
        private List<Type> DataTypes = new List<Type>();

        // Make a list of the table's fields.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Compose the database file name.
            // This assumes it's in the executable's directory.
            string filename = @"C:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\__db\_access\Books.accdb";

            // Prepare the form for use.
            PrepareForm(filename, "BookInfo");
        }

        // Make a list of the table's field names and prepare the first ComboBox.
        private void PrepareForm(string db_name, string table_name)
        {
            TableName = table_name;

            // Make the connection object.
            Conn = new OleDbConnection(
                "Provider=Microsoft.ACE.OLEDB.12.0;" +
                "Data Source=" + db_name + ";" +
                "Mode=Share Deny None");

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

        // Build and execute the appropriate query.
        private void btnQuery_Click(object sender, EventArgs e)
        {
            string where_clause = "";
            for (int i = 0; i < CboField.Length; i++)
            {
                // See if the field and operator are non-blank.
                if ((CboField[i].SelectedIndex <= 0) ||
                    (CboOperator[i].SelectedIndex <= 0))
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
                    where_clause += " AND " +
                        CboField[i].SelectedItem.ToString() + " " +
                        CboOperator[i].SelectedItem.ToString() + " " +
                        delimiter + value + delimiter;
                }   // if field and operator are selected.
            }   // for (int i = 0; i < CboField.Length; i++)

            // If where_clause is non-blank, remove the initial " AND ".
            if (where_clause.Length > 0) where_clause = where_clause.Substring(5);

            // Compose the query.
            string query = "SELECT * FROM " + TableName;
            if (where_clause.Length > 0) query += " WHERE " + where_clause;
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
            dgvBookInfo.DataSource = data_table;
        }
    }
}
