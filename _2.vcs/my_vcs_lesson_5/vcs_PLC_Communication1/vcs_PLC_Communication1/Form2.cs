using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Diagnostics;       //for Process, Stopwatch
using System.Drawing.Imaging;

using vcs_PLC_Communication1.PLC_Communication;

namespace vcs_PLC_Communication1
{

    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            this.plC_Open_Time1.MitsubishiIP = "192.168.3.39";
            this.plC_Open_Time1.Interval = 500;
            this.plC_Open_Time1.Enabled = true;
            this.plC_Open_Time1.Mitsubishi_Open = true;
            this.plC_Open_Time1.Start();

            add_automation_controls();
            show_item_location();
        }
        void show_item_location()
        {
            cb_random.Checked = true;

            this.Size = new Size(PLC_PANEL_WIDTH + BORDER * 4, PLC_PANEL_HEIGHT + groupBox1.Height + BORDER * 6);
            groupBox1.Location = new Point(BORDER, PLC_PANEL_HEIGHT + BORDER * 1);

            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point(10, 10);

            // C# 設定視窗載入位置 
            //this.StartPosition = FormStartPosition.CenterScreen; //居中顯示
        }
        private void Form2_FormClosing(object sender, FormClosingEventArgs e)
        {


        }
        private void Form2_FormClosed(object sender, FormClosedEventArgs e)
        {
            //C# 強制關閉 Process
            Process.GetCurrentProcess().Kill();
        }

        private void bt_generate_Click(object sender, EventArgs e)
        {
            string random_data = string.Empty;
            if (cb_random.Checked == true)
            {
                random_data = make_random_data();
            }
            else
            {
                random_data = "A1234567B1234";
            }
            richTextBox_plc.Text += "相機序號：" + random_data + "\n";
            tb_data_d.Text = random_data;
        }

        string make_random_data()
        {
            //[C#] 產生一組亂數
            //最後產生的finalString就是我們要的亂數,至於亂數長度,你可以調整第二行中8這個數字,如果沒改就是長度8的亂數.
            string random_data = string.Empty;
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
            random_data = new String(stringChars1);
            return random_data;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox_plc.Text += "測試 get_plc_m_status()\n";

            string contact_address = "10000";
            bool ret = false;

            contact_address = "10000";
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "10001";
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "10002";
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "12000";
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "12001";
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "12002";
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "8000";
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "8001";
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "8002";
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "8012";
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "8013";
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            string data_read;
            contact_address = "8013";
            data_read = get_plc_d_data(contact_address);
            richTextBox_plc.Text += "讀取 D" + contact_address + "\t結果 : " + data_read + "\n";

            contact_address = "8014";
            data_read = get_plc_d_data(contact_address);
            richTextBox_plc.Text += "讀取 D" + contact_address + "\t結果 : " + data_read + "\n";

            contact_address = "8015";
            data_read = get_plc_d_data(contact_address);
            richTextBox_plc.Text += "讀取 D" + contact_address + "\t結果 : " + data_read + "\n";

            contact_address = "8016";
            data_read = get_plc_d_data(contact_address);
            richTextBox_plc.Text += "讀取 D" + contact_address + "\t結果 : " + data_read + "\n";

            contact_address = "8017";
            data_read = get_plc_d_data(contact_address);
            richTextBox_plc.Text += "讀取 D" + contact_address + "\t結果 : " + data_read + "\n";

            contact_address = "8018";
            data_read = get_plc_d_data(contact_address);
            richTextBox_plc.Text += "讀取 D" + contact_address + "\t結果 : " + data_read + "\n";

            contact_address = "8019";
            data_read = get_plc_d_data(contact_address);
            richTextBox_plc.Text += "讀取 D" + contact_address + "\t結果 : " + data_read + "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            get_all_plc_m_status();
        }

        private void bt_erase_d_Click(object sender, EventArgs e)
        {
            tb_data_d.Text = "";
        }

        private void bt_read_d_Click(object sender, EventArgs e)
        {
            string contact_address = tb_contact_address_d.Text;

            if (contact_address.Length <= 0)
            {
                show_plc_main_message1("無位址", S_OK, 30);
                return;
            }

            show_plc_main_message1("讀取: M" + contact_address, S_OK, 30);

            string data_read = get_plc_d_data(contact_address);
            tb_data_d.Text = data_read;
        }

        private void bt_write_d_Click(object sender, EventArgs e)
        {
            string contact_address = tb_contact_address_d.Text;
            string write_data = tb_data_d.Text;
            tb_data_d.Text = "";

            if (contact_address.Length <= 0)
            {
                show_plc_main_message1("無位址", S_OK, 30);
                return;
            }
            if (write_data.Length <= 0)
            {
                show_plc_main_message1("無資料", S_OK, 30);
                return;
            }
            if (write_data == "無資料")
            {
                show_plc_main_message1("無資料", S_OK, 30);
                return;
            }
            if (write_data == "無寫入資料")
            {
                show_plc_main_message1("無資料", S_OK, 30);
                return;
            }

            show_plc_main_message1("寫入: D" + contact_address + ", 資料: " + write_data, S_OK, 30);

            set_plc_d_data(contact_address, write_data);
        }

        private void bt_erase_m_Click(object sender, EventArgs e)
        {
            tb_data_m.Text = "";
            tb_data_m.BackColor = Color.White;
        }

        private void bt_read_m_Click(object sender, EventArgs e)
        {
            string contact_address = tb_contact_address_m.Text;

            if (contact_address.Length <= 0)
            {
                show_plc_main_message1("無位址", S_OK, 30);
                return;
            }

            show_plc_main_message1("讀取: M" + contact_address, S_OK, 30);

            bool ret = get_plc_m_status(contact_address);
            //richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

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

            if (contact_address.Length <= 0)
            {
                show_plc_main_message1("無位址", S_OK, 30);
                return;
            }

            show_plc_main_message1("寫入: M" + contact_address + ", 資料: " + button_State, S_OK, 30);

            set_plc_m_status(contact_address, button_State);
        }

        private void button8_Click(object sender, EventArgs e)
        {
            string contact_address = string.Empty;

            richTextBox_plc.Text += "[M status] M12000 LOW\n";
            contact_address = "12000";
            set_plc_m_status(contact_address, LOW);

            richTextBox_plc.Text += "[M status] M12001 LOW\n";
            contact_address = "12001";
            set_plc_m_status(contact_address, LOW);

            richTextBox_plc.Text += "[M status] M12002 LOW\n";
            contact_address = "12002";
            set_plc_m_status(contact_address, LOW);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string contact_address = "8010";
            int length = 1;
            erase_plc_d_data(contact_address, length);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //Print D2000
            string contact_address = "2000";
            print_plc_d_data(contact_address);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox_plc.Text += "\n\n(7) PC 做完色調, 將結果碼寫在 D8010\t";

            Random r = new Random();
            int color_result = r.Next(0, 20);
            richTextBox_plc.Text += "色調結果: 0x" + color_result.ToString("X2") + " = " + color_result.ToString() + "\n";
            string contact_address = "8010";
            string write_data = color_result.ToString();
            show_plc_main_message1("寫入: D" + contact_address + ", 資料: " + write_data, S_OK, 30);
            set_plc_d_data_bcd16(contact_address, write_data);
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

        void save_image_to_drive() //用時間檔名存檔 不檢查序號
        {
            show_plc_main_message1("存檔中...", S_OK, 10);
            delay(10);

            Bitmap bitmap1 = (Bitmap)pictureBox_plc_status.Image;

            if (bitmap1 != null)
            {
                IntPtr pHdc;
                Graphics g = Graphics.FromImage(bitmap1);
                Pen p = new Pen(Color.Red, 1);
                SolidBrush drawBrush = new SolidBrush(Color.Yellow);
                Font drawFont = new Font("Arial", 6, FontStyle.Bold, GraphicsUnit.Millimeter);
                pHdc = g.GetHdc();

                g.ReleaseHdc();
                g.Dispose();

                string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
                try
                {
                    bitmap1.Save(filename, ImageFormat.Bmp);

                    richTextBox_plc.Text += "存檔成功\n";
                    richTextBox_plc.Text += "已存檔 : " + filename + "\n";
                    show_plc_main_message1("已存檔BMP", S_OK, 30);
                }
                catch (Exception ex)
                {
                    richTextBox_plc.Text += "xxx錯誤訊息e39 : " + ex.Message + "\n";
                    show_plc_main_message1("存檔失敗", S_OK, 30);
                    //show_plc_main_message1("存檔失敗 : " + ex.Message, S_OK, 30);
                }
            }
            else
            {
                richTextBox_plc.Text += "無圖可存\n";
                show_plc_main_message1("無圖可存a", S_FALSE, 30);
                show_plc_main_message1("無圖可存a", S_FALSE, 30);
            }
            return;
        }
    }
}
