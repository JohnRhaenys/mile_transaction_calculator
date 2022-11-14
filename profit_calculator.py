from web_scraper import get_prices_per_program

MINIMUM_BONUS_PERCENTAGE = 30
MAXIMUM_BONUS_PERCENTAGE = 100
BONUS_PERCENTAGE_STEP = 5
MINIMUM_NUMBER_OF_POINTS = 5_000
MAXIMUM_NUMBER_OF_POINTS = 500_000
POINT_STEP = 10_000


def get_all_possible_transactions(livelo_points_price):
    transactions = []
    for bonus in range(MINIMUM_BONUS_PERCENTAGE, MAXIMUM_BONUS_PERCENTAGE + 1, BONUS_PERCENTAGE_STEP):
        multiplier = 1 + (1 * bonus / 100)
        for current_points in range(MINIMUM_NUMBER_OF_POINTS, MAXIMUM_NUMBER_OF_POINTS + 1, POINT_STEP):
            total_invested = (current_points * livelo_points_price) / 1_000
            total_points_acquired = int(current_points * multiplier)
            price_paid_for_a_thousand_miles = round(((total_invested * 1000) / total_points_acquired), 2)
            transaction = {
                'multiplier': multiplier,
                'total_points_bought': current_points,
                'total_money_invested': total_invested,
                'total_miles_acquired_after_bonus_transaction': total_points_acquired,
                'price_paid_for_a_thousand_miles': price_paid_for_a_thousand_miles
            }
            transactions.append(transaction)
    return transactions


def get_thousand_miles_sale_price(transaction, program_price_ranges):
    for price_range, price in program_price_ranges.items():
        if transaction.get('total_miles_acquired_after_bonus_transaction') in price_range:
            return price
    return None


def get_profitable_transactions(livelo_price, filter_params):
    profitable_transactions = []
    prices_per_program = get_prices_per_program()
    for transaction in get_all_possible_transactions(livelo_price):
        for program in prices_per_program:
            thousand_miles_sale_price = get_thousand_miles_sale_price(transaction, prices_per_program.get(program))
            if thousand_miles_sale_price is not None:
                if transaction.get('price_paid_for_a_thousand_miles') < thousand_miles_sale_price:
                    transaction['program'] = program
                    transaction['sale_price'] = thousand_miles_sale_price

                    profit_per_thousand_miles = \
                        thousand_miles_sale_price - transaction.get('price_paid_for_a_thousand_miles')
                    transaction['profit_per_thousand_miles'] = round(profit_per_thousand_miles, 2)

                    total_profit = \
                        profit_per_thousand_miles * transaction.get('total_miles_acquired_after_bonus_transaction')
                    transaction['total_profit'] = round((total_profit / 1000), 2)

                    total_received_for_all_miles_sold = \
                        thousand_miles_sale_price * transaction.get('total_miles_acquired_after_bonus_transaction')
                    transaction['total_received_for_all_miles_sold'] = round((total_received_for_all_miles_sold / 1000), 2)

                    transaction['livelo_price_per_thousand_points'] = livelo_price

                    profitable_transactions.append(transaction)

    profitable_transactions.sort(key=lambda t: t.get(filter_params.get('key')), reverse=filter_params.get('reversed'))

    return profitable_transactions
