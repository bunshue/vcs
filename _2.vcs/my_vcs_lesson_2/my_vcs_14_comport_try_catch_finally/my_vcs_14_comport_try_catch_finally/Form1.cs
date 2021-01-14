using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace my_vcs_14_comport_try_catch_finally
{
    public partial class Form1 : Form
    {
        string RxString;

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            serialPort1.PortName = textBox1.Text;
            serialPort1.BaudRate = int.Parse(textBox2.Text);

            //serialPort1.Open(); //原本是這一行，改成以下16行。
            try
            {   //可能會產生錯誤的程式區段
                serialPort1.Open();
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                MessageBox.Show(ex.Message);
            }
            finally
            {
                //一定會被執行的程式區段
                if (serialPort1.IsOpen)
                    MessageBox.Show("已經連上" + serialPort1.PortName);
                else
                    MessageBox.Show("連結Comport失敗");
            }

            if (serialPort1.IsOpen)
            {
                button1.Enabled = false;
                button2.Enabled = true;
                richTextBox1.ReadOnly = false;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen)
            {
                serialPort1.Close();
                button1.Enabled = true;
                button2.Enabled = false;
                richTextBox1.ReadOnly = true;
            }
        }

        private void richTextBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            // If the port is closed, don't try to send a character.
            if (!serialPort1.IsOpen) return;

            // If the port is Open, declare a char[] array with one element.
            char[] buff = new char[1];

            // Load element 0 with the key character.
            buff[0] = e.KeyChar;

            // Send the one character buffer.
            serialPort1.Write(buff, 0, 1);

            // Set the KeyPress event as handled so the character won't
            // display locally. If you want it to display, omit the next line.
            e.Handled = true;
        }

        private void DisplayText(object sender, EventArgs e)
        {
            richTextBox1.AppendText(RxString);
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void serialPort1_DataReceived(object sender, System.IO.Ports.SerialDataReceivedEventArgs e)
        {
            RxString = serialPort1.ReadExisting();
            this.Invoke(new EventHandler(DisplayText));
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            MessageBox.Show("從my_vcs_03改來，try-catch-finally範例，測試comport連接錯誤狀況");
        }

        // Perform the calculation.
        private void btnCalculate_Click(object sender, EventArgs e)
        {
            // Clear the result (in case the calculation fails).
            txtResult.Clear();

            try
            {
                // Perform the operations that might fail.
                int x = int.Parse(txtX.Text);
                int y = int.Parse(txtY.Text);
                float result = x / y;
                txtResult.Text = result.ToString();
            }
            catch (FormatException)
            {
                // A formatting error occurred.
                // Report the error to the user.
                richTextBox2.Text += "數值錯誤\n";
            }
            catch (Exception ex)
            {
                // Some other error occurred.
                // Report the error to the user.
                richTextBox2.Text += "計算錯誤\t原因 : " + ex + "\n";
                richTextBox2.Text += "計算錯誤\t原因 : " + ex.GetType().Name + "\n";
            }
            finally
            {
                richTextBox2.Text += "計算結束\n";
            }
        }
    }
}
