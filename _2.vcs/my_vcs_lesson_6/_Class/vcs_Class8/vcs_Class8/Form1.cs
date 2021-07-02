using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_Class8
{
    public partial class Form1 : Form
    {
Person[] person_data = new Person[100];  //統一管理物件

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            showCounter();
        }

        private void showCounter()
        {
            lb_count.Text = "目前共有 " + Person.counter() + " 人, ";
            lb_count.Text += "老師 " + Teacher.counter() + " 人, ";
            lb_count.Text += "學生 " + Student.counter() + " 人";

            richTextBox1.Text += "目前共有 " + Person.counter() + " 人, ";
            richTextBox1.Text += "老師 " + Teacher.counter() + " 人, ";
            richTextBox1.Text += "學生 " + Student.counter() + " 人\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "新增老師資料, 建立新表單, 若按OK, 回傳新表單的資料\n";
            tForm tf = new tForm();  //建立老師表單
            if (tf.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "新增老師資料 OK\t加入tf資料之內部物件\n";
                int pos = Person.counter() - 1;
                person_data[pos] = tf.tObj;
                richTextBox1.Text += "新增的老師\r\n" + person_data[pos].show() + "\n";
                showCounter();
            }
            else
            {
                richTextBox1.Text += "新增老師資料 Cancel\n";
            }
            tf.Dispose(); //釋放表單資源
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "新增學生資料, 建立新表單, 若按OK, 回傳新表單的資料\n";
            sForm sf = new sForm(); //建立學生表單
            if (sf.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "新增學生資料 OK\t加入sf資料之內部物件\n";
                int pos = Person.counter() - 1;
                person_data[pos] = sf.sObj;
                richTextBox1.Text += "新增的學生\r\n" + person_data[pos].show() + "\n";
                showCounter();
            }
            else
            {
                richTextBox1.Text += "新增學生資料 Cancel\n";
            }
            sf.Dispose();  //釋放表單資源

        }

        private void button3_Click(object sender, EventArgs e)
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

        private void button4_Click(object sender, EventArgs e)
        {
            FileStream fs = new FileStream("DataFile.dat", FileMode.Create);

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

        private void button5_Click(object sender, EventArgs e)
        {
            FileStream fs = new FileStream("../../DataFile.dat", FileMode.Open);

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

            showCounter();

        }
    }
}
