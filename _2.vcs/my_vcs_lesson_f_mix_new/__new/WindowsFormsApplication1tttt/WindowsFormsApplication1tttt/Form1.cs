using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Xml;


//把文件轉換為XML的C#代碼
/// <summary>
/// 這個示例演示如何把Office文件編碼為xml文件以及如何把生成的xml文件轉換成Office文件
/// 把文件轉換成xml格式,然後就可以用web服務,.NET Remoting,WinSock等傳送了(其中後兩者可以不轉換也可以傳送)

/// xml解決了在多層架構中數據傳輸的問題,比如說在客戶端可以用Web服務獲取服務器端的office文件,修改後再回傳給服務器
/// 只要把文件轉換成xml格式,便有好多方案可以使用了,而xml具有平台無關性,你可以在服務端用.net用發布web服務,然後客戶端用
/// Java寫一段applit小程序來處理發送過來的文件,當然我舉的例子幾乎沒有任何顯示意義,它卻給了我們不少的啟示.
/// 另外如果你的解決方案是基於多平台的,那麼他們之間的交互最好不要用遠程應用程序接口調用(RPC),應該盡量用基於文檔的交互,
/// 比如說.net下的MSMQ,j2ee的JMQ.
///
/// 示例中設計到好多的類,我並沒有在所有的地方做過多注釋,有不明白的地方請參閱MSDN,這是偶第一個windows程序,有不對的地方
/// 歡迎各位指導
/// </summary>


namespace WindowsFormsApplication1tttt
{
    public partial class Form1 : Form
    {
        private System.Xml.XmlDocument mXmlDoc;
        private System.Xml.XmlDocument doc;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.button1.Text = "生成xml";
            this.button2.Text = "生成doc";
            this.button3.Text = "加載doc";
            this.button4.Text = "加載xml";




        }

        /// <summary>
        /// 卸載窗體時把臨時變量全部釋放
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            mXmlDoc = null;
            doc = null;
        }

        /// <summary>
        /// 把加載的Office文件轉換為xml文件
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void button1_Click(object sender, System.EventArgs e)
        {
            saveFileDialog1.Filter = "xml 文件|*.xml";//設置打開對話框的文件過濾條件
            saveFileDialog1.Title = "保存成 xml 文件";//設置打開對話框的標題
            saveFileDialog1.FileName = "";
            saveFileDialog1.ShowDialog();//打開對話框
            if (saveFileDialog1.FileName != "")//檢測用戶是否輸入了保存文件名
            {
                mXmlDoc.Save(saveFileDialog1.FileName);//用私有對象mXmlDoc保存文件,mXmlDoc在前面聲明過
                MessageBox.Show("保存成功");
            }
        }

        /// <summary>
        /// 把加載的xml文件轉換為Office文件
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void button2_Click(object sender, System.EventArgs e)
        {
            //從私有對象dox裡選取me節點,這裡的一些對xml對象的操作詳細說明可以參考msdn以獲取更多信息
            XmlNode node = doc.DocumentElement.SelectSingleNode("me");
            XmlElement ele = (XmlElement)node;//獲取一個xml元素
            string pic = ele.GetAttribute("aa");//獲取ele元素的aa屬性並報訊在一個臨時字符串變量pic
            byte[] bytes = Convert.FromBase64String(pic);//聲明一個byte[]用來存放Base64解碼轉換過來的數據流

            //從保存對話框裡獲取文件保存地址
            saveFileDialog1.Filter = "Office Documents(*.doc, *.xls, *.ppt)|*.doc;*.xls;*.ppt";
            saveFileDialog1.Title = "保存成 office 文件";
            saveFileDialog1.FileName = "";
            saveFileDialog1.ShowDialog();
            if (saveFileDialog1.FileName != "")
            {
                //創建文件流並保存
                FileStream outfile = new System.IO.FileStream(saveFileDialog1.FileName, System.IO.FileMode.CreateNew);
                outfile.Write(bytes, 0, (int)bytes.Length);
                MessageBox.Show("保存成功");
            }
        }


        /// <summary>
        /// 加載office文件並編碼序列花為一個XmlDocument變量
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void button3_Click(object sender, System.EventArgs e)
        {
            string strFileName;
            openFileDialog1.Filter = "Office Documents(*.doc, *.xls, *.ppt)|*.doc;*.xls;*.ppt";
            openFileDialog1.FilterIndex = 1;
            openFileDialog1.FileName = "";
            openFileDialog1.ShowDialog();
            strFileName = openFileDialog1.FileName;
            if (strFileName.Length != 0)
            {
                System.IO.FileStream inFile = new FileStream(strFileName, System.IO.FileMode.Open, System.IO.FileAccess.Read);
                byte[] binaryData = new byte[inFile.Length];
                inFile.Read(binaryData, 0, (int)inFile.Length);
                string mStr = Convert.ToBase64String(binaryData);
                string hh = mStr;
                mXmlDoc = new System.Xml.XmlDocument();

                mStr = string.Format("<wawa><me aa=\"{0}\"/></wawa>", mStr);
                mXmlDoc.LoadXml(mStr);
                MessageBox.Show("加載成功");
            }
        }
        /// <summary>
        /// 加載xml文件到私有對象dox
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void button4_Click(object sender, System.EventArgs e)
        {
            string strFileName;
            openFileDialog1.Filter = "xml 文件|*.xml";
            openFileDialog1.FilterIndex = 1;
            openFileDialog1.FileName = "";
            openFileDialog1.ShowDialog();
            strFileName = openFileDialog1.FileName;
            //If the user does not cancel, open the document.
            if (strFileName.Length != 0)
            {
                doc = new XmlDocument();
                doc.Load(strFileName);
                MessageBox.Show("加載成功");
            }



        }
    }
}


