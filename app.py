import streamlit as st

st.set_page_config(page_title="TronPick Auto", page_icon="🚀", layout="centered")

st.title("🚀 TronPick Auto-Claimer")
st.markdown("**Fitaovana Auto-Claim isaky ny 65 minitra + Captcha detection**")

st.divider()

# Fikirana
col1, col2 = st.columns(2)
with col1:
    minitra = st.number_input("⏰ Elanelana (minitra)", 60, 120, 65, 1)
with col2:
    captcha_wait = st.number_input("🧩 Fiandrasana Captcha (segondra)", 10, 120, 30, 5)

st.info(f"🕐 Hanao **claim iray isaky ny {minitra} minitra**\n\n🧩 Hijanona **{captcha_wait} segondra** raha misy Captcha")

st.divider()

# Script vokarina
interval_ms = minitra * 60 * 1000
captcha_ms = captcha_wait * 1000

script_code = f"""// ==UserScript==
// @name         TronPick Auto-Claimer Pro
// @namespace    https://tronpick.io
// @version      3.0
// @description  Auto claim isaky ny {minitra} minitra + Captcha handler
// @match        *://*tronpick.io/*
// @grant        none
// @run-at       document-idle
// ==/UserScript==

(function() {{
    'use strict';
    
    const CLAIM_INTERVAL = {interval_ms}; // {minitra} minitra
    const CAPTCHA_WAIT = {captcha_ms};    // {captcha_wait} segondra
    let claimCount = 0;
    
    console.log("%c🚀 TronPick Auto-Claimer v3.0 STARTED", "color:lime;font-size:16px;font-weight:bold");
    console.log("⏰ Claim isaky ny {minitra} minitra");
    
    // === FONCTION: Mitady Captcha ===
    function detectCaptcha() {{
        // hCaptcha
        const hcaptcha = document.querySelector('iframe[src*="hcaptcha"], iframe[title*="hCaptcha"], .h-captcha');
        // reCaptcha
        const recaptcha = document.querySelector('iframe[src*="recaptcha"], .g-recaptcha');
        // Cloudflare
        const cloudflare = document.querySelector('iframe[src*="cloudflare"], .cf-turnstile');
        
        return hcaptcha || recaptcha || cloudflare;
    }}
    
    // === FONCTION: Mitady Bokotra Claim ===
    function findClaimButton() {{
        const buttons = document.querySelectorAll('button, input[type="submit"], input[type="button"], a.btn, div[role="button"]');
        for (let btn of buttons) {{
            const txt = (btn.innerText || btn.value || '').toLowerCase().trim();
            if (txt === 'claim' || txt === 'roll' || txt === 'mine' || 
                txt.includes('claim now') || txt.includes('start mining') ||
                txt.includes('claim reward')) {{
                return btn;
            }}
        }}
        return null;
    }}
    
    // === FONCTION PRINCIPALE: Auto Claim ===
    async function doClaim() {{
        console.log("%c🎯 Manomboka claim...", "color:cyan;font-size:14px");
        
        // Etape 1: Tadiavo ny bokotra Claim
        const claimBtn = findClaimButton();
        
        if (!claimBtn) {{
            console.log("⚠️ Tsy hita ny bokotra Claim. Andrasana claim manaraka...");
            return;
        }}
        
        // Etape 2: Tsindrio ny bokotra
        claimBtn.click();
        console.log("✅ Bokotra Claim voatsindry!");
        
        // Etape 3: Andraso 3 segondra dia jereo raha misy Captcha
        setTimeout(async () => {{
            const captcha = detectCaptcha();
            
            if (captcha) {{
                console.log("%c🧩 CAPTCHA HITA! Ataovy manually...", "color:orange;font-size:18px;font-weight:bold");
                
                // Alerte visuel
                showAlert("🧩 CAPTCHA ILAINA! Vahao haingana!");
                
                // Feo
                playSound();
                
                // Andraso ny mpampiasa hamaha ny captcha
                console.log(`⏳ Fiandrasana {captcha_wait} segondra...`);
                
                setTimeout(() => {{
                    // Aorian'ny captcha, tsindrio Claim indray raha ilaina
                    const finalBtn = findClaimButton();
                    if (finalBtn) {{
                        finalBtn.click();
                        console.log("✅ Bokotra farany voatsindry!");
                    }}
                    claimCount++;
                    console.log(`%c🏆 Claim #${{claimCount}} vita!`, "color:gold;font-size:16px");
                }}, CAPTCHA_WAIT);
                
            }} else {{
                claimCount++;
                console.log(`%c🏆 Claim #${{claimCount}} vita (tsy misy captcha)!`, "color:gold;font-size:16px");
            }}
        }}, 3000);
    }}
    
    // === FONCTION: Alerte ===
    function showAlert(msg) {{
        const div = document.createElement('div');
        div.style.cssText = `
            position:fixed; top:20px; left:50%; transform:translateX(-50%);
            background:red; color:white; padding:20px 40px;
            font-size:20px; font-weight:bold; z-index:99999;
            border-radius:10px; box-shadow:0 0 20px red;
            animation: blink 1s infinite;
        `;
        div.innerText = msg;
        document.body.appendChild(div);
        setTimeout(() => div.remove(), {captcha_wait * 1000});
    }}
    
    // === FONCTION: Feo Fampitandremana ===
    function playSound() {{
        try {{
            const audio = new AudioContext();
            const osc = audio.createOscillator();
            osc.frequency.value = 800;
            osc.connect(audio.destination);
            osc.start();
            setTimeout(() => osc.stop(), 500);
        }} catch(e) {{}}
    }}
    
    // === Manomboka: Claim voalohany aorian'ny 5 segondra ===
    setTimeout(doClaim, 5000);
    
    // === Claim isaky ny X minitra ===
    setInterval(doClaim, CLAIM_INTERVAL);
    
    // === Compteur miseho eo amin'ny pejy ===
    const counter = document.createElement('div');
    counter.id = 'auto-claim-counter';
    counter.style.cssText = `
        position:fixed; bottom:10px; right:10px;
        background:rgba(0,255,0,0.8); color:black;
        padding:10px 15px; font-weight:bold;
        z-index:99999; border-radius:8px;
        font-family:monospace; font-size:13px;
    `;
    counter.innerText = "🚀 Auto-Claim ACTIVE";
    document.body.appendChild(counter);
    
}})();
"""

st.subheader("📋 Script ho an'ny Tampermonkey")
st.code(script_code, language="javascript")

st.success("👉 Adikao io script io ary apetaho ao amin'ny **Tampermonkey**")

st.divider()

with st.expander("📖 Fomba fampiasana"):
    st.markdown(f"""
    ### 🎯 Ahoana no fiasan'ilay Script:
    
    1. **Manomboka**: 5 segondra aorian'ny fisokafan'ny pejy, hanao claim voalohany izy.
    
    2. **Claim mahazatra**: Isaky ny **{minitra} minitra**, hitady sy hitsindry ny bokotra "Claim" izy.
    
    3. **Captcha Detection**:
       - Raha misy Captcha (hCaptcha, reCaptcha, Cloudflare) → **hijanona {captcha_wait} segondra**
       - Hisy **alerte mena** miseho eo ambony pejy
       - Hisy **feo** hampandre anao
       - **Ianao no mamaha manually** ny Captcha
       - Aorian'ny fiandrasana, hitsindry Claim indray izy
    
    4. **Compteur**: Hita eo amin'ny **zoro havanana ambany** ny statuts.
    
    ### 💡 Torohevitra:
    - Aza akatona ny pejy TronPick.
    - Ampio **feo** ny finday mba handrenesanao raha misy Captcha.
    - Ovay isan'andro ny elanelana (65-75 minitra) mba tsy ho hitan'ny anti-bot.
    """)

st.caption("⚠️ Ampiasao amim-pahendrena • Made with ❤️")
