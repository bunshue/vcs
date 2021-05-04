using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using ADOX;
using JRO;
using System.IO; 
//首先引用C:\Program Files\Common Files\System\ado\msadox.dll,該DLL包含ADOX命名空間;
//接著引用C:\Program Files\Common Files\System\ado\msjro.dll,該DLL包含JRO命名空間
namespace 如何編程修復Access數據庫
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        //打開選擇數庫咱徑
        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "Access數據庫|*.mdb";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                textBox1.Text = openFileDialog1.FileName;
                strPathMdb = textBox1.Text.TrimEnd();
            }

        }
        //開始壓縮數據庫庫
        string strPathMdb = null;
        private void button2_Click(object sender, EventArgs e)
        {
            if (!File.Exists(strPathMdb)) //檢查數據庫是否已存在
            {

                MessageBox.Show("目標數據庫不存在,無法壓縮","操作提示");
                return;
            }
            //宣告臨時數據庫的名稱
            string temp = DateTime.Now.Year.ToString();
            temp += DateTime.Now.Month.ToString();
            temp += DateTime.Now.Day.ToString();
            temp += DateTime.Now.Hour.ToString();
            temp += DateTime.Now.Minute.ToString();
            temp += DateTime.Now.Second.ToString() + ".bak";
            temp = strPathMdb.Substring(0, strPathMdb.LastIndexOf("\\") + 1) + temp;
            //定義臨時數據庫的連接字串
            string temp2 = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + temp;
            //定義目標數據庫的連接字串
            string strPathMdb2 = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + strPathMdb;
            //建立一個JetEngineClass對象的實例
            JRO.JetEngineClass jt = new JRO.JetEngineClass();
            //使用JetEngineClass對象的CompactDatabase方法壓縮修復數據庫
            jt.CompactDatabase(strPathMdb2, temp2);
            //拷貝臨時數據庫到目標數據庫(覆蓋)
            File.Copy(temp, strPathMdb, true);
            //最後刪除臨時數據庫
            File.Delete(temp);
            MessageBox.Show("修復完成");
        }
        ////////////////////
  

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }


        ///////////////////////
    }
}