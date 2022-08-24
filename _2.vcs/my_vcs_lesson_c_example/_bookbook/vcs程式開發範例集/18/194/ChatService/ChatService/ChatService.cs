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
            // TODO: 在此处添加代码以启动服务。
            server = new Form1();
            server.Start();
        }

        protected override void OnStop()
        {
            // TODO: 在此处添加代码以执行停止服务所需的关闭操作。
            server.Stop();
        }
    }
}
