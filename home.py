import streamlit as st

st.set_page_config(
    page_title="California Housing App",
    page_icon="🏠",
    layout="centered"
)

# 主页标题与欢迎说明
st.title("🏠 California Housing Data Analysis Lab")
st.write("欢迎来到 1990 年加利福尼亚州房屋数据分析实验应用！")

st.markdown("---")

st.subheader("实验说明与功能简介")
st.write("""
本应用基于 1990 年加利福尼亚州的人口普查数据集，通过 Streamlit 实现了交互式数据过滤与可视化。
在左侧侧边栏或页面组件中，你可以：
- **过滤房屋最低中位价**（Minimal Median House Value）
- **按地理位置类型进行筛选**（Ocean Proximity）
- **按收入水平进行分组查看**（Income Level: Low / Medium / High）
- 实时查看对应地理位置的**散点地图**以及房屋中位价的**直方图分布**。
""")

st.markdown("---")

st.subheader("开始探索")
st.write("点击下方按钮即可前往实验可视化页面：")

if st.button("进入房产数据可视化页面 🚀", type="primary"):
    st.switch_page("pages/app-housing.py")