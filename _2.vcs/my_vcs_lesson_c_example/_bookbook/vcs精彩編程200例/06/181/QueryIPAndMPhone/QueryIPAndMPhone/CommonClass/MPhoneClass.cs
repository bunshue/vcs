using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace QueryIPAndMPhone.CommonClass
{
    //=====================================================
    //Copyright (C) 2008-2009 小科
    //All rights reserved
    //CLR版本:           2.0.50727.1433
    //新建项输入的名称:  MPhoneClass
    //机器名称:          MRWXK
    //命名空间名称:      QueryIPAndMPhone.CommonClass
    //文件名:            MPhoneClass
    //当前系统时间:      2008-10-14 10:20:44
    //当前登录用户名:    Administrator
    //创建年份:          2008
    //http://www.mingribook.com
    //======================================================
    class MPhoneClass
    {
        //查询手机号码,返回号码段和归属地信息
        public static MPhoneStruct GetMPhonePlace(string strPath, int intMPhone)
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
            int intIndex = GetMPhoneIndex(FStream, BReader, intFirst, intLast, intMPhone);
            MPhoneStruct myMPhoneStruct;
            if (intIndex >= 0)
            {
                FStream.Seek(intIndex,SeekOrigin.Begin);
                //读取号码段起始地址和结束地址
                myMPhoneStruct.MPhoneStart = BReader.ReadInt32();
                myMPhoneStruct.MPhoneEnd = BReader.ReadInt32();
                //如果查询的号码处于中间空段
                if (intMPhone > myMPhoneStruct.MPhoneEnd)
                {
                    myMPhoneStruct.MPhoneStart = 0; 
                    myMPhoneStruct.MPhoneEnd = 0;
                    myMPhoneStruct.Place = "未知地址";
                }
                else
                {
                    //读取字符串偏移量3字节!
                    int intIndex1 = IPClass.ReadInt(BReader);
                    FStream.Seek(intIndex1,SeekOrigin.Begin);
                    //读取归属地字符串
                    myMPhoneStruct.Place = IPClass.ReadString(BReader);
                }
            }
            else
            {
                myMPhoneStruct.MPhoneStart = 0; 
                myMPhoneStruct.MPhoneEnd = 0;
                myMPhoneStruct.Place = "未知地址";
            }
            BReader.Close();
            FStream.Close();
            return myMPhoneStruct;
        }
        //获取号码段记录在文件中的偏移量
        private static int GetMPhoneIndex(FileStream FStream, BinaryReader BReader, int intFirst, int intLast, int intMPhone)
        {
            int intMiddle;              //中间偏移量
            int intMValue;              //中间值
            int intFValue, intLValue;   //边界值
            FStream.Seek(intFirst, SeekOrigin.Begin);
            intFValue = BReader.ReadInt32();
            FStream.Seek(intLast, SeekOrigin.Begin);
            intLValue = BReader.ReadInt32();
            //边界检测处理
            if (intMPhone < intFValue)
                return -1;
            else if (intMPhone > intLValue)
                return -1;
            //确定记录偏移量
            do
            {
                intMiddle = intFirst + (intLast - intFirst) / 11 / 2 * 11;
                FStream.Seek(intMiddle, SeekOrigin.Begin);
                intMValue = BReader.ReadInt32();
                if (intMPhone >= intMValue)
                    intFirst = intMiddle;
                else
                    intLast = intMiddle;
                if (intLast - intFirst == 11)
                    intMiddle = intLast = intFirst;
            } while (intFirst != intLast);
            return intMiddle;
        }
    }
    //手机归属地结构
    public struct MPhoneStruct
    {
        public int MPhoneStart;     //开始号码
        public int MPhoneEnd;       //结束号码
        public string Place;        //归属地
    }
}
