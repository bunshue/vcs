using System;
using System.Collections.Generic;
using System.Text;
using System.Data;
using System.Data.SqlClient;

namespace CallClass
{
    public class DataBaseDAO
    {
        public void UserAccount_Inert(string name, string sex, string age, string address)
        {
            SqlConnection conn = new SqlConnection("Data Source=MR-PC\\YL;Initial Catalog=db_35;User ID=sa");
            conn.Open();
            SqlCommand cmd = new SqlCommand("insert userAccount (name,sex,age,address) values (@name,@sex,@age,@address) ", conn);
            cmd.Parameters.AddWithValue("@name", name);
            cmd.Parameters.AddWithValue("@sex", sex);
            cmd.Parameters.AddWithValue("@age", age);
            cmd.Parameters.AddWithValue("@address", address);
            cmd.ExecuteNonQuery();
            conn.Close();
        }
    }
}
