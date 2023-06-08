def calculate_cogs(raw_material_cost_kg):
    # Calculate cost of 200 grams of raw material
    raw_material_cost_200g = raw_material_cost_kg / 5

    # Calculate RM cost of 200 grams + packaging, label, and carton box cost
    rm_total = raw_material_cost_200g + 8

    # Calculate 5% GSt
    gst = 0.05 * rm_total

    # Calculate labor charges (2% of RM total)
    labor_charges = 0.02 * rm_total

    # Calculate testing charges (2% of RM total)
    testing_charges = 0.02 * rm_total

    # Calculate handling charges (5% of RM total)
    handling_charges = 0.05 * rm_total

    # Calculate COGS (including GST, transportation, labor charges, testing charges, and handling charges)
    cogs = rm_total + gst + 5 + labor_charges + testing_charges + handling_charges

    return raw_material_cost_200g, cogs

# Calculate selling price on Amazon
def calculate_selling_price(mrp):
    # Calculate selling price on Amazon (40% of MRP)
    selling_price = 0.4 * mrp

    # Calculate Amazon commission (50% of selling price)
    commission = 0.5 * selling_price

    # Calculate final profit (COGS - commission)
    profit = commission - cogs

    return selling_price, profit

# Input the name of the product and cost of raw material per kg
product_name = input("Enter the name of the product: ")
raw_material_cost_kg = float(input("Enter the cost of raw material per kg: "))

# Calculate the cost per 200 grams and COGS
cost_200g, cogs = calculate_cogs(raw_material_cost_kg)

# Prompt for MRP of the product
mrp = float(input("Enter the MRP of the product: "))

# Calculate selling price on Amazon and final profit
selling_price, profit = calculate_selling_price(mrp)

# Print the cost per 200 grams, COGS, selling price, and final profit
print(f"The cost per 200 grams of {product_name} is: {cost_200g}")
print(f"The COGS for {product_name} is: {cogs}")
print(f"The selling price on Amazon for {product_name} is: {selling_price}")
print(f"The final profit for {product_name} is: {profit}")

# Print the inputs
print("Inputs:")
print(f"Raw Material Cost per kg: {raw_material_cost_kg}")
print(f"Raw Material Cost per 200 grams: {cost_200g}")
print(f"Packaging, Label & Carton Box Cost: 8")
print(f"GST Percentage: 5%")
print(f"Transportation: 5")
print(f"Labor Charges: {0.02 * cogs}")
print(f"Testing Charges: {0.02 * cogs}")
print(f"Handling Charges: {0.05 * cogs}")

# Thank the user for using the program
print("Thanks for using Pranik costing program!Now let me take a rest boss")
