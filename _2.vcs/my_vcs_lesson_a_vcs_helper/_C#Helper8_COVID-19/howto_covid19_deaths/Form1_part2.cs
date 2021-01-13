using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace howto_covid19_deaths
{
    public partial class Form1
    {
        private void LoadPopulationData()
        {
            Dictionary<string, int> population_dict =
                new Dictionary<string, int>();

            // Population data from https://www.worldometers.info/world-population/population-by-country/.
            population_dict.Add("China", 1439323776);
            population_dict.Add("India", 1380004385);
            population_dict.Add("US", 331002651);    // United States
            population_dict.Add("Indonesia", 273523615);
            population_dict.Add("Pakistan", 220892340);
            population_dict.Add("Brazil", 212559417);
            population_dict.Add("Nigeria", 206139589);
            population_dict.Add("Bangladesh", 164689383);
            population_dict.Add("Russia", 145934462);
            population_dict.Add("Mexico", 128932753);
            population_dict.Add("Japan", 126476461);
            population_dict.Add("Ethiopia", 114963588);
            population_dict.Add("Philippines", 109581078);
            population_dict.Add("Egypt", 102334404);
            population_dict.Add("Vietnam", 97338579);
            population_dict.Add("DR Congo", 89561403);
            population_dict.Add("Turkey", 84339067);
            population_dict.Add("Iran", 83992949);
            population_dict.Add("Germany", 83783942);
            population_dict.Add("Thailand", 69799978);
            population_dict.Add("United Kingdom", 67886011);
            population_dict.Add("France", 65273511);
            population_dict.Add("Italy", 60461826);
            population_dict.Add("Tanzania", 59734218);
            population_dict.Add("South Africa", 59308690);
            population_dict.Add("Burma", 54409800);  // Myanmar
            population_dict.Add("Kenya", 53771296);
            population_dict.Add("Korea, South", 51269185);   // South Korea
            population_dict.Add("Colombia", 50882891);
            population_dict.Add("Spain", 46754778);
            population_dict.Add("Uganda", 45741007);
            population_dict.Add("Argentina", 45195774);
            population_dict.Add("Algeria", 43851044);
            population_dict.Add("Sudan", 43849260);
            population_dict.Add("Ukraine", 43733762);
            population_dict.Add("Iraq", 40222493);
            population_dict.Add("Afghanistan", 38928346);
            population_dict.Add("Poland", 37846611);
            population_dict.Add("Canada", 37742154);
            population_dict.Add("Morocco", 36910560);
            population_dict.Add("Saudi Arabia", 34813871);
            population_dict.Add("Uzbekistan", 33469203);
            population_dict.Add("Peru", 32971854);
            population_dict.Add("Angola", 32866272);
            population_dict.Add("Malaysia", 32365999);
            population_dict.Add("Mozambique", 31255435);
            population_dict.Add("Ghana", 31072940);
            population_dict.Add("Yemen", 29825964);
            population_dict.Add("Nepal", 29136808);
            population_dict.Add("Venezuela", 28435940);
            population_dict.Add("Madagascar", 27691018);
            population_dict.Add("Cameroon", 26545863);
            population_dict.Add("Cote d'Ivoire", 26378274);  // Côte d'Ivoire
            population_dict.Add("North Korea", 25778816);
            population_dict.Add("Australia", 25499884);
            population_dict.Add("Niger", 24206644);
            population_dict.Add("Taiwan*", 23816775);    // Taiwan
            population_dict.Add("Sri Lanka", 21413249);
            population_dict.Add("Burkina Faso", 20903273);
            population_dict.Add("Mali", 20250833);
            population_dict.Add("Romania", 19237691);
            population_dict.Add("Malawi", 19129952);
            population_dict.Add("Chile", 19116201);
            population_dict.Add("Kazakhstan", 18776707);
            population_dict.Add("Zambia", 18383955);
            population_dict.Add("Guatemala", 17915568);
            population_dict.Add("Ecuador", 17643054);
            population_dict.Add("Syria", 17500658);
            population_dict.Add("Netherlands", 17134872);
            population_dict.Add("Senegal", 16743927);
            population_dict.Add("Cambodia", 16718965);
            population_dict.Add("Chad", 16425864);
            population_dict.Add("Somalia", 15893222);
            population_dict.Add("Zimbabwe", 14862924);
            population_dict.Add("Guinea", 13132795);
            population_dict.Add("Rwanda", 12952218);
            population_dict.Add("Benin", 12123200);
            population_dict.Add("Burundi", 11890784);
            population_dict.Add("Tunisia", 11818619);
            population_dict.Add("Bolivia", 11673021);
            population_dict.Add("Belgium", 11589623);
            population_dict.Add("Haiti", 11402528);
            population_dict.Add("Cuba", 11326616);
            population_dict.Add("South Sudan", 11193725);
            population_dict.Add("Dominican Republic", 10847910);
            population_dict.Add("Czechia", 10708981);    // Czech Republic (Czechia)
            population_dict.Add("Greece", 10423054);
            population_dict.Add("Jordan", 10203134);
            population_dict.Add("Portugal", 10196709);
            population_dict.Add("Azerbaijan", 10139177);
            population_dict.Add("Sweden", 10099265);
            population_dict.Add("Honduras", 9904607);
            population_dict.Add("United Arab Emirates", 9890402);
            population_dict.Add("Hungary", 9660351);
            population_dict.Add("Tajikistan", 9537645);
            population_dict.Add("Belarus", 9449323);
            population_dict.Add("Austria", 9006398);
            population_dict.Add("Papua New Guinea", 8947024);
            population_dict.Add("Serbia", 8737371);
            population_dict.Add("Israel", 8655535);
            population_dict.Add("Switzerland", 8654622);
            population_dict.Add("Togo", 8278724);
            population_dict.Add("Sierra Leone", 7976983);
            population_dict.Add("Hong Kong", 7496981);
            population_dict.Add("Laos", 7275560);
            population_dict.Add("Paraguay", 7132538);
            population_dict.Add("Bulgaria", 6948445);
            population_dict.Add("Libya", 6871292);
            population_dict.Add("Lebanon", 6825445);
            population_dict.Add("Nicaragua", 6624554);
            population_dict.Add("Kyrgyzstan", 6524195);
            population_dict.Add("El Salvador", 6486205);
            population_dict.Add("Turkmenistan", 6031200);
            population_dict.Add("Singapore", 5850342);
            population_dict.Add("Denmark", 5792202);
            population_dict.Add("Finland", 5540720);
            population_dict.Add("Congo", 5518087);
            population_dict.Add("Slovakia", 5459642);
            population_dict.Add("Norway", 5421241);
            population_dict.Add("Oman", 5106626);
            population_dict.Add("West Bank and Gaza", 5101414);  // State of Palestine
            population_dict.Add("Costa Rica", 5094118);
            population_dict.Add("Liberia", 5057681);
            population_dict.Add("Ireland", 4937786);
            population_dict.Add("Central African Republic", 4829767);
            population_dict.Add("New Zealand", 4822233);
            population_dict.Add("Mauritania", 4649658);
            population_dict.Add("Panama", 4314767);
            population_dict.Add("Kuwait", 4270571);
            population_dict.Add("Croatia", 4105267);
            population_dict.Add("Moldova", 4033963);
            population_dict.Add("Georgia", 3989167);
            population_dict.Add("Eritrea", 3546421);
            population_dict.Add("Uruguay", 3473730);
            population_dict.Add("Bosnia and Herzegovina", 3280819);
            population_dict.Add("Mongolia", 3278290);
            population_dict.Add("Armenia", 2963243);
            population_dict.Add("Jamaica", 2961167);
            population_dict.Add("Qatar", 2881053);
            population_dict.Add("Albania", 2877797);
            population_dict.Add("Puerto Rico", 2860853);
            population_dict.Add("Lithuania", 2722289);
            population_dict.Add("Namibia", 2540905);
            population_dict.Add("Gambia", 2416668);
            population_dict.Add("Botswana", 2351627);
            population_dict.Add("Gabon", 2225734);
            population_dict.Add("Lesotho", 2142249);
            population_dict.Add("North Macedonia", 2083374);
            population_dict.Add("Slovenia", 2078938);
            population_dict.Add("Guinea-Bissau", 1968001);
            population_dict.Add("Latvia", 1886198);
            population_dict.Add("Bahrain", 1701575);
            population_dict.Add("Equatorial Guinea", 1402985);
            population_dict.Add("Trinidad and Tobago", 1399488);
            population_dict.Add("Estonia", 1326535);
            population_dict.Add("Timor-Leste", 1318445);
            population_dict.Add("Mauritius", 1271768);
            population_dict.Add("Cyprus", 1207359);
            population_dict.Add("Eswatini", 1160164);
            population_dict.Add("Djibouti", 988000);
            population_dict.Add("Fiji", 896445);
            population_dict.Add("Réunion", 895312);
            population_dict.Add("Comoros", 869601);
            population_dict.Add("Guyana", 786552);
            population_dict.Add("Bhutan", 771608);
            population_dict.Add("Solomon Islands", 686884);
            population_dict.Add("Macao", 649335);
            population_dict.Add("Montenegro", 628066);
            population_dict.Add("Luxembourg", 625978);
            population_dict.Add("Western Sahara", 597339);
            population_dict.Add("Suriname", 586632);
            population_dict.Add("Cabo Verde", 555987);
            population_dict.Add("Maldives", 540544);
            population_dict.Add("Malta", 441543);
            population_dict.Add("Brunei", 437479);
            population_dict.Add("Guadeloupe", 400124);
            population_dict.Add("Belize", 397628);
            population_dict.Add("Bahamas", 393244);
            population_dict.Add("Martinique", 375265);
            population_dict.Add("Iceland", 341243);
            population_dict.Add("Vanuatu", 307145);
            population_dict.Add("French Guiana", 298682);
            population_dict.Add("Barbados", 287375);
            population_dict.Add("New Caledonia", 285498);
            population_dict.Add("French Polynesia", 280908);
            population_dict.Add("Mayotte", 272815);
            population_dict.Add("Sao Tome & Principe", 219159);
            population_dict.Add("Samoa", 198414);
            population_dict.Add("Saint Lucia", 183627);
            population_dict.Add("Channel Islands", 173863);
            population_dict.Add("Guam", 168775);
            population_dict.Add("Curaçao", 164093);
            population_dict.Add("Kiribati", 119449);
            population_dict.Add("Micronesia", 115023);
            population_dict.Add("Grenada", 112523);
            population_dict.Add("Saint Vincent and the Grenadines", 110940); // St. Vincent & Grenadines
            population_dict.Add("Aruba", 106766);
            population_dict.Add("Tonga", 105695);
            population_dict.Add("U.S. Virgin Islands", 104425);
            population_dict.Add("Seychelles", 98347);
            population_dict.Add("Antigua and Barbuda", 97929);
            population_dict.Add("Isle of Man", 85033);
            population_dict.Add("Andorra", 77265);
            population_dict.Add("Dominica", 71986);
            population_dict.Add("Cayman Islands", 65722);
            population_dict.Add("Bermuda", 62278);
            population_dict.Add("Marshall Islands", 59190);
            population_dict.Add("Northern Mariana Islands", 57559);
            population_dict.Add("Greenland", 56770);
            population_dict.Add("American Samoa", 55191);
            population_dict.Add("Saint Kitts and Nevis", 53199); // Saint Kitts & Nevis
            population_dict.Add("Faeroe Islands", 48863);
            population_dict.Add("Sint Maarten", 42876);
            population_dict.Add("Monaco", 39242);
            population_dict.Add("Turks and Caicos", 38717);
            population_dict.Add("Saint Martin", 38666);
            population_dict.Add("Liechtenstein", 38128);
            population_dict.Add("San Marino", 33931);
            population_dict.Add("Gibraltar", 33691);
            population_dict.Add("British Virgin Islands", 30231);
            population_dict.Add("Caribbean Netherlands", 26223);
            population_dict.Add("Palau", 18094);
            population_dict.Add("Cook Islands", 17564);
            population_dict.Add("Anguilla", 15003);
            population_dict.Add("Tuvalu", 11792);
            population_dict.Add("Wallis & Futuna", 11239);
            population_dict.Add("Nauru", 10824);
            population_dict.Add("Saint Barthelemy", 9877);
            population_dict.Add("Saint Helena", 6077);
            population_dict.Add("Saint Pierre & Miquelon", 5794);
            population_dict.Add("Montserrat", 4992);
            population_dict.Add("Falkland Islands", 3480);
            population_dict.Add("Niue", 1626);
            population_dict.Add("Tokelau", 1357);
            population_dict.Add("Holy See", 801);

            // Add the population data to the country data.
            Console.WriteLine("No population data for these countries:");
            foreach (CountryData country in CountryList)
            {
                if (population_dict.ContainsKey(country.Name))
                    country.Population = population_dict[country.Name];
                else
                    Console.WriteLine(country.Name);
            }

            // Calculate cases per million.
            // You could do this only when needed.
            // I'm using extra memory so we don't need
            // to do it later.
            foreach (CountryData country in CountryList)
            {
                country.CalculateCasesPerMillion();
                country.CalculateDeathsPerMillion();
            }
        }
    }
}
