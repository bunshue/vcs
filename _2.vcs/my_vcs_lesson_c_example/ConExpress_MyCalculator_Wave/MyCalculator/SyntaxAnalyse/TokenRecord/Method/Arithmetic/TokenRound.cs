using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenRound : TokenArithmeticMethod
    {
        public TokenRound(int Index, int Length)
            : base(Index, Length)
        { }

        public override void Execute()
        {
            this.CheckChildCount("round语句的运算元素数量不合法");

            TokenRecord TokenSouece = this.ChildList[0];
            TokenRecord TokenLength = this.ChildList[1];
            TokenSouece.Execute();
            TokenLength.Execute();

            //check child token type
            double dblSource = TokenSouece.ChangeTokenToDouble("round语句的运算元素不是数值");
            int intLength = Convert.ToInt32(TokenLength.ChangeTokenToDouble("round语句的截取位数不是数值"));

            //检测保留小数位长度是否合法
            intLength = intLength < 0 ? 0 : intLength;
            intLength = intLength > 28 ? 28 : intLength;

            this.TokenValue = Math.Round(dblSource, intLength);
        }
    }
}
