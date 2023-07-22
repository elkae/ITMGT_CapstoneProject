# ITMGT_CapstoneProject
ITMGT Project (Taylor's Version)

Instructions on How to Run the Project:

    1. Open the directory on a terminal.
    
    2. Install Django in your path.
    
    3. To start the Django server input: python manage.py runserver
    
    4. Once the server starts, you will see an output with the link. Follow the link into your web browser. It will lead you to the main page where you will see the six products available.

Logging in as a superuser:

    1. Copy the link of the homepage in your web browser and append “admin/” to the end of the link.
    
    2. This will lead you to a log-in interface of django admin.
    
    3. Input these to log-in as a superuser (can access as a customer and as an admin):
        Username: Elle
        Password: itmgt2503
        
    4. Refresh the homepage.

Project Features:

Navbar Features:

    1. You can click “Papers and Pens” and “Store” to return to the mainpage
    
    2. Once you click the search bar, it allows you to perform searches for products depending on your product query.
    
    3. Upon clicking on the “Search” button the website will display relevant products matching your search query.
    
    4. Unfortunately, the login button does not work, since we prioritized the add-to-cart and checkout functions.

Homepage/Mainpage Features:

    1. When you click “Add” on any of the products, the number above the cart icon will increase by how many times you clicked.
    
    2. When you click the "View" button, users will have the opportunity to gather more information about the products before making a purchasing decision.

Cart Page Features:

    1. When you click on the cart icon, it will lead you to the cart page where you can see all the items you added to your cart.
    
    2. In the cart page, you can use the arrow buttons next to the quantity to add or remove products from your cart.
    
    3. Whenever you make changes to your cart, such as adding or removing products, the cart page will dynamically update and display the total amount of the products in your cart. This allows you to see the current total price as you make changes.

Checkout & Payment Method Features:

    1. After reviewing the cart, the user can now proceed to click on the “continue” button and provide their personal details for shipping and order confirmation.
    
    2. It will prompt the user to input their name, email address, and shipping information: users must provide details such as, address, city, province, and zip code.
    
    3. After entering the personal details and shipping information, the user can click on the “continue” button to proceed to the payment step.
    
    4. At this stage, a pop-up window will appear with options for payment methods. Two common options are: Paypal and Credit Card.
