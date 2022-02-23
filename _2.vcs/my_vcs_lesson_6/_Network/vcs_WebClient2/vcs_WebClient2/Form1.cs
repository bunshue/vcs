using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;   //for WebClient

//http://vip.astro.sina.com.cn/astro/view/libra


namespace vcs_WebClient2
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
            var fate = StarSignsUtil.GetFateToday("天秤座");
            richTextBox1.Text += fate.StarSign.Title + "\n";
            richTextBox1.Text += fate.StarSign.Id + "\n";
            richTextBox1.Text += fate.StarSign.DateRange + "\n";

            richTextBox1.Text += fate.Date + "\n";

            richTextBox1.Text += fate.Desc + "\n";

            richTextBox1.Text += "顯示此Dictionary的資料\n";
            richTextBox1.Text += "共有 " + fate.Datas.Count.ToString() + " 筆資料\n";

            foreach (string n in fate.Datas.Keys)
            {
                richTextBox1.Text += "Keys = " + n + "\tValues = " + fate.Datas[n] + "\n";
            }
        }
    }

    public static class StarSignsUtil
    {
        /// <summary>
        /// 紀錄星座資料的模型
        /// </summary>
        public class StarSignInfo
        {
            public string Title { get; set; }
            public string Id { get; set; }
            public string DateRange { get; set; }
        }


        /// <summary>
        /// 查詢後的回應資料
        /// </summary>
        public class FateResult
        {
            public StarSignInfo StarSign { get; set; }
            public string Date { get; set; }


            public string Desc { get; set; }


            public System.Collections.Generic.Dictionary<string, string> Datas { get; set; }

            public FateResult()
            {
                Datas = new System.Collections.Generic.Dictionary<string, string>();
            }

        }

        /// <summary>
        /// 星座資料
        /// </summary>
        public static System.Collections.Generic.List<StarSignInfo> Datas { get; set; }


        //Ctor
        static StarSignsUtil()
        {
            Datas = new System.Collections.Generic.List<StarSignInfo>();
            Datas.Add(new StarSignInfo { Title = "白羊座", Id = "aries", DateRange = "03/21-04/19" });
            Datas.Add(new StarSignInfo { Title = "金牛座", Id = "taurus", DateRange = "04/20-05/20" });
            Datas.Add(new StarSignInfo { Title = "雙子座", Id = "gemini", DateRange = "05/21-06/21" });
            Datas.Add(new StarSignInfo { Title = "巨蟹座", Id = "cancer", DateRange = "06/22-07/22" });
            Datas.Add(new StarSignInfo { Title = "獅子座", Id = "leo", DateRange = "07/23-08/22" });
            Datas.Add(new StarSignInfo { Title = "處女座", Id = "virgo", DateRange = "08/23-09/22" });
            Datas.Add(new StarSignInfo { Title = "天秤座", Id = "libra", DateRange = "09/23-10/23" });
            Datas.Add(new StarSignInfo { Title = "天蠍座", Id = "scorpio", DateRange = "10/24-11/22" });
            Datas.Add(new StarSignInfo { Title = "射手座", Id = "sagittarius", DateRange = "11/23-12/21" });
            Datas.Add(new StarSignInfo { Title = "魔羯座", Id = "capricorn", DateRange = "12/22-01/19" });
            Datas.Add(new StarSignInfo { Title = "水瓶座", Id = "aquarius", DateRange = "01/20-02/18" });
            Datas.Add(new StarSignInfo { Title = "雙魚座", Id = "pisces", DateRange = "02/19-03/20" });
        }


        public static FateResult GetFateToday(string title)
        {
            var sInfo = Datas.SingleOrDefault(x => x.Title == title);
            if (sInfo == null)
            {
                throw new System.Exception("此星座我沒有找到");
            }


            var result = new StarSignsUtil.FateResult();
            result.StarSign = sInfo;

            string url = @"http://vip.astro.sina.com.cn/astro/view/" + sInfo.Id + "/";

            WebClient wc = new WebClient();     // 建立 WebClient
            wc.Encoding = Encoding.UTF8;        // 指定 WebClient 的編碼
            string source = wc.DownloadString(url);
            //MessageBox.Show(sInfo.Id);

            var regex = new System.Text.RegularExpressions.Regex(@"<div class=[\s""']tab[\s""']><h4>(?<KEY>.*?)</h4><p>(?<VALUE>.*?)</p>", System.Text.RegularExpressions.RegexOptions.IgnoreCase);
            System.Text.RegularExpressions.MatchCollection matches = regex.Matches(source);
            foreach (System.Text.RegularExpressions.Match match in matches)
            {
                if (match.Success)
                {
                    var k = match.Groups["KEY"].Value.Replace("&nbsp;", "");
                    var v = match.Groups["VALUE"].Value.Replace("&nbsp;", "");
                    if (!string.IsNullOrEmpty(k) && !string.IsNullOrEmpty(v) && !result.Datas.ContainsKey(k))
                    {
                        result.Datas.Add(k, v);
                    }
                    //MessageBox.Show(k);
                    //MessageBox.Show(v);
                }
            }

            regex = new System.Text.RegularExpressions.Regex(@"&lt;p&gt;(?<VALUE>.*?)&lt;/p&gt", System.Text.RegularExpressions.RegexOptions.IgnoreCase | System.Text.RegularExpressions.RegexOptions.Singleline);
            matches = regex.Matches(source);

            foreach (System.Text.RegularExpressions.Match match in matches)
            {
                if (match.Success)
                {

                    var v = match.Groups["VALUE"].Value.Trim();

                    if (!string.IsNullOrEmpty(v))
                    {
                        if (v.Contains("："))
                        {
                            result.Datas.Add(v.Split('：')[0].Trim(), v.Split('：')[1].Trim());
                        }
                        else
                        {
                            result.Desc = v.Trim();
                        }
                    }
                }
            }

            regex = new System.Text.RegularExpressions.Regex(@"有效日期:(?<VALUE>.*?)</li>", System.Text.RegularExpressions.RegexOptions.IgnoreCase | System.Text.RegularExpressions.RegexOptions.Singleline);
            matches = regex.Matches(source);
            foreach (System.Text.RegularExpressions.Match match in matches)
            {
                if (match.Success)
                {

                    result.Date = match.Groups["VALUE"].Value.Trim();
                }
            }
            return result;
        }
    }
}


