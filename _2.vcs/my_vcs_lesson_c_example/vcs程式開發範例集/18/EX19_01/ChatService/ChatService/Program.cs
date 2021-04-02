using System;
using System.Collections.Generic;
using System.Linq;
using System.ServiceProcess;
using System.Text;

namespace ChatService
{
    static class Program
    {
        /// <summary>
        /// 運用程序的主入口點。
        /// </summary>
        static void Main()
        {
            ServiceBase[] ServicesToRun;
            ServicesToRun = new ServiceBase[] 
			{ 
				//new Service1() 
			};
            ServiceBase.Run(ServicesToRun);
        }
    }
}
