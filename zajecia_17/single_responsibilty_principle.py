# def zrob_przelew(id_pierwszego_klienta, kwota, id_drugiego_klienta):
#     print("Pobierz dane pierwszego klienta")
#     print("Zrob przelew")
#     print("Pobierz dane drugiego klienta")
#     print("Dodanie operacji do listy operacji")
#
#
# zrob_przelew("123", 1000, "234")
#
#
# lista_operacji = []
# def pobieranie_danych_od_klienta(id_klienta):
#     print(f"Pobieranie danych od klienta {id_klienta}")
#
#
# def przelewanie_kwoty(id_pierwszego_klienta, id_drugiego_klienta):
#     print(f"Przelewam kwotę od {id_pierwszego_klienta} do {id_drugiego_klienta}")
#
# def dodanie_operacji_do_listy(operacja):
#     lista_operacji.append(operacja)
#
#
# def zrob_przelew_2(id_pierwszego_klienta, kwota, id_drugiego_klienta):
#     pobieranie_danych_od_klienta(id_pierwszego_klienta)
#     pobieranie_danych_od_klienta(id_drugiego_klienta)
#     przelewanie_kwoty(id_pierwszego_klienta, id_drugiego_klienta)
#     dodanie_operacji_do_listy("Przelew")


class UsersManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)


class EmailSender:
    def send_email(self, user, content):
        print(f"Sending email to {user}: {content}")


class UsersManagerWitoutSendingEmails(UsersManager):
    pass

class UsersManagerWithSubsrpition(UsersManager, EmailSender):
    pass


users_without_subscription = UsersManagerWitoutSendingEmails()
users_with_subscription = UsersManagerWithSubsrpition()

users_without_subscription.add_user("Michal")
users_with_subscription.add_user("Tomek")
users_with_subscription.add_user("Adam")
users_with_subscription.add_user("Zuzia")
for user in users_with_subscription.users:
    users_with_subscription.send_email(user, "Nowy produkt na stanie!!!")