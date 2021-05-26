using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;
namespace EncryptDog
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        string str;
        string cn="";
        private void Form1_Load(object sender, EventArgs e)
        {

            Dog dog = new Dog(100);
            dog.DogAddr = 0;			
            dog.DogBytes = 10;			
            str = "19820112";
            for (int i = 0; i < str.Length; i++)
            {
                dog.DogData[i] = (byte)str[i];
            }
            dog.WriteDog();
            label1.Location = new Point(this.Width/4,30);
            label1.ForeColor = Color.White;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            string dogdata = "";
            Dog dog = new Dog(100);
            dog.DogAddr = 0;			
            dog.DogBytes = 10;			
            dog.ReadDog();
            if (dog.Retcode == 0)
            {
                char[] chTemp = new char[str.Length];
                for (int i = 0; i < str.Length; i++)
                {
                    chTemp[i] = (char)dog.DogData[i];
                }

                String strs = new String(chTemp);
                dogdata = strs;
            }
            else
            {
                dogdata = "2:" + dog.Retcode;
            }
            if (dogdata == cn)
            {
                label1.Text = "当前版本为正式版本";
                groupBox1.Visible = false;
            }
            else
            {
                label1.Text = "软件未注册！";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            cn = textBox1.Text.Trim();
        }
    }
    [StructLayout(LayoutKind.Sequential)]
    //这个类用于读写加密狗。
    public unsafe class Dog
    {

        public uint DogBytes, DogAddr;  //设置加密狗起始地址
        public byte[] DogData;          //设置数据的长度
        public uint Retcode;

        [DllImport("Win32dll.dll", CharSet = CharSet.Ansi)]
        public static unsafe extern uint DogRead(uint idogBytes, uint idogAddr, byte* pdogData);
        [DllImport("Win32dll.dll", CharSet = CharSet.Ansi)]
        public static unsafe extern uint DogWrite(uint idogBytes, uint idogAddr, byte* pdogData);

        public unsafe Dog(ushort num)
        {
            DogBytes = num;
            DogData = new byte[DogBytes]; //设置数据的长度
        }

        public unsafe void ReadDog()
        {
            fixed (byte* pDogData = &DogData[0])
            {
                Retcode = DogRead(DogBytes, DogAddr, pDogData);　　//将数据读出加密狗
            }
        }
        public unsafe void WriteDog()
        {
            fixed (byte* pDogData = &DogData[0])
            {
                Retcode = DogWrite(DogBytes, DogAddr, pDogData);　//将数据写入加密狗
            }
        }
    }
}
