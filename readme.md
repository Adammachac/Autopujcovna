AutoPůjčovna
Tento projekt je jednoduchá webová aplikace pro správu autopůjčovny, vytvořená pomocí frameworku Django.

Požadavky
Pro spuštění projektu je potřeba mít nainstalovaný Python ve verzi 3.8 nebo novější a nástroj pip pro správu balíčků. Doporučuje se také používat virtualenv pro vytvoření odděleného virtuálního prostředí.

Jak projekt spustit na jiném počítači
Stáhni projekt – buď si stáhni ZIP archiv a rozbal ho, nebo použij příkaz git clone a adresu repozitáře.

Otevři terminál (nebo příkazový řádek) a přejdi do složky s projektem.

Vytvoř virtuální prostředí pomocí příkazu:
python -m venv venv
Poté prostředí aktivuj.
Na Windows: venv\Scripts\activate
Na macOS / Linux: source venv/bin/activate

Nainstaluj potřebné balíčky. Pokud je v projektu soubor requirements.txt, použij příkaz:
pip install -r requirements.txt
Pokud tento soubor není, stačí nainstalovat Django ručně pomocí:
pip install django

Vytvoř databázi spuštěním příkazu:
python manage.py migrate
Tím se vytvoří soubor databáze (db.sqlite3) a potřebné tabulky.

Spusť vývojový server příkazem:
python manage.py runserver

Otevři webový prohlížeč a zadej adresu:
http://127.0.0.1:8000/
Tím se zobrazí úvodní stránka aplikace.

Struktura projektu
Složka projektu obsahuje následující části:

manage.py – hlavní soubor pro spouštění příkazů Django

db.sqlite3 – soubor databáze (vytvoří se automaticky)

složka s aplikací – obsahuje šablony, statické soubory, modely a pohledy

složka s nastavením projektu – obsahuje settings.py, urls.py a další konfigurační soubory

Poznámky
Projekt používá SQLite jako výchozí databázi.

HTML šablony jsou ve složce templates.

CSS styly, obrázky a další statické soubory jsou ve složce static.

Registrace, přehled aut i zákazníků je řešen přímo v administraci nebo z vlastních šablon.

Autor
Adam Macháč


