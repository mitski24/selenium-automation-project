from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_complete_flow(setup):
    driver = setup

    login = LoginPage(driver)
    login.open_site()

    # Invalid login
    login.login("invalid", "wrong")
    assert "do not match" in login.get_error()

    # Valid login
    login.open_site()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

    inventory = InventoryPage(driver)
    inventory.sort_low_to_high()
    inventory.add_two_items()
    assert inventory.cart_count() == "2"

    inventory.open_onesie()
    driver.find_element("id", "add-to-cart").click()
    assert inventory.cart_count() == "3"

    cart = CartPage(driver)
    cart.open_cart()
    cart.remove_item()
    assert inventory.cart_count() == "2"

    cart.checkout()

    checkout = CheckoutPage(driver)
    checkout.enter_details()
    print(checkout.get_total())
    checkout.finish_checkout()

    assert checkout.get_success_message() == "Thank you for your order!"

