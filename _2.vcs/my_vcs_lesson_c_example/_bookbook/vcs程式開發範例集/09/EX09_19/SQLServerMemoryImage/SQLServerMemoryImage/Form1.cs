using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;
using System.IO;

namespace SQLServerMemoryImage
{
    public partial class Form1 : Form
    {
        SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09");
        byte[] imgBytesIn;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string[] strSex = { "男", "女" };
            this.comboBox1.DataSource = strSex;
            string strSql = "select 員工編號,姓名,性別,籍貫,電話,部門名稱 from 員工訊息";
            this.dataGridView1.DataSource = DataBinding(strSql).DefaultView;
            this.button1.Enabled = false;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            setValue();
            insertInfo();
            string strSql = "select 員工編號,姓名,性別,籍貫,電話,部門名稱 from 員工訊息";
            this.dataGridView1.DataSource = DataBinding(strSql).DefaultView;
        }

        private void pictureBox1_DoubleClick(object sender, EventArgs e)
        {
            this.openFileImage.ShowDialog();
        }

        private void openFileImage_FileOk(object sender, CancelEventArgs e)
        {
            try
            {
                this.pictureBox1.Image = Image.FromStream(this.openFileImage.OpenFile());
                string strimg = openFileImage.FileName.ToString();
                FileStream fs = new FileStream(strimg, FileMode.Open, FileAccess.Read);
                BinaryReader br = new BinaryReader(fs);
                imgBytesIn = br.ReadBytes((int)fs.Length);
            }
            catch
            {
                MessageBox.Show("您選擇的圖片不能被讀取或文件類型不對！", "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                this.pictureBox1.Image = null;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void dataGridView1_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            string str = this.dataGridView1[0, e.RowIndex].Value.ToString();
            if (str != "")
            {
                string strSql = "select * from 員工訊息 where 員工編號='" + str + "'";
                DataTable dt = DataBinding(strSql);
                if (dt.Rows.Count > 0)
                {
                    NumID = dt.Rows[0][0].ToString();
                    name = dt.Rows[0][1].ToString();
                    pic = (byte[])dt.Rows[0][2];
                    sex = dt.Rows[0][3].ToString();
                    birthday = dt.Rows[0][4].ToString();
                    city = dt.Rows[0][5].ToString();
                    years = Convert.ToInt16(dt.Rows[0][6].ToString());
                    phone = dt.Rows[0][7].ToString();
                    part = dt.Rows[0][8].ToString();
                }
            }

            getValue();
        }

        //#region method
        private bool insertInfo()
        {
            try
            {
                con.Open();
                StringBuilder strSql = new StringBuilder();
                strSql.Append("insert into 員工訊息 values(@員工編號,");
                strSql.Append("@姓名,@照片,@性別,@出生日期,@籍貫,@工齡,@電話,");
                strSql.Append("@部門名稱)");
                SqlCommand cmd = new SqlCommand(strSql.ToString(), con);
                cmd.Parameters.Add("@員工編號", SqlDbType.Text).Value = NumID;
                cmd.Parameters.Add("@姓名", SqlDbType.Text).Value = name;
                cmd.Parameters.Add("@照片", SqlDbType.Binary).Value = pic;
                cmd.Parameters.Add("@性別", SqlDbType.Text).Value = sex;
                cmd.Parameters.Add("@出生日期", SqlDbType.Text).Value = birthday;
                cmd.Parameters.Add("@籍貫", SqlDbType.Text).Value = city;
                cmd.Parameters.Add("@工齡", SqlDbType.Int).Value = years;
                cmd.Parameters.Add("@電話", SqlDbType.Text).Value = phone;
                cmd.Parameters.Add("@部門名稱", SqlDbType.Text).Value = part;
                cmd.ExecuteNonQuery();
                con.Close();
                MessageBox.Show("OK");
                this.button3.Enabled = true;
                this.button1.Enabled = false;
                return true;
            }
            catch (Exception ey)
            {
                this.button1.Enabled = true;
                this.button2.Enabled = false;
                return false;
            }
        }

        private void setValue()
        {
            NumID = this.textBox2.Text;
            name = this.textBox3.Text;
            pic = imgBytesIn;
            sex = comboBox1.Text;
            birthday = this.textBox4.Text;
            city = this.textBox5.Text;
            years = Convert.ToInt16(this.textBox6.Text);
            phone = this.textBox7.Text;
            part = this.textBox8.Text;
        }

        private void getValue()
        {
            this.textBox2.Text = NumID;
            this.textBox3.Text = name;
            MemoryStream ms = new MemoryStream(pic);			//二進制流
            this.pictureBox1.Image = Image.FromStream(ms);
            comboBox1.Text = sex;
            this.textBox4.Text = birthday;
            this.textBox5.Text = city;
            this.textBox6.Text = years.ToString();
            this.textBox7.Text = phone;
            this.textBox8.Text = part;
        }

        private DataTable DataBinding(string Sql)
        {
            using (SqlDataAdapter da = new SqlDataAdapter())
            {
                SqlCommand cmd = new SqlCommand();
                cmd.Connection = con;
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.CommandText = "proc_select";
                cmd.Parameters.Add("@Sql", SqlDbType.VarChar, 500).Value = Sql;
                da.SelectCommand = cmd;
                DataTable dt = new DataTable();
                da.Fill(dt);
                return dt;
            }
        }

        private void clearText()
        {
            foreach (Control cl in this.groupBox1.Controls)
            {
                if (cl is TextBox)
                {
                    cl.Text = "";
                }
            }
        }
        //#endregion

        //#region//存取器
        private string 員工編號;
        private string 姓名;
        private byte[] 照片;
        private string 性別;
        private string 出生日期;
        private string 籍貫;
        private int 工齡;
        private string 電話;
        private string 部門名稱;
        private string NumID
        {
            get { return 員工編號; }
            set { 員工編號 = value; }
        }
        private string name
        {
            get { return 姓名; }
            set { 姓名 = value; }
        }
        private byte[] pic
        {
            get { return 照片; }
            set { 照片 = value; }
        }
        private string sex
        {
            get { return 性別; }
            set { 性別 = value; }
        }
        private string birthday
        {
            get { return 出生日期; }
            set { 出生日期 = value; }
        }
        private string city
        {
            get { return 籍貫; }
            set { 籍貫 = value; }
        }
        private int years
        {
            get { return 工齡; }
            set { 工齡 = value; }
        }
        private string phone
        {
            get { return 電話; }
            set { 電話 = value; }
        }
        private string part
        {
            get { return 部門名稱; }
            set { 部門名稱 = value; }
        }
        //#endregion

        private void button3_Click(object sender, EventArgs e)
        {
            this.button1.Enabled = true;
            this.button3.Enabled = false;
            imgBytesIn = null;
            clearText();
        }
    }
}
