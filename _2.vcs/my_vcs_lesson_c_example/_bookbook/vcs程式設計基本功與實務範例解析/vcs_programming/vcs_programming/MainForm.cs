using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;


namespace vcs_programming
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void radioButton3_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void btnExit_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        Person[] P = new Person[100];  //統一管理物件
        
        private void MainForm_Load(object sender, EventArgs e)
        {
            showCounter();
        }

        private void showCounter()
        {
            lblCounter.Text = "目前共有" + Person.counter() + "人, ";
            lblCounter.Text += "學生" + Student.counter() + "人, ";
            lblCounter.Text += "老師" + Teacher.counter() + "人";
        }

        private void btnEnter_Click(object sender, EventArgs e)
        {
            // add a Teacher
            if (rdbTeacher.Checked) {
                tForm tf = new tForm();  //建立老師表單
                if (tf.ShowDialog() == DialogResult.OK) { //開啟表單
                    int pos = Person.counter() - 1;
                    P[ pos ] = tf.tObj;
                    txtOutput.Text = "新增的老師\r\n" + P[pos].show() + "\r\n";
                    showCounter();
                }
                tf.Dispose(); //釋放表單資源
            }
            // add a Student
            if (rdbStudent.Checked) {
                sForm sf = new sForm(); //建立學生表單
                if (sf.ShowDialog() == DialogResult.OK) { //開啟表單
                    int pos = Person.counter()-1;
                    P[pos] = sf.sObj;
                    txtOutput.Text = "新增的學生\r\n" + P[pos].show() + "\r\n";
                    showCounter();
                }
                sf.Dispose();  //釋放表單資源
            }
            //list all elements
            if (rdbAllElements.Checked) {
                string str = "<<< 成員列表 >>>\r\n";
	            for(int i = 0; i < Person.counter(); i++)
		            str += P[i].show() + "--------------------\r\n";
                txtOutput.Text = str;
            }            
        }

        private void btnSave_Click(object sender, EventArgs e)
        {
            FileStream fs = new FileStream("DataFile.dat", FileMode.Create);

            BinaryWriter bw = new BinaryWriter(fs);

            for (int i = 0; i < Person.counter(); i++)
            {
                //MessageBox.Show(P[i].GetType().Name);
                string classname = P[i].GetType().Name;  //類別名稱

                bw.Write(classname);  //儲存類別名稱

                bw.Write(P[i].getName());  //儲存父類別Person的成員
                bw.Write(P[i].getAge());
                bw.Write(P[i].getGender());

                Date d = P[i].getDate();

                bw.Write(d.getYear());
                bw.Write(d.getMonth());
                bw.Write(d.getDay());

                if (classname == "Teacher") //儲存子類別Teacher的成員
                {
                    bw.Write(((Teacher)P[i]).getRank());
                }
                else if (classname == "Student") //儲存子類別Student的成員
                {
                    bw.Write(((Student)P[i]).getChinese());
                    bw.Write(((Student)P[i]).getMath());
                }
            }

            bw.Flush();
            bw.Close();
            fs.Close();
        }

        private void btnLoad_Click(object sender, EventArgs e)
        {
            FileStream fs = new FileStream("DataFile.dat", FileMode.Open);

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

                if (classname == "Teacher") {
                    //讀取子父類別Teacher的成員，建立Teacher物件                    
                    P[ i ] = new Teacher(name, age, gender,
                                         new Date(day, month, year),
                                         br.ReadString());
                }
                else if (classname == "Student") {
                    //讀取子父類別Student的成員，建立Student物件
                    P[i] = new Student(name, age, gender,
                                       new Date(day, month, year),
                                       br.ReadInt32(),
                                       br.ReadInt32());
                }

                i++;
            }

            br.Close();
            fs.Close();

            showCounter();
        }
    }
}
