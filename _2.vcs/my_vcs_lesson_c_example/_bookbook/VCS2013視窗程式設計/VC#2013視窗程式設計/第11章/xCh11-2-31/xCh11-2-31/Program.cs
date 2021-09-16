using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace xCh11_2_31
{
    class Product
    {
        public string Name { get; set; }
        public int CategoryID { get; set; }
    }

    class Category
    {
        public string Name { get; set; }
        public int ID { get; set; }
    }

    class joinDemonstration
    {
        // 建構第一組資料來源
        List<Category> categories = new List<Category>()
            { 
                new Category()  {Name="飲料",   ID=001},
                new Category()  {Name="佐料",   ID=002},
                new Category()  {Name="蔬菜",   ID=003},
                new Category()  {Name="穀類",   ID=004},
                new Category()  {Name="水果",   ID=005}            
            };

        // 建構第二組資料來源
        List<Product> products = new List<Product>()
            {
                new Product {Name="可樂",   CategoryID=001},
                new Product {Name="茶品",   CategoryID=001},
                new Product {Name="芥末",   CategoryID=002},
                new Product {Name="泡菜",   CategoryID=002},
                new Product {Name="蘿蔔",   CategoryID=003},
                new Product {Name="白菜",   CategoryID=003},
                new Product {Name="桃子",   CategoryID=005},
                new Product {Name="甜瓜",   CategoryID=005},
            };

        public void InnerJoin()
        {
            var innerJoinQuery =
               from category in categories
               join prod in products on category.ID equals prod.CategoryID
               select new { Category = category.ID, Product = prod.Name };

            Console.Write("*** 內部聯結：");
            Console.WriteLine(
                "查詢運算結果->{0} 項目位於1個群組中。", innerJoinQuery.Count());
            Console.WriteLine("{0,-8}{1}", "品名", "種類");

            foreach (var item in innerJoinQuery)
            {
                Console.WriteLine("{0,-10}{1}", item.Product, item.Category);
            }
        }

        public void GroupJoin1()
        {
            var groupJoinQuery =
               from category in categories
               join prod in products on category.ID equals prod.CategoryID into prodGroup
               select prodGroup;

            int totalItems = 0;
            Console.WriteLine("*** 群組聯結：");
            Console.WriteLine("   {0,-8}{1}", "品名", "種類");

            foreach (var prodGrouping in groupJoinQuery)
            {
                Console.WriteLine("群組：");
                foreach (var item in prodGrouping)
                {
                    totalItems++;
                    Console.WriteLine("   {0,-10}{1}", item.Name, item.CategoryID);
                }
            }

            Console.WriteLine(
                "查詢運算結果->Unshaped GroupJoin: {0} 項目位於 {1} 個未具名的群組中",
                    totalItems, groupJoinQuery.Count());
        }

        public void GroupJoin2()
        {
            var groupJoinQuery =
                from category in categories
                join product in products on category.ID equals product.CategoryID into prodGroup
                from prod in prodGroup
                orderby prod.CategoryID
                select new { Category = prod.CategoryID, ProductName = prod.Name };

            int totalItems = 0;
            Console.WriteLine("*** 群組聯結：");
            Console.WriteLine("   {0,-8}{1}", "品名", "種類");

            foreach (var item in groupJoinQuery)
            {
                totalItems++;
                Console.WriteLine("   {0,-10}{1}", item.ProductName, item.Category);
            }

            Console.WriteLine("查詢運算結果-> {0} 項目位於1個群組中",
                totalItems, groupJoinQuery.Count());
        }

        public void GroupInnerJoin()
        {
            var groupJoinQuery =
                from category in categories
                orderby category.ID
                join prod in products on category.ID equals prod.CategoryID into prodGroup
                select new
                {
                    Category = category.Name,
                    Products = from prod2 in prodGroup
                               orderby prod2.Name
                               select prod2
                };

            int totalItems = 0;
            Console.WriteLine("*** 群組/內部聯結：");
            Console.WriteLine("  {0,-8}{1}", "品名", "種類");

            foreach (var productGroup in groupJoinQuery)
            {
                Console.WriteLine(productGroup.Category);
                foreach (var prodItem in productGroup.Products)
                {
                    totalItems++;
                    Console.WriteLine("  {0,-10} {1}", prodItem.Name, prodItem.CategoryID);
                }
            }

            Console.WriteLine("查詢運算結果-> {0} 項目位於 {1} 個具名的群組中",
                totalItems, groupJoinQuery.Count());
        }

        public void LeftOuterJoin1()
        {
            var leftOuterQuery =
               from category in categories
               join prod in products on category.ID equals prod.CategoryID into prodGroup
               select prodGroup.DefaultIfEmpty(
                    new Product() { Name = "左側來源無相符項目 !", CategoryID = category.ID });

            int totalItems = 0;
            Console.WriteLine("左外部聯結：");

            foreach (var prodGrouping in leftOuterQuery)
            {
                Console.WriteLine("群組：", prodGrouping.Count());
                Console.WriteLine("  {0,-8}{1}", "品名", "種類");

                foreach (var item in prodGrouping)
                {
                    totalItems++;

                    Console.WriteLine("  {0,-10}{1}", item.Name, item.CategoryID);
                }
            }

            Console.WriteLine("查詢運算結果-> {0} 項目位於 in {1} 個群組中",
                totalItems, leftOuterQuery.Count());
        }

        public void LeftOuterJoin2()
        {
            var leftOuterQuery =
               from category in categories
               join prod in products on category.ID equals prod.CategoryID into prodGroup
               from item in prodGroup.DefaultIfEmpty()
               select new { 
                   Name = item == null ? 
                   "左側來源無相符項目 !" : 
                   item.Name, CategoryID = category.ID };

            int totalItems = 0;
            Console.WriteLine("左外部聯結：");
            Console.WriteLine("{0,-23}{1}", "品名", "種類");

            foreach (var item in leftOuterQuery)
            {
                totalItems++;
                Console.WriteLine("{0,-23}{1}", item.Name, item.CategoryID);
            }

            Console.WriteLine("查詢運算結果-> {0} 項目位於1個群組中", totalItems);
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            joinDemonstration app = new joinDemonstration();
            //app.InnerJoin();                // 內部等聯結
            //app.GroupJoin1();
            //app.GroupJoin2();
            app.GroupInnerJoin();

            //app.LeftOuterJoin1();
            //app.LeftOuterJoin2();
        }
    }
}
