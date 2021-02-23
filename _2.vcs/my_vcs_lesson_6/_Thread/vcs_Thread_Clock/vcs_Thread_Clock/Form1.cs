using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
namespace vcs_Thread_Clock
{
    public partial class Form1 : Form
    {
        private ChangeTime timechange;
        public Form1()
        {
            InitializeComponent();


            //產生一個類別，專門來管理時間運作
            timechange = new ChangeTime(this);
            //timechange.change();


            //使用一個thread來增加時間的秒數
            System.Threading.Thread thread = new System.Threading.Thread(new System.Threading.ThreadStart(timechange.run));
            thread.Start();

            //this.

        }
        //委派function
        public delegate void InvokeFunction(int h, int m, int s);
        //設定時間
        public void setTime(int h,int m,int s) 
         { 
            setHH(h);
            setMM(m);
            setSS(s);
        } 


        public void setHH(int h)
        {
            this.label1.Text = h.ToString();
        }
        public void setMM(int m)
        {
            this.label2.Text = m.ToString();
        }
        public void setSS(int s)
        {
            this.label3.Text = s.ToString();
        }




    }
}
