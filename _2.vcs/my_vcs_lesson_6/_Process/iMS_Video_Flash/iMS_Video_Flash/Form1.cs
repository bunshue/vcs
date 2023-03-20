using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Diagnostics;

namespace iMS_Video_Flash
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;
            int w;
            int h;

            w = 140;
            h = 60;

            //button
            x_st = 20;
            y_st = 20;
            dx = w + 60;
            dy = h + 30;

            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            textBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 10);
            checkBox1.Location = new Point(x_st + dx * 0 + 70, y_st + dy * 1 - 30);
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 5);

            Bitmap bitmap1 = new Bitmap(iMS_Video_Flash.Properties.Resources.burn);
            bitmap1.MakeTransparent(Color.Black);     //使用默認的透明顏色進行透明設置
            pictureBox1.Image = bitmap1;
            pictureBox1.Size = new Size(100, 100);
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Location = new Point(x_st + dx * 7, y_st + dy * 0 - 15);

            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 1);

            groupBox1.Size = new Size(20 + w + 20, 550);
            richTextBox1.Size += new Size(1200, 540);
            this.Size = new Size(1550, 800);

            label1.Text = "";
            groupBox2.Location = new Point(x_st + dx * 0, y_st + dy * 0 - 10);
            groupBox2.Size = new Size(800, 90);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button6.Location = new Point(x_st + dx * 0 + 80 * 1, y_st + dy * 0);
            label1.Location = new Point(x_st + dx * 0 + 80 * 2, y_st + dy * 0 + 15);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            string filename = @"C:\_git\ims1\iMS_Video\iMS_Video.sdk\" + textBox1.Text;

            //檢查映像檔
            if (checkBox1.Checked == false)
            {
                if (File.Exists(filename) == true)            //確認檔案是否存在
                {
                    richTextBox1.Text += "映像檔 : " + filename + " 已存在, 無法重新建立\n";
                    return;
                }
            }

            //製作映像檔
            richTextBox1.Text += "製作映像檔\n";
            string exe_filename = "cmd";
            //string parameters = @" /C C:\Xilinx\SDK\2019.1\bin\bootgen -image C:\_git\ims1\iMS_Video\iMS_Video.sdk\output.bif -arch zynq -o C:\_git\ims1\iMS_Video\iMS_Video.sdk\BOOT.bin";
            string parameters = @" /C C:\Xilinx\SDK\2019.1\bin\bootgen -image C:\_git\ims1\iMS_Video\iMS_Video.sdk\output.bif -arch zynq -o " + filename;

            if (checkBox1.Checked == true)
            {
                parameters += " -w on";
            }

            run_command_line_process_async(exe_filename, parameters);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text == "")
            {
                richTextBox1.Text += "未設定燒錄檔檔名\n";
                return;
            }

            //燒錄映像檔
            string exe_filename = "cmd";
            //string parameters = @" /C C:\Xilinx\SDK\2019.1\bin\program_flash -f C:\_git\ims1\iMS_Video\iMS_Video.sdk\BOOT.bin -offset 0 -flash_type qspi-x1-single -fsbl C:\_git\ims1\iMS_Video\iMS_Video.sdk\aries\Release\aries.elf -cable type xilinx_tcf url TCP:127.0.0.1:3121";
            string parameters = @" /C C:\Xilinx\SDK\2019.1\bin\program_flash -f C:\_git\ims1\iMS_Video\iMS_Video.sdk\" + textBox1.Text + @" -offset 0 -flash_type qspi-x1-single -fsbl C:\_git\ims1\iMS_Video\iMS_Video.sdk\aries\Release\aries.elf -cable type xilinx_tcf url TCP:127.0.0.1:3121";
            //richTextBox1.Text += parameters + "\n";

            run_command_line_process_async(exe_filename, parameters);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //製作並燒錄映像檔

            string filename = @"C:\_git\ims1\iMS_Video\iMS_Video.sdk\" + textBox1.Text;

            //檢查映像檔
            if (checkBox1.Checked == false)
            {
                if (File.Exists(filename) == true)            //確認檔案是否存在
                {
                    richTextBox1.Text += "映像檔 : " + filename + " 已存在, 無法重新建立\n";
                    return;
                }
            }

            //製作映像檔
            richTextBox1.Text += "製作映像檔\n";
            string exe_filename = "cmd";
            //string parameters = @" /C C:\Xilinx\SDK\2019.1\bin\bootgen -image C:\_git\ims1\iMS_Video\iMS_Video.sdk\output.bif -arch zynq -o C:\_git\ims1\iMS_Video\iMS_Video.sdk\BOOT.bin";
            string parameters = @" /C C:\Xilinx\SDK\2019.1\bin\bootgen -image C:\_git\ims1\iMS_Video\iMS_Video.sdk\output.bif -arch zynq -o " + filename;

            if (checkBox1.Checked == true)
            {
                parameters += " -w on";
            }

            run_command_line_process_async(exe_filename, parameters);

            //燒錄映像檔
            //parameters = @" /C C:\Xilinx\SDK\2019.1\bin\program_flash -f C:\_git\ims1\iMS_Video\iMS_Video.sdk\BOOT.bin -offset 0 -flash_type qspi-x1-single -fsbl C:\_git\ims1\iMS_Video\iMS_Video.sdk\aries\Release\aries.elf -cable type xilinx_tcf url TCP:127.0.0.1:3121";
            parameters = @" /C C:\Xilinx\SDK\2019.1\bin\program_flash -f C:\_git\ims1\iMS_Video\iMS_Video.sdk\" + textBox1.Text + @" -offset 0 -flash_type qspi-x1-single -fsbl C:\_git\ims1\iMS_Video\iMS_Video.sdk\aries\Release\aries.elf -cable type xilinx_tcf url TCP:127.0.0.1:3121";
            richTextBox1.Text += parameters + "\n";

            run_command_line_process_async(exe_filename, parameters);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //映像檔資訊
            string exe_filename = "cmd";
            string parameters = @" /C C:\Xilinx\SDK\2019.1\gnu\aarch32\nt\gcc-arm-none-eabi\bin\arm-none-eabi-size.exe C:\_git\ims1\iMS_Video\iMS_Video.sdk\aries_main\Release\aries_main.elf";

            run_command_line_process_async(exe_filename, parameters);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //刪除映像檔

            string filename = @"C:\_git\ims1\iMS_Video\iMS_Video.sdk\" + textBox1.Text;

            if (File.Exists(filename) == false)     //確認檔案是否存在
            {
                richTextBox1.Text += "映像檔 : " + filename + ", 不存在, 無法刪除\n";
            }
            else
            {
                File.Delete(filename);
                richTextBox1.Text += "映像檔 : " + filename + ", 已刪除\n";
            }
        }

        //非同步 Process使用
        void run_command_line_process_async(string exe_filename, string command)
        {
            Process process_async = new Process();    //創建一個進程用於調用外部程序

            process_async.StartInfo.FileName = exe_filename;  //設定要啟動的程式
            //process_async.StartInfo.Arguments = "/c " + command; //設定程式執行參數, 也可直接把command寫在這裡, 就不用後面的 StandardInput.WriteLine 了, 要加/c
            //process_async.StartInfo.Arguments = "/c systeminfo";  //可, 要加/c
            process_async.StartInfo.Arguments = command;
            //process_async.StandardInput.AutoFlush = true;

            process_async.StartInfo.UseShellExecute = false;  //false, 關閉Shell的使用, 是否指定操作系統外殼進程啟動程序, 可能接受來自調用程序的輸入信息
            process_async.StartInfo.RedirectStandardInput = true; //重定向標準輸入, 可能接受來自調用程序的輸入信息
            process_async.StartInfo.RedirectStandardOutput = true; //重定向標準輸出, 由調用程序獲取輸出信息
            process_async.StartInfo.RedirectStandardError = true; //重定向錯誤輸出
            process_async.StartInfo.CreateNoWindow = true; //true: 設置不顯示程式窗口, false: 出現cmd的黑窗體
            process_async.StartInfo.ErrorDialog = false;
            //process_async.StartInfo.WindowStyle = ProcessWindowStyle.Normal;  //測不出來
            //process_async.StartInfo.WindowStyle = ProcessWindowStyle.Hidden,

            process_async.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;

            //設定非同步資料處理 output and error handlers
            process_async.OutputDataReceived += new DataReceivedEventHandler(OutputHandler);
            process_async.ErrorDataReceived += new DataReceivedEventHandler(OutputHandler);

            process_async.Start();    //啟動程式

            //啟動讀取資料輸出與錯誤輸出
            process_async.BeginOutputReadLine();
            process_async.BeginErrorReadLine();

            richTextBox1.Text += "等待程式結束.......\n";
            process_async.WaitForExit();	//等待退出
            richTextBox1.Text += "程式結束\n";
        }

        void OutputHandler(object sendingProcess, DataReceivedEventArgs outLine)
        {
            //目前無法做到換行, 也不能操作richTextBox的內容
            richTextBox1.Text += outLine.Data;

            //跳至最後面 fail
            //richTextBox1.Focus();
            //richTextBox1.Select(richTextBox1.Text.Length, 0);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog1 = new OpenFileDialog();
            openFileDialog1.Title = "開啟燒錄檔案";
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.bin";
            openFileDialog1.Filter = "bin檔(*.bin)|*.bin";
            openFileDialog1.InitialDirectory = @"C:\_git\ims2\_release";
            openFileDialog1.Multiselect = false;    //單選

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                /*
                richTextBox1.Text += "已選取檔案: " + openFileDialog1.FileName + "\n";
                FileInfo f = new FileInfo(openFileDialog1.FileName);
                richTextBox1.Text += "Name: " + f.Name + "\n";
                richTextBox1.Text += "FullName: " + f.FullName + "\n";
                richTextBox1.Text += "Extension: " + f.Extension + "\n";
                richTextBox1.Text += "size: " + f.Length.ToString() + "\n";
                richTextBox1.Text += "Directory: " + f.Directory + "\n";
                richTextBox1.Text += "DirectoryName: " + f.DirectoryName + "\n";
                */
                label1.Text = openFileDialog1.FileName;
            }
            else
            {
                label1.Text = "";
            }


        }

        private void button6_Click(object sender, EventArgs e)
        {
            if (label1.Text == "")
            {
                richTextBox1.Text += "未選取燒錄檔\n";
                return;
            }

            //燒錄映像檔
            string exe_filename = "cmd";
            //string parameters = @" /C C:\Xilinx\SDK\2019.1\bin\program_flash -f C:\_git\ims1\iMS_Video\iMS_Video.sdk\BOOT.bin -offset 0 -flash_type qspi-x1-single -fsbl C:\_git\ims1\iMS_Video\iMS_Video.sdk\aries\Release\aries.elf -cable type xilinx_tcf url TCP:127.0.0.1:3121";
            string parameters = @" /C C:\Xilinx\SDK\2019.1\bin\program_flash -f " + label1.Text + @" -offset 0 -flash_type qspi-x1-single -fsbl C:\_git\ims1\iMS_Video\iMS_Video.sdk\aries\Release\aries.elf -cable type xilinx_tcf url TCP:127.0.0.1:3121";
            //richTextBox1.Text += parameters + "\n";

            run_command_line_process_async(exe_filename, parameters);
        }
    }
}
