import streamlit as st
import time
import datetime
from pymongo import MongoClient 
from openai import OpenAI

MONGO_DB_URI = st.secrets['MONGO_DB_URI']
OPEN_AI_KEY = st.secrets[]
