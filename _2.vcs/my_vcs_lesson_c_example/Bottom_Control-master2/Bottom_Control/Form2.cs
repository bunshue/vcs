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
using CCWin.SkinClass;

namespace Bottom_Control
{
    public partial class Form2 : Form
    {
        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE

        public Form2()
        {
            InitializeComponent();
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            this.plC_Open_Time1.Enabled = true;
            this.plC_Open_Time1.Start();
            lb_main_mesg1.Visible = true;
            lb_main_mesg1.Text = "";
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            cb_random.Checked = true;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            show_main_message1("讀取 D2000", S_OK, 30);
            string contact_point = "D";
            string contact_address = "2000";
            read_data_from_plc(contact_point, contact_address);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            show_main_message1("寫入 D8000", S_OK, 30);
            string contact_point = "D";
            string contact_address = "8000";
            string write_data = tb_data_to_write.Text;
            tb_data_to_write.Text = "";

            write_data_to_plc(contact_point, contact_address, write_data);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            show_main_message1("讀取 D8000", S_OK, 30);
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
                string finalString1 = "A1234567B1234";
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
                if ((i == 0) || (i == 8))
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

                //string dddd = mitsubishi.PLC_read_D_register(button_base.PLC_Contact, button_base.PLC_Address, numerical_format.Hex_16_Bit);
                //string dddd = mitsubishi.PLC_read_D_register("M", "10000", numerical_format.Signed_16_Bit);
                string dddd = mitsubishi.PLC_read_D_register("Y", "20", numerical_format.Signed_16_Bit);
                richTextBox1.Text += "len = " + dddd.Length.ToString() + "\t";
                richTextBox1.Text += "data : " + dddd[0] + "\n";

                string contact_point = "D";
                string contact_address = "2000";
                richTextBox1.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";
                tb_contact_address.Text = "觸點 : " + contact_point + "\t位址 : " + contact_address;

                List<bool> data = mitsubishi.PLC_read_M_bit(contact_point, contact_address);    //讀取狀態
                richTextBox1.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";
                richTextBox1.Text += "\n";

                dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.String_32_Bit);

                tb_data_read.Text = dddd;
                tb_data.Text = dddd;

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
                //richTextBox1.Text += "三菱PLC 不 ready\n";
            }

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //讀取 Y20
            IPLC_interface mitsubishi = new Mitsubishi_realize();//实例化接口--实现三菱在线访问
            if (mitsubishi.PLC_ready)//PLC是否准备完成
            {
                richTextBox1.Text += "三菱PLC ready\n";

                //string dddd = mitsubishi.PLC_read_D_register(button_base.PLC_Contact, button_base.PLC_Address, numerical_format.Hex_16_Bit);
                //string dddd = mitsubishi.PLC_read_D_register("M", "10000", numerical_format.Signed_16_Bit);

                string contact_point = "Y";
                string contact_address = "20";
                richTextBox1.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";
                tb_contact_address.Text = "觸點 : " + contact_point + "\t位址 : " + contact_address;

                string dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.Signed_16_Bit);
                richTextBox1.Text += "len = " + dddd.Length.ToString() + "\t";
                richTextBox1.Text += "data : " + dddd[0] + "\n";
            }
            else
            {
                //richTextBox1.Text += "三菱PLC 不 ready\n";
            }

        }

        void read_data_from_plc(string contact_point, string contact_address)
        {
            IPLC_interface mitsubishi = new Mitsubishi_realize();//实例化接口--实现三菱在线访问
            if (mitsubishi.PLC_ready)//PLC是否准备完成
            {
                //richTextBox1.Text += "三菱PLC ready\n";

                richTextBox1.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";
                tb_contact_address.Text = "觸點 : " + contact_point + "\t位址 : " + contact_address;

                List<bool> data = mitsubishi.PLC_read_M_bit(contact_point, contact_address);    //讀取狀態
                richTextBox1.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

                if (data[0] == true)
                {
                    string dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.String_32_Bit);
                    tb_data_read.Text = dddd;
                    tb_data.Text = dddd;

                    richTextBox1.Text += "b len = " + dddd.Length.ToString() + "\t";
                    richTextBox1.Text += "data : " + dddd + "\n";
                }
                else
                {
                    tb_data_read.Text = "無資料";
                    tb_data.Text = "無資料";

                }
            }
            else
            {
                //richTextBox1.Text += "三菱PLC 不 ready\n";
            }
        }
        void write_data_to_plc(string contact_point, string contact_address, string write_data)
        {
            if (write_data.Length == 0)
            {
                tb_data_read.Text = "無寫入資料";
                tb_data.Text = "無寫入資料";
                return;
            }

            IPLC_interface mitsubishi = new Mitsubishi_realize();//实例化接口--实现三菱在线访问
            if (mitsubishi.PLC_ready)//PLC是否准备完成
            {
                //richTextBox1.Text += "三菱PLC ready\n";

                richTextBox1.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";
                tb_contact_address.Text = "觸點 : " + contact_point + "\t位址 : " + contact_address;

                string dddd = mitsubishi.PLC_write_D_register(contact_point, contact_address, write_data, numerical_format.String_32_Bit);

                richTextBox1.Text += "cccc len = " + dddd.Length.ToString() + "\t";
                richTextBox1.Text += "data : " + dddd + "\n";
                richTextBox1.Text += "\n";
            }
            else
            {
                //richTextBox1.Text += "三菱PLC 不 ready\n";
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            updata_status_data();


            draw_status();

        }

        private const int N = 11;
        int y1_value = 0;
        int[] y1_data = new int[N];

        void updata_status_data()
        {
            Random r = new Random();
            int rrrr = r.Next(0, 2);
            //richTextBox1.Text += rrrr.ToString() + " ";

            bool status = get_plc_data_status();

            //y1_value = rrrr;
            if (status == true)
            {
                y1_value = 1;

            }
            else
            {
                y1_value = 0;

            }

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

            //畫X軸 Y軸
            Point px1 = new Point(W * 10 / 100, H * 90 / 100);
            Point px2 = new Point(W * 90 / 100, H * 90 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
            Point py1 = new Point(W * 10 / 100, H * 90 / 100);
            Point py2 = new Point(W * 10 / 100, H * 10 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), py1, py2);

            int x_st = W * 10 / 100;
            int x_sp = W * 90 / 100;
            int y_st = H * 10 / 100;
            int y_sp = H * 90 / 100;
            int w = x_sp - x_st;
            int h = y_sp - y_st;
            int step = w / (N - 1);

            //richTextBox1.Text += "step  = " + step.ToString() + " ";

            // Create pens.
            Pen redPen = new Pen(Color.Red, 3);
            Pen grayPen = new Pen(Color.Gray, 5);
            Point[] curvePoints = new Point[N];    //一維陣列內有 N 個Point

            int i;
            for (i = 0; i < N; i++)
            {
                curvePoints[i].X = x_st + step * i;
                curvePoints[i].Y = H - y_st - (h / 1) * y1_data[i] - 5;
            }
            // Draw lines between original points to screen.
            g.DrawLines(redPen, curvePoints);   //畫直線
            // Draw curve to screen.
            //g.DrawCurve(redPen, curvePoints); //畫曲線

            pictureBox1.Image = bitmap1;

            g.Dispose();

        }

        bool get_plc_data_status()
        {
            //讀取 M10000 看資料是否 Ready
            IPLC_interface mitsubishi = new Mitsubishi_realize();//实例化接口--实现三菱在线访问
            if (mitsubishi.PLC_ready)//PLC是否准备完成
            {
                //richTextBox1.Text += "三菱PLC ready\n";
                List<bool> data = mitsubishi.PLC_read_M_bit("M", "10000");//读取状态
                //richTextBox1.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

                if (data[0] == true)
                {
                    return true;

                }
                else
                {
                    return false;
                }

                /*
                //string dddd = mitsubishi.PLC_read_D_register(button_base.PLC_Contact, button_base.PLC_Address, numerical_format.Hex_16_Bit);
                //string dddd = mitsubishi.PLC_read_D_register("M", "10000", numerical_format.Signed_16_Bit);

                string contact_point = "Y";
                string contact_address = "20";
                richTextBox1.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";
                tb_contact_address.Text = "觸點 : " + contact_point + "\t位址 : " + contact_address;

                string dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.Signed_16_Bit);
                richTextBox1.Text += "len = " + dddd.Length.ToString() + "\t";
                richTextBox1.Text += "data : " + dddd[0] + "\n";
                */
            }
            else
            {
                //richTextBox1.Text += "三菱PLC 不 ready\n";
                return false;
            }
        }

        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;

        void show_main_message1(string mesg, int number, int timeout)
        {
            lb_main_mesg1.Text = mesg;
            //playSound(number);

            timer_display_show_main_mesg_count = 0;
            timer_display_show_main_mesg_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        private void timer_display_Tick(object sender, EventArgs e)
        {
            if (timer_display_show_main_mesg_count < timer_display_show_main_mesg_count_target)      //display main message timeout
            {
                timer_display_show_main_mesg_count++;
                if (timer_display_show_main_mesg_count >= timer_display_show_main_mesg_count_target)
                {
                    lb_main_mesg1.Text = "";
                }
                /*
                if (timer_display_show_main_mesg_count >= (timer_display_show_main_mesg_count_target * 2))
                {
                    //lb_main_mesg.Text = "";
                    lb_main_mesg2.Text = "";
                }
                */
            }

        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_erase_Click(object sender, EventArgs e)
        {
            tb_data.Text = "";
        }

        private void bt_read_Click(object sender, EventArgs e)
        {
            string contact_point = tb_contact_point.Text;
            string contact_address = tb_contact_address2.Text;

            if (contact_point.Length <= 0)
            {
                show_main_message1("無觸點", S_OK, 30);
                return;
            }
            if (contact_address.Length <= 0)
            {
                show_main_message1("無位址", S_OK, 30);
                return;
            }

            show_main_message1("讀取: " + contact_point + contact_address, S_OK, 30);

            read_data_from_plc(contact_point, contact_address);
        }

        private void bt_write_Click(object sender, EventArgs e)
        {
            string contact_point = tb_contact_point.Text;
            string contact_address = tb_contact_address2.Text;
            string write_data = tb_data.Text;
            tb_data.Text = "";

            if (contact_point.Length <= 0)
            {
                show_main_message1("無觸點", S_OK, 30);
                return;
            }
            if (contact_address.Length <= 0)
            {
                show_main_message1("無位址", S_OK, 30);
                return;
            }
            if (write_data.Length <= 0)
            {
                show_main_message1("無資料", S_OK, 30);
                return;
            }
            if (write_data == "無資料")
            {
                show_main_message1("無資料", S_OK, 30);
                return;
            }
            if (write_data == "無寫入資料")
            {
                show_main_message1("無資料", S_OK, 30);
                return;
            }

            show_main_message1("寫入: " + contact_point + contact_address + ", 資料: " + write_data, S_OK, 30);

            write_data_to_plc(contact_point, contact_address, write_data);
        }
    }
}
