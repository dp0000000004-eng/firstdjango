class Hostel:
    def __init__(self, name, age, home):
        if not name:
            raise ValueError("Missing Name!")
        self.name = name
        self.age = age
        self.home = home

    def __str__(self):
        return f"{self.name} is from {self.home}. And {self.age} years."
    
    @property
    def home(self):
        return self._home

    @home.setter
    def home(self, home):
        if home not in ["Odisha"]:
            raise ValueError("Invalid Home")
        self._home = home

def main():
    hostel = get_info()
    print(hostel)
    


def get_info():
    name = input("What is Your name ? ")
    age = int(input("What's Your age ? "))
    home = input("Where are you from ? ")
    hostel = Hostel(name, age, home)
    return hostel

if __name__ == "__main__":
    main()