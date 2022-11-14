LIVELO_POINTS_MENU_TITLE = 'PRICE PAID FOR 1000 LIVELO POINTS'
FILTER_MENU_TITLE = 'TRANSACTION CALCULATOR'
MAX_LIVELO_POINTS_PRICE = 70.00


def display_livelo_points_menu():
    print(f'\t{LIVELO_POINTS_MENU_TITLE}\t')
    print('=' * (8 + len(LIVELO_POINTS_MENU_TITLE)))
    print(f'How much are you paying for 1000 Livelo Points?')


def get_livelo_points_price():
    price = float(input())
    return price if 0 < price <= MAX_LIVELO_POINTS_PRICE else None


FILTER_OPTIONS = [
    {
        'PROFIT (MOST TO LEAST)': {
            'filter_params': {
                'key': 'total_profit',
                'reversed': True
            },
            'filename': 'profitable_most_to_least.json'
        }
    },
    {
        'TOTAL INVESTED (HIGHEST TO LOWEST)': {
            'filter_params': {
                'key': 'total_money_invested',
                'reversed': True
            },
            'filename': 'total_invested_highest_to_lowest.json'
        },
    },
    {
        'PROFIT (LEAST TO MOST)': {
            'filter_params': {
                'key': 'total_profit',
                'reversed': False
            },
            'filename': 'profitable_least_to_most.json'
        },
    },
    {
        'TOTAL INVESTED (LOWEST TO HIGHEST)': {
            'filter_params': {
                'key': 'total_money_invested',
                'reversed': False
            },
            'filename': 'total_invested_lowest_to_highest.json'
        }
    }
]


def display_filter_menu():
    print(f'\t{FILTER_MENU_TITLE}\t')
    print('=' * (8 + len(FILTER_MENU_TITLE)))
    print(f'How would you like to filter the results?')
    for index, option in enumerate(FILTER_OPTIONS):
        print(f'[{index}]: {list(option.keys())[0]}')


def get_user_filter_option():
    chosen_option = int(input())
    return list(FILTER_OPTIONS[chosen_option].values())[0] if 0 <= chosen_option < len(FILTER_OPTIONS) else None
