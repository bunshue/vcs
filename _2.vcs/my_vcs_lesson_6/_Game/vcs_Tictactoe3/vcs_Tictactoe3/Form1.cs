﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace vcs_Tictactoe3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            Symbol1_tb.TextChanged += SymbolTextChenge;
            Symbol2_tb.TextChanged += SymbolTextChenge;
            Symbol1_tb.MouseClick += Symbol_tb_MouseClick;
            Symbol2_tb.MouseClick += Symbol_tb_MouseClick;
        }

        private void Symbol_tb_MouseClick(object sender, MouseEventArgs e)
        {
            TextBox tb = sender as TextBox;
            tb.SelectAll();
        }

        private void SymbolTextChenge(object sender, EventArgs e)
        {
            TextBox tb = sender as TextBox;
            if (tb.TextLength >= 2)
            {
                tb.SelectAll();
                MessageBox.Show("只能輸入一個字!", "錯誤!", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        Button[,] btn = new Button[3, 3];
        Label label;
        Font font = new Font("微軟正黑體", 12);
        bool nowIndex = false;
        string symbol1, symbol2;
        int count;
        DialogResult result;
        Panel panel;
        private void Start_btn_Click(object sender, EventArgs e)
        {
            StartGame();
        }

        private void StartGame()
        {
            symbol1 = Symbol1_tb.Text;
            symbol2 = Symbol2_tb.Text;
            panel1.Visible = false;
            if (panel != null)
            {
                panel.Visible = true;
                Start_btn.Enabled = false;
            }
            nowIndex = false;
            this.Size = new Size(420, 440);
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
                for (int y = 0; y < btn.GetLength(1); y++)
                {
                    btn[x, y] = new Button();
                    btn[x, y].Size = new Size(100, 100);
                    btn[x, y].Text = "";
                    btn[x, y].Location = new Point(50 + x * 100, 50 + y * 100);
                    btn[x, y].Font = font;
                    btn[x, y].Click += ButtonsClick;
                    panel.Controls.Add(btn[x, y]);
                }
            if (label == null)
                label = new Label();
            label.Font = font;
            label.Size = new Size(200, 20);
            label.Text = "玩家一，請選擇。";
            label.Location = new Point(50, 20);
            panel.Controls.Add(label);
        }

        private void ButtonsClick(object sender, EventArgs e)
        {
            Button btn = sender as Button;
            if (btn.Text == "" && count < 9)
            {
                btn.Text = nowIndex == true ? symbol2 : symbol1;
                nowIndex = !nowIndex;
                label.Text = nowIndex == true ? "玩家二，請選擇。" : "玩家一，請選擇。";
                Check();
                count++;
                if (count == 9)
                {
                    label.Text = "GameOver!";
                    GameOver("GameOver");
                }
                Console.WriteLine(count);
            }
        }

        private void Check()
        {
            for (int x = 0; x < btn.GetLength(0); x++)
                if (btn[x, 0].Text == btn[x, 1].Text && btn[x, 1].Text == btn[x, 2].Text && btn[x, 0].Text != "" && btn[x, 1].Text != "" && btn[x, 2].Text != "")
                    GameOver(btn[x, 0].Text);
            for (int y = 0; y < btn.GetLength(1); y++)
                if (btn[0, y].Text == btn[1, y].Text && btn[1, y].Text == btn[2, y].Text && btn[0, y].Text != "" && btn[1, y].Text != "" && btn[2, y].Text != "")
                    GameOver(btn[0, y].Text);
            if (btn[0, 0].Text == btn[1, 1].Text && btn[1, 1].Text == btn[2, 2].Text && btn[0, 0].Text != "" && btn[1, 1].Text != "" && btn[2, 2].Text != "")
                GameOver(btn[0, 0].Text);
            if (btn[2, 0].Text == btn[1, 1].Text && btn[1, 1].Text == btn[0, 2].Text && btn[2, 0].Text != "" && btn[1, 1].Text != "" && btn[0, 2].Text != "")
                GameOver(btn[2, 0].Text);
        }

        private void GameOver(string str)
        {
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
                Start_btn.Enabled = true;
                panel.Visible = false;
                this.Size = new Size(307, 254);
            }
        }
    }
}
