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
            this.TokenValueType = typeof(double);//部分操作符必须根据实际修改
        }

        protected override void SetChildCount()
        {
            this.m_ChildCount = 2;//必须根据实际修改
        }

        public abstract override void Execute();
    }
}