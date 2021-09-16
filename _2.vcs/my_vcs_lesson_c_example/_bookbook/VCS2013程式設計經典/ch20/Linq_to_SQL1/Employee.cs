using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


using System.Data.Linq.Mapping;	//含入System.Data.Linq.Mapping


namespace Linq_to_SQL1
{
    [Table(Name = "員工")]   	// Employee類別對應員工資料表
    class Employee
    {
        [Column]  		// 編號屬性對應至員工資料表的編號欄位
        public int 編號 { get; set; }
        [Column]  		// 姓名屬性對應至員工資料表的姓名欄位
        public string 姓名 { get; set; }
        [Column]  		// 職稱屬性對應至員工資料表的職稱欄位
        public string 職稱 { get; set; }
        [Column]  		// 電話屬性對應至員工資料表的電話欄位
        public string 電話 { get; set; }
        [Column]  		// 薪資屬性對應至員工資料表的薪資欄位
        public int 薪資 { get; set; }
    }

}
