using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using Bottom_Control.PLC通讯协议;
using Bottom_Control.基本控件;

namespace Bottom_Control
{
    public partial class Form2 : Form
    {
        public enum Button_state
        {
            Off, ON
        }

        public Form2()
        {
            InitializeComponent();
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            this.plC_Open_Time1.Enabled = true;
            this.plC_Open_Time1.Start();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            IPLC_interface mitsubishi = new Mitsubishi_realize();//实例化接口--实现三菱在线访问
            if (mitsubishi.PLC_ready)//PLC是否准备完成
            {
                richTextBox1.Text += "三菱PLC ready\n";

                //Button_write_select(Button.Pattern.ToString(), mitsubishi, Button);//根据按钮模式进行写入操作

                richTextBox1.Text += "read_M, name = " + daButton1.PLC_Contact + ", id = " + daButton1.PLC_Address + "\n";

                List<bool> data = mitsubishi.PLC_read_M_bit(daButton1.PLC_Contact, daButton1.PLC_Address);//读取状态

                richTextBox1.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

                Button_state button_State = Button_state.Off;//按钮状态

                button_State = data[0] == true ? Button_state.ON : Button_state.Off;
                //button_state(button, button_State);

                richTextBox1.Text += "button_State = " + button_State.ToString() + "\n";

                //string dddd = mitsubishi.PLC_read_D_register(button_base.PLC_Contact, button_base.PLC_Address, numerical_format.Hex_16_Bit);
                string dddd = mitsubishi.PLC_read_D_register("M", "10000", numerical_format.Signed_16_Bit);
                richTextBox1.Text += "data : " + dddd + "\n";

            }
            else
            {
                richTextBox1.Text += "三菱PLC 不 ready\n";
            }



        }
    }
}
