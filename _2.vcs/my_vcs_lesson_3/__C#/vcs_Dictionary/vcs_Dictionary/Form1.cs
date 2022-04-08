using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Dictionary
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 180;
            dy = 80;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);


            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Dictionary字典用法1\n";
            //Dictionary的用法
            Dictionary<string, string> AnimalData = new Dictionary<string, string>() {
            { "mouse", "Mickey" },
            { "bull", "Benny" },
            { "tiger", "Eric" },
            { "rabbit", "Cony" }
            };
            string animal_type;
            string animal_name;

            animal_type = "mouse";
            if (AnimalData.ContainsKey(animal_type))
            {
                animal_name = AnimalData[animal_type];
                richTextBox1.Text += "got animal name = " + animal_name + "\n";
            }
            else
                richTextBox1.Text += "no matched animal name\n";

            animal_type = "bull";
            if (AnimalData.ContainsKey(animal_type))
            {
                animal_name = AnimalData[animal_type];
                richTextBox1.Text += "got animal name = " + animal_name + "\n";
            }
            else
                richTextBox1.Text += "no matched animal name\n";

            animal_type = "tiger";
            if (AnimalData.ContainsKey(animal_type))
            {
                animal_name = AnimalData[animal_type];
                richTextBox1.Text += "got animal name = " + animal_name + "\n";
            }
            else
                richTextBox1.Text += "no matched animal name\n";

            animal_type = "rabbit";
            if (AnimalData.ContainsKey(animal_type))
            {
                animal_name = AnimalData[animal_type];
                richTextBox1.Text += "got animal name = " + animal_name + "\n";
            }
            else
                richTextBox1.Text += "no matched animal name\n";

            animal_type = "dragon";
            if (AnimalData.ContainsKey(animal_type))
            {
                animal_name = AnimalData[animal_type];
                richTextBox1.Text += "got animal name = " + animal_name + "\n";
            }
            else
                richTextBox1.Text += "no matched animal name\n";

        }

        // The dictionary of digit names.
        private Dictionary<int, string> Numbers = new Dictionary<int, string>()
        {
            {0, "Zero"},
            {1, "One"},
            {2, "Two"},
            {3, "Three"},
            {4, "Four"},
            {5, "Five"},
            {6, "Six"},
            {7, "Seven"},
            {8, "Eight"},
            {9, "Nine"}
        };

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Dictionary字典用法2\n";
            // Display values from the dictionary.
            for (int i = 0; i < 10; i++)
            {
                richTextBox1.Text += i.ToString() + '\t' + Numbers[i] + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Dictionary<string, long> population_dict = new Dictionary<string, long>();

            // Population data from https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population.
            population_dict.Add("AK", 731545);
            population_dict.Add("AL", 4903185);
            population_dict.Add("AR", 3017825);
            population_dict.Add("AS", 55641);
            population_dict.Add("AZ", 7278717);
            population_dict.Add("CA", 39512223);
            population_dict.Add("CO", 5758736);
            population_dict.Add("CT", 3565287);
            population_dict.Add("DC", 705749);
            population_dict.Add("DE", 973764);
            population_dict.Add("FL", 21477737);
            population_dict.Add("GA", 10617423);
            population_dict.Add("GU", 165718);
            population_dict.Add("HI", 1415872);
            population_dict.Add("IA", 3155070);
            population_dict.Add("ID", 1787065);
            population_dict.Add("IL", 12671821);
            population_dict.Add("IN", 6732219);
            population_dict.Add("KS", 2913314);
            population_dict.Add("KY", 4467673);
            population_dict.Add("LA", 4648794);
            population_dict.Add("MA", 6949503);
            population_dict.Add("MD", 6045680);
            population_dict.Add("ME", 1344212);
            population_dict.Add("MI", 9986857);
            population_dict.Add("MN", 5639632);
            population_dict.Add("MO", 6137428);
            population_dict.Add("MP", 55194);
            population_dict.Add("MS", 2976149);
            population_dict.Add("MT", 1068778);
            population_dict.Add("NC", 10488084);
            population_dict.Add("ND", 762062);
            population_dict.Add("NE", 1934408);
            population_dict.Add("NH", 1359711);
            population_dict.Add("NJ", 8882190);
            population_dict.Add("NM", 2096829);
            population_dict.Add("NV", 3080156);
            population_dict.Add("NY", 19453561);
            population_dict.Add("OH", 11689100);
            population_dict.Add("OK", 3956971);
            population_dict.Add("OR", 4217737);
            population_dict.Add("PA", 12801989);
            population_dict.Add("PR", 3193694);
            population_dict.Add("RI", 1059361);
            population_dict.Add("SC", 5148714);
            population_dict.Add("SD", 884659);
            population_dict.Add("TN", 6833174);
            population_dict.Add("TX", 28995881);
            population_dict.Add("UT", 3205958);
            population_dict.Add("VA", 8535519);
            population_dict.Add("VI", 104914);
            population_dict.Add("VT", 623989);
            population_dict.Add("WA", 7614893);
            population_dict.Add("WI", 5822434);
            population_dict.Add("WV", 1792147);
            population_dict.Add("WY", 578759);

            // Get the state population.
            long all_pop = 0;
            foreach (int value in population_dict.Values)
            {
                all_pop += value;
            }
            population_dict.Add("ALL STATES", all_pop);

            richTextBox1.Text += "顯示此Dictionary的資料\n";
            richTextBox1.Text += "共有 " + population_dict.Count.ToString() + " 筆資料\n";
            foreach (string n in population_dict.Keys)
            {
                long p;
                richTextBox1.Text += "找到 州 " + n + "\t";
                if (population_dict.ContainsKey(n))
                    p = population_dict[n];
                else
                    p = 0;
                richTextBox1.Text += "人口 : " + p.ToString() + "\n";
            }

            string state_name;
            long population;

            state_name = "NY";
            if (population_dict.ContainsKey(state_name))
                population = population_dict[state_name];
            else
                population = 0;
            richTextBox1.Text += "州 : " + state_name + "\t人口 : " + population.ToString() + "\n";

            state_name = "CA";
            if (population_dict.ContainsKey(state_name))
                population = population_dict[state_name];
            else
                population = 0;
            richTextBox1.Text += "州 : " + state_name + "\t人口 : " + population.ToString() + "\n";

            state_name = "ALL STATES";
            if (population_dict.ContainsKey(state_name))
                population = population_dict[state_name];
            else
                population = 0;
            richTextBox1.Text += "全國 :\t人口 : " + population.ToString() + "\n";

        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Dictionary字典用法4 用Class\n";

            // Make a dictionary.
            DictionaryWithDefault<string, string> dict = new DictionaryWithDefault<string, string>("<Missing>");

            // Add some items to the dictionary.
            dict["Ann"] = "Archer";
            dict["Chuck"] = "Cider";
            dict["Dora"] = "Deevers";

            // Display some values.
            richTextBox1.Text += "Ann" + "\t" + dict["Ann"] + "\n";
            richTextBox1.Text += "Ben" + "\t" + dict["Ben"] + "\n";
            richTextBox1.Text += "Chuck" + "\t" + dict["Chuck"] + "\n";
            richTextBox1.Text += "Dora" + "\t" + dict["Dora"] + "\n";
            richTextBox1.Text += "Ed" + "\t" + dict["Ed"] + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

    }
    class DictionaryWithDefault<TKey, TValue>
    {
        // Store items here.
        private Dictionary<TKey, TValue> Entries
            = new Dictionary<TKey, TValue>();

        // The default value.
        private TValue DefaultValue;

        // Constructor.
        public DictionaryWithDefault(TValue default_value)
        {
            DefaultValue = default_value;
        }

        // Make the indexer property.
        public TValue this[TKey key]
        {
            get
            {
                // Return the value for this key or the default value.
                if (Entries.ContainsKey(key)) return Entries[key];
                return DefaultValue;
            }
            set
            {
                // Set the property's value for the key.
                Entries.Add(key, value);
            }
        }
    }
}
