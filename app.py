import streamlit as st

st.set_page_config(page_title="TronPick Auto", page_icon="🚀")

st.title("🚀 TronPick Auto-Clicker")
st.markdown("**Fitaovana fifehezana ny Auto-Click amin'ny TronPick.io**")

st.divider()

# Fikirana
vitesse = st.slider("⚡ Hafainganana (millisecondes)", 500, 2000, 800, 50)
st.caption(f"Click isaky ny {vitesse}ms (~{round(60000/vitesse)} click/min)")

# Script vokarina
script_code = f"""// ==UserScript==
// @name         TronPick AutoClicker
// @match        *://*tronpick.io/*
// @grant        none
// ==/UserScript==

(function() {{
    console.log("🚀 TronPick AutoClicker Started");
    setInterval(() => {{
        const buttons = document.querySelectorAll('button, div[role="button"]');
        buttons.forEach(btn => {{
            const txt = (btn.innerText || '').toLowerCase();
            if(txt.includes('mine') || txt.includes('claim') || txt.includes('roll')) {{
                btn.click();
                console.log('✅ Clicked:', txt);
            }}
        }});
    }}, {vitesse});
}})();
"""

st.subheader("📋 Script ho an'ny Tampermonkey")
st.code(script_code, language="javascript")

st.info("👉 Adikao io script io ary apetaho ao amin'ny **Tampermonkey** (Kiwi Browser)")

st.divider()
st.caption("⚠️ Ampiasao amim-pahendrena")
