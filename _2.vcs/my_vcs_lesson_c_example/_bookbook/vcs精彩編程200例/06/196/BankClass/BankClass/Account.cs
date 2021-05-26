﻿using System;
using System.Collections.Generic;
using System.Text;
using System.EnterpriseServices;
using System.Data;
using System.Data.SqlClient;
using System.Diagnostics;

namespace BankClass
{
    public class Account
    {
        public void Saveing(string bank, float balance,string account)
        {
            try
            {
                SqlConnection con = new SqlConnection("Server=USER-20170504OU,DataBase=db_35,uid=sa,pwd");
                con.Open();
                SqlCommand cmd = new SqlCommand("UPDATE " + bank + " SET balance = balance + " + Convert.ToDouble(balance) + " WHERE (account = 123456)", con);
                int i = (int)cmd.ExecuteNonQuery();
                con.Close();
                WriteInfo(DateTime.Now.ToString() + " 银行名称：" + bank + " 账号：" + account + "存入金额为：" + balance.ToString());
            }
            catch(Exception ex)
            {
                WriteError(ex.Message);
                throw new Exception(ex.Message);
            }
        }

        public void Fetch(string bank, float balance,string account)
        {
            try
            {
                if (balance >Convert.ToSingle(GetBalance(bank, balance, account)))
                {
                    throw new Exception("银行：" + bank + " 账号：" + account + "余额不足！");
                }

                SqlConnection con = new SqlConnection("Server=MR-PC\\YL,DataBase=db_35,uid=sa,pwd");
                con.Open();
                SqlCommand cmd = new SqlCommand("UPDATE " + bank + " SET balance = balance - " + Convert.ToDouble(balance) + " WHERE (account = 123456)", con);
                int i = (int)cmd.ExecuteNonQuery();
                con.Close();
                WriteInfo(DateTime.Now.ToString() + " 银行名称：" + bank + " 账号：" + account + "提取金额为：" + balance.ToString());
            }
            catch (Exception ex)
            {
                WriteError(ex.Message.ToString());
                throw new Exception(ex.Message);
            }
        }

        public int GetBalance( string bank, float balance,string account)
        {
            SqlConnection con = new SqlConnection("Server=MR-PC\\YL,DataBase=db_35,uid=sa,pwd");
            SqlDataAdapter dap = new SqlDataAdapter("select * from " + bank + "where account='" + account + "'", con);
            DataSet ds = new DataSet();
            dap.Fill(ds);
            return int.Parse(ds.Tables[0].Rows[0]["balance"].ToString());
        }

        public void WriteError(string error)
        {
            EventLog.WriteEntry("示例BankClass COM+组件服务", error, EventLogEntryType.Error);
        }
        public void WriteInfo(string info)
        {
            EventLog.WriteEntry("示例BankClass COM+组件服务", info, EventLogEntryType.Information);
        }
    }
}
