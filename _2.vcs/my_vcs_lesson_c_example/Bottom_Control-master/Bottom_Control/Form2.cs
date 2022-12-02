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
using CCWin.SkinClass;

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
                //string dddd = mitsubishi.PLC_read_D_register("M", "10000", numerical_format.Signed_16_Bit);
                string dddd = mitsubishi.PLC_read_D_register("Y", "20", numerical_format.Signed_16_Bit);
                richTextBox1.Text += "len = " + dddd.Length.ToString() + "\t";
                richTextBox1.Text += "data : " + dddd[0] + "\n";

                string contact_point = "M";
                string contact_address = "10000";

                richTextBox1.Text += "\n\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";

                data = mitsubishi.PLC_read_M_bit(contact_point, contact_address);
                richTextBox1.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

                dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.Signed_16_Bit);
                richTextBox1.Text += "a len = " + dddd.Length.ToString() + "\n";
                richTextBox1.Text += "data : " + dddd + "\n";

                dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.String_32_Bit);
                richTextBox1.Text += "b len = " + dddd.Length.ToString() + "\t";
                richTextBox1.Text += "data : " + dddd + "\n\n";
                richTextBox1.Text += "\ndata[0] : " + dddd[0].ToString("X8") + "\n";
                /*
                richTextBox1.Text += "\ndata[1] : " + dddd[1].ToString("X8") + "\n";
                richTextBox1.Text += "\ndata[2] : " + dddd[2].ToString("X8") + "\n";
                richTextBox1.Text += "\ndata[3] : " + dddd[3].ToString("X8") + "\n";
                richTextBox1.Text += "\ndata[4] : " + dddd[4].ToString("X8") + "\n";
                richTextBox1.Text += "\ndata[5] : " + dddd[5].ToString("X8") + "\n";
                richTextBox1.Text += "\ndata[6] : " + dddd[6].ToString("X8") + "\n";
                richTextBox1.Text += "\ndata[7] : " + dddd[7].ToString("X8") + "\n";
                richTextBox1.Text += "\ndata[8] : " + dddd[8].ToString("X8") + "\n";
                richTextBox1.Text += "\ndata[9] : " + dddd[9].ToString("X8") + "\n";
                */
                dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.Signed_32_Bit);
                richTextBox1.Text += "\nc len = " + dddd.Length.ToString() + "\t";
                richTextBox1.Text += "data : " + dddd + "\n";

                dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.Binary_16_Bit);
                richTextBox1.Text += "d len = " + dddd.Length.ToString() + "\t";
                richTextBox1.Text += "data : " + dddd + "\n";

                dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.BCD_32_Bit);
                richTextBox1.Text += "e len = " + dddd.Length.ToString() + "\t";
                richTextBox1.Text += "data : " + dddd + "\n";

                dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.Unsigned_16_Bit);
                richTextBox1.Text += "f len = " + dddd.Length.ToString() + "\t";
                richTextBox1.Text += "data : " + dddd + "\n";

                dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.BCD_16_Bit);
                richTextBox1.Text += "g len = " + dddd.Length.ToString() + "\t";
                richTextBox1.Text += "data : " + dddd + "\n";

                dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.Unsigned_32_Bit);
                richTextBox1.Text += "h len = " + dddd.Length.ToString() + "\t";
                richTextBox1.Text += "data : " + dddd + "\n";

                dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.Hex_16_Bit);
                richTextBox1.Text += "i len = " + dddd.Length.ToString() + "\t";
                richTextBox1.Text += "data : " + dddd + "\n";

                dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.Hex_32_Bit);
                richTextBox1.Text += "j len = " + dddd.Length.ToString() + "\t";
                richTextBox1.Text += "data : " + dddd + "\n";

                dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.Float_32_Bit);
                richTextBox1.Text += "k len = " + dddd.Length.ToString() + "\t";
                richTextBox1.Text += "data : " + dddd + "\n";

                dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.Unsigned_16_Bit);
                richTextBox1.Text += "l len = " + dddd.Length.ToString() + "\t";
                richTextBox1.Text += "data : " + dddd + "\n";

                dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.Unsigned_16_Bit);
                richTextBox1.Text += "m len = " + dddd.Length.ToString() + "\t";
                richTextBox1.Text += "data : " + dddd + "\n";

                int format = 0;
                for (format = 0; format < 20; format++)
                {
                    dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, (numerical_format)format);
                    richTextBox1.Text += "format = "+ format.ToString() + ", len = " + dddd.Length.ToString() + "\t";
                    richTextBox1.Text += "data : " + dddd + "\n";
                    if(dddd.Length>1)
                    {
                        int i;
                        int len = dddd.Length;
                        for (i = 0; i < len; i++)
                        {
                            richTextBox1.Text += "\ndata[" + i.ToString() + "] = " + dddd[i].ToString() + "\n";
                        }

                    }
                }

            }
            else
            {
                richTextBox1.Text += "三菱PLC 不 ready\n";
            }



        }
    }
}
