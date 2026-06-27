using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport

namespace vcs_MouseCursor1
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
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            label1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            comboBox1.Size = new Size(400, 80);
            comboBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0 + 40);

            richTextBox1.Size = new Size(400, 690 - 80);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0 + 80);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1070, 750);
            this.Text = "vcs_MouseCursor1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void delay(int delay)
        {
            Application.DoEvents();         //執行某一事件，以達到延遲效果。
            for (int j = 0; j < delay; j++)
            {
                System.Threading.Thread.Sleep(1);
            }
        }

        //------------------------------------------------------------  # 60個

        //移動滑鼠鼠標
        [DllImport("user32")]
        static extern bool SetCursorPos(int X, int Y);

        int screenWidth = Screen.PrimaryScreen.Bounds.Width;
        int screenHeight = Screen.PrimaryScreen.Bounds.Height;

        private void button0_Click(object sender, EventArgs e)
        {
            //移動滑鼠鼠標
            //移動滑鼠鼠標
            int xx = screenWidth / 2;
            int yy = screenHeight / 2;
            SetCursorPos(xx, yy);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx - 100, yy);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx - 100, yy - 100);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx, yy - 100);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx + 100, yy - 100);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx + 100, yy);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx + 100, yy + 100);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx, yy + 100);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx - 100, yy + 100);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx - 100, yy);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx, yy);  //把滑鼠移到 (xx,yy) 的位置
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            //取得滑鼠資訊

            if (SystemInformation.MousePresent)  // 是否安裝滑鼠
            {
                richTextBox1.Text += "是否安裝滑鼠 : 是\n";
            }
            else
            {
                richTextBox1.Text += "是否安裝滑鼠 : 否\n";
            }

            // 滑鼠按鈕的數目
            richTextBox1.Text += "滑鼠按鈕的數目 : " + SystemInformation.MouseButtons.ToString() + "\n";

            if (SystemInformation.MouseWheelPresent) // 滑鼠是否有滾輪
            {
                richTextBox1.Text += "滑鼠是否有滾輪 : 是\n";
            }
            else
            {
                richTextBox1.Text += "滑鼠是否有滾輪 : 否\n";
            }
            // 滑鼠速度 (1 ~ 20)
            richTextBox1.Text += "滑鼠速度 (1 ~ 20) : " + SystemInformation.MouseSpeed.ToString() + "\n";

        }

        //------------------------------------------------------------  # 60個

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

        private void button20_Click(object sender, EventArgs e)
        {
        }

        private void button21_Click(object sender, EventArgs e)
        {
        }

        private void button22_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {
        }

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
        }

        private void button27_Click(object sender, EventArgs e)
        {
        }

        private void button28_Click(object sender, EventArgs e)
        {
        }

        private void button29_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            switch (comboBox1.SelectedIndex)
            {
                case 0: this.Cursor = Cursors.Default; break;
                case 1: this.Cursor = Cursors.Arrow; break;
                case 2: this.Cursor = Cursors.Cross; break;
                case 3: this.Cursor = Cursors.No; break;
                case 4: this.Cursor = Cursors.WaitCursor; break;
                case 5: this.Cursor = Cursors.Hand; break;
                case 6: this.Cursor = Cursors.Help; break;
                case 7: this.Cursor = Cursors.HSplit; break;
                case 8: this.Cursor = Cursors.AppStarting; break;
                case 9: this.Cursor = Cursors.IBeam; break;
                case 10: this.Cursor = Cursors.NoMove2D; break;
                case 11: this.Cursor = Cursors.NoMoveHoriz; break;
                case 12: this.Cursor = Cursors.NoMoveVert; break;
                case 13: this.Cursor = Cursors.PanEast; break;
                case 14: this.Cursor = Cursors.PanNE; break;
                case 15: this.Cursor = Cursors.PanNorth; break;
                case 16: this.Cursor = Cursors.PanNW; break;
                case 17: this.Cursor = Cursors.PanSE; break;
                case 18: this.Cursor = Cursors.PanSouth; break;
                case 19: this.Cursor = Cursors.PanSW; break;
                case 20: this.Cursor = Cursors.PanWest; break;
                case 21: this.Cursor = Cursors.SizeAll; break;
                case 22: this.Cursor = Cursors.SizeNESW; break;
                case 23: this.Cursor = Cursors.SizeNS; break;
                case 24: this.Cursor = Cursors.SizeNWSE; break;
                case 25: this.Cursor = Cursors.SizeWE; break;
                case 26: this.Cursor = Cursors.UpArrow; break;
                case 27: this.Cursor = Cursors.VSplit; break;
                default: break;
            }
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

/*  可搬出

*/

