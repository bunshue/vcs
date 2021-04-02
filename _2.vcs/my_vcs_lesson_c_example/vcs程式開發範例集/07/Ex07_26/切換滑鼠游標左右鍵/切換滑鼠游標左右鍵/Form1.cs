using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 切換滑鼠游標左右鍵
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        [System.Runtime.InteropServices.DllImport("user32.dll", EntryPoint = "SwapMouseButton")]
        public extern static int SwapMouseButton(int bSwap);
        [System.Runtime.InteropServices.DllImport("user32.dll")]
        public extern static int GetSystemMetrics(int nIndes);
        private void checkBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (((CheckBox)sender).Checked == true)//如果為選取狀態
            {
                pictureBox1.Image = null;//清空圖片
                pictureBox1.Image = Properties.Resources.滑鼠游標右鍵;//顯示圖片
                SwapMouseButton(1);//切換滑鼠游標左右鍵
            }
            else//如果不為選取狀態
            {
                if (((CheckBox)sender).Checked == false)
                {
                    pictureBox1.Image = null;//清空圖片
                    pictureBox1.Image = Properties.Resources.滑鼠游標左鍵;//顯示圖片
                    SwapMouseButton(0);//恢復，設定左鍵為主鍵
                }
            }
        }
        const int SM_SWAPBUTTON = 23;//如左右滑鼠游標鍵已經交換，則為TRUE
        private void Form1_Load(object sender, EventArgs e)
        {
            if (GetSystemMetrics(SM_SWAPBUTTON) == 0)//如果滑鼠游標的左右鍵沒有切換
            {
                pictureBox1.Image = null;//清空圖片
                pictureBox1.Image = Properties.Resources.滑鼠游標左鍵;//顯示圖片
                checkBox1.Checked = false;//設定復選框為不選取狀態
            }
            else//如果滑鼠游標左右切換
            {
                pictureBox1.Image = null;//清空圖片
                pictureBox1.Image = Properties.Resources.滑鼠游標右鍵;//顯示圖片
                checkBox1.Checked = true;//設定復選框為選取狀態
            }
        }
    }
}
