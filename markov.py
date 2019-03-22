import numpy as np

def normalize(xs):
    total = sum(xs.values())
    return {key: value / total for key, value in xs.items()}


def build_transitions(text):
    #text = text.lower()

    # Build up counts
    prev_c = text[0]
    counts = {}
    for curr_c in text[1:]:
        c_next_counts         =        counts.get(prev_c, dict())
        c_next_counts[curr_c] = c_next_counts.get(curr_c, 0) + 1
        counts[prev_c]        = c_next_counts

        prev_c = curr_c


    probabilities = {letter: normalize(next_counts) for letter, next_counts in counts.items()}
    return probabilities

def gen_next_character(transitions, start = ""):
    state_list = [k for k in transitions]
    state = np.random.choice(state_list, 1)[0]

    stop_chars = [".", "!", "?"]

    count = 0
    while True:
        yield state

        # Do some prep
        next_probs = [(l, p) for l, p in transitions.get(state, dict()).items()]

        # Stop if we're done, or 
        count += 1
        if count > 100 or state in stop_chars or len(next_probs) == 0:
            break

        state_list, prob_list = zip(*next_probs)
        state = np.random.choice(state_list, size = 1, p = prob_list)[0]




text = """
Economic activity in Mongolia has traditionally been based on agriculture and livestock. Mongolia also has extensive mineral deposits: copper, coal, molybdenum, tin, tungsten, and gold account for a large part of industrial production. Soviet assistance, at its height one-third of Gross domestic product (GDP), disappeared almost overnight in 1990–91, at the time of the Collapse of the Soviet Union. Mongolia was driven into deep recession. Reform has been held back by the ex-communist MPRP opposition and by the political instability brought about through four successive governments under the DUC. Economic growth picked up in 1997–99 after stalling in 1996 due to a series of natural disasters and increases in world prices of copper and cashmere. Public revenues and exports collapsed in 1998 and 1999 due to the repercussions of the Asian financial crisis. In August and September 1999, the economy suffered from a temporary Russian ban on exports of oil and oil products. Mongolia joined the World Trade Organization (WTO) in 1997. The international donor community pledged over $300 million per year at the last Consultative Group Meeting, held in Ulaanbaatar in June 1999. Recently, the Mongolian economy has grown at a fast pace due to an increase in mining and Mongolia attained a GDP growth rate of 11.7% in 2013. However, because much of this growth is export-based, Mongolia is suffering from the global slowdown in mining caused by decreased growth in China.

The rapid political changes of 1990–91 marked the beginning of Mongolia's efforts to develop a market economy, but these efforts have been complicated and disrupted by the dissolution and continuing deterioration of the economy of the former Soviet Union. Prior to 1991, 80% of Mongolia's trade was with the former Soviet Union, and 15% was with other Council for Mutual Economic Assistance (CMEA) countries. Mongolia was heavily dependent upon the former Soviet Union for fuel, medicine, and spare parts for its factories and power plants.

The former Soviet Union served as the primary market for Mongolian industry. In the 1980s, Mongolia's industrial sector became increasingly important. By 1989, it accounted for an estimated 34% of material products, compared to 18% from agriculture. However, minerals, animals, and animal-derived products still constitute a large proportion of the country's exports. Principal imports included machinery, petroleum, cloth, and building materials.

In the late 1980s, the government began to improve links with non-communist Asia and the West, and tourism in Mongolia developed. As of 1 January 1991, Mongolia and the former Soviet Union agreed to conduct bilateral trade in hard currency at world prices.

Despite its external trade difficulties, Mongolia has continued to press ahead with reform. Privatization of small shops and enterprises has largely been completed in the 1990s, and most prices have been freed. Privatization of large state enterprises has begun. Tax reforms also have begun, and the barter and official exchange rates were unified in late 1991.
"""

trans_ps = build_transitions(text)

for i in range(10):
    generated_str = ''.join([letter for letter in gen_next_character(trans_ps)])
    print(generated_str)
    print
