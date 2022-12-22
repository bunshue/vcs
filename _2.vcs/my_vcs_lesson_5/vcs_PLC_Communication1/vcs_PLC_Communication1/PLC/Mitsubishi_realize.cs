using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading;
using System.Windows.Forms;

using HslCommunication;
using HslCommunication.Profinet;

namespace vcs_PLC_Communication1.PLC_Communication
{
    /// <summary>
    /// 采用3E幀通訊協議--open-讀取-寫入--繼承接口IPLC_interface
    /// </summary>
    class Mitsubishi_realize : IPLC_interface
    {
        /// <summary>
        /// IP地址
        /// </summary>
        public IPEndPoint IPEndPoint { get; set; }//IP地址
        static private bool PLC_ready;//內部PLC狀態
        //三菱3E幀類--
        /// <summary>
        /// 三菱3E幀類
        /// </summary>
        public static MelsecNet melsec_net = new MelsecNet();//實例化對象;
        //互斥鎖(Mutex)，用于多線程中防止兩條線程同時對一個公共資源進行讀寫的機制。
        /// <summary>
        /// 互斥鎖(Mutex)，用于多線程中防止兩條線程同時對一個公共資源進行讀寫的機制
        /// </summary>
        static Mutex mutex = new Mutex();//實例化互斥鎖(Mutex);//定義互斥鎖名稱
        //實現接口的屬性
        /// <summary>
        ///  三菱 Mitsubishi PLC狀態
        /// </summary>
        bool IPLC_interface.PLC_ready   //PLC狀態
        {
            get
            {
                return PLC_ready;
            }
        }

        public Mitsubishi_realize()//構造函數---多態
        {

        }
        /// <summary>
        /// 三菱 Mitsubishi 鏈接PLC
        /// </summary>
        /// <returns></returns>
        string IPLC_interface.PLC_open()
        {
            if (melsec_net == null) return "鏈接PLC異常";
            try
            {
                //利用三菱3E幀實現
                melsec_net.PLCIpAddress = IPEndPoint.Address;//獲取設置的IP
                melsec_net.PortRead = IPEndPoint.Port;//獲取設置的端口
                melsec_net.ConnectClose();//切換通訊模式
                melsec_net.ConnectTimeout = 500;
                OperateResult connect = melsec_net.ConnectServer();//獲取操作結果
                if (connect.IsSuccess)//判斷是否連接成功
                {
                    PLC_ready = true;//PLC開放正常
                    return "已成功鏈接到" + this.IPEndPoint.Address;
                }
                else
                {
                    PLC_ready = false;//PLC開放異常
                    // 切斷連接
                    melsec_net.ConnectClose();
                    return "鏈接PLC異常";//嘗試連接PLC，如果連接成功則返回值為0
                }
            }
            catch (Exception e)
            {
                err(e);//異常處理
                return "鏈接PLC異常";//嘗試連接PLC，如果連接成功則返回值為0
            }
        }
        /// <summary>
        ///   三菱 Mitsubishi /讀取PLC
        /// </summary>
        /// <param name="Name"></param>
        /// <param name="id"></param>
        /// <returns></returns>
        List<bool> IPLC_interface.PLC_read_M_bit(string Name, string id)//讀取PLC 位狀態 --D_bit這類需要自己在表流獲取當前位狀態--M這類不需要
        {
            string result = "FALSE";//定義獲取數據變量
            lock (this)
            {
                try
                {
                    mutex.WaitOne(100);

                    // 讀取bool變量 重寫方法
                    //不是Y的寫法
                    readResultRender(melsec_net.ReadBoolFromPLC(Name.Trim() + id.Trim()), Name.Trim() + id.Trim(), ref result);//讀取自定地址變量狀態

                    mutex.ReleaseMutex();//解鎖
                }
                catch { }
            }
            return new List<bool>() { Convert.ToBoolean(result ?? "FALSE") };//返回數據
        }

        /// <summary>
        ///  三菱 Mitsubishi  寫入PLC
        /// </summary>
        /// <param name="Name"></param>
        /// <param name="id"></param>
        /// <param name="button_State"></param>
        /// <returns></returns>
        List<bool> IPLC_interface.PLC_write_M_bit(string Name, string id, Button_state button_State)//寫入PLC 位狀態 --D_bit這類需要自己在表流獲取當前位狀態--M這類不需要
        {
            string result = "FALSE";//定義獲取數據變量
            lock (this)
            {
                try
                {
                    mutex.WaitOne(100);

                    //不是Y的寫法
                    bool write_data = false;
                    if (button_State == Button_state.ON)
                    {
                        write_data = true;
                    }
                    else
                    {
                        write_data = false;
                    }
                    //bool write_data = (button_State == Button_state.ON) ? true : false;

                    OperateResult operateResult = melsec_net.WriteIntoPLC(Name.Trim() + id.Trim(), write_data);
                    writeResultRender(operateResult, Name.Trim() + id.Trim());//寫入自定地址變量狀態

                    mutex.ReleaseMutex();//解鎖
                }
                catch { }
            }
            return new List<bool>() { Convert.ToBoolean(result ?? "FALSE") };//返回數據
        }

        /// <summary>
        ///  三菱 Mitsubishi 讀寄存器
        /// </summary>
        /// <param name="Name"></param>
        /// <param name="id"></param>
        /// <param name="format"></param>
        /// <returns></returns>
        string IPLC_interface.PLC_read_D_register(string Name, string id, numerical_format format)//讀寄存器--轉換相應類型
        {
            string result = "0";//定義獲取數據變量
            lock (this)
            {
                try
                {
                    mutex.WaitOne(100);
                    switch (format)
                    {
                        case numerical_format.Signed_16_Bit:
                        case numerical_format.BCD_16_Bit:
                            // 讀取short變量
                            readResultRender(melsec_net.ReadShortFromPLC(Name.Trim() + id.Trim()), Name.Trim() + id.Trim(), ref result);
                            break;
                        case numerical_format.Signed_32_Bit:
                        case numerical_format.BCD_32_Bit:
                            // 讀取int變量
                            readResultRender(melsec_net.ReadIntFromPLC(Name.Trim() + id.Trim()), Name.Trim() + id.Trim(), ref result);
                            break;
                        case numerical_format.Binary_16_Bit:
                            /*
                            // 不支持
                            // 讀取16位二進制數
                            String data_1 = Convert.ToString(result.ToInt32(), 2);
                            readResultRender(melsec_net.ReadShortFromPLC(Name.Trim() + id.Trim()), Name.Trim() + id.Trim(), ref result);
                            */
                            break;
                        case numerical_format.Binary_32_Bit:
                            /*
                            // 不支持
                            // 讀取32位二進制數
                            String data_2 = Convert.ToString(result.ToInt32(), 2);
                            readResultRender(melsec_net.ReadIntFromPLC(Name.Trim() + id.Trim()), Name.Trim() + id.Trim(), ref result);
                            */
                            break;
                        case numerical_format.Float_32_Bit:
                            // 讀取float變量
                            readResultRender(melsec_net.ReadFloatFromPLC(Name.Trim() + id.Trim()), Name.Trim() + id.Trim(), ref result);
                            break;
                        case numerical_format.Hex_16_Bit:
                            // 讀取short變量
                            readResultRender(melsec_net.ReadShortFromPLC(Name.Trim() + id.Trim()), Name.Trim() + id.Trim(), ref result);
                            result = Convert.ToInt32(result).ToString("X");
                            break;
                        case numerical_format.Hex_32_Bit:
                            // 讀取int變量
                            readResultRender(melsec_net.ReadIntFromPLC(Name.Trim() + id.Trim()), Name.Trim() + id.Trim(), ref result);
                            result = Convert.ToInt32(result).ToString("X");
                            break;
                        case numerical_format.Unsigned_16_Bit:
                            // 讀取ushort變量
                            readResultRender(melsec_net.ReadUShortFromPLC(Name.Trim() + id.Trim()), Name.Trim() + id.Trim(), ref result);
                            break;
                        case numerical_format.Unsigned_32_Bit:
                            // 讀取uint變量
                            readResultRender(melsec_net.ReadUIntFromPLC(Name.Trim() + id.Trim()), Name.Trim() + id.Trim(), ref result);
                            break;
                        case numerical_format.String_32_Bit:
                            readResultRender(melsec_net.ReadStringFromPLC(Name.Trim() + id.Trim(), 10), Name.Trim() + id.Trim(), ref result);
                            break;
                    }
                    mutex.ReleaseMutex();
                }
                catch { }
            }
            return result;//返回數據
        }
        /// <summary>
        /// 三菱 Mitsubishi 寫寄存器
        /// </summary>
        /// <param name="Name"></param>
        /// <param name="id"></param>
        /// <param name="content"></param>
        /// <param name="format"></param>
        /// <returns></returns>
        string IPLC_interface.PLC_write_D_register(string Name, string id, string content, numerical_format format)//寫寄存器--轉換類型--并且寫入
        {
            string result = "0";//定義獲取數據變量           
            lock (this)
            {
                try
                {
                    mutex.WaitOne(100);
                    switch (format)
                    {
                        case numerical_format.Signed_16_Bit:
                        case numerical_format.BCD_16_Bit:
                            writeResultRender(melsec_net.WriteIntoPLC(Name.Trim() + id.Trim(), short.Parse(content)), Name.Trim() + id.Trim());
                            break;
                        case numerical_format.Signed_32_Bit:
                        case numerical_format.BCD_32_Bit:
                            writeResultRender(melsec_net.WriteIntoPLC(Name.Trim() + id.Trim(), int.Parse(content)), Name.Trim() + id.Trim());
                            break;
                        case numerical_format.Binary_16_Bit:
                            writeResultRender(melsec_net.WriteIntoPLC(Name.Trim() + id.Trim(), short.Parse(Convert.ToInt32(content, 2).ToString())), Name.Trim() + id.Trim());
                            break;
                        case numerical_format.Binary_32_Bit:
                            writeResultRender(melsec_net.WriteIntoPLC(Name.Trim() + id.Trim(), int.Parse(Convert.ToInt32(content, 2).ToString())), Name.Trim() + id.Trim());
                            break;
                        case numerical_format.Float_32_Bit:
                            writeResultRender(melsec_net.WriteIntoPLC(Name.Trim() + id.Trim(), float.Parse(content)), Name.Trim() + id.Trim());
                            break;
                        case numerical_format.Hex_16_Bit:
                            writeResultRender(melsec_net.WriteIntoPLC(Name.Trim() + id.Trim(), short.Parse(Convert.ToInt32(content, 16).ToString())), Name.Trim() + id.Trim());
                            break;
                        case numerical_format.Hex_32_Bit:
                            writeResultRender(melsec_net.WriteIntoPLC(Name.Trim() + id.Trim(), int.Parse(Convert.ToInt32(content, 16).ToString())), Name.Trim() + id.Trim());
                            break;
                        case numerical_format.Unsigned_16_Bit:
                            writeResultRender(melsec_net.WriteIntoPLC(Name.Trim() + id.Trim(), int.Parse(content)), Name.Trim() + id.Trim());
                            break;
                        case numerical_format.Unsigned_32_Bit:
                            writeResultRender(melsec_net.WriteIntoPLC(Name.Trim() + id.Trim(), int.Parse(content)), Name.Trim() + id.Trim());
                            break;
                        case numerical_format.String_32_Bit:
                            writeResultRender(melsec_net.WriteAsciiStringIntoPLC(Name.Trim() + id.Trim(), content), Name.Trim() + id.Trim());
                            break;
                    }
                    mutex.ReleaseMutex();
                }
                catch { }
            }
            return result;//返回數據
        }
        /// <summary>
        /// 統一的讀取結果的數據解析，顯示
        /// </summary>
        /// <typeparam name="T"></typeparam>
        /// <param name="result"></param>
        /// <param name="address"></param>
        /// <param name="data"></param>
        private void readResultRender<T>(OperateResult<T> result, string address, ref string data)
        {
            if (result.IsSuccess)
            {
                data = result.Content.ToString();//獲取回傳的數據
            }
            else
            {

            }
        }

        /// <summary>
        /// 統一的數據寫入的結果顯示
        /// </summary>
        /// <param name="result"></param>
        /// <param name="address"></param>
        private void writeResultRender(OperateResult result, string address)
        {
            if (result.IsSuccess != true)
            {
                PLC_ready = false;//讀取異常
            }
        }
        /// <summary>
        /// Err處理
        /// </summary>
        /// <param name="e"></param>
        private void err(Exception e)
        {
            PLC_ready = false;//PLC開放異常
        }
    }
}
