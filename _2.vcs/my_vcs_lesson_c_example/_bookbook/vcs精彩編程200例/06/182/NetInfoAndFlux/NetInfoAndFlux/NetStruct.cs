using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Diagnostics;

namespace NetInfoAndFlux
{
    //=====================================================
    //Copyright (C) 2008-2009 小科
    //All rights reserved
    //CLR版本:           2.0.50727.1433
    //新建项输入的名称:  NetStruct
    //机器名称:          MRWXK
    //命名空间名称:      NetInfoAndFlux
    //文件名:            NetStruct
    //当前系统时间:      2008-10-16 17:54:32
    //当前登录用户名:    Administrator
    //创建年份:          2008
    //http://www.mingribook.com
    //======================================================
    class NetStruct
    {
        public NetStruct(string strname)
		{
            name = strname;
		}

        private long receive, send;
        private long receiveValue, sendValue;
        private long receiveOldValue, sendOldValue;
        private string name;
        internal PerformanceCounter receiveCounter, sendCounter;

		///<summary>
		///初始化流量
		///</summary>
        internal void BeInfo()
		{
            receiveOldValue = receiveCounter.NextSample().RawValue;
            sendOldValue = sendCounter.NextSample().RawValue;
		}

		///<summary>
		///刷新网络流量
		///</summary>
        internal void ReInfo()
		{
            receiveValue = receiveCounter.NextSample().RawValue;
            sendValue = sendCounter.NextSample().RawValue;
            receive = receiveValue - receiveOldValue;
            send = sendValue - sendOldValue;
            receiveOldValue = receiveValue;
            sendOldValue = sendValue;
		}

		public override string ToString()
		{
			return name;
		}

		public string Name
		{
			get
			{
				return name;
			}
		}
		
        public long Receive
		{
			get
			{
				return receive;
			}
		}
		
        public long Send
		{
			get
			{
                return send;
			}
		}
    }
}
