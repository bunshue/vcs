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
                    tb_data_d.Text = dddd;
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
                    tb_data_d.Text = "無資料";
                }
            }
            else
            {
                //richTextBox1.Text += "三菱PLC 不 ready\n";
            }
        }


    }
}

