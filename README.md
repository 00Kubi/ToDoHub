# ToDoHub

ToDoHub to prosty, ale potężny system zarządzania zadaniami, który pozwala użytkownikom na tworzenie, aktualizację i śledzenie swoich zadań. Posiada system logowania z uprawnieniami administratora, co sprawia, że nadaje się zarówno do użytku osobistego, jak i do zarządzania małymi zespołami.

## Funkcje

- Rejestracja użytkowników i logowanie
- Tworzenie, modyfikowanie i usuwanie zadań
- Aktualizacja statusu zadań (np. "w trakcie", "zrobione")
- Panel administratora do zarządzania użytkownikami i przypisywania zadań
- Śledzenie sesji użytkowników
- Kolorowe oznaczenia statusów zadań dla lepszej wizualizacji
- Interfejs wiersza poleceń (CLI)

## Spis treści

- [Instalacja](#instalacja)
- [Użytkowanie](#użytkowanie)
- [Funkcje administratora](#funkcje-administratora)
- [Funkcje użytkownika](#funkcje-użytkownika)
- [Licencja](#licencja)

## Instalacja

Aby rozpocząć korzystanie z ToDoHub, wykonaj następujące kroki:

1. **Sklonuj repozytorium:**

   ```bash
   git clone https://github.com/00Kubi/ToDoHub.git
   ```

2. **Przejdź do katalogu projektu:**

   ```bash
   cd ToDoHub
   ```

3. **Zainstaluj wymagane zależności:**

   ToDoHub korzysta z biblioteki `colorama` do kolorowego wyświetlania tekstu. Zainstaluj ją, używając pip:

   ```bash
   pip install colorama
   ```

4. **Uruchom aplikację:**

   ```bash
   python main.py
   ```

## Użytkowanie

### Uruchamianie aplikacji

Po uruchomieniu aplikacji, zobaczysz ekran logowania. Możesz zalogować się jako administrator (domyślne dane: `admin/admin`) lub jako zwykły użytkownik.

### Uprawnienia administratora

Administratorzy mają dostęp do panelu administratora, który pozwala na:

- Dodawanie nowych użytkowników
- Usuwanie zadań użytkowników
- Przypisywanie zadań użytkownikom
- Wyświetlanie wszystkich zarejestrowanych użytkowników i ich statusów logowania

### Zadania użytkowników

Po zalogowaniu się jako użytkownik, możesz:

- Dodawać nowe zadania z tytułem i opisem
- Wyświetlać swoje zadania
- Usuwać zadania
- Aktualizować status zadań (np. "w trakcie", "zrobione")
- Odczytywać opisy zadań

## Funkcje administratora

Administratorzy mogą:

1. **Dodawać użytkowników:**
   - Dodawać nowych użytkowników z nazwą użytkownika i hasłem.
   
2. **Usuwać zadania:**
   - Usuwać zadania przypisane do użytkowników, wybierając odpowiedni indeks zadania.
   
3. **Przypisywać zadania:**
   - Przypisywać zadania dowolnym użytkownikom z poziomu panelu administratora.

4. **Wyświetlać użytkowników:**
   - Zobaczyć listę użytkowników oraz ich status zalogowania.

## Funkcje użytkownika

Zwykli użytkownicy mogą:

1. **Dodawać zadania:**
   - Tworzyć zadania z tytułem i opisem.
   
2. **Wyświetlać zadania:**
   - Wyświetlać wszystkie zadania z kolorowymi oznaczeniami statusów dla lepszego zarządzania.
   
3. **Aktualizować status zadań:**
   - Zmieniać status zadań na "w trakcie" lub "zrobione".

4. **Usuwać zadania:**
   - Usuwać zadania na podstawie ich indeksu.

5. **Odczytywać opisy zadań:**
   - Wyświetlać szczegółowy opis zadań.

## Licencja

Projekt jest licencjonowany na warunkach licencji MIT - zobacz plik [LICENSE](LICENSE), aby uzyskać więcej informacji.

---

Ciesz się korzystaniem z **ToDoHub** i efektywnym zarządzaniem swoimi zadaniami!
