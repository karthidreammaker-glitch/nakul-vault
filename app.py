import streamlit as st
import streamlit.components.v1 as components

# 1. Page Setup
st.set_page_config(page_title="👶 The Big Reveal!", layout="centered", page_icon="✨")

# 2. Hide Streamlit's default developer chrome to make it feel like a native mobile app
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container { padding-top: 1rem; padding-bottom: 0rem; }
    </style>
""", unsafe_allow_html=True)

# 3. The Standalone HTML5 Arcade Game 
GAME_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nakul Reveal</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800;900&display=swap');
        body { font-family: 'Plus Jakarta Sans', sans-serif; background: #0f172a; color: #f8fafc; overflow-x: hidden; user-select: none; }
        .perspective { perspective: 1000px; }
        .transform-3d { transform-style: preserve-3d; transition: transform 0.5s cubic-bezier(0.4, 0.2, 0.2, 1); }
        .rotate-y-180 { transform: rotateY(180deg); }
        .backface-hidden { backface-visibility: hidden; }
        @keyframes float { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-6px); } }
        .floating { animation: float 3s ease-in-out infinite; }
    </style>
</head>
<body class="flex flex-col items-center justify-between min-h-screen p-4 max-w-md mx-auto">

    <div id="header-zone" class="text-center w-full pt-2">
        <span class="bg-indigo-500/10 border border-indigo-500/30 text-indigo-400 px-3.5 py-1 rounded-full text-xs font-black tracking-widest uppercase shadow-sm">
            Top Secret Moniker
        </span>
        <h1 class="text-2xl sm:text-3xl font-black tracking-tight mt-2 text-white">The Baby Name Reveal</h1>
        
        <div class="flex justify-center items-center gap-3 mt-2 text-xs font-bold text-slate-400">
            <span class="bg-slate-800/80 px-3 py-1 rounded-lg border border-slate-700">Mistakes: <span id="mistake-count" class="text-rose-400">0</span></span>
            <span class="bg-slate-800/80 px-3 py-1 rounded-lg border border-slate-700">Unlocked: <span id="found-count" class="text-emerald-400">0</span>/12</span>
        </div>
    </div>

    <div id="board-zone" class="w-full my-auto flex flex-col gap-3.5 items-center justify-center py-6">
        </div>

    <div id="victory-zone" class="hidden my-auto w-full flex-col items-center text-center bg-gradient-to-b from-indigo-950/90 to-slate-900 border-2 border-indigo-500/50 p-6 rounded-3xl shadow-2xl backdrop-blur-xl floating">
        <div class="text-5xl mb-2">👑</div>
        <div class="text-xs font-black uppercase tracking-widest text-indigo-300">Welcome to the Universe</div>
        <h2 class="text-3xl sm:text-4xl font-black text-white mt-1 mb-4 tracking-wider drop-shadow-md">NAKUL VEDANTH</h2>
        
        <div class="bg-slate-950/70 p-4 rounded-2xl border border-indigo-500/20 shadow-inner w-full">
            <p class="text-xs sm:text-sm text-indigo-200 italic font-medium leading-relaxed">
                "Two little feet, one giant leap of love,<br>
                Sent to our arms from the cosmos above.<br>
                With wisdom in your soul and wonder in your eyes,<br>
                Welcome Nakul Vedanth—our sweetest sunrise!"
            </p>
        </div>
        <button onclick="triggerConfetti()" class="mt-5 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold py-3 px-6 rounded-xl shadow-lg transition active:scale-95">
            🎉 Shower More Confetti!
        </button>
    </div>

    <div id="control-zone" class="w-full flex flex-col gap-3 pb-2 max-w-sm">
        <div id="hint-display" class="hidden text-center bg-indigo-950/60 border border-indigo-500/30 text-indigo-200 text-xs py-2.5 px-3 rounded-xl font-medium shadow-inner animate-pulse"></div>
        
        <button id="hint-btn" onclick="showHint()" class="w-full py-3 bg-slate-800 hover:bg-slate-700 active:scale-[0.98] border border-slate-700 rounded-xl text-xs font-extrabold text-indigo-400 transition shadow flex items-center justify-center gap-1.5">
            <span>💡</span> Tap for a Stork Hint
        </button>

        <div id="keyboard" class="grid grid-cols-7 gap-1.5 sm:gap-2 pt-1"></div>
    </div>

    <script>
        const words = ["NAKUL", "VEDANTH"];
        const secretString = "NAKULVEDANTH";
        const uniqueChars = new Set(secretString.split(''));

        let rightSet = new Set();
        let wrongSet = new Set();
        let mistakeCount = 0;

        const hints = [
            "💡 Hint 1: His first name belongs to the deeply wise, handsome 4th Pandava brother!",
            "💡 Hint 2: His second name translates to 'The Bearer of Ultimate Sacred Wisdom'.",
            "💡 Hint 3: There are exactly 4 unique vowels hidden across these tiles (A, E, U...).",
            "💡 Hint 4: Keep an eye out for the letter 'N'—it's a double feature!"
        ];
        let hintIdx = 0;

        function initBoard() {
            const dock = document.getElementById('board-zone');
            dock.innerHTML = '';

            words.forEach(w => {
                const row = document.createElement('div');
                row.className = 'flex gap-1.5 sm:gap-2 justify-center';

                w.split('').forEach(char => {
                    const isFound = rightSet.has(char);
                    const slot = document.createElement('div');
                    slot.className = 'perspective w-10 h-13 sm:w-12 sm:h-15';
                    
                    slot.innerHTML = `
                        <div class="transform-3d relative w-full h-full rounded-xl shadow-lg ${isFound ? 'rotate-y-180' : ''}">
                            <div class="backface-hidden absolute inset-0 bg-slate-800 border-2 border-slate-700 rounded-xl flex items-center justify-center text-slate-500 font-black text-xl sm:text-2xl shadow-inner">
                                ?
                            </div>
                            <div class="backface-hidden rotate-y-180 absolute inset-0 bg-gradient-to-br from-indigo-500 to-blue-600 rounded-xl flex items-center justify-center text-white font-black text-xl sm:text-2xl shadow-md border border-indigo-400/30">
                                ${char}
                            </div>
                        </div>
                    `;
                    row.appendChild(slot);
                });
                dock.appendChild(row);
            });

            // Update solved count
            let solvedCount = 0;
            secretString.split('').forEach(c => { if(rightSet.has(c)) solvedCount++; });
            document.getElementById('found-count').innerText = solvedCount;
        }

        function initKeyboard() {
            const kb = document.getElementById('keyboard');
            kb.innerHTML = '';
            const letters = "ABCDEFGHIJKLM-NOPQRSTUVWXYZ".split('');

            letters.forEach(l => {
                if (l === '-') {
                    kb.appendChild(document.createElement('div'));
                    return;
                }

                const btn = document.createElement('button');
                btn.innerText = l;

                let customStyle = "bg-slate-800 text-slate-200 border-slate-700 active:scale-95 shadow";
                if (rightSet.has(l)) customStyle = "bg-emerald-500/20 text-emerald-400 border-emerald-500/30 opacity-60 cursor-default";
                if (wrongSet.has(l)) customStyle = "bg-rose-950/30 text-rose-500 border-rose-800/30 opacity-30 cursor-default line-through";

                btn.className = `h-10 sm:h-11 rounded-xl font-extrabold text-sm sm:text-base border transition flex items-center justify-center ${customStyle}`;
                
                if (!rightSet.has(l) && !wrongSet.has(l)) {
                    btn.onclick = () => pressKey(l);
                }
                kb.appendChild(btn);
            });
        }

        function pressKey(char) {
            if (uniqueChars.has(char)) {
                rightSet.add(char);
                initBoard();
                initKeyboard();
                checkWinCondition();
            } else {
                wrongSet.add(char);
                mistakeCount++;
                document.getElementById('mistake-count').innerText = mistakeCount;
                initKeyboard();
            }
        }

        function showHint() {
            const display = document.getElementById('hint-display');
            display.innerText = hints[hintIdx];
            display.classList.remove('hidden');
            hintIdx = (hintIdx + 1) % hints.length;
        }

        function triggerConfetti() {
            confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 } });
        }

        function checkWinCondition() {
            if (rightSet.size === uniqueChars.size) {
                document.getElementById('header-zone').classList.add('hidden');
                document.getElementById('board-zone').classList.add('hidden');
                document.getElementById('control-zone').classList.add('hidden');
                
                const winZone = document.getElementById('victory-zone');
                winZone.classList.remove('hidden');
                winZone.classList.add('flex');

                // Triple wave confetti supernova
                setTimeout(() => confetti({ particleCount: 120, spread: 80, origin: { y: 0.6 } }), 100);
                setTimeout(() => confetti({ particleCount: 90, angle: 60, spread: 55, origin: { x: 0 } }), 400);
                setTimeout(() => confetti({ particleCount: 90, angle: 120, spread: 55, origin: { x: 1 } }), 750);
            }
        }

        initBoard();
        initKeyboard();
    </script>
</body>
</html>
"""

# 4. Mount the app into Streamlit
components.html(GAME_HTML, height=780)
