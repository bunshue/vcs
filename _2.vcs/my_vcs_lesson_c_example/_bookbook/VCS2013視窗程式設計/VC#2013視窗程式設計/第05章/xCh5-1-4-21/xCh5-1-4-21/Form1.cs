using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh5_1_4_21
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // 新增ComboBox物件的選項，下列人名取自MSDN範例
            // 第2筆及最後1筆特別加上xx，只是為了方等會執行時方便輸入
            string[] employees = new string[]{"Hamilton, David", "xxHensien, Kari",
				"Hammond, Maria", "Harris, Keith", "Henshaw, Jeff D.", 
				"Hanson, Mark", "Harnpadoungsataya, Sariya", 
				"Harrington, Mark", "Harris, Keith", "Hartwig, Doris", 
				"Harui, Roger", "Hassall, Mark", "Hasselberg, Jonas", 
				"Harnpadoungsataya, Sariya", "Henshaw, Jeff D.", 
				"Henshaw, Jeff D.", "Hensien, Kari", "Harris, Keith", 
				"Henshaw, Jeff D.", "Hensien, Kari", "Hasselberg, Jonas",
				"Harrington, Mark", "Hedlund, Magnus", "Hay, Jeff", 
				"xxHensien, Kari"};

            comboBox1.Items.AddRange(employees);

            label1.Text = "姓名：";
            button1.Text = "查詢";
            button2.Text = "刪除";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int count = 0;
            int resultIndex = -1;

            resultIndex = comboBox1.FindString(textBox1.Text);
            int myFlag = 0;
            if (resultIndex != -1) myFlag = resultIndex;

            while (resultIndex != -1)
            {
                // FindString會循環的找，所以又重頭時，要離開
                count += 1;
                resultIndex = comboBox1.FindString(textBox1.Text, resultIndex);
                if (resultIndex == myFlag) break;
            }
            
            MessageBox.Show("共有 " + count.ToString() + " 筆的 " + textBox1.Text,
                "FindString()方法",MessageBoxButtons.OK,MessageBoxIcon.Information);  
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string selectedEmployee = (string)comboBox1.SelectedItem;

            int count = 0;
            int resultIndex = -1;

            resultIndex = comboBox1.FindStringExact(selectedEmployee);

            while (resultIndex != -1)
            {
                comboBox1.Items.RemoveAt(resultIndex);
                // 如果被移除的是最後一筆，那麼在接下來的再度尋找的時
                // 因為會再度使用上次的resultIndex的值，但是那個值代表的
                // 位置已經被移除，所以，目前的最後一筆會是
                // resultIndex的值減1
                if (resultIndex == (comboBox1.Items.Count)) resultIndex--;

                count += 1;
                resultIndex = comboBox1.FindStringExact(
                    selectedEmployee,
                    resultIndex);
            }

            MessageBox.Show("共有 " + count.ToString() + " 筆的 " + 
                selectedEmployee + "被移除",
                "FindStringExact()方法", 
                MessageBoxButtons.OK,
                MessageBoxIcon.Information);
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            int selectedIndex = comboBox1.SelectedIndex;
            Object selectedItem = comboBox1.SelectedItem;

            MessageBox.Show("被選取的項目是： " + selectedItem.ToString() + "\n" +
                            "其索引值為：" + selectedIndex.ToString(),
                            "SelectedIndexChanged事件",
                MessageBoxButtons.OK,
                MessageBoxIcon.Information);
        }
    }
}
