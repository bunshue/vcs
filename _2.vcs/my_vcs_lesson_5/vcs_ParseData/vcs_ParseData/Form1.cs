using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;   //for IPAddress
using System.Globalization; //for NumberStyles

namespace vcs_ParseData
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                int value = int.Parse(textBox1.Text);
                richTextBox1.Text += value.ToString() + "\n";
            }
            catch
            {
                richTextBox1.Text += "Error\n";
            }
            richTextBox1.Text += "得到int數字： " + int.Parse(textBox1.Text) + "\n";
        }
        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "得到float數字： " + float.Parse(textBox2.Text) + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "得到double數字： " + double.Parse(textBox3.Text) + "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            try
            {   //可能會產生錯誤的程式區段
                DateTime dt = DateTime.Parse(textBox4.Text);
                richTextBox1.Text += dt.ToString() + "\n";
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                MessageBox.Show(ex.Message);
            }
            finally
            {
                //一定會被執行的程式區段
                richTextBox1.Text += "DateTime.Parse完成\n";
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            int number = 0;
            bool conversionSuccessful = int.TryParse(textBox1.Text, out number);    //out為必須
            if (conversionSuccessful == true)
                richTextBox1.Text += "得到int數字： " + number + "\n";
            else
                richTextBox1.Text += "int.TryParse 失敗\n";
        }

        private void button7_Click(object sender, EventArgs e)
        {
            float number = 0;
            bool conversionSuccessful = float.TryParse(textBox2.Text, out number);    //out為必須
            if (conversionSuccessful == true)
                richTextBox1.Text += "得到float數字： " + number + "\n";
            else
                richTextBox1.Text += "float.TryParse 失敗\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            double number = 0;
            bool conversionSuccessful = double.TryParse(textBox3.Text, out number);    //out為必須
            if (conversionSuccessful == true)
                richTextBox1.Text += "得到double數字： " + number + "\n";
            else
                richTextBox1.Text += "double.TryParse 失敗\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Now;
            bool conversionSuccessful = DateTime.TryParse(textBox4.Text, out dt);    //out為必須
            if (conversionSuccessful == true)
                richTextBox1.Text += "得到DateTime資料： " + dt.ToString() + "\n";
            else
                richTextBox1.Text += "DateTime.TryParse 失敗\n";
        }

        private void button11_Click(object sender, EventArgs e)
        {
            try
            {   //可能會產生錯誤的程式區段
                //將IP位址字串轉換為IPAddress類別
                IPAddress ipAddr = IPAddress.Parse(textBox5.Text);
                richTextBox1.Text += ipAddr.ToString() + "\n";
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                MessageBox.Show(ex.Message);
            }
            finally
            {
                //一定會被執行的程式區段
                richTextBox1.Text += "IPAddress.Parse完成\n";
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            IPAddress ipAddr;

            //將IP位址字串轉換為IPAddress類別
            bool conversionSuccessful = IPAddress.TryParse(textBox5.Text, out ipAddr);    //out為必須
            if (conversionSuccessful == true)
                richTextBox1.Text += "得到IPAddress資料： " + ipAddr.ToString() + "\n";
            else
                richTextBox1.Text += "IPAddress.TryParse 失敗\n";
        }

        private void button12_Click(object sender, EventArgs e)
        {
            DateTime timeBirth;
            string birthstr = "6/10/1989 3:50:59 AM";
            timeBirth = DateTime.Parse(birthstr);
            richTextBox1.Text += "日期變數 : " + timeBirth + "\n";
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //long number = long.Parse(textBox6.Text);    //無法解讀逗號
            long number = long.Parse(textBox6.Text, NumberStyles.Any);
            richTextBox1.Text += "取得數字:\t" + number.ToString() + "\n";
        }

        private void button14_Click(object sender, EventArgs e)
        {
            // Default parsing behavior.
            try
            {
                decimal value = decimal.Parse(textBox7.Text);
                richTextBox1.Text += value.ToString("C") + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }

            // Parse with Any format.
            try
            {
                decimal value = decimal.Parse(textBox7.Text, NumberStyles.Any);
                richTextBox1.Text += value.ToString("C") + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }

            double value2;
            if (!double.TryParse(textBox7.Text, out value2))
                value2 = -1;

            decimal currency;
            if (!decimal.TryParse(textBox7.Text, NumberStyles.Any, null, out currency))
                currency = -1;

            richTextBox1.Text += "Value: " + value2.ToString() + "\n";
            richTextBox1.Text += "Currency: " + currency.ToString() + "\n";


        }

        private void button15_Click(object sender, EventArgs e)
        {
            textBox6.Text = "123456";

            long number;
            bool conversionSuccessful = long.TryParse(textBox6.Text, out number);   //out為必須
            if (conversionSuccessful == true)
                richTextBox1.Text += "得到int數字： " + number + "\n";
            else
                richTextBox1.Text += "long.TryParse 失敗\n";
        }
    }
}
