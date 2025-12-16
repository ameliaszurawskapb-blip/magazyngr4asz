import streamlit as st

# Funkcja wykonująca dodawanie produktu i resetująca pole wejściowe
def dodaj_produkt():
    """Pobiera produkt z pola wejściowego, dodaje do magazynu i czyści pole."""
    nowy_produkt = st.session_state.input_dodaj
    if nowy_produkt:
        # Dodanie produktu do listy w st.session_state
        st.session_state.magazyn.append(nowy_produkt.strip())
        st.success(f"Produkt **{nowy_produkt.strip()}** został dodany.")
        # Zerowanie pola tekstowego - to jest poprawny sposób
        st.session_state.input_dodaj = "" 
    else:
        st.warning("Proszę podać nazwę produktu.")

def main():
    # Inicjalizacja magazynu w 'session_state' Streamlit, jeśli jeszcze nie istnieje
    if 'magazyn' not in st.session_state:
        st.session_state.magazyn = []

    # --- Układ nagłówka z obrazkiem Mikołaja ---
    col1, col2 = st.columns([0.7, 0.3]) # Dzielimy szerokość na 70% dla tytułu i 30% dla obrazka

    with col1:
        st.title("📦 Prosta Aplikacja Magazynowa")
    with col2:
        # Pamiętaj, aby plik 'santa.png' (lub inny obrazek) znajdował się w tym samym katalogu
        # co plik app.py, lub podaj pełną ścieżkę do obrazka.
        st.image("santa.png", width=150) # Zmieniamy rozmiar, aby pasował do nagłówka

    st.markdown("---")

    # --- Sekcja Dodawania Produktu ---
    st.header("➕ Dodaj Produkt")
    
    st.text_input("Nazwa nowego produktu:", key="input_dodaj")

    st.button(
        "Dodaj do Magazynu", 
        on_click=dodaj_produkt,
    )
    
    st.markdown("---")

    # --- Sekcja Wyświetlania Magazynu ---
    st.header("📋 Aktualny Stan Magazynu")
    
    if st.session_state.magazyn:
        st.dataframe(
            {'Produkt': st.session_state.magazyn}, 
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("Magazyn jest pusty.")

    st.markdown("---")

    # --- Sekcja Usuwania Produktu ---
    st.header("🗑️ Usuń Produkt")
    
    produkty_do_usuniecia = st.session_state.magazyn
    
    if produkty_do_usuniecia:
        wybrany_produkt = st.selectbox(
            "Wybierz produkt do usunięcia:",
            options=produkty_do_usuniecia,
            key="select_usun"
        )

        if st.button("Usuń z Magazynu"):
            try:
                st.session_state.magazyn.remove(wybrany_produkt)
                st.success(f"Produkt **{wybrany_produkt}** został usunięty.")
                st.rerun() 
            except ValueError:
                st.error("Wystąpił błąd podczas usuwania produktu.")
    else:
        st.info("Brak produktów do usunięcia.")


if __name__ == "__main__":
    main()
