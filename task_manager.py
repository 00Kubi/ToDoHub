import os
import time
from colorama import Fore, Style, init

# Inicjalizacja colorama
init(autoreset=True)

class User:
    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.password = password
        self.is_admin = is_admin
        self.tasks = []
        self.is_logged_in = False  # Nowa flaga, która będzie śledzić status logowania

class TaskManager:
    def __init__(self):
        self.users = []
        self.logged_in_user = None

    def register_user(self, username, password, is_admin=False):
        user = User(username, password, is_admin)
        self.users.append(user)
        self.animate_text(f"Użytkownik '{username}' został zarejestrowany.")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.logged_in_user = user
                user.is_logged_in = True  # Ustawiamy flagę na zalogowany
                self.animate_text(f"Witaj, {username}!")
                return True
        print(Fore.RED + "Nieprawidłowa nazwa użytkownika lub hasło.")
        return False

    def logout(self):
        if self.logged_in_user:
            self.logged_in_user.is_logged_in = False  # Ustawiamy flagę na niezalogowany
        self.logged_in_user = None
        self.animate_text("Zostałeś wylogowany.")

    def add_task(self, title, description, user=None):
        if user is None:
            user = self.logged_in_user
        task = {"title": title, "description": description, "status": "nieukończone"}
        user.tasks.append(task)
        self.animate_text(f"Zadanie '{title}' zostało dodane użytkownikowi '{user.username}'.")

    def remove_task(self, index, user=None):
        if user is None:
            user = self.logged_in_user
        if 0 <= index < len(user.tasks):
            removed_task = user.tasks.pop(index)
            self.animate_text(f"Zadanie '{removed_task['title']}' zostało usunięte.")
        else:
            print(Fore.RED + "Nieprawidłowy indeks zadania.")

    def update_task_status(self, index, status, user=None):
        if user is None:
            user = self.logged_in_user
        if 0 <= index < len(user.tasks):
            user.tasks[index]["status"] = status
            self.animate_text(f"Zadanie '{user.tasks[index]['title']}' zostało oznaczone jako {status}.")
        else:
            print(Fore.RED + "Nieprawidłowy indeks zadania.")

    def show_tasks(self, user=None):
        if user is None:
            user = self.logged_in_user
        if not user.tasks:
            print(Fore.YELLOW + "Brak zadań.")
        else:
            print(Fore.CYAN + f"Zadania użytkownika: {user.username}")
            print(Fore.CYAN + f"{'Nr':<5}{'Tytuł':<30}{'Status'}")
            print(Fore.CYAN + "-" * 45)
            for i, task in enumerate(user.tasks):
                status_color = self.get_status_color(task["status"])
                print(status_color + f"{i:<5}{task['title']:<30}{task['status']}")
            print("\n")

    def get_status_color(self, status):
        if status == "zrobione":
            return Fore.GREEN
        elif status == "w trakcie":
            return Fore.YELLOW
        else:
            return Fore.RED

    def read_task_description(self, index, user=None):
        if user is None:
            user = self.logged_in_user
        if 0 <= index < len(user.tasks):
            task = user.tasks[index]
            print(Fore.CYAN + f"\nTytuł: {task['title']}")
            print(Fore.CYAN + f"Opis: {task['description']}\n")
        else:
            print(Fore.RED + "Nieprawidłowy indeks zadania.")

    def show_users(self):
        """ Funkcja do wyświetlania listy użytkowników z ich statusem zalogowania. """
        print(Fore.CYAN + f"\nLista użytkowników:")
        print(Fore.CYAN + f"{'Nr':<5}{'Nazwa użytkownika':<20}{'Zalogowany'}")
        print(Fore.CYAN + "-" * 40)
        for i, user in enumerate(self.users):
            status = Fore.GREEN + "Tak" if user.is_logged_in else Fore.RED + "Nie"
            print(Fore.CYAN + f"{i:<5}{user.username:<20}{status}")
        print("\n")

    def animate_text(self, text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        print()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

def admin_panel(task_manager):
    while True:
        task_manager.clear_screen()
        print(Fore.BLUE + "\n--- Panel Administratora ---")
        print(Fore.CYAN + "1. Dodaj użytkownika")
        print(Fore.CYAN + "2. Usuń zadanie użytkownika")
        print(Fore.CYAN + "3. Przypisz zadanie użytkownikowi")
        print(Fore.CYAN + "4. Wyświetl listę użytkowników")
        print(Fore.CYAN + "5. Wyloguj\n")

        choice = input(Fore.YELLOW + "Wybierz opcję: ")

        if choice == "1":
            username = input(Fore.YELLOW + "Podaj nazwę użytkownika: ")
            password = input(Fore.YELLOW + "Podaj hasło: ")
            task_manager.register_user(username, password)
            time.sleep(1)
        elif choice == "2":
            task_manager.clear_screen()
            for i, user in enumerate(task_manager.users):
                print(f"{i}. {user.username}")
            try:
                user_index = int(input(Fore.YELLOW + "Podaj numer użytkownika: "))
                task_manager.show_tasks(task_manager.users[user_index])
                index = int(input(Fore.YELLOW + "Podaj indeks zadania do usunięcia: "))
                task_manager.remove_task(index, task_manager.users[user_index])
            except (ValueError, IndexError):
                print(Fore.RED + "Nieprawidłowy wybór.")
            time.sleep(1)
        elif choice == "3":
            task_manager.clear_screen()
            for i, user in enumerate(task_manager.users):
                print(f"{i}. {user.username}")
            try:
                user_index = int(input(Fore.YELLOW + "Podaj numer użytkownika: "))
                title = input(Fore.YELLOW + "Podaj tytuł zadania: ")
                description = input(Fore.YELLOW + "Podaj opis zadania: ")
                task_manager.add_task(title, description, task_manager.users[user_index])
            except (ValueError, IndexError):
                print(Fore.RED + "Nieprawidłowy wybór.")
            time.sleep(1)
        elif choice == "4":
            task_manager.show_users()
            input(Fore.YELLOW + "Naciśnij Enter, aby kontynuować...")
        elif choice == "5":
            task_manager.logout()
            break
        else:
            print(Fore.RED + "Nieprawidłowy wybór.")
            time.sleep(1)

def main():
    task_manager = TaskManager()
    
    # Rejestracja konta administratora
    task_manager.register_user("admin", "admin", is_admin=True)

    while True:
        task_manager.clear_screen()
        print(Fore.BLUE + "\n--- System Logowania ---")
        username = input(Fore.YELLOW + "Podaj nazwę użytkownika: ")
        password = input(Fore.YELLOW + "Podaj hasło: ")

        if task_manager.login(username, password):
            if task_manager.logged_in_user.is_admin:
                admin_panel(task_manager)
            else:
                while True:
                    task_manager.clear_screen()
                    print(Fore.BLUE + "\n--- Menedżer Zadań ---")
                    print(Fore.CYAN + "1. Dodaj zadanie")
                    print(Fore.CYAN + "2. Usuń zadanie")
                    print(Fore.CYAN + "3. Oznacz zadanie jako w trakcie")
                    print(Fore.CYAN + "4. Oznacz zadanie jako zrobione")
                    print(Fore.CYAN + "5. Wyświetl moje zadania")
                    print(Fore.CYAN + "6. Odczytaj opis zadania")
                    print(Fore.CYAN + "7. Wyloguj\n")

                    choice = input(Fore.YELLOW + "Wybierz opcję: ")

                    if choice == "1":
                        title = input(Fore.YELLOW + "Podaj tytuł zadania: ")
                        description = input(Fore.YELLOW + "Podaj opis zadania: ")
                        task_manager.add_task(title, description)
                        time.sleep(1)
                    elif choice == "2":
                        task_manager.show_tasks()
                        try:
                            index = int(input(Fore.YELLOW + "Podaj indeks zadania do usunięcia: "))
                            task_manager.remove_task(index)
                        except ValueError:
                            print(Fore.RED + "Nieprawidłowy indeks.")
                        time.sleep(1)
                    elif choice == "3":
                        task_manager.show_tasks()
                        try:
                            index = int(input(Fore.YELLOW + "Podaj indeks zadania do oznaczenia jako w trakcie: "))
                            task_manager.update_task_status(index, "w trakcie")
                        except ValueError:
                            print(Fore.RED + "Nieprawidłowy indeks.")
                        time.sleep(1)
                    elif choice == "4":
                        task_manager.show_tasks()
                        try:
                            index = int(input(Fore.YELLOW + "Podaj indeks zadania do oznaczenia jako zrobione: "))
                            task_manager.update_task_status(index, "zrobione")
                        except ValueError:
                            print(Fore.RED + "Nieprawidłowy indeks.")
                        time.sleep(1)
                    elif choice == "5":
                        task_manager.show_tasks()
                        input(Fore.YELLOW + "Naciśnij Enter, aby kontynuować...")
                    elif choice == "6":
                        task_manager.show_tasks()
                        try:
                            index = int(input(Fore.YELLOW + "Podaj indeks zadania, którego opis chcesz odczytać: "))
                            task_manager.read_task_description(index)
                        except ValueError:
                            print(Fore.RED + "Nieprawidłowy indeks.")
                        input(Fore.YELLOW + "Naciśnij Enter, aby kontynuować...")
                    elif choice == "7":
                        task_manager.logout()
                        break
                    else:
                        print(Fore.RED + "Nieprawidłowy wybór.")
                        time.sleep(1)
        else:
            time.sleep(1)

if __name__ == "__main__":
    main()
