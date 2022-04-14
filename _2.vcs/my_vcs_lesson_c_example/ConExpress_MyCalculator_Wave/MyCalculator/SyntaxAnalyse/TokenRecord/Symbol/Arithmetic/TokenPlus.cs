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
            this.CheckChildCount("�ӷ�������Ԫ���������Ϸ�");

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
                this.TokenValue = TokenFirst.ChangeTokenToDouble("�޷�ת��Ϊ���֡�") + TokenSecond.ChangeTokenToDouble("�޷�ת��Ϊ���֡�");
            }
        }
    }
}
