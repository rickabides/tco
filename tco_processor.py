import pandas as pd
import json
import matplotlib.pyplot as plt

class CostCalculator:
    def __init__(self, cost_overheads):
        self.growth_rate = cost_overheads["growth_rate"]
        self.amortization_years = cost_overheads["amortization_years"]
        self.discount_rate = cost_overheads["discount_rate"]

class OnPremCostCalculator(CostCalculator):
    def __init__(self, on_prem_costs, cost_overheads):
        super().__init__(cost_overheads)
        self.hardware_costs = on_prem_costs
        self.maintenance_rate = cost_overheads["maintenance_rate"]
        self.admin_overhead = cost_overheads["admin_overhead"]

    def calculate_initial_costs(self):
        total_cost = (
            self.hardware_costs['web_servers']['count'] * self.hardware_costs['web_servers']['price'] +
            self.hardware_costs['db_servers']['count'] * self.hardware_costs['db_servers']['price'] +
            self.hardware_costs['storage']['tb'] * self.hardware_costs['storage']['price_per_tb'] +
            self.hardware_costs.get('network', {}).get('monthly_cost', 0) * 12 +
            self.hardware_costs.get('colo', {}).get('monthly_cost', 0) * 12
        )
        discounted_cost = total_cost * (1 - self.discount_rate)
        print(f"Initial On-Prem Costs (Discounted): ${discounted_cost:.2f}")
        return discounted_cost

    def calculate_total_cost(self):
        initial_costs = self.calculate_initial_costs()
        annual_maintenance = initial_costs * self.maintenance_rate
        total_cost = initial_costs
        print(f"Initial Costs: ${initial_costs:.2f}, Annual Maintenance: ${annual_maintenance:.2f}")
        for year in range(self.amortization_years):
            total_cost += annual_maintenance * (1 + self.admin_overhead)
            annual_maintenance *= (1 + self.growth_rate)
            print(f"Year {year+1}: Total Cost: ${total_cost:.2f}, Next Year Maintenance: ${annual_maintenance:.2f}")
        return total_cost

class AWSCostCalculator(CostCalculator):
    def __init__(self, aws_pricing, cost_overheads):
        super().__init__(cost_overheads)
        self.pricing_data = pd.DataFrame(aws_pricing)

    def get_instance_cost(self, instance_type, hours=24*365):
        instance_info = self.pricing_data[self.pricing_data['Type'] == instance_type].iloc[0]
        if instance_type == 'EBS':
        # For EBS, calculate cost based on gigabytes per month
            cost = instance_info['Price'] * instance_info['Qty'] * 12  # Calculate yearly cost from monthly cost
            print(f"{instance_type} Storage Cost for 1 Year (GB per month): ${cost:.2f}")
        else:
        # For other types, calculate cost based on hourly pricing
            cost = instance_info['Price'] * instance_info['Qty'] * hours
            print(f"{instance_type} Instance Cost for 1 Year: ${cost:.2f}")
        return cost

    def calculate_total_annual_cost(self):
        total_cost = 0
        for _, row in self.pricing_data.iterrows():
            # Use the get_instance_cost method to calculate the cost for each type
            instance_cost = self.get_instance_cost(row['Type'])
            total_cost += instance_cost
            print(f"Adding {row['Type']} cost: ${instance_cost:.2f}")
        discounted_total_cost = total_cost * (1 - self.discount_rate)
        print(f"Total AWS Annual Cost (Discounted): ${discounted_total_cost:.2f}")
        return discounted_total_cost


    def project_costs(self):
        current_cost = self.calculate_total_annual_cost()
        projected_costs = {}
        for year in range(1, self.amortization_years + 1):
            current_cost *= (1 + self.growth_rate)
            projected_costs[year] = current_cost
            print(f"Projected AWS Cost Year {year}: ${current_cost:.2f}")
        return projected_costs

def load_configuration(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config

# Main execution
config = load_configuration('cost_config.json')
on_prem_calculator = OnPremCostCalculator(config["on_prem_costs"], config["cost_overheads"])
aws_calculator = AWSCostCalculator(config["aws_pricing"], config["cost_overheads"])

# Calculate projected costs
on_prem_costs = [on_prem_calculator.calculate_total_cost()]
aws_costs = list(aws_calculator.project_costs().values())

# Visualization
years = [1, 2, 3]
plt.figure(figsize=(10, 5))
plt.plot(years, on_prem_costs * len(years), label='On-Premises', marker='o')  # Repeat on-prem costs for visualization
plt.plot(years, aws_costs, label='AWS Cloud', marker='x')
plt.title('Cost Comparison: On-Premises vs. AWS Cloud Over 3 Years')
plt.xlabel('Year')
plt.ylabel('Total Cost (USD)')
plt.legend()
plt.grid(True)
plt.show()

# Print the report
print("Cost Comparison Report: On-Premises vs. AWS Cloud Over 3 Years")
print("--------------------------------------------------------------")
print("{:<10} {:<15} {:<15}".format("Year", "On-Premises", "AWS Cloud"))
for year in range(3):
    print("{:<10} ${:<14,.2f} ${:<14,.2f}".format(year+1, on_prem_costs[0], aws_costs[year]))

