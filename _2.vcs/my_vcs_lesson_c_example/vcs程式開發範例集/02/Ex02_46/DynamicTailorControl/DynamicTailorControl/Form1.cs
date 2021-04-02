using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace DynamicTailorControl
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        public int counter = 1;
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            TextBox txtx = new TextBox();
            //�]�w�L���W�٩MText�ݩʡA�H�β��ͪ���m
            txtx.Left = e.X;
            txtx.Top = e.Y;
            txtx.Name = "TextBox " + counter;
            txtx.Text = "�奻��" + counter;
            //�����ͪ��s��TextBox�ե�]�w�ƥ�A���夤�����ͪ��奻�س]�w�F���Өƥ�
            txtx.Click += new EventHandler(txtx_Click);
            txtx.MouseEnter += new EventHandler(txtx_MouseEnter);
            //�b���餤��ܦ��奻��
            this.Controls.Add(txtx);
            counter++;
        }
        //�w�q�ƥ�
        private void txtx_Click(object sender, System.EventArgs e)
        {
            if (sender.GetType() == typeof(TextBox))
            {
                TextBox control = (TextBox)sender;
                MessageBox.Show(control.Text + "�Q���ʤF�I");
            }
        }
        private void txtx_MouseEnter(object sender, System.EventArgs e)
        {
            //�X�c

            TextBox currentTextBox = (TextBox)sender;
            //�]�w���s���I����
            currentTextBox.BackColor = Color.Yellow;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}