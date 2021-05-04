using System;
using System.Collections.Generic;
using System.Text;
using System.EnterpriseServices;

namespace CallClass
{
    [Transaction(TransactionOption.RequiresNew)]
    [ObjectPooling(true, 1, 100)]

    public class ComDLL:ServicedComponent
    {
        public bool insert(string name, string sex, string age, string address)
        {
            try
            {
                DataBaseDAO dao = new DataBaseDAO();
                dao.UserAccount_Inert(name, sex, age, address);
                return true;
            }
            catch (Exception e)
            {
                return false;
            }
        }
    }
}
