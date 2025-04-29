import math

import streamlit as st

# タイトルとヘッダー
st.title("俺の預金利息計算")
st.markdown(
    "預金利息から源泉徴収税(所得税と復興特別所得税)と利息総額を計算します。2016（平成28）年1月1日以降に対応。"
)

# 入力フォーム
col1, col2 = st.columns([1, 1])
with col1:
    st.write("利息の入金額（円）")
with col2:
    interest_amount = st.number_input(
        "",
        min_value=0,
        value=10000,
        step=1000,
        format="%d",
        label_visibility="collapsed",
    )

# 個人/法人の選択
col1, col2 = st.columns([1, 1])
with col1:
    st.write("区分")
with col2:
    tax_type = st.radio(
        "", ["個人", "法人"], horizontal=True, label_visibility="collapsed"
    )

# 水平線
st.markdown("---")

# 計算結果の表示領域
result_placeholder = st.empty()

# 所得税 15% + 復興特別所得税 0.315%
income_tax_rate = 0.15315

# 個人の場合は地方税5%、法人の場合は0%
local_tax_rate = 0.05 if tax_type == "個人" else 0

# 合計税率
total_tax_rate = income_tax_rate + local_tax_rate

# 税引前利息（割り戻し計算）
gross_interest = math.floor(interest_amount / (1 - total_tax_rate))

# 税金の計算
income_tax = math.floor(gross_interest * income_tax_rate)
local_tax = math.floor(gross_interest * local_tax_rate)

# 合計税額
total_tax = income_tax + local_tax

# 税引前利息（足し上げ）計算
gross_interes_final = interest_amount + total_tax

# 結果表示
with result_placeholder.container():
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("利息の入金額（円）")
    with col2:
        st.text_input(
            "",
            value=f"{interest_amount}",
            key="interest_result",
            disabled=True,
            label_visibility="collapsed",
        )

    col1, col2 = st.columns([1, 1])
    with col1:
        st.write(
            "所得税および復興特別所得税（円）",
            help="所得税（15%）+ 復興特別所得税（0.315%）",
        )
    with col2:
        st.text_input(
            "",
            value=f"{income_tax}",
            key="income_tax_result",
            disabled=True,
            label_visibility="collapsed",
        )

    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("地方税利子割（円）", help="地方税（5%）※個人のみ")
    with col2:
        st.text_input(
            "",
            value=f"{local_tax}",
            key="local_tax_result",
            disabled=True,
            label_visibility="collapsed",
        )

    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("源泉徴収合計（円）")
    with col2:
        st.text_input(
            "",
            value=f"{total_tax}",
            key="total_tax_result",
            disabled=True,
            label_visibility="collapsed",
        )

    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("利息の総額（円）")
    with col2:
        st.text_input(
            "",
            value=f"{gross_interes_final}",
            key="gross_interest_result",
            disabled=True,
            label_visibility="collapsed",
        )

# 源泉徴収税率の表示
st.subheader("源泉徴収税率")
st.markdown(
    """
- 個人: 20.315% = 所得税（15%）+ 復興特別所得税（0.315%）+ 地方税（5%）
- 法人: 15.315% = 所得税（15%）+ 復興特別所得税（0.315%）
"""
)

st.caption("円未満切り捨ての端数処理により、計算結果に誤差が発生する場合があります。")
