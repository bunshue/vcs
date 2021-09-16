using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinFormPolymorphism5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
         // 宣告Control類別的參考物件變數objToMove
         Control objToMove;
         // 表單載入時執行
         private void Form1_Load(object sender, EventArgs e)
         {
             objToMove = comboBox1; // objToMove參考指向comboBox1
         }

         // 按一下comboBox1時執行
         private void comboBox1_Click(object sender, EventArgs e)
         {
             objToMove = comboBox1; // objToMove參考指向comboBox1
         }
        
         // 按一下button1時執行
         private void button1_Click(object sender, EventArgs e)
         {
             objToMove = button1; // objToMove參考指向button1
         }

         // 按一下linkLabel1時執行
         private void linkLabel1_Click(object sender, EventArgs e)
         {
             objToMove = linkLabel1; // objToMove參考指向linkLabel1
         }

         // 按一下checkBox1時執行
         private void checkBox1_Click(object sender, EventArgs e)
         {
             objToMove = checkBox1; // objToMove參考指向checkBox1
         }

         // 按一下btnMove1(向右移動鈕)時執行
         private void btnMove_Click(object sender, EventArgs e)
         {
             // 目前objToMove參考指向的控制項往右移動 10 Pixel
             objToMove.Left += 10;
         }


         
        

        

      

       

       
    }
}
