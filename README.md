<!doctype html>
<html lang="id" data-theme="dark">
  <head>
    <meta charset="utf-8">
    <!-- PENTING UNTUK IPHONE: viewport-fit=cover disandingkan dengan disable zoom agar terasa seperti aplikasi asli -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    
    <title>KALUNG Studio — Diagram Terjemahan</title>
  
    <!-- PWA & IOS OPTIMIZATION -->
    <!-- Mengizinkan aplikasi dibuka Full-Screen tanpa address bar Safari saat di Add to Home Screen -->
    <meta name="apple-mobile-web-app-capable" content="yes">
    <!-- Mengatur warna status bar iPhone (jam, baterai, dll). Pilihan: default, black, atau black-translucent -->
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <!-- Nama singkat aplikasi saat muncul di Layar Utama -->
    <meta name="apple-mobile-web-app-title" content="KALUNG Studio">
    <!-- Mengatur warna tema browser mobile (Android Chrome & iOS Safari) -->
    <meta name="theme-color" content="#0f172a">
  
    <!-- FONTS -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@500&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  </head>

<style>
:root {
  --bg-app: #080c14;
  --bg-surface: #101726;
  --bg-surface-elevated: #182238;
  --border: #23334d;
  --text-main: #f1f5f9;
  --text-muted: #8493a8;
  --primary: #38bdf8;
  --primary-glow: rgba(56, 189, 248, 0.25);
  --reg-low: #f43f5e;
  --reg-mid: #38bdf8;
  --reg-high: #34d399;
  --reg-high2: #fbbf24;
  --radius-sm: 8px;
}

[data-theme="light"] {
  --bg-app: #f1f5f9;
  --bg-surface: #ffffff;
  --bg-surface-elevated: #f8fafc;
  --border: #cbd5e1;
  --text-main: #0f172a;
  --text-muted: #64748b;
  --primary: #0284c7;
  --primary-glow: rgba(2, 132, 199, 0.15);
}

* { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }
body {
  font-family: 'Plus Jakarta Sans', sans-serif;
  background-color: var(--bg-app);
  color: var(--text-main);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  overflow-x: hidden;
  user-select: none;
}

.app-header {
  height: 64px;
  padding: 0 24px;
  border-bottom: 1px solid var(--border);
  background: var(--bg-surface);
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: sticky;
  top: 0;
  z-index: 100;
}
.brand { display: flex; align-items: center; gap: 12px; }
.brand-icon {
  width: 36px; height: 36px;
  border-radius: var(--radius-sm);
  background: linear-gradient(135deg, var(--primary), #6366f1);
  display: grid; place-items: center;
  color: #fff; font-weight: 700; font-size: 1.1rem;
}
.brand-title { font-weight: 700; font-size: 1.1rem; letter-spacing: -0.02em; }
.brand-subtitle { font-size: 0.72rem; color: var(--text-muted); font-weight: 500; }

.header-actions { display: flex; gap: 8px; }
.icon-btn {
  width: 38px; height: 38px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border);
  background: var(--bg-surface-elevated);
  color: var(--text-main);
  cursor: pointer;
  display: grid; place-items: center;
  transition: all 0.2s;
}

.studio-container {
  display: grid;
  grid-template-columns: 300px 1fr;
  flex: 1;
  min-height: calc(100vh - 64px);
}

.control-panel {
  background: var(--bg-surface);
  border-right: 1px solid var(--border);
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.panel-section-title {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-muted);
  font-weight: 700;
  margin-bottom: 8px;
}
.form-group { display: flex; flex-direction: column; gap: 6px; }
.form-group label { font-size: 0.82rem; font-weight: 600; color: var(--text-main); }

.select-custom {
  width: 100%;
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border);
  color: var(--text-main);
  border-radius: var(--radius-sm);
  padding: 10px 12px;
  outline: none;
  font-weight: 600;
}

.inline-do-select {
  width: 100%;
  height: 100%;
  background: #ef4444;
  color: #ffffff;
  border: 2px solid #ffffff;
  border-radius: 8px;
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-weight: 700;
  font-size: 14px;
  text-align: center;
  outline: none;
  cursor: pointer;
  box-shadow: 0 0 12px rgba(239, 68, 68, 0.5);
  padding: 0 4px;
}
.inline-do-select option {
  background: var(--bg-surface);
  color: var(--text-main);
}

.preset-chips { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 4px; }
.chip-btn {
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border);
  color: var(--text-muted);
  padding: 6px 10px;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 500;
  cursor: pointer;
}
.chip-btn:hover, .chip-btn.active { color: var(--primary); border-color: var(--primary); background: var(--primary-glow); }

.stage-panel {
  padding: 16px 24px 24px 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  background: radial-gradient(circle at center, var(--bg-surface-elevated) 0%, var(--bg-app) 100%);
  position: relative;
}

/* Area Diagram Diperbesar */
.radial-canvas-container {
  width: 100%;
  max-width: 720px;
  aspect-ratio: 1 / 1;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  touch-action: none;
}

#radialSvg {
  width: 100%;
  height: 100%;
  overflow: visible;
  touch-action: none;
}

.ring-interactive {
  cursor: grab;
  touch-action: none;
}
.ring-interactive:active {
  cursor: grabbing;
}

.ring-guide-bg { 
  fill: none; 
  stroke: rgba(255, 255, 255, 0.001);
  stroke-width: 44; 
  pointer-events: stroke;
}

.ring-guide-line { fill: none; stroke: var(--border); stroke-dasharray: 4 4; stroke-width: 1.2; pointer-events: none; }

.do-trigger-line {
  stroke: #ef4444;
  stroke-width: 2.5;
  stroke-dasharray: 6 3;
  pointer-events: none;
}

/* Tipografi Identitas Ring Diperhalus */
.grid-identity-label {
  font-family: 'Fira Code', monospace;
  font-size: 11px;
  font-weight: 500;
  fill: var(--text-muted);
  text-anchor: middle;
  dominant-baseline: central;
  pointer-events: none;
}

.translation-overlay-group {
  pointer-events: none;
}

/* Tipografi Hasil Terjemahan Diperjelas & Font Weight Ditiadakan Yang Terlalu Tebal */
.translated-text {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 20px;
  font-weight: 600;
  text-anchor: middle;
  dominant-baseline: central;
}

.legend-bar {
  display: flex;
  gap: 16px;
  background: var(--bg-surface);
  padding: 8px 18px;
  border-radius: 99px;
  border: 1px solid var(--border);
  font-size: 0.75rem;
  font-weight: 500;
  flex-wrap: wrap;
  justify-content: center;
}
.legend-item { display: flex; align-items: center; gap: 6px; }
.legend-color { width: 10px; height: 10px; border-radius: 50%; }

.toast {
  position: fixed;
  bottom: 20px; right: 20px;
  background: var(--primary);
  color: #fff;
  padding: 10px 18px;
  border-radius: var(--radius-sm);
  font-weight: 600;
  font-size: 0.82rem;
  opacity: 0;
  transition: all 0.3s;
}
.toast.show { opacity: 1; }

@media (max-width: 860px) {
  .studio-container { grid-template-columns: 1fr; }
  .control-panel { border-right: none; border-bottom: 1px solid var(--border); }
  .stage-panel { padding: 12px; }
}
</style>
</head>
<body>

<header class="app-header">
  <div class="brand">
    <div class="brand-icon">K</div>
    <div>
      <div class="brand-title">KALUNG Studio</div>
      <div class="brand-subtitle">Diagram Terjemahan Oktaf Ring</div>
    </div>
  </div>
  <div class="header-actions">
    <button class="icon-btn" id="themeToggle" title="Ganti Tema">◐</button>
  </div>
</header>

<div class="studio-container">
  <aside class="control-panel">
    <div class="form-group">
      <label for="doSelect">Pilih Nada Dasar (do)</label>
      <select id="doSelect" class="select-custom"></select>
      <div class="preset-chips" id="doChips"></div>
    </div>

    <div style="margin-top:20px;">
      <div class="panel-section-title">Aksi Cepat</div>
      <button class="chip-btn" id="btnAlignC" style="width:100%; padding: 10px; margin-bottom: 8px; font-weight:600;">
        Posisikan Nada C (6, 18, 30) di Garis Merah
      </button>
      <button class="chip-btn" id="btnResetAll" style="width:100%; padding: 8px;">Reset Posisi Ring</button>
    </div>
  </aside>

  <main class="stage-panel">
    <!-- Banner kontrol dihapus agar fokus ke diagram -->

    <div class="radial-canvas-container">
      <svg id="radialSvg" viewBox="-260 -310 520 580">
        <defs>
          <filter id="neonGlow" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="2.5" result="coloredBlur"/>
            <feMerge>
              <feMergeNode in="coloredBlur"/>
              <feMergeNode in="SourceGraphic"/>
            </feMerge>
          </filter>
        </defs>

        <g id="bgSpokesGroup"></g>

        <g id="ringGroup_rendah" class="ring-interactive" data-ring="rendah"></g>
        <g id="ringGroup_tengah" class="ring-interactive" data-ring="tengah"></g>
        <g id="ringGroup_tinggi" class="ring-interactive" data-ring="tinggi"></g>
        <g id="ringGroup_tinggi2" class="ring-interactive" data-ring="tinggi 2 oktaf"></g>

        <g id="fixedTriggerGroup">
          <line x1="0" y1="0" x2="0" y2="-215" class="do-trigger-line" />
          <polygon points="-7,-210 7,-210 0,-223" fill="#ef4444" />
          
          <foreignObject x="-45" y="-295" width="90" height="38">
            <select id="inlineDoSelect" class="inline-do-select" title="Pilih Nada Dasar"></select>
          </foreignObject>
        </g>

        <g id="translationOverlayGroup" class="translation-overlay-group"></g>
      </svg>
    </div>

    <div class="legend-bar">
      <div class="legend-item"><div class="legend-color" style="background:var(--reg-low)"></div>Ring 1: Bass</div>
      <div class="legend-item"><div class="legend-color" style="background:var(--reg-mid)"></div>Ring 2: Tengah</div>
      <div class="legend-item"><div class="legend-color" style="background:var(--reg-high)"></div>Ring 3: Tinggi</div>
      <div class="legend-item"><div class="legend-color" style="background:var(--reg-high2)"></div>Ring 4: Tinggi 2 Oktaf</div>
    </div>
  </main>
</div>

<div class="toast" id="toast"></div>

<script>
const ABSOLUTE_NOTES = ['C','Cis','D','Dis','E','F','Fis','G','Gis','A','Ais','B'];
const SOLFEGE_CHROMATIC = ['do','di','re','ri','mi','fa','fi','sol','sel','la','sa','ti'];
const BASS_KEYS = ['c','cis','d','dis','e','f','fis','g','gis','a','ais','b'];

const SOLFEGE_COLORS = {
  'do':  '#f43f5e', 'di':  '#fb923c', 're':  '#facc15', 'ri':  '#a3e635',
  'mi':  '#34d399', 'fa':  '#2dd4bf', 'fi':  '#38bdf8', 'sol': '#6366f1',
  'sel': '#8b5cf6', 'la':  '#d946ef', 'sa':  '#ec4899', 'ti':  '#f43f5e'
};

const noteToIndex = Object.fromEntries(ABSOLUTE_NOTES.map((n,i)=>[n,i]));
const mod = (n,m) => ((n%m)+m)%m;

function cipher(s) {
  return ({
    do:['1',''],   di:['1','/'],  re:['2',''],   ri:['2','/'],
    mi:['3',''],   fa:['4',''],   fi:['4','/'],  sol:['5',''],
    sel:['5','/'], la:['6',''],   sa:['7','\\'], ti:['7','']
  }[s] || ['-','']);
}

function getAbsoluteNoteFromIdentity(ringKey, idxInRing) {
  if (ringKey === 'rendah') return ABSOLUTE_NOTES[idxInRing];
  return ABSOLUTE_NOTES[mod(idxInRing + 6, 12)];
}

function getIdentityText(ringKey, idxInRing) {
  if (ringKey === 'rendah') return BASS_KEYS[idxInRing];
  if (ringKey === 'tengah') return String(idxInRing);
  if (ringKey === 'tinggi') return String(idxInRing + 12);
  return String(idxInRing + 24);
}

function getOctaveDots(ringKey) {
  if (ringKey === 'rendah') return { dots: 1, position: 'bottom' };
  if (ringKey === 'tengah') return { dots: 0, position: 'none' };
  if (ringKey === 'tinggi') return { dots: 1, position: 'top' };
  if (ringKey === 'tinggi 2 oktaf') return { dots: 2, position: 'top' };
  return { dots: 0, position: 'none' };
}

const $ = id => document.getElementById(id);
const doSelect = $('doSelect');
const inlineDoSelect = $('inlineDoSelect');
const radialSvg = $('radialSvg');

const RING_RADII = {
  'rendah': 65,
  'tengah': 110,
  'tinggi': 155,
  'tinggi 2 oktaf': 200
};

const ringAngles = {
  'rendah': 0,
  'tengah': 0,
  'tinggi': 0,
  'tinggi 2 oktaf': 0
};

let activeDraggingRing = null;
let dragStartAngle = 0;
let dragBaseAngle = 0;

function initStaticSpokes() {
  const bgSpokesGroup = $('bgSpokesGroup');
  bgSpokesGroup.innerHTML = '';

  ABSOLUTE_NOTES.forEach((_, index) => {
    const angle = (index * 30 - 90) * (Math.PI / 180);
    const xEnd = Math.cos(angle) * 225;
    const yEnd = Math.sin(angle) * 225;

    const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
    line.setAttribute("x1", 0); line.setAttribute("y1", 0);
    line.setAttribute("x2", xEnd); line.setAttribute("y2", yEnd);
    line.setAttribute("stroke", "var(--border)");
    line.setAttribute("stroke-width", "1");
    line.setAttribute("opacity", "0.25");
    bgSpokesGroup.appendChild(line);
  });
}

function buildRings() {
  Object.keys(RING_RADII).forEach(ringKey => {
    const groupKey = ringKey === 'tinggi 2 oktaf' ? 'tinggi2' : ringKey;
    const group = $(`ringGroup_${groupKey}`);
    group.innerHTML = '';
    const radius = RING_RADII[ringKey];

    const touchBg = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    touchBg.setAttribute("r", radius);
    touchBg.setAttribute("class", "ring-guide-bg");
    group.appendChild(touchBg);

    const lineGuide = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    lineGuide.setAttribute("r", radius);
    lineGuide.setAttribute("class", "ring-guide-line");
    group.appendChild(lineGuide);

    for (let i = 0; i < 12; i++) {
      const identityStr = getIdentityText(ringKey, i);

      const gLabel = document.createElementNS("http://www.w3.org/2000/svg", "g");
      gLabel.setAttribute("class", "identity-node-wrapper");
      gLabel.setAttribute("data-slot-idx", i);

      const circleBg = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      circleBg.setAttribute("class", "node-circle-bg");
      circleBg.setAttribute("r", 12);
      circleBg.setAttribute("fill", "var(--bg-surface)");
      circleBg.setAttribute("stroke", "var(--border)");
      circleBg.setAttribute("stroke-width", "1");
      circleBg.setAttribute("style", "pointer-events: none;");

      const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
      text.setAttribute("class", "grid-identity-label");
      text.textContent = identityStr;

      gLabel.appendChild(circleBg);
      gLabel.appendChild(text);
      group.appendChild(gLabel);
    }
  });
}

function updateVisuals() {
  const currentDo = doSelect.value;
  const currentDoIdx = noteToIndex[currentDo];
  const overlayGroup = $('translationOverlayGroup');
  overlayGroup.innerHTML = '';

  Object.keys(RING_RADII).forEach(ringKey => {
    const groupKey = ringKey === 'tinggi 2 oktaf' ? 'tinggi2' : ringKey;
    const group = $(`ringGroup_${groupKey}`);
    const rAngle = ringAngles[ringKey];
    const radius = RING_RADII[ringKey];

    group.setAttribute("transform", `rotate(${rAngle})`);

    const wrappers = group.querySelectorAll('.identity-node-wrapper');
    wrappers.forEach(wrapper => {
      const i = Number(wrapper.dataset.slotIdx);
      const baseAngleDeg = (i * 30 - 90);
      const rad = baseAngleDeg * (Math.PI / 180);

      const x = Math.cos(rad) * radius;
      const y = Math.sin(rad) * radius;

      wrapper.setAttribute("transform", `translate(${x}, ${y}) rotate(${- (baseAngleDeg + rAngle + 90)})`);

      const currentPosDeg = mod(baseAngleDeg + rAngle, 360);
      const diff = Math.abs(mod(currentPosDeg - 270 + 180, 360) - 180);

      if (diff < 2) {
        const absNote = getAbsoluteNoteFromIdentity(ringKey, i);
        const absNoteIdx = noteToIndex[absNote];

        const solfegeIdx = mod(absNoteIdx - currentDoIdx, 12);
        const solfegeStr = SOLFEGE_CHROMATIC[solfegeIdx];
        const [cNum, cMark] = cipher(solfegeStr);
        const color = SOLFEGE_COLORS[solfegeStr] || '#38bdf8';

        const offsetRadius = radius + 22; 
        const overlayX = 0;
        const overlayY = -offsetRadius;

        const gOverlay = document.createElementNS("http://www.w3.org/2000/svg", "g");

        // Badge hasil terjemahan yang lebih bersih & jelas
        const badgeBg = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        badgeBg.setAttribute("cx", overlayX);
        badgeBg.setAttribute("cy", overlayY);
        badgeBg.setAttribute("r", 18);
        badgeBg.setAttribute("fill", "var(--bg-app)");
        badgeBg.setAttribute("stroke", color);
        badgeBg.setAttribute("stroke-width", "2");
        badgeBg.setAttribute("filter", "url(#neonGlow)");
        gOverlay.appendChild(badgeBg);

        const badgeText = document.createElementNS("http://www.w3.org/2000/svg", "text");
        badgeText.setAttribute("x", overlayX);
        badgeText.setAttribute("y", overlayY + 1);
        badgeText.setAttribute("class", "translated-text");
        badgeText.setAttribute("fill", color);
        badgeText.textContent = cNum;
        gOverlay.appendChild(badgeText);

        // Garis Mol/Crest yang lebih proporsional
        if (cMark === '/') {
          const slashLine = document.createElementNS("http://www.w3.org/2000/svg", "line");
          slashLine.setAttribute("x1", overlayX - 5);
          slashLine.setAttribute("y1", overlayY + 8);
          slashLine.setAttribute("x2", overlayX + 5);
          slashLine.setAttribute("y2", overlayY - 8);
          slashLine.setAttribute("stroke", color);
          slashLine.setAttribute("stroke-width", "2");
          slashLine.setAttribute("stroke-linecap", "round");
          gOverlay.appendChild(slashLine);
        } else if (cMark === '\\') {
          const backslashLine = document.createElementNS("http://www.w3.org/2000/svg", "line");
          backslashLine.setAttribute("x1", overlayX - 5);
          backslashLine.setAttribute("y1", overlayY - 8);
          backslashLine.setAttribute("x2", overlayX + 5);
          backslashLine.setAttribute("y2", overlayY + 8);
          backslashLine.setAttribute("stroke", color);
          backslashLine.setAttribute("stroke-width", "2");
          backslashLine.setAttribute("stroke-linecap", "round");
          gOverlay.appendChild(backslashLine);
        }

        // Titik Oktaf
        const octInfo = getOctaveDots(ringKey);
        if (octInfo.dots > 0) {
          const dotRadius = 2;
          const dotSpacing = 5;
          
          if (octInfo.position === 'top') {
            const targetY = overlayY - 12;
            if (octInfo.dots === 1) {
              const dot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
              dot.setAttribute("cx", overlayX);
              dot.setAttribute("cy", targetY);
              dot.setAttribute("r", dotRadius);
              dot.setAttribute("fill", color);
              gOverlay.appendChild(dot);
            } else if (octInfo.dots === 2) {
              [-dotSpacing/2, dotSpacing/2].forEach(xOffset => {
                const dot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
                dot.setAttribute("cx", overlayX + xOffset);
                dot.setAttribute("cy", targetY);
                dot.setAttribute("r", dotRadius);
                dot.setAttribute("fill", color);
                gOverlay.appendChild(dot);
              });
            }
          } else if (octInfo.position === 'bottom') {
            const targetY = overlayY + 12;
            const dot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
            dot.setAttribute("cx", overlayX);
            dot.setAttribute("cy", targetY);
            dot.setAttribute("r", dotRadius);
            dot.setAttribute("fill", color);
            gOverlay.appendChild(dot);
          }
        }

        overlayGroup.appendChild(gOverlay);
      }
    });
  });
}

function getSVGPoint(e) {
  const pt = radialSvg.createSVGPoint();
  pt.x = e.clientX || (e.touches && e.touches[0].clientX) || 0;
  pt.y = e.clientY || (e.touches && e.touches[0].clientY) || 0;
  return pt.matrixTransform(radialSvg.getScreenCTM().inverse());
}

function getAngleFromSVGPoint(svgPt) {
  return Math.atan2(svgPt.y, svgPt.x) * (180 / Math.PI);
}

function getDistanceFromSVGPoint(svgPt) {
  return Math.sqrt(svgPt.x * svgPt.x + svgPt.y * svgPt.y);
}

function detectRingFromRadius(dist) {
  if (dist >= 40 && dist < 87) return 'rendah';
  if (dist >= 87 && dist < 132) return 'tengah';
  if (dist >= 132 && dist < 177) return 'tinggi';
  if (dist >= 177 && dist < 230) return 'tinggi 2 oktaf';
  return null;
}

radialSvg.addEventListener('pointerdown', (e) => {
  if (e.target.closest('foreignObject')) return;

  const svgPt = getSVGPoint(e);
  const dist = getDistanceFromSVGPoint(svgPt);
  const ring = detectRingFromRadius(dist);
  
  if (!ring) return;

  activeDraggingRing = ring;
  dragStartAngle = getAngleFromSVGPoint(svgPt);
  dragBaseAngle = ringAngles[ring];
  
  try {
    radialSvg.setPointerCapture(e.pointerId);
  } catch(err) {}
});

radialSvg.addEventListener('pointermove', (e) => {
  if (!activeDraggingRing) return;
  const svgPt = getSVGPoint(e);
  const angleNow = getAngleFromSVGPoint(svgPt);
  const delta = angleNow - dragStartAngle;
  ringAngles[activeDraggingRing] = dragBaseAngle + delta;
  updateVisuals();
});

const handlePointerEnd = (e) => {
  if (!activeDraggingRing) return;
  
  const rawAngle = ringAngles[activeDraggingRing];
  ringAngles[activeDraggingRing] = Math.round(rawAngle / 30) * 30;
  
  activeDraggingRing = null;
  try {
    radialSvg.releasePointerCapture(e.pointerId);
  } catch(err) {}
  updateVisuals();
};

radialSvg.addEventListener('pointerup', handlePointerEnd);
radialSvg.addEventListener('pointercancel', handlePointerEnd);

function alignNoteC() {
  ringAngles['rendah'] = 0;
  ringAngles['tengah'] = -180;
  ringAngles['tinggi'] = -180;
  ringAngles['tinggi 2 oktaf'] = -180;
  updateVisuals();
  showToast("Angklung C diposisikan di Garis Merah");
}

function resetAll() {
  Object.keys(ringAngles).forEach(k => ringAngles[k] = 0);
  updateVisuals();
  showToast("Posisi ring di-reset");
}

function showToast(msg) {
  const toast = $('toast');
  toast.textContent = msg;
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 2000);
}

function setDoValue(val) {
  doSelect.value = val;
  inlineDoSelect.value = val;
  document.querySelectorAll('[data-do]').forEach(x => {
    x.classList.toggle('active', x.dataset.do === val);
  });
  updateVisuals();
}

function init() {
  const optionsHtml = ABSOLUTE_NOTES.map(x => `<option value="${x}">${x}</option>`).join('');
  doSelect.innerHTML = optionsHtml;
  inlineDoSelect.innerHTML = optionsHtml;

  doSelect.value = 'C';
  inlineDoSelect.value = 'C';

  $('doChips').innerHTML = ['C','G','D','F','Ais'].map(x => `<button class="chip-btn ${x==='C'?'active':''}" data-do="${x}">${x}</button>`).join('');
  
  document.querySelectorAll('[data-do]').forEach(b => b.onclick = () => { 
    setDoValue(b.dataset.do);
  });

  doSelect.onchange = (e) => setDoValue(e.target.value);
  inlineDoSelect.onchange = (e) => setDoValue(e.target.value);

  $('btnAlignC').onclick = alignNoteC;
  $('btnResetAll').onclick = resetAll;

  $('themeToggle').onclick = () => {
    const current = document.documentElement.getAttribute('data-theme');
    document.documentElement.setAttribute('data-theme', current === 'dark' ? 'light' : 'dark');
  };

  initStaticSpokes();
  buildRings();
  alignNoteC();
}

init();
</script>
</body>
</html>
