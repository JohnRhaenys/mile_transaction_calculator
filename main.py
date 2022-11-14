from menu_handler import display_filter_menu, get_user_filter_option, display_livelo_points_menu, \
    get_livelo_points_price
from profit_calculator import get_profitable_transactions
import json


def main():
    display_livelo_points_menu()
    livelo_points_price = get_livelo_points_price()
    if livelo_points_price is None:
        print('Invalid price!')
        return
    display_filter_menu()
    user_option = get_user_filter_option()
    if user_option is None:
        print('That option is not valid!')
        return
    with open(user_option.get('filename'), 'w') as fp:
        json.dump(get_profitable_transactions(livelo_points_price, user_option.get('filter_params')), fp, indent=4)


if __name__ == '__main__':
    main()
