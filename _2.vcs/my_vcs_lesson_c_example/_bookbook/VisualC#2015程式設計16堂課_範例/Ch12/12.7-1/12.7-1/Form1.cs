using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void startButton_Click(object sender, EventArgs e)
        {
            int num = int.Parse(numText.Text);

            listA.Items.Clear();
            listB.Items.Clear();
            listC.Items.Clear();
            moveList.Items.Clear();
            for (int i=1; i <= num; ++i){
                listA.Items.Add(i);
                listB.Items.Add("-");
                listC.Items.Add("-");
            }

            Hanoi(num, 'A', 'B', 'C');
        }

        void Hanoi(int num, char source, char tmp, char target){
            if(num > 0){
                Hanoi (num-1 ,source ,target ,tmp);
                move(source, target);
                Hanoi (num-1 ,tmp ,source ,target);
            }
        }

        ListBox trans(char c){
            if (c == 'A')
                return listA;
            else if (c == 'B')
                return listB;
            else
                return listC;
        }

        void move(char source, char target) {
            System.Threading.Thread.Sleep(500);
            moveList.Items.Add(source + "->" + target);
            moveList.Refresh();
            string srcText = " ";

            ListBox srcList = trans(source);
            for (int i = 0; i < srcList.Items.Count; ++i){
                if (srcList.Items[i].ToString() != "-"){
                    srcText = srcList.Items[i].ToString();
                    srcList.Items[i] = "-";
                    break;
                }
            }
            srcList.Refresh();

            ListBox trgList = trans(target);
            for (int i = 0; i < trgList.Items.Count; ++i){
                if (trgList.Items[i].ToString() != "-"){
                    trgList.Items[i - 1] = srcText;
                    break;
                }
                else if (i == trgList.Items.Count - 1)
                    trgList.Items[i] = srcText;
            }
            trgList.Refresh();
        }
    }
}
