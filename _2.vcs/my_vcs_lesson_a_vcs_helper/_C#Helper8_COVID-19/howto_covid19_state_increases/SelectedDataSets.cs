using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;

namespace howto_covid19_state_increases
{
    public struct SelectedDataSets
    {
        public static bool PerMillion = false;
        public static bool Positive = false;
        public static bool Negative = false;
        public static bool Pending = false;
        public static bool HospitalizedNow = false;
        public static bool HospitalizedTotal = false;
        public static bool IcuNow = false;
        public static bool IcuTotal = false;
        public static bool VentNow = false;
        public static bool VentTotal = false;
        public static bool Recovered = false;
        public static bool Deaths = false;
        public static bool DeathsPerResolution = false;
        public static bool PositiveIncrease = false;
        public static bool HospitalizedIncrease = false;
        public static bool DeathsIncrease = false;

        public static bool DataSetsAreSelected = false;

        public static void SetSelectedDataSets(Form1 form1)
        {
            PerMillion = form1.chkPerMillion.Checked;
            Positive = form1.chkTotalPositive.Checked;
            Negative = form1.chkTotalNegative.Checked;
            Pending = form1.chkPending.Checked;
            HospitalizedNow = form1.chkHospitalizedNow.Checked;
            HospitalizedTotal = form1.chkHospitalizedTotal.Checked;
            IcuNow = form1.chkIcuNow.Checked;
            IcuTotal = form1.chkIcuTotal.Checked;
            VentNow = form1.chkVentNow.Checked;
            VentTotal = form1.chkVentTotal.Checked;
            Recovered = form1.chkRecovered.Checked;
            Deaths = form1.chkDeaths.Checked;
            DeathsPerResolution = form1.chkDeathsPerResolution.Checked;
            PositiveIncrease = form1.chkPositiveIncrease.Checked;
            HospitalizedIncrease = form1.chkHospitalizedIncrease.Checked;
            DeathsIncrease = form1.chkDeathsIncrease.Checked;

            DataSetsAreSelected =
                Positive ||
                Negative ||
                Pending ||
                HospitalizedNow ||
                HospitalizedTotal ||
                IcuNow ||
                IcuTotal ||
                VentNow ||
                VentTotal ||
                Recovered ||
                Deaths ||
                DeathsPerResolution ||
                PositiveIncrease ||
                HospitalizedIncrease ||
                DeathsIncrease;
        }
    }
}
