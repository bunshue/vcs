using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for WindowsAPI的訊息框

namespace vcs_MessageBox
{
    public partial class Form1 : Form
    {
        private MessageBoxIcon iIcon;
        private MessageBoxButtons iButton;
        private MessageBoxDefaultButton iDefaultButton;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            this.Icon1.Click += new System.EventHandler(this.IconClick);
            this.Icon2.Click += new System.EventHandler(this.IconClick);
            this.Icon3.Click += new System.EventHandler(this.IconClick);
            this.Icon4.Click += new System.EventHandler(this.IconClick);
            this.Icon5.Click += new System.EventHandler(this.IconClick);
            this.Icon6.Click += new System.EventHandler(this.IconClick);
            this.Icon7.Click += new System.EventHandler(this.IconClick);
            this.Icon8.Click += new System.EventHandler(this.IconClick);

            this.Button1.Click += new System.EventHandler(this.ButtonClick);
            this.Button2.Click += new System.EventHandler(this.ButtonClick);
            this.Button3.Click += new System.EventHandler(this.ButtonClick);
            this.Button4.Click += new System.EventHandler(this.ButtonClick);
            this.Button5.Click += new System.EventHandler(this.ButtonClick);
            this.Button6.Click += new System.EventHandler(this.ButtonClick);

            this.DefaultButton1.Click += new System.EventHandler(this.DefaultButtonClick);
            this.DefaultButton2.Click += new System.EventHandler(this.DefaultButtonClick);
            this.DefaultButton3.Click += new System.EventHandler(this.DefaultButtonClick);

            iIcon = MessageBoxIcon.Information;
            iButton = MessageBoxButtons.YesNo;
            iDefaultButton = MessageBoxDefaultButton.Button1;
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            groupBox3.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button0.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button8.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            richTextBox1.Size = new Size(300, 540);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1000, 600);
            this.Text = "vcs_MessageBox";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void IconClick(object sender, System.EventArgs e)
        {
            switch (((RadioButton)sender).Name)
            {
                case "Icon1":
                    iIcon = MessageBoxIcon.Asterisk;
                    break;
                case "Icon2":
                    iIcon = MessageBoxIcon.Error;
                    break;
                case "Icon3":
                    iIcon = MessageBoxIcon.Exclamation;
                    break;
                case "Icon4":
                    iIcon = MessageBoxIcon.Hand;
                    break;
                case "Icon5":
                    iIcon = MessageBoxIcon.Information;
                    break;
                case "Icon6":
                    iIcon = MessageBoxIcon.Question;
                    break;
                case "Icon7":
                    iIcon = MessageBoxIcon.Stop;
                    break;
                case "Icon8":
                    iIcon = MessageBoxIcon.Warning;
                    break;
            }
        }

        private void ButtonClick(object sender, System.EventArgs e)
        {
            switch (((RadioButton)sender).Name)
            {
                case "Button1":
                    iButton = MessageBoxButtons.AbortRetryIgnore;
                    break;
                case "Button2":
                    iButton = MessageBoxButtons.OK;
                    break;
                case "Button3":
                    iButton = MessageBoxButtons.OKCancel;
                    break;
                case "Button4":
                    iButton = MessageBoxButtons.RetryCancel;
                    break;
                case "Button5":
                    iButton = MessageBoxButtons.YesNo;
                    break;
                case "Button6":
                    iButton = MessageBoxButtons.YesNoCancel;
                    break;
            }
        }

        public void DefaultButtonClick(object sender, System.EventArgs e)
        {
            switch (((RadioButton)sender).Name)
            {
                case "DefaultButton1":
                    iDefaultButton = MessageBoxDefaultButton.Button1;
                    break;
                case "DefaultButton2":
                    iDefaultButton = MessageBoxDefaultButton.Button2;
                    break;
                case "DefaultButton3":
                    iDefaultButton = MessageBoxDefaultButton.Button3;
                    break;
            }
        }

        private void btnShow_Click(object sender, EventArgs e)
        {
            DialogResult iResult;

            iResult = MessageBox.Show(txtMsg.Text, txtCaption.Text, iButton, iIcon, iDefaultButton);

            switch (iResult)
            {
                case DialogResult.Abort:
                    txtResult.Text = "DialogResult.Abort";
                    break;
                case DialogResult.Retry:
                    txtResult.Text = "DialogResult.Retry";
                    break;
                case DialogResult.Ignore:
                    txtResult.Text = "DialogResult.Ignore";
                    break;
                case DialogResult.OK:
                    txtResult.Text = "DialogResult.OK";
                    break;
                case DialogResult.Cancel:
                    txtResult.Text = "DialogResult.Cancel";
                    break;
                case DialogResult.Yes:
                    txtResult.Text = "DialogResult.Yes";
                    break;
                case DialogResult.No:
                    txtResult.Text = "DialogResult.No";
                    break;
            }
        }

        //------------------------------------------------------------  # 60個

        //用WindowsAPI的訊息框 ST

        public const int MB_OKCANCEL = 1;
        public const int MB_ICONINFORMATION = 64;

        //[DllImport("user32.dll")]
        //public static extern int MessageBox(int hWnd, string lpText, string lpCaption, uint wType);

        private void button0_Click(object sender, EventArgs e)
        {
            //用WindowsAPI的訊息框
            //int iResult = MessageBox(0, "要通知的訊息內容", "使用Windows API", MB_OKCANCEL | MB_ICONINFORMATION);
        }
        //用WindowsAPI的訊息框 SP

        //------------------------------------------------------------  # 60個

        //使用自建類別的訊息框
        private void button8_Click(object sender, EventArgs e)
        {
            //新類別的訊息框
            int iResult = Test.MessageBox(0, "要通知的訊息內容", "使用自建類別", Test.MB_OKCANCEL | Test.MB_ICONINFORMATION);
        }

        //------------------------------------------------------------  # 60個
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

*/

