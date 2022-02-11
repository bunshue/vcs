using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
方案總管/右鍵/加入服務參考

按 進階

按 加入Web參考

URL欄 輸入 : http://www.webxml.com.cn/WebServices/WeatherWebService.asmx
按Enter

按 加入參考

在方案總管裡面看到兩個項目: System.Web.Services 和Web References/cn.com/webxml.www


note:
這是中國提供的天氣預報的Web服務。在該站點的主頁 http://www.webxml.com.cn/zh_cn/web_services.aspx 上，
還能找到其它諸如查詢手機號碼歸屬地、航班時刻表、匯率、英漢翻譯、QQ是否在線、驗證碼圖片生成等Web服務。
另外介紹幾個國外提供的Web Service站點（沒試過，不知能不能用）：
專門關於地圖的Web服務：
http://www.opengeospatial.org/standards/wms
一個很豐富的Web服務站點：
http://www.programmableweb.com/apis/directory/1?sort=category
*/

namespace vcs_WebService
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //獲取天氣預報
            // get weather
            string city = "武汉";
            vcs_WebService.cn.com.webxml.www.WeatherWebService wws = new cn.com.webxml.www.WeatherWebService();
            string[] wwsArray = wws.getWeatherbyCityName(city);

            richTextBox1.Text = wwsArray[0] + " " + wwsArray[1] + " " + wwsArray[5] + " " + wwsArray[6] + "。" + "\n" + wwsArray[10] + "。" + "\n" + wwsArray[11] + "\n";

        }
    }
}

