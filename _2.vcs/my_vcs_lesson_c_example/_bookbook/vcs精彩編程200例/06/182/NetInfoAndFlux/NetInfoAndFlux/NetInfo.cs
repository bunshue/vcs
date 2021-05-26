using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Collections;
using System.Diagnostics;
using System.Timers;

namespace NetInfoAndFlux
{
    //=====================================================
    //Copyright (C) 2008-2009 小科
    //All rights reserved
    //CLR版本:           2.0.50727.1433
    //新建项输入的名称:  NetInfo
    //机器名称:          MRWXK
    //命名空间名称:      NetInfoAndFlux
    //文件名:            NetInfo
    //当前系统时间:      2008-10-16 17:55:02
    //当前登录用户名:    Administrator
    //创建年份:          2008
    //http://www.mingribook.com
    //======================================================
    class NetInfo
    {
        private Timer timer;			//计时器
        private ArrayList listnet;		//本地机器正在使用的网卡
        private ArrayList listnets;		//本地机器上的网卡

        public NetInfo()
        {
            listnet = new ArrayList();
            listnets = new ArrayList();
            ISNet();
            timer = new Timer(1000);
            timer.Elapsed += new ElapsedEventHandler(timer_Elapsed);
        }

        ///<summary>
        ///判断网卡是否存在
        ///</summary>
        private void ISNet()
        {
            PerformanceCounterCategory category = new PerformanceCounterCategory("Network Interface");
            foreach (string name in category.GetInstanceNames())
            {
                if (name == "MS TCP Loopback interface")
                    continue;
                NetStruct myNetStruct = new NetStruct(name);
                myNetStruct.receiveCounter = new PerformanceCounter("Network Interface", "Bytes Received/sec", name);
                myNetStruct.sendCounter = new PerformanceCounter("Network Interface", "Bytes Sent/sec", name);
                listnet.Add(myNetStruct);
            }
        }

        private void timer_Elapsed(object sender, ElapsedEventArgs e)
        {
            foreach (NetStruct myNetStruct in listnets)
                myNetStruct.ReInfo();
        }

        public NetStruct[] myNetStructs
        {
            get
            {
                return (NetStruct[])listnet.ToArray(typeof(NetStruct));
            }
        }

        public void GetInfo(NetStruct myNetStruct)
        {
            if (!listnets.Contains(myNetStruct))
            {
                listnets.Add(myNetStruct);
                myNetStruct.BeInfo();
            }
            timer.Enabled = true;
        }
    }
}