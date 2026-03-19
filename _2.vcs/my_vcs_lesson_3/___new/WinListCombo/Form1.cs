using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinListCombo
{
    public partial class Form1 : Form
    {
        // 定義Member類別，此類別建立的物件可用來存放會員資料
        class Member
        {
            public string Name { get; set; }    	// 姓名屬性
            public DateTime BirthdDay { get; set; }  	// 生日屬性
            public string Sex { get; set; }            // 性別屬性
            public string Job { get; set; }            // 職業屬性
        }

        // 建立SortedList串列物件 member 用來存放Member會員物件
        // Key鍵值為string型別即會員姓名，Value對應值為Member會員物件
        SortedList<string, Member> member = new SortedList<string, Member>();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //ListBox預設選項
            // 建立Job字串陣列用來存放職業
            String[] Job = new String[] { "士", "農", "工", "商", "兵", "其它" };
            lstJob.Items.AddRange(Job); // lstJob清單放入Job陣列內容
            lstJob.SelectedIndex = 0;   // lstJob清單預設第1個選項被選取
        }

        // 姓名下拉式清單被選取時執行
        private void cboName_SelectedIndexChanged(object sender, EventArgs e)
        {
            // 取得姓名下拉式清單的會員姓名
            // 該會員姓名為 member 串列中的Key鍵值，透過鍵值可找到 member 串列中的某筆會員資料
            // 再將找到的會員資料指定給 sm 物件參考
            Member sm = member[cboName.Text];

            // 透過Member會員物件參考 sm，將找到的會員資料顯示在表單的各控制項上
            cboYear.Text = sm.BirthdDay.Year.ToString();
            cboMonth.Text = sm.BirthdDay.Month.ToString();
            cboDay.Text = sm.BirthdDay.Day.ToString();

            if (sm.Sex == "男")
            {
                rdbF.Checked = true;
            }
            else
            {
                rdbM.Checked = true;
            }

            int JobIndex = lstJob.FindString(sm.Job);
            lstJob.SelectedIndex = JobIndex;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //字串二維陣列
            string[,] members = new string[5, 4] {
            { "Doraemon", "9/3/2112", "男", "士" },
            { "Dorami", "12/2/2114", "女", "農" },
            { "Mickey", "11/18/1928", "男", "工" },
            { "Benny", "8/14/2000", "男", "商" },
            { "Cony", "4/17/2013", "女", "兵" }
            };

            string name = members[0, 0];
            string birthday = members[0, 1];
            string sex = members[0, 2];
            string job = members[0, 3];
            // 將姓名下拉式清單所輸入的值放入下拉式清單的選項內
            cboName.Items.Add(name);
            // 將Member會員物件新增至 member 串列內
            // Key鍵值為會員姓名，Value對應值為Member會員物件
            member.Add(name, new Member() { Name = name, BirthdDay = DateTime.Parse(birthday), Sex = sex, Job = job });

            name = members[1, 0];
            birthday = members[1, 1];
            sex = members[1, 2];
            job = members[1, 3];
            // 將姓名下拉式清單所輸入的值放入下拉式清單的選項內
            cboName.Items.Add(name);
            // 將Member會員物件新增至 member 串列內
            // Key鍵值為會員姓名，Value對應值為Member會員物件
            member.Add(name, new Member() { Name = name, BirthdDay = DateTime.Parse(birthday), Sex = sex, Job = job });

            name = members[2, 0];
            birthday = members[2, 1];
            sex = members[2, 2];
            job = members[2, 3];
            // 將姓名下拉式清單所輸入的值放入下拉式清單的選項內
            cboName.Items.Add(name);
            // 將Member會員物件新增至 member 串列內
            // Key鍵值為會員姓名，Value對應值為Member會員物件
            member.Add(name, new Member() { Name = name, BirthdDay = DateTime.Parse(birthday), Sex = sex, Job = job });

            name = members[3, 0];
            birthday = members[3, 1];
            sex = members[3, 2];
            job = members[3, 3];
            // 將姓名下拉式清單所輸入的值放入下拉式清單的選項內
            cboName.Items.Add(name);
            // 將Member會員物件新增至 member 串列內
            // Key鍵值為會員姓名，Value對應值為Member會員物件
            member.Add(name, new Member() { Name = name, BirthdDay = DateTime.Parse(birthday), Sex = sex, Job = job });

            name = members[4, 0];
            birthday = members[4, 1];
            sex = members[4, 2];
            job = members[4, 3];
            // 將姓名下拉式清單所輸入的值放入下拉式清單的選項內
            cboName.Items.Add(name);
            // 將Member會員物件新增至 member 串列內
            // Key鍵值為會員姓名，Value對應值為Member會員物件
            member.Add(name, new Member() { Name = name, BirthdDay = DateTime.Parse(birthday), Sex = sex, Job = job });
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string check_name = "Doraemon";
            // 使用ContainsKey方法檢查會員的鍵值(姓名)是否在 member 串列物件中
            if (member.ContainsKey(check_name))
            {
                richTextBox1.Text += "資料已存在!\n";
            }
            else
            {
                richTextBox1.Text += "無此資料\n";
            }

            check_name = "Jerry";
            // 使用ContainsKey方法檢查會員的鍵值(姓名)是否在 member 串列物件中
            if (member.ContainsKey(check_name))
            {
                richTextBox1.Text += "資料已存在!\n";
            }
            else
            {
                richTextBox1.Text += "無此資料\n";
            }

        }
    }
}
