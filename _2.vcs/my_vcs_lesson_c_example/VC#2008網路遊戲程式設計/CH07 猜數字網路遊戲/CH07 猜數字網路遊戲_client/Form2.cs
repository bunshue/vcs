using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Windows.Forms;

using System.Net;
using System.Net.Sockets; //ServerSocket = new Socket(...)時使用
using System.Threading;  //Thread時使用
using System.Text;       //Encoding.Unicode.GetString(...) 時使用
using System.IO;         //使用FileInfo類別，來建立一個檔案實體物件

namespace 猜數字_網路對戰_client
{
    public partial class Form2 : System.Windows.Forms.Form 
    {
      
        int  enter;
     
        public Form2()
        {
            InitializeComponent();
        }
        public static string rand;
        public string Rand
        {

            set { rand = value;  }


            get { return rand; }

        }
        
        
        private void Form2_Load(object sender, EventArgs e)
        {

            timer1.Enabled = true;
        }
     
        private void button1_Click(object sender, EventArgs e)
        {

            if (button1.Text == "清空提示")
            {

                    label1.Text = "提示 :";
                    if (textBox1.Enabled == true) textBox1.Enabled = false;
                    textBox1.Text = "";
                   
                    
            }          
            
        }
        
        private void checknumber()
        {
            if (enter < int.Parse(rand))  label1.Text = label1.Text + "\n使用者輸入:" + enter + "\n" + enter + " < Ｘ" ;
                           
            else if (enter > int.Parse(rand)) label1.Text = label1.Text + "\n使用者輸入:" + enter + "\n" + enter + " > Ｘ" ;

            else 
            {
                    Form1 f1 = new Form1();
                    
                   
                    f1.Win = "win";
                    MessageBox.Show("恭喜你答對了。贏了");
                    
                    
                    
            }
            textBox1.Text = "";
            
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (textBox1.Text != "")
            {

                enter = int.Parse(textBox1.Text);

                if (enter < 1000) checknumber();

            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (rand != null)
            {
                textBox1.Enabled = true;
                timer1.Enabled = false;
            }
        }
        
    }
}
