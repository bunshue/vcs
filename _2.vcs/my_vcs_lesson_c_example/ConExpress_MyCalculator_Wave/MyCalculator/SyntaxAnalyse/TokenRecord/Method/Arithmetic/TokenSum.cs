using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    /// <summary>
    /// 计算和
    /// </summary>
    /// <remarks>Author:Alex Leo; Date:2009-5-21;</remarks>
    public class TokenSum : TokenArithmeticMethod
    {
        public TokenSum(int Index, int Length)
            : base(Index, Length)
        { }

        /// <summary>
        /// 检查下级数量
        /// </summary>
        /// <returns></returns>
        public new void CheckChildCount(string ErrorInformation)
        {
            if (this.ChildList.Count < 1)
            {
                throw new SyntaxException(this.Index, this.Length, ErrorInformation);
            }
        }

        private const string c_IsNotNumber = "Sum方法的操作数不是数字";
        public override void Execute()
        {
            this.CheckChildCount("Sum方法的运算元素数量不合法");

            double dblSum = 0D;
            foreach (TokenRecord item in this.ChildList)
            {
                item.Execute();
                dblSum += item.ChangeTokenToDouble(c_IsNotNumber);
            }

            this.TokenValue = dblSum;
        }

    }
}
