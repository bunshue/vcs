using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Newtonsoft.Json;
using System.Xml;
using System.Xml.Linq;
using System.Xml.Serialization;

//  參考 https://dotblogs.com.tw/berrynote/2016/08/18/200338

/*
[.NET] [C#] [JSON.NET] Serialize序列化與Deserialize反序列

[.NET] [C#] [JSON.NET]
使用JSON.NET
SerializeObject()將物件與Dataset序列化(Serialize)為JSON
DeserializeObject()將Json反序列化(Deserialize)為物件

JSON是一種簡單輕量的資料交換格式。可用 陣列 [ ] 與 物件 { } 來寫入資料，資料的名稱與值;name / value 成對，名稱與值的中間以 : 隔開
*/

namespace vcs_JSON
{
    public partial class Form1 : Form
    {
        public class Introduction
        {
            public string Name { get; set; }         //名稱
            public int Age { get; set; }             //年紀
            public bool Marry { get; set; }          //結婚
            public List<string> Habit { get; set; }  //興趣
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
            Introduction Introduction = new Introduction
            {
                Name = "Berry",
                Age = 18,
                Marry = false,
                Habit = new List<string>
                {
                    "Sing",
                    "Dance",
                    "Code",
                    "Sleep"
                }
            };
            //轉成JSON格式
            string json = JsonConvert.SerializeObject(Introduction);
            richTextBox1.Text += "將物件序列化成JSON格式\n";
            richTextBox1.Text += json + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            DataSet dataSet = new DataSet("dataSet"); //建立DataSet
            DataTable table = new DataTable(); //建立DataTable
            DataColumn idColumn = new DataColumn("id", typeof(int)); //建立id欄
            DataColumn itemColumn = new DataColumn("item"); //建立item欄

            //DataTable加入欄位
            table.Columns.Add(idColumn);
            table.Columns.Add(itemColumn);

            //DataSet加入Table
            dataSet.Tables.Add(table);

            //跑回圈產生資料
            for (int i = 1; i < 5; i++)
            {
                DataRow newRow = table.NewRow();
                newRow["id"] = i;
                newRow["item"] = "這是第" + i + "個項目";
                table.Rows.Add(newRow);
            }

            //轉成JSON格式
            string json = JsonConvert.SerializeObject(dataSet);
            richTextBox1.Text += "將DataSet序列化成JSON格式\n";
            richTextBox1.Text += json + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //JSON字串
            string Json = "{ 'Name': 'Berry', 'Age': 18, 'Marry': false, 'Habit': [ 'Sing','Dance','Code','Sleep' ] }";

            //轉成物件
            Introduction Introduction = JsonConvert.DeserializeObject<Introduction>(Json);

            richTextBox1.Text += "反序列化成物件\n";
            richTextBox1.Text += "Name : " + Introduction.Name + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //JSON字串
            string Json = "{ 'Table1': [ { 'id': 1, 'item': '這是第1個項目' }, { 'id': 2, 'item': '這是第2個項目' }, { 'id': 3, 'item': '這是第3個項目' }, { 'id': 4, 'item': '這是第4個項目' } ] }";

            //將JSON字串轉為DataSet
            DataSet dataSet = JsonConvert.DeserializeObject<DataSet>(Json);

            //建立DataTable，並塞進dataSet的值
            DataTable dataTable = dataSet.Tables["Table1"];

            richTextBox1.Text += "反序列化成DataSet\n";
            //顯示DataTable的筆數
            richTextBox1.Text += "共" + dataTable.Rows.Count + "筆資料\n";

            //顯示DataTable的筆數
            foreach (DataRow row in dataTable.Rows)
            {
                richTextBox1.Text += row["id"] + " - " + row["item"] + "\n";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            Country china;
            try
            {
                //byte[] buffer = Properties.Resources.ChinaBoundary_Province_City;
                byte[] buffer = Properties.Resources.ChinaBoundary;
                china = ChinaMapRegion.GetChinaRegionFromJsonBinaryBytes(buffer);


                if (china != null)
                {
                    foreach (var provice in china.Province)
                    {
                        //this.comboBoxProvince.Items.Add(provice);
                        //richTextBox1.Text += provice + "\n";
                        richTextBox1.Text += provice.name + "\n";
                    }
                    //this.comboBoxProvince.DisplayMember = "name";
                    //this.comboBoxProvince.SelectedIndex = 0;
                    //this.comboBoxProvince.SelectedValueChanged += ComboBoxProvince_SelectedValueChanged;

                    richTextBox1.Text += "\n\n";
                    Province province = china.Province[9];  //江蘇省
                    if (province != null)
                    {
                        //this.comboBoxCity.Items.Clear();
                        foreach (var city in province.City)
                        {
                            richTextBox1.Text += city.name + "\n";
                        }
                        //this.comboBoxCity.DisplayMember = "name";
                        //this.comboBoxCity.SelectedIndex = 0;
                    }


                }

            }
            catch (Exception ex)
            {
                //log.Error(ex);
            }


        }
    }

    public class Piecearea
    {
        [XmlAttribute]
        public string code { set; get; }

        [XmlAttribute]
        public string name { set; get; }

        [XmlAttribute]
        public string rings { set; get; }
    }

    public class City
    {
        [XmlAttribute]
        public string code { set; get; }

        [XmlAttribute]
        public string name { set; get; }

        [XmlAttribute]
        public string rings { set; get; }

        [XmlElement]
        public List<Piecearea> Piecearea { set; get; }
    }

    public class Province
    {
        [XmlAttribute]
        public string ID { set; get; }

        [XmlAttribute]
        public string code { set; get; }

        [XmlAttribute]
        public string name { set; get; }

        [XmlAttribute]
        public string rings { set; get; }

        [XmlElement]
        public List<City> City { set; get; }
    }

    public class Country
    {
        [XmlAttribute]
        public string ID { set; get; }

        [XmlAttribute]
        public string code { set; get; }

        [XmlAttribute]
        public string name { set; get; }

        [XmlElement]
        public List<Province> Province { set; get; }
    }

    public static class ChinaMapRegion
    {
        public static Country GetChinaRegionFromJsonBinaryBytes(byte[] buffer)
        {
            Country china = JsonHelper.JsonDeserializeFromBinaryBytes<Country>(buffer);
            return china;
        }

        public static Country GetChinaRegionFromJsonFile(string filePath)
        {
            Country china = JsonHelper.JsonDeserializeFromFile<Country>(filePath, Encoding.UTF8);
            return china;
        }

        public static Country GetChinaRegionFromXmlFile(string filePath)
        {
            Country china = XmlHelper.XmlDeserializeFromFile<Country>(filePath, Encoding.UTF8);
            return china;
        }

        /*
        public static GMapPolygon GetRegionPolygon(string name, string rings)
        {
            if (string.IsNullOrEmpty(rings))
            {
                return null;
            }
            else
            {
                List<PointLatLng> pointList = new List<PointLatLng>();
                string[] pairPoints = rings.Split(',');
                foreach (var points in pairPoints)
                {
                    string[] point = points.Split(' ');
                    if (point.Length == 2)
                    {
                        PointLatLng p = new PointLatLng(double.Parse(point[1]), double.Parse(point[0]));
                        pointList.Add(p);
                    }
                }
                GMapPolygon polygon = new GMapPolygon(pointList, name);
                polygon.Fill = new SolidBrush(Color.FromArgb(0, Color.White));
                return polygon;
            }
        }
        */
    }
}

