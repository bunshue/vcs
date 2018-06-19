using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO.Ports;          //for serial ports

namespace my_vcs_09_ComboBox
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            MessageBox.Show("ComboBox到Items下加選項");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("選擇內容：\ncomport : " + select_comport.Text + "  Baud = " + select_baud.Text + "\ncom_idx : " + select_comport.SelectedIndex + "            Baud_idx : " + select_baud.SelectedIndex);
            //select_comport.Text     選取文字
            //select_baud.Text        選取文字
            //Convert.ToInt32(select_baud.Text) 把文字轉成數字
        }

        string[] COM_Ports_NameArr;
        private void button3_Click(object sender, EventArgs e)
        {
            string[] tempString = SerialPort.GetPortNames();
            Array.Resize(ref COM_Ports_NameArr, tempString.Length);
            tempString.CopyTo(COM_Ports_NameArr, 0);

            comboBox1.Items.Clear();    //Clear All items in Combobox

            foreach (string port in COM_Ports_NameArr)
            {
                //MessageBox.Show("get comport : " + port);
                comboBox1.Items.Add(port);
            }

            if (COM_Ports_NameArr.Length > 0)
                comboBox1.Text = COM_Ports_NameArr[0];

        }
    }
}
