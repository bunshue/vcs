using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_LCDTest
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int color = 0;
        private void Form1_Load(object sender, EventArgs e)
        {
            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;
            string message = string.Empty;
            message += "目前色彩深度\n";
            message += "目前解析度  " + screenWidth.ToString() + " X " + screenHeight.ToString() + "\n\n";
            message += "按 R 鍵 測試 紅色\n";
            message += "按 G 鍵 測試 綠色\n";
            message += "按 B 鍵 測試 藍色\n";
            message += "按 W 鍵 測試 白色\n";
            message += "按 SPACE 鍵 測試 黑色\n\n";
            message += "按 ESC 鍵 離開程式\n\n";
            message += "按 上下鍵及Click 循環測試\n\n";
            message += "按 S 鍵 設定螢幕解析度\n";
            MessageBox.Show(message, "LCD螢幕壞點測試操作說明");
            this.FormBorderStyle = FormBorderStyle.None;
            //this.WindowState = FormWindowState.Maximized;
            this.WindowState = FormWindowState.Maximized;  // 設定表單最大化
            ShowColor(color);
        }

        void ShowColor(int color)
        {
            switch (color)
            {
                case 0:
                    this.BackColor = Color.White;
                    break;
                case 1:
                    this.BackColor = Color.Red;
                    break;
                case 2:
                    this.BackColor = Color.Green;
                    break;
                case 3:
                    this.BackColor = Color.Blue;
                    break;
                case 4:
                    this.BackColor = Color.Black;
                    break;
                default:
                    this.BackColor = Color.White;
                    break;
            }
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)   //根據e.KeyCode分別執行
            {
                case Keys.Escape:
                    MessageBox.Show("版權沒有，歡迎散發", "LCDTEST");
                    Application.Exit();
                    break;
                case Keys.R:
                    color = 1;
                    ShowColor(color);
                    break;
                case Keys.G:
                    color = 2;
                    ShowColor(color);
                    break;
                case Keys.B:
                    color = 3;
                    ShowColor(color);
                    break;
                case Keys.W:
                    color = 0;
                    ShowColor(color);
                    break;
                case Keys.Space:
                    color = 4;
                    ShowColor(color);
                    break;
                case Keys.Up:
                    color++;
                    if (color > 4)
                        color = 0;
                    ShowColor(color);
                    break;
                case Keys.Down:
                    color--;
                    if (color < 0)
                        color = 4;
                    ShowColor(color);
                    break;
                default:
                    //MessageBox.Show("x, KeyCode: " + e.KeyCode.ToString());
                    break;
            }
        }

        private void Form1_Click(object sender, EventArgs e)
        {
            color++;
            if (color > 4)
                color = 0;
            ShowColor(color);
        }
    }
}
