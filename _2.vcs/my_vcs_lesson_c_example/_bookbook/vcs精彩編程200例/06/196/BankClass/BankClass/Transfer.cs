using System;
using System.Collections.Generic;
using System.Text;
using System.EnterpriseServices;


namespace BankClass
{
    [Transaction(TransactionOption.RequiresNew)]
    [ObjectPooling(true, 1, 100)]

    public class Transfer : ServicedComponent
    {
        public bool BankTransfer(string FromBank, string FromAccount, string ToBank,string ToAccount, float balance)
        {
            Account fromAccount = new BankClass.Account();
            Account toAccount = new BankClass.Account();
            try
            {
                toAccount.Saveing(ToBank, balance, ToAccount);
                fromAccount.Fetch(FromBank, balance, FromAccount);
                ContextUtil.SetComplete();
                toAccount.WriteError("From Bank��" + FromAccount + " TO Bank��" + toAccount + "ת�ʳɹ�");
                return true;
            }
            catch(System.Exception ex)
            {
                ContextUtil.SetAbort();
                toAccount.WriteError("From Bank��" + FromAccount + " TO Bank��" + toAccount + "ת��ʧ��"+ex.Message);
                return false;
            }
        }
    }
}
