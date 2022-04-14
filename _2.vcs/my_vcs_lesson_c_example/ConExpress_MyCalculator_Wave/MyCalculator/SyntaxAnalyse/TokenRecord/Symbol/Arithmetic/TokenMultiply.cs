using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenMultiply : TokenArithmeticSymbol
    {
        public TokenMultiply(int Index, int Length)
            : base(Index, Length)
        {
        }

        protected override void SetPriority()
        {
            this.m_Priority = 3;
        }

        public override void Execute()
        {
            this.CheckChildCount("�˷�������Ԫ���������Ϸ�");

            TokenRecord TokenFirst = this.ChildList[0];
            TokenRecord TokenSecond = this.ChildList[1];
            TokenFirst.Execute();
            TokenSecond.Execute();

            this.TokenValue = TokenFirst.ChangeTokenToDouble("�˷�������Ԫ�ز�����ֵ") * TokenSecond.ChangeTokenToDouble("�˷�������Ԫ�ز�����ֵ");
        }
    }
}
