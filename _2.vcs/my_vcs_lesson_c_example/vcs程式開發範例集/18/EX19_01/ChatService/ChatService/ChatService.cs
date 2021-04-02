using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.ServiceProcess;
using System.Text;
using ChatServer;

namespace ChatService
{
    public partial class ChatService : ServiceBase
    {
        ChatServer.Form1 server;
        public ChatService()
        {
            InitializeComponent();
        }

        protected override void OnStart(string[] args)
        {
            // TODO: 在此處新增程式碼以啟動服務。
            server = new Form1();
            server.Start();
        }

        protected override void OnStop()
        {
            // TODO: 在此處新增程式碼以執行停止服務所需的關閉操作。
            server.Stop();
        }
    }
}
