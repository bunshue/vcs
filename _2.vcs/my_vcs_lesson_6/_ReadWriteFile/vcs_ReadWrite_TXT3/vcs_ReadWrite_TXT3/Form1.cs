﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Microsoft.VisualBasic.FileIO;
using System.IO;

namespace vcs_ReadWrite_TXT3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            txtResult.Text = File.ReadAllText("../../test.txt");
            DataGridView1.ColumnHeadersVisible = true;
            // 設定欄標題樣式。
            DataGridViewCellStyle columnHeaderStyle = new DataGridViewCellStyle();
            columnHeaderStyle.BackColor = Color.Beige;
            columnHeaderStyle.Font = new Font("Verdana", 9, FontStyle.Bold);
            DataGridView1.ColumnHeadersDefaultCellStyle = columnHeaderStyle;
            // 設定 DataGridView 控件的字段數目。
            DataGridView1.ColumnCount = 3;
            // 設定各欄的標題名稱。
            DataGridView1.Columns[0].Name = "類別編號";
            DataGridView1.Columns[1].Name = "類別名稱";
            DataGridView1.Columns[2].Name = "說明";
            DataGridView1.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.AllCells;
            DataGridView2.ColumnHeadersVisible = true;
            DataGridView2.ColumnHeadersDefaultCellStyle = columnHeaderStyle;
            // 設定 DataGridView 控件的字段數目。
            DataGridView2.ColumnCount = 4;
            // 設定各欄的標題名稱。
            DataGridView2.Columns[0].Name = "產品編號";
            DataGridView2.Columns[1].Name = "產品名稱";
            DataGridView2.Columns[2].Name = "單位數量";
            DataGridView2.Columns[3].Name = "單價";
            DataGridView2.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.AllCells;
            DataGridView3.ColumnHeadersVisible = true;
            DataGridView3.ColumnHeadersDefaultCellStyle = columnHeaderStyle;
            // 設定 DataGridView 控件的字段數目。
            DataGridView3.ColumnCount = 3;
            // 設定各欄的標題名稱。
            DataGridView3.Columns[0].Name = "貨運公司編號";
            DataGridView3.Columns[1].Name = "貨運公司名稱";
            DataGridView3.Columns[2].Name = "電話";
            DataGridView3.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.AllCells;
        }

        private void btnParseTextFiles_Click(object sender, EventArgs e)
        {
            using (TextFieldParser myReader = new TextFieldParser("../../test.txt"))
            {
                // 定義三種格式之各欄的寬度與分隔字符。
                int[] FirstFormat = { 5, 10, -1 };
                int[] SecondFormat = { 6, 10, 17, -1 };
                string[] ThirdFormat = { "," };
                this.DataGridView1.Rows.Clear();
                this.DataGridView2.Rows.Clear();
                this.DataGridView3.Rows.Clear();
                string[] CurrentRow;
                while (!myReader.EndOfData)
                {
                    try
                    {
                        string RowType = myReader.PeekChars(2);
                        switch (RowType)
                        {
                            case "CK":
                                myReader.TextFieldType = FieldType.FixedWidth;
                                myReader.FieldWidths = FirstFormat; // 或是 myReader.SetFieldWidths(FirstFormat);
                                CurrentRow = myReader.ReadFields();
                                this.DataGridView1.Rows.Add(CurrentRow);
                                break;
                            case "PB":
                                myReader.TextFieldType = FieldType.FixedWidth;
                                myReader.FieldWidths = SecondFormat; // 或是 myReader.SetFieldWidths(SecondFormat);
                                CurrentRow = myReader.ReadFields();
                                this.DataGridView2.Rows.Add(CurrentRow);
                                break;
                            case "SP":
                                myReader.TextFieldType = FieldType.Delimited;
                                myReader.Delimiters = ThirdFormat; // 或是 myReader.SetDelimiters(ThirdFormat);
                                CurrentRow = myReader.ReadFields();
                                this.DataGridView3.Rows.Add(CurrentRow);
                                break;
                        }
                    }
                    catch (MalformedLineException ex)
                    {
                        MessageBox.Show("行 " + ex.Message + " 是無效的。略過。");
                    }
                }
                // 排序各個 DataGridView 控件的內容。
                DataGridView1.Sort(DataGridView1.Columns[0], System.ComponentModel.ListSortDirection.Ascending);
                DataGridView2.Sort(DataGridView2.Columns[0], System.ComponentModel.ListSortDirection.Ascending);
                DataGridView3.Sort(DataGridView3.Columns[0], System.ComponentModel.ListSortDirection.Ascending);
            }
        }
    }
}
