def filter_words(st):
    st = st.lower()
    st = st[0].upper() + st[1:]
    st = ' '.join(st.split())
    return st