using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//使用ObservableCollection類別必須引用此命名空間
using System.Collections.ObjectModel;
//使用WebClient類別必須引用此命名空間
using System.Net;
//使用JsonConvert類別必須引用此命名空間
using Newtonsoft.Json;
//使用JArray類別必須引用此命名空間
using Newtonsoft.Json.Linq;   

namespace TaipeiSPAApp
{
   public   class MainViewModel
    {
        public ObservableCollection<SPAPlace> Items { get; set; }

        public MainViewModel()
        {
            Items = new ObservableCollection<SPAPlace>();
        }

        public bool IsDataLoaded
        {
            get;
            private set;
        }

        public void LoadData()
        {
            WebClient wc = new WebClient();
            wc.DownloadStringAsync(new Uri("http://data.taipei.gov.tw/opendata/apply/json/RjQzRThDNjUtMzU3OS00MTU5LUEwOUEtMUI2NzFDOTE5NDcz"));
            wc.DownloadStringCompleted += wc_DownloadStringCompleted;
        }

        void wc_DownloadStringCompleted(object sender, DownloadStringCompletedEventArgs e)
        {
            JArray spaJspn = JsonConvert.DeserializeObject<JArray>(e.Result);
            int i = 0; 
            foreach (var s in spaJspn)
            {
                this.Items.Add (new SPAPlace()
                {
                    ID  = i,
                    PlaceName = (string)s["name"],
                    Address = (string)s["poi_addr"],
                    Tel = (string)s["tel"],
                    Lng = (double)s["X"],
                    Lat = (double )s["Y"]
                });
                i++;
            }
            this.IsDataLoaded = true;
        }
    }
}
