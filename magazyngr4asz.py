import streamlit as st

def main():
    # Inicjalizacja magazynu w 'session_state' Streamlit, jeśli jeszcze nie istnieje
    # Używamy st.session_state do przechowywania stanu magazynu, co jest konieczne w aplikacjach Streamlit
    if 'magazyn' not in st.session_state:
        st.session_state.magazyn = []

    st.title("📦 Prosta Aplikacja Magazynowa")
    st.markdown("---")

    # --- Sekcja Dodawania Produktu ---
    st.header("➕ Dodaj Produkt")
    
    # Pole do wprowadzania nazwy produktu
    nowy_produkt = st.text_input("Nazwa nowego produktu:", key="input_dodaj")

    # Przycisk do dodania produktu
    if st.button("Dodaj do Magazynu"):
        if nowy_produkt:
            # Dodanie produktu do listy w st.session_state
            st.session_state.magazyn.append(nowy_produkt.strip())
            st.success(f"Produkt **{nowy_produkt.strip()}** został dodany.")
            # Wymuszenie odświeżenia pola tekstowego (opcjonalne, dla estetyki)
            st.session_state.input_dodaj = "" 
        else:
            st.warning("Proszę podać nazwę produktu.")

    st.markdown("---")

    # --- Sekcja Wyświetlania Magazynu ---
    st.header("📋 Aktualny Stan Magazynu")
    
    if st.session_state.magazyn:
        # Wyświetlanie listy produktów
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
    
    # Tworzenie listy opcji do usunięcia
    produkty_do_usuniecia = st.session_state.magazyn
    
    if produkty_do_usuniecia:
        # Wybór produktu z listy rozwijanej
        wybrany_produkt = st.selectbox(
            "Wybierz produkt do usunięcia:",
            options=produkty_do_usuniecia,
            key="select_usun"
        )

        # Przycisk do usunięcia
        if st.button("Usuń z Magazynu"):
            try:
                # Usunięcie produktu z listy
                st.session_state.magazyn.remove(wybrany_produkt)
                st.success(f"Produkt **{wybrany_produkt}** został usunięty.")
                # Ponowne uruchomienie aplikacji (Streamlit) w celu odświeżenia stanu listy rozwijanej
                st.rerun() 
            except ValueError:
                st.error("Wystąpił błąd podczas usuwania produktu.")
    else:
        st.info("Brak produktów do usunięcia.")


if __name__ == "__main__":
    main()
