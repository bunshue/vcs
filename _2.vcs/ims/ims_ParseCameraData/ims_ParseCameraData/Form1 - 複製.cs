using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;                //for file read/write

namespace test_parse_camera_data
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string camera_setup_filename = "i2c_init_table.mem";
            string camera_setup_filename_clean = "i2c_init_table_clean.mem";

            if (System.IO.File.Exists(camera_setup_filename) == false)
            {
                richTextBox1.Text += "檔案 " + camera_setup_filename + " 不存在，製作一個。" + "\n";
                StreamWriter sw = File.CreateText(camera_setup_filename);
                string content = "";
                //content += SelectedLanguage.ToString();
                content += "\n";
                //content += ezisp_path;
                content += "\n";

                sw.WriteLine(content);
                sw.Close();

                //comboBox3.SelectedIndex = 0;
            }
            else
            {
                richTextBox1.Text += "檔案 " + camera_setup_filename + " 存在, 開啟，並讀入設定" + "\n";

                StreamWriter sw = File.CreateText(camera_setup_filename_clean);
                string content = "";

                using (StreamReader sr = new StreamReader(camera_setup_filename))
                {
                    string line;
                    // Read and display lines from the file until the end of 
                    // the file is reached.
                    while ((line = sr.ReadLine()) != null)
                    {
                        //richTextBox1.Text += "old: " + i.ToString() + "\t" + line + "\t" + "len = " + line.Length.ToString() + "\n";
                        //MessageBox.Show(line);
                        line = parse_line_data(line);
                        //richTextBox1.Text += "new: " + i.ToString() + "\t" + line + "\t" + "len = " + line.Length.ToString() + "\n";
                        if (line.Length > 0)
                        {
                            content += line + "\n";
                        }
                    }
                    sr.Close();
                }


                sw.WriteLine(content);
                sw.Close();
                richTextBox1.Text += "存檔完成\n";

                parse_command(camera_setup_filename_clean);

            }

        }

        void parse_command(string filename)
        {
            if (System.IO.File.Exists(filename) == false)
            {
                richTextBox1.Text += "檔案 " + filename + " 不存在，abort。" + "\n";
                return;
            }
            else
            {
                richTextBox1.Text += "檔案 " + filename + " 存在, 開啟" + "\n";

                byte[] data = new byte[1000];
                byte[] data2 = null;
                int index = 0;

                using (StreamReader sr = new StreamReader(filename))
                {
                    string line;
                    int tmp;
                    // Read and display lines from the file until the end of 
                    // the file is reached.
                    while ((line = sr.ReadLine()) != null)
                    {
                        //richTextBox1.Text += "old: " + i.ToString() + "\t" + line + "\t" + "len = " + line.Length.ToString() + "\n";
                        //MessageBox.Show(line);
                        ////line = parse_line_data(line);
                        //richTextBox1.Text += "new: " + i.ToString() + "\t" + line + "\t" + "len = " + line.Length.ToString() + "\n";
                        if (line.Length > 0)
                        {
                            //content += line + "\n";
                            //data[index] = byte.Parse(line);
                            //string hexString = "8E2";
                            data[index] = byte.Parse(line, System.Globalization.NumberStyles.HexNumber);
                            //richTextBox1.Text += num.ToString() + " ";
                            //Console.WriteLine(num);
                            //tmp = int.Parse(line);
                            index++;
                        }
                    }
                    sr.Close();
                }
                richTextBox1.Text += "total length = " + index.ToString() + "\n";
                for (int i = 0; i < index; i++)
                {
                    //richTextBox1.Text += Convert.ToString(data[i], 16) + "\t" + data[i] + "\n";  
                    //richTextBox1.Text += Convert.ToString(data[i], 16) + "\n";  
                
                }

                byte cmd_length = 0;
                byte cmd_op_code = 0;
                byte cmd_sensor_addr = 0;
                byte cmd_sensor_offset_h = 0;
                byte cmd_sensor_offset_l = 0;
                byte cmd_data = 0;
                int cmd_offset = 0;
                byte cmd1 = 0;
                byte cmd2 = 0;

                for (int i = 0; i < index; i++)
                {
                    cmd_length = data[i];
                    if (cmd_length == 6)
                    {
                        cmd_op_code = data[i + 1];          //I2C read / I2C write / delay
                        cmd_sensor_addr = data[i + 2];      //0x78
                        cmd_sensor_offset_h = data[i + 3];
                        cmd_sensor_offset_l = data[i + 4];
                        cmd_data = data[i + 5];
                        i += 5;
                    }
                    else if (cmd_length == 3)
                    {
                        cmd1 = data[i + 1];
                        cmd2 = data[i + 2];
                        i += 2;
                    }
                    else if (cmd_length == 0xff)
                    {
                        richTextBox1.Text += "END of Table\n";
                    }
                    else
                    {
                        richTextBox1.Text += "unknown length = " + cmd_length.ToString() + "\n";
                    }

                    cmd_offset = (int)cmd_sensor_offset_h * 256 + (int)cmd_sensor_offset_l;

                    if (cmd_length == 6)
                    {
                        richTextBox1.Text +=
                            cmd_length.ToString("X2") + "\t" +
                            cmd_op_code.ToString("X2") + "\t" +
                            cmd_sensor_addr.ToString("X2") + "\t" +
                            cmd_sensor_offset_h.ToString("X2") +
                            cmd_sensor_offset_l.ToString("X2") + "\t" +
                            cmd_data.ToString("X2") + "\n";
                    }
                    else if (cmd_length == 3)
                    {
                        richTextBox1.Text +=
                            cmd_length.ToString("X2") + "\t" +
                            cmd1.ToString("X2") + "\t" +
                            cmd2.ToString("X2") + "\n";
                    }



                
                }


                    richTextBox1.Text += "處理完成\n";


            }

        }

        string parse_line_data(string line)
        {
            int skip_mode = 0;
            string new_data = "";
            //int index = 0;
            //richTextBox1.Text += "parse data = " + line + "len = " + line.Length.ToString() + "\n";
            for (int i = 0; i < line.Length; i++)
            {
                if ((i>0) && (line[i] == '/') && (line[i-1] == '/'))
                {
                    skip_mode = 1;
                }

                if (((line[i] >= '0') && (line[i] <= '9')) || ((line[i] >= 'a') && (line[i] <= 'f')) || ((line[i] >= 'A') && (line[i] <= 'F')))
                {
                    //index++;
                    if(skip_mode == 0)
                        new_data += line[i];
                }
            }

            return new_data;
        }

        string parse_line_data2(string line)
        {
            /*
            int skip_mode = 0;
            string new_data = "";
            //int index = 0;
            //richTextBox1.Text += "parse data = " + line + "len = " + line.Length.ToString() + "\n";
            for (int i = 0; i < line.Length; i++)
            {
                if ((i > 0) && (line[i] == '/') && (line[i - 1] == '/'))
                {
                    skip_mode = 1;
                }

                if (((line[i] >= '0') && (line[i] <= '9')) || ((line[i] >= 'a') && (line[i] <= 'f')) || ((line[i] >= 'A') && (line[i] <= 'F')))
                {
                    //index++;
                    if (skip_mode == 0)
                        new_data += line[i];
                }
            }
            */
            //return new_data;
            return line;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            /*
            byte byteValue = 254;

            // Display integer values by calling the ToString method.
            //richTextBox1.Text += byteValue.ToString("D8").ToString() + "\t" + byteValue.ToString("X8") + "\n";

            richTextBox1.Text += byteValue.ToString("X8") + "\n";
            */

            string input_filename = "ov_register1.h";
            string output_filename = "ov_register2.h";
            string output_filename2 = "ov_register3.h";

            if (System.IO.File.Exists(input_filename) == false)
            {
                richTextBox1.Text += "檔案 " + input_filename + " 不存在，abort。" + "\n";
                return;
            }
            else
            {
                richTextBox1.Text += "檔案 " + input_filename + " 存在, 開啟，並讀入設定" + "\n";

                StreamWriter sw = File.CreateText(output_filename);
                StreamWriter sw2 = File.CreateText(output_filename2);
                string content = "";
                string content2 = "";

                using (StreamReader sr = new StreamReader(input_filename))
                {
                    byte flag_comment = 0;
                    string line;
                    // Read and display lines from the file until the end of 
                    // the file is reached.
                    while ((line = sr.ReadLine()) != null)
                    {
                        string[] words = line.Split(' ');
                        flag_comment = 0;
                        if ((line.Length > 0) && (line[0] == '/') && (line[1] == '/'))
                        {
                            flag_comment = 1;
                        }

                        if ((line.Length > 0) && (flag_comment == 0))
                        {
                            richTextBox1.Text += "line_len = " + line.Length.ToString() + ", segment = " + words.Length.ToString() + "\t";
                            foreach (var seg in words)
                                richTextBox1.Text += seg + " ";
                            richTextBox1.Text += "\n";

                            content2 += "#define\t";

                            for (int i = 1; i < words.Length; i++)
                            {
                                if(i>1)
                                    content2 += '_';
                                content2 += words[i];
                            }
                            content2 += '\t' + words[0] + '\n';

                            //content2 += words[0] + "\n";
                        }

                        //richTextBox1.Text += "old: " + i.ToString() + "\t" + line + "\t" + "len = " + line.Length.ToString() + "\n";
                        //MessageBox.Show(line);
                        line = parse_line_data2(line);
                        //richTextBox1.Text += "new: " + i.ToString() + "\t" + line + "\t" + "len = " + line.Length.ToString() + "\n";
                        //if (line.Length > 0)
                        {
                            content += line + "\n";
                        }
                    }
                    sr.Close();
                }

                sw.WriteLine(content);
                sw.Close();
                sw2.WriteLine(content2);
                sw2.Close();
                richTextBox1.Text += "存檔完成\n";

                //parse_command(camera_setup_filename_clean);

            }


        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }


    }
}
