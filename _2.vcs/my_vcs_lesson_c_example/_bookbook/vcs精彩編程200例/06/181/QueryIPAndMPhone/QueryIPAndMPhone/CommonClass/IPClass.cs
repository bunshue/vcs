using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Text.RegularExpressions;

namespace QueryIPAndMPhone.CommonClass
{
    //=====================================================
    //Copyright (C) 2008-2009 小科
    //All rights reserved
    //CLR版本:           2.0.50727.1433
    //新建项输入的名称:  IPClass
    //机器名称:          MRWXK
    //命名空间名称:      QueryIPAndMPhone.CommonClass
    //文件名:            IPClass
    //当前系统时间:      2008-10-14 10:20:23
    //当前登录用户名:    Administrator
    //创建年份:          2008
    //http://www.mingribook.com
    //======================================================
    class IPClass
    {
        //查找IP
        public static IPStruct SearchIP(string strPath, string strIPS)
        {
            if (!File.Exists(strPath))
            {
                throw new Exception("文件不存在!");
            }
            FileStream FStream = new FileStream(strPath, FileMode.Open, FileAccess.Read, FileShare.Read);
            BinaryReader BReader = new BinaryReader(FStream);
            //获取首末记录偏移量
            int intFirst = BReader.ReadInt32();
            int intLast = BReader.ReadInt32();
            //IP值
            uint uintIP = IPToInt(strIPS);
            //获取IP索引记录偏移值
            int intIndex = GetIPIndex(FStream, BReader, intFirst, intLast, uintIP);
            IPStruct myIPStruct;
            if (intIndex >= 0)
            {
                FStream.Seek(intIndex,SeekOrigin.Begin);
                //读取开头IP值
                myIPStruct.IPStart = BReader.ReadUInt32();
                FStream.Seek(ReadInt(BReader),SeekOrigin.Begin);
                //读取结尾IP值
                myIPStruct.IPEnd = BReader.ReadUInt32();
                myIPStruct.Country = GetIPPlace(FStream, BReader);
                myIPStruct.City = GetIPPlace(FStream, BReader);
            }
            else
            {
                myIPStruct.IPStart = 0;
                myIPStruct.IPEnd = 0;
                myIPStruct.Country = "未知国家";
                myIPStruct.City = "未知地址";
            }
            BReader.Close();
            FStream.Close();
            return myIPStruct;
        }
        //定位IP索引记录位置
        private static int GetIPIndex(FileStream FStream, BinaryReader BReader, int intFirst, int intLast, uint uintIP)
        {
            int intMiddle;                  //中间偏移量
            uint uintMValue;                //中间值
            uint uintFValue, uintLValue;    //边界值
            uint uintTmpLValue;             //临时边界末尾值
            FStream.Seek(intFirst, SeekOrigin.Begin);
            uintFValue = BReader.ReadUInt32();
            FStream.Seek(intLast, SeekOrigin.Begin);
            uintLValue = BReader.ReadUInt32();
            //临时记录偏移量
            intMiddle = ReadInt(BReader);
            FStream.Seek(intMiddle, SeekOrigin.Begin);
            uintTmpLValue = BReader.ReadUInt32();
            //边界检测处理
            if (uintIP < uintFValue)
                return -1;
            else if (uintIP > uintTmpLValue)
                return -1;
            //确定记录偏移量
            do
            {
                intMiddle = intFirst + (intLast - intFirst) / 7 / 2 * 7;
                FStream.Seek(intMiddle, SeekOrigin.Begin);
                uintMValue = BReader.ReadUInt32();
                if (uintIP >= uintMValue)
                    intFirst = intMiddle;
                else
                    intLast = intMiddle;
                if (intLast - intFirst == 7)
                    intMiddle = intLast = intFirst;
            } while (intFirst != intLast);
            return intMiddle;
        }
        //判断字符串是否为数值类型
        private static bool IsNumeric(string str)
        {
            if (str != null && Regex.IsMatch(str, @"^-?\d+$"))
                return true;
            else
                return false;
        }
        //将IP字符串转换为长整型值
        private static uint IPToInt(string strIPS)
        {
            uint uintIP = 0;
            string[] strIP = strIPS.Split('.');
            int i;
            uint ui;
            for (i = 0; i < 4 && i < strIP.Length; i++)
            {
                if (IsNumeric(strIP[i]))
                {
                    ui = (uint)Math.Abs(Convert.ToInt32(strIP[i]));
                    if (ui > 255) ui = 255;
                    uintIP += ui << (3 - i) * 8;
                }
            }
            return uintIP;
        }
        //将长整型值转化为IP字符串
        public static string IntToIP(uint uintIP)
        {
            string strIP = "";
            strIP += (uintIP >> 24) + "." + ((uintIP & 0x00FF0000) >> 16) + "." + ((uintIP & 0x0000FF00) >> 8) + "." + (uintIP & 0x000000FF);
            return strIP;
        }
        //读取字符串
        public static string ReadString(BinaryReader BReader)
        {
            byte[] btContent = new byte[128];
            int i = 0;
            do
            {
                btContent[i] = BReader.ReadByte();
            } while (btContent[i++] != '\0' && i < 128);
            return Encoding.Default.GetString(btContent).TrimEnd('\0');
        }
        //读取3字节的整数
        public static int ReadInt(BinaryReader BReader)
        {
            if (BReader == null) return -1;
            int intNum = 0;
            intNum |= (int)BReader.ReadByte();
            intNum |= (int)BReader.ReadByte() << 8 & 0xFF00;
            intNum |= (int)BReader.ReadByte() << 16 & 0xFF0000;
            return intNum;
        }
        //读取IP所在地字符串
        private static string GetIPPlace(FileStream FStream, BinaryReader BReader)
        {
            byte Tag;
            int OffSet;
            Tag = BReader.ReadByte();
            if (Tag == 0x01)		//城市信息随国家信息定向
            {
                OffSet = ReadInt(BReader);
                FStream.Seek(OffSet,SeekOrigin.Begin);
                return GetIPPlace(FStream, BReader);
            }
            else if (Tag == 0x02)	//城市信息不随国家信息定向
            {
                OffSet = ReadInt(BReader);
                int tmpOffSet = (int)FStream.Position;
                FStream.Seek(OffSet,SeekOrigin.Begin);
                string tmpStr = GetIPPlace(FStream, BReader);
                FStream.Seek(tmpOffSet,SeekOrigin.Begin);
                return tmpStr;
            }
            else	                //最简单模式
            {
                FStream.Seek(-1,SeekOrigin.Current);
                return ReadString(BReader);
            }
        }
    }
    //IP地址结构
    public struct IPStruct
    {
        public uint IPStart;        //开始IP
        public uint IPEnd;          //结束IP
        public string Country;      //省份
        public string City;         //城市
    }
}
