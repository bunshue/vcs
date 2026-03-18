using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Diagnostics;

namespace vcs_NetFlux
{
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
