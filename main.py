class Pizza :
    def __init__(self, nom, prix, ingredients, vegetarienne = False) -> None:
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne

    def Afficher(self):
        veg_str = ""
        if self.vegetarienne :
            veg_str= " - VEGETARIENNE"
        
        print(f"PIZZA {self.nom} : {self.prix}$" + veg_str)
        print(", ".join(self.ingredients))


class PizzaPersonnalise(Pizza):
    def __init__(self, nom, prix, ingredients, vegetarienne=False) -> None:
        super().__init__(nom, prix, ingredients, vegetarienne)

    def demander_ingredients_utilisateur(self):
        ingredient = input("Ajoutez un ingredient (ou ENTER pour terminer) : ")
        if ingredient == "" :
            return 
        self.ingredients.append(ingredient)
        self.demander_ingredients_utilisateur()

pizzas = [
    Pizza("4 Fromages", 8.5, ("brie", "emmental", "compte", "parmesan"), True),
    Pizza("Queen", 11, ("viande", "fromage", "gruyere")),
    Pizza("Vegetarienne", 13, ("champignon", "tomate", "oignon", "poivron"), True),
    Pizza("Fermiere", 5, ("poulet", "saumon fume", "poivron", "gruyere"))
]

pizza1 = PizzaPersonnalise("Hawai", 10, [])
pizza1.demander_ingredients_utilisateur()
pizza1.Afficher()

# for pizza in pizzas:
#     pizza.Afficher()
#     print()