class PoprosOWyjscieNaPiwo:
    def __enter__(self):
        print("Poproś żonę o pozwolenie na wyjście z kolegami")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Podziękuj żonie za pozwolenie!")


with PoprosOWyjscieNaPiwo():
    print("Wypij jedno piwo")
    print("Wypij drugie piwo")
    print("Wróc bezpiecznie do domu")
#
# print("Wypij jedno piwo")
# print("Wypij drugie piwo")
# print("Wróc bezpiecznie do domu")