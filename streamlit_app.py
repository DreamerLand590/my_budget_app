import streamlit as st
import pandas as pd
from pathlib import Path


from app.data_loader import load_expenses
from app.services import calculate_total, group_by_category
from app.exceptions import DataFileError
from app import config


st.set_page_config(page_title="Мій Бюджет", page_icon="💰")
st.title("💰 Аналіз домашнього бюджету")
st.caption("Цей застосунок створено на основі домашнього завдання 5. Він читає файл з витратами та показує статистику.")


data_path = config.DATA_FILE

try:
    
    expenses, warnings = load_expenses(data_path)
    
    if not expenses:
        st.warning("Файл порожній або всі рядки містять помилки.")
    else:
        
        df = pd.DataFrame([{"Дата": e.date, "Категорія": e.category, "Сума": e.amount} for e in expenses])
        
        
        st.sidebar.header("Фільтри")
        
        
        categories = df["Категорія"].unique().tolist()
        selected_categories = st.sidebar.multiselect("Оберіть категорії:", categories, default=categories)
        
        
        min_amount = st.sidebar.slider("Мінімальна сума витрат (грн):", 0, int(df["Сума"].max()), 0)
        
        
        filtered_df = df[(df["Категорія"].isin(selected_categories)) & (df["Сума"] >= min_amount)]
        
        
        if filtered_df.empty:
            st.warning("За вашими фільтрами нічого не знайдено. Спробуйте змінити умови.")
        else:
            
            total_sum = filtered_df["Сума"].sum()
            st.metric("Загальна сума (за фільтром)", f"{total_sum:.2f} грн")
            
            
            st.subheader("Таблиця витрат")
            st.dataframe(filtered_df, use_container_width=True)
            
            
            st.subheader("Розподіл витрат за категоріями")
            chart_data = filtered_df.groupby("Категорія")["Сума"].sum()
            st.bar_chart(chart_data)

except DataFileError as e:
    
    st.error(f"Помилка завантаження даних: {e}")
    st.stop()
except Exception as e:
    
    st.error(f"Сталася непередбачена помилка: {e}")
    st.stop()