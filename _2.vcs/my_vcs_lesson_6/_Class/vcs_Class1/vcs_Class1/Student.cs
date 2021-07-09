using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Windows.Forms;     //for MessageBox

namespace vcs_Class1
{
    public class Student0    //將預設的class Class1 改成 class Student定義Student類別  
    {
        public string Name;       //Name姓名欄位
        public int Score;         //Score成績欄位, 此時的Score無限制

        public void ShowMsg()     //ShowMsg顯示姓名與成績的方法
        {
            MessageBox.Show(Name + "同學的分數是 " + Convert.ToString(Score));
        }

        public string GetMsg()   //GetMsg傳回姓名與成績的方法
        {
            return Name + "同學的分數是 " + Convert.ToString(Score);
        }
    }

    public class StudentA           //定義StudentA類別
    {
        public string Name;        //Name姓名欄位宣告為public
        private int _Score;        //_Score成績欄位宣告為private
        private static int _Total = 0;  //_Total用來計算共產生多少個物件，宣告為static和private

        public StudentA()                //建構式1, 無參數, 不做任何事
        {
            _Total++;                 //_Total++，物件總數加1
        }

        public StudentA(string _vName)  //建構式2, 可設定姓名
        {
            Name = _vName;
            _Total++;                 //_Total++，物件總數加1
        }

        public StudentA(string _vName, int _vScore) //建構式3, 可設定姓名和分數
        {
            Name = _vName;
            Score = _vScore;
            _Total++;                 //_Total++，物件總數加1
        }

        public int Score              //建立Score屬性，此屬性限制在0~100
        {
            get
            {
                return _Score;
            }
            set
            {
                if (value > 100)
                    value = 100;   //Score屬性最大值為100
                if (value < 0)
                    value = 0;       //Score屬性最小值為0
                _Score = value;
            }
        }

        public void ShowMsg()      //ShowMsg顯示姓名與成績的方法
        {
            MessageBox.Show(Name + "同學的分數是 " + Convert.ToString(Score));
        }

        public string GetMsg()   //GetMsg傳回姓名與成績的方法
        {
            return Name + "同學的分數是 " + Convert.ToString(Score);
        }

        public static string GetTotalStudent()   //傳回共產生多少學生物件
        {
            return "本班共有 " + Convert.ToString(_Total) + " 位同學";
        }
    }
}
