import streamlit as st
import streamlit.components.v1 as components

# 1. Page Setup
st.set_page_config(page_title="👶 Nakul Vedanth Reveal!", layout="centered", page_icon="✨")

# 2. Strip Streamlit's branding entirely 
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container { padding-top: 0.2rem; padding-bottom: 0rem; }
    </style>
""", unsafe_allow_html=True)

# 3. The Standalone Deluxe HTML5 Web App
DELUXE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nakul Deluxe</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;800;900&display=swap');
        body { font-family: 'Outfit', sans-serif; background: #070913; color: #f8fafc; overflow-x: hidden; user-select: none; margin:0; }
        .perspective { perspective: 1000px; }
        .transform-3d { transform-style: preserve-3d; transition: transform 0.6s cubic-bezier(0.34, 1.56, 0.64, 1); }
        .rotate-y-180 { transform: rotateY(180deg); }
        .backface-hidden { backface-visibility: hidden; }
        
        @keyframes float { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-6px); } }
        .floating { animation: float 3s ease-in-out infinite; }
    </style>
</head>
<body class="relative flex flex-col items-center justify-between min-h-screen p-3 sm:p-4 max-w-md mx-auto z-10">

    <canvas id="starfield" class="absolute inset-0 pointer-events-none z-0 opacity-60"></canvas>

    <div class="relative z-10 w-full flex flex-col items-center justify-between min-h-[95vh]">
        
        <div id="header-zone" class="text-center w-full pt-1">
            <div class="inline-flex items-center gap-1.5 bg-gradient-to-r from-amber-500/10 via-indigo-500/20 to-amber-500/10 border border-indigo-500/30 text-indigo-300 px-4 py-1 rounded-full text-xs font-black tracking-widest uppercase shadow-inner">
                <span class="animate-bounce">✨</span> Top Secret Mission
            </div>
            <h1 class="text-2xl sm:text-3xl font-black tracking-tight mt-1.5 bg-gradient-to-r from-white via-indigo-100 to-indigo-300 bg-clip-text text-transparent">
                Crack The Baby Vault
            </h1>
            
            <div class="flex justify-center items-center gap-2.5 mt-2 text-xs font-extrabold">
                <span class="bg-slate-900/90 text-slate-300 px-3 py-1 rounded-xl border border-rose-500/30 shadow-sm flex items-center gap-1">
                    <span class="text-rose-400">⚡ Mistakes:</span> 
                    <span id="mistake-count" class="text-rose-400 font-black text-sm">0</span>
                </span>
                <span class="bg-slate-900/90 text-slate-300 px-3 py-1 rounded-xl border border-emerald-500/30 shadow-sm flex items-center gap-1">
                    <span class="text-emerald-400">🔒 Unlocked:</span> 
                    <span id="found-count" class="text-emerald-400 font-black text-sm">0</span><span class="text-slate-500">/12</span>
                </span>
            </div>
        </div>

        <div id="board-zone" class="w-full my-auto flex flex-col gap-3 sm:gap-4 items-center justify-center py-3">
            </div>

        <div id="victory-zone" class="hidden my-auto w-full flex-col items-center text-center bg-gradient-to-b from-indigo-950/95 via-slate-900/95 to-slate-950 border-2 border-amber-400/60 p-6 rounded-3xl shadow-[0_0_50px_rgba(79,70,229,0.3)] backdrop-blur-2xl floating">
            <div class="text-5xl sm:text-6xl mb-1 animate-bounce">👑</div>
            <div class="text-[10px] font-black uppercase tracking-widest text-amber-400/90 bg-amber-400/10 px-3 py-0.5 rounded-full border border-amber-400/20 mb-1">
                Vault Successfully Decrypted
            </div>
            <h2 class="text-3xl sm:text-4xl font-black text-white mt-1 mb-3 tracking-wider drop-shadow-[0_2px_10px_rgba(255,255,255,0.4)]">
                NAKUL VEDANTH
            </h2>
            
            <div class="bg-slate-950/80 p-4 rounded-2xl border border-indigo-500/30 shadow-inner w-full relative overflow-hidden">
                <div class="absolute -right-6 -bottom-6 w-24 h-24 bg-indigo-500/10 rounded-full blur-xl pointer-events-none"></div>
                <p class="text-xs sm:text-sm text-indigo-100 italic font-medium leading-relaxed m-0">
                    "Two little feet, one giant leap of love,<br>
                    Sent to our arms from the cosmos above.<br>
                    With wisdom in your soul and wonder in your eyes,<br>
                    Welcome Nakul Vedanth—our sweetest sunrise!"
                </p>
            </div>

            <div class="flex flex-col sm:flex-row gap-2.5 w-full mt-4">
                <button onclick="triggerConfetti(); sfxWin();" class="flex-1 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-extrabold py-3.5 px-4 rounded-xl shadow-lg transition active:scale-95 flex items-center justify-center gap-1.5">
                    <span>🎉</span> More Confetti!
                </button>
                
                <a id="wa-btn" href="#" target="_blank" class="flex-1 bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-extrabold py-3.5 px-4 rounded-xl shadow-lg transition active:scale-95 flex items-center justify-center gap-1.5">
                    <span>💬</span> Brag on WhatsApp
                </a>
            </div>
        </div>

        <div id="control-zone" class="w-full flex flex-col gap-2 pb-1 max-w-sm">
            <div id="hint-display" class="hidden text-center bg-indigo-950/90 border border-indigo-400/30 text-indigo-200 text-xs py-2 px-3 rounded-xl font-semibold shadow-inner"></div>
            
            <button id="hint-btn" onclick="showHint()" class="w-full py-2.5 bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 hover:from-indigo-950 hover:to-slate-900 active:scale-[0.98] border border-indigo-500/30 rounded-xl text-xs font-extrabold text-indigo-300 transition shadow-lg flex items-center justify-center gap-2">
                <span class="text-amber-400 text-sm">💡</span> 
                <span>Tap for a Stork Hint</span>
            </button>

            <div id="keyboard" class="grid grid-cols-7 gap-1.5 sm:gap-2 pt-1"></div>
        </div>

    </div>

    <script>
        // NATIVE SYNTHESIZER AUDIO ENGINE
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        let audioCtx = null;

        function initAudio() { if(!audioCtx) audioCtx = new AudioContext(); }

        function playTone(freq, type, duration) {
            try {
                initAudio();
                let osc = audioCtx.createOscillator();
                let gain = audioCtx.createGain();
                osc.type = type; osc.frequency.value = freq;
                osc.connect(gain); gain.connect(audioCtx.destination);
                osc.start();
                gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + duration);
                osc.stop(audioCtx.currentTime + duration);
            } catch(e){}
        }

        function sfxTap() { playTone(550, 'sine', 0.04); }
        function sfxReveal() { [523.25, 659.25, 783.99, 1046.50].forEach((f, i) => setTimeout(() => playTone(f, 'triangle', 0.18), i * 55)); }
        function sfxWrong() { playTone(160, 'sawtooth', 0.12); setTimeout(() => playTone(110, 'sawtooth', 0.2), 90); }
        function sfxWin() { [440, 554.37, 659.25, 880, 880, 880].forEach((n, i) => setTimeout(() => playTone(n, 'triangle', 0.25), i * 130)); }

        // BACKGROUND STARFIELD
        const canvas = document.getElementById('starfield');
        const ctx = canvas.getContext('2d');
        function resizeCanvas() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
        window.addEventListener('resize', resizeCanvas); resizeCanvas();

        const stars = Array(65).fill().map(() => ({
