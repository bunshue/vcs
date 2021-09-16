using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinFormPolymorphism4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
         Cal myCal;  // 宣告Cal類別物件myCal
         CalAdd myCalAdd = new CalAdd(); // 建立CalAdd類別物件myCalAdd
         CalSub myCalSub = new CalSub(); // 建立CalSub類別物件myCalSub
         CalMul myCalMul = new CalMul(); // 建立CalMul類別物件myCalMul
         CalDiv myCalDiv = new CalDiv(); // 建立CalDiv類別物件myCalDiv

         // 表單載入時執行
         private void Form1_Load(object sender, EventArgs e)
         {
             myCal = myCalAdd;   // myCal參考指向myCalAdd物件
             txtAns.ReadOnly = true;
         }

         // 當 [加] 選項按鈕Checked屬性值變更時執行
         private void rdbAdd_CheckedChanged(object sender, EventArgs e)
         {
             myCal = myCalAdd;   // myCal參考指向myCalAdd物件
         }
        
         // 當 [減] 選項按鈕Checked屬性值變更時執行
         private void rdbSub_CheckedChanged(object sender, EventArgs e)
         {
             myCal = myCalSub;   // myCal參考指向myCalSub物件
         }

         // 當 [乘] 選項按鈕Checked屬性值變更時執行
         private void rdbMul_CheckedChanged(object sender, EventArgs e)
         {
             myCal = myCalMul;   // myCal參考指向myCalMul物件
         }

         // 當 [除] 選項按鈕Checked屬性值變更時執行
         private void rdbDiv_CheckedChanged(object sender, EventArgs e)
         {
             myCal = myCalDiv;   // myCal參考指向myCalDiv物件
         }

         // 當按下 [計算] 鈕時執行
         private void btnCal_Click(object sender, EventArgs e)
         {
             try
             {
                 myCal.X = int.Parse(txtX.Text);
                 myCal.Y = int.Parse(txtY.Text);
                 // 執行Answer方法進行X, Y兩數的加, 減, 乘或除法
                 // 並將結果顯示在txtAns文字方塊上
                 txtAns.Text = myCal.Answer().ToString();
             }
             catch (Exception ex)
             {
                 // MessageBox.Show方法可顯示對話方塊
                 MessageBox.Show(ex.Message);
             }
         }


         
       


         

        

         

        

         
     }
 }
