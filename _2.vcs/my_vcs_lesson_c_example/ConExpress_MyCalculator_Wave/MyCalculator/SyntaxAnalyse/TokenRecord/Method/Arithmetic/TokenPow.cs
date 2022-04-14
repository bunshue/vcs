using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenPow : TokenArithmeticMethod
    {
        public TokenPow(int Index, int Length)
            : base(Index, Length)
        { }

        public override void Execute()
        {
            this.CheckChildCount("������Ĳ������������Ϸ�");

            TokenRecord TokenFirst = this.ChildList[0];
            TokenRecord TokenSecond = this.ChildList[1];
            TokenFirst.Execute();
            TokenSecond.Execute();

            this.TokenValue = Math.Pow(TokenFirst.ChangeTokenToDouble("�����������Ԫ�ز�����ֵ"), TokenSecond.ChangeTokenToDouble("�����������Ԫ�ز�����ֵ"));
        }
    }
}
