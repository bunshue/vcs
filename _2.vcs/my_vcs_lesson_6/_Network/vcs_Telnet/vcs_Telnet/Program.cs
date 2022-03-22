using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Net.Sockets;   //for telnet

namespace vcs_Telnet
{
    class Program
    {
        static void Main(string[] args)
        {
            //create a new telnet connection to hostname "gobelijn" on port "23" 
            TelnetConnection tc = new TelnetConnection("192.168.2.248", 22);

            //login with user "root",password "rootpassword", using a timeout of 100ms,  
            //and show server output 
            string s = tc.Login("pi", "035631166", 100);
            Console.Write(s);

            // server output should end with "{1}quot; or ">", otherwise the connection failed 
            string prompt = s.TrimEnd();
            prompt = s.Substring(prompt.Length - 1, 1);
            if (prompt != ":")
                throw new Exception("Connection failed");

            prompt = "";

            // while connected 
            while (tc.IsConnected && prompt.Trim() != "exit")
            {
                // display server output 
                Console.Write(tc.Read());

                // send client input to server 
                prompt = Console.ReadLine();
                tc.WriteLine(prompt);

                // display server output 
                Console.Write(tc.Read());
            }

            Console.WriteLine("***DISCONNECTED");
            Console.ReadLine();



        }
    }

    enum Verbs
    {
        WILL = 251,
        WONT = 252,
        DO = 253,
        DONT = 254,
        IAC = 255
    }

    enum Options
    {
        SGA = 3
    }

    class TelnetConnection
    {
        TcpClient tcpSocket;

        int TimeOutMs = 1 * 1000;

        public TelnetConnection(String Hostname, int Port)
        {
            tcpSocket = new TcpClient(Hostname, Port);
        }

        public string Login(string Username, string Password, int LoginTimeOutMs)
        {
            int oldTimeOutMs = TimeOutMs;
            TimeOutMs = LoginTimeOutMs;
            string s = Read();
            if (!s.TrimEnd().EndsWith(":"))
                throw new Exception("Failed to connect : no login prompt");
            WriteLine(Username);

            s += Read();
            if (!s.TrimEnd().EndsWith(":"))
                throw new Exception("Failed to connect : no password prompt");
            WriteLine(Password);

            s += Read();
            TimeOutMs = oldTimeOutMs;

            return s;
        }

        public void DisConnect()
        {
            if (tcpSocket != null)
            {
                if (tcpSocket.Connected)
                {
                    tcpSocket.Client.Disconnect(true);
                }
            }
        }

        public void WriteLine(string cmd)
        {
            Write(cmd + "\r\n");
        }

        public void Write(string cmd)
        {
            if (!tcpSocket.Connected) return;

            byte[] buf = System.Text.ASCIIEncoding.ASCII.GetBytes(cmd.Replace("\0xFF", "\0xFF\0xFF"));
            tcpSocket.GetStream().Write(buf, 0, buf.Length);
        }

        public string Read()
        {
            if (!tcpSocket.Connected) return null;
            StringBuilder sb = new StringBuilder();
            do
            {
                ParseTelnet(sb);
                System.Threading.Thread.Sleep(TimeOutMs);
            } while (tcpSocket.Available > 0);

            return ConvertToGB2312(sb.ToString());
        }

        public bool IsConnected
        {
            get { return tcpSocket.Connected; }
        }

        void ParseTelnet(StringBuilder sb)
        {
            while (tcpSocket.Available > 0)
            {
                int input = tcpSocket.GetStream().ReadByte();
                switch (input)
                {
                    case -1:
                        break;
                    case (int)Verbs.IAC:
                        // interpret as command
                        int inputverb = tcpSocket.GetStream().ReadByte();
                        if (inputverb == -1) break;
                        switch (inputverb)
                        {
                            case (int)Verbs.IAC:
                                //literal IAC = 255 escaped, so append char 255 to string
                                sb.Append(inputverb);
                                break;
                            case (int)Verbs.DO:
                            case (int)Verbs.DONT:
                            case (int)Verbs.WILL:
                            case (int)Verbs.WONT:
                                // reply to all commands with "WONT", unless it is SGA (suppres go ahead)
                                int inputoption = tcpSocket.GetStream().ReadByte();
                                if (inputoption == -1) break;
                                tcpSocket.GetStream().WriteByte((byte)Verbs.IAC);
                                if (inputoption == (int)Options.SGA)
                                    tcpSocket.GetStream().WriteByte(inputverb == (int)Verbs.DO ? (byte)Verbs.WILL : (byte)Verbs.DO);
                                else
                                    tcpSocket.GetStream().WriteByte(inputverb == (int)Verbs.DO ? (byte)Verbs.WONT : (byte)Verbs.DONT);
                                tcpSocket.GetStream().WriteByte((byte)inputoption);
                                break;
                            default:
                                break;
                        }
                        break;
                    default:
                        sb.Append((char)input);
                        break;
                }
            }
        }

        private string ConvertToGB2312(string str_origin)
        {
            char[] chars = str_origin.ToCharArray();
            byte[] bytes = new byte[chars.Length];
            for (int i = 0; i < chars.Length; i++)
            {
                int c = (int)chars[i];
                bytes[i] = (byte)c;
            }
            Encoding Encoding_GB2312 = Encoding.GetEncoding("GB2312");
            string str_converted = Encoding_GB2312.GetString(bytes);
            return str_converted;
        }
    }
}

