﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;
using System.Drawing.Drawing2D;
using System.Reflection;    //for Assembly
using System.Security.Cryptography; //for HashAlgorithm
using System.Diagnostics;   //for Process
using System.Threading;

namespace vcs_Mix03
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
            dy = 80;

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


            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        void show_button_text(object sender)
        {
            richTextBox1.Text += ((Button)sender).Text + "\n";
        }

        private void button0_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            
        }

        private void button1_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button2_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button3_Click(object sender, EventArgs e)
        {
            show_button_text(sender);


        }

        private void button4_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button5_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button6_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button7_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button8_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button9_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button10_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button11_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button12_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button13_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button14_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button15_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button16_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button17_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button18_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button19_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button20_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button21_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button22_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button23_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button24_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button25_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button26_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button27_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button28_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button29_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

    }
}
