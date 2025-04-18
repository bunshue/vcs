﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Tictactoe4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        Button[,] btn = new Button[3, 3];
        Label label;
        bool nowIndex = false;
        string symbol1, symbol2;
        int count;
        DialogResult result;
        Panel panel;

        private void button1_Click(object sender, EventArgs e)
        {
            StartGame();
            button2.Enabled = true;
        }

        private void StartGame()
        {
            symbol1 = "O";
            symbol2 = "X";
            panel1.Visible = false;
            if (panel != null)
            {
                panel.Visible = true;
                button1.Enabled = false;
            }
            nowIndex = false;
            if (panel == null)
            {
                panel = new Panel();
                panel.Size = new Size(this.DisplayRectangle.Width, this.DisplayRectangle.Height);
            }
            this.Controls.Add(panel);
            Creat_btn_label();
        }

        private void Creat_btn_label()
        {
            for (int x = 0; x < btn.GetLength(0); x++)
                for (int y = 0; y < btn.GetLength(0); y++)
                {
                    panel.Controls.Remove(btn[x, y]);
                    if (btn[x, y] != null)
                        btn[x, y].Dispose();
                }
            btn = new Button[3, 3];
            for (int x = 0; x < btn.GetLength(0); x++)
            {
                for (int y = 0; y < btn.GetLength(1); y++)
                {
                    btn[x, y] = new Button();
                    btn[x, y].Size = new Size(100, 100);
                    btn[x, y].Text = "";
                    btn[x, y].Location = new Point(50 + x * 100, 50 + y * 100);
                    btn[x, y].Click += ButtonsClick;
                    panel.Controls.Add(btn[x, y]);
                    richTextBox1.Text += "建立Button btn[" + x.ToString() + ", " + y.ToString() + "], 方法ButtonsClick()\n";
                }
            }
            if (label == null)
                label = new Label();
            label.Size = new Size(200, 20);
            label.Text = "玩家一，請選擇，畫圈。";
            label.Location = new Point(50, 20);
            panel.Controls.Add(label);
        }

        private void ButtonsClick(object sender, EventArgs e)
        {
            richTextBox1.Text += "ButtonsClick()";
            Button btn = sender as Button;
            if (btn.Text == "" && count < 9)
            {
                btn.Text = nowIndex == true ? symbol2 : symbol1;
                nowIndex = !nowIndex;
                label.Text = nowIndex == true ? "玩家二，請選擇，畫叉。" : "玩家一，請選擇，畫圈。";
                Check();
                count++;
                richTextBox1.Text += "\tButtonsClick, count = " + count.ToString() + "\n";
                if (count == 9)
                {
                    richTextBox1.Text += "走滿棋格, count = " + count.ToString() + "\n";
                    label.Text = "GameOver!";
                    GameOver("GameOver");
                }
            }
            else
                richTextBox1.Text += "\n";
        }

        private void Check()
        {
            richTextBox1.Text += "\t檢查\n";
            for (int x = 0; x < btn.GetLength(0); x++)
            {
                //檢查直的
                richTextBox1.Text += "檢查第 " + (x + 1).ToString() + " 條直線\n";
                if (btn[x, 0].Text == btn[x, 1].Text && btn[x, 1].Text == btn[x, 2].Text && btn[x, 0].Text != "" && btn[x, 1].Text != "" && btn[x, 2].Text != "")
                {
                    richTextBox1.Text += "call GameOver 1\n";
                    btn[x, 0].BackColor = Color.Pink;
                    btn[x, 1].BackColor = Color.Pink;
                    btn[x, 2].BackColor = Color.Pink;
                    GameOver(btn[x, 0].Text);
                }
            }
            for (int y = 0; y < btn.GetLength(1); y++)
            {
                //檢查橫的
                richTextBox1.Text += "檢查第 " + (y + 1).ToString() + " 條橫線\n";
                if (btn[0, y].Text == btn[1, y].Text && btn[1, y].Text == btn[2, y].Text && btn[0, y].Text != "" && btn[1, y].Text != "" && btn[2, y].Text != "")
                {
                    richTextBox1.Text += "call GameOver 2\n";
                    btn[0, y].BackColor = Color.Pink;
                    btn[1, y].BackColor = Color.Pink;
                    btn[2, y].BackColor = Color.Pink;
                    GameOver(btn[0, y].Text);
                }
            }

            richTextBox1.Text += "檢查 左上到右下\n";
            if (btn[0, 0].Text == btn[1, 1].Text && btn[1, 1].Text == btn[2, 2].Text && btn[0, 0].Text != "" && btn[1, 1].Text != "" && btn[2, 2].Text != "")
            {
                richTextBox1.Text += "call GameOver 3, 左上到右下\n";
                btn[0, 0].BackColor = Color.Pink;
                btn[1, 1].BackColor = Color.Pink;
                btn[2, 2].BackColor = Color.Pink;
                GameOver(btn[0, 0].Text);
            }

            richTextBox1.Text += "檢查 右上到左下\n";
            if (btn[2, 0].Text == btn[1, 1].Text && btn[1, 1].Text == btn[0, 2].Text && btn[2, 0].Text != "" && btn[1, 1].Text != "" && btn[0, 2].Text != "")
            {
                richTextBox1.Text += "call GameOver 4, 右上到左下\n";
                btn[2, 0].BackColor = Color.Pink;
                btn[1, 1].BackColor = Color.Pink;
                btn[0, 2].BackColor = Color.Pink;
                GameOver(btn[2, 0].Text);
            }
        }

        private void GameOver(string str)
        {
            richTextBox1.Text += "GameOver, str = " + str + "\n";
            count = 10;
            string msg = "";
            if (str == symbol1)
            {
                msg = "玩家一獲勝!";
                count = -1;
            }
            else if (str == symbol2)
            {
                msg = "玩家二獲勝!";
                count = -1;
            }
            else if (str == "GameOver")
            {
                msg = "平局";
                count = 0;
            }
            label.Text = "GameOver!";
            result = MessageBox.Show(msg, "", MessageBoxButtons.OKCancel, MessageBoxIcon.None);
            if (result == DialogResult.OK)
                StartGame();
            else
            {
                panel1.Visible = true;
                button1.Enabled = true;
                panel.Visible = false;
                this.Size = new Size(800, 600);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //panel1.Visible = true;
            label.Text = "";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

    }
}
