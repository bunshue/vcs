using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TaipeiSPAApp
{
    public  class SPAPlace  //SPA地點類別
    {
        //將來當索引編號
        public int ID { get; set; }
        //地名
        public string PlaceName{get;set;}
        //電話
        public string Tel{get;set;}
        //地址
        public string Address{get;set;}
        //經度
        public double Lng{get;set;}
        //緯度
        public double Lat{get;set;}
    }
}
