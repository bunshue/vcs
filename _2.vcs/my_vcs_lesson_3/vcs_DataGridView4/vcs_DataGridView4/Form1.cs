using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DataGridView4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Load_DataGridView_Data1();
            //Load_DataGridView_Data2();
        }

        void Load_DataGridView_Data1()
        {
            // Make some data items.
            dataGridView1.Rows.Add(new object[] { "Pencils, dozen", 1.24m, 4 });
            dataGridView1.Rows.Add(new object[] { "Paper, ream", 3.75m, 3 });
            dataGridView1.Rows.Add(new object[] { "Cookies, box", 2.17m, 12 });
            dataGridView1.Rows.Add(new object[] { "Notebook", 1.95m, 2 });
            dataGridView1.Rows.Add(new object[] { "Pencil sharpener", 12.95m, 1 });
            dataGridView1.Rows.Add(new object[] { "Paper clips, 100", 0.75m, 1 });

            // Define a column style at run time.
            DataGridViewCellStyle cell_style = new DataGridViewCellStyle();
            cell_style.BackColor = Color.LightGreen;
            cell_style.Alignment = DataGridViewContentAlignment.MiddleRight;
            cell_style.Format = "C2";
            dataGridView1.Columns[3].DefaultCellStyle = cell_style;

            // Calculate totals.
            CalculateTotals();
        }

        // Calculate the total costs and highlight totals greater than $9.99.
        private void CalculateTotals()
        {
            // Make a style for values greater than $9.99.
            DataGridViewCellStyle highlight_style = new DataGridViewCellStyle();
            highlight_style.ForeColor = Color.Red;
            highlight_style.BackColor = Color.Yellow;
            highlight_style.Font = new Font(dataGridView1.Font, FontStyle.Bold);

            // Calculate the total costs.
            foreach (DataGridViewRow row in dataGridView1.Rows)
            {
                // Calculate total cost.
                decimal total_cost =
                    (decimal)row.Cells["PriceEach"].Value *
                    (int)row.Cells["Quantity"].Value;

                // Display the value.
                row.Cells["Total"].Value = total_cost;

                // Highlight the cell if the vcalue is big.
                if (total_cost > 9.99m) row.Cells["Total"].Style = highlight_style;
            }
        }

        void Load_DataGridView_Data2()
        {
            // Make some data items.
            OrderItem[] order_items = 
            {
                new OrderItem("Pencils, dozen", 1.24m, 4),
                new OrderItem("Cookies, box", 2.17m, 1),
                new OrderItem("Notebook", 1.95m, 2),
                new OrderItem("Paper, ream", 3.75m, 3),
                new OrderItem("Pencil sharpener", 12.95m, 1),
                new OrderItem("Paper clips, 100", 0.75m, 1),
            };

            // Add the items to the DataGridView.
            AddOrderItems(order_items);

            // Define a column style at run time.
            DataGridViewCellStyle cell_style = new DataGridViewCellStyle();
            cell_style.BackColor = Color.LightGreen;
            cell_style.Alignment = DataGridViewContentAlignment.MiddleRight;
            cell_style.Format = "C2";
            dataGridView1.Columns[3].DefaultCellStyle = cell_style;
        }

        // Add the items to the DataGridView.
        private void AddOrderItems(OrderItem[] order_items)
        {
            foreach (OrderItem item in order_items)
            {
                dataGridView1.Rows.Add(new object[]
                    {
                        item.Description,
                        item.UnitPrice,
                        item.Quantity,
                        item.TotalCost
                    }
                );
            }
        }
    }

    public class OrderItem
    {
        public string Description;
        public int Quantity;
        public decimal UnitPrice, TotalCost;
        public OrderItem(string new_description, decimal new_unitprice, int new_quantity)
        {
            Description = new_description;
            UnitPrice = new_unitprice;
            Quantity = new_quantity;

            // Calculate total.
            TotalCost = UnitPrice * Quantity;
        }
    }

}
