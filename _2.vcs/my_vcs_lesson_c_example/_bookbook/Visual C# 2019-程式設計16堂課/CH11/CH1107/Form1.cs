using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1107
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //初始化cobSubject-建立陣列，再以AddRange()方法加入
            string[] subject =
               { "日語入門", "多媒體導論", "資料庫", "英文會話" };
            cobSubject.Items.AddRange(subject);
            //設定文字方塊的字型
            rtxtChoice.SelectionFont = new Font("標楷體", 14);
        }

        private void btnOK_Click(object sender, EventArgs e)
        {
            //空陣列，儲存資料
            string[] tmp = new string[4];
            //屬性SelectedItem取得ComboBox選取的項目值
            var item = cobMain.SelectedItem;
            var course = cobSubject.SelectedItem;
            //將取得的資料依序放入陣列
            tmp[0] = $"日期：{dtpLogin.Text}";
            tmp[1] = $"名稱：{txtName.Text}";
            tmp[2] = $"主科目：{item}";
            tmp[3] = $"副科目：{course}";
            //將陣列的內容利用屬性Lines放入文字方塊中
            rtxtChoice.Lines = tmp;
        }
    }
}
