using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace vcs_ColorPalette3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        //表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            //設定軌跡捲棒的初值為最大值 
            tkbAlpha.Value = 255;
            tkbRed.Value = 255;
            tkbGreen.Value = 255;
            tkbBlue.Value = 255;
            //顯示目前軌跡捲棒的設定值
            lblRed.Text = "R = " + Convert.ToString(tkbRed.Value);
            lblGreen.Text = "G = " + Convert.ToString(tkbGreen.Value);
            lblBlue.Text = "B = " + Convert.ToString(tkbBlue.Value);
            lblAlpha.Text = "A= " + Convert.ToString(tkbAlpha.Value);
            //顯示各軌跡棒目前設定的顏色 
            picRed.BackColor = Color.FromArgb(tkbAlpha.Value, tkbRed.Value, 0, 0);
            picGreen.BackColor = Color.FromArgb(tkbAlpha.Value, 0, tkbGreen.Value, 0);
            picBlue.BackColor = Color.FromArgb(tkbAlpha.Value, 0, 0, tkbBlue.Value);
            picAlpha.BackColor = Color.FromArgb(tkbAlpha.Value, 0, 0, 0);
            //顯示混光出來的的色光置於調色盤中
            picPaint.BackColor = Color.FromArgb(tkbAlpha.Value, tkbRed.Value, tkbGreen.Value, tkbBlue.Value);
            lblPaint.Text = "目前顏色設定值：\nARGB(" + Convert.ToString(tkbAlpha.Value) + ", " + Convert.ToString(tkbRed.Value) + ", " + Convert.ToString(tkbGreen.Value) + ", " + Convert.ToString(tkbBlue.Value) + ")";
            //tkbAlpha, tkbRed, tkbGreen, tkbBlue的Scroll事件被觸發時
            //皆會執行tkb_Scroll事件處理函式
            tkbAlpha.Scroll += new EventHandler(tkb_Scroll);
            tkbRed.Scroll += new EventHandler(tkb_Scroll);
            tkbGreen.Scroll += new EventHandler(tkb_Scroll);
            tkbBlue.Scroll += new EventHandler(tkb_Scroll);
        }
        //tkbAlpha, tkbRed, tkbGreen, tkbBlue的Scroll事件被觸發時皆執行此事件處理函式
        private void tkb_Scroll(object sender, EventArgs e)
        {
            //顯示目前軌跡捲棒的設定值
            lblRed.Text = "R = " + Convert.ToString(tkbRed.Value);
            lblGreen.Text = "G = " + Convert.ToString(tkbGreen.Value);
            lblBlue.Text = "B = " + Convert.ToString(tkbBlue.Value);
            lblAlpha.Text = "A= " + Convert.ToString(tkbAlpha.Value);
            //顯示各軌跡棒目前設定的顏色
            picRed.BackColor = Color.FromArgb(tkbAlpha.Value, tkbRed.Value, 0, 0);
            picGreen.BackColor = Color.FromArgb(tkbAlpha.Value, 0, tkbGreen.Value, 0);
            picBlue.BackColor = Color.FromArgb(tkbAlpha.Value, 0, 0, tkbBlue.Value);
            picAlpha.BackColor = Color.FromArgb(tkbAlpha.Value, 0, 0, 0);
            //顯示混光出來的的色光置於調色盤中
            picPaint.BackColor = Color.FromArgb(tkbAlpha.Value, tkbRed.Value, tkbGreen.Value, tkbBlue.Value);
            lblPaint.Text = "目前顏色設定值：\nARGB(" + Convert.ToString(tkbAlpha.Value) + ", " + Convert.ToString(tkbRed.Value) + ", " + Convert.ToString(tkbGreen.Value) + ", " + Convert.ToString(tkbBlue.Value) + ")";
        }
    }
}
