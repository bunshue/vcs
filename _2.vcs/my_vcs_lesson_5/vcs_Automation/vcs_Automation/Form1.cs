using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;
using System.Threading;

using System.Windows.Automation; // 需要加入 UIAutomationClient.dll 參考

//參考/加入參考/.NET/UIAutomationClient 和 UIAutomationTypes

namespace vcs_Automation
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        private void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            richTextBox1.Size = new Size(600, 690);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1060, 750);
            this.Text = "vcs_Automation";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            string exe_filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_5\vcs_Automation\vcs_PushButtonTest.exe";

            // 啟動要測試的程式
            Process p = Process.Start(exe_filename);

            Thread.Sleep(2000); // 等待程式啟動

            // 取得主視窗
            AutomationElement mainWindow = AutomationElement.FromHandle(p.MainWindowHandle);

            if (mainWindow == null)
            {
                MessageBox.Show("找不到程式的主視窗");
                return;
            }

            // 找出所有 Button
            AutomationElementCollection buttons = mainWindow.FindAll(
                TreeScope.Descendants,
                new PropertyCondition(AutomationElement.ControlTypeProperty, ControlType.Button));

            int count = 0;
            foreach (AutomationElement btn in buttons)
            {
                richTextBox1.Text += btn.ToString() + "\n";
                //richTextBox1.Text += btn.Current.ToString() + "\n";
                //richTextBox1.Text += btn.Current.ProcessId + "\n";

                if (btn.Current.Name != null)
                {
                    richTextBox1.Text += btn.Current.Name.ToString() + "\n";

                    string name = btn.Current.Name.ToString();
                    //richTextBox1.Text += btn.Current.IsOffscreen.ToString() + "\t" + btn.Current.IsEnabled.ToString() + "\n";

                    if ((name.Length > 3) && (name.Substring(0, 3) == "btn"))
                    {
                        richTextBox1.Text += "取得 : " + name + "\n";

                        bool isEnabled = !btn.Current.IsOffscreen && btn.Current.IsEnabled;

                        if (isEnabled)
                        {
                            count++;
                            // 模擬點擊
                            InvokePattern clickPattern = btn.GetCurrentPattern(InvokePattern.Pattern) as InvokePattern;
                            clickPattern.Invoke();
                            Thread.Sleep(500); // 等待半秒
                        }
                    }
                }
            }

            richTextBox1.Text += "作業完成, 共點擊 " + count.ToString() + " 個按鈕\n";
        }


        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

