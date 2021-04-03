import sys
import argparse

# Total Overall Signal Importance Calculator for MoniGoMani v0.8.0
# ----------------------------------------------------------------
# Paste the results from your HyperOpt over below `buy_params` & `sell_params` arrays
# Then execute: `python ./user_data/Total-Overall-Signal-Importance-Calculator.py` from your favorite
# terminal / CLI to calculate the overall importance of the signals being used.
# The higher the score of a signal the better

########################################################################################################################
#                                  START OF HYPEROPT BUY/SELL RESULTS COPY-PASTE SECTION                               #
########################################################################################################################

# Buy hyperspace params:
buy_params = {
    'buy___trades_when_downwards': True,
    'buy___trades_when_sideways': False,
    'buy___trades_when_upwards': True,
    'buy__downwards_trend_total_signal_needed': 2,
    'buy__sideways_trend_total_signal_needed': 29,
    'buy__upwards_trend_total_signal_needed': 19,
    'buy_downwards_trend_adx_strong_up_weight': 76,
    'buy_downwards_trend_bollinger_bands_weight': 94,
    'buy_downwards_trend_ema_long_golden_cross_weight': 55,
    'buy_downwards_trend_ema_short_golden_cross_weight': 32,
    'buy_downwards_trend_macd_weight': 18,
    'buy_downwards_trend_rsi_weight': 94,
    'buy_downwards_trend_sma_long_golden_cross_weight': 69,
    'buy_downwards_trend_sma_short_golden_cross_weight': 81,
    'buy_downwards_trend_vwap_cross_weight': 41,
    'buy_sideways_trend_adx_strong_up_weight': 15,
    'buy_sideways_trend_bollinger_bands_weight': 53,
    'buy_sideways_trend_ema_long_golden_cross_weight': 83,
    'buy_sideways_trend_ema_short_golden_cross_weight': 85,
    'buy_sideways_trend_macd_weight': 40,
    'buy_sideways_trend_rsi_weight': 1,
    'buy_sideways_trend_sma_long_golden_cross_weight': 80,
    'buy_sideways_trend_sma_short_golden_cross_weight': 63,
    'buy_sideways_trend_vwap_cross_weight': 65,
    'buy_upwards_trend_adx_strong_up_weight': 18,
    'buy_upwards_trend_bollinger_bands_weight': 61,
    'buy_upwards_trend_ema_long_golden_cross_weight': 18,
    'buy_upwards_trend_ema_short_golden_cross_weight': 81,
    'buy_upwards_trend_macd_weight': 48,
    'buy_upwards_trend_rsi_weight': 94,
    'buy_upwards_trend_sma_long_golden_cross_weight': 70,
    'buy_upwards_trend_sma_short_golden_cross_weight': 99,
    'buy_upwards_trend_vwap_cross_weight': 31
}
# Sell hyperspace params:
sell_params = {
    'sell___trades_when_downwards': False,
    'sell___trades_when_sideways': True,
    'sell___trades_when_upwards': True,
    'sell__downwards_trend_total_signal_needed': 11,
    'sell__sideways_trend_total_signal_needed': 41,
    'sell__upwards_trend_total_signal_needed': 87,
    'sell_downwards_trend_adx_strong_down_weight': 33,
    'sell_downwards_trend_bollinger_bands_weight': 21,
    'sell_downwards_trend_ema_long_death_cross_weight': 92,
    'sell_downwards_trend_ema_short_death_cross_weight': 96,
    'sell_downwards_trend_macd_weight': 1,
    'sell_downwards_trend_rsi_weight': 20,
    'sell_downwards_trend_sma_long_death_cross_weight': 62,
    'sell_downwards_trend_sma_short_death_cross_weight': 30,
    'sell_downwards_trend_vwap_cross_weight': 73,
    'sell_sideways_trend_adx_strong_down_weight': 43,
    'sell_sideways_trend_bollinger_bands_weight': 76,
    'sell_sideways_trend_ema_long_death_cross_weight': 72,
    'sell_sideways_trend_ema_short_death_cross_weight': 44,
    'sell_sideways_trend_macd_weight': 21,
    'sell_sideways_trend_rsi_weight': 24,
    'sell_sideways_trend_sma_long_death_cross_weight': 27,
    'sell_sideways_trend_sma_short_death_cross_weight': 86,
    'sell_sideways_trend_vwap_cross_weight': 60,
    'sell_upwards_trend_adx_strong_down_weight': 56,
    'sell_upwards_trend_bollinger_bands_weight': 1,
    'sell_upwards_trend_ema_long_death_cross_weight': 80,
    'sell_upwards_trend_ema_short_death_cross_weight': 72,
    'sell_upwards_trend_macd_weight': 46,
    'sell_upwards_trend_rsi_weight': 8,
    'sell_upwards_trend_sma_long_death_cross_weight': 18,
    'sell_upwards_trend_sma_short_death_cross_weight': 83,
    'sell_upwards_trend_vwap_cross_weight': 10
}


########################################################################################################################
#                                   END OF HYPEROPT BUY/SELL RESULTS COPY-PASTE SECTION                                #
########################################################################################################################
class FileAndConsoleLogger(object):
    def __init__(self, *files):
        self.files = files

    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()  # If you want the output to be visible immediately

    def flush(self):
        for f in self.files:
            f.flush()


def print_spacer():
    print("--------------------------------------------------------------------")


def print_section_header(header, whitespace=True):
    if whitespace:
        print("")
    print(header)
    print_spacer()


initial_offset = 40
signal_format = '{:<35s}{:>6s}'
full_signal_format = '{:<35s}{:>6s} | {:>6s} | {:>6s} | {:>6s}'


def print_signal(signal, importance):
    print(signal_format.format(str(signal) + ":", str(round(importance, 2)) + "%"))


def print_full_signal_header():
    print(full_signal_format.format("", "avg", "down", "side", "up"))


def print_full_buy_signal(signal, importance):
    print(full_signal_format.format(str(signal) + ":",
                                    str(round(importance, 2)) + "%",
                                    str(round(buy_params["buy_downwards_trend_" + signal + "_weight"], 2)) + "%",
                                    str(round(buy_params["buy_sideways_trend_" + signal + "_weight"], 2)) + "%",
                                    str(round(buy_params["buy_upwards_trend_" + signal + "_weight"], 2)) + "%"))


def print_full_sell_signal(signal, importance):
    print(full_signal_format.format(str(signal) + ":",
                                    str(round(importance, 2)) + "%",
                                    str(round(sell_params["sell_downwards_trend_" + signal + "_weight"], 2)) + "%",
                                    str(round(sell_params["sell_sideways_trend_" + signal + "_weight"], 2)) + "%",
                                    str(round(sell_params["sell_upwards_trend_" + signal + "_weight"], 2)) + "%"))


def print_full_avg_signal(signal, importance, avg_weights):
    print(full_signal_format.format(str(signal) + ":",
                                    str(round(importance, 2)) + "%",
                                    str(round(avg_weights["avg_downwards_trend_" + signal + "_weight"], 2)) + "%",
                                    str(round(avg_weights["avg_sideways_trend_" + signal + "_weight"], 2)) + "%",
                                    str(round(avg_weights["avg_upwards_trend_" + signal + "_weight"], 2)) + "%"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-sc', '--stake-currency', dest='stake_currency', type=str, required=True,
                        help='Stake currency used when generating these settings')
    parser.add_argument('-f', '--file', dest='file', type=str, default='importance.log',
                        help='Filename to save result to')
    parser.add_argument('-nf', '--no-file', dest='output_to_file', const=False, default=True, nargs='?',
                        help='Do not output to a file')
    args = parser.parse_args()

    trend_names = ['downwards', 'sideways', 'upwards']
    buy_indicator_names = [
        'adx_strong_up',
        'bollinger_bands',
        'ema_long_golden_cross',
        'ema_short_golden_cross',
        'macd',
        'rsi',
        'sma_long_golden_cross',
        'sma_short_golden_cross',
        'vwap_cross',
    ]

    sell_indicator_names = [
        'adx_strong_down',
        'bollinger_bands',
        'ema_long_death_cross',
        'ema_short_death_cross',
        'macd',
        'rsi',
        'sma_long_death_cross',
        'sma_short_death_cross',
        'vwap_cross',
    ]

    combined_indicator_names = {
        'adx_strong_up_down': ['adx_strong_up', 'adx_strong_down'],
        'bollinger_bands': ['bollinger_bands'],
        'ema_long_golden_death_cross': ['ema_long_golden_cross', 'ema_long_death_cross'],
        'ema_short_golden_death_cross': ['ema_short_golden_cross', 'ema_short_death_cross'],
        'macd': ['macd'],
        'rsi': ['rsi'],
        'sma_long_golden_death_cross': ['sma_long_golden_cross', 'sma_long_death_cross'],
        'sma_short_golden_death_cross': ['sma_short_golden_cross', 'sma_short_death_cross'],
        'vwap_cross': ['vwap_cross']
    }

    total_overall_buy_weights = {}
    total_overall_sell_weights = {}
    total_overall_weights = {}
    avg_trend_weights = {}

    for indicator in buy_indicator_names:
        buy_weight = 0
        for trend in trend_names:
            buy_weight += buy_params["buy_" + trend + "_trend_" + indicator + "_weight"]
        total_overall_buy_weights[indicator] = buy_weight / len(trend_names)
    for indicator in sell_indicator_names:
        sell_weight = 0
        for trend in trend_names:
            sell_weight += sell_params["sell_" + trend + "_trend_" + indicator + "_weight"]
        total_overall_sell_weights[indicator] = sell_weight / len(trend_names)
    for combined_indicator in combined_indicator_names.keys():
        indicators = combined_indicator_names[combined_indicator]

        for trend in trend_names:
            avg_weight = (buy_params["buy_" + trend + "_trend_" + indicators[0] + "_weight"] +
                          sell_params["sell_" + trend + "_trend_" + indicators[-1] + "_weight"]) / 2
            avg_trend_weights["avg_" + trend + "_trend_" + combined_indicator + "_weight"] = avg_weight

        total_overall_weights[combined_indicator] = (total_overall_buy_weights[indicators[0]] +
                                                     total_overall_sell_weights[indicators[-1]]) / 2

    # to output our prints to a file redirect the stdout
    original_stdout = sys.stdout
    f = {}

    if args.output_to_file:
        f = open(args.file, 'w')
        sys.stdout = FileAndConsoleLogger(sys.stdout, f)

    print_section_header("Signal importance report", False)
    print(signal_format.format('Stake currency' + ":", args.stake_currency))

    print_section_header("Total Overall Signal Importance:")
    print_full_signal_header()
    for signal, importance in total_overall_weights.items():
        print_full_avg_signal(signal, importance, avg_trend_weights)

    print_section_header("Total Overall Buy Signal Importance:")
    print_full_signal_header()
    for signal, importance in total_overall_buy_weights.items():
        print_full_buy_signal(signal, importance)

    print_section_header("Total Overall Sell Signal Importance:")
    print_full_signal_header()
    for signal, importance in total_overall_sell_weights.items():
        print_full_sell_signal(signal, importance)

    if args.output_to_file:
        f.close()
        sys.stdout = original_stdout


if __name__ == "__main__":
    main()