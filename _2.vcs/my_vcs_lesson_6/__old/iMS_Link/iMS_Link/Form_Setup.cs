using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Runtime.InteropServices;   //for dll

namespace iMS_Link
{
    public partial class Form_Setup : Form
    {
        String software_version = "A06.0816";
        string iMS_Link_ini_filename = @"./iMS_Link.ini";
        string automation_setup_save_data_path = string.Empty;
        string automation_setup_save_picture_path = string.Empty;

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE
        int timer_display_show_main_mesg1_count = 0;
        int timer_display_show_main_mesg1_count_target = 0;
        int timer_display_show_main_mesg2_count = 0;
        int timer_display_show_main_mesg2_count_target = 0;

        int setup_operation_mode = 0; //0: 色彩調教, 1: 資料燒錄
        bool setup_automation_use_plc = false;    //是否使用真上位
        bool setup_automation_use_ims = true;     //是否使用真下位
        int setup_egd_type = 0;
        int setup_language = 0;

        private string form_confirm_data;
        public string SetupForm1Data
        {
            set
            {
                form_confirm_data = value;
            }
        }

        public void setForm1Value()
        {
            //this.richTextBox1.Text += "父得到信息 : " + form_confirm_data + "\n";
        }

        Form_Confirm form_confirm = new Form_Confirm();     //實體化Form_Confirm視窗物件

        public Form_Setup()
        {
            InitializeComponent();
        }

        private void Form_Setup_Load(object sender, EventArgs e)
        {
            show_item_location();

            get_default_setup();

            show_panel_image();
        }

        void show_item_location()
        {
            lb_main_mesg1.Text = "";
            lb_main_mesg2.Text = "";
            lb_setup0.Text = "資料儲存路徑";
            lb_setup1.Text = "圖片儲存路徑";

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            //this.FormBorderStyle = FormBorderStyle.FixedSingle;
            //this.WindowState = FormWindowState.Maximized;  // 設定表單最大化

            int x_st;
            int y_st;
            int dx;
            int dy;

            x_st = 20;
            y_st = 50;
            dx = 150;
            dy = 55;

            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0 - 30);
            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 2 - 20);
            groupBox2.Location = new Point(x_st + dx * 0 + 220, y_st + dy * 2 - 20);
            groupBox3.Location = new Point(x_st + dx * 0 + 220 + 220, y_st + dy * 0 - 30);
            groupBox4.Location = new Point(x_st + dx * 0 + 220 + 220, y_st + dy * 2 - 20);
            cb_auto_start.Location = new Point(x_st + dx * 0 + 220 + 220 + 220, y_st + dy * 0 - 30 + 20);
            cb_auto_start.Text = "開機啟動\n自動化測試";

            lb_setup0.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            lb_setup1.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            tb_setup0.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            tb_setup1.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            bt_setup0.Location = new Point(x_st + dx * 5, y_st + dy * 4);
            bt_setup1.Location = new Point(x_st + dx * 5, y_st + dy * 5);
            bt_setup6.Location = new Point(x_st + dx * 5, y_st + dy * 6);
            bt_setup7.Location = new Point(x_st + dx * 5 - 100, y_st + dy * 6);
            bt_setup8.Location = new Point(x_st + dx * 5 - 100 - 100, y_st + dy * 6);

            lb_main_mesg1.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            lb_main_mesg2.Location = new Point(x_st + dx * 0, y_st + dy * 7 - 20);

            richTextBox1.Size = new Size(200, 230);
            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 7 + 10);
            richTextBox1.Dock = DockStyle.Bottom;

            //groupbox0
            x_st = 20;
            y_st = 20;
            dx = 200;
            dy = 30;
            rb_operation_mode1.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 10);
            rb_operation_mode2.Location = new Point(x_st + dx * 1 + 20, y_st + dy * 0 + 10);
            panel_awb.Location = new Point(x_st + dx * 0 + 80, y_st + dy * 0);
            panel_data_write.Location = new Point(x_st + dx * 1 + 100, y_st + dy * 0);
            panel_awb.Size = new Size(80, 80);
            panel_awb.BackgroundImageLayout = ImageLayout.Zoom;
            //panel_awb.BackgroundImage = Properties.Resources.awb1;
            panel_data_write.Size = new Size(80, 80);
            panel_data_write.BackgroundImageLayout = ImageLayout.Zoom;
            //panel_data_write.BackgroundImage = Properties.Resources.data_write1;
            groupBox0.Text = "自動化項目";
            groupBox0.Size = new Size(420, 112);

            dy = 30;
            //groupbox1
            rb_use_plc1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            rb_use_plc2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            panel_plc.Location = new Point(x_st + dx * 0 + 80, y_st + dy * 0);
            panel_plc.Size = new Size(80, 80);
            panel_plc.BackgroundImageLayout = ImageLayout.Zoom;
            //panel_plc.BackgroundImage = Properties.Resources.plc1;
            groupBox1.Text = "上位";
            groupBox1.Size = new Size(200, 112);

            //groupbox2
            rb_use_ims1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            rb_use_ims2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            panel_ims.Location = new Point(x_st + dx * 0 + 80, y_st + dy * 0);
            panel_ims.Size = new Size(80, 80);
            panel_ims.BackgroundImageLayout = ImageLayout.Zoom;
            //panel_ims.BackgroundImage = Properties.Resources.use_ims1;
            groupBox2.Text = "下位";
            groupBox2.Size = new Size(200, 112);

            //groupbox3
            rb_egd_type1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            rb_egd_type2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            panel_egd_type.Location = new Point(x_st + dx * 0 + 80, y_st + dy * 0);
            panel_egd_type.Size = new Size(80, 80);
            panel_egd_type.BackgroundImageLayout = ImageLayout.Zoom;
            //panel_egd_type.BackgroundImage = Properties.Resources.egd_type1;
            groupBox3.Size = new Size(200, 112);

            //groupbox4
            rb_language1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            rb_language2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            rb_language3.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            panel_language.Location = new Point(x_st + dx * 0 + 80, y_st + dy * 0);
            panel_language.Size = new Size(80, 80);
            panel_language.BackgroundImageLayout = ImageLayout.Zoom;
            //panel_language.BackgroundImage = Properties.Resources.language1;
            groupBox4.Size = new Size(200, 112);

            bool flag_factory_mode = Properties.Settings.Default.factory_mode;
            if (flag_factory_mode == true)
            {
                //工廠模式, 可以設定作業種類
                groupBox0.Enabled = true;
                groupBox1.Enabled = true;
                groupBox2.Enabled = true;
                groupBox3.Enabled = true;
                groupBox4.Enabled = true;
            }
            else
            {
                //一般模式, 不可以設定作業種類
                groupBox0.Enabled = false;
                groupBox1.Enabled = false;
                groupBox2.Enabled = false;
                groupBox3.Enabled = false;
                groupBox4.Enabled = false;
            }

            bt_exit_setup();
            this.Size = new Size(900, 700);
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            //Application.Exit();
            this.Close();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_setup0_Click(object sender, EventArgs e)
        {
            folderBrowserDialog1.SelectedPath = Application.StartupPath;    //預設開啟的路徑
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                tb_setup0.Text = folderBrowserDialog1.SelectedPath;
            }
            else
            {
                //richTextBox2.Text = "未選取資料夾\n";
            }
        }

        private void bt_setup1_Click(object sender, EventArgs e)
        {
            folderBrowserDialog1.SelectedPath = Application.StartupPath;    //預設開啟的路徑
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                tb_setup1.Text = folderBrowserDialog1.SelectedPath;
            }
            else
            {
                //richTextBox2.Text = "未選取資料夾\n";
            }
        }

        private void bt_setup6_Click(object sender, EventArgs e)
        {
            form_confirm.Owner = this;
            form_confirm.StartPosition = FormStartPosition.CenterScreen;    //設定視窗居中顯示
            DialogResult result = form_confirm.ShowDialog();

            if (result == DialogResult.Ignore)
            {
                //show_main_message1(form_confirm_data, S_OK, 100);
                //richTextBox1.Text += "你選擇了 " + form_confirm_data + "\n";
                if ((form_confirm_data == "iloveims") || (form_confirm_data == "ilovemic"))
                {
                    show_main_message1("密碼正確, 儲存設定", S_OK, 100);
                    richTextBox1.Text += "密碼正確, 儲存設定\n";
                }
                else
                {
                    show_main_message1("密碼錯誤, 不儲存設定", S_OK, 100);
                    richTextBox1.Text += "密碼錯誤, 不儲存設定\n";
                    return;
                }
            }
            else
            {
                show_main_message1("不儲存設定", S_OK, 100);
                richTextBox1.Text += "取消, 不儲存設定\n";
                return;
            }

            if (Directory.Exists(tb_setup0.Text) == false)
            {
                show_main_message1("資料儲存路徑 不存在, 無法儲存設定", S_OK, 100);
                richTextBox1.Text += "資料儲存路徑 不存在, 無法儲存設定\n";
            }
            else
            {
                //儲存
                automation_setup_save_data_path = tb_setup0.Text;
                show_main_message1("資料儲存路徑 存在, 儲存設定完成", S_OK, 30);
                richTextBox1.Text += "資料儲存路徑 存在, 儲存設定完成\n";
            }

            if (Directory.Exists(tb_setup1.Text) == false)
            {
                show_main_message2("圖片儲存路徑 不存在, 無法儲存設定", S_OK, 100);
                richTextBox1.Text += "圖片儲存路徑 不存在, 無法儲存設定\n";
            }
            else
            {
                //儲存
                automation_setup_save_picture_path = tb_setup1.Text;
                show_main_message2("圖片儲存路徑 存在, 儲存設定完成", S_OK, 30);
                richTextBox1.Text += "圖片儲存路徑 存在, 儲存設定完成\n";
            }

            if (rb_operation_mode1.Checked == true)
            {
                Properties.Settings.Default.operation_mode = 0;
            }
            else if (rb_operation_mode2.Checked == true)
            {
                Properties.Settings.Default.operation_mode = 1;
            }
            else
            {
                Properties.Settings.Default.operation_mode = 0;
            }

            if (rb_use_plc1.Checked == true)
            {
                Properties.Settings.Default.automation_use_plc = true;
            }
            else
            {
                Properties.Settings.Default.automation_use_plc = false;
            }

            if (rb_use_ims1.Checked == true)
            {
                Properties.Settings.Default.automation_use_ims = true;
            }
            else
            {
                Properties.Settings.Default.automation_use_ims = false;
            }

            if (rb_egd_type1.Checked == true)
            {
                Properties.Settings.Default.egd_type = 0;
            }
            else if (rb_egd_type2.Checked == true)
            {
                Properties.Settings.Default.egd_type = 1;
            }
            else
            {
                Properties.Settings.Default.egd_type = 0;
            }
            if (rb_language1.Checked == true)
            {

            }
            else if (rb_language2.Checked == true)
            {

            }
            else if (rb_language3.Checked == true)
            {

            }
            else
            {

            }
            Properties.Settings.Default.Save();
            save_default_setting_to_file();
        }

        private void bt_setup7_Click(object sender, EventArgs e)
        {
            //恢復預設值

            form_confirm.Owner = this;
            form_confirm.StartPosition = FormStartPosition.CenterScreen;    //設定視窗居中顯示
            DialogResult result = form_confirm.ShowDialog();

            if (result == DialogResult.Ignore)
            {
                //show_main_message1(form_confirm_data, S_OK, 100);
                //richTextBox1.Text += "你選擇了 " + form_confirm_data + "\n";
                if ((form_confirm_data == "iloveims") || (form_confirm_data == "ilovemic"))
                {
                    show_main_message1("密碼正確, 恢復預設值, 請重啟程式", S_OK, 100);
                    richTextBox1.Text += "密碼正確, 恢復預設值, 請重啟程式\n";
                }
                else
                {
                    show_main_message1("密碼錯誤, 不恢復預設值", S_OK, 100);
                    richTextBox1.Text += "密碼錯誤, 不恢復預設值\n";
                    return;
                }
            }
            else
            {
                show_main_message1("不恢復預設值", S_OK, 100);
                richTextBox1.Text += "取消, 不恢復預設值\n";
                return;
            }

            Properties.Settings.Default.restore_default = true;
            Properties.Settings.Default.Save();
        }

        private void bt_setup8_Click(object sender, EventArgs e)
        {
            //工廠模式

            form_confirm.Owner = this;
            form_confirm.StartPosition = FormStartPosition.CenterScreen;    //設定視窗居中顯示
            DialogResult result = form_confirm.ShowDialog();

            if (result == DialogResult.Ignore)
            {
                //show_main_message1(form_confirm_data, S_OK, 100);
                //richTextBox1.Text += "你選擇了 " + form_confirm_data + "\n";
                if ((form_confirm_data == "iloveims") || (form_confirm_data == "ilovemic"))
                {
                    show_main_message1("密碼正確, 設定為工廠模式, 請重啟程式", S_OK, 100);
                    richTextBox1.Text += "密碼正確, 設定為工廠模式, 請重啟程式\n";
                }
                else
                {
                    show_main_message1("密碼錯誤, 不設定為工廠模式", S_OK, 100);
                    richTextBox1.Text += "密碼錯誤, 不設定為工廠模式\n";
                    return;
                }
            }
            else
            {
                show_main_message1("不設定為工廠模式", S_OK, 100);
                richTextBox1.Text += "取消, 不設定為工廠模式\n";
                return;
            }

            bool flag_factory_mode = Properties.Settings.Default.factory_mode;
            if (flag_factory_mode == true)
            {
                richTextBox1.Text += "工廠模式 => 一般模式\n";
                bt_setup8.Text = "開啟 工廠 模式";
                Properties.Settings.Default.factory_mode = false;
            }
            else
            {
                richTextBox1.Text += "一般模式 => 工廠模式\n";
                bt_setup8.Text = "關閉 工廠 模式";
                Properties.Settings.Default.factory_mode = true;
            }
            Properties.Settings.Default.Save();
        }

        void show_main_message1(string mesg, int number, int timeout)
        {
            lb_main_mesg1.Text = mesg;
            //playSound(number);

            timer_display_show_main_mesg1_count = 0;
            timer_display_show_main_mesg1_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        void show_main_message2(string mesg, int number, int timeout)
        {
            lb_main_mesg2.Text = mesg;
            //playSound(number);

            timer_display_show_main_mesg2_count = 0;
            timer_display_show_main_mesg2_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        private void timer_display_Tick(object sender, EventArgs e)
        {
            if (timer_display_show_main_mesg1_count < timer_display_show_main_mesg1_count_target)      //display main message 1 timeout
            {
                timer_display_show_main_mesg1_count++;
                if (timer_display_show_main_mesg1_count >= timer_display_show_main_mesg1_count_target)
                {
                    lb_main_mesg1.Text = "";
                }
            }
            if (timer_display_show_main_mesg2_count < timer_display_show_main_mesg2_count_target)      //display main message 1 timeout
            {
                timer_display_show_main_mesg2_count++;
                if (timer_display_show_main_mesg2_count >= timer_display_show_main_mesg2_count_target)
                {
                    lb_main_mesg2.Text = "";
                }
            }
        }

        private void rb_operation_mode_CheckedChanged(object sender, EventArgs e)
        {
            if (rb_operation_mode1.Checked == true)
            {
                panel_awb.BackgroundImage = Properties.Resources.awb1;
                panel_data_write.BackgroundImage = null;
            }
            else
            {
                panel_awb.BackgroundImage = null;
                panel_data_write.BackgroundImage = Properties.Resources.data_write1;
            }
        }

        private void rb_use_plc_CheckedChanged(object sender, EventArgs e)
        {
            if (rb_use_plc1.Checked == true)
            {
                panel_plc.BackgroundImage = Properties.Resources.plc1;
            }
            else
            {
                panel_plc.BackgroundImage = Properties.Resources.plc2;
            }
        }

        private void rb_use_ims_CheckedChanged(object sender, EventArgs e)
        {
            if (rb_use_ims1.Checked == true)
            {
                panel_ims.BackgroundImage = Properties.Resources.use_ims1;
            }
            else
            {
                panel_ims.BackgroundImage = Properties.Resources.use_ims2;
            }
        }

        private void rb_egd_type_CheckedChanged(object sender, EventArgs e)
        {
            if (rb_egd_type1.Checked == true)
            {
                panel_egd_type.BackgroundImage = Properties.Resources.egd_type1;
            }
            else
            {
                panel_egd_type.BackgroundImage = Properties.Resources.egd_type2;
            }
        }

        private void rb_language_CheckedChanged(object sender, EventArgs e)
        {
            if (rb_language1.Checked == true)
            {
                panel_language.BackgroundImage = Properties.Resources.language1;
            }
            else if (rb_language2.Checked == true)
            {
                panel_language.BackgroundImage = Properties.Resources.language2;
            }
            else if (rb_language3.Checked == true)
            {
                panel_language.BackgroundImage = Properties.Resources.language3;
            }
        }

        [DllImport("kernel32")]
        private static extern int GetPrivateProfileString(string sectionName, string key, string defaultValue, byte[] returnBuffer, int size, string filePath);

        /// <summary>
        /// 写入ini配置文件
        /// </summary>
        /// <param name="sectionName">要写入的section名</param>
        /// <param name="key">要写入的key，如果传入为null，整个sectionName被清除</param>
        /// <param name="value">key所对应的值，如果传入为null，此key将被清除</param>
        /// <param name="filePath">ini文件的完整路径和文件名</param>
        /// <see cref="https://msdn.microsoft.com/zh-cn/library/ms725501.aspx"/>
        /// <returns></returns>

        /// <summary>
        /// 根据key读取Value
        /// </summary>
        /// <param name="sectionName">section名称</param>
        /// <param name="key">key的名称</param>
        /// <param name="filePath">文件路径</param>
        public static string GetIniFileValue(string sectionName, string key, string filePath)
        {
            byte[] buffer = new byte[2048];
            int length = GetPrivateProfileString(sectionName, key, "", buffer, 999, filePath);
            string rs = System.Text.UTF8Encoding.Default.GetString(buffer, 0, length);
            return rs;
        }

        void get_default_setup()
        {
            //從.ini檔讀取資料

            string automation_save_data_path = string.Empty;
            string automation_save_picture_path = string.Empty;

            //先讀.ini的設定  若這部分可用 就不要再用系統參數了
            richTextBox1.Text += "Read ini data from " + iMS_Link_ini_filename + "\n";
            StringBuilder temp = new StringBuilder(1024);//定義一個最大長度為1024的可變字符串

            string section_name = "SetupWRITE_DATA";
            //0: 色彩調教, 1: 資料燒錄
            int operation_mode = Properties.Settings.Default.operation_mode;
            if (operation_mode == 0)  //0: 色彩調教
            {
                //色調
                section_name = "SetupAWB";
            }
            else if (operation_mode == 1)  //1: 資料燒錄
            {
                //燒錄
                section_name = "SetupWRITE_DATA";
            }
            else
            {
                //色調
                section_name = "SetupAWB";
            }

            string COM_Port_OK_Name = string.Empty;
            string parameter_name = "ComportName";
            GetPrivateProfileString(section_name, parameter_name, "", temp, 255, iMS_Link_ini_filename);
            if (temp.Length > 2)
                COM_Port_OK_Name = temp.ToString();
            //richTextBox1.Text += "取得資料 : " + temp + "\n";
            //richTextBox1.Text += "COM_Port_OK_Name : " + COM_Port_OK_Name + "\n";

            int SelectedLanguage = 0;
            parameter_name = "Language";
            GetPrivateProfileString(section_name, parameter_name, "", temp, 255, iMS_Link_ini_filename);
            if (temp.Length > 0)
                SelectedLanguage = int.Parse(temp.ToString());
            //richTextBox1.Text += "取得資料 : " + temp + "\n";
            //richTextBox1.Text += "取得資料len : " + temp.Length.ToString() + "\n";
            //richTextBox1.Text += "SelectedLanguage : " + SelectedLanguage.ToString() + "\n";

            //CSV路徑
            parameter_name = "CSVPath";
            string data = GetIniFileValue(section_name, parameter_name, iMS_Link_ini_filename);
            //richTextBox1.Text += data + "\n";
            //richTextBox1.Text += "len = " + data.Length.ToString() + "\n";
            automation_save_data_path = data;

            //圖片路徑
            parameter_name = "PicturePath";
            data = GetIniFileValue(section_name, parameter_name, iMS_Link_ini_filename);
            //richTextBox1.Text += data + "\n";
            //richTextBox1.Text += "len = " + data.Length.ToString() + "\n";
            automation_save_picture_path = data;

            //相機路徑
            string insighteyes_name = string.Empty;
            parameter_name = "CameraName";
            data = GetIniFileValue(section_name, parameter_name, iMS_Link_ini_filename);
            //richTextBox1.Text += data + "\n";
            //richTextBox1.Text += "len = " + data.Length.ToString() + "\n";
            insighteyes_name = data;

            richTextBox1.Text += "取得資料路徑 : " + automation_save_data_path + "\n";
            richTextBox1.Text += "取得圖片路徑 : " + automation_save_picture_path + "\n";
            richTextBox1.Text += "取得相機名稱 : " + insighteyes_name + "\n";


            tb_setup0.Text = automation_save_data_path;
            tb_setup1.Text = automation_save_picture_path;

            if (Directory.Exists(tb_setup0.Text) == false)
            {
                show_main_message1("資料儲存路徑 不存在", S_OK, 100);
            }
            else
            {
                show_main_message1("資料儲存路徑 OK", S_OK, 100);
            }

            if (Directory.Exists(tb_setup1.Text) == false)
            {
                show_main_message2("圖片儲存路徑 不存在", S_OK, 100);
            }
            else
            {
                show_main_message2("圖片儲存路徑 OK", S_OK, 100);
            }

            //0: 色彩調教, 1: 資料燒錄
            operation_mode = Properties.Settings.Default.operation_mode;
            if (operation_mode == 0)  //0: 色彩調教
            {
                setup_operation_mode = 0;
                rb_operation_mode1.Checked = true;
                rb_operation_mode2.Checked = false;
            }
            else if (operation_mode == 1)  //1: 資料燒錄
            {
                setup_operation_mode = 1;
                rb_operation_mode1.Checked = false;
                rb_operation_mode2.Checked = true;
            }
            else
            {
                setup_operation_mode = 0;
                rb_operation_mode1.Checked = true;
                rb_operation_mode2.Checked = false;
            }

            //是否使用真上位
            bool automation_use_plc = Properties.Settings.Default.automation_use_plc;
            if (automation_use_plc == true)
            {
                setup_automation_use_plc = true;
                rb_use_plc1.Checked = true;
                rb_use_plc2.Checked = false;
            }
            else
            {
                setup_automation_use_plc = false;
                rb_use_plc1.Checked = false;
                rb_use_plc2.Checked = true;
            }

            //是否使用真下位
            bool automation_use_ims = Properties.Settings.Default.automation_use_ims;
            if (automation_use_ims == true)
            {
                setup_automation_use_ims = true;
                rb_use_ims1.Checked = true;
                rb_use_ims2.Checked = false;
            }
            else
            {
                setup_automation_use_ims = false;
                rb_use_ims1.Checked = false;
                rb_use_ims2.Checked = true;
            }

            int egd_type = Properties.Settings.Default.egd_type;
            if (egd_type == 0)
            {
                setup_egd_type = egd_type;
                rb_egd_type1.Checked = true;
            }
            else if (egd_type == 1)
            {
                setup_egd_type = egd_type;
                rb_egd_type2.Checked = true;
            }
            else
            {
                setup_egd_type = 0;
                rb_egd_type1.Checked = true;
            }

            int language = 0;
            if (language == 0)
            {
                rb_language1.Checked = true;
                setup_language = language;
            }
            else if (language == 1)
            {
                rb_language2.Checked = true;
                setup_language = language;
            }
            else if (language == 2)
            {
                rb_language3.Checked = true;
                setup_language = language;
            }
            else
            {
                rb_language1.Checked = true;
                setup_language = 0;
            }

            richTextBox1.Text += "作業模式 : " + Properties.Settings.Default.operation_mode + "\n";
            richTextBox1.Text += "使用上位 : " + Properties.Settings.Default.automation_use_plc + "\n";
            richTextBox1.Text += "使用下位 : " + Properties.Settings.Default.automation_use_ims + "\n";
            richTextBox1.Text += "內視鏡 : " + Properties.Settings.Default.egd_type + "\n";
            //richTextBox1.Text += "語言 : " +  + "\n";

            bool flag_factory_mode = Properties.Settings.Default.factory_mode;
            if (flag_factory_mode == true)
            {
                richTextBox1.Text += "工廠模式\n";
                bt_setup8.Text = "關閉 工廠 模式";
            }
            else
            {
                richTextBox1.Text += "一般模式\n";
                bt_setup8.Text = "開啟 工廠 模式";
            }
        }

        void show_panel_image()
        {
            //0: 色彩調教, 1: 資料燒錄
            if (setup_operation_mode == 0)  //0: 色彩調教
            {
                panel_awb.BackgroundImage = Properties.Resources.awb1;
                panel_data_write.BackgroundImage = null;
            }
            else if (setup_operation_mode == 1)  //1: 資料燒錄
            {
                panel_awb.BackgroundImage = null;
                panel_data_write.BackgroundImage = Properties.Resources.data_write1;
            }
            else
            {
                panel_awb.BackgroundImage = Properties.Resources.awb1;
                panel_data_write.BackgroundImage = null;
            }

            //是否使用真上位
            if (setup_automation_use_plc == true)
            {
                panel_plc.BackgroundImage = Properties.Resources.plc1;

            }
            else
            {
                panel_plc.BackgroundImage = Properties.Resources.plc2;
            }

            //是否使用真下位
            if (setup_automation_use_ims == true)
            {
                panel_ims.BackgroundImage = Properties.Resources.use_ims1;
            }
            else
            {
                panel_ims.BackgroundImage = Properties.Resources.use_ims2;
            }

            if (setup_egd_type == 0)
                panel_egd_type.BackgroundImage = Properties.Resources.egd_type1;
            else if (setup_egd_type == 1)
                panel_egd_type.BackgroundImage = Properties.Resources.egd_type2;
            else
                panel_egd_type.BackgroundImage = Properties.Resources.egd_type1;

            if (setup_language == 0)
                panel_language.BackgroundImage = Properties.Resources.language1;
            else if (setup_language == 1)
                panel_language.BackgroundImage = Properties.Resources.language2;
            else if (setup_language == 2)
                panel_language.BackgroundImage = Properties.Resources.language3;
            else
                panel_language.BackgroundImage = Properties.Resources.language1;
        }

        [DllImport("kernel32", CharSet = CharSet.Unicode, SetLastError = true)]
        private static extern bool WritePrivateProfileString(string lpAppName, string lpKeyName, string lpString, string lpFileName);

        [DllImport("kernel32", CharSet = CharSet.Unicode, SetLastError = true)]
        private static extern int GetPrivateProfileString(string lpAppName, string lpKeyName, string lpDefault, StringBuilder lpReturnedString, int nSize, string lpFileName);

        [DllImport("kernel32", CharSet = CharSet.Unicode, SetLastError = true)]
        private static extern int GetPrivateProfileInt(string lpAppName, string lpKeyName, int lpDefault, string lpFileName);

        void save_default_setting_to_file()
        {
            if (Directory.Exists(tb_setup0.Text) == false)
            {
                show_main_message1("資料儲存路徑 不存在, 無法儲存設定", S_OK, 100);
                richTextBox1.Text += "資料儲存路徑 不存在, 無法儲存設定\n";
                automation_setup_save_data_path = string.Empty;
            }
            else
            {
                //儲存
                show_main_message1("資料儲存路徑 存在, 儲存設定完成", S_OK, 30);
                richTextBox1.Text += "資料儲存路徑 存在, 儲存設定完成\n";
                automation_setup_save_data_path = tb_setup0.Text;
            }

            if (Directory.Exists(tb_setup1.Text) == false)
            {
                show_main_message2("圖片儲存路徑 不存在, 無法儲存設定", S_OK, 100);
                richTextBox1.Text += "圖片儲存路徑 不存在, 無法儲存設定\n";
                automation_setup_save_picture_path = string.Empty;
            }
            else
            {
                //儲存
                show_main_message2("圖片儲存路徑 存在, 儲存設定完成", S_OK, 30);
                richTextBox1.Text += "圖片儲存路徑 存在, 儲存設定完成\n";
                automation_setup_save_picture_path = tb_setup1.Text;
            }

            //0: 色彩調教, 1: 資料燒錄
            int operation_mode = Properties.Settings.Default.operation_mode;
            if (operation_mode == 0)  //0: 色彩調教
            {
                setup_operation_mode = 0;
            }
            else if (operation_mode == 1)  //1: 資料燒錄
            {
                setup_operation_mode = 1;
            }
            else
            {
                setup_operation_mode = 0;
            }

            //是否使用真上位
            bool automation_use_plc = Properties.Settings.Default.automation_use_plc;
            if (automation_use_plc == true)
            {
                setup_automation_use_plc = true;
            }
            else
            {
                setup_automation_use_plc = false;
            }

            //是否使用真下位
            bool automation_use_ims = Properties.Settings.Default.automation_use_ims;
            if (automation_use_ims == true)
            {
                setup_automation_use_ims = true;
            }
            else
            {
                setup_automation_use_ims = false;
            }

            int egd_type = Properties.Settings.Default.egd_type;
            if (egd_type == 0)
            {
                setup_egd_type = egd_type;
            }
            else if (egd_type == 1)
            {
                setup_egd_type = egd_type;
            }
            else
            {
                setup_egd_type = 0;
            }

            int language = 0;
            if (language == 0)
            {
                setup_language = language;
            }
            else if (language == 1)
            {
                setup_language = language;
            }
            else if (language == 2)
            {
                setup_language = language;
            }
            else
            {
                setup_language = 0;
            }

            richTextBox1.Text += "作業模式 : " + Properties.Settings.Default.operation_mode + "\n";
            richTextBox1.Text += "使用上位 : " + Properties.Settings.Default.automation_use_plc + "\n";
            richTextBox1.Text += "使用下位 : " + Properties.Settings.Default.automation_use_ims + "\n";
            richTextBox1.Text += "內視鏡 : " + Properties.Settings.Default.egd_type + "\n";
            //richTextBox1.Text += "語言 : " +  + "\n";

            bool flag_factory_mode = Properties.Settings.Default.factory_mode;
            if (flag_factory_mode == true)
            {
                richTextBox1.Text += "工廠模式\n";
            }
            else
            {
                richTextBox1.Text += "一般模式\n";
            }

            richTextBox1.Text += "aaaWrite ini data to " + iMS_Link_ini_filename + "\n";

            string section_name = "SetupWRITE_DATA";
            //0: 色彩調教, 1: 資料燒錄
            if (operation_mode == 0)  //0: 色彩調教
            {
                //色調
                section_name = "SetupAWB";
            }
            else if (operation_mode == 1)  //1: 資料燒錄
            {
                //燒錄
                section_name = "SetupWRITE_DATA";
            }
            else
            {
                //色調
                section_name = "SetupAWB";
            }

            int awb_brightness_upper_limit = 240;
            int awb_brightness_lower_limit = 160;
            richTextBox1.Text += "取得AWB亮度上限 : " + awb_brightness_upper_limit.ToString() + "\n";
            richTextBox1.Text += "取得AWB亮度下限 : " + awb_brightness_lower_limit.ToString() + "\n";

            WritePrivateProfileString(section_name, "ProgramUsePlc", automation_use_plc.ToString(), iMS_Link_ini_filename);
            WritePrivateProfileString(section_name, "ProgramUseIms", automation_use_ims.ToString(), iMS_Link_ini_filename);
            WritePrivateProfileString(section_name, "FactoryMode", flag_factory_mode.ToString(), iMS_Link_ini_filename);
            WritePrivateProfileString(section_name, "CSVPath", automation_setup_save_data_path, iMS_Link_ini_filename);
            WritePrivateProfileString(section_name, "PicturePath", automation_setup_save_picture_path, iMS_Link_ini_filename);
            //WritePrivateProfileString(section_name, "CameraName", insighteyes_name, iMS_Link_ini_filename);
            //WritePrivateProfileString(section_name, "ComportName", COM_Port_OK_Name, iMS_Link_ini_filename);
            WritePrivateProfileString(section_name, "Language", language.ToString(), iMS_Link_ini_filename);
            WritePrivateProfileString(section_name, "AWB_Upper", awb_brightness_upper_limit.ToString(), iMS_Link_ini_filename);
            WritePrivateProfileString(section_name, "AWB_Lower", awb_brightness_lower_limit.ToString(), iMS_Link_ini_filename);

            //程式資訊
            string program_name1 = "AWB";
            string program_name2 = "";
            if (operation_mode == 1)
            {
                //燒錄
                section_name = "ProgramInfoWriteData";
                program_name1 = "WriteData";
                program_name2 = "資料燒錄";
            }
            else
            {
                //色調
                section_name = "ProgramInfoAWB";
                program_name1 = "AWB";
                program_name2 = "色彩調教";
            }

            string iMS_Link_exe_filename = @"iMS_Link.exe";
            //程式所在位置
            string appPath = Application.ExecutablePath;
            //richTextBox1.Text += "本程式\n" + appPath + "\n";

            FileInfo finfo = new FileInfo(appPath);
            //richTextBox1.Text += finfo.Name + "\n";
            //richTextBox1.Text += finfo.Name + "\t" + finfo.FullName + "\t" + finfo.Length.ToString() + "\t" + finfo.CreationTime.ToShortDateString() + "\n";
            iMS_Link_exe_filename = finfo.Name;

            string file_compile_time = "2024/01/23 12:34:56";
            if (File.Exists(iMS_Link_exe_filename) == false)   //確認檔案是否存在
            {
                richTextBox1.Text += "檔案 : " + iMS_Link_exe_filename + ", 不存在\n";
            }
            else
            {
                file_compile_time = File.GetLastWriteTime(iMS_Link_exe_filename).ToString("yyyy/MM/dd HH:mm:ss");
                richTextBox1.Text += "檔案時間 : " + file_compile_time + "\n";
            }

            string program_version = software_version;
            string program_date = file_compile_time;
            WritePrivateProfileString(section_name, "ProgramName", program_name1, iMS_Link_ini_filename);
            WritePrivateProfileString(section_name, "程式名稱", program_name2, iMS_Link_ini_filename);
            WritePrivateProfileString(section_name, "程式版本", program_version, iMS_Link_ini_filename);
            WritePrivateProfileString(section_name, "編譯時間", program_date, iMS_Link_ini_filename);
        }
    }
}
