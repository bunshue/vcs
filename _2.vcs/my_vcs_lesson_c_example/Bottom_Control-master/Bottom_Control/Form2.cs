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
using Bottom_Control.按钮__TO__PLC方法;
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
            bt_copy_to_clipboard.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width * 2, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            bt_copy_to_clipboard.BackgroundImage = Properties.Resources.clipboard;
            bt_copy_to_clipboard.BackgroundImageLayout = ImageLayout.Zoom;
            cb_random.Checked = true;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            show_main_message1("讀取 D2000", S_OK, 30);
            string contact_point = "D";
            string contact_address = "2000";
            string data_read = read_data_from_plc_d_register(contact_point, contact_address);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            show_main_message1("寫入 D8000", S_OK, 30);
            string contact_point = "D";
            string contact_address = "8000";
            string write_data = tb_data_to_write.Text;
            tb_data_to_write.Text = "";

            write_data_to_plc_d_register(contact_point, contact_address, write_data);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            show_main_message1("讀取 D8000", S_OK, 30);
            string contact_point = "D";
            string contact_address = "8000";
            string data_read = read_data_from_plc_d_register(contact_point, contact_address);
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
                //richTextBox1.Text += "三菱PLC ready\n";

                //Button_write_select(Button.Pattern.ToString(), mitsubishi, Button);//根据按钮模式进行写入操作

                richTextBox1.Text += "read_M, name = " + daButton1.PLC_Contact + ", id = " + daButton1.PLC_Address + "\n";

                List<bool> data = mitsubishi.PLC_read_M_bit(daButton1.PLC_Contact, daButton1.PLC_Address);//读取状态

                richTextBox1.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

                string dddd = mitsubishi.PLC_read_D_register("Y", "20", numerical_format.Signed_16_Bit);
                richTextBox1.Text += "len = " + dddd.Length.ToString() + "\t";
                richTextBox1.Text += "data : " + dddd[0] + "\n";

                string contact_point = "D";
                string contact_address = "2000";
                richTextBox1.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";
                tb_contact_address.Text = "觸點 : " + contact_point + "\t位址 : " + contact_address;

                data = mitsubishi.PLC_read_M_bit(contact_point, contact_address);
                richTextBox1.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";
                richTextBox1.Text += "\n";

                dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.String_32_Bit);

                tb_data_read.Text = dddd;
                tb_data_d.Text = dddd;

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
                //richTextBox1.Text += "三菱PLC ready\n";

                richTextBox1.Text += "read_M, name = " + daButton1.PLC_Contact + ", id = " + daButton1.PLC_Address + "\n";

                List<bool> data = mitsubishi.PLC_read_M_bit(daButton1.PLC_Contact, daButton1.PLC_Address);//读取状态

                richTextBox1.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

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

        string read_data_from_plc_d_register(string contact_point, string contact_address)
        {
            string data_read = "";
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
                    tb_data_d.Text = dddd;
                    data_read = dddd;
                    //richTextBox1.Text += "b len = " + dddd.Length.ToString() + "\t";
                    //richTextBox1.Text += "data : " + dddd + "\n";
                }
                else
                {
                    tb_data_read.Text = "無資料";
                    tb_data_d.Text = "無資料";

                }
            }
            else
            {
                //richTextBox1.Text += "三菱PLC 不 ready\n";
            }
            return data_read;
        }
        void write_data_to_plc_d_register(string contact_point, string contact_address, string write_data)
        {
            if (write_data.Length == 0)
            {
                tb_data_read.Text = "無寫入資料";
                tb_data_d.Text = "無寫入資料";
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

        private void bt_copy_to_clipboard_Click(object sender, EventArgs e)
        {
            //C# – 複製資料到剪貼簿
            //Clipboard.SetData(DataFormats.Text, richTextBox1.Text + "\n");
            Clipboard.SetDataObject(richTextBox1.Text + "\n");      //建議用此
            richTextBox1.Text += "已複製資料到系統剪貼簿\n";
        }

        private void bt_erase_d_Click(object sender, EventArgs e)
        {
            tb_data_d.Text = "";
        }

        private void bt_read_d_Click(object sender, EventArgs e)
        {
            string contact_point = tb_contact_point_d.Text;
            string contact_address = tb_contact_address_d.Text;

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

            string data_read = read_data_from_plc_d_register(contact_point, contact_address);
        }

        private void bt_write_d_Click(object sender, EventArgs e)
        {
            string contact_point = tb_contact_point_d.Text;
            string contact_address = tb_contact_address_d.Text;
            string write_data = tb_data_d.Text;
            tb_data_d.Text = "";

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

            write_data_to_plc_d_register(contact_point, contact_address, write_data);
        }

        private void bt_erase_m_Click(object sender, EventArgs e)
        {
            tb_data_m.Text = "";
            tb_data_m.BackColor = Color.White;
        }

        private void bt_read_m_Click(object sender, EventArgs e)
        {
            string contact_point = tb_contact_point_m.Text;
            string contact_address = tb_contact_address_m.Text;

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

            bool ret = read_data_from_plc_m_bit(contact_point, contact_address);
            if (ret == true)
            {
                tb_data_m.BackColor = Color.Lime;
                tb_data_m.Text = "High";
            }
            else
            {
                tb_data_m.BackColor = Color.Gray;
                tb_data_m.Text = "Low";
            }

        }

        private void bt_write_m_Click(object sender, EventArgs e)
        {
            string contact_point = tb_contact_point_m.Text;
            string contact_address = tb_contact_address_m.Text;

            Button_state button_State;
            if (rb_high.Checked == true)
            {
                button_State = Button_state.ON;
            }
            else
            {
                button_State = Button_state.Off;
            }

            tb_data_m.Text = "";
            tb_data_m.BackColor = Color.White;

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

            show_main_message1("寫入: " + contact_point + contact_address + ", 資料: " + button_State, S_OK, 30);

            write_data_to_plc_m_bit(contact_point, contact_address, button_State);
        }

        bool read_data_from_plc_m_bit(string contact_point, string contact_address)
        {
            bool ret = false;
            IPLC_interface mitsubishi = new Mitsubishi_realize();//实例化接口--实现三菱在线访问
            if (mitsubishi.PLC_ready)//PLC是否准备完成
            {
                //richTextBox1.Text += "三菱PLC ready\n";

                //richTextBox1.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";
                tb_contact_address.Text = "觸點 : " + contact_point + "\t位址 : " + contact_address;

                List<bool> data = mitsubishi.PLC_read_M_bit(contact_point, contact_address);    //讀取狀態
                //richTextBox1.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

                if (data[0] == true)
                {
                    tb_data_read.Text = "True";
                    tb_data_m.Text = "True";
                    ret = true;
                }
                else
                {
                    tb_data_read.Text = "False";
                    tb_data_m.Text = "False";
                    ret = false;
                }
            }
            else
            {
                //richTextBox1.Text += "三菱PLC 不 ready\n";
                ret = false;
            }
            return ret;
        }
        void write_data_to_plc_m_bit(string contact_point, string contact_address, Button_state write_data)
        {
            IPLC_interface mitsubishi = new Mitsubishi_realize();//实例化接口--实现三菱在线访问
            if (mitsubishi.PLC_ready)//PLC是否准备完成
            {
                //richTextBox1.Text += "三菱PLC ready\n";

                richTextBox1.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";
                tb_contact_address.Text = "觸點 : " + contact_point + "\t位址 : " + contact_address;

                //List<bool>                   PLC_write_M_bit(string Name,   string id, Button_state button_State);//写入--位
                List<bool> data = mitsubishi.PLC_write_M_bit(contact_point, contact_address, write_data);



            }
            else
            {
                //richTextBox1.Text += "三菱PLC 不 ready\n";
            }
        }

        //delay 10000 約 10秒
        //C# 不lag的延遲時間
        private void delay(int delay_milliseconds)
        {
            delay_milliseconds *= 2;
            DateTime time_before = DateTime.Now;
            while (((TimeSpan)(DateTime.Now - time_before)).TotalMilliseconds < delay_milliseconds)
            {
                Application.DoEvents();
            }
        }

        bool flag_plc_test = false;
        private void button6_Click(object sender, EventArgs e)
        {
            int i;
            string contact_point = String.Empty;
            string contact_address = String.Empty;
            bool ret = false;

            richTextBox1.Text += "測試PLC作業流程\n";

            flag_plc_test = true;

            richTextBox1.Text += "(1) PLC 把資料放在 D2000\n";
            richTextBox1.Text += "(2a) PLC 拉高 M10000, 供PC讀取, 通知條碼內容已備便\n";
            richTextBox1.Text += "(2b) PC 讀取 M10000 狀態\n";
            contact_point = "M";
            contact_address = "10000";
            ret = false;
            for (i = 0; i < 1000; i++)
            {
                ret = read_data_from_plc_m_bit(contact_point, contact_address);

                //richTextBox1.Text += "測試PLC作業流程\t" + i.ToString() + "\t" + DateTime.Now.ToString() + "\n";
                //richTextBox1.Text += ret.ToString() + "\n";

                if (ret == false)
                {
                    //richTextBox1.Text += "取得 M10000 為 OFF  ";
                    richTextBox1.Text += "OFF  ";
                    delay(500);
                }
                else
                {
                    richTextBox1.Text += "\n取得 M10000 為 ON\n";

                    richTextBox1.Text += "(3a) PC 讀取 D2000 資料\n";

                    show_main_message1("讀取 D2000", S_OK, 30);
                    contact_point = "D";
                    contact_address = "2000";
                    string data_read = read_data_from_plc_d_register(contact_point, contact_address);
                    if (data_read.Length > 0)
                    {
                        richTextBox1.Text += "取得 D2000 資料 : " + data_read + "\n";

                        richTextBox1.Text += "\nlen = " + data_read.Length.ToString() + "\n";

                        richTextBox1.Text += "(3b) PC 將 從 D2000 取得的資料 寫到 D8000\n";

                        string data_to_write = data_read.Substring(0, 16);

                        richTextBox1.Text += "欲寫入 D8000 資料 : " + data_to_write + ", len = " + data_to_write.Length.ToString() + "\n";

                        show_main_message1("寫入 D8000", S_OK, 30);
                        contact_point = "D";
                        contact_address = "8000";
                        //write_data = tb_data_to_write.Text;
                        //tb_data_to_write.Text = "";

                        write_data_to_plc_d_register(contact_point, contact_address, data_to_write);

                        richTextBox1.Text += "(4) PC 拉高 M12000, 供PLC讀取\n";

                        contact_point = "M";
                        contact_address = "12000";

                        Button_state button_State;
                        button_State = Button_state.ON;

                        tb_data_m.Text = "";
                        tb_data_m.BackColor = Color.White;

                        show_main_message1("寫入: " + contact_point + contact_address + ", 資料: " + button_State, S_OK, 30);

                        write_data_to_plc_m_bit(contact_point, contact_address, button_State);

                        richTextBox1.Text += "(5a) PLC 拉高 M10001, 供PC讀取, 通知開始做色調\n";
                        richTextBox1.Text += "(5b) PC 讀取 M10001 狀態\n";
                        contact_point = "M";
                        contact_address = "10001";
                        ret = false;
                        for (i = 0; i < 1000; i++)
                        {
                            ret = read_data_from_plc_m_bit(contact_point, contact_address);

                            if (ret == false)
                            {
                                richTextBox1.Text += "取得 M10001 為 OFF  ";
                                richTextBox1.Text += "OFF  ";
                                delay(500);
                            }
                            else
                            {
                                richTextBox1.Text += "\n取得 M10001 為 ON\n";

                                richTextBox1.Text += "(6) PC 拉高 M12001, 供PLC讀取, 通知PC已開始做色調\n";

                                contact_point = "M";
                                contact_address = "12001";

                                button_State = Button_state.ON;

                                tb_data_m.Text = "";
                                tb_data_m.BackColor = Color.White;

                                show_main_message1("寫入: " + contact_point + contact_address + ", 資料: " + button_State, S_OK, 30);
                                write_data_to_plc_m_bit(contact_point, contact_address, button_State);

                                richTextBox1.Text += "\n\n\nPC開始做色調\n\n\n\n";

                                richTextBox1.Text += "(7) PC 做完色調, 將結果碼寫在 D8010\n";
                                //TBD


                                richTextBox1.Text += "(8) PC 拉高 M12002, 供PLC讀取, 通知PC已做完色調\n";

                                contact_point = "M";
                                contact_address = "12002";

                                button_State = Button_state.ON;

                                tb_data_m.Text = "";
                                tb_data_m.BackColor = Color.White;

                                show_main_message1("寫入: " + contact_point + contact_address + ", 資料: " + button_State, S_OK, 30);
                                write_data_to_plc_m_bit(contact_point, contact_address, button_State);


                                richTextBox1.Text += "測試PLC作業流程完成\n";

                                break;
                            }
                        }

                        richTextBox1.Text += "AAAAAAAAAAAAAAAAAAA\n";







                    }
                    else
                    {
                        richTextBox1.Text += "未取得 D2000 資料\n";
                    }




                    break;



                }

                if (flag_plc_test == false)
                {
                    richTextBox1.Text += "測試PLC作業流程 中斷\n";
                    break;
                }
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "設定 中斷\n";
            flag_plc_test = false;
        }

        private void button7_MouseDown(object sender, MouseEventArgs e)
        {
            richTextBox1.Text += "設定 中斷\n";
            flag_plc_test = false;

        }
    }
}
