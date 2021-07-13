using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_Class1
{
    class Person2
    {
        private string firstname = "DEFAULT";
        private string lastname = "CAN NOT CHANGE";
        private int age;

        public string FirstName  //可讀可寫, 有get有set
        {
            get
            {
                return firstname;
            }
            set
            {
                firstname = value;
            }
        }

        public string LastName  //可讀不可寫, 只有get
        {
            get
            {
                return lastname;
            }
        }

        public int Age  //可讀可寫, 有get有set
        //可讀可寫  set部分可加入判斷式來對傳入的值做相對應處理
        {
            get
            {
                return age;
            }
            set
            {
                age = (value < 10) ? 0 : 100; //if簡寫
                //原表示
                /*if(value<10)
                {
                        age =0;
                }
                else
                {
                        age =100;
                }*/
            }
        }

        public string Sex  //get set 簡寫  可讀可寫
        {
            get;
            set;
        }

        public string ADDR  //get set 簡寫  可讀不可寫
        {
            get;
            private set;
        }
    }
}

