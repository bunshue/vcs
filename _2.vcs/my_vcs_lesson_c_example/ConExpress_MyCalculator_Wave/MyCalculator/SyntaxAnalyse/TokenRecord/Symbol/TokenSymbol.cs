using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public abstract class TokenSymbol : TokenRecord
    {
        public TokenSymbol(int Index, int Length)
            : base(Index, Length)
        {
            this.TokenValueType = typeof(double);//���ֲ������������ʵ���޸�
        }

        protected override void SetChildCount()
        {
            this.m_ChildCount = 2;//�������ʵ���޸�
        }

        public abstract override void Execute();
    }
}