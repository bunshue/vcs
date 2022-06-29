using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

namespace vcs_Form3_Loading
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        //顯示Loading表單
        private void button1_Click(object sender, EventArgs e)
        {
            LoadingControl pLoading = LoadingControl.getLoading();
            pLoading.SetExecuteMethod(method);
            pLoading.ShowDialog();
        }

        private void method()
        {
            LoadingControl pLoading = LoadingControl.getLoading();
            for (int i = 0; i < 10; i++)
            {
                pLoading.SetCaptionAndDescription("", "", "執行進度" + i.ToString() + "/10");

                //XXXXXXX

                Thread.Sleep(200);
            }
            LoadingControl.getLoading().CloseLoadingForm();
        }
    }
}
