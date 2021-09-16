using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

 // 引用System.Windows.Forms命名空間
 // 如此才能使用較簡潔的物件名稱來使用Form, Button, TextBox, Label...等類別
 using System.Windows.Forms;
 

namespace ConsoleWinForm1
{
     // 定義Form1繼承System.Windows.Forms命名空間下的Form類別
     class Form1 : Form
     { 
         // 宣告System.Windows.Forms命名空間下的Label標籤
         Label lblName;  	// 物件名稱為lblName

         // 宣告System.Windows.Forms命名空間下的Button按鈕
         Button btnOk;   	// 物件名稱為btnOk

         // 宣告System.Windows.Forms命名空間下的TextBok文字方塊
         TextBox txtName;	// 物件名稱為txtName
 
         public Form1()  // Form1類別的建構式
         {
             //建立lblName為Label標籤物件名稱，並設定屬性
             lblName = new Label();
             lblName.Text = "姓名";
             lblName.AutoSize = true;
             lblName.Visible = true;
             lblName.Left = 60;
             lblName.Top = 55;             

             //建立txtName為TextBox文字方塊物件名稱，並設定屬性
             txtName = new TextBox();
             txtName.Width = 100;
             txtName.Height = 30;
             txtName.Visible = true;
             txtName.Left = 100;
             txtName.Top = 45;

             //建立btnOk為Button按鈕物件名稱，並設定屬性
             btnOk = new Button();
             btnOk.Text = "確定";
             btnOk.Width = 60;
             btnOk.Height = 25;
             btnOk.Visible = true;
             btnOk.Left = 140;
             btnOk.Top = 100;

             // 設定表單大小和建立相關控制項
             this.Width = 250;    //表單寬設為250
             this.Height = 200;   //表單高設為130
             this.Controls.Add(lblName);   	//表單放入lblNam標籤
             this.Controls.Add(btnOk);      //表單放入btnOK按鈕
             this.Controls.Add(txtName);    //表單放入txtName文字方塊        
             this.Text = "主控模式的視窗程式"; // 表單標題欄文字

             //指定btnOk.Click事件的事件處理函式為btnOk_Click
             // 即當使用者在btnOk按一下時會執行btnOk_Click事件處理函式
             btnOk.Click += new EventHandler(btnOk_Click);
         }
 
         // 當按下 [確定] 鈕時執行
         private void btnOk_Click(object sender, EventArgs e)
         {
       // 使用System.Windows.Forms命名空間下的messBox.Show方法顯示對話方塊
             MessageBox.Show(txtName.Text + " 您好 !,","Hello 訊息對話方塊");
         }
     }

    class Program
    {
        static void Main(string[] args)
        {
             Form1 f = new Form1();	// 建立f表單物件為Form1類別
             f.ShowDialog();		//呼叫f.ShowDialog()方法使視窗顯示
        }
    }
}
