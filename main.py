import data  # Task 3: Import test data
import helpers  # Task 4: Import helper functions for server check

class TestUrbanRoutes:

    # Task 4: Setup class to check server connection before running tests
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    # Task 3: Create empty test functions to be implemented in Sprint 8

    def test_set_route(self):
        # Add in S8
        print("function created for set route")
        pass

    def test_select_plan(self):
        # Add in S8
        print("function created for select plan")
        pass

    def test_fill_phone_number(self):
        # Add in S8
        print("function created for fill phone number")
        pass

    def test_fill_card(self):
        # Add in S8
        print("function created for fill card")
        pass

    def test_comment_for_driver(self):
        # Add in S8
        print("function created for comment for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("function created for order blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        # Task 5: Set up loop to prepare for ice cream order logic
        for _ in range(2):
            # Add in S8
            pass
        print("function created for order 2 ice creams")

    def test_car_search_model_appears(self):
        # Add in S8
        print("function created for car search model appears")
        pass