using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


using System.Data.Linq.Mapping; //含入System.Data.Linq.Mapping


namespace Linq_to_SQL2
{
    [Table(Name = "員工")]
    class Employee
    {
        [Column(Name = "編號")]	// 將員工編號屬性對應至員工資料表的編號欄位
        public int 員工編號 { get; set; }
        [Column(Name = "姓名")]	// 將員工姓名屬性對應至員工資料表的姓名欄位
        public string 員工姓名 { get; set; }
        [Column(Name = "職稱")]	// 將職位屬性對應至員工資料表的職稱欄位
        public string 職位 { get; set; }
        [Column(Name = "電話")]	// 將聯絡電話屬性對應至員工資料表的電話欄位
        public string 聯絡電話 { get; set; }
        [Column(Name = "薪資")]	// 將月薪屬性對應至員工資料表的薪資欄位
        public int 月薪 { get; set; }
    }

}
