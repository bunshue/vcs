using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public abstract class TokenStringMethod : TokenMethod
    {
        public TokenStringMethod(int Index, int Length)
            : base(Index, Length)
        {
            this.TokenValueType = typeof(string);
        }

        public abstract override void Execute();
    }
}
