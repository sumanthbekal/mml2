def calculate_probability(material_balance):
    total_value = sum(material_balance.values())
    probability = material_balance.get('white', 0) / total_value if total_value else 0.5
    return probability

def main():
    material_balance = {'white': 39, 'black': 42}
    probability = calculate_probability(material_balance)
    print("Probability of white winning:", probability)

if __name__ == "_main_":
    main()