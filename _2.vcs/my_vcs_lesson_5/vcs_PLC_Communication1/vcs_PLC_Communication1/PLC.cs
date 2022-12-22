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
        string get_plc_d_data(string contact_address)
        {
            string contact_point = "D";
            string data_read = "";

            IPLC_interface mitsubishi = new Mitsubishi_realize();//實例化接口--實現三菱在線訪問
            if (mitsubishi.PLC_ready)//PLC是否準備完成
            {
                //richTextBox1.Text += "三菱PLC ready 1\n";
                //richTextBox1.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";

                List<bool> data = mitsubishi.PLC_read_M_bit(contact_point, contact_address);    //讀取狀態
                //richTextBox1.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

                if (data[0] == true)
                {
                    string dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.String_32_Bit);
                    data_read = dddd;
                }
                else
                {
                    data_read = "無資料";
                }
            }
            else
            {
                //richTextBox1.Text += "三菱PLC 不 ready\n";
            }
            return data_read;
        }

        void set_plc_d_data(string contact_address, string write_data)
        {
            string contact_point = "D";

            if (write_data.Length == 0)
            {
                richTextBox1.Text += "無寫入資料";
                richTextBox1.Text += "清除資料\t觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";
                return;
            }

            IPLC_interface mitsubishi = new Mitsubishi_realize();//實例化接口--實現三菱在線訪問
            if (mitsubishi.PLC_ready)//PLC是否準備完成
            {
                //richTextBox1.Text += "三菱PLC ready 2\n";
                //richTextBox1.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";

                string dddd = mitsubishi.PLC_write_D_register(contact_point, contact_address, write_data, numerical_format.String_32_Bit);

                //richTextBox1.Text += "cccc len = " + dddd.Length.ToString() + "\tdata : " + dddd + "\n\n";
            }
            else
            {
                //richTextBox1.Text += "三菱PLC 不 ready\n";
            }
        }

        void set_plc_d_data_bcd16(string contact_address, string write_data)
        {
            string contact_point = "D";

            if (write_data.Length == 0)
            {
                richTextBox1.Text += "無寫入資料";
                richTextBox1.Text += "清除資料\t觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";
                return;
            }

            IPLC_interface mitsubishi = new Mitsubishi_realize();//實例化接口--實現三菱在線訪問
            if (mitsubishi.PLC_ready)//PLC是否準備完成
            {
                //richTextBox1.Text += "三菱PLC ready 2\n";
                //richTextBox1.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";

                string dddd = mitsubishi.PLC_write_D_register(contact_point, contact_address, write_data, numerical_format.BCD_16_Bit);

                //richTextBox1.Text += "cccc len = " + dddd.Length.ToString() + "\tdata : " + dddd + "\n\n";
            }
            else
            {
                //richTextBox1.Text += "三菱PLC 不 ready\n";
            }
        }

        void erase_plc_d_data(string contact_address, int length)
        {
            string contact_point = "D";
            int contact_address_d = int.Parse(contact_address);
            //richTextBox1.Text += "contact_address_d = " + contact_address_d + ", len = " + length.ToString() + "\n";

            if (length < 1)
            {
                richTextBox1.Text += "清除資料 長度錯誤, 至少要 1\n";
                return;
            }

            //richTextBox1.Text += "清除資料\t觸點 : " + contact_point + "\t位址 : " + contact_address + "\t長度 : " + length.ToString() + "\n";

            IPLC_interface mitsubishi = new Mitsubishi_realize();//實例化接口--實現三菱在線訪問
            if (mitsubishi.PLC_ready)//PLC是否準備完成
            {
                //richTextBox1.Text += "三菱PLC ready 2\n";

                string write_data = "0";
                for (int i = 0; i < length; i++)
                {
                    string dddd = mitsubishi.PLC_write_D_register(contact_point, (contact_address_d + i).ToString(), write_data, numerical_format.BCD_16_Bit);
                }
            }
            else
            {
                //richTextBox1.Text += "三菱PLC 不 ready\n";
            }
        }

        void print_plc_d_data(string contact_address)
        {
            string contact_point = "D";
            string data_read = "";

            IPLC_interface mitsubishi = new Mitsubishi_realize();//實例化接口--實現三菱在線訪問
            if (mitsubishi.PLC_ready)//PLC是否準備完成
            {
                //richTextBox1.Text += "三菱PLC ready 1\n";
                //richTextBox1.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";

                List<bool> data = mitsubishi.PLC_read_M_bit(contact_point, contact_address);    //讀取狀態
                //richTextBox1.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

                data[0] = true; //一律打印

                if (data[0] == true)
                {
                    string dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.String_32_Bit);
                    data_read = dddd;

                    //richTextBox1.Text += "\nb len = " + dddd.Length.ToString() + "\n";
                    //richTextBox1.Text += "data1 : " + dddd + "\n";
                    //richTextBox1.Text += "\n";

                    int len = dddd.Length;

                    for (int i = 0; i < len; i++)
                    {
                        richTextBox1.Text += ((int)dddd[i]).ToString("X2").PadLeft(3);
                    }
                    richTextBox1.Text += "\n";

                    for (int i = 0; i < len; i++)
                    {
                        int vv = (int)dddd[i];

                        if ((vv < 32) || (vv > 126))
                        {
                            richTextBox1.Text += " --";
                        }
                        else
                        {
                            richTextBox1.Text += ((char)vv).ToString().PadLeft(3);
                        }
                    }
                    richTextBox1.Text += "\n";

                }
                else
                {
                    richTextBox1.Text += "無資料";
                }
            }
            else
            {
                //richTextBox1.Text += "三菱PLC 不 ready\n";
            }
        }

        bool get_plc_m_status(string contact_address)
        {
            string contact_point = "M";

            if ((contact_address.Length != 4) && (contact_address.Length != 5))
            {
                show_main_message1("位址錯誤", S_OK, 30);
                richTextBox1.Text += "位址錯誤 : " + contact_address + "\n";
                return false;
            }

            bool ret = false;
            IPLC_interface mitsubishi = new Mitsubishi_realize();//實例化接口--實現三菱在線訪問
            if (mitsubishi.PLC_ready)//PLC是否準備完成
            {
                //richTextBox1.Text += "三菱PLC ready 5\n";

                List<bool> data = mitsubishi.PLC_read_M_bit(contact_point, contact_address);    //讀取狀態
                //richTextBox1.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

                if (data[0] == true)
                {
                    ret = true;
                }
                else
                {
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

        void set_plc_m_status(string contact_address, Button_state write_data)
        {
            IPLC_interface mitsubishi = new Mitsubishi_realize();//實例化接口--實現三菱在線訪問
            if (mitsubishi.PLC_ready)//PLC是否準備完成
            {
                //richTextBox1.Text += "三菱PLC ready 6\n";

                //richTextBox1.Text += "\n觸點 : M\t位址 : " + contact_address + "\n";

                List<bool> data = mitsubishi.PLC_write_M_bit("M", contact_address, write_data);
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

        void polling_m_status(string contact_address, Button_state polling_status)
        {
            int i;
            bool ret = false;
            for (i = 0; i < 1000; i++)
            {
                if (flag_plc_test_break == true)
                {
                    richTextBox1.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                    break;
                }

                ret = get_plc_m_status(contact_address);
                if (ret == false)
                {
                    richTextBox1.Text += "OFF  ";
                    if (polling_status == HIGH)
                        delay(500);
                    else
                        break;
                }
                else
                {
                    richTextBox1.Text += "ON  ";
                    if (polling_status == HIGH)
                        break;
                    else
                        delay(500);
                }
            }
        }

        void get_all_plc_m_status()
        {
            string contact_address = String.Empty;
            bool ret = false;

            //richTextBox1.Text += "測試 get_plc_m_status()\n";

            contact_address = "10000";
            ret = get_plc_m_status(contact_address);
            richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "10001";
            ret = get_plc_m_status(contact_address);
            richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "10002";
            ret = get_plc_m_status(contact_address);
            richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "12000";
            ret = get_plc_m_status(contact_address);
            richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "12001";
            ret = get_plc_m_status(contact_address);
            richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "12002";
            ret = get_plc_m_status(contact_address);
            richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
        }

        bool check_all_plc_m_status_low()
        {
            string contact_address = String.Empty;
            bool ret = false;
            bool all_plc_m_status = true;

            //richTextBox1.Text += "測試 get_plc_m_status()\n";

            /* 不用檢查 M10000
            contact_address = "10000";
            ret = get_plc_m_status(contact_address);
            //richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
            if (ret == true)
                all_plc_m_status = false;
            */

            contact_address = "10001";
            ret = get_plc_m_status(contact_address);
            //richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
            if (ret == true)
                all_plc_m_status = false;

            contact_address = "10002";
            ret = get_plc_m_status(contact_address);
            //richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
            if (ret == true)
                all_plc_m_status = false;

            contact_address = "12000";
            ret = get_plc_m_status(contact_address);
            //richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
            if (ret == true)
                all_plc_m_status = false;

            contact_address = "12001";
            ret = get_plc_m_status(contact_address);
            //richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
            if (ret == true)
                all_plc_m_status = false;

            contact_address = "12002";
            ret = get_plc_m_status(contact_address);
            //richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
            if (ret == true)
                all_plc_m_status = false;

            return all_plc_m_status;
        }
    }
}
