import streamlit as st
import pandas as pd
from modules.library import Library


def show_library():

    library = Library()

    st.title("📚 Library Management")

    tab1, tab2, tab3, tab4 = st.tabs([
        "➕ Add Book",
        "📋 View Books",
        "🔍 Search",
        "🗑 Delete"
    ])

    # ==========================
    # ADD BOOK
    # ==========================
    with tab1:

        book_code = st.text_input("Book Code")

        book_name = st.text_input("Book Name")

        author = st.text_input("Author")

        publisher = st.text_input("Publisher")

        category = st.text_input("Category")

        quantity = st.number_input(
            "Quantity",
            min_value=1,
            value=1
        )

        shelf_no = st.text_input("Shelf Number")

        if st.button("Add Book"):

            library.add_book(
                book_code,
                book_name,
                author,
                publisher,
                category,
                quantity,
                quantity,
                shelf_no
            )

            st.success("Book Added Successfully!")

    # ==========================
    # VIEW BOOKS
    # ==========================
    with tab2:

        data = library.get_all_books()

        if data:

            columns = [
                "Book ID",
                "Book Code",
                "Book Name",
                "Author",
                "Publisher",
                "Category",
                "Quantity",
                "Available",
                "Shelf",
                "Created At"
            ]

            st.dataframe(
                pd.DataFrame(data, columns=columns),
                use_container_width=True
            )

        else:
            st.info("No Books Found.")

    # ==========================
    # SEARCH
    # ==========================
    with tab3:

        keyword = st.text_input("Search Book")

        if keyword:

            data = library.search_book(keyword)

            if data:

                columns = [
                    "Book ID",
                    "Book Code",
                    "Book Name",
                    "Author",
                    "Publisher",
                    "Category",
                    "Quantity",
                    "Available",
                    "Shelf",
                    "Created At"
                ]

                st.dataframe(
                    pd.DataFrame(data, columns=columns),
                    use_container_width=True
                )

            else:
                st.warning("Book Not Found.")

    # ==========================
    # DELETE
    # ==========================
    with tab4:

        book_id = st.number_input(
            "Book ID",
            min_value=1,
            step=1
        )

        if st.button("Delete Book"):

            library.delete_book(book_id)

            st.success("Book Deleted Successfully!")

    st.divider()

    _, col, _ = st.columns([1, 2, 1])

    with col:
        if st.button(
            "⬅ Back to Dashboard",
            use_container_width=True
        ):
            st.session_state.page = "dashboard"
            st.rerun()