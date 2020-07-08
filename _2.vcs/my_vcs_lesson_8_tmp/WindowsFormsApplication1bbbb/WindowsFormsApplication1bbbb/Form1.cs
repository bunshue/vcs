using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1bbbb
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            label1.Text = String.Format("X：{0}, Y：{1}", e.X, e.Y);

            /*
            說明：把label裡的文字，放入格式化字串，其中寫入MouseEventArgs e 的 e.X ,e.Y 位置。

            補充：所有視窗程式設計(C# ,vb,android,java.....)計算視窗座標都是由左上角為基準(0,0)
            */


        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            String s = "";
            switch (e.Button)
            {
                case System.Windows.Forms.MouseButtons.Left: s = "左鍵"; break;
                case System.Windows.Forms.MouseButtons.Middle: s = "中間鍵"; break;
                case System.Windows.Forms.MouseButtons.Right: s = "右鍵"; break;
            }
            label2.Text = String.Format("按了{0}於 X：{1}, Y：{2}", s, e.X, e.Y);

            /*
            說明：利用switch來判斷e.Button按下的是那個按鍵
            需要注意的是，判讀的值在System.Windows.Forms.MouseButtons 裡對應
            */
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            label3.Text = String.Format("按了 {0} 鍵，鍵碼：{1}", e.KeyCode, e.KeyValue);
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

            switch (e.KeyData)
            {//監聽上、下、左、右來移動圖片
                case Keys.Up: pictureBox1.Top -= pictureBox1.Height / 2; break;
                case Keys.Down: pictureBox1.Top += pictureBox1.Height / 2; break;
                case Keys.Left: pictureBox1.Left -= pictureBox1.Width / 2; break;
                case Keys.Right: pictureBox1.Left += pictureBox1.Width / 2; break;
            }

            /*
            說明：KeyDown與KeyPress不同在於：
            KeyDown可聽功能鍵(如Ctrl Alt F1....)
            KeyPress是聽輸入的文字(數字、字母或特殊符號)
            */
        }

        private void Form1_KeyPress(object sender, KeyPressEventArgs e)
        {
            label4.Text = String.Format("打了 {0} ，字碼：{1}", e.KeyChar, (int)e.KeyChar);
        }
    }
}
