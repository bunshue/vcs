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
            //讀取 D2000
            string contact_point = "D";
            string contact_address = "2000";
            read_data_from_plc(contact_point, contact_address);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //寫入 D8000
            string contact_point = "D";
            string contact_address = "8000";
            string write_data = tb_data_to_write.Text;

            write_data_to_plc(contact_point, contact_address, write_data);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //讀取 D8000
            string contact_point = "D";
            string contact_address = "8000";
            read_data_from_plc(contact_point, contact_address);
        }

        private void bt_generate_Click(object sender, EventArgs e)
        {
            if (cb_random.Checked == true)
            {
                make_random_data();
            }
            else
            {
                string finalString1 = "ABCDE12345678";
                richTextBox1.Text += "相機序號：" + finalString1 + "\n";
                tb_data_to_write.Text = finalString1;
            }
        }

        void make_random_data()
        {
            //[C#] 產生一組亂數
            //最後產生的finalString就是我們要的亂數,至於亂數長度,你可以調整第二行中8這個數字,如果沒改就是長度8的亂數.
            var chars1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            var chars2 = "0123456789";
            var stringChars1 = new char[13];
            var random = new Random();
            for (int i = 0; i < stringChars1.Length; i++)
            {
                if (i < 2)
                {
                    stringChars1[i] = chars1[random.Next(chars1.Length)];
                }
                else
                {
                    stringChars1[i] = chars2[random.Next(chars2.Length)];
                }
            }
            var finalString1 = new String(stringChars1);
            richTextBox1.Text += "相機序號：" + finalString1 + "\n";
            tb_data_to_write.Text = finalString1;
            return;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //讀取 D2000
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

                string contact_point = "D";
                string contact_address = "2000";
                richTextBox1.Text += "\n\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";
                tb_contact_address.Text = "觸點 : " + contact_point + "\t位址 : " + contact_address;

                data = mitsubishi.PLC_read_M_bit(contact_point, contact_address);
                richTextBox1.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";
                richTextBox1.Text += "\n";

                dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.String_32_Bit);

                tb_data_read.Text = dddd;
                richTextBox1.Text += "b len = " + dddd.Length.ToString() + "\t";
                richTextBox1.Text += "data : " + dddd + "\n";
                richTextBox1.Text += "\n";
                richTextBox1.Text += "data[0] : " + dddd[0].ToString("X8") + "\n";
                richTextBox1.Text += "data[1] : " + dddd[1].ToString() + "\n";
                richTextBox1.Text += "data[2] : " + dddd[2] + "\n";
                richTextBox1.Text += "data[3] : " + dddd[3].ToString("X8") + "\n";
                richTextBox1.Text += "data[4] : " + dddd[4].ToString("X8") + "\n";
                richTextBox1.Text += "data[5] : " + dddd[5].ToString("X8") + "\n";
                richTextBox1.Text += "data[6] : " + dddd[6].ToString("X8") + "\n";
                richTextBox1.Text += "data[7] : " + dddd[7].ToString("X8") + "\n";
                richTextBox1.Text += "data[8] : " + dddd[8].ToString("X8") + "\n";
                richTextBox1.Text += "data[9] : " + dddd[9].ToString("X8") + "\n";
                richTextBox1.Text += "data[10] : " + dddd[10].ToString("X8") + "\n";
                richTextBox1.Text += "data[11] : " + dddd[11].ToString() + "\n";
                richTextBox1.Text += "data[12] : " + dddd[12] + "\n";
                richTextBox1.Text += "data[13] : " + dddd[13].ToString("X8") + "\n";
                richTextBox1.Text += "data[14] : " + dddd[14].ToString("X8") + "\n";
                richTextBox1.Text += "data[15] : " + dddd[15].ToString("X8") + "\n";
                richTextBox1.Text += "data[16] : " + dddd[16].ToString("X8") + "\n";
                richTextBox1.Text += "data[17] : " + dddd[17].ToString("X8") + "\n";
                richTextBox1.Text += "data[18] : " + dddd[18].ToString("X8") + "\n";
                richTextBox1.Text += "data[19] : " + dddd[19].ToString("X8") + "\n";
                richTextBox1.Text += "\n";

                int format = 0;
                for (format = 0; format < 15; format++)
                {
                    dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, (numerical_format)format);
                    richTextBox1.Text += "format = " + format.ToString() + ", len = " + dddd.Length.ToString() + "\t";
                    richTextBox1.Text += "data : " + dddd + "\n";
                    if (dddd.Length > 1)
                    {
                        int i;
                        int len = dddd.Length;
                        for (i = 0; i < len; i++)
                        {
                            richTextBox1.Text += "data[" + i.ToString() + "] = " + dddd[i].ToString() + "\n";
                        }

                    }
                }
            }
            else
            {
                richTextBox1.Text += "三菱PLC 不 ready\n";
            }

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //讀取 Y20
            IPLC_interface mitsubishi = new Mitsubishi_realize();//实例化接口--实现三菱在线访问
            if (mitsubishi.PLC_ready)//PLC是否准备完成
            {
                richTextBox1.Text += "三菱PLC ready\n";

                richTextBox1.Text += "read_M, name = " + daButton1.PLC_Contact + ", id = " + daButton1.PLC_Address + "\n";

                List<bool> data = mitsubishi.PLC_read_M_bit(daButton1.PLC_Contact, daButton1.PLC_Address);//读取状态

                richTextBox1.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

                Button_state button_State = Button_state.Off;//按钮状态

                button_State = data[0] == true ? Button_state.ON : Button_state.Off;
                //button_state(button, button_State);

                richTextBox1.Text += "button_State = " + button_State.ToString() + "\n";

                //string dddd = mitsubishi.PLC_read_D_register(button_base.PLC_Contact, button_base.PLC_Address, numerical_format.Hex_16_Bit);
                //string dddd = mitsubishi.PLC_read_D_register("M", "10000", numerical_format.Signed_16_Bit);

                string contact_point = "Y";
                string contact_address = "20";
                richTextBox1.Text += "\n\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";
                tb_contact_address.Text = "觸點 : " + contact_point + "\t位址 : " + contact_address;

                string dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.Signed_16_Bit);
                richTextBox1.Text += "len = " + dddd.Length.ToString() + "\t";
                richTextBox1.Text += "data : " + dddd[0] + "\n";
            }
            else
            {
                richTextBox1.Text += "三菱PLC 不 ready\n";
            }

        }

        void read_data_from_plc(string contact_point, string contact_address)
        {
            IPLC_interface mitsubishi = new Mitsubishi_realize();//实例化接口--实现三菱在线访问
            if (mitsubishi.PLC_ready)//PLC是否准备完成
            {
                richTextBox1.Text += "三菱PLC ready\n";

                richTextBox1.Text += "\n\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";
                tb_contact_address.Text = "觸點 : " + contact_point + "\t位址 : " + contact_address;

                List<bool> data = mitsubishi.PLC_read_M_bit(contact_point, contact_address);
                richTextBox1.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

                if (data[0] == true)
                {
                    string dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.String_32_Bit);
                    tb_data_read.Text = dddd;
                    richTextBox1.Text += "b len = " + dddd.Length.ToString() + "\t";
                    richTextBox1.Text += "data : " + dddd + "\n\n";
                }
                else
                {
                    tb_data_read.Text = "無資料";

                }
            }
            else
            {
                richTextBox1.Text += "三菱PLC 不 ready\n";
            }
        }
        void write_data_to_plc(string contact_point, string contact_address, string write_data)
        {
            if(write_data.Length==0)
            {
                tb_data_read.Text = "無寫入資料";
                return;
            }

            IPLC_interface mitsubishi = new Mitsubishi_realize();//实例化接口--实现三菱在线访问
            if (mitsubishi.PLC_ready)//PLC是否准备完成
            {
                richTextBox1.Text += "三菱PLC ready\n";

                richTextBox1.Text += "\n\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";
                tb_contact_address.Text = "觸點 : " + contact_point + "\t位址 : " + contact_address;

                string dddd = mitsubishi.PLC_write_D_register(contact_point, contact_address, write_data, numerical_format.String_32_Bit);

                richTextBox1.Text += "cccc len = " + dddd.Length.ToString() + "\t";
                richTextBox1.Text += "data : " + dddd + "\n";
                richTextBox1.Text += "\n";
            }
            else
            {
                richTextBox1.Text += "三菱PLC 不 ready\n";
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            updata_status_data();


            draw_status();

        }

        private const int N = 15;
        int y1_value = 0;
        int y2_value = 0;
        int y3_value = 0;
        int[] y1_data = new int[15];
        int[] y2_data = new int[15];
        int[] y3_data = new int[15];
        int x_st = 0;
        int x_step = 0;
        int h_st = 0;
        int ratio_vr = 0;
        int ratio_duty = 0;
        int ratio_rpm = 0;
        int control_data2 = 0;
        int control_data3 = 0;
        int board_number = 0;
        int loop = 0;
        int loop_old = -1;

        void updata_status_data()
        {
            y1_value = 30;

            for (int i = 0; i < (N - 1); i++)
            {
                y1_data[i] = y1_data[i + 1];
            }
            y1_data[N - 1] = y1_value;
        }

        void draw_status()
        {
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            Bitmap bitmap1 = new Bitmap(W, H);

            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);

            // Create pens.
            Pen redPen = new Pen(Color.Red, 3);
            Pen grayPen = new Pen(Color.Gray, 10);

            Point[] curvePoints = new Point[N];    //一維陣列內有 N 個Point

            int i;
            for (i = 0; i < N; i++)
            {
                curvePoints[i].X = 10 * i;
                curvePoints[i].Y = 155 - (y1_data[i]);
            }
            // Draw lines between original points to screen.
            g.DrawLines(grayPen, curvePoints);   //畫直線
            // Draw curve to screen.
            //g.DrawCurve(redPen, curvePoints); //畫曲線

            pictureBox1.Image = bitmap1;
        }
    }
}
