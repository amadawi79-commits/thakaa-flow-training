import streamlit as st
import pandas as pd

st.set_page_config(page_title="ميزان الفضاء", page_icon="🚀")

GRAVITY = {
    "Mercury": 0.38,
    "Venus": 0.90,
    "Earth": 1.00,
    "Moon": 0.17,
    "Mars": 0.38,
    "Jupiter": 2.53,
    "Saturn": 1.07,
    "Uranus": 0.89,
    "Neptune": 1.14
}

st.title("🚀 ميزان الفضاء")
st.write("اكتشفي كيف تتغير قراءة وزنك باختلاف الجاذبية.")

earth_weight = st.number_input(
    "وزنك على الأرض بالكيلوجرام",
    min_value=1.0,
    value=70.0,
    step=1.0
)

planet = st.selectbox("اختاري العالم", list(GRAVITY))

factor = GRAVITY[planet]
space_weight = earth_weight * factor
difference = space_weight - earth_weight

st.metric(
    f"قراءة الوزن على {planet}",
    f"{space_weight:.2f} كجم",
    delta=f"{difference:+.2f} كجم مقارنة بالأرض",
    delta_color="off"
)

if factor < 1:
    st.success(
        f"ستكونين أخف! نظريًا يمكنك القفز أعلى "
        f"بنحو {1 / factor:.2f} مرة، بافتراض سرعة الانطلاق نفسها."
    )
elif factor > 1:
    st.warning("ستكونين أثقل بسبب زيادة الجاذبية!")
else:
    st.info("هذه جاذبية الأرض، لذلك قراءة وزنك لا تتغير.")

st.subheader("مقارنة الوزن على جميع العوالم")

comparison = pd.DataFrame({
    "World": list(GRAVITY),
    "Weight": [earth_weight * g for g in GRAVITY.values()]
}).set_index("World")

st.bar_chart(comparison)

st.caption(
    "الحساب يستخدم معاملات الجاذبية المعطاة في المهمة. "
    "الكتلة ثابتة، والمعروض قراءة وزن مكافئة بالكيلوجرام."
)
