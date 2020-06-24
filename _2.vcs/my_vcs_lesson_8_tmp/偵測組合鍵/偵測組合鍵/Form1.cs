using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 偵測組合鍵
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            label1.Text = "偵測按鍵";
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Escape)//按下ESC
            {
                Application.Exit();//關閉程式
            }
            else
            {
                if (e.Control == true && e.Alt == true && e.KeyCode == Keys.T)//按住組合鍵 Ctrl + Alt + T
                {
                    MessageBox.Show("Ctrl + Alt + T");
                }
                else
                {
                    label1.Text = "按了 " + e.KeyCode;
                }

                if (e.Control == true)
                    label2.Text = "Ctrl : true";
                else
                    label2.Text = "Ctrl : false";

                if (e.Alt == true)
                    label3.Text = "Alt : true";
                else
                    label3.Text = "Alt : false";

                if (e.Shift == true)
                    label4.Text = "Shift : true";
                else
                    label4.Text = "Shift : false";

                label5.Text = "KeyCode : " + e.KeyCode.ToString();

            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //關閉程式前 確認視窗
            DialogResult Result = MessageBox.Show("尚未儲存確定要關閉程式?", "關閉確認", MessageBoxButtons.YesNo);
            if (Result == System.Windows.Forms.DialogResult.Yes)
            {
                // 關閉Form 
                e.Cancel = false;
            }
            else
            {
                e.Cancel = true;
            }

        }
    }
}
