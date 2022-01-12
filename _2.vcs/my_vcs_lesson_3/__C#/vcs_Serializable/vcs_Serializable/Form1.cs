using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Runtime.Serialization; //for IFormatter
using System.Runtime.Serialization.Formatters.Binary;   //for BinaryFormatter

using System.Collections;

namespace vcs_Serializable
{
    public partial class Form1 : Form
    {
        [Serializable]
        public class ScoreObject
        {
            public String Name = null;
            public int Score_Chinese = 0;
            public int Score_English = 0;
            public int Score_Math = 0;
            public double Score_Average = 0;
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
            //將類別的執行個體序列化成檔案

            ScoreObject obj = new ScoreObject();
            obj.Name = "David Wang";
            obj.Score_Chinese = 95;
            obj.Score_English = 94;
            obj.Score_Math = 100;
            obj.Score_Average = (double)(obj.Score_Chinese + obj.Score_English + obj.Score_Math) / 3;
            IFormatter formatter = new BinaryFormatter();
            Stream stream = new FileStream("score.bin", FileMode.Create, FileAccess.Write, FileShare.None);
            formatter.Serialize(stream, obj);
            stream.Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //將物件還原成其先前的狀態
            //建立供讀取的資料流和 Formatter，然後指示格式子對物件還原序列化
            IFormatter formatter = new BinaryFormatter();
            Stream stream = new FileStream("score.bin", FileMode.Open, FileAccess.Read, FileShare.Read);
            ScoreObject obj = (ScoreObject)formatter.Deserialize(stream);
            stream.Close();

            richTextBox1.Text += "姓名 :\t" + obj.Name.ToString() + "\n";
            richTextBox1.Text += "國文 :\t" + obj.Score_Chinese.ToString() + "\n";
            richTextBox1.Text += "英文 :\t" + obj.Score_English.ToString() + "\n";
            richTextBox1.Text += "數學 :\t" + obj.Score_Math.ToString() + "\n";
            richTextBox1.Text += "平均 :\t" + obj.Score_Average.ToString() + "\n";

        }

        private void button3_Click(object sender, EventArgs e)
        {
            Serialize();

        }

        private void button4_Click(object sender, EventArgs e)
        {
            Deserialize();
        }

        static void Serialize()
        {
            // Create a hashtable of values that will eventually be serialized.
            Hashtable addresses = new Hashtable();
            addresses.Add("Jeff", "123 Main Street, Redmond, WA 98052");
            addresses.Add("Fred", "987 Pine Road, Phila., PA 19116");
            addresses.Add("Mary", "PO Box 112233, Palo Alto, CA 94301");

            // To serialize the hashtable and its key/value pairs,
            // you must first open a stream for writing.
            // In this case, use a file stream.
            FileStream fs = new FileStream("serialize_data.dat", FileMode.Create);

            // Construct a BinaryFormatter and use it to serialize the data to the stream.
            BinaryFormatter formatter = new BinaryFormatter();
            try
            {
                formatter.Serialize(fs, addresses);
            }
            catch (SerializationException e)
            {
                Console.WriteLine("Failed to serialize. Reason: " + e.Message);
                throw;
            }
            finally
            {
                fs.Close();
            }
        }

        static void Deserialize()
        {
            // Declare the hashtable reference.
            Hashtable addresses = null;

            // Open the file containing the data that you want to deserialize.
            FileStream fs = new FileStream("serialize_data.dat", FileMode.Open);
            try
            {
                BinaryFormatter formatter = new BinaryFormatter();

                // Deserialize the hashtable from the file and
                // assign the reference to the local variable.
                addresses = (Hashtable)formatter.Deserialize(fs);
            }
            catch (SerializationException e)
            {
                Console.WriteLine("Failed to deserialize. Reason: " + e.Message);
                throw;
            }
            finally
            {
                fs.Close();
            }

            // To prove that the table deserialized correctly,
            // display the key/value pairs.
            foreach (DictionaryEntry de in addresses)
            {
                Console.WriteLine("{0} lives at {1}.", de.Key, de.Value);
            }
        }

    }
}

