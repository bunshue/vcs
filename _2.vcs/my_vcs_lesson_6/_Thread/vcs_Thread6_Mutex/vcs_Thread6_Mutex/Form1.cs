using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading; //for Mutex

//使用Mutex禁止程式重複啟動

namespace vcs_Thread6_Mutex
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bool Exist = false; //定義一個變量, 用來表示是否已經運行
            //建立一個Mutex
            Mutex mutex = new Mutex(true, "僅一次", out Exist);
            if (Exist == true)//如果没有運行
            {
                mutex.ReleaseMutex();    //運行新表單
            }
            else
            {
                MessageBox.Show("本程式禁止重複啟動", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
                this.Close();
            }
        }
    }
}

