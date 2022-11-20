class Client:
    def __init__(self, first_name, last_name, city, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.balance = balance

    def privacy_data_сlient(self):
        return f'Client: {self.first_name} {self.last_name}. {self.city}. Баланс: {self.balance} руб.'

    def data_clients(self):
        return f'Client: {self.first_name} {self.last_name}. {self.city}.'


client_1 = Client('Иван', 'Петров', 'Москва', 50)
client_2 = Client('Валентина', 'Строганова', 'Чехов', 1000)
client_3 = Client('Александр', 'Пряж', 'Ижевск', 0)


сlients_list = [client_1, client_2, client_3]

for сlient in сlients_list:
    print(сlient.data_clients())
