using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;       // 引用System.Windows.Forms

namespace InheritsForm
{
    //MyForm繼承Form類別
    class MyForm : Form
    {
        Button btnOk;	       //宣告btnOk按鈕 
        TextBox txtName;       //宣告txtName文字方塊
        public MyForm()
        {
            //建立btnOk為Button按鈕，並設定屬性
            btnOk = new Button();
            btnOk.Text = "確定";
            btnOk.Width = 60;
            btnOk.Height = 25;
            btnOk.Visible = true;
            btnOk.Left = 20;
            btnOk.Top = 15;
            //建立btnOk為TextBox文字方塊，並設定屬性
            txtName = new TextBox();
            txtName.Width = 100;
            txtName.Height = 30;
            txtName.Visible = true;
            txtName.Left = 100;
            txtName.Top = 15;
            this.Width = 250;    //表單寬設為250
            this.Height = 100;   //表單高設為100
            this.Controls.Add(btnOk);       //表單放入btnOK按鈕
            this.Controls.Add(txtName);     //表單放入txtName文字方塊
            this.Text = "MyForm類別視窗";
            //指定btnOk.Click事件的事件處理函式為btnOk_Click
            btnOk.Click += new EventHandler(btnOk_Click);
        }
        // btnOk_Click事件處理函式
        private void btnOk_Click(object sender, EventArgs e)
        {
            //顯示對話方塊
            MessageBox.Show(txtName.Text + " 您好");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            MyForm f = new MyForm();    //建立f 為MyForm類別
            f.ShowDialog();			//呼叫f.ShowDialog()方法使視窗顯示
        }
    }
}



