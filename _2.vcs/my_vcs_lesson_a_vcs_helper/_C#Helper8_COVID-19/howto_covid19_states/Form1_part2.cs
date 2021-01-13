using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace howto_covid19_states
{
    public partial class Form1
    {
        private void LoadPopulationData()
        {
            Dictionary<string, long> population_dict =
                new Dictionary<string, long>();

            // Population data from https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population.
            population_dict.Add("AK", 731545);
            population_dict.Add("AL", 4903185);
            population_dict.Add("AR", 3017825);
            population_dict.Add("AS", 55641);
            population_dict.Add("AZ", 7278717);
            population_dict.Add("CA", 39512223);
            population_dict.Add("CO", 5758736);
            population_dict.Add("CT", 3565287);
            population_dict.Add("DC", 705749);
            population_dict.Add("DE", 973764);
            population_dict.Add("FL", 21477737);
            population_dict.Add("GA", 10617423);
            population_dict.Add("GU", 165718);
            population_dict.Add("HI", 1415872);
            population_dict.Add("IA", 3155070);
            population_dict.Add("ID", 1787065);
            population_dict.Add("IL", 12671821);
            population_dict.Add("IN", 6732219);
            population_dict.Add("KS", 2913314);
            population_dict.Add("KY", 4467673);
            population_dict.Add("LA", 4648794);
            population_dict.Add("MA", 6949503);
            population_dict.Add("MD", 6045680);
            population_dict.Add("ME", 1344212);
            population_dict.Add("MI", 9986857);
            population_dict.Add("MN", 5639632);
            population_dict.Add("MO", 6137428);
            population_dict.Add("MP", 55194);
            population_dict.Add("MS", 2976149);
            population_dict.Add("MT", 1068778);
            population_dict.Add("NC", 10488084);
            population_dict.Add("ND", 762062);
            population_dict.Add("NE", 1934408);
            population_dict.Add("NH", 1359711);
            population_dict.Add("NJ", 8882190);
            population_dict.Add("NM", 2096829);
            population_dict.Add("NV", 3080156);
            population_dict.Add("NY", 19453561);
            population_dict.Add("OH", 11689100);
            population_dict.Add("OK", 3956971);
            population_dict.Add("OR", 4217737);
            population_dict.Add("PA", 12801989);
            population_dict.Add("PR", 3193694);
            population_dict.Add("RI", 1059361);
            population_dict.Add("SC", 5148714);
            population_dict.Add("SD", 884659);
            population_dict.Add("TN", 6833174);
            population_dict.Add("TX", 28995881);
            population_dict.Add("UT", 3205958);
            population_dict.Add("VA", 8535519);
            population_dict.Add("VI", 104914);
            population_dict.Add("VT", 623989);
            population_dict.Add("WA", 7614893);
            population_dict.Add("WI", 5822434);
            population_dict.Add("WV", 1792147);
            population_dict.Add("WY", 578759);

            // Get the state population.
            long all_pop = 0;
            foreach (int value in population_dict.Values)
            {
                all_pop += value;
            }
            population_dict.Add("ALL STATES", all_pop);

            // Add the population data to the state data.
            Console.WriteLine("No population data for these states:");
            foreach (StateData state in StateList)
            {
                if (population_dict.ContainsKey(state.Name))
                    state.Population = population_dict[state.Name];
                else
                    Console.WriteLine(state.Name);
            }
        }
    }
}
