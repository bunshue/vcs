using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;


//天氣助手

/*

天氣助手
//C#調用WebService制作天氣預報


//在C#项目中如何添加“Web引用”？
https://blog.csdn.net/mengmakies/article/details/51737596


C#调用WebService制作天气预报	完整
https://www.yisu.com/zixun/105578.html



C#調用WebService制作天氣預報	有欠缺
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/190491.html

*/


namespace vcs_WebService2
{
    public partial class Form1 : Form
    {
        public string[] GetWeather(string xCity)
        {
            cn.com.webxml.www.WeatherWebService mWeatherWebService = new cn.com.webxml.www.WeatherWebService();
            string[] WeatherOfCity = mWeatherWebService.getWeatherbyCityName(xCity);
            return WeatherOfCity;
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
            //richTextBox1.Text
            Weather_Shown(sender, e);
        }

        public void Weather_Shown(object sender, EventArgs e)
        {
            try
            {
                cn.com.webxml.www.WeatherWebService mWeatherWebService = new cn.com.webxml.www.WeatherWebService();
                string[] mArea = mWeatherWebService.getSupportProvince();

                int mCount = mArea.Length - 1;

                comboBox1.Items.Clear();
                for (int mI = 0; mI <= mCount; mI++)
                {
                    comboBox1.Items.Add(mArea[mI].ToString());
                    richTextBox1.Text += mArea[mI].ToString() + "\n";

                }
                comboBox1.SelectedIndex = 0;


            }
            catch
            {

            }
        }


        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            try
            {
                cn.com.webxml.www.WeatherWebService mWeatherWebService = new cn.com.webxml.www.WeatherWebService();
                string[] mCity = mWeatherWebService.getSupportCity(comboBox1.Text);

                int mCount = mCity.Length - 1;

                comboBox2.Items.Clear();
                for (int mI = 0; mI <= mCount; mI++)
                {
                    comboBox2.Items.Add(mCity[mI].Remove(mCity[mI].IndexOf("(")));

                }
                comboBox2.SelectedIndex = 0;
            }
            catch
            {

            }


        }

        private void comboBox2_SelectedIndexChanged(object sender, EventArgs e)
        {
            try
            {
                string[] WeatherOfCity = GetWeather(comboBox2.Items[comboBox2.SelectedIndex].ToString());

                label3.Text = WeatherOfCity[0].ToString();
                label5.Text = WeatherOfCity[1].ToString();

                label6.Text = WeatherOfCity[10].ToString();

                //今天
                pictureBox1.ImageLocation = @"p_w_picpaths/weather/" + WeatherOfCity[8].ToString();
                pictureBox2.ImageLocation = @"p_w_picpaths/weather/" + WeatherOfCity[9].ToString();
                label7.Text = WeatherOfCity[6].ToString() + WeatherOfCity[5].ToString() + WeatherOfCity[7].ToString();
                label8.Text = WeatherOfCity[11].ToString();

                //明天
                pictureBox3.ImageLocation = @"p_w_picpaths/weather/" + WeatherOfCity[15].ToString();
                pictureBox4.ImageLocation = @"p_w_picpaths/weather/" + WeatherOfCity[16].ToString();
                label16.Text = WeatherOfCity[13].ToString() + WeatherOfCity[12].ToString() + WeatherOfCity[14].ToString();

                //后天
                pictureBox5.ImageLocation = @"p_w_picpaths/weather/" + WeatherOfCity[20].ToString();
                pictureBox6.ImageLocation = @"p_w_picpaths/weather/" + WeatherOfCity[21].ToString();
                label17.Text = WeatherOfCity[18].ToString() + WeatherOfCity[17].ToString() + WeatherOfCity[19].ToString();

                //城市说明及图片
                pictureBox7.ImageLocation = @"http://www.cma.gov.cn/tqyb/img/city/" + WeatherOfCity[3].ToString();
                label18.Text = WeatherOfCity[22].ToString();

                //预计时间
                label19.Text = "预报时间：" + WeatherOfCity[4].ToString();

            }
            catch
            {

            }
            

        }
    }
}
