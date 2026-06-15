using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;  // For FileMode

namespace vcs_Class2
{
    public partial class Form1 : Form
    {
        Person[] person_data = new Person[100];  //統一管理物件
        ShapeCollection ShapeManager = new ShapeCollection();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            showCounter1();
            showCounter2();
        }

        private void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            groupBox1.Size = new Size(200, 450);
            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox2.Size = new Size(200, 310);
            groupBox2.Location = new Point(x_st + dx * 0, y_st + dy * 6 + 30);

            richTextBox1.Size = new Size(600, 760);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            x_st = 10;
            y_st = 100;
            lb_count1.Location = new Point(x_st + dx * 0, y_st + dy * 0 - 80);
            bt_class00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_class01.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_class02.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_class03.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_class04.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            lb_count2.Location = new Point(x_st + dx * 0, y_st + dy * 0 - 80);
            bt_class10.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_class11.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_class12.Location = new Point(x_st + dx * 0, y_st + dy * 2);

            this.Size = new Size(870, 820);
            this.Text = "vcs_Class2";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void showCounter1()
        {
            lb_count1.Text = "目前共有 " + Person.counter() + " 人\n";
            lb_count1.Text += "老師 " + Teacher.counter() + " 人\n";
            lb_count1.Text += "學生 " + Student.counter() + " 人";

            richTextBox1.Text += "目前共有 " + Person.counter() + " 人, ";
            richTextBox1.Text += "老師 " + Teacher.counter() + " 人, ";
            richTextBox1.Text += "學生 " + Student.counter() + " 人\n";
        }

        private void bt_class00_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "新增老師資料, 建立新表單, 若按OK, 回傳新表單的資料\n";
            tForm tf = new tForm();  //建立老師表單
            if (tf.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "新增老師資料 OK\t加入tf資料之內部物件\n";
                int pos = Person.counter() - 1;
                person_data[pos] = tf.tObj;
                richTextBox1.Text += "新增的老師\r\n" + person_data[pos].show() + "\n";
                showCounter1();
            }
            else
            {
                richTextBox1.Text += "新增老師資料 Cancel\n";
            }
            tf.Dispose(); //釋放表單資源
        }

        private void bt_class01_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "新增學生資料, 建立新表單, 若按OK, 回傳新表單的資料\n";
            sForm sf = new sForm(); //建立學生表單
            if (sf.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "新增學生資料 OK\t加入sf資料之內部物件\n";
                int pos = Person.counter() - 1;
                person_data[pos] = sf.sObj;
                richTextBox1.Text += "新增的學生\r\n" + person_data[pos].show() + "\n";
                showCounter1();
            }
            else
            {
                richTextBox1.Text += "新增學生資料 Cancel\n";
            }
            sf.Dispose();  //釋放表單資源
        }

        private void bt_class02_Click(object sender, EventArgs e)
        {
            string str = "<<< 成員列表 >>>\r\n";
            for (int i = 0; i < Person.counter(); i++)
                str += person_data[i].show() + "--------------------\r\n";
            richTextBox1.Text += str;



            richTextBox1.Text += "共有成員 " + Person.counter().ToString() + " 人\n";
            richTextBox1.Text += "<<< 成員列表 >>>\n";
            for (int i = 0; i < Person.counter(); i++)
            {
                richTextBox1.Text += person_data[i].show() + "--------------------\n";
            }
        }

        private void bt_class03_Click(object sender, EventArgs e)
        {
            FileStream fs = new FileStream("tmp_SchoolMemberDataFile.dat", FileMode.Create);

            BinaryWriter bw = new BinaryWriter(fs);

            for (int i = 0; i < Person.counter(); i++)
            {
                string classname = person_data[i].GetType().Name;  //類別名稱

                bw.Write(classname);  //儲存類別名稱

                bw.Write(person_data[i].getName());  //儲存父類別Person的成員
                bw.Write(person_data[i].getAge());
                bw.Write(person_data[i].getGender());

                Date d = person_data[i].getDate();

                bw.Write(d.getYear());
                bw.Write(d.getMonth());
                bw.Write(d.getDay());

                if (classname == "Teacher") //儲存子類別Teacher的成員
                {
                    bw.Write(((Teacher)person_data[i]).getRank());
                }
                else if (classname == "Student") //儲存子類別Student的成員
                {
                    bw.Write(((Student)person_data[i]).getChinese());
                    bw.Write(((Student)person_data[i]).getMath());
                }
            }

            bw.Flush();
            bw.Close();
            fs.Close();
        }

        private void bt_class04_Click(object sender, EventArgs e)
        {
            FileStream fs = new FileStream("../../SchoolMemberDataFile.dat", FileMode.Open);

            BinaryReader br = new BinaryReader(fs);

            int i = Person.counter(); //以附加的方式匯入

            while (br.PeekChar() >= 0)
            {
                string classname = br.ReadString(); //讀取類別名稱

                string name = br.ReadString(); //讀取父類別Person的成員
                int age = br.ReadInt32();
                char gender = br.ReadChar();

                int year = br.ReadInt32();
                int month = br.ReadInt32();
                int day = br.ReadInt32();

                if (classname == "Teacher")
                {
                    //讀取子父類別Teacher的成員，建立Teacher物件                    
                    person_data[i] = new Teacher(name, age, gender, new Date(day, month, year), br.ReadString());
                }
                else if (classname == "Student")
                {
                    //讀取子父類別Student的成員，建立Student物件
                    person_data[i] = new Student(name, age, gender, new Date(day, month, year), br.ReadInt32(), br.ReadInt32());
                }
                i++;
            }

            br.Close();
            fs.Close();

            showCounter1();
        }

        //------------------------------------------------------------  # 60個

        private void showCounter2()
        {
            lb_count2.Text = ShapeManager.getCount().ToString();
        }

        private void bt_class10_Click(object sender, EventArgs e)
        {
            //新增三角形
            richTextBox1.Text += "新增三角形, 建立新表單, 若按OK, 回傳新表單的資料\n";
            TriangleForm tForm = new TriangleForm();

            if (tForm.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "新增三角形 OK\t加入tForm資料之內部物件\n";
                ShapeManager.add(tForm.tObj);
                richTextBox1.Text += "內容\t" + tForm.tObj.show() + "\n";
                showCounter2();
            }
            else
            {
                richTextBox1.Text += "新增三角形 Cancel\n";
            }
            tForm.Dispose();
        }

        private void bt_class11_Click(object sender, EventArgs e)
        {
            //新增矩形
            richTextBox1.Text += "新增矩形, 建立新表單, 若按OK, 回傳新表單的資料\n";
            RectangleForm rForm = new RectangleForm();

            if (rForm.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "新增矩形 OK\t加入rForm資料之內部物件\n";
                ShapeManager.add(rForm.rObj);
                richTextBox1.Text += "內容\t" + rForm.rObj.show() + "\n";
                showCounter2();
            }
            else
            {
                richTextBox1.Text += "新增矩形 Cancel\n";
            }
            rForm.Dispose();
        }

        private void bt_class12_Click(object sender, EventArgs e)
        {
            //info
            richTextBox1.Text += "目前共有 " + ShapeManager.getCount() + " 個圖形\n";
            richTextBox1.Text += "內容:\n";
            richTextBox1.Text += ShapeManager.listing() + "\n";
            richTextBox1.Text += "圖形次序: " + ShapeManager.rankShape() + "\n";
            richTextBox1.Text += "最大圖形: " + ShapeManager.maxShape() + "\n";
        }

        //------------------------------------------------------------  # 60個
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



/*
測試struct與class

        public struct MyRectangle
        {
            public string name;
            public int x_st;        //顯示座標x
            public int y_st;        //顯示座標y
            public int w;           //width
            public int h;           //height
            public int line_out;    //邊框大小
            public Color c_out;     //邊框顏色
            public Color c_in;      //內部顏色

        } 

        private void button4_Click(object sender, EventArgs e)
        {
            MyRectangle r1 = new MyRectangle();
        }

        public static class define  //define some constant
        {
            public const int MAX_LENGTH_OF_IDENTICARDID = 20;   //maximum length of identicardid
            public const int MAX_LENGTH_OF_NAME = 50;           //maximum length of name
            public const int MAX_LENGTH_OF_COUNTRY = 50;        //maximum length of country
            public const int MAX_LENGTH_OF_NATION = 50;         //maximum length of nation
            public const int MAX_LENGTH_OF_BIRTHDAY = 8;        //maximum length of birthday
            public const int MAX_LENGTH_OF_ADDRESS = 200;       //maximum length of address
        }

*/

