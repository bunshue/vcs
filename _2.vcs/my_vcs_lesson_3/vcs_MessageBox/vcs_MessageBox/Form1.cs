using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

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
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 5;
            dy = 60 + 5;

            groupBox3.Location = new Point(10, 10);

            richTextBox1.Size = new Size(300, 540);
            richTextBox1.Location = new Point(x_st + dx * 3-50, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(890, 600);
        }


        private void bt_clear_Click(object sender, EventArgs e)
        {

        }


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

        private void button0_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }
    }
}

