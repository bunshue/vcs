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

        // 建立SortedList串列物件 m 用來存放Member會員物件
        // Key鍵值為string型別即會員姓名，Value對應值為Member會員物件
        SortedList<string, Member> m = new SortedList<string, Member>();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // 年下拉式清單預設值100年前
            cboYear.Text = (DateTime.Now.Year - 100).ToString();
            cboMonth.Text = "1"; // 月下拉式清單預設值1
            cboDay.Text = "1";      // 日下拉式清單預設值 1
            // 年下拉式清單的範圍100年前~今年
            for (int i = DateTime.Now.Year - 100; i <= DateTime.Now.Year; i++)
            {
                cboYear.Items.Add(i.ToString());
            }
            for (int i = 1; i <= 12; i++) // 月下拉式清單的範圍是1-12
            {
                cboMonth.Items.Add(i.ToString());
            }
            for (int i = 1; i <= 31; i++) // 日下拉式清單的範圍是1-31
            {
                cboDay.Items.Add(i.ToString());
            }
            rdbM.Checked = true;  // 男選項鈕預設被選取
            // 建立Job字串陣列用來存放職業
            String[] Job = new String[] { "學生", "公教", "服務", "製造", "家管", "其它" };
            lstJob.Items.AddRange(Job); // lstJob清單放入Job陣列內容
            lstJob.SelectedIndex = 0;   // lstJob清單預設第1個選項被選取
        }

        // 按新增鈕執行
        private void btnAdd_Click(object sender, EventArgs e)
        {
            if (cboName.Text == "")  // 檢查姓名是否為空字串
            {
                MessageBox.Show("請輸入姓名");
                return;   // 離開此事件處理函式
            }
            // 使用ContainsKey方法檢查會員的鍵值(姓名)是否在 m 串列物件中
            if (m.ContainsKey(cboName.Text))
            {
                MessageBox.Show("資料已存在!");
                return; // 離開此事件處理函式
            }
            else
            {
                // 建立日期物件用來存放會員的生日
                DateTime myBirthDay = new DateTime();
                try   // 使用例外處理補捉輸入生日可能會發生的例外
                {
                    myBirthDay = DateTime.Parse
                    (cboYear.Text + "/" + cboMonth.Text + "/" + cboDay.Text);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("生日有誤");
                    return;  // 如果生日有誤即離開此事件處理函式
                }
                // 將姓名下拉式清單所輸入的值放入下拉式清單的選項內
                cboName.Items.Add(cboName.Text);

                // 將Member會員物件新增至 m 串列內
                // Key鍵值為會員姓名，Value對應值為Member會員物件
                m.Add(cboName.Text, new Member() { Name = cboName.Text, BirthdDay = myBirthDay, Sex = rdbF.Checked ? "男" : "女", Job = lstJob.SelectedItem.ToString() });
                MessageBox.Show("會員新增成功");
            }
        }

        // 姓名下拉式清單被選取時執行
        private void cboName_SelectedIndexChanged(object sender, EventArgs e)
        {
            // 取得姓名下拉式清單的會員姓名
            // 該會員姓名為 m 串列中的Key鍵值，透過鍵值可找到 m 串列中的某筆會員資料
            // 再將找到的會員資料指定給 sm 物件參考
            Member sm = m[cboName.Text];

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
    }
}
