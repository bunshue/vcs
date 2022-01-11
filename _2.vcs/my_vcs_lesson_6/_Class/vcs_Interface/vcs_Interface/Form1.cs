using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Interface
{
    public partial class Form1 : Form
    {
        USB usb;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            richTextBox1.Text += "USB Interface(接口) 使用範例\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            usb = new UDisk();//插入U盤
            usb.OutputFile();//從U盤讀出文件
            usb.InputFile();//往U盤寫入文件
            usb.Dispose();//拔出U盤
        }

        private void button2_Click(object sender, EventArgs e)
        {
            usb = new MDisk();//插入移動硬盤
            usb.OutputFile();//從移動硬盤讀出文件
            usb.InputFile();//往移動硬盤寫入文件
            usb.Dispose();//拔出移動硬盤
        }

        private void button3_Click(object sender, EventArgs e)
        {
            usb = new MP4();//插入MP4
            usb.OutputFile();//從MP4讀出文件
            usb.InputFile();//往MP4寫入文件
            usb.Dispose();//拔出MP4
        }

        //USB接口
        public interface USB : IDisposable
        {
            void OutputFile();//讀出文件
            void InputFile();//寫入文件
        }

        //U盤
        public class UDisk : USB
        {
            public UDisk()
            {
                Console.WriteLine("U盤准備就緒...");
            }
            public void OutputFile()
            {
                Console.WriteLine("從U盤讀出文件");
            }
            public void InputFile()
            {
                Console.WriteLine("往U盤寫入文件");
            }
            public void Dispose()
            {
                Console.WriteLine("U盤已被拔出");
            }
        }

        //移動硬盤
        public class MDisk : USB
        {
            public MDisk()
            {
                Console.WriteLine("移動硬盤准備就緒...");
            }
            public void OutputFile()
            {
                Console.WriteLine("從移動硬盤讀出文件");
            }
            public void InputFile()
            {
                Console.WriteLine("往移動硬盤寫入文件");
            }
            public void Dispose()
            {
                Console.WriteLine("移動硬盤已被拔出");
            }
        }

        //MP4
        public class MP4 : USB
        {
            public MP4()
            {
                Console.WriteLine("MP4准備就緒...");
            }
            public void OutputFile()
            {
                Console.WriteLine("從MP4讀出文件");
            }
            public void InputFile()
            {
                Console.WriteLine("往MP4寫入文件");
            }
            public void Dispose()
            {
                Console.WriteLine("MP4已被拔出");
            }
        }
    }
}
