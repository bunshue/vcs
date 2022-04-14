using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public abstract class TokenArithmeticSymbol : TokenSymbol
    {
        public TokenArithmeticSymbol(int Index, int Length)
            : base(Index, Length)
        {
        }

        public abstract override void Execute();
    }
}
