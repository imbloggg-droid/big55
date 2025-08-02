
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Big Five Football MVP", layout="wide")

# Загрузка данных
df = pd.read_csv("players.csv")

# Выбор игрока
player_names = df['Name'].unique()
selected_player = st.selectbox("Выберите игрока", player_names)

# Фильтрация данных по выбранному игроку
player_data = df[df['Name'] == selected_player].iloc[0]

st.title(f"🧠 Психологический профиль: {selected_player}")
st.markdown(f"**Позиция:** {player_data['Player Position']}")
st.markdown(f"**Источник интервью:** [ссылка]({player_data['Source URL']})")
st.markdown("---")

# Отображение оценок Big Five
st.subheader("Big Five Оценки")
traits = {
    "Openness": "O_exp",
    "Conscientiousness": "C_exp",
    "Extraversion": "E_exp",
    "Agreeableness": "A_exp",
    "Neuroticism": "N_exp"
}

for trait, exp_field in traits.items():
    score = player_data[trait]
    explanation = player_data[exp_field]
    st.markdown(f"**{trait}**: {score}  \n_{explanation}_")
st.markdown("---")
st.subheader("💬 Общий комментарий")
st.markdown(player_data['Comment'])

st.markdown("---")
st.subheader("📄 JSON результат")
st.json({
    "player": player_data["Name"],
    "position": player_data["Player Position"],
    "scores": {trait: player_data[trait] for trait in traits},
    "comment": player_data["Comment"],
    "confidence": player_data["Confidence"],
    "validated": player_data["Validated"]
})
