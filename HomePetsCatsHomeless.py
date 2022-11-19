from HomePetsCats import PetCat
class PetCatHomeless(PetCat):
    there_are_cats = True
cat1 = PetCatHomeless(name = "Сэм", gender = "мальчик", age = "2")

print("В приюте есть кошка по имени", cat1.name,", пол", cat1.gender, ", возраст -", cat1.age)