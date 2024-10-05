import streamlit as st
import os
import pandas as pd
import json


def load_csv(file_name):
    """csvファイルのの読み込み"""
    file_path = os.path.join('database', file_name)

    try:
        df = pd.read_csv(file_path)
        return df
    
    except FileNotFoundError:
        print(f"エラー: ファイル '{file_path}' が見つかりません。パスを確認してください。")
        return None
    except Exception as e:
        print(f"エラー: {e}")
        return None


def load_api_key():
    api_key = KEY = st.secrets["ApiKey"]["OPENAI_API_KEY"]

    return api_key
