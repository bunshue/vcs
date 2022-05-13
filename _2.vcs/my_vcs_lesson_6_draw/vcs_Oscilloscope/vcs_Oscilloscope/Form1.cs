using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_Oscilloscope
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

        private void btnLoad_Click(object sender, EventArgs e)
        {
            string filename = @"..\..\data\MappingData1.txt";

            string data;
            string[] splitData;
            using (TextReader reader = File.OpenText(filename))
            {
                data = reader.ReadToEnd();
                splitData = data.Split(new char[] { '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries);
            }
            List<int> mapData = new List<int>();
            foreach (string info in splitData)
            {
                try
                {
                    int xxx = Convert.ToInt32(info);
                    if (xxx > 0)
                    {
                        mapData.Add(xxx);
                    }
                }
                catch (System.Exception ex)
                {
                }
            }
            ucOscilloscope1.MappingDatas = mapData;
            //Console.WriteLine("Read end");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"..\..\data\MappingData2.txt";

            string data;
            string[] splitData;
            using (TextReader reader = File.OpenText(filename))
            {
                data = reader.ReadToEnd();
                splitData = data.Split(new char[] { '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries);
            }
            List<int> mapData = new List<int>();
            foreach (string info in splitData)
            {
                try
                {
                    int xxx = Convert.ToInt32(info);
                    if (xxx > 0)
                    {
                        mapData.Add(xxx);
                    }
                }
                catch (System.Exception ex)
                {
                }
            }
            ucOscilloscope1.MappingDatas = mapData;
        }
    }
}
