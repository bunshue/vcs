using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    /// <summary>
    /// Max记号类，求两个数中较大的一个，对应关键字max，不区分大小写。
    /// </summary>
    /// <example>用法max(15,20)，返回20。</example>
    public class TokenMax : TokenArithmeticMethod
    {
        public TokenMax(int Index, int Length)
            : base(Index, Length)
        { }

        /// <summary>
        /// 检查下级数量
        /// </summary>
        /// <returns></returns>
        public new void CheckChildCount(string ErrorInformation)
        {
            if (this.ChildList.Count < 2)
            {
                throw new SyntaxException(this.Index, this.Length, ErrorInformation);
            }
        }

        private const string c_IsNotNumber = "Max方法的操作数不是数字";
        public override void Execute()
        {
            this.CheckChildCount("Max方法的运算元素数量不合法");

            List<double> myList = new List<double>();
            foreach (TokenRecord item in this.ChildList)
            {
                item.Execute();
                myList.Add(item.ChangeTokenToDouble(c_IsNotNumber));
            }
            myList.Sort();

            this.TokenValue = myList[myList.Count - 1];
        }
    }
}
