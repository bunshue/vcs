using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Xml;
using System.Text.RegularExpressions;
using System.Management;
using System.IO;
using Shell32;
using System.Runtime.InteropServices;

namespace test2
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

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 180;
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            button8.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            //控件位置
            bt_exit.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_exit.Size.Width, richTextBox1.Location.Y + 0);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //C#遍歷窗體控件
            string find_ctrl = "button8";
            ForeachFormControls(find_ctrl);
        }

        /// <summary>
        /// Winform C#遍历窗体控件
        /// </summary>
        /// <param name="ctrlName">控件名称</param>
        public void ForeachFormControls(string ctrlName)
        {
            foreach (Control ctrl in this.Controls)
            {
                if (ctrl is Panel)
                {
                    //相關操作代碼
                    ctrl.BackColor = Color.Aquamarine;
                }
                else if (ctrl is Button)
                {
                    ctrl.ForeColor = Color.RoyalBlue;
                }
                else if (ctrl is TextBox)
                {
                    ctrl.Text = null;
                }

                //根據控件名稱找某個控件
                if (ctrl.Name.Equals(ctrlName))
                {
                    //ctrl.Name = string.Empty;
                    ctrl.BackColor = Color.Red;
                }
            }
        }

        /* 找panel1內的控件
        /// <summary>
        /// C#遍历子控件
        /// </summary>
        /// <param name="ctrlName">控件名称</param>
        public void ForeachPanelControls(string ctrlName)
        {
            foreach (Control ctrl in panel1.Controls)
            {
                if (ctrl is Button)
                {
                    if (ctrl.Name.Equals(ctrlName))
                        ctrl.ForeColor = Color.RoyalBlue;
                    else
                        ctrl.ForeColor = Color.SkyBlue;
                }
                else if (ctrl is TextBox)
                {
                    if (ctrl.Name.Equals(ctrlName))
                        ctrl.Name = "当前值";
                    else
                        ctrl.Text = null;
                }
            }
        }
        */

        /* 找chekbox內的控件
        private void ForeachCheckBox(Control ctrls, bool currVal)
        {
            CheckBox cb;
            foreach (Control ctrl in ctrls.Controls)
            {
                if (ctrl is CheckBox)
                {
                    cb = (CheckBox)ctrl;
                    cb.Checked = currVal;
                }
            }
        }
        //same
        private void ForeachCheckBoxes(Control ctrls, bool currVal)
        {
            CheckBox cb;
            foreach (Control ctrl in ctrls.Controls.OfType<CheckBox>())
            {
                cb = (CheckBox)ctrl;
                cb.Checked = currVal;
            }
        }
        */

        private void button1_Click(object sender, EventArgs e)
        {
            //方法1    
            //例：窗体的透明度为50% 
            //this.Opacity = 0.5; 

            //方法2，我用的方法2，窗体透明控件不透明了
            // TransparencyKey只支持透明或不透明，不支持过度色，比如PNG图片中的从不透明到透明的过渡色会显示出讨厌的效果
            this.BackColor = Color.Black;
            this.TransparencyKey = Color.Black;

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

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Close();
        }


    }
}

