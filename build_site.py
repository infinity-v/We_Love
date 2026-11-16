# -*- coding: utf-8 -*-
"""
Generator script for Zlata's 6-Month Anniversary Website (index.html)
Replicating the authentic Celamur typography portrait & 3D spiral galaxy.
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
    {"name": "с чего все началось.jpg", "caption": "С чего всё началось 🤍"},
    {"name": "первые цветы.jpg", "caption": "Твои первые цветы 💐"},
    {"name": "свидание на природе.jpg", "caption": "Наше свидание на природе 🌿"},
    {"name": "свидание на природе 2 фото.jpg", "caption": "Тёплые моменты на свежем воздухе 🍃"},
    {"name": "IMG_20261115_230355_318.jpg", "caption": "Солнечный день на крыше ☀️"},
    {"name": "IMG_20261115_230620_235.jpg", "caption": "Твоя красота и нежность ✨"},
    {"name": "IMG_20261115_232741_361.jpg", "caption": "Уютный кофе вдвоём ☕"},
    {"name": "IMG_20261115_233109_723.jpg", "caption": "Счастливы вместе 🤍"},
    {"name": "IMG_20261116_000248_096.jpg", "caption": "Навсегда в моём сердце 💌"},
    {"name": "5462926877434519487.jpg", "caption": "Твоя любимая улыбка 🥰"},
    {"name": "5462926877434519488.jpg", "caption": "Счастье в простых моментах 🍓"},
    {"name": "5462926877434519489.jpg", "caption": "Всегда рядом с тобой 🤍"},
    {"name": "5462926877434519490.jpg", "caption": "Самая прекрасная ✨"},
    {"name": "5462926877434519491.jpg", "caption": "Любимый взгляд 💫"},
    {"name": "мы самые яркие звезды.mp4", "caption": "Мы — самые яркие звёзды ✨"},
    {"name": "video5462926876974558922.mp4", "caption": "Наши живые мгновения 🎬"},
    {"name": "video5462926876974558921.mp4", "caption": "Тёплые воспоминания 🎞️"},
    {"name": "HnVideoEditor_2026_11_16_002803168.mp4", "caption": "История нашей любви 💖"}
]

memory_files_json = json.dumps(memory_files, ensure_ascii=False)

html_template = f'''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>Злата — Наша Вселенная 🤍</title>
  
  <!-- Fonts: Great Vibes for signature cursive, Inter for sleek UI -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Great+Vibes&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <style>
    :root {{
      --bg: #000000;
      --card-bg: rgba(22, 18, 25, 0.75);
      --card-border: rgba(255, 255, 255, 0.08);
      --accent-pink: #ff6b8b;
      --accent-gradient: linear-gradient(135deg, #ff7597 0%, #ff4b72 100%);
      --accent-glow: rgba(255, 107, 139, 0.4);
      --text-main: #ffffff;
      --text-muted: #a69eac;
      --font-cursive: 'Great Vibes', 'Caveat', cursive;
      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
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

    /* Global ambient background */
    #ambientBg {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 0;
      background: radial-gradient(circle at 50% 25%, rgba(45, 15, 30, 0.4) 0%, rgba(5, 2, 8, 0.8) 50%, #000000 100%);
    }}

    /* Screens wrapper */
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
      transform: scale(0.96) translateY(12px);
      transition: opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1), transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
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

    /* Top step dots */
    .top-dots {{
      position: absolute;
      top: 18px;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      gap: 6px;
      z-index: 10;
    }}
    .top-dots span {{
      width: 18px;
      height: 3px;
      border-radius: 2px;
      background: rgba(255, 255, 255, 0.15);
      transition: all 0.4s ease;
    }}
    .top-dots span.active {{
      width: 32px;
      background: var(--accent-pink);
      box-shadow: 0 0 10px var(--accent-glow);
    }}

    /* Audio button fixed */
    .audio-btn {{
      position: fixed;
      top: 18px;
      right: 20px;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.12);
      backdrop-filter: blur(10px);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      cursor: pointer;
      z-index: 100;
      transition: all 0.3s ease;
    }}
    .audio-btn:hover {{
      transform: scale(1.08);
      background: rgba(255, 255, 255, 0.15);
    }}

    /* ========================================================
       SCREEN 1: THE PLAYFUL HOOK
       ======================================================== */
    .hook-container {{
      max-width: 380px;
      width: 100%;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;
    }}

    .avatar-wrapper {{
      position: relative;
      width: 130px;
      height: 130px;
      margin-bottom: 8px;
    }}
    .avatar-glow {{
      position: absolute;
      inset: -6px;
      border-radius: 50%;
      background: var(--accent-gradient);
      opacity: 0.6;
      filter: blur(12px);
      animation: pulseGlow 3s infinite alternate;
    }}
    @keyframes pulseGlow {{
      0% {{ transform: scale(0.95); opacity: 0.4; }}
      100% {{ transform: scale(1.08); opacity: 0.8; }}
    }}
    .avatar-img {{
      position: relative;
      width: 100%;
      height: 100%;
      border-radius: 50%;
      object-fit: cover;
      border: 2px solid rgba(255, 255, 255, 0.3);
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.6);
    }}

    .hook-badge {{
      display: inline-block;
      padding: 6px 14px;
      border-radius: 9999px;
      background: rgba(255, 107, 139, 0.12);
      border: 1px solid rgba(255, 107, 139, 0.3);
      color: #ff9bb2;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 1.5px;
      text-transform: uppercase;
    }}

    .hook-title {{
      font-family: var(--font-cursive);
      font-size: 46px;
      line-height: 1;
      color: #fff;
      text-shadow: 0 0 20px rgba(255, 180, 200, 0.5);
    }}

    .hook-subtitle {{
      font-size: 18px;
      color: #dfd7e3;
      font-weight: 400;
      line-height: 1.4;
      margin-top: -6px;
    }}

    .hook-buttons {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      width: 100%;
      margin-top: 10px;
      position: relative;
      min-height: 120px;
    }}

    .btn-yes {{
      background: var(--accent-gradient);
      color: #ffffff;
      border: none;
      padding: 16px 28px;
      border-radius: 9999px;
      font-size: 16px;
      font-weight: 600;
      cursor: pointer;
      box-shadow: 0 10px 30px var(--accent-glow);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }}
    .btn-yes:active {{
      transform: scale(0.97);
    }}

    .btn-no {{
      background: rgba(255, 255, 255, 0.06);
      color: var(--text-muted);
      border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 14px 28px;
      border-radius: 9999px;
      font-size: 15px;
      cursor: pointer;
      transition: all 0.2s ease;
      position: relative;
    }}

    .no-comment {{
      font-size: 13px;
      color: #ff8fab;
      min-height: 18px;
      transition: opacity 0.3s;
    }}

    /* ========================================================
       SCREEN 2: THE PERSONALIZED QUIZ
       ======================================================== */
    .quiz-container {{
      max-width: 420px;
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}

    .quiz-card {{
      width: 100%;
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-radius: 28px;
      padding: 28px 22px;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7);
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}

    .quiz-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .quiz-step-title {{
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 1.2px;
      color: #ff9bb2;
      font-weight: 600;
    }}
    .quiz-step-counter {{
      font-size: 12px;
      color: var(--text-muted);
    }}

    .quiz-progress {{
      width: 100%;
      height: 4px;
      background: rgba(255, 255, 255, 0.08);
      border-radius: 2px;
      overflow: hidden;
    }}
    .quiz-progress-bar {{
      height: 100%;
      width: 20%;
      background: var(--accent-gradient);
      border-radius: 2px;
      transition: width 0.4s ease;
    }}

    .quiz-question {{
      font-size: 18px;
      font-weight: 600;
      color: #ffffff;
      line-height: 1.4;
      text-align: left;
    }}

    .quiz-options {{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .quiz-opt {{
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 14px 18px;
      border-radius: 16px;
      color: #ded6e3;
      font-size: 14px;
      font-weight: 400;
      text-align: left;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      transition: all 0.25s ease;
    }}
    .quiz-opt:hover {{
      background: rgba(255, 255, 255, 0.08);
      border-color: rgba(255, 255, 255, 0.18);
    }}
    .quiz-opt.correct {{
      background: rgba(46, 213, 115, 0.15);
      border-color: #2ed573;
      color: #ffffff;
      transform: scale(1.02);
      box-shadow: 0 0 15px rgba(46, 213, 115, 0.3);
    }}
    .quiz-opt.wrong {{
      background: rgba(255, 71, 87, 0.15);
      border-color: #ff4757;
      color: #ff6b81;
      animation: shake 0.4s;
    }}
    @keyframes shake {{
      0%, 100% {{ transform: translateX(0); }}
      20%, 60% {{ transform: translateX(-6px); }}
      40%, 80% {{ transform: translateX(6px); }}
    }}

    .quiz-hint {{
      font-size: 13px;
      color: #ff8fab;
      text-align: center;
      min-height: 18px;
    }}

    /* ========================================================
       SCREEN 3: THE CELAMUR PORTRAIT & 3D SPIRAL GALAXY
       ======================================================== */
    .celamur-screen {{
      padding: 10px 16px 24px 16px;
      justify-content: space-between;
    }}

    .celamur-viewport {{
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
    .celamur-controls {{
      width: 100%;
      max-width: 380px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 12px;
      z-index: 5;
    }}

    .play-circle-btn {{
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.18);
      backdrop-filter: blur(10px);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      cursor: pointer;
      transition: all 0.3s ease;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
    }}
    .play-circle-btn:active {{
      transform: scale(0.92);
    }}
    .play-circle-btn svg {{
      width: 20px;
      height: 20px;
      fill: currentColor;
    }}

    .celamur-title {{
      font-family: var(--font-cursive);
      font-size: 44px;
      line-height: 1;
      color: #ffffff;
      text-shadow: 0 0 20px rgba(255, 180, 210, 0.6);
      margin-top: -2px;
    }}

    .celamur-subtitle-1 {{
      font-size: 15px;
      font-weight: 400;
      color: #e9dfe8;
      letter-spacing: 0.3px;
    }}

    .celamur-subtitle-2 {{
      font-size: 13px;
      font-weight: 400;
      color: #ff8fab;
      margin-top: -6px;
    }}

    .celamur-hint {{
      font-size: 11px;
      color: rgba(255, 255, 255, 0.45);
      letter-spacing: 0.5px;
      margin-top: -4px;
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    .celamur-actions {{
      display: flex;
      flex-direction: column;
      gap: 10px;
      width: 100%;
      margin-top: 4px;
    }}

    .btn-celamur-primary {{
      background: var(--accent-gradient);
      color: #ffffff;
      border: none;
      padding: 14px 28px;
      border-radius: 9999px;
      font-size: 15px;
      font-weight: 600;
      cursor: pointer;
      box-shadow: 0 8px 25px var(--accent-glow);
      transition: all 0.3s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }}
    .btn-celamur-primary:active {{
      transform: scale(0.97);
    }}

    .btn-celamur-secondary {{
      background: rgba(255, 255, 255, 0.08);
      color: #eae3ec;
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 13px 28px;
      border-radius: 9999px;
      font-size: 14px;
      font-weight: 500;
      cursor: pointer;
      backdrop-filter: blur(10px);
      transition: all 0.3s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }}
    .btn-celamur-secondary:hover {{
      background: rgba(255, 255, 255, 0.14);
    }}

    /* ========================================================
       SCREEN 4: ANNIVERSARY TIMER & MEMORIES
       ======================================================== */
    .finale-container {{
      max-width: 440px;
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 22px;
      text-align: center;
    }}

    .finale-badge {{
      display: inline-block;
      padding: 6px 16px;
      border-radius: 9999px;
      background: rgba(255, 107, 139, 0.12);
      border: 1px solid rgba(255, 107, 139, 0.3);
      color: #ff9bb2;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 1.5px;
      text-transform: uppercase;
    }}

    .finale-title {{
      font-family: var(--font-cursive);
      font-size: 46px;
      line-height: 1;
      color: #ffffff;
      text-shadow: 0 0 20px rgba(255, 180, 200, 0.5);
    }}

    /* Live countdown cards */
    .timer-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
      width: 100%;
    }}

    .timer-card {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 18px;
      padding: 14px 6px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
      backdrop-filter: blur(10px);
    }}
    .timer-val {{
      font-size: 26px;
      font-weight: 700;
      color: #ffffff;
      font-variant-numeric: tabular-nums;
      line-height: 1;
    }}
    .timer-lbl {{
      font-size: 10px;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.8px;
    }}

    /* Verbatim quote requested by user */
    .verbatim-quote-card {{
      background: rgba(255, 255, 255, 0.03);
      border-left: 3px solid var(--accent-pink);
      border-radius: 4px 16px 16px 4px;
      padding: 18px 20px;
      font-size: 14px;
      line-height: 1.6;
      color: #eae1ec;
      font-style: italic;
      text-align: left;
      position: relative;
    }}
    .verbatim-quote-card::before {{
      content: '“';
      position: absolute;
      top: -12px;
      left: 12px;
      font-size: 44px;
      color: rgba(255, 107, 139, 0.25);
      font-family: serif;
    }}

    .btn-memories {{
      background: var(--accent-gradient);
      color: #ffffff;
      border: none;
      padding: 16px 32px;
      border-radius: 9999px;
      font-size: 15px;
      font-weight: 600;
      cursor: pointer;
      box-shadow: 0 10px 30px var(--accent-glow);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      width: 100%;
      transition: all 0.3s ease;
    }}
    .btn-memories:active {{
      transform: scale(0.97);
    }}

    /* ========================================================
       MEMORIES MODAL / SLIDER
       ======================================================== */
    .memories-modal {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.94);
      backdrop-filter: blur(25px);
      -webkit-backdrop-filter: blur(25px);
      z-index: 1000;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 20px;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.4s ease;
    }}
    .memories-modal.open {{
      opacity: 1;
      pointer-events: auto;
    }}

    .modal-close-btn {{
      position: absolute;
      top: 24px;
      right: 24px;
      width: 44px;
      height: 44px;
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
    .modal-close-btn:hover {{
      background: rgba(255, 255, 255, 0.2);
    }}

    .slider-card {{
      max-width: 440px;
      width: 100%;
      background: rgba(20, 16, 24, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 28px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8);
    }}

    .slider-media-box {{
      width: 100%;
      height: 380px;
      background: #08060a;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }}

    .slider-img {{
      width: 100%;
      height: 100%;
      object-fit: contain;
      transition: opacity 0.3s ease;
    }}

    .slider-video {{
      width: 100%;
      height: 100%;
      object-fit: contain;
    }}

    .slider-info {{
      padding: 18px 20px 22px 20px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      text-align: center;
    }}

    .slider-caption {{
      font-size: 16px;
      font-weight: 500;
      color: #ffffff;
    }}

    .slider-counter {{
      font-size: 12px;
      color: var(--text-muted);
      letter-spacing: 1px;
    }}

    .slider-nav {{
      display: flex;
      gap: 10px;
      width: 100%;
    }}

    .slider-nav-btn {{
      flex: 1;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 12px;
      border-radius: 9999px;
      color: #ffffff;
      font-size: 13px;
      font-weight: 500;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.2s ease;
    }}
    .slider-nav-btn:hover {{
      background: rgba(255, 255, 255, 0.15);
    }}

    /* Floating hearts on click */
    .heart-particle {{
      position: fixed;
      pointer-events: none;
      z-index: 9999;
      font-size: 20px;
      animation: floatHeart 1.2s forwards ease-out;
    }}
    @keyframes floatHeart {{
      0% {{ transform: translate(0, 0) scale(0.8); opacity: 1; }}
      100% {{ transform: translate(var(--tx), var(--ty)) scale(1.4); opacity: 0; }}
    }}
  </style>
</head>
<body>

  <!-- Ambient background -->
  <div id="ambientBg"></div>

  <!-- Audio element -->
  <audio id="bgMusic" src="media/music.mp3" preload="auto" loop></audio>

  <!-- Top audio button -->
  <button class="audio-btn" id="audioToggleBtn" title="Музыка">
    <svg id="audioIcon" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
      <path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/>
    </svg>
  </button>

  <!-- ========================================================
       SCREEN 1: THE PLAYFUL HOOK
       ======================================================== -->
  <div class="screen active" id="screen1">
    <div class="top-dots">
      <span class="active"></span>
      <span></span>
      <span></span>
      <span></span>
    </div>

    <div class="hook-container">
      <div class="avatar-wrapper">
        <div class="avatar-glow"></div>
        <img src="media/5462926877434519487.jpg" class="avatar-img" alt="Злата">
      </div>

      <div class="hook-badge">6 месяцев вместе 🤍</div>
      <h1 class="hook-title">Злата</h1>
      <p class="hook-subtitle">Ты меня сильно любишь?</p>

      <div class="hook-buttons" id="hookButtonsBox">
        <button class="btn-yes" id="btnYes">
          <span>ДА, ОЧЕНЬ! ❤️</span>
        </button>
        <button class="btn-no" id="btnNo">
          <span>НЕТ</span>
        </button>
      </div>
      <div class="no-comment" id="noComment"></div>
    </div>
  </div>

  <!-- ========================================================
       SCREEN 2: THE QUIZ
       ======================================================== -->
  <div class="screen" id="screen2">
    <div class="top-dots">
      <span></span>
      <span class="active"></span>
      <span></span>
      <span></span>
    </div>

    <div class="quiz-container">
      <div class="quiz-card">
        <div class="quiz-header">
          <span class="quiz-step-title">Тест для Златы 💌</span>
          <span class="quiz-step-counter" id="quizCounter">1 из 5</span>
        </div>

        <div class="quiz-progress">
          <div class="quiz-progress-bar" id="quizProgressBar"></div>
        </div>

        <div class="quiz-question" id="quizQuestionText">Вопрос...</div>

        <div class="quiz-options" id="quizOptionsBox">
          <!-- Populated by JS -->
        </div>

        <div class="quiz-hint" id="quizHint"></div>
      </div>
    </div>
  </div>

  <!-- ========================================================
       SCREEN 3: CELAMUR PORTRAIT & 3D SPIRAL GALAXY
       ======================================================== -->
  <div class="screen celamur-screen" id="screen3">
    <div class="top-dots">
      <span></span>
      <span></span>
      <span class="active"></span>
      <span></span>
    </div>

    <div class="celamur-viewport" id="celamurViewport">
      <canvas id="galaxyCanvas"></canvas>
    </div>

    <div class="celamur-controls">
      <!-- Circular play button -->
      <button class="play-circle-btn" id="celamurPlayBtn" title="Слушать">
        <svg id="playBtnIcon" viewBox="0 0 24 24">
          <polygon points="5,3 19,12 5,21" />
        </svg>
      </button>

      <!-- Signature title -->
      <div class="celamur-title">Злата</div>
      <div class="celamur-subtitle-1">ты выглядишь божественно</div>
      <div class="celamur-subtitle-2">я тебя люблю на всех языках мира</div>
      <div class="celamur-hint" id="celamurHint">✦ проведи пальцем вбок, и она снова станет звёздами ✦</div>

      <!-- Actions -->
      <div class="celamur-actions">
        <button class="btn-celamur-primary" id="btnToggleGalaxy">
          <span id="btnToggleText">Рассыпать в звёзды 🌌</span>
        </button>
        <button class="btn-celamur-secondary" id="btnGotoFinale">
          <span>Наше время →</span>
        </button>
      </div>
    </div>
  </div>

  <!-- ========================================================
       SCREEN 4: ANNIVERSARY TIMER & MEMORIES
       ======================================================== -->
  <div class="screen" id="screen4">
    <div class="top-dots">
      <span></span>
      <span></span>
      <span></span>
      <span class="active"></span>
    </div>

    <div class="finale-container">
      <div class="finale-badge">20.05.2026 19:40</div>
      <h1 class="finale-title">Полгода вместе 🤍</h1>

      <!-- Countdown -->
      <div class="timer-grid">
        <div class="timer-card">
          <div class="timer-val" id="tDays">00</div>
          <div class="timer-lbl">Дней</div>
        </div>
        <div class="timer-card">
          <div class="timer-val" id="tHours">00</div>
          <div class="timer-lbl">Часов</div>
        </div>
        <div class="timer-card">
          <div class="timer-val" id="tMins">00</div>
          <div class="timer-lbl">Минут</div>
        </div>
        <div class="timer-card">
          <div class="timer-val" id="tSecs">00</div>
          <div class="timer-lbl">Секунд</div>
        </div>
      </div>

      <!-- Verbatim quote -->
      <div class="verbatim-quote-card">
        «Вот мы уже пол года вместе, прошли много сложностей и неудач, но нас ждёт долгий и счастливый путь.»
      </div>

      <!-- Button to open memories -->
      <button class="btn-memories" id="btnOpenMemories">
        <span>Открыть наши воспоминания 📸</span>
      </button>
    </div>
  </div>

  <!-- ========================================================
       MEMORIES MODAL / SLIDER (NO ELEVATOR PHOTO)
       ======================================================== -->
  <div class="memories-modal" id="memoriesModal">
    <button class="modal-close-btn" id="btnCloseMemories" title="Закрыть">×</button>

    <div class="slider-card" id="sliderCard">
      <div class="slider-media-box" id="sliderMediaBox">
        <img src="" class="slider-img" id="sliderImg" alt="Воспоминание">
        <video class="slider-video" id="sliderVideo" controls style="display:none;"></video>
      </div>

      <div class="slider-info">
        <div class="slider-caption" id="sliderCaption">Загрузка...</div>
        <div class="slider-counter" id="sliderCounter">1 / 18</div>
        <div class="slider-nav">
          <button class="slider-nav-btn" id="btnPrevSlide">← Предыдущее</button>
          <button class="slider-nav-btn" id="btnNextSlide">Следующее →</button>
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================================
       JAVASCRIPT ENGINE
       ======================================================== -->
  <script>
    // Embedded Data
    const CELAMUR_PORTRAIT_B64 = "{celamur_base64}";
    const GALAXY_PARTICLES = {particles_data};
    const MEMORY_FILES = {memory_files_json};

    // Navigation state
    let currentScreen = 1;
    function goToScreen(num) {{
      document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
      const next = document.getElementById('screen' + num);
      if (next) {{
        next.classList.add('active');
        currentScreen = num;
        if (num === 3) {{
          initCelamurCanvas();
        }}
      }}
    }}

    // Audio controls
    const bgMusic = document.getElementById('bgMusic');
    const audioToggleBtn = document.getElementById('audioToggleBtn');
    let isPlayingAudio = false;

    function toggleMusic() {{
      if (isPlayingAudio) {{
        bgMusic.pause();
        isPlayingAudio = false;
        audioToggleBtn.style.opacity = '0.5';
        updatePlayIcon(false);
      }} else {{
        bgMusic.play().then(() => {{
          isPlayingAudio = true;
          audioToggleBtn.style.opacity = '1';
          updatePlayIcon(true);
        }}).catch(() => {{}});
      }}
    }}

    function updatePlayIcon(playing) {{
      const icon = document.getElementById('playBtnIcon');
      if (icon) {{
        if (playing) {{
          icon.innerHTML = '<rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/>';
        }} else {{
          icon.innerHTML = '<polygon points="5,3 19,12 5,21" />';
        }}
      }}
    }}

    audioToggleBtn.addEventListener('click', toggleMusic);
    document.getElementById('celamurPlayBtn').addEventListener('click', toggleMusic);

    // Screen 1: Dodging NO button
    const btnNo = document.getElementById('btnNo');
    const btnYes = document.getElementById('btnYes');
    const noComment = document.getElementById('noComment');
    let noAttempts = 0;
    const noComments = [
      "Эй, ну так нечестно! 😜",
      "Кнопка сломалась, жми ДА! ❤️",
      "Попробуй поймать! 💫",
      "Я знаю, что ты меня любишь! 🥰",
      "Даже не думай нажимать НЕТ! 🤍"
    ];

    function dodgeNo(e) {{
      noAttempts++;
      noComment.textContent = noComments[noAttempts % noComments.length];
      const maxOffset = 110;
      const rx = (Math.random() - 0.5) * maxOffset * 2;
      const ry = (Math.random() - 0.5) * maxOffset * 1.5;
      btnNo.style.transform = `translate(${{rx}}px, ${{ry}}px) scale(${{Math.max(0.7, 1 - noAttempts * 0.05)}})`;
      spawnHearts(e.clientX || window.innerWidth/2, e.clientY || window.innerHeight/2, 2);
    }}

    btnNo.addEventListener('mouseenter', dodgeNo);
    btnNo.addEventListener('touchstart', (e) => {{
      e.preventDefault();
      dodgeNo(e.touches[0]);
    }});
    btnNo.addEventListener('click', dodgeNo);

    btnYes.addEventListener('click', (e) => {{
      spawnHearts(e.clientX, e.clientY, 15);
      // auto-start music on first user engagement
      if (!isPlayingAudio) toggleMusic();
      setTimeout(() => goToScreen(2), 500);
    }});

    function spawnHearts(x, y, count) {{
      for (let i = 0; i < count; i++) {{
        const heart = document.createElement('div');
        heart.className = 'heart-particle';
        heart.textContent = ['🤍', '💖', '✨', '🌸', '💫'][Math.floor(Math.random() * 5)];
        heart.style.left = (x || window.innerWidth/2) + 'px';
        heart.style.top = (y || window.innerHeight/2) + 'px';
        const tx = (Math.random() - 0.5) * 200 + 'px';
        const ty = -(Math.random() * 150 + 50) + 'px';
        heart.style.setProperty('--tx', tx);
        heart.style.setProperty('--ty', ty);
        document.body.appendChild(heart);
        setTimeout(() => heart.remove(), 1200);
      }}
    }}

    // ========================================================
    // Screen 2: Quiz Logic
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
          "Залипаю в мыслях 💭"
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
      document.getElementById('quizCounter').textContent = `${{currentQ + 1}} из ${{quizQuestions.length}}`;
      document.getElementById('quizProgressBar').style.width = `${{((currentQ + 1) / quizQuestions.length) * 100}}%`;
      document.getElementById('quizQuestionText').textContent = q.q;
      document.getElementById('quizHint').textContent = "";

      const box = document.getElementById('quizOptionsBox');
      box.innerHTML = '';
      q.opts.forEach((optText, idx) => {{
        const btn = document.createElement('button');
        btn.className = 'quiz-opt';
        btn.innerHTML = `<span>${{optText}}</span>`;
        btn.addEventListener('click', () => handleQuizAnswer(idx, btn));
        box.appendChild(btn);
      }});
    }}

    function handleQuizAnswer(selectedIdx, btnElement) {{
      const q = quizQuestions[currentQ];
      if (selectedIdx === q.ans) {{
        btnElement.classList.add('correct');
        spawnHearts(window.innerWidth/2, window.innerHeight/2, 8);
        document.getElementById('quizHint').textContent = "В точку! 🥰";
        setTimeout(() => {{
          currentQ++;
          if (currentQ < quizQuestions.length) {{
            renderQuiz();
          }} else {{
            document.getElementById('quizHint').textContent = "100% совпадение! Ты знаешь меня лучше всех... 💫";
            setTimeout(() => goToScreen(3), 900);
          }}
        }}, 600);
      }} else {{
        btnElement.classList.add('wrong');
        document.getElementById('quizHint').textContent = "Подумай ещё разок, зайка 😉";
        setTimeout(() => btnElement.classList.remove('wrong'), 600);
      }}
    }}
    renderQuiz();

    // ========================================================
    // Screen 3: Celamur Interactive Portrait & 3D Spiral Galaxy
    // ========================================================
    let canvas, ctx;
    let portraitImg = new Image();
    portraitImg.src = CELAMUR_PORTRAIT_B64;

    let isGalaxyMode = false; // Starts in portrait mode
    let morphProgress = 1.0;  // 1 = portrait, 0 = galaxy
    let targetMorph = 1.0;

    // Galaxy 3D Camera & Physics
    let rotY = 0.8;
    let rotX = 66 * Math.PI / 180; // 66 degree inclination tilt
    let velRotY = 0.003;
    let velRotX = 0;
    let isDragging = false;
    let startX = 0, startY = 0;
    let lastX = 0, lastY = 0;

    let canvasWidth = 400;
    let canvasHeight = 460;
    let initializedCanvas = false;

    function initCelamurCanvas() {{
      if (initializedCanvas) return;
      initializedCanvas = true;

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

      // Touch / Mouse controls for 3D Galaxy Drag
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
        rotX = Math.max(0.4, Math.min(1.4, rotX + velRotX));
      }});
      window.addEventListener('mouseup', (e) => {{
        if (isDragging) {{
          const totalDx = Math.abs(e.clientX - startX);
          if (totalDx > 40) {{
            // Horizontal swipe gesture toggles mode!
            toggleGalaxyMode();
          }}
        }}
        isDragging = false;
      }});

      // Touch events
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
        rotX = Math.max(0.4, Math.min(1.4, rotX + velRotX));
      }}, {{ passive: true }});
      canvas.addEventListener('touchend', (e) => {{
        if (isDragging) {{
          const totalDx = Math.abs(lastX - startX);
          if (totalDx > 40) {{
            toggleGalaxyMode();
          }}
        }}
        isDragging = false;
      }});

      requestAnimationFrame(renderLoop);
    }}

    function toggleGalaxyMode() {{
      isGalaxyMode = !isGalaxyMode;
      targetMorph = isGalaxyMode ? 0.0 : 1.0;

      const btnText = document.getElementById('btnToggleText');
      const hint = document.getElementById('celamurHint');
      if (isGalaxyMode) {{
        btnText.textContent = "Собрать портрет ✨";
        hint.textContent = "✦ покрути нашу галактику любви ✦";
      }} else {{
        btnText.textContent = "Рассыпать в звёзды 🌌";
        hint.textContent = "✦ проведи пальцем вбок, и она снова станет звёздами ✦";
      }}
    }}

    document.getElementById('btnToggleGalaxy').addEventListener('click', toggleGalaxyMode);
    document.getElementById('btnGotoFinale').addEventListener('click', () => goToScreen(4));

    // Render loop
    function renderLoop() {{
      if (currentScreen === 3) {{
        // Ease morph progress
        morphProgress += (targetMorph - morphProgress) * 0.08;

        // Auto rotate galaxy with inertia
        if (!isDragging) {{
          velRotY *= 0.96;
          rotY += 0.004 + velRotY;
          velRotX *= 0.92;
          rotX = Math.max(0.4, Math.min(1.4, rotX + velRotX));
        }}

        drawCelamurScene();
      }}
      requestAnimationFrame(renderLoop);
    }}

    function drawCelamurScene() {{
      const W = canvasWidth;
      const H = canvasHeight;
      const cx = W / 2;
      const cy = H / 2 - 15;

      ctx.clearRect(0, 0, W, H);

      // 1. Draw glowing Galaxy Core if in galaxy transition
      const galaxyAlpha = 1.0 - morphProgress;
      if (galaxyAlpha > 0.02) {{
        ctx.save();
        ctx.globalAlpha = galaxyAlpha;
        const coreGrad = ctx.createRadialGradient(cx, cy, 0, cx, cy, 140);
        coreGrad.addColorStop(0, 'rgba(255, 235, 245, 0.85)');
        coreGrad.addColorStop(0.2, 'rgba(255, 120, 160, 0.45)');
        coreGrad.addColorStop(0.5, 'rgba(180, 50, 110, 0.18)');
        coreGrad.addColorStop(1, 'rgba(0, 0, 0, 0)');
        ctx.fillStyle = coreGrad;
        ctx.beginPath();
        ctx.ellipse(cx, cy, 150, 55, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      }}

      // 2. Draw Portrait Duotone base photo if in portrait mode
      if (morphProgress > 0.02 && portraitImg.complete && portraitImg.naturalWidth > 0) {{
        ctx.save();
        ctx.globalAlpha = Math.pow(morphProgress, 1.8) * 0.95;
        // Draw centered with aspect ratio
        const pw = 300;
        const ph = 390;
        ctx.drawImage(portraitImg, cx - pw/2, cy - ph/2, pw, ph);
        ctx.restore();
      }}

      // 3. Render 3D Galaxy and Portrait Scanline Particles
      const D = 420; // 3D Camera distance
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';

      const cosY = Math.cos(rotY);
      const sinY = Math.sin(rotY);
      const cosX = Math.cos(rotX);
      const sinX = Math.sin(rotX);

      // Pre-sort particles by 3D Z depth in galaxy mode
      const len = GALAXY_PARTICLES.length;
      for (let i = 0; i < len; i++) {{
        const p = GALAXY_PARTICLES[i];

        // 3D coordinates in Galaxy
        const gx = p.gx;
        const gy = p.gy;
        const gz = p.gz;

        // Rotate Y
        const x1 = gx * cosY + gz * sinY;
        const z1 = -gx * sinY + gz * cosY;
        const y1 = gy;

        // Rotate X (pitch tilt)
        const y2 = y1 * cosX - z1 * sinX;
        const z2 = y1 * sinX + z1 * cosX;
        const x2 = x1;

        const fov = D / (D + z2);
        const galScreenX = cx + x2 * fov;
        const galScreenY = cy + y2 * fov;

        // 2D Portrait coordinates
        const portScreenX = cx + p.px * 0.95;
        const portScreenY = cy + p.py * 0.95;

        // Interpolated screen position
        const screenX = galScreenX + (portScreenX - galScreenX) * morphProgress;
        const screenY = galScreenY + (portScreenY - galScreenY) * morphProgress;

        // Particle typography styling
        let fontSize, alpha, col;
        if (morphProgress > 0.5) {{
          // Portrait scanline micro-text mode
          fontSize = 7;
          alpha = 0.55 + 0.35 * morphProgress;
          col = `rgba(255, 225, 235, ${{alpha}})`;
        }} else {{
          // Galaxy 3D starfield mode
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
          ctx.fillText(p.t, screenX, screenY);
        }}
      }}
    }}

    // ========================================================
    // Screen 4: Countdown Timer (from 20.05.2026, 19:40)
    // ========================================================
    const anniversaryDate = new Date(2026, 4, 20, 19, 40, 0); // Month 4 is May

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
    // Memories Modal / Slider (NO ELEVATOR PHOTO)
    // ========================================================
    let currentSlide = 0;
    const memoriesModal = document.getElementById('memoriesModal');
    const sliderImg = document.getElementById('sliderImg');
    const sliderVideo = document.getElementById('sliderVideo');
    const sliderCaption = document.getElementById('sliderCaption');
    const sliderCounter = document.getElementById('sliderCounter');

    function openMemories() {{
      memoriesModal.classList.add('open');
      showSlide(0);
    }}

    function closeMemories() {{
      memoriesModal.classList.remove('open');
      sliderVideo.pause();
    }}

    function showSlide(idx) {{
      if (idx < 0) idx = MEMORY_FILES.length - 1;
      if (idx >= MEMORY_FILES.length) idx = 0;
      currentSlide = idx;

      const item = MEMORY_FILES[idx];
      sliderCaption.textContent = item.caption;
      sliderCounter.textContent = `${{idx + 1}} / ${{MEMORY_FILES.length}}`;

      const isVideo = item.name.toLowerCase().endsWith('.mp4');
      const mediaPath = 'media/' + item.name;

      if (isVideo) {{
        sliderImg.style.display = 'none';
        sliderVideo.style.display = 'block';
        sliderVideo.src = mediaPath;
        sliderVideo.play().catch(() => {{}});
      }} else {{
        sliderVideo.pause();
        sliderVideo.style.display = 'none';
        sliderImg.style.display = 'block';
        sliderImg.src = mediaPath;
      }}
    }}

    document.getElementById('btnOpenMemories').addEventListener('click', openMemories);
    document.getElementById('btnCloseMemories').addEventListener('click', closeMemories);
    document.getElementById('btnPrevSlide').addEventListener('click', () => showSlide(currentSlide - 1));
    document.getElementById('btnNextSlide').addEventListener('click', () => showSlide(currentSlide + 1));

    // Keyboard and touch swipe for slider
    window.addEventListener('keydown', (e) => {{
      if (!memoriesModal.classList.contains('open')) return;
      if (e.key === 'ArrowLeft') showSlide(currentSlide - 1);
      if (e.key === 'ArrowRight') showSlide(currentSlide + 1);
      if (e.key === 'Escape') closeMemories();
    }});

    let touchStartX = 0;
    memoriesModal.addEventListener('touchstart', (e) => {{
      touchStartX = e.touches[0].clientX;
    }}, {{ passive: true }});
    memoriesModal.addEventListener('touchend', (e) => {{
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

print('SUCCESS! d:/подарки пол года/index.html generated successfully!')
print(f'File size: {os.path.getsize("d:/подарки пол года/index.html")} bytes')
