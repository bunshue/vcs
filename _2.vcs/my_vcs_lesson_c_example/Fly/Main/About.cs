using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace Main
{
    public partial class aboutForm : Form
    {
        public aboutForm()
        {
            InitializeComponent();
        }

        private void aboutForm_Load(object sender, EventArgs e)
        {
            lbAbout.Text = "��С����ǻ�����ǰ����������Ʈ��Love���ع������������Ͽ���ԭ��\r\n     ������Դ�����ṩ�������";
        }

        private void lbContact_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start("IExplore.exe", "http://wpa.qq.com/msgrd?V=1&Uin=313769823");
        }
    }
}