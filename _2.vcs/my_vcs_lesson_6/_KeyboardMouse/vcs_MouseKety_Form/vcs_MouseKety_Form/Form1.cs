using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MouseKety_Form
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label2.Text = "";
            lb_key.Text = "";
            lb_shift.BackColor = Color.Gray;
            lb_ctrl.BackColor = Color.Gray;
            lb_alt.BackColor = Color.Gray;
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            label2.Text = String.Format("按了 {0} 鍵，鍵碼：{1}", e.KeyCode, e.KeyValue);

            switch (e.KeyCode)
            {
                case Keys.Up:       // 判斷是否按鍵盤上鍵
                    label1.Text = "上";
                    break;
                case Keys.Down:      // 判斷是否按鍵盤下鍵
                    label1.Text = "下";

                    break;
                case Keys.Left:    // 判斷是否按鍵盤左鍵
                    label1.Text = "左";
                    break;
                case Keys.Right:   // 判斷是否按鍵盤右鍵
                    label1.Text = "右";
                    break;
                default:
                    label1.Text = "Form1_KeyDown你按了" + e.KeyCode.ToString() + "";
                    break;
            }


            switch (e.KeyData)
            {//監聽上、下、左、右來移動圖片
                case Keys.Up: pictureBox1.Top -= 10; break;
                case Keys.Down: pictureBox1.Top += 10; break;
                case Keys.Left: pictureBox1.Left -= 10; break;
                case Keys.Right: pictureBox1.Left += 10; break;
            }

            /*
            說明：KeyDown與KeyPress不同在於：
            KeyDown可聽功能鍵(如Ctrl Alt F1....)
            KeyPress是聽輸入的文字(數字、字母或特殊符號)
            */

            //監聽按下的鍵值
            if (e.Control && e.Alt && e.KeyCode == Keys.H)
                MessageBox.Show("哈哈哈！");//若按下Ctrl + Alt + H 
            else if (e.Control && e.Alt && e.KeyCode == Keys.E)//若按下Ctrl + Alt + E
            {
                DialogResult ans = MessageBox.Show("請問是否結束本程式？", "結束",
                                    MessageBoxButtons.YesNo, MessageBoxIcon.Question);
                //跳出訊息視窗，取得 DialogResult ans的結果
                if (ans == System.Windows.Forms.DialogResult.Yes)
                {
                    Application.Exit();
                }
            }

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
                    lb_key.Text = e.KeyCode.ToString();
                }

                if (e.Shift == true)
                {
                    lb_shift.BackColor = Color.Red;
                }
                else
                {
                    lb_shift.BackColor = Color.Gray;
                }

                if (e.Control == true)
                {
                    lb_ctrl.BackColor = Color.Red;
                }
                else
                {
                    lb_ctrl.BackColor = Color.Gray;
                }

                if (e.Alt == true)
                {
                    lb_alt.BackColor = Color.Red;
                }
                else
                {
                    lb_alt.BackColor = Color.Gray;
                }
            }
        }

        private void Form1_KeyPress(object sender, KeyPressEventArgs e)
        {
            label2.Text = String.Format("打了 {0} ，字碼：{1}", e.KeyChar, (int)e.KeyChar);
        }
    }
}
