using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;


using System.Runtime.Serialization;

//使用剪貼板保存自定義對象
/*
放置到剪貼板上的對象必須是可序列化的。
剪貼板接收一個實現了IDataObject接口的對象，可以用此對象“包裝”具體的數據對象。
可以多次調用IDataObject. SetData方法將多種類型的對象復制到剪貼板中。在獲取剪貼板中的數據時通過DataFormat進行識別
在進行粘貼之前，需要確保剪貼板上的數據是所需要的格式。
*/


namespace WindowsFormsApplication1ex
{
    public partial class Form1 : Form
    {
        [Serializable]
        class MyPic
        {
            public Image pic;       //圖片 
            public string picInfo;  //圖片信息說明 
        }

        //圖片 
        private Image bmp
        {
            get
            {
                return pictureBox1.Image;
            }
            set
            {
                pictureBox1.Image = value;
            }
        }
        //圖片說明 
        private string info
        {
            get
            {
                return txtImageInfo.Text;
            }
            set
            {
                txtImageInfo.Text = value;
            }
        } 
 
 

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            ChooseImageFile();
        }

        //選擇圖片
        private void ChooseImageFile()
        {
            richTextBox1.Text += "請選擇圖片\n";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                string name = openFileDialog1.FileName;
                txtImageInfo.Text = name;
                bmp = new Bitmap(name);
                richTextBox1.Text += "已選擇圖片 : " + name + "\n";
            }
        }
        //根據用戶設定的信息創建對象 
        private MyPic CreateMyPicObj()
        {
            MyPic obj = new MyPic();
            obj.pic = bmp;
            obj.picInfo = info;
            return obj;
        }

        //將對象復制到剪貼板上 
        private void CopyToClipboard()
        {
            //創建MyPic對象 
            MyPic obj = CreateMyPicObj();

            //創建一個數據對象，將MyPic類型的對象裝入 
            IDataObject dataobj = new DataObject(obj);

            //其它類型的數據也可以裝入到數據對象中 
            dataobj.SetData(DataFormats.UnicodeText, info);
            dataobj.SetData(DataFormats.Bitmap, bmp);

            //復制到剪貼板上，第二個參數表明程序退出時不清空剪貼板 
            Clipboard.SetDataObject(dataobj, true);
        }
       

        private void button2_Click(object sender, EventArgs e)
        {
            CopyToClipboard();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            PasteFromClipboard();
        }

        //從剪貼板獲取數據 
        private void PasteFromClipboard()
        {
            //剪貼板上有我需要的數據嗎？格式為“項目名稱.數據格式名” 
            if (Clipboard.ContainsData("UseClipboard.MyPic") == false)//根據指定的DataFormat獲取數據對象 
                return;
            //讀取數據 
            IDataObject clipobj = Clipboard.GetDataObject();
            //將數據轉換為需要的類型 
            MyPic mypicobj = clipobj.GetData("UseClipboard.MyPic") as MyPic;
            //從數據對象中分解出需要的數據 
            info = mypicobj.picInfo;
            pictureBox1.Image = mypicobj.pic;

            if (Clipboard.ContainsData(DataFormats.UnicodeText) == false)//根據指定的DataFormat獲取數據對象 
                return;
            string str = clipobj.GetData(DataFormats.UnicodeText) as string;
            MessageBox.Show(str);
        } 


        private void button4_Click(object sender, EventArgs e)
        {
            Close();
        }
    }
}
