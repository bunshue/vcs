﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
DrawListBox使用方法
方案總管/加入/現有項目, 選DrawListBox.cs, 會自動帶入DrawListBox.Designer.cs
改namespace
工具箱會出現 DrawListBox
使用方法如同ListBox, 就是多了顏色, 把GradualC改為true
*/

namespace vcs_ListBox3
{
    public partial class Form1 : Form
    {
        string[] animal_array = { "ape", "bear", "cat", "dolphin", "eagle", "fox", "giraffe" };
        List<string> animal_list;
        List<string> cookies = new List<string>() 
            { 
                "Chocolate Chip", 
                "Snickerdoodle", 
                "Peanut Butter" 
            };

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            animal_list = new List<string>(animal_array);       //string 轉 List


        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.DataSource = animal_array;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            listBox1.DataSource = animal_list;

            listBox1.DataSource = cookies;
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {
            Person[] people = 
            {
                new Person() { FirstName="Simon", LastName="Green" },
                new Person() { FirstName="Terry", LastName="Pratchett" },
                new Person() { FirstName="Eowin", LastName="Colfer" },
            };
            listBox1.DataSource = people;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            listBox1.MultiColumn = true;    //多欄
            listBox1.ColumnWidth = 60;      //欄寬
            int i;
            for (i = 0; i < 100; i++)
            {
                listBox1.Items.Add(i);
            }
        }
    }

    // A simple Person class.
    public class Person
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }

        public override string ToString()
        {
            return FirstName + " " + LastName;
        }
    }

}
