# -*- coding: utf-8 -*-
"""
Generator script for Zlata's 6-Month Anniversary Website (index.html)
Features:
- Screen 1: Clean romantic hook -> Click YES triggers playful "Try NO first!" -> NO dodges with animated Telegram cat -> Unlocks YES with celebration!
- Screen 2: Cute quiz with animated reactions and heart progress
- Screen 3: Celamur Galaxy STARTS IN 3D DISPERSED MODE first! Morph is purely button-controlled so she can rotate the 3D galaxy without accidental triggering.
- Screen 4: Countdown timer + verbatim quote + "Back to Galaxy" button + Stories memories carousel with instant preloading!
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
    {"name": "с чего все началось.jpg", "caption": "С чего всё началось 🤍", "date": "Начало нашей истории", "sticker": "hello.gif"},
    {"name": "первые цветы.jpg", "caption": "Твои первые цветы 💐", "date": "Самый нежный момент", "sticker": "adore.gif"},
    {"name": "свидание на природе.jpg", "caption": "Наше свидание на природе 🌿", "date": "Только ты и я 🍃", "sticker": "serene.gif"},
    {"name": "свидание на природе 2 фото.jpg", "caption": "Наше свидание на природе 🌿", "date": "Только ты и я 🍃", "sticker": "serene.gif"},
    {"name": "IMG_20261115_230355_318.jpg", "caption": "Золотой закат на балконе — ты невероятно красива 🌅", "date": "Не могу оторвать взгляд ✨", "sticker": "shy.gif"},
    {"name": "IMG_20261115_230620_235.jpg", "caption": "Счастливы вместе — настоящие мы ✨", "date": "В любые трудности вместе 🤍", "sticker": "cat_love.gif"},
    {"name": "IMG_20261115_232741_361.jpg", "caption": "Открытость, искренность и самые душевные разговоры 🤍", "date": "Тёплые разговоры 💌", "sticker": "smile.gif"},
    {"name": "IMG_20261115_233109_723.jpg", "caption": "Хочу сделать так, чтобы ты всегда сияла 💫", "date": "Моё сияние ✨", "sticker": "glowing.gif"},
    {"name": "IMG_20261116_000248_096.jpg", "caption": "Навсегда в моём сердце 💌", "date": "Любимый кадр", "sticker": "love.gif"},
    {"name": "5462926877434519487.jpg", "caption": "Твоя любимая улыбка 🥰", "date": "Самая милая", "sticker": "happy.gif"},
    {"name": "5462926877434519488.jpg", "caption": "Счастье в простых моментах 🍓", "date": "Вкусные радости", "sticker": "sushi.gif"},
    {"name": "5462926877434519489.jpg", "caption": "Всегда рядом с тобой 🤍", "date": "Наше тепло", "sticker": "relaxed.gif"},
    {"name": "5462926877434519490.jpg", "caption": "Самая прекрасная ✨", "date": "Моё вдохновение", "sticker": "sparkle.gif"},
    {"name": "5462926877434519491.jpg", "caption": "Твой любимый взгляд 💫", "date": "В твоих глазах весь мир", "sticker": "wink.gif"},
    {"name": "мы самые яркие звезды.mp4", "caption": "Мы — самые яркие звёзды ✨", "date": "Наше сияние 🎬", "sticker": "dancing.gif"},
    {"name": "video5462926876974558922.mp4", "caption": "Полностью хуйня 😂", "date": "Живые моменты 🎬", "sticker": "laughing.gif"},
    {"name": "video5462926876974558921.mp4", "caption": "Тёплые воспоминания 🎞️", "date": "Лето нашей любви", "sticker": "playful.gif"},
    {"name": "HnVideoEditor_2026_11_16_002803168.mp4", "caption": "Хочу мокнуть под дождём с тобой всегда 🌧️🤍", "date": "Полгода вместе 💖", "sticker": "rain.gif"}
]

memory_files_json = json.dumps(memory_files, ensure_ascii=False)

html_template = f'''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>Злата — Наша Вселенная 🤍</title>
  
  <!-- Premium & Cute Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Great+Vibes&family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">

  <style>
    :root {{
      --bg: #060209;
      --card-bg: rgba(28, 16, 34, 0.78);
      --card-border: rgba(255, 180, 210, 0.2);
      --pink-primary: #ff527b;
      --pink-glow: rgba(255, 82, 123, 0.55);
      --pink-candy: linear-gradient(135deg, #ff7597 0%, #ff3b68 100%);
      --pink-shadow: #b31d42;
      --yellow-butter: #ffeaa7;
      --text-white: #ffffff;
      --text-cream: #f7eef7;
      --text-muted: #b8a6be;
      --font-rounded: 'Nunito', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-hand: 'Caveat', cursive;
      --font-cursive: 'Great Vibes', cursive;
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
      color: var(--text-white);
      font-family: var(--font-rounded);
      overflow: hidden;
      position: fixed;
    }}

    /* Starry dynamic background */
    #ambientSkyCanvas {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 0;
    }}

    /* Soft colorful light blobs */
    .blob-ambient {{
      position: fixed;
      width: 340px;
      height: 340px;
      border-radius: 50%;
      filter: blur(90px);
      pointer-events: none;
      z-index: 0;
      opacity: 0.32;
      animation: floatBlobs 12s infinite alternate ease-in-out;
    }}
    .blob-top {{
      top: -80px;
      left: 50%;
      transform: translateX(-50%);
      background: radial-gradient(circle, #ff4071 0%, transparent 70%);
    }}
    .blob-bottom {{
      bottom: -60px;
      right: -40px;
      background: radial-gradient(circle, #8a2be2 0%, transparent 70%);
      animation-delay: -6s;
    }}
    @keyframes floatBlobs {{
      0% {{ transform: translate(-50%, 0) scale(0.9); }}
      100% {{ transform: translate(-50%, 45px) scale(1.18); }}
    }}

    /* Ambient floating animated stickers in deep starry background */
    .ambient-stickers-container {{
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 1;
      overflow: hidden;
    }}

    .floating-bg-sticker {{
      position: absolute;
      width: 66px;
      height: auto;
      opacity: 0.22;
      filter: drop-shadow(0 0 16px rgba(255, 130, 180, 0.45));
      pointer-events: none;
      will-change: transform, opacity;
    }}

    .fbs-1 {{
      left: 7%;
      bottom: -80px;
      animation: floatDriftUp1 28s infinite linear;
    }}
    .fbs-2 {{
      right: 8%;
      bottom: -90px;
      width: 74px;
      animation: floatDriftUp2 34s infinite linear 5s;
    }}
    .fbs-3 {{
      left: 18%;
      bottom: -85px;
      width: 60px;
      animation: floatDriftUp3 30s infinite linear 12s;
    }}
    .fbs-4 {{
      right: 20%;
      bottom: -80px;
      width: 64px;
      animation: floatDriftUp1 36s infinite linear 18s;
    }}
    .fbs-5 {{
      left: 45%;
      bottom: -90px;
      width: 68px;
      animation: floatDriftUp2 32s infinite linear 24s;
    }}

    @keyframes floatDriftUp1 {{
      0% {{
        transform: translateY(0) translateX(0) rotate(0deg) scale(0.85);
        opacity: 0;
      }}
      10% {{ opacity: 0.24; }}
      50% {{
        transform: translateY(-55vh) translateX(35px) rotate(8deg) scale(1);
        opacity: 0.28;
      }}
      90% {{ opacity: 0.22; }}
      100% {{
        transform: translateY(-115vh) translateX(-20px) rotate(-6deg) scale(0.9);
        opacity: 0;
      }}
    }}

    @keyframes floatDriftUp2 {{
      0% {{
        transform: translateY(0) translateX(0) rotate(0deg) scale(0.9);
        opacity: 0;
      }}
      12% {{ opacity: 0.26; }}
      50% {{
        transform: translateY(-60vh) translateX(-40px) rotate(-10deg) scale(1.05);
        opacity: 0.3;
      }}
      88% {{ opacity: 0.22; }}
      100% {{
        transform: translateY(-118vh) translateX(25px) rotate(8deg) scale(0.88);
        opacity: 0;
      }}
    }}

    @keyframes floatDriftUp3 {{
      0% {{
        transform: translateY(0) translateX(0) rotate(0deg) scale(0.8);
        opacity: 0;
      }}
      15% {{ opacity: 0.22; }}
      50% {{
        transform: translateY(-50vh) translateX(28px) rotate(6deg) scale(0.95);
        opacity: 0.26;
      }}
      85% {{ opacity: 0.18; }}
      100% {{
        transform: translateY(-112vh) translateX(-30px) rotate(-8deg) scale(0.85);
        opacity: 0;
      }}
    }}

    /* Global screen container */
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
      padding: 24px 18px;
      opacity: 0;
      pointer-events: none;
      transform: scale(0.94) translateY(24px);
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

    /* Cute Header Navigation */
    .cute-nav-bar {{
      position: fixed;
      top: 14px;
      left: 0;
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 18px;
      z-index: 50;
      pointer-events: none;
    }}

    .candy-hearts-track {{
      display: flex;
      gap: 7px;
      pointer-events: auto;
      background: rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(15px);
      -webkit-backdrop-filter: blur(15px);
      padding: 6px 14px;
      border-radius: 9999px;
      border: 1px solid rgba(255, 255, 255, 0.12);
      box-shadow: 0 4px 16px rgba(0,0,0,0.4);
    }}
    .candy-heart {{
      font-size: 14px;
      opacity: 0.35;
      transform: scale(0.85);
      transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    .candy-heart.glow {{
      opacity: 1;
      transform: scale(1.15);
      filter: drop-shadow(0 0 8px var(--pink-primary));
    }}

    .cute-music-btn {{
      pointer-events: auto;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.08);
      border: 1.5px solid rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(15px);
      -webkit-backdrop-filter: blur(15px);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      cursor: pointer;
      box-shadow: 0 4px 18px rgba(0,0,0,0.4);
      transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    .cute-music-btn:active {{
      transform: scale(0.88);
    }}
    .cute-music-btn.playing {{
      border-color: #ff6584;
      color: #ff6584;
      box-shadow: 0 0 20px var(--pink-glow);
      animation: musicBeat 1.8s infinite ease-in-out;
    }}
    @keyframes musicBeat {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.1); }}
    }}

    /* ========================================================
       SCREEN 1: THE POLAROID & PLAYFUL DODGING 'NO'
       ======================================================== */
    .hook-wrapper {{
      max-width: 360px;
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      position: relative;
      margin-top: 15px;
    }}

    /* Tilted Aesthetic Polaroid */
    .polaroid-frame {{
      position: relative;
      background: #ffffff;
      padding: 10px 10px 24px 10px;
      border-radius: 12px;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.7), 0 2px 10px rgba(255, 255, 255, 0.1);
      transform: rotate(-2.5deg);
      transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
      cursor: pointer;
      width: 175px;
      margin-bottom: 8px;
    }}
    .polaroid-frame:hover, .polaroid-frame:active {{
      transform: rotate(0deg) scale(1.04);
    }}
    .polaroid-tape {{
      position: absolute;
      top: -12px;
      left: 50%;
      transform: translateX(-50%) rotate(2deg);
      width: 60px;
      height: 22px;
      background: rgba(255, 175, 195, 0.85);
      border-radius: 4px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.2);
    }}
    .polaroid-photo {{
      width: 100%;
      height: 165px;
      border-radius: 8px;
      object-fit: cover;
      display: block;
    }}
    .polaroid-caption {{
      font-family: var(--font-hand);
      color: #2b1f2d;
      font-size: 17px;
      font-weight: 700;
      margin-top: 7px;
      line-height: 1;
    }}

    /* Animated Telegram Cat Stickers */
    .animated-sticker-cat {{
      position: absolute;
      width: 65px;
      height: 65px;
      pointer-events: none;
      filter: drop-shadow(0 6px 14px rgba(0,0,0,0.6));
      z-index: 10;
    }}
    .cat-corner-left {{
      top: 15px;
      left: -8px;
      animation: floatCat 3.5s infinite alternate ease-in-out;
    }}
    .cat-corner-right {{
      top: 110px;
      right: -8px;
      animation: floatCat 3.5s infinite alternate ease-in-out -1.7s;
    }}
    @keyframes floatCat {{
      0% {{ transform: translateY(0) rotate(-5deg); }}
      100% {{ transform: translateY(-8px) rotate(5deg); }}
    }}

    .hook-name {{
      font-family: var(--font-cursive);
      font-size: 52px;
      line-height: 1;
      color: #ffffff;
      text-shadow: 0 0 25px rgba(255, 140, 180, 0.7);
      margin-top: 4px;
    }}

    .hook-question-text {{
      font-size: 21px;
      font-weight: 800;
      color: var(--text-cream);
      margin-top: -4px;
    }}

    /* Teasing banner - APPEARS ONLY WHEN SHE TAPS YES FIRST! */
    .tease-banner-alert {{
      display: none;
      align-items: center;
      gap: 10px;
      background: linear-gradient(135deg, rgba(255, 234, 167, 0.22) 0%, rgba(255, 180, 100, 0.18) 100%);
      border: 1.5px dashed rgba(255, 234, 167, 0.7);
      color: #ffeaa7;
      padding: 10px 18px;
      border-radius: 18px;
      font-size: 14px;
      font-weight: 800;
      margin-top: 8px;
      box-shadow: 0 4px 18px rgba(255, 234, 167, 0.2);
      animation: popIn 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    .tease-banner-alert.show {{
      display: flex;
    }}
    .tease-cat-icon {{
      width: 28px;
      height: 28px;
      flex-shrink: 0;
    }}
    @keyframes popIn {{
      0% {{ transform: scale(0.85); opacity: 0; }}
      100% {{ transform: scale(1); opacity: 1; }}
    }}

    /* Button interaction area */
    .hook-playground {{
      position: relative;
      width: 100%;
      min-height: 145px;
      margin-top: 12px;
    }}

    /* Physical 3D Marshmallow Button (YES) */
    .marshmallow-btn-yes {{
      width: 100%;
      background: var(--pink-candy);
      color: #ffffff;
      border: none;
      padding: 16px 28px;
      border-radius: 9999px;
      font-size: 16px;
      font-weight: 900;
      cursor: pointer;
      box-shadow: 0 6px 0 var(--pink-shadow), 0 12px 25px var(--pink-glow);
      transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }}
    .marshmallow-btn-yes:active {{
      transform: translateY(4px);
      box-shadow: 0 2px 0 var(--pink-shadow), 0 6px 15px var(--pink-glow);
    }}
    .marshmallow-btn-yes.ready-pulse {{
      animation: readyPulseAnim 1.1s infinite alternate ease-in-out;
    }}
    @keyframes readyPulseAnim {{
      0% {{ transform: scale(1); box-shadow: 0 6px 0 var(--pink-shadow), 0 10px 25px var(--pink-glow); }}
      100% {{ transform: scale(1.05); box-shadow: 0 6px 0 var(--pink-shadow), 0 16px 40px rgba(255, 82, 123, 0.85); }}
    }}

    /* Dodging NO button */
    .dodging-btn-no {{
      position: absolute;
      top: 74px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(255, 255, 255, 0.1);
      color: #ff7597;
      border: 2px solid rgba(255, 117, 151, 0.5);
      padding: 12px 36px;
      border-radius: 9999px;
      font-size: 16px;
      font-weight: 800;
      cursor: pointer;
      box-shadow: 0 4px 0 rgba(0,0,0,0.4), 0 8px 20px rgba(0,0,0,0.5);
      transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1), background 0.2s;
      white-space: nowrap;
      z-index: 10;
    }}
    .dodging-btn-no:hover, .dodging-btn-no:active {{
      background: rgba(255, 117, 151, 0.25);
    }}
    .dodging-btn-no.highlight-wiggle {{
      animation: wiggleNo 0.8s infinite alternate ease-in-out;
      border-color: #ffeaa7;
      color: #ffeaa7;
      box-shadow: 0 0 20px rgba(255, 234, 167, 0.5);
    }}
    @keyframes wiggleNo {{
      0% {{ transform: translateX(-50%) rotate(-4deg); }}
      100% {{ transform: translateX(-50%) rotate(4deg); }}
    }}

    /* Comic speech bubble with animated cat */
    .comic-speech-bubble {{
      position: absolute;
      top: -54px;
      left: 50%;
      transform: translateX(-50%) scale(0.7);
      background: #ffffff;
      color: #1a0820;
      padding: 6px 14px;
      border-radius: 14px;
      font-size: 13px;
      font-weight: 800;
      white-space: nowrap;
      box-shadow: 0 8px 25px rgba(0,0,0,0.6);
      opacity: 0;
      pointer-events: none;
      transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .comic-speech-bubble img {{
      width: 26px;
      height: 26px;
    }}
    .comic-speech-bubble::after {{
      content: '';
      position: absolute;
      bottom: -6px;
      left: 50%;
      transform: translateX(-50%);
      border-width: 6px 6px 0 6px;
      border-style: solid;
      border-color: #ffffff transparent transparent transparent;
    }}
    .comic-speech-bubble.active {{
      opacity: 1;
      transform: translateX(-50%) scale(1);
    }}

    /* ========================================================
       SCREEN 2: CUTE QUIZ DECK
       ======================================================== */
    .quiz-container-box {{
      max-width: 390px;
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .quiz-interactive-card {{
      background: var(--card-bg);
      border: 1.5px solid var(--card-border);
      backdrop-filter: blur(25px);
      -webkit-backdrop-filter: blur(25px);
      border-radius: 34px;
      padding: 26px 20px;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.75), inset 0 1px 0 rgba(255, 255, 255, 0.2);
      display: flex;
      flex-direction: column;
      gap: 18px;
      position: relative;
    }}

    .quiz-top-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .quiz-love-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 82, 123, 0.15);
      border: 1px solid rgba(255, 82, 123, 0.3);
      padding: 5px 12px;
      border-radius: 9999px;
      color: #ff9bb5;
      font-size: 12px;
      font-weight: 800;
    }}
    .quiz-love-badge img {{
      width: 20px;
      height: 20px;
    }}
    .quiz-index-pill {{
      background: rgba(255, 255, 255, 0.08);
      padding: 4px 12px;
      border-radius: 9999px;
      font-size: 11px;
      font-weight: 800;
      color: var(--text-muted);
    }}

    .quiz-question-heading {{
      font-size: 20px;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.35;
      text-align: left;
    }}

    .quiz-choices-stack {{
      display: flex;
      flex-direction: column;
      gap: 11px;
    }}

    .quiz-pill-choice {{
      background: rgba(255, 255, 255, 0.05);
      border: 1.5px solid rgba(255, 255, 255, 0.1);
      padding: 15px 18px;
      border-radius: 20px;
      color: var(--text-cream);
      font-size: 15px;
      font-weight: 700;
      text-align: left;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
      transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    .quiz-pill-choice:active {{
      transform: scale(0.97);
    }}
    .quiz-pill-choice.correct {{
      background: rgba(46, 213, 115, 0.2);
      border-color: #2ed573;
      color: #ffffff;
      box-shadow: 0 0 25px rgba(46, 213, 115, 0.4);
      transform: scale(1.02);
    }}
    .quiz-pill-choice.wrong {{
      background: rgba(255, 71, 87, 0.2);
      border-color: #ff4757;
      color: #ff6b81;
      animation: cardShake 0.4s ease;
    }}
    @keyframes cardShake {{
      0%, 100% {{ transform: translateX(0); }}
      25% {{ transform: translateX(-8px); }}
      75% {{ transform: translateX(8px); }}
    }}

    .quiz-feedback-toast {{
      font-size: 14px;
      font-weight: 800;
      color: #ff8fab;
      text-align: center;
      min-height: 22px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }}
    .quiz-feedback-toast img {{
      width: 22px;
      height: 22px;
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
      padding: 16px 16px 26px 16px;
    }}

    .celamur-stage-viewport {{
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

    .celamur-controls-box {{
      width: 100%;
      max-width: 380px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 10px;
      z-index: 10;
    }}

    .celamur-play-disc {{
      width: 52px;
      height: 52px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.12);
      border: 1.5px solid rgba(255, 255, 255, 0.22);
      backdrop-filter: blur(15px);
      -webkit-backdrop-filter: blur(15px);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      cursor: pointer;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.7);
      transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    .celamur-play-disc:active {{
      transform: scale(0.9);
    }}
    .celamur-play-disc svg {{
      width: 22px;
      height: 22px;
      fill: currentColor;
    }}

    .celamur-main-title {{
      font-family: var(--font-cursive);
      font-size: clamp(34px, 8.5vw, 46px);
      line-height: 1.1;
      color: #ffffff;
      text-shadow: 0 0 25px rgba(255, 180, 210, 0.75), 0 0 50px rgba(255, 82, 123, 0.4);
      margin-top: -2px;
      white-space: nowrap;
      text-align: center;
    }}

    .celamur-subtitle-divine {{
      font-size: 16px;
      font-weight: 800;
      color: #fff0f6;
      letter-spacing: 0.3px;
      text-shadow: 0 0 12px rgba(255, 180, 210, 0.5);
    }}

    .celamur-subtitle-languages {{
      font-size: 13.5px;
      font-weight: 700;
      color: #f7d2e4;
      margin-top: -2px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 5px;
      flex-wrap: wrap;
    }}

    .celamur-love-highlight {{
      background: linear-gradient(135deg, #ffffff 0%, #ff85a2 40%, #ff3366 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      font-size: 15.5px;
      font-weight: 900;
      filter: drop-shadow(0 0 8px rgba(255, 82, 123, 0.7));
      letter-spacing: 0.3px;
    }}

    .celamur-drag-hint-pill {{
      font-size: 11px;
      font-weight: 600;
      color: rgba(255, 255, 255, 0.5);
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    .celamur-actions-group {{
      display: flex;
      flex-direction: column;
      gap: 10px;
      width: 100%;
      margin-top: 6px;
    }}

    .btn-marshmallow-pink {{
      background: var(--pink-candy);
      color: #ffffff;
      border: none;
      padding: 15px 28px;
      border-radius: 9999px;
      font-size: 15px;
      font-weight: 800;
      cursor: pointer;
      box-shadow: 0 5px 0 var(--pink-shadow), 0 10px 25px var(--pink-glow);
      transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }}
    .btn-marshmallow-pink:active {{
      transform: translateY(3px);
      box-shadow: 0 2px 0 var(--pink-shadow), 0 5px 15px var(--pink-glow);
    }}

    .btn-marshmallow-glass {{
      background: rgba(255, 255, 255, 0.08);
      color: #ede4f0;
      border: 1.5px solid rgba(255, 255, 255, 0.15);
      padding: 14px 28px;
      border-radius: 9999px;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      backdrop-filter: blur(15px);
      -webkit-backdrop-filter: blur(15px);
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }}
    .btn-marshmallow-glass:active {{
      transform: scale(0.97);
    }}

    /* ========================================================
       SCREEN 4: ANNIVERSARY TIMER & MEMORIES
       ======================================================== */
    .finale-box {{
      max-width: 410px;
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 16px;
      text-align: center;
    }}

    .finale-top-nav-row {{
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .btn-back-galaxy {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      padding: 6px 14px;
      border-radius: 9999px;
      color: #f7eef7;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.2s ease;
    }}
    .btn-back-galaxy:active {{
      transform: scale(0.95);
      background: rgba(255, 255, 255, 0.15);
    }}

    .finale-cute-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: 9999px;
      background: rgba(255, 82, 123, 0.15);
      border: 1px solid rgba(255, 82, 123, 0.35);
      color: #ff9bb5;
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.5px;
    }}

    .finale-title-text {{
      font-family: var(--font-cursive);
      font-size: 48px;
      line-height: 1;
      color: #ffffff;
      text-shadow: 0 0 25px rgba(255, 180, 200, 0.6);
    }}

    /* Modern Squircle Widget Countdown */
    .timer-squircle-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
      width: 100%;
    }}

    .squircle-card {{
      background: rgba(255, 255, 255, 0.05);
      border: 1.5px solid rgba(255, 255, 255, 0.12);
      border-radius: 22px;
      padding: 14px 4px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
      backdrop-filter: blur(15px);
      -webkit-backdrop-filter: blur(15px);
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }}
    .squircle-val {{
      font-size: 27px;
      font-weight: 900;
      color: #ffffff;
      font-variant-numeric: tabular-nums;
      line-height: 1;
    }}
    .squircle-lbl {{
      font-size: 11px;
      color: var(--text-muted);
      text-transform: uppercase;
      font-weight: 800;
      letter-spacing: 0.8px;
    }}

    /* Romantic Letter Card with Verbatim Quote */
    .letter-romantic-card {{
      background: rgba(255, 255, 255, 0.04);
      border-left: 3.5px solid var(--pink-primary);
      border-radius: 8px 22px 22px 8px;
      padding: 18px 20px;
      font-size: 15px;
      line-height: 1.6;
      color: #ede2f0;
      font-style: italic;
      text-align: left;
      position: relative;
      backdrop-filter: blur(15px);
      -webkit-backdrop-filter: blur(15px);
      box-shadow: 0 10px 35px rgba(0,0,0,0.5);
    }}
    .letter-romantic-card::before {{
      content: '“';
      position: absolute;
      top: -12px;
      left: 12px;
      font-size: 46px;
      color: rgba(255, 82, 123, 0.35);
      font-family: serif;
    }}
    .letter-signature-tag {{
      margin-top: 8px;
      font-family: var(--font-hand);
      font-size: 19px;
      font-weight: 700;
      color: #ffeaa7;
      text-align: right;
    }}

    .btn-memories-trigger {{
      background: var(--pink-candy);
      color: #ffffff;
      border: none;
      padding: 16px 32px;
      border-radius: 9999px;
      font-size: 16px;
      font-weight: 800;
      cursor: pointer;
      box-shadow: 0 6px 0 var(--pink-shadow), 0 12px 30px var(--pink-glow);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      width: 100%;
      transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    .btn-memories-trigger:active {{
      transform: translateY(4px);
      box-shadow: 0 2px 0 var(--pink-shadow), 0 6px 15px var(--pink-glow);
    }}

    /* ========================================================
       MEMORIES STORY VIEWER (FULLSCREEN INSTAGRAM STORIES STYLE)
       ======================================================== */
    .story-viewer-modal {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.96);
      backdrop-filter: blur(35px);
      -webkit-backdrop-filter: blur(35px);
      z-index: 1000;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 18px 16px;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.35s ease;
    }}
    .story-viewer-modal.active {{
      opacity: 1;
      pointer-events: auto;
    }}

    .story-close-round-btn {{
      position: absolute;
      top: 18px;
      right: 18px;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #fff;
      font-size: 26px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 1010;
      transition: all 0.2s ease;
    }}
    .story-close-round-btn:active {{
      transform: scale(0.9);
    }}

    .story-stage-card {{
      max-width: 410px;
      width: 100%;
      background: rgba(22, 14, 26, 0.92);
      border: 1.5px solid rgba(255, 255, 255, 0.14);
      border-radius: 34px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 25px 70px rgba(0, 0, 0, 0.9);
      position: relative;
    }}

    /* Instagram-style segmented story progress bars */
    .story-segments-header {{
      display: flex;
      gap: 4px;
      padding: 12px 14px 4px 14px;
      width: 100%;
    }}
    .story-segment-bar {{
      flex: 1;
      height: 3px;
      background: rgba(255, 255, 255, 0.2);
      border-radius: 2px;
      overflow: hidden;
    }}
    .story-segment-bar.viewed {{
      background: var(--pink-primary);
    }}

    .story-viewport-box {{
      width: 100%;
      height: 380px;
      background: #000000;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }}

    .story-img-element {{
      width: 100%;
      height: 100%;
      object-fit: contain;
      transition: opacity 0.25s ease;
    }}

    .story-video-element {{
      width: 100%;
      height: 100%;
      object-fit: contain;
    }}

    .story-details-footer {{
      padding: 16px 20px 20px 20px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      text-align: center;
    }}

    .story-date-badge {{
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: #ff9bb5;
    }}

    .story-caption-title {{
      font-size: 17px;
      font-weight: 800;
      color: #ffffff;
      margin-top: -6px;
    }}

    .story-slide-counter {{
      font-size: 12px;
      color: var(--text-muted);
      font-weight: 700;
      letter-spacing: 1px;
    }}

    .story-navigation-row {{
      display: flex;
      gap: 10px;
      width: 100%;
    }}

    .story-nav-btn {{
      flex: 1;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.14);
      padding: 13px;
      border-radius: 9999px;
      color: #ffffff;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.2s ease;
    }}
    .story-nav-btn:active {{
      background: rgba(255, 255, 255, 0.16);
      transform: scale(0.97);
    }}

    /* Physical heart particle generator */
    .burst-heart-item {{
      position: fixed;
      pointer-events: none;
      z-index: 99999;
      font-size: 22px;
      will-change: transform, opacity;
    }}

    /* Polaroid peeking cute mascot */
    .polaroid-mascot-peek {{
      position: absolute;
      top: -34px;
      right: -8px;
      width: 54px;
      height: auto;
      z-index: 10;
      filter: drop-shadow(0 4px 10px rgba(0,0,0,0.5));
      animation: cuteBobbing 3.5s infinite ease-in-out;
      pointer-events: none;
    }}
    @keyframes cuteBobbing {{
      0%, 100% {{ transform: translateY(0) rotate(2deg); }}
      50% {{ transform: translateY(-4px) rotate(-3deg); }}
    }}

    /* Button mini sticker */
    .btn-cat-mini-sticker {{
      width: 24px;
      height: 24px;
      object-fit: contain;
      vertical-align: middle;
      margin-right: 6px;
    }}

    /* Quiz cheerleader mascot */
    .quiz-cat-cheerleader {{
      position: absolute;
      top: -38px;
      right: 12px;
      width: 58px;
      height: auto;
      z-index: 15;
      filter: drop-shadow(0 4px 12px rgba(0,0,0,0.5));
      transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
      pointer-events: none;
    }}

    /* Letter card cat */
    .letter-corner-cat {{
      position: absolute;
      top: -24px;
      right: 14px;
      width: 48px;
      height: auto;
      filter: drop-shadow(0 4px 12px rgba(0,0,0,0.5));
      animation: softSway 4s infinite ease-in-out;
      pointer-events: none;
    }}
    @keyframes softSway {{
      0%, 100% {{ transform: rotate(0deg) translateY(0); }}
      50% {{ transform: rotate(4deg) translateY(-3px); }}
    }}

    /* Stories footer sticker */
    .story-date-row {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
    }}
    .story-footer-cat-sticker {{
      width: 38px;
      height: 38px;
      object-fit: contain;
      filter: drop-shadow(0 2px 8px rgba(255, 82, 123, 0.45));
    }}
    @keyframes cuteStickerPop {{
      0% {{ transform: scale(0.6); opacity: 0; }}
      100% {{ transform: scale(1); opacity: 1; }}
    }}
  </style>
</head>
<body>

  <!-- Starry Ambient Canvas & Lights -->
  <canvas id="ambientSkyCanvas"></canvas>
  <div class="blob-ambient blob-top"></div>
  <div class="blob-ambient blob-bottom"></div>

  <!-- Ambient floating animated stickers in deep starry sky -->
  <div class="ambient-stickers-container">
    <img src="media/stickers/sleepy.gif" class="floating-bg-sticker fbs-1" alt="Cat">
    <img src="media/stickers/sparkle.gif" class="floating-bg-sticker fbs-2" alt="Cat">
    <img src="media/stickers/cat_love.gif" class="floating-bg-sticker fbs-3" alt="Cat">
    <img src="media/stickers/hello.gif" class="floating-bg-sticker fbs-4" alt="Cat">
    <img src="media/stickers/relaxed.gif" class="floating-bg-sticker fbs-5" alt="Cat">
  </div>

  <!-- Background Music Audio -->
  <audio id="bgMusic" src="media/music.mp3" preload="auto" loop></audio>

  <!-- Top Navigation Bar -->
  <div class="cute-nav-bar">
    <div class="candy-hearts-track" id="candyTrack">
      <span class="candy-heart glow" id="ch1">💖</span>
      <span class="candy-heart" id="ch2">🤍</span>
      <span class="candy-heart" id="ch3">🤍</span>
      <span class="candy-heart" id="ch4">🤍</span>
    </div>

    <button class="cute-music-btn" id="musicToggleBtn" title="Музыка">
      <svg id="musicIconSvg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
        <path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/>
      </svg>
    </button>
  </div>

  <!-- ========================================================
       SCREEN 1: THE POLAROID & PLAYFUL DODGING 'NO'
       ======================================================== -->
  <div class="screen active" id="screen1">
    <div class="hook-wrapper">
      
      <!-- Animated Telegram Cat Stickers -->
      <img src="media/stickers/love.gif" class="animated-sticker-cat cat-corner-left" alt="Котик">
      <img src="media/stickers/adore.gif" class="animated-sticker-cat cat-corner-right" alt="Котик">

      <!-- Tilted Aesthetic Polaroid -->
      <div class="polaroid-frame" id="polaroidCard">
        <div class="polaroid-tape"></div>
        <img src="media/stickers/hello.gif" class="polaroid-mascot-peek" alt="Привет">
        <img src="media/5462926877434519487.jpg" class="polaroid-photo" alt="Злата">
        <div class="polaroid-caption">моя любимая девочка 🤍</div>
      </div>

      <h1 class="hook-name">Злата</h1>
      <p class="hook-question-text">Ты меня сильно любишь?</p>

      <!-- Teasing alert banner - APPEARS ONLY WHEN SHE TAPS YES FIRST! -->
      <div class="tease-banner-alert" id="teaseAlert">
        <img src="media/stickers/teasing.gif" class="tease-cat-icon" alt="Кот">
        <span id="teaseAlertText">Эй, так просто не пойдёт! Попробуй сначала нажать «НЕТ» 😜👇</span>
      </div>

      <!-- Interactive Playground -->
      <div class="hook-playground" id="playgroundArea">
        <!-- YES button -->
        <button class="marshmallow-btn-yes" id="btnYes">
          <img src="media/stickers/happy.gif" class="btn-cat-mini-sticker" id="yesBtnCat" alt="Котик">
          <span id="btnYesText">ДА, ОЧЕНЬ! ❤️</span>
        </button>

        <!-- Dodging NO button -->
        <button class="dodging-btn-no" id="btnNo">
          <span>НЕТ 💔 😜</span>
          <div class="comic-speech-bubble" id="speechBubble">
            <img src="media/stickers/fast.gif" alt="Котик">
            <span id="bubbleText">Ой! Я улетела! 🏃‍♀️💨</span>
          </div>
        </button>
      </div>
    </div>
  </div>

  <!-- ========================================================
       SCREEN 2: CUTE QUIZ DECK
       ======================================================== -->
  <div class="screen" id="screen2">
    <div class="quiz-container-box">
      <div class="quiz-interactive-card">
        <img src="media/stickers/encouragement.gif" class="quiz-cat-cheerleader" id="quizCatMascot" alt="Котик">
        <div class="quiz-top-row">
          <div class="quiz-love-badge">
            <img src="media/stickers/adore.gif" alt="Котик">
            <span>Тест для любимой</span>
          </div>
          <div class="quiz-index-pill" id="quizStepPill">Вопрос 1 из 5</div>
        </div>

        <div class="quiz-question-heading" id="quizQuestionText">Загрузка вопроса...</div>

        <div class="quiz-choices-stack" id="quizOptionsBox">
          <!-- Populated dynamically -->
        </div>

        <div class="quiz-feedback-toast" id="quizFeedbackToast"></div>
      </div>
    </div>
  </div>

  <!-- ========================================================
       SCREEN 3: CELAMUR PORTRAIT & 3D SPIRAL GALAXY
       ======================================================== -->
  <div class="screen" id="screen3" style="padding: 10px 16px 24px 16px; justify-content: space-between;">
    <div class="celamur-stage-viewport" id="celamurViewport">
      <canvas id="galaxyCanvas"></canvas>
    </div>

    <div class="celamur-controls-box">
      <!-- Circular play button -->
      <button class="celamur-play-disc" id="celamurPlayBtn" title="Слушать">
        <svg id="playIconSvg" viewBox="0 0 24 24">
          <polygon points="6,4 19,12 6,20" />
        </svg>
      </button>

      <!-- Signature title & exact subtitles -->
      <div class="celamur-main-title">Злата + Вадим</div>
      <div class="celamur-subtitle-divine">Мы самая красивая пара ✨</div>
      <div class="celamur-subtitle-languages"><span class="celamur-love-highlight">«Я тебя люблю»</span> на всех языках мира 💫</div>
      <div class="celamur-drag-hint-pill" id="celamurHint">✦ покрути нашу галактику ✦</div>

      <!-- Action buttons -->
      <div class="celamur-actions-group">
        <button class="btn-marshmallow-pink" id="btnToggleGalaxy">
          <span id="btnToggleText">Собрать портрет ✨</span>
        </button>
        <button class="btn-marshmallow-glass" id="btnGotoFinale">
          <span>Наше время →</span>
        </button>
      </div>
    </div>
  </div>

  <!-- ========================================================
       SCREEN 4: ANNIVERSARY TIMER & MEMORIES
       ======================================================== -->
  <div class="screen" id="screen4">
    <div class="finale-box">
      <!-- Top navigation with return to galaxy -->
      <div class="finale-top-nav-row">
        <button class="btn-back-galaxy" id="btnBackToGalaxy">
          <span>← Галактика 🌌</span>
        </button>
        <div class="finale-cute-badge">20.05.2026 19:40 🤍</div>
      </div>

      <h1 class="finale-title-text">Полгода вместе</h1>

      <!-- Countdown -->
      <div class="timer-squircle-grid">
        <div class="squircle-card">
          <div class="squircle-val" id="tDays">00</div>
          <div class="squircle-lbl">Дней</div>
        </div>
        <div class="squircle-card">
          <div class="squircle-val" id="tHours">00</div>
          <div class="squircle-lbl">Часов</div>
        </div>
        <div class="squircle-card">
          <div class="squircle-val" id="tMins">00</div>
          <div class="squircle-lbl">Минут</div>
        </div>
        <div class="squircle-card">
          <div class="squircle-val" id="tSecs">00</div>
          <div class="squircle-lbl">Секунд</div>
        </div>
      </div>

      <!-- Verbatim quote requested by user -->
      <div class="letter-romantic-card">
        <img src="media/stickers/cat_love.gif" class="letter-corner-cat" alt="Любовь">
        «Вот мы уже пол года вместе, прошли много сложностей и неудач, но нас ждёт долгий и счастливый путь.»
        <div class="letter-signature-tag">Навсегда твой 🤍</div>
      </div>

      <!-- Button to open memories -->
      <button class="btn-memories-trigger" id="btnOpenMemories">
        <span>Открыть наш альбом воспоминаний 📸</span>
      </button>
    </div>
  </div>

  <!-- ========================================================
       MEMORIES STORY VIEWER (FULLSCREEN INSTAGRAM STORIES STYLE)
       ======================================================== -->
  <div class="story-viewer-modal" id="storyModal">
    <button class="story-close-round-btn" id="btnCloseMemories" title="Закрыть">×</button>

    <div class="story-stage-card">
      <!-- Segmented Stories header bars -->
      <div class="story-segments-header" id="storySegmentsBox"></div>

      <div class="story-viewport-box" id="storyViewport">
        <img src="" class="story-img-element" id="storyImg" alt="Воспоминание">
        <video class="story-video-element" id="storyVideo" controls playsinline style="display:none;"></video>
      </div>

      <div class="story-details-footer">
        <div class="story-date-row">
          <img id="storySticker" class="story-footer-cat-sticker" src="media/stickers/hello.gif" alt="Котик">
          <div class="story-date-badge" id="storyDateBadge">Начало истории</div>
        </div>
        <div class="story-caption-title" id="storyCaption">Загрузка...</div>
        <div class="story-slide-counter" id="storyCounter">1 / 18</div>
        <div class="story-navigation-row">
          <button class="story-nav-btn" id="btnPrevSlide">← Назад</button>
          <button class="story-nav-btn" id="btnNextSlide">Вперёд →</button>
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================================
       JAVASCRIPT GAMEPLAY, AUDIO & MOTION ENGINE
       ======================================================== -->
  <script>
    // Embedded Data
    const CELAMUR_PORTRAIT_B64 = "{celamur_base64}";
    const GALAXY_PARTICLES = {particles_data};
    const MEMORY_FILES = {memory_files_json};

    // Preload next images in background for instant 0ms latency
    const imageCache = {{}};
    function preloadMedia(index) {{
      for (let offset = 1; offset <= 3; offset++) {{
        const targetIdx = (index + offset) % MEMORY_FILES.length;
        const itm = MEMORY_FILES[targetIdx];
        if (!itm.name.toLowerCase().endsWith('.mp4') && !imageCache[itm.name]) {{
          const img = new Image();
          img.src = 'media/' + itm.name;
          imageCache[itm.name] = img;
        }}
      }}
    }}

    // Screen transition logic
    let currentScreen = 1;
    function goToScreen(num) {{
      document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
      const next = document.getElementById('screen' + num);
      if (next) {{
        next.classList.add('active');
        currentScreen = num;

        // Update candy heart progress
        for (let i = 1; i <= 4; i++) {{
          const ch = document.getElementById('ch' + i);
          if (ch) {{
            if (i <= num) {{
              ch.classList.add('glow');
              ch.textContent = '💖';
            }} else {{
              ch.classList.remove('glow');
              ch.textContent = '🤍';
            }}
          }}
        }}

        if (num === 3) {{
          initCelamurCanvas();
        }}
      }}
    }}

    // Return to galaxy from screen 4
    document.getElementById('btnBackToGalaxy').addEventListener('click', () => {{
      goToScreen(3);
    }});

    // Ambient space canvas
    (function initAmbientSky() {{
      const canvas = document.getElementById('ambientSkyCanvas');
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
          const alpha = (Math.sin(s.a) + 1) * 0.45 + 0.1;
          ctx.beginPath();
          ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
          ctx.fillStyle = `rgba(255, 230, 245, ${{alpha}})`;
          ctx.fill();
        }}
        requestAnimationFrame(loop);
      }}
      loop();
    }})();

    // Background Audio Controls
    const bgMusic = document.getElementById('bgMusic');
    const musicToggleBtn = document.getElementById('musicToggleBtn');
    let isPlayingAudio = false;

    function toggleMusic() {{
      if (isPlayingAudio) {{
        bgMusic.pause();
        isPlayingAudio = false;
        musicToggleBtn.classList.remove('playing');
        updatePlayIcons(false);
      }} else {{
        bgMusic.play().then(() => {{
          isPlayingAudio = true;
          musicToggleBtn.classList.add('playing');
          updatePlayIcons(true);
        }}).catch(() => {{}});
      }}
    }}

    function updatePlayIcons(playing) {{
      const icon = document.getElementById('playIconSvg');
      if (icon) {{
        if (playing) {{
          icon.innerHTML = '<rect x="6" y="5" width="4" height="14"/><rect x="14" y="5" width="4" height="14"/>';
        }} else {{
          icon.innerHTML = '<polygon points="6,4 19,12 6,20" />';
        }}
      }}
    }}

    musicToggleBtn.addEventListener('click', toggleMusic);
    document.getElementById('celamurPlayBtn').addEventListener('click', toggleMusic);

    // ========================================================
    // SCREEN 1: THE PLAYFUL FLOW (CLICK YES -> TEASE TO TRY NO -> DODGE -> UNLOCK YES)
    // ========================================================
    const btnNo = document.getElementById('btnNo');
    const btnYes = document.getElementById('btnYes');
    const btnYesText = document.getElementById('btnYesText');
    const teaseAlert = document.getElementById('teaseAlert');
    const teaseAlertText = document.getElementById('teaseAlertText');
    const speechBubble = document.getElementById('speechBubble');
    const bubbleText = document.getElementById('bubbleText');
    const playgroundArea = document.getElementById('playgroundArea');

    let triedYesFirst = false;
    let noDodgeCount = 0;
    let yesUnlocked = false;

    const funnyQuotes = [
      "Ой! Я улетела! 🏃‍♀️💨",
      "Ты правда думала нажать? 😂",
      "Хи-хи, догоняй! 🪂",
      "Эта кнопка тут для красоты! ✨",
      "Ладно, ладно, сдаюсь! Жми ДА! 💖"
    ];

    // When user taps YES first
    btnYes.addEventListener('click', (e) => {{
      if (!yesUnlocked) {{
        // She tapped YES before trying NO!
        triedYesFirst = true;

        // Show cute teasing banner
        teaseAlert.classList.add('show');
        teaseAlertText.textContent = "Эй, так просто не пойдёт! Попробуй сначала нажать «НЕТ» 😜👇";

        // Highlight NO button
        btnNo.classList.add('highlight-wiggle');

        // Bouncy feedback on YES
        btnYes.style.animation = 'none';
        void btnYes.offsetWidth;
        btnYes.style.animation = 'cardShake 0.4s ease';

        spawnBurstParticles(e.clientX || window.innerWidth/2, e.clientY || window.innerHeight/2, 5, ['😜', '🐾', '✨']);
        return;
      }}

      // YES is unlocked! Proceed with massive celebration!
      if (!isPlayingAudio) toggleMusic();

      spawnBurstParticles(e.clientX || window.innerWidth/2, e.clientY || window.innerHeight/2, 30, ['💖', '🤍', '🌸', '✨', '🥰', '💫', '🍓']);

      setTimeout(() => {{
        goToScreen(2);
      }}, 550);
    }});

    // When user touches or hovers over NO
    let lastDodgeTime = 0;
    function handleNoDodge(e) {{
      const now = Date.now();
      if (now - lastDodgeTime < 180) return;
      lastDodgeTime = now;

      noDodgeCount++;

      // Bubble reaction with cat - stays visible until next tap/dodge!
      bubbleText.textContent = funnyQuotes[Math.min(noDodgeCount - 1, funnyQuotes.length - 1)];
      speechBubble.classList.add('active');

      // Spring physics leap
      const rect = playgroundArea.getBoundingClientRect();
      const maxX = rect.width / 2 - 65;
      const maxY = 50;

      const rx = (Math.random() - 0.5) * maxX * 2;
      const ry = (Math.random() - 0.5) * maxY * 2;
      btnNo.style.transform = `translate(${{rx}}px, ${{ry}}px) scale(${{Math.max(0.75, 1 - noDodgeCount * 0.05)}})`;

      // Puff of smoke & sparkles
      spawnBurstParticles(e.clientX || rect.left + rect.width/2, e.clientY || rect.top + 70, 5, ['💨', '✨', '😜', '⭐']);

      // UNLOCK YES BUTTON AFTER SHE TRIES NO!
      if (noDodgeCount >= 2 && !yesUnlocked) {{
        unlockYesButton();
      }}
    }}

    function unlockYesButton() {{
      yesUnlocked = true;
      btnNo.classList.remove('highlight-wiggle');

      btnYes.classList.add('ready-pulse');
      btnYesText.textContent = "ДА, ОЧЕНЬ СИЛЬНО! ❤️✨";

      teaseAlert.classList.add('show');
      teaseAlert.style.background = "linear-gradient(135deg, rgba(46, 213, 115, 0.25) 0%, rgba(46, 213, 115, 0.15) 100%)";
      teaseAlert.style.borderColor = "#2ed573";
      teaseAlert.style.color = "#2ed573";
      teaseAlert.innerHTML = '<img src="media/stickers/happy.gif" class="tease-cat-icon" alt="Кот"> <span>Умничка! Вот теперь нажимай ДА! 🥰</span>';

      spawnBurstParticles(window.innerWidth / 2, btnYes.getBoundingClientRect().top + 25, 18, ['💖', '✨', '🤍', '🌸']);
    }}

    btnNo.addEventListener('mouseenter', handleNoDodge);
    btnNo.addEventListener('touchstart', (e) => {{
      e.preventDefault();
      handleNoDodge(e.touches[0]);
    }});
    btnNo.addEventListener('click', handleNoDodge);

    // Physical particle explosion generator
    function spawnBurstParticles(x, y, count, symbols) {{
      for (let i = 0; i < count; i++) {{
        const el = document.createElement('div');
        el.className = 'burst-heart-item';
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
          vy += 0.25;
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
    // SCREEN 2: CUTE QUIZ DECK
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
      document.getElementById('quizStepPill').textContent = `Вопрос ${{currentQ + 1}} из ${{quizQuestions.length}}`;
      document.getElementById('quizQuestionText').textContent = q.q;
      document.getElementById('quizFeedbackToast').innerHTML = "";

      const mascot = document.getElementById('quizCatMascot');
      if (mascot) mascot.src = (currentQ % 2 === 0 ? 'media/stickers/encouragement.gif' : 'media/stickers/wink.gif');

      const box = document.getElementById('quizOptionsBox');
      box.innerHTML = '';
      q.opts.forEach((optText, idx) => {{
        const btn = document.createElement('button');
        btn.className = 'quiz-pill-choice';
        btn.innerHTML = `<span>${{optText}}</span>`;
        btn.addEventListener('click', () => handleQuizPick(idx, btn));
        box.appendChild(btn);
      }});
    }}

    function handleQuizPick(idx, btn) {{
      const q = quizQuestions[currentQ];
      const mascot = document.getElementById('quizCatMascot');
      if (idx === q.ans) {{
        btn.classList.add('correct');
        if (mascot) mascot.src = 'media/stickers/happy.gif';
        const rect = btn.getBoundingClientRect();
        spawnBurstParticles(rect.left + rect.width/2, rect.top + rect.height/2, 12, ['✨', '💖', '🥰', '🌸']);
        document.getElementById('quizFeedbackToast').innerHTML = '<img src="media/stickers/happy.gif" alt="Кот"> <span>В точку! Ты знаешь меня идеально 🥰</span>';

        setTimeout(() => {{
          currentQ++;
          if (currentQ < quizQuestions.length) {{
            renderQuiz();
          }} else {{
            if (mascot) mascot.src = 'media/stickers/dancing.gif';
            document.getElementById('quizFeedbackToast').innerHTML = '<img src="media/stickers/dancing.gif" alt="Кот"> <span>100% совпадение! А теперь смотри... 💫</span>';
            setTimeout(() => goToScreen(3), 900);
          }}
        }}, 650);
      }} else {{
        btn.classList.add('wrong');
        if (mascot) mascot.src = 'media/stickers/giggle.gif';
        document.getElementById('quizFeedbackToast').innerHTML = '<img src="media/stickers/giggle.gif" alt="Кот"> <span>Не-а, мимо! Подумай ещё разок 😉</span>';
        setTimeout(() => {{
          btn.classList.remove('wrong');
          if (mascot) mascot.src = 'media/stickers/teasing.gif';
        }}, 600);
      }}
    }}
    renderQuiz();

    // ========================================================
    // SCREEN 3: CELAMUR PORTRAIT & 3D SPIRAL GALAXY
    // STARTS IN DISPERSED 3D GALAXY MODE FIRST!
    // ========================================================
    let canvas, ctx;
    let portraitImg = new Image();
    portraitImg.src = CELAMUR_PORTRAIT_B64;

    // STARTS IN DISPERSED GALAXY MODE!
    let isGalaxyMode = true;
    let morphProgress = 0.0;
    let targetMorph = 0.0;

    let rotY = 0.8;
    let rotX = 66 * Math.PI / 180;
    let velRotY = 0.003;
    let velRotX = 0;
    let isDragging = false;
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

      // Dragging is 100% dedicated to FREE 3D ROTATION without accidental morphing!
      canvas.addEventListener('mousedown', (e) => {{
        isDragging = true;
        lastX = e.clientX;
        lastY = e.clientY;
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
      window.addEventListener('mouseup', () => {{
        isDragging = false;
      }});

      // Touch drag
      canvas.addEventListener('touchstart', (e) => {{
        isDragging = true;
        lastX = e.touches[0].clientX;
        lastY = e.touches[0].clientY;
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
      canvas.addEventListener('touchend', () => {{
        isDragging = false;
      }});

      requestAnimationFrame(renderCelamur);
    }}

    // Morphing happens PURELY BY BUTTON for 100% control & comfort!
    function toggleGalaxy() {{
      isGalaxyMode = !isGalaxyMode;
      targetMorph = isGalaxyMode ? 0.0 : 1.0;

      const btnText = document.getElementById('btnToggleText');
      const hint = document.getElementById('celamurHint');
      if (isGalaxyMode) {{
        btnText.textContent = "Собрать портрет ✨";
        hint.textContent = "✦ покрути нашу галактику ✦";
        spawnBurstParticles(window.innerWidth/2, window.innerHeight/2, 15, ['🌌', '✨', '💫']);
      }} else {{
        btnText.textContent = "Рассыпать в звёзды 🌌";
        hint.textContent = "✦ нажми кнопку, чтобы снова стать звёздами ✦";
        spawnBurstParticles(window.innerWidth/2, window.innerHeight/2, 15, ['🤍', '✨', '💖']);
      }}
    }}

    document.getElementById('btnToggleGalaxy').addEventListener('click', toggleGalaxy);
    document.getElementById('btnGotoFinale').addEventListener('click', () => goToScreen(4));

    function renderCelamur() {{
      if (currentScreen === 3) {{
        morphProgress += (targetMorph - morphProgress) * 0.08;

        if (!isDragging) {{
          velRotY *= 0.96;
          rotY += 0.004 + velRotY;
          velRotX *= 0.92;
          rotX = Math.max(0.35, Math.min(1.45, rotX + velRotX));
        }}

        drawCelamurScene();
      }}
      requestAnimationFrame(renderCelamur);
    }}

    function drawCelamurScene() {{
      const W = canvasWidth;
      const H = canvasHeight;
      const cx = W / 2;
      const cy = H / 2 - 15;

      ctx.clearRect(0, 0, W, H);

      // 1. Center Nebula Glow
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
          ctx.font = `${{fontSize}}px var(--font-rounded)`;
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
    // MEMORIES STORY VIEWER (FULLSCREEN INSTAGRAM STORIES STYLE)
    // ========================================================
    let currentSlide = 0;
    const storyModal = document.getElementById('storyModal');
    const storyImg = document.getElementById('storyImg');
    const storyVideo = document.getElementById('storyVideo');
    const storyCaption = document.getElementById('storyCaption');
    const storyDateBadge = document.getElementById('storyDateBadge');
    const storyCounter = document.getElementById('storyCounter');
    const storySegmentsBox = document.getElementById('storySegmentsBox');

    // Create segment bars
    for (let i = 0; i < MEMORY_FILES.length; i++) {{
      const bar = document.createElement('div');
      bar.className = 'story-segment-bar';
      bar.id = 'segBar' + i;
      storySegmentsBox.appendChild(bar);
    }}

    function openMemories() {{
      storyModal.classList.add('active');
      showSlide(0);
      preloadMedia(0);
    }}

    function closeMemories() {{
      storyModal.classList.remove('active');
      storyVideo.pause();
    }}

    function showSlide(idx) {{
      if (idx < 0) idx = MEMORY_FILES.length - 1;
      if (idx >= MEMORY_FILES.length) idx = 0;
      currentSlide = idx;

      // Update segment bars
      for (let i = 0; i < MEMORY_FILES.length; i++) {{
        const b = document.getElementById('segBar' + i);
        if (b) {{
          if (i <= idx) b.classList.add('viewed');
          else b.classList.remove('viewed');
        }}
      }}

      const item = MEMORY_FILES[idx];
      storyDateBadge.textContent = item.date || "Наше мгновение";
      storyCaption.textContent = item.caption;
      storyCounter.textContent = `${{idx + 1}} / ${{MEMORY_FILES.length}}`;

      const stickerImg = document.getElementById('storySticker');
      if (stickerImg && item.sticker) {{
        stickerImg.src = 'media/stickers/' + item.sticker;
        stickerImg.style.animation = 'none';
        void stickerImg.offsetWidth;
        stickerImg.style.animation = 'cuteStickerPop 0.35s cubic-bezier(0.34, 1.56, 0.64, 1)';
      }}

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

      // Preload next items
      preloadMedia(idx);
    }}

    document.getElementById('btnOpenMemories').addEventListener('click', openMemories);
    document.getElementById('btnCloseMemories').addEventListener('click', closeMemories);
    document.getElementById('btnPrevSlide').addEventListener('click', () => showSlide(currentSlide - 1));
    document.getElementById('btnNextSlide').addEventListener('click', () => showSlide(currentSlide + 1));

    window.addEventListener('keydown', (e) => {{
      if (!storyModal.classList.contains('active')) return;
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

print('SUCCESS! d:/подарки пол года/index.html rewritten with all requested features!')
print(f'File size: {os.path.getsize("d:/подарки пол года/index.html")} bytes')
