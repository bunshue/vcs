using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenPlus : TokenArithmeticSymbol
    {
        public TokenPlus(int Index, int Length)
            : base(Index, Length)
        {
        }
        
        protected override void SetPriority()
        {
            this.m_Priority = 2;
        }

        public override void Execute()
        {
            this.CheckChildCount("加法的运算元素数量不合法");

            TokenRecord TokenFirst = this.ChildList[0];
            TokenRecord TokenSecond = this.ChildList[1];
            TokenFirst.Execute();
            TokenSecond.Execute();

            this.TokenValueType = ((TokenFirst.TokenValueType == TokenSecond.TokenValueType) ? TokenFirst.TokenValueType : typeof(string));

            if (this.TokenValueType == typeof(string))
            {
                this.TokenValue = TokenFirst.ChangeTokenToString() + TokenSecond.ChangeTokenToString();
            }
            else
            {
                this.TokenValue = TokenFirst.ChangeTokenToDouble("无法转换为数字。") + TokenSecond.ChangeTokenToDouble("无法转换为数字。");
            }
        }
    }
}
