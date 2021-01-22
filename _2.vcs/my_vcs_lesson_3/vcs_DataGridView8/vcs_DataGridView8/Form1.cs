using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.OleDb;

namespace vcs_DataGridView8
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The DataAdapters and the DataSet.
        private OleDbDataAdapter DaAddresses, DaTestScores;
        private DataSet DsContacts;

        private void Form1_Load(object sender, EventArgs e)
        {
            const string SELECT_ADDRESSES = "SELECT * FROM Addresses";
            const string SELECT_TEST_SCORES = "SELECT * FROM TestScores";

            // Get the database file name.
            // This assumes the database is in the executable directory.
            string db_name = Application.StartupPath + "\\Contacts.mdb";

            // Compose the connection string.
            string connect_string =
                "Provider=Microsoft.ACE.OLEDB.12.0;" +
                "Data Source=" + db_name + ";" +
                "Persist Security Info=False";

            // Create a DataAdapter to load the Addresses table.
            DaAddresses = new OleDbDataAdapter(SELECT_ADDRESSES, connect_string);

            // Create a DataAdapter to load the Addresses table.
            DaTestScores = new OleDbDataAdapter(SELECT_TEST_SCORES, connect_string);

            // Create and fill the DataSet.
            DsContacts = new DataSet("ContactsDataSet");
            DaAddresses.Fill(DsContacts, "Addresses");
            DaTestScores.Fill(DsContacts, "TestScores");

            // Bind the DataGrid to the DataSet.
            dgContacts.DataSource = DsContacts;
        }

        // Save changes to the data.
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            // Use a CommandBuilder to make the INSERT,
            // UPDATE, and DELETE commands as needed.
            OleDbCommandBuilder command_builder;
            command_builder = new OleDbCommandBuilder(DaAddresses);
            command_builder = new OleDbCommandBuilder(DaTestScores);

            // Update the database.
            try
            {
                DaAddresses.Update(DsContacts, "Addresses");
                DaTestScores.Update(DsContacts, "TestScores");
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
    }
}
