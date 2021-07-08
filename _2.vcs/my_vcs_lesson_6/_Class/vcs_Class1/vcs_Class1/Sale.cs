using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_Class1
{
    class Sale
    {
        public Sale()
        {
        }

        public Sale(string productName, DateTime saleDate, double salePrice)
        {
            this.ProductName = productName;
            this.SaleDate = saleDate;
            this.SalePrice = salePrice;
        }
        public string ProductName { get; set; } //貨品名稱
        public DateTime SaleDate { get; set; }  //銷售日期
        public double SalePrice { get; set; }   //銷售價格
    }
}
