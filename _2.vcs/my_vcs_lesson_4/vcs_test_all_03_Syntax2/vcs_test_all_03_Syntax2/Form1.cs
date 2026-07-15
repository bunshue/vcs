using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_03_Syntax2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        private void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            richTextBox1.Size = new Size(400, 690);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1070, 750);
            this.Text = "vcs_test_all_03_Syntax2";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            //使用 ref
            byte[] number = new byte[6];
            //呼叫靜態方法，以陣列為引數
            Lotto(ref number);
            Console.WriteLine("今天的樂透--");
            //讀取陣列元素
            foreach (byte item in number)
            {
                Console.Write("{item}, 3");
            }
        }


        //靜態方法
        static void Lotto(ref byte[] anyArr)
        {
            //以Random類別呼叫NextBytes()方法產生隨機數
            Random rand = new Random();
            //建立能存放6個元素的陣列
            anyArr = new byte[6];
            rand.NextBytes(anyArr);
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            //Call By Value / Reference

            //傳值
            //Call by Value vs Call by Reference
            //value

            richTextBox1.Text += string.Format("\n  **** Call By Value 傳值呼叫 **** \n");
            int a = 10;
            int b = 12;
            richTextBox1.Text += string.Format("\n呼叫敘述 未進入方法前\t\t：a= {0} b={1}", a, b);
            CallValue(a, b);
            richTextBox1.Text += string.Format("\n呼叫敘述 離開方法回原處時\t：a={0}  b={1}", a, b);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //傳址
            //reference

            richTextBox1.Text += string.Format("\n  **** Call By Reference 參考呼叫 **** \n");
            a = 10;
            b = 12;
            richTextBox1.Text += string.Format("\n呼叫敘述 未進入方法前\t：a= {0}  b={1}", a, b);
            CallRef(ref a, ref b);
            richTextBox1.Text += string.Format("\n呼叫敘述 離開方法回原處\t：a= {0}  b={1}", a, b);
        }


        private static void CallValue(int x, int y)
        {
            int z;
            x = 20;
            y = 30;
            //richTextBox1.Text +=string.Format("\n方法內 交換前\t\t\t：x= {0}   y={1} ", x, y);
            z = x;   //透過第三個變數來做x,y值作互換
            x = y;
            y = z;
            //richTextBox1.Text += string.Format("\n方法內 交換後\t\t\t：x= {0}   y={1}", x, y);
        }

        private static void CallRef(ref int x, ref int y)
        {
            int z;
            x = 20;
            y = 30;
            //richTextBox1.Text +=string.Format("\n方法內 交換前\t\t：x= {0}   y={1} ", x, y);
            z = x;  //透過第三個變數來做x,y值作互換
            x = y;
            y = z;
            //richTextBox1.Text += string.Format("\n方法內 交換後\t\t：x= {0}   y={1} ", x, y);
        }

        //------------------------------------------------------------  # 60個

        private void button2_Click(object sender, EventArgs e)
        {
            //傳值 vs 傳址

            //傳值

            int a = 10, b = 15;
            //label1.Text = "1.主程式:呼叫方法前: a = " + a.ToString() + "  b = " + b.ToString() + "\n\n";
            PassValue(a, b);
            //label1.Text += "4.主程式:呼叫方法後: a = " + a.ToString() + "  b = " + b.ToString() + "\n\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //傳址

            //label1.Text = "1.主程式:呼叫方法前: a = " + a.ToString() + "  b = " + b.ToString() + "\n\n";
            PassRef(ref a, ref b);
            //label1.Text += "4.主程式:呼叫方法後: a = " + a.ToString() + "  b = " + b.ToString() + "\n\n";

        }

        //以傳值方式呼叫PassValue方法
        private void PassValue(int x, int y)
        {
            //label1.Text += "2.方法中:變數計算前: x = " + x.ToString() + "  y = " + y.ToString() + "\n\n";
            x += 3; //虛引數x加3
            y += 2; //虛引數y加2
            //label1.Text += "3.方法中:變數計算後: x = " + x.ToString() + "  y = " + y.ToString() + "\n\n";
        }

        //以參考呼叫PassRef方法
        private void PassRef(ref int x, ref int y)
        {
            //label1.Text += "2.方法中:變數計算前: x = " + x.ToString() + "  y = " + y.ToString() + "\n\n";
            x += 3; //虛引數x加3
            y += 2; //虛引數y加2
            //label1.Text += "3.方法中:變數計算後: x = " + x.ToString() + "  y = " + y.ToString() + "\n\n";
        }

        //------------------------------------------------------------  # 60個


        private void button3_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
        {
        }

        private void button21_Click(object sender, EventArgs e)
        {
        }

        private void button22_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {
        }

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
        }

        private void button27_Click(object sender, EventArgs e)
        {
        }

        private void button28_Click(object sender, EventArgs e)
        {
        }

        private void button29_Click(object sender, EventArgs e)
        {
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/

