# -*- coding: utf-8 -*-
"""
Generator script for Zlata's 6-Month Anniversary Website (index.html)
Redesigned with cute, modern motion, tactile physics, and Celamur 3D Galaxy.
"""

import json
import os

# Load base64 portrait
with open('d:/подарки пол года/media/celamur_portrait_base64.txt', 'r', encoding='utf-8') as f:
    celamur_base64 = f.read().strip()

# Load galaxy particles
with open('d:/подарки пол года/media/galaxy_particles.json', 'r', encoding='utf-8') as f:
    particles_data = f.read().strip()

# Verified authentic memories (NO elevator photo! Elevator photo is exclusive to Celamur portrait)
memory_files = [
    {"name": "с чего все началось.jpg", "caption": "С чего всё началось 🤍", "date": "Начало нашей истории"},
    {"name": "первые цветы.jpg", "caption": "Твои первые цветы 💐", "date": "Самый нежный момент"},
    {"name": "свидание на природе.jpg", "caption": "Наше свидание на природе 🌿", "date": "Только ты и я"},
    {"name": "свидание на природе 2 фото.jpg", "caption": "Тёплые моменты на свежем воздухе 🍃", "date": "Улыбки и тепло"},
    {"name": "IMG_20261115_230355_318.jpg", "caption": "Солнечный день на крыше ☀️", "date": "Ближе к небу"},
    {"name": "IMG_20261115_230620_235.jpg", "caption": "Твоя красота и нежность ✨", "date": "Не могу оторвать взгляд"},
    {"name": "IMG_20261115_232741_361.jpg", "caption": "Уютный кофе вдвоём ☕", "date": "Тёплые разговоры"},
    {"name": "IMG_20261115_233109_723.jpg", "caption": "Счастливы вместе 🤍", "date": "Настоящие мы"},
    {"name": "IMG_20261116_000248_096.jpg", "caption": "Навсегда в моём сердце 💌", "date": "Любимый кадр"},
    {"name": "5462926877434519487.jpg", "caption": "Твоя любимая улыбка 🥰", "date": "Самая милая"},
    {"name": "5462926877434519488.jpg", "caption": "Счастье в простых моментах 🍓", "date": "Вкусные радости"},
    {"name": "5462926877434519489.jpg", "caption": "Всегда рядом с тобой 🤍", "date": "Наше тепло"},
    {"name": "5462926877434519490.jpg", "caption": "Самая прекрасная ✨", "date": "Моё вдохновение"},
    {"name": "5462926877434519491.jpg", "caption": "Любимый взгляд 💫", "date": "В твоих глазах весь мир"},
    {"name": "мы самые яркие звезды.mp4", "caption": "Мы — самые яркие звёзды ✨", "date": "Наше сияние 🎬"},
    {"name": "video5462926876974558922.mp4", "caption": "Наши живые мгновения 🎬", "date": "Моменты счастья"},
    {"name": "video5462926876974558921.mp4", "caption": "Тёплые воспоминания 🎞️", "date": "Лето нашей любви"},
    {"name": "HnVideoEditor_2026_11_16_002803168.mp4", "caption": "История нашей любви 💖", "date": "Полгода вместе"}
]

memory_files_json = json.dumps(memory_files, ensure_ascii=False)

html_template = f'''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>Злата — Наша Вселенная 🤍</title>
  
  <!-- Premium Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Great+Vibes&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
    :root {{
      --bg: #030105;
      --card-bg: rgba(26, 18, 30, 0.7);
      --card-border: rgba(255, 255, 255, 0.1);
      --accent-pink: #ff6088;
      --accent-gradient: linear-gradient(135deg, #ff7597 0%, #ff4b72 100%);
      --accent-glow: rgba(255, 96, 136, 0.45);
      --gold: #ffeaa7;
      --text-main: #ffffff;
      --text-muted: #b4a8ba;
      --font-cursive: 'Caveat', 'Great Vibes', cursive;
      --font-title: 'Great Vibes', cursive;
      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
      -webkit-user-select: none;
      -webkit-tap-highlight-color: transparent;
    }}

    html, body {{
      width: 100%;
      height: 100%;
      background: var(--bg);
      color: var(--text-main);
      font-family: var(--font-sans);
      overflow: hidden;
      position: fixed;
    }}

    /* Dynamic starry ambient canvas */
    #spaceStarsCanvas {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 0;
    }}

    /* Glow blobs */
    .ambient-glow {{
      position: fixed;
      width: 320px;
      height: 320px;
      border-radius: 50%;
      filter: blur(80px);
      pointer-events: none;
      z-index: 0;
      opacity: 0.35;
      animation: floatGlow 10s infinite alternate ease-in-out;
    }}
    .glow-1 {{
      top: -60px;
      left: 50%;
      transform: translateX(-50%);
      background: radial-gradient(circle, #ff5277, transparent 70%);
    }}
    .glow-2 {{
      bottom: -60px;
      right: -40px;
      background: radial-gradient(circle, #7d2ae8, transparent 70%);
      animation-delay: -5s;
    }}
    @keyframes floatGlow {{
      0% {{ transform: translate(-50%, 0) scale(0.9); }}
      100% {{ transform: translate(-50%, 40px) scale(1.15); }}
    }}

    /* Screen containers */
    .screen {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 24px 20px;
      opacity: 0;
      pointer-events: none;
      transform: scale(0.94) translateY(20px);
      transition: opacity 0.5s cubic-bezier(0.34, 1.56, 0.64, 1), transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
      z-index: 1;
      overflow-y: auto;
      -webkit-overflow-scrolling: touch;
    }}

    .screen.active {{
      opacity: 1;
      pointer-events: auto;
      transform: scale(1) translateY(0);
      z-index: 2;
    }}

    /* Minimalist status bar / navigation */
    .top-nav-bar {{
      position: fixed;
      top: 16px;
      left: 0;
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 20px;
      z-index: 50;
      pointer-events: none;
    }}

    .progress-hearts {{
      display: flex;
      gap: 6px;
      pointer-events: auto;
      background: rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      padding: 6px 12px;
      border-radius: 9999px;
      border: 1px solid rgba(255, 255, 255, 0.1);
    }}
    .progress-hearts span {{
      font-size: 13px;
      opacity: 0.3;
      transform: scale(0.85);
      transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    .progress-hearts span.filled {{
      opacity: 1;
      transform: scale(1.1);
      filter: drop-shadow(0 0 6px var(--accent-pink));
    }}

    .music-btn {{
      pointer-events: auto;
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.12);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      cursor: pointer;
      box-shadow: 0 4px 15px rgba(0,0,0,0.4);
      transition: all 0.25s ease;
    }}
    .music-btn:active {{
      transform: scale(0.9);
    }}
    .music-btn.playing {{
      border-color: var(--accent-pink);
      color: var(--accent-pink);
      box-shadow: 0 0 15px var(--accent-glow);
      animation: pulseMusic 2s infinite ease-in-out;
    }}
    @keyframes pulseMusic {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.08); }}
    }}

    /* ========================================================
       SCREEN 1: THE PLAYFUL HOOK (TRY 'NO' FIRST!)
       ======================================================== */
    .hook-card {{
      max-width: 360px;
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      gap: 16px;
      position: relative;
    }}

    /* Floating cute sticker emojis */
    .floating-sticker {{
      position: absolute;
      font-size: 24px;
      pointer-events: none;
      animation: floatSticker 3.5s infinite ease-in-out alternate;
      filter: drop-shadow(0 4px 10px rgba(0,0,0,0.5));
    }}
    .st-1 {{ top: 10px; left: -10px; animation-delay: 0s; }}
    .st-2 {{ top: 25px; right: -8px; animation-delay: -1.2s; }}
    .st-3 {{ bottom: 120px; left: 10px; animation-delay: -2s; font-size: 20px; }}
    .st-4 {{ bottom: 130px; right: 15px; animation-delay: -0.7s; font-size: 22px; }}
    @keyframes floatSticker {{
      0% {{ transform: translateY(0) rotate(-6deg); }}
      100% {{ transform: translateY(-10px) rotate(8deg); }}
    }}

    .avatar-box {{
      position: relative;
      width: 130px;
      height: 130px;
      margin-top: 10px;
    }}
    .avatar-halo {{
      position: absolute;
      inset: -8px;
      border-radius: 42px;
      background: var(--accent-gradient);
      opacity: 0.6;
      filter: blur(14px);
      animation: haloPulse 3s infinite alternate ease-in-out;
    }}
    @keyframes haloPulse {{
      0% {{ transform: scale(0.92); opacity: 0.4; }}
      100% {{ transform: scale(1.08); opacity: 0.8; }}
    }}
    .avatar-img-squircle {{
      position: relative;
      width: 100%;
      height: 100%;
      border-radius: 36px;
      object-fit: cover;
      border: 2px solid rgba(255, 255, 255, 0.4);
      box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6);
    }}

    .hook-badge-pill {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 16px;
      border-radius: 9999px;
      background: rgba(255, 96, 136, 0.12);
      border: 1px solid rgba(255, 96, 136, 0.3);
      color: #ff9bb5;
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 0.5px;
    }}

    .hook-headline {{
      font-family: var(--font-cursive);
      font-size: 48px;
      font-weight: 700;
      color: #ffffff;
      line-height: 1;
      text-shadow: 0 0 25px rgba(255, 140, 180, 0.6);
    }}

    .hook-sub {{
      font-size: 19px;
      color: #ede2f0;
      font-weight: 500;
      line-height: 1.3;
      margin-top: -6px;
    }}

    /* Instruction badge to force trying 'NO' */
    .hook-try-no-hint {{
      background: rgba(255, 234, 167, 0.12);
      border: 1px dashed rgba(255, 234, 167, 0.45);
      color: #ffeaa7;
      padding: 8px 16px;
      border-radius: 14px;
      font-size: 13px;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 8px;
      animation: hintWiggle 2s infinite ease-in-out;
    }}
    @keyframes hintWiggle {{
      0%, 100% {{ transform: translateX(0); }}
      25% {{ transform: translateX(-4px); }}
      75% {{ transform: translateX(4px); }}
    }}

    /* Playground for buttons */
    .hook-buttons-area {{
      position: relative;
      width: 100%;
      min-height: 140px;
      margin-top: 6px;
    }}

    .btn-action-yes {{
      width: 100%;
      background: var(--accent-gradient);
      color: #ffffff;
      border: none;
      padding: 16px 28px;
      border-radius: 9999px;
      font-size: 16px;
      font-weight: 700;
      cursor: pointer;
      box-shadow: 0 10px 30px var(--accent-glow);
      transition: all 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }}
    .btn-action-yes:active {{
      transform: scale(0.95);
    }}
    .btn-action-yes.locked {{
      background: rgba(255, 255, 255, 0.08);
      color: rgba(255, 255, 255, 0.35);
      box-shadow: none;
      cursor: not-allowed;
      border: 1px solid rgba(255, 255, 255, 0.1);
    }}
    .btn-action-yes.unlocked-pulse {{
      animation: unlockPulse 1.2s infinite alternate ease-in-out;
    }}
    @keyframes unlockPulse {{
      0% {{ transform: scale(1); box-shadow: 0 8px 25px var(--accent-glow); }}
      100% {{ transform: scale(1.05); box-shadow: 0 12px 40px rgba(255, 96, 136, 0.7); }}
    }}

    /* Dodging NO button */
    .btn-action-no {{
      position: absolute;
      top: 68px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(255, 255, 255, 0.08);
      color: #ff85a1;
      border: 1.5px solid rgba(255, 96, 136, 0.4);
      padding: 12px 34px;
      border-radius: 9999px;
      font-size: 15px;
      font-weight: 700;
      cursor: pointer;
      transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1), background 0.2s, opacity 0.2s;
      white-space: nowrap;
      z-index: 10;
    }}
    .btn-action-no:hover, .btn-action-no:active {{
      background: rgba(255, 96, 136, 0.2);
    }}

    /* Cute speech bubble reaction */
    .bubble-reaction {{
      position: absolute;
      top: -38px;
      left: 50%;
      transform: translateX(-50%) scale(0.8);
      background: #ffffff;
      color: #1a0f1d;
      padding: 6px 14px;
      border-radius: 12px;
      font-size: 12px;
      font-weight: 700;
      white-space: nowrap;
      box-shadow: 0 8px 20px rgba(0,0,0,0.5);
      opacity: 0;
      pointer-events: none;
      transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    .bubble-reaction::after {{
      content: '';
      position: absolute;
      bottom: -6px;
      left: 50%;
      transform: translateX(-50%);
      border-width: 6px 6px 0 6px;
      border-style: solid;
      border-color: #ffffff transparent transparent transparent;
    }}
    .bubble-reaction.show {{
      opacity: 1;
      transform: translateX(-50%) scale(1);
    }}

    /* ========================================================
       SCREEN 2: THE QUIZ (MODERN CAROUSEL CARD)
       ======================================================== */
    .quiz-layout {{
      max-width: 400px;
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .quiz-card-bubble {{
      width: 100%;
      background: rgba(30, 20, 36, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.12);
      backdrop-filter: blur(25px);
      -webkit-backdrop-filter: blur(25px);
      border-radius: 32px;
      padding: 26px 22px;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.7);
      display: flex;
      flex-direction: column;
      gap: 18px;
      position: relative;
    }}

    .quiz-meta-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .quiz-tag {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: #ff9bb5;
    }}
    .quiz-step-bubble {{
      background: rgba(255, 255, 255, 0.08);
      padding: 4px 10px;
      border-radius: 9999px;
      font-size: 11px;
      font-weight: 700;
      color: var(--text-muted);
    }}

    .quiz-q-title {{
      font-size: 19px;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.35;
      text-align: left;
    }}

    .quiz-options-grid {{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .quiz-option-pill {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 15px 18px;
      border-radius: 20px;
      color: #ece1f0;
      font-size: 14px;
      font-weight: 600;
      text-align: left;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    .quiz-option-pill:active {{
      transform: scale(0.97);
    }}
    .quiz-option-pill.correct {{
      background: rgba(46, 213, 115, 0.2);
      border-color: #2ed573;
      color: #ffffff;
      transform: scale(1.02);
      box-shadow: 0 0 20px rgba(46, 213, 115, 0.4);
    }}
    .quiz-option-pill.wrong {{
      background: rgba(255, 71, 87, 0.2);
      border-color: #ff4757;
      color: #ff6b81;
      animation: shakeCard 0.4s ease;
    }}
    @keyframes shakeCard {{
      0%, 100% {{ transform: translateX(0); }}
      25% {{ transform: translateX(-8px); }}
      75% {{ transform: translateX(8px); }}
    }}

    .quiz-reaction-toast {{
      font-size: 13px;
      font-weight: 600;
      color: #ff8fab;
      text-align: center;
      min-height: 20px;
    }}

    /* ========================================================
       SCREEN 3: CELAMUR PORTRAIT & 3D SPIRAL GALAXY
       ======================================================== */
    .celamur-layout {{
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
      padding: 20px 16px 28px 16px;
    }}

    .celamur-stage {{
      position: relative;
      width: 100%;
      max-width: 420px;
      height: 480px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-top: 10px;
    }}

    #galaxyCanvas {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 2;
      touch-action: none;
      cursor: grab;
    }}
    #galaxyCanvas:active {{
      cursor: grabbing;
    }}

    /* Controls beneath canvas */
    .celamur-meta {{
      width: 100%;
      max-width: 380px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 10px;
      z-index: 10;
    }}

    .celamur-play-circle {{
      width: 50px;
      height: 50px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.12);
      border: 1.5px solid rgba(255, 255, 255, 0.2);
      backdrop-filter: blur(15px);
      -webkit-backdrop-filter: blur(15px);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      cursor: pointer;
      box-shadow: 0 8px 25px rgba(0, 0, 0, 0.6);
      transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    .celamur-play-circle:active {{
      transform: scale(0.9);
    }}
    .celamur-play-circle svg {{
      width: 22px;
      height: 22px;
      fill: currentColor;
    }}

    .celamur-signature {{
      font-family: var(--font-title);
      font-size: 46px;
      line-height: 1;
      color: #ffffff;
      text-shadow: 0 0 25px rgba(255, 180, 210, 0.7);
      margin-top: -2px;
    }}

    .celamur-sub-1 {{
      font-size: 15px;
      font-weight: 500;
      color: #f1e4f0;
      letter-spacing: 0.3px;
    }}

    .celamur-sub-2 {{
      font-size: 13px;
      font-weight: 500;
      color: #ff8fab;
      margin-top: -4px;
    }}

    .celamur-swipe-hint {{
      font-size: 11px;
      color: rgba(255, 255, 255, 0.45);
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    .celamur-buttons-stack {{
      display: flex;
      flex-direction: column;
      gap: 10px;
      width: 100%;
      margin-top: 6px;
    }}

    .btn-pill-pink {{
      background: var(--accent-gradient);
      color: #ffffff;
      border: none;
      padding: 15px 28px;
      border-radius: 9999px;
      font-size: 15px;
      font-weight: 700;
      cursor: pointer;
      box-shadow: 0 8px 25px var(--accent-glow);
      transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }}
    .btn-pill-pink:active {{
      transform: scale(0.96);
    }}

    .btn-pill-glass {{
      background: rgba(255, 255, 255, 0.08);
      color: #ede4f0;
      border: 1px solid rgba(255, 255, 255, 0.14);
      padding: 14px 28px;
      border-radius: 9999px;
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      backdrop-filter: blur(15px);
      -webkit-backdrop-filter: blur(15px);
      transition: all 0.25s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }}
    .btn-pill-glass:active {{
      transform: scale(0.96);
    }}

    /* ========================================================
       SCREEN 4: ANNIVERSARY TIMER & MEMORIES
       ======================================================== */
    .finale-layout {{
      max-width: 420px;
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;
      text-align: center;
    }}

    .finale-header-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 16px;
      border-radius: 9999px;
      background: rgba(255, 96, 136, 0.12);
      border: 1px solid rgba(255, 96, 136, 0.3);
      color: #ff9bb5;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 1px;
    }}

    .finale-headline {{
      font-family: var(--font-title);
      font-size: 48px;
      line-height: 1;
      color: #ffffff;
      text-shadow: 0 0 25px rgba(255, 180, 200, 0.6);
    }}

    /* Modern timer squircle cards */
    .timer-cards-row {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
      width: 100%;
    }}

    .timer-squircle {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 20px;
      padding: 14px 4px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
      backdrop-filter: blur(15px);
      -webkit-backdrop-filter: blur(15px);
    }}
    .timer-num {{
      font-size: 26px;
      font-weight: 800;
      color: #ffffff;
      font-variant-numeric: tabular-nums;
      line-height: 1;
    }}
    .timer-sub {{
      font-size: 10px;
      color: var(--text-muted);
      text-transform: uppercase;
      font-weight: 700;
      letter-spacing: 0.8px;
    }}

    /* Verbatim quote in aesthetic handwritten style */
    .polaroid-quote {{
      background: rgba(255, 255, 255, 0.04);
      border-left: 3px solid var(--accent-pink);
      border-radius: 6px 20px 20px 6px;
      padding: 18px 20px;
      font-size: 14px;
      line-height: 1.6;
      color: #ede2f0;
      font-style: italic;
      text-align: left;
      position: relative;
      backdrop-filter: blur(15px);
    }}
    .polaroid-quote::before {{
      content: '“';
      position: absolute;
      top: -10px;
      left: 10px;
      font-size: 40px;
      color: rgba(255, 96, 136, 0.3);
      font-family: serif;
    }}

    .btn-memories-open {{
      background: var(--accent-gradient);
      color: #ffffff;
      border: none;
      padding: 16px 32px;
      border-radius: 9999px;
      font-size: 15px;
      font-weight: 700;
      cursor: pointer;
      box-shadow: 0 10px 30px var(--accent-glow);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      width: 100%;
      transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    .btn-memories-open:active {{
      transform: scale(0.96);
    }}

    /* ========================================================
       MEMORIES MODAL / STORY SLIDER (NO ELEVATOR PHOTO)
       ======================================================== */
    .story-modal {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.95);
      backdrop-filter: blur(30px);
      -webkit-backdrop-filter: blur(30px);
      z-index: 1000;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 20px 16px;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.4s ease;
    }}
    .story-modal.open {{
      opacity: 1;
      pointer-events: auto;
    }}

    .story-close-btn {{
      position: absolute;
      top: 20px;
      right: 20px;
      width: 42px;
      height: 42px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #fff;
      font-size: 24px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 1010;
      transition: all 0.2s ease;
    }}
    .story-close-btn:active {{
      transform: scale(0.9);
    }}

    .story-frame {{
      max-width: 420px;
      width: 100%;
      background: rgba(24, 16, 28, 0.9);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 32px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.85);
    }}

    .story-media-container {{
      width: 100%;
      height: 380px;
      background: #000000;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }}

    .story-img {{
      width: 100%;
      height: 100%;
      object-fit: contain;
      transition: opacity 0.3s ease;
    }}

    .story-video {{
      width: 100%;
      height: 100%;
      object-fit: contain;
    }}

    .story-bottom-info {{
      padding: 18px 20px 22px 20px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      text-align: center;
    }}

    .story-date-tag {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: #ff9bb5;
    }}

    .story-caption-text {{
      font-size: 16px;
      font-weight: 600;
      color: #ffffff;
      margin-top: -6px;
    }}

    .story-counter-dots {{
      font-size: 12px;
      color: var(--text-muted);
      font-weight: 600;
      letter-spacing: 1px;
    }}

    .story-nav-buttons {{
      display: flex;
      gap: 10px;
      width: 100%;
    }}

    .story-btn-nav {{
      flex: 1;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 13px;
      border-radius: 9999px;
      color: #ffffff;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.2s ease;
    }}
    .story-btn-nav:active {{
      background: rgba(255, 255, 255, 0.16);
      transform: scale(0.98);
    }}

    /* Physical particle explosions */
    .burst-particle {{
      position: fixed;
      pointer-events: none;
      z-index: 99999;
      font-size: 20px;
      will-change: transform, opacity;
    }}
  </style>
</head>
<body>

  <!-- Background Space Canvas -->
  <canvas id="spaceStarsCanvas"></canvas>
  <div class="ambient-glow glow-1"></div>
  <div class="ambient-glow glow-2"></div>

  <!-- Audio element -->
  <audio id="bgMusic" src="media/music.mp3" preload="auto" loop></audio>

  <!-- Top Navigation Bar -->
  <div class="top-nav-bar">
    <div class="progress-hearts" id="progressHearts">
      <span class="filled" id="h1">🤍</span>
      <span id="h2">🤍</span>
      <span id="h3">🤍</span>
      <span id="h4">🤍</span>
    </div>

    <button class="music-btn" id="audioToggleBtn" title="Музыка">
      <svg id="musicIcon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
        <path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/>
      </svg>
    </button>
  </div>

  <!-- ========================================================
       SCREEN 1: THE PLAYFUL HOOK (TRY 'NO' FIRST!)
       ======================================================== -->
  <div class="screen active" id="screen1">
    <div class="hook-card">
      <!-- Floating Cute Stickers -->
      <div class="floating-sticker st-1">✨</div>
      <div class="floating-sticker st-2">💖</div>
      <div class="floating-sticker st-3">🧸</div>
      <div class="floating-sticker st-4">🌸</div>

      <div class="avatar-box">
        <div class="avatar-halo"></div>
        <img src="media/5462926877434519487.jpg" class="avatar-img-squircle" alt="Злата">
      </div>

      <div class="hook-badge-pill">6 месяцев вместе 🤍</div>
      <h1 class="hook-headline">Злата</h1>
      <p class="hook-sub">Ты меня сильно любишь?</p>

      <!-- Forced Try NO Instruction -->
      <div class="hook-try-no-hint" id="tryNoBanner">
        <span>👉</span> <span>(попробуй нажать нет 😉)</span>
      </div>

      <div class="hook-buttons-area" id="hookArea">
        <!-- YES is initially locked until she tries NO! -->
        <button class="btn-action-yes locked" id="btnYes" disabled>
          <span id="btnYesText">Сначала нажми «НЕТ» 🤭</span>
        </button>

        <!-- Dodging NO button -->
        <button class="btn-action-no" id="btnNo">
          <span>НЕТ 💔</span>
          <div class="bubble-reaction" id="bubbleReaction">Ой! Куда это я? 🏃‍♂️</div>
        </button>
      </div>
    </div>
  </div>

  <!-- ========================================================
       SCREEN 2: THE QUIZ
       ======================================================== -->
  <div class="screen" id="screen2">
    <div class="quiz-layout">
      <div class="quiz-card-bubble">
        <div class="quiz-meta-row">
          <div class="quiz-tag">
            <span>💌</span> <span>Тест для любимой</span>
          </div>
          <div class="quiz-step-bubble" id="quizStepBadge">Вопрос 1 из 5</div>
        </div>

        <div class="quiz-q-title" id="quizQuestionText">Вопрос загружается...</div>

        <div class="quiz-options-grid" id="quizOptionsBox">
          <!-- Populated dynamically -->
        </div>

        <div class="quiz-reaction-toast" id="quizReactionToast"></div>
      </div>
    </div>
  </div>

  <!-- ========================================================
       SCREEN 3: CELAMUR PORTRAIT & 3D SPIRAL GALAXY
       ======================================================== -->
  <div class="screen" id="screen3" style="padding: 10px 16px 24px 16px; justify-content: space-between;">
    <div class="celamur-stage" id="celamurViewport">
      <canvas id="galaxyCanvas"></canvas>
    </div>

    <div class="celamur-meta">
      <!-- Circular play button -->
      <button class="celamur-play-circle" id="celamurPlayBtn" title="Слушать">
        <svg id="playBtnIcon" viewBox="0 0 24 24">
          <polygon points="6,4 19,12 6,20" />
        </svg>
      </button>

      <!-- Signature title & exact subtitles -->
      <div class="celamur-signature">Злата</div>
      <div class="celamur-sub-1">ты выглядишь божественно</div>
      <div class="celamur-sub-2">я тебя люблю на всех языках мира</div>
      <div class="celamur-swipe-hint" id="celamurHint">✦ проведи пальцем вбок, и она снова станет звёздами ✦</div>

      <!-- Action buttons -->
      <div class="celamur-buttons-stack">
        <button class="btn-pill-pink" id="btnToggleGalaxy">
          <span id="btnToggleText">Рассыпать в звёзды 🌌</span>
        </button>
        <button class="btn-pill-glass" id="btnGotoFinale">
          <span>Наше время →</span>
        </button>
      </div>
    </div>
  </div>

  <!-- ========================================================
       SCREEN 4: ANNIVERSARY TIMER & MEMORIES
       ======================================================== -->
  <div class="screen" id="screen4">
    <div class="finale-layout">
      <div class="finale-header-badge">20.05.2026 19:40 🤍</div>
      <h1 class="finale-headline">Полгода вместе</h1>

      <!-- Countdown -->
      <div class="timer-cards-row">
        <div class="timer-squircle">
          <div class="timer-num" id="tDays">00</div>
          <div class="timer-sub">Дней</div>
        </div>
        <div class="timer-squircle">
          <div class="timer-num" id="tHours">00</div>
          <div class="timer-sub">Часов</div>
        </div>
        <div class="timer-squircle">
          <div class="timer-num" id="tMins">00</div>
          <div class="timer-sub">Минут</div>
        </div>
        <div class="timer-squircle">
          <div class="timer-num" id="tSecs">00</div>
          <div class="timer-sub">Секунд</div>
        </div>
      </div>

      <!-- Verbatim quote requested by user -->
      <div class="polaroid-quote">
        «Вот мы уже пол года вместе, прошли много сложностей и неудач, но нас ждёт долгий и счастливый путь.»
      </div>

      <!-- Button to open memories -->
      <button class="btn-memories-open" id="btnOpenMemories">
        <span>Открыть наши воспоминания 📸</span>
      </button>
    </div>
  </div>

  <!-- ========================================================
       MEMORIES MODAL / STORY SLIDER (NO ELEVATOR PHOTO)
       ======================================================== -->
  <div class="story-modal" id="storyModal">
    <button class="story-close-btn" id="btnCloseMemories" title="Закрыть">×</button>

    <div class="story-frame">
      <div class="story-media-container" id="storyMediaBox">
        <img src="" class="story-img" id="storyImg" alt="Воспоминание">
        <video class="story-video" id="storyVideo" controls playsinline style="display:none;"></video>
      </div>

      <div class="story-bottom-info">
        <div class="story-date-tag" id="storyDateTag">Начало истории</div>
        <div class="story-caption-text" id="storyCaption">Загрузка...</div>
        <div class="story-counter-dots" id="storyCounter">1 / 18</div>
        <div class="story-nav-buttons">
          <button class="story-btn-nav" id="btnPrevSlide">← Назад</button>
          <button class="story-btn-nav" id="btnNextSlide">Вперёд →</button>
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================================
       JAVASCRIPT MOTION & GAMEPLAY ENGINE
       ======================================================== -->
  <script>
    // Embedded Data
    const CELAMUR_PORTRAIT_B64 = "{celamur_base64}";
    const GALAXY_PARTICLES = {particles_data};
    const MEMORY_FILES = {memory_files_json};

    // Screen navigation
    let currentScreen = 1;
    function goToScreen(num) {{
      document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
      const next = document.getElementById('screen' + num);
      if (next) {{
        next.classList.add('active');
        currentScreen = num;

        // Update progress hearts
        for (let i = 1; i <= 4; i++) {{
          const h = document.getElementById('h' + i);
          if (h) {{
            if (i <= num) h.classList.add('filled');
            else h.classList.remove('filled');
          }}
        }}

        if (num === 3) {{
          initCelamurCanvas();
        }}
      }}
    }}

    // Ambient space background starfield
    (function initSpaceStars() {{
      const canvas = document.getElementById('spaceStarsCanvas');
      const ctx = canvas.getContext('2d');
      let w, h;
      const stars = [];

      function resize() {{
        w = canvas.width = window.innerWidth;
        h = canvas.height = window.innerHeight;
      }}
      resize();
      window.addEventListener('resize', resize);

      for (let i = 0; i < 90; i++) {{
        stars.push({{
          x: Math.random() * w,
          y: Math.random() * h,
          r: Math.random() * 1.5 + 0.4,
          a: Math.random(),
          speed: Math.random() * 0.015 + 0.005
        }});
      }}

      function loop() {{
        ctx.clearRect(0, 0, w, h);
        for (let i = 0; i < stars.length; i++) {{
          const s = stars[i];
          s.a += s.speed;
          const alpha = (Math.sin(s.a) + 1) * 0.4 + 0.1;
          ctx.beginPath();
          ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
          ctx.fillStyle = `rgba(255, 230, 245, ${{alpha}})`;
          ctx.fill();
        }}
        requestAnimationFrame(loop);
      }}
      loop();
    }})();

    // Audio controls
    const bgMusic = document.getElementById('bgMusic');
    const audioToggleBtn = document.getElementById('audioToggleBtn');
    let isPlayingAudio = false;

    function toggleMusic() {{
      if (isPlayingAudio) {{
        bgMusic.pause();
        isPlayingAudio = false;
        audioToggleBtn.classList.remove('playing');
        updatePlayIcon(false);
      }} else {{
        bgMusic.play().then(() => {{
          isPlayingAudio = true;
          audioToggleBtn.classList.add('playing');
          updatePlayIcon(true);
        }}).catch(() => {{}});
      }}
    }}

    function updatePlayIcon(playing) {{
      const icon = document.getElementById('playBtnIcon');
      if (icon) {{
        if (playing) {{
          icon.innerHTML = '<rect x="6" y="5" width="4" height="14"/><rect x="14" y="5" width="4" height="14"/>';
        }} else {{
          icon.innerHTML = '<polygon points="6,4 19,12 6,20" />';
        }}
      }}
    }}

    audioToggleBtn.addEventListener('click', toggleMusic);
    document.getElementById('celamurPlayBtn').addEventListener('click', toggleMusic);

    // ========================================================
    // SCREEN 1: THE PLAYFUL DODGING 'NO' MECHANIC
    // ========================================================
    const btnNo = document.getElementById('btnNo');
    const btnYes = document.getElementById('btnYes');
    const btnYesText = document.getElementById('btnYesText');
    const tryNoBanner = document.getElementById('tryNoBanner');
    const bubbleReaction = document.getElementById('bubbleReaction');
    const hookArea = document.getElementById('hookArea');

    let noEscapeCount = 0;
    let yesUnlocked = false;

    const noQuotes = [
      "Ой! Куда это я? 🏃‍♂️💨",
      "Ты правда думала нажать? 😂",
      "Хи-хи, не поймаешь! 😜",
      "Эта кнопка тут для красоты! ✨",
      "Всё, я устала бегать! Жми ДА! ❤️"
    ];

    function handleNoDodge(e) {{
      noEscapeCount++;
      
      // Show cute reaction bubble
      bubbleReaction.textContent = noQuotes[Math.min(noEscapeCount - 1, noQuotes.length - 1)];
      bubbleReaction.classList.add('show');
      setTimeout(() => bubbleReaction.classList.remove('show'), 1600);

      // Physics leap
      const areaRect = hookArea.getBoundingClientRect();
      const maxX = areaRect.width / 2 - 60;
      const maxY = 45;
      
      const rx = (Math.random() - 0.5) * maxX * 2;
      const ry = (Math.random() - 0.5) * maxY * 2;
      btnNo.style.transform = `translate(${{rx}}px, ${{ry}}px) scale(${{Math.max(0.75, 1 - noEscapeCount * 0.05)}})`;

      // Spawn burst of mischievous sparkles
      spawnBurstParticles(e.clientX || areaRect.left + areaRect.width/2, e.clientY || areaRect.top + 70, 3, ['💨', '✨', '😜']);

      // UNLOCK YES BUTTON AFTER AT LEAST 2 TRIES!
      if (noEscapeCount >= 2 && !yesUnlocked) {{
        unlockYesButton();
      }}
    }}

    function unlockYesButton() {{
      yesUnlocked = true;
      btnYes.disabled = false;
      btnYes.classList.remove('locked');
      btnYes.classList.add('unlocked-pulse');
      btnYesText.textContent = "ДА, ОЧЕНЬ! ❤️";
      
      tryNoBanner.style.background = "rgba(46, 213, 115, 0.15)";
      tryNoBanner.style.borderColor = "#2ed573";
      tryNoBanner.style.color = "#2ed573";
      tryNoBanner.innerHTML = "<span>✨</span> <span>Умничка! Теперь нажимай ДА! 🥰</span>";

      spawnBurstParticles(window.innerWidth / 2, btnYes.getBoundingClientRect().top + 25, 12, ['💖', '✨', '🤍']);
    }}

    btnNo.addEventListener('mouseenter', handleNoDodge);
    btnNo.addEventListener('touchstart', (e) => {{
      e.preventDefault();
      handleNoDodge(e.touches[0]);
    }});
    btnNo.addEventListener('click', handleNoDodge);

    // Clicking YES when unlocked
    btnYes.addEventListener('click', (e) => {{
      if (!yesUnlocked) {{
        // Shake hint
        tryNoBanner.style.animation = 'none';
        void tryNoBanner.offsetWidth;
        tryNoBanner.style.animation = 'shakeCard 0.4s ease';
        return;
      }}

      // Start music on first active engagement
      if (!isPlayingAudio) toggleMusic();

      // Confetti burst
      spawnBurstParticles(e.clientX || window.innerWidth/2, e.clientY || window.innerHeight/2, 25, ['💖', '🤍', '🌸', '✨', '🥰']);

      setTimeout(() => {{
        goToScreen(2);
      }}, 550);
    }});

    // Physics Particle Burst Generator
    function spawnBurstParticles(x, y, count, symbols) {{
      for (let i = 0; i < count; i++) {{
        const el = document.createElement('div');
        el.className = 'burst-particle';
        el.textContent = symbols[Math.floor(Math.random() * symbols.length)];
        el.style.left = x + 'px';
        el.style.top = y + 'px';
        document.body.appendChild(el);

        const angle = Math.random() * Math.PI * 2;
        const speed = Math.random() * 8 + 3;
        let vx = Math.cos(angle) * speed;
        let vy = Math.sin(angle) * speed - 3;
        let curX = 0, curY = 0;
        let opacity = 1.0;

        function step() {{
          curX += vx;
          curY += vy;
          vy += 0.25; // gravity
          opacity -= 0.025;
          el.style.transform = `translate(${{curX}}px, ${{curY}}px) scale(${{opacity * 1.2}})`;
          el.style.opacity = opacity;

          if (opacity > 0) {{
            requestAnimationFrame(step);
          }} else {{
            el.remove();
          }}
        }}
        requestAnimationFrame(step);
      }}
    }}

    // ========================================================
    // SCREEN 2: THE PERSONALIZED QUIZ
    // ========================================================
    const quizQuestions = [
      {{
        q: "Что мне больше всего нравится?",
        opts: [
          "Спать до обеда 😴",
          "Реализация импульсивных идей ⚡",
          "Сидеть дома в тишине 🤫",
          "Спорить обо всём подряд 🗣️"
        ],
        ans: 1
      }},
      {{
        q: "Моя суперспособность в любой ситуации?",
        opts: [
          "Впадать в панику 🌪️",
          "Решать ненужные проблемы 🧠",
          "Опаздывать на полчаса ⏰",
          "Делать вид, что всё знаю 🕶️"
        ],
        ans: 1
      }},
      {{
        q: "Какое наше идеальное свидание?",
        opts: [
          "Дорогой пафосный ресторан 🥂",
          "Гулять сколько захотим 🌃",
          "Молча смотреть кино 🎬",
          "Сидеть в телефонах рядом 📱"
        ],
        ans: 1
      }},
      {{
        q: "Что я дольше всего делаю перед выходом?",
        opts: [
          "Ищу ключи и телефон 🔑",
          "Одеваюсь 👕",
          "Причёсываюсь перед зеркалом 🪞",
          "Зависаю в мыслях 💭"
        ],
        ans: 1
      }},
      {{
        q: "Какая моя самая любимая еда на свете?",
        opts: [
          "Пицца из доставки 🍕",
          "Бургеры и картошка 🍔",
          "Твоя 🤍",
          "Стейк из ресторана 🥩"
        ],
        ans: 2
      }}
    ];

    let currentQ = 0;
    function renderQuiz() {{
      const q = quizQuestions[currentQ];
      document.getElementById('quizStepBadge').textContent = `Вопрос ${{currentQ + 1}} из ${{quizQuestions.length}}`;
      document.getElementById('quizQuestionText').textContent = q.q;
      document.getElementById('quizReactionToast').textContent = "";

      const box = document.getElementById('quizOptionsBox');
      box.innerHTML = '';
      q.opts.forEach((optText, idx) => {{
        const btn = document.createElement('button');
        btn.className = 'quiz-option-pill';
        btn.innerHTML = `<span>${{optText}}</span>`;
        btn.addEventListener('click', () => handleAnswer(idx, btn));
        box.appendChild(btn);
      }});
    }}

    function handleAnswer(idx, btn) {{
      const q = quizQuestions[currentQ];
      if (idx === q.ans) {{
        btn.classList.add('correct');
        const rect = btn.getBoundingClientRect();
        spawnBurstParticles(rect.left + rect.width/2, rect.top + rect.height/2, 10, ['✨', '💖', '🥰']);
        document.getElementById('quizReactionToast').textContent = "В точку! Ты знаешь меня идеально 🥰";

        setTimeout(() => {{
          currentQ++;
          if (currentQ < quizQuestions.length) {{
            renderQuiz();
          }} else {{
            document.getElementById('quizReactionToast').textContent = "100% совпадение! А теперь смотри... 💫";
            setTimeout(() => goToScreen(3), 900);
          }}
        }}, 650);
      }} else {{
        btn.classList.add('wrong');
        document.getElementById('quizReactionToast').textContent = "Не-а, мимо! Подумай ещё разок 😉";
        setTimeout(() => btn.classList.remove('wrong'), 600);
      }}
    }}
    renderQuiz();

    // ========================================================
    // SCREEN 3: CELAMUR PORTRAIT & 3D SPIRAL GALAXY
    // ========================================================
    let canvas, ctx;
    let portraitImg = new Image();
    portraitImg.src = CELAMUR_PORTRAIT_B64;

    let isGalaxyMode = false;
    let morphProgress = 1.0; // 1 = portrait, 0 = galaxy
    let targetMorph = 1.0;

    let rotY = 0.8;
    let rotX = 66 * Math.PI / 180;
    let velRotY = 0.003;
    let velRotX = 0;
    let isDragging = false;
    let startX = 0, startY = 0;
    let lastX = 0, lastY = 0;

    let canvasWidth = 400;
    let canvasHeight = 460;
    let canvasReady = false;

    function initCelamurCanvas() {{
      if (canvasReady) return;
      canvasReady = true;

      canvas = document.getElementById('galaxyCanvas');
      ctx = canvas.getContext('2d');

      function resize() {{
        const rect = canvas.getBoundingClientRect();
        canvasWidth = rect.width || 380;
        canvasHeight = rect.height || 450;
        const dpr = Math.min(window.devicePixelRatio || 1, 2);
        canvas.width = canvasWidth * dpr;
        canvas.height = canvasHeight * dpr;
        ctx.scale(dpr, dpr);
      }}
      resize();
      window.addEventListener('resize', resize);

      // Mouse drag controls
      canvas.addEventListener('mousedown', (e) => {{
        isDragging = true;
        startX = lastX = e.clientX;
        startY = lastY = e.clientY;
      }});
      window.addEventListener('mousemove', (e) => {{
        if (!isDragging) return;
        const dx = e.clientX - lastX;
        const dy = e.clientY - lastY;
        lastX = e.clientX;
        lastY = e.clientY;
        velRotY = dx * 0.008;
        velRotX = dy * 0.008;
        rotY += velRotY;
        rotX = Math.max(0.35, Math.min(1.45, rotX + velRotX));
      }});
      window.addEventListener('mouseup', (e) => {{
        if (isDragging) {{
          if (Math.abs(e.clientX - startX) > 40) toggleGalaxyMode();
        }}
        isDragging = false;
      }});

      // Touch drag controls
      canvas.addEventListener('touchstart', (e) => {{
        isDragging = true;
        startX = lastX = e.touches[0].clientX;
        startY = lastY = e.touches[0].clientY;
      }}, {{ passive: true }});
      canvas.addEventListener('touchmove', (e) => {{
        if (!isDragging) return;
        const dx = e.touches[0].clientX - lastX;
        const dy = e.touches[0].clientY - lastY;
        lastX = e.touches[0].clientX;
        lastY = e.touches[0].clientY;
        velRotY = dx * 0.008;
        velRotX = dy * 0.008;
        rotY += velRotY;
        rotX = Math.max(0.35, Math.min(1.45, rotX + velRotX));
      }}, {{ passive: true }});
      canvas.addEventListener('touchend', (e) => {{
        if (isDragging) {{
          if (Math.abs(lastX - startX) > 40) toggleGalaxyMode();
        }}
        isDragging = false;
      }});

      requestAnimationFrame(renderCelamurLoop);
    }}

    function toggleGalaxyMode() {{
      isGalaxyMode = !isGalaxyMode;
      targetMorph = isGalaxyMode ? 0.0 : 1.0;

      const btnText = document.getElementById('btnToggleText');
      const hint = document.getElementById('celamurHint');
      if (isGalaxyMode) {{
        btnText.textContent = "Собрать портрет ✨";
        hint.textContent = "✦ покрути нашу галактику любви ✦";
        spawnBurstParticles(window.innerWidth/2, window.innerHeight/2, 15, ['🌌', '✨', '💫']);
      }} else {{
        btnText.textContent = "Рассыпать в звёзды 🌌";
        hint.textContent = "✦ проведи пальцем вбок, и она снова станет звёздами ✦";
        spawnBurstParticles(window.innerWidth/2, window.innerHeight/2, 15, ['🤍', '✨', '💖']);
      }}
    }}

    document.getElementById('btnToggleGalaxy').addEventListener('click', toggleGalaxyMode);
    document.getElementById('btnGotoFinale').addEventListener('click', () => goToScreen(4));

    function renderCelamurLoop() {{
      if (currentScreen === 3) {{
        morphProgress += (targetMorph - morphProgress) * 0.08;

        if (!isDragging) {{
          velRotY *= 0.96;
          rotY += 0.004 + velRotY;
          velRotX *= 0.92;
          rotX = Math.max(0.35, Math.min(1.45, rotX + velRotX));
        }}

        drawCelamur();
      }}
      requestAnimationFrame(renderCelamurLoop);
    }}

    function drawCelamur() {{
      const W = canvasWidth;
      const H = canvasHeight;
      const cx = W / 2;
      const cy = H / 2 - 15;

      ctx.clearRect(0, 0, W, H);

      // 1. Glowing Center Nebula
      const galA = 1.0 - morphProgress;
      if (galA > 0.02) {{
        ctx.save();
        ctx.globalAlpha = galA;
        const grad = ctx.createRadialGradient(cx, cy, 0, cx, cy, 145);
        grad.addColorStop(0, 'rgba(255, 235, 245, 0.85)');
        grad.addColorStop(0.2, 'rgba(255, 110, 160, 0.45)');
        grad.addColorStop(0.5, 'rgba(160, 40, 100, 0.15)');
        grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
        ctx.fillStyle = grad;
        ctx.beginPath();
        ctx.ellipse(cx, cy, 155, 58, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      }}

      // 2. Base Duotone Photo
      if (morphProgress > 0.02 && portraitImg.complete && portraitImg.naturalWidth > 0) {{
        ctx.save();
        ctx.globalAlpha = Math.pow(morphProgress, 1.8) * 0.95;
        const pw = 300;
        const ph = 390;
        ctx.drawImage(portraitImg, cx - pw/2, cy - ph/2, pw, ph);
        ctx.restore();
      }}

      // 3. Scanline & 3D Spiral Typography Particles
      const D = 420;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';

      const cosY = Math.cos(rotY);
      const sinY = Math.sin(rotY);
      const cosX = Math.cos(rotX);
      const sinX = Math.sin(rotX);

      const len = GALAXY_PARTICLES.length;
      for (let i = 0; i < len; i++) {{
        const p = GALAXY_PARTICLES[i];

        const gx = p.gx;
        const gy = p.gy;
        const gz = p.gz;

        const x1 = gx * cosY + gz * sinY;
        const z1 = -gx * sinY + gz * cosY;
        const y1 = gy;

        const y2 = y1 * cosX - z1 * sinX;
        const z2 = y1 * sinX + z1 * cosX;
        const x2 = x1;

        const fov = D / (D + z2);
        const galX = cx + x2 * fov;
        const galY = cy + y2 * fov;

        const portX = cx + p.px * 0.95;
        const portY = cy + p.py * 0.95;

        const curX = galX + (portX - galX) * morphProgress;
        const curY = galY + (portY - galY) * morphProgress;

        let fontSize, alpha, col;
        if (morphProgress > 0.5) {{
          fontSize = 7;
          alpha = 0.55 + 0.35 * morphProgress;
          col = `rgba(255, 225, 235, ${{alpha}})`;
        }} else {{
          const depthScale = Math.max(0.4, Math.min(1.3, fov));
          fontSize = Math.round(7 * depthScale * p.s);
          const distCore = Math.sqrt(gx*gx + gz*gz);
          const coreFactor = Math.max(0.3, 1.0 - (distCore / 320.0) * 0.5);
          alpha = Math.min(1.0, coreFactor * depthScale * (1.0 - morphProgress));
          col = `rgba(255, 230, 240, ${{alpha}})`;
        }}

        if (alpha > 0.1) {{
          ctx.font = `${{fontSize}}px var(--font-sans)`;
          ctx.fillStyle = col;
          ctx.fillText(p.t, curX, curY);
        }}
      }}
    }}

    // ========================================================
    // SCREEN 4: COUNTDOWN TIMER (FROM 20.05.2026, 19:40)
    // ========================================================
    const anniversaryDate = new Date(2026, 4, 20, 19, 40, 0);

    function updateTimer() {{
      const now = new Date();
      let diff = now - anniversaryDate;
      if (diff < 0) diff = 0;

      const days = Math.floor(diff / (1000 * 60 * 60 * 24));
      const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
      const mins = Math.floor((diff / (1000 * 60)) % 60);
      const secs = Math.floor((diff / 1000) % 60);

      document.getElementById('tDays').textContent = String(days).padStart(2, '0');
      document.getElementById('tHours').textContent = String(hours).padStart(2, '0');
      document.getElementById('tMins').textContent = String(mins).padStart(2, '0');
      document.getElementById('tSecs').textContent = String(secs).padStart(2, '0');
    }}
    setInterval(updateTimer, 1000);
    updateTimer();

    // ========================================================
    // MEMORIES STORY MODAL (NO ELEVATOR PHOTO)
    // ========================================================
    let currentSlide = 0;
    const storyModal = document.getElementById('storyModal');
    const storyImg = document.getElementById('storyImg');
    const storyVideo = document.getElementById('storyVideo');
    const storyCaption = document.getElementById('storyCaption');
    const storyDateTag = document.getElementById('storyDateTag');
    const storyCounter = document.getElementById('storyCounter');

    function openMemories() {{
      storyModal.classList.add('open');
      showSlide(0);
    }}

    function closeMemories() {{
      storyModal.classList.remove('open');
      storyVideo.pause();
    }}

    function showSlide(idx) {{
      if (idx < 0) idx = MEMORY_FILES.length - 1;
      if (idx >= MEMORY_FILES.length) idx = 0;
      currentSlide = idx;

      const item = MEMORY_FILES[idx];
      storyDateTag.textContent = item.date || "Наше мгновение";
      storyCaption.textContent = item.caption;
      storyCounter.textContent = `${{idx + 1}} / ${{MEMORY_FILES.length}}`;

      const isVideo = item.name.toLowerCase().endsWith('.mp4');
      const mediaPath = 'media/' + item.name;

      if (isVideo) {{
        storyImg.style.display = 'none';
        storyVideo.style.display = 'block';
        storyVideo.src = mediaPath;
        storyVideo.play().catch(() => {{}});
      }} else {{
        storyVideo.pause();
        storyVideo.style.display = 'none';
        storyImg.style.display = 'block';
        storyImg.src = mediaPath;
      }}
    }}

    document.getElementById('btnOpenMemories').addEventListener('click', openMemories);
    document.getElementById('btnCloseMemories').addEventListener('click', closeMemories);
    document.getElementById('btnPrevSlide').addEventListener('click', () => showSlide(currentSlide - 1));
    document.getElementById('btnNextSlide').addEventListener('click', () => showSlide(currentSlide + 1));

    window.addEventListener('keydown', (e) => {{
      if (!storyModal.classList.contains('open')) return;
      if (e.key === 'ArrowLeft') showSlide(currentSlide - 1);
      if (e.key === 'ArrowRight') showSlide(currentSlide + 1);
      if (e.key === 'Escape') closeMemories();
    }});

    let touchStartX = 0;
    storyModal.addEventListener('touchstart', (e) => {{
      touchStartX = e.touches[0].clientX;
    }}, {{ passive: true }});
    storyModal.addEventListener('touchend', (e) => {{
      const touchEndX = e.changedTouches[0].clientX;
      if (touchEndX - touchStartX > 50) showSlide(currentSlide - 1);
      if (touchStartX - touchEndX > 50) showSlide(currentSlide + 1);
    }});
  </script>
</body>
</html>
'''

with open('d:/подарки пол года/index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print('SUCCESS! d:/подарки пол года/index.html generated successfully with cute motion overhaul!')
print(f'File size: {os.path.getsize("d:/подарки пол года/index.html")} bytes')
