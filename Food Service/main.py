import psycopg2

connect = psycopg2.connect(
        host="localhost",
        database="food_service",
        user="postgres",
        password="1234",
        port=5432

    )

class Quantity:

    def __init__(self, m_q=0, a_q=0, d_q=0, r_q=0, g_q=0, p_q=0, b_q=0):
        global food_id
        self.m_q = m_q
        self.a_q = a_q
        self.d_q = d_q
        self.r_q = r_q
        self.g_q = g_q
        self.p_q = p_q
        self.b_q = b_q

        if m_q == m_q:
            food_id = 1
            print(food_id)
        elif a_q == a_q:
            food_id = 2
        cursor = connect.cursor()
        cursor.execute("""INSERT INTO orders(user_id, food_id, quantity, tota_price) VALUES(%s, %s, %s, %s)""", (food_id))


def find_user(cursor, password):
    cursor.execute(
        """
        SELECT users.user_id, users.name,
               cart.user_name, cart.quantity,
               orders.food_id, orders.total_price, orders.order_date
        FROM users
        LEFT JOIN orders ON users.user_id = orders.order_id
        LEFT JOIN cart ON users.user_id = cart.cart_id
        WHERE users.password = %s
        """,
        (password,)
    )

    return cursor.fetchone()

def main():

    cursor = connect.cursor()

    while True:
        print("\n1 For Create Account")
        print("2 For Login Account")
        print("3 For Exit")
        choice = input("chose: ")
        if choice == "1":
            cursor.execute("INSERT INTO users(name, email, password) VALUES (%s, %s, %s)", (input("Enter Your Name"), input("Enter Your Email: "), input("Enter Password: "))

                           )
            connect.commit()
            print("Account Created")

        elif choice == "2":
            password = input("Enter Password")
            user = find_user(cursor, password)
            if user:
                while True:
                    print(f"\nUser Found {user}")
                    print("1 For Menu")
                    print("2 For Cart")
                    print("3 For Check Out")
                    print("4 For Exit")
                    choice = input("Chose: ")
                    if choice == "1":
                        while True:
                            m_q = a_q = d_q = r_q = g_q = p_q = b_q = 0
                            print("\n1 Mango 1$ ")
                            print("2 Apple 2$")
                            print("3 dragon Fruit 8$")
                            print("4 Rubbery 3$")
                            print("5 grapes 1$")
                            print("6 pineapple 1$")
                            print("7 banana 1$")
                            print("8 Exit")
                            choice = input("Chose: ")

                            if choice == "1":
                                m_q = int(input("How Much Mango: "))
                                a_q = int(input("How Much Apple: "))
                                d_q = int(input("How  Dragon Fruit: "))
                                r_q = int(input("How Much Rubbery: "))
                                g_q = int(input("How Much Grapes: "))
                                p_q = int(input("How Much PineApple: "))
                                b_q = int(input("How Much Banana: "))
                                quantity = Quantity(m_q, a_q, d_q, r_q, g_q, p_q, b_q)
                            elif choice == "8":
                                break

                    elif choice == "2":
                        ...
                    elif choice == "3":
                        ...
                    elif choice == "4":
                        break
        elif choice == "3":
            break
if __name__ == "__main__":
    main()