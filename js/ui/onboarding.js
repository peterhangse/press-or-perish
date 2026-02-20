/**
 * ONBOARDING SCREEN — Degree → Flashy jobs → Rejections → Småstad → Boss → PRESS OR PERISH
 */

import * as ScreenManager from './screen-manager.js';
import * as SFX from '../engine/sfx-engine.js';

// Onboarding sequence steps
const SEQUENCE = [
  // Journalism degree
  {
    type: 'diploma',
    header: 'STOCKHOLM UNIVERSITY',
    body: 'This certifies that the bearer has completed the requirements for a Bachelor of Arts in Journalism & Media Studies.',
    detail: 'Class of 1974 · Magna Cum Laude',
    footer: 'The world awaits.',
  },
  // Flashy job ads (clickable feel)
  {
    type: 'job-ad',
    header: 'DAGENS NYHETER',
    tagline: 'Sweden\'s Largest Morning Paper · Est. 1864',
    body: 'WANTED: Investigative Reporter. Join our award-winning newsroom in the heart of Stockholm. Competitive salary, international assignments, press pass to Parliament.',
    salary: '80,000 kr/month + benefits',
    style: 'prestigious',
  },
  {
    type: 'rejection',
    header: 'Dagens Nyheter',
    body: 'Thank you for your interest. Unfortunately, we are not currently hiring junior reporters. We wish you the best in your future career.',
    sender: '— Margareta Svensson, HR Director',
  },
  {
    type: 'job-ad',
    header: 'EXPRESSEN',
    tagline: 'Breaking News. Breaking Ground.',
    body: 'REPORTER POSITION: Fast-paced environment. Must thrive under pressure. Minimum 5 years experience in daily news.',
    salary: '60,000 kr/month',
    style: 'prestigious',
  },
  {
    type: 'rejection',
    header: 'Expressen',
    body: 'No.',
    sender: '— Editor-in-Chief Bo Strömberg',
  },
  {
    type: 'job-ad',
    header: 'GÖTEBORGS-POSTEN',
    tagline: 'The West Coast\'s Leading Paper',
    body: 'JUNIOR REPORTER: Human interest and culture beat. University degree required. Portfolio of published work essential.',
    salary: '45,000 kr/month',
    style: 'prestigious',
  },
  {
    type: 'rejection',
    header: 'Göteborgs-Posten',
    body: 'We appreciate your application but have chosen to proceed with candidates who have professional experience. Competition was fierce — 340 applicants for one position.',
    sender: '— The Editorial Board',
  },
  // The shitty opening
  {
    type: 'job-ad',
    header: 'Småstads Tidning',
    tagline: '',
    body: 'Reporter needed. Immediate start. No experience required. The pay is modest. Present yourself Monday morning.',
    salary: '21,500 kr/month',
    style: 'shabby',
  },
  // Acceptance
  {
    type: 'acceptance',
    header: 'Småstads Tidning',
    body: 'You got the job. Nobody else applied.',
    sender: '— Gunnar Ek, Editor-in-Chief',
  },
  // Boss meeting — starts warm
  {
    type: 'boss',
    name: 'Gunnar Ek',
    speech: 'Welcome, {name}! It\'s good to have someone young on the team. I\'m Gunnar. Sit down, make yourself comfortable.',
    mood: 'warm',
  },
  // The twist
  {
    type: 'boss',
    name: 'Gunnar Ek',
    speech: 'I\'ll be honest with you, {name}. We\'re dying. Regionbladet is eating our lunch every single day. Subscribers are leaving. Advertisers are leaving. This paper has maybe... weeks.',
    mood: 'serious',
  },
  // The ultimatum
  {
    type: 'boss',
    name: 'Gunnar Ek',
    speech: 'Management already told me to let you go before you even start, {name}. But I convinced them to give you one week. FIVE DAYS. If you can\'t outperform the competition by then... there\'s no job. Not for you. Not for me. Not for anyone here.',
    mood: 'intense',
  },
  // Title card
  {
    type: 'title-card',
    title: 'PRESS OR PERISH',
  },
];

let currentStep = 0;
let enteredName = '';

/**
 * Get the player name entered during onboarding
 */
export function getPlayerName() {
  return enteredName || 'kid';
}

/**
 * Start the onboarding sequence
 */
export function start() {
  currentStep = 0;
  const container = document.getElementById('screen-onboarding');
  container.innerHTML = '';
  ScreenManager.switchTo('onboarding');
  showStep(container);
}

/**
 * Render the current step
 */
function showStep(container) {
  if (currentStep >= SEQUENCE.length) {
    // Onboarding complete — emit event with player name
    container.dispatchEvent(new CustomEvent('onboarding-complete', { bubbles: true, detail: { playerName: enteredName } }));
    return;
  }

  const step = SEQUENCE[currentStep];

  // For consecutive boss steps, keep the boss frame — only update speech bubble
  const prevBossFrame = container.querySelector('.onboarding-boss');
  const isBossStep = step.type === 'boss';

  if (isBossStep && prevBossFrame) {
    // Remove old continue button, keep everything else
    const oldBtn = container.querySelector('.onboarding-continue');
    if (oldBtn) oldBtn.remove();
  } else {
    container.innerHTML = '';
  }

  let wrapper;
  if (isBossStep && prevBossFrame) {
    wrapper = container.querySelector('.onboarding-container');
  } else {
    wrapper = document.createElement('div');
    wrapper.className = 'onboarding-container';
  }

  // --- DIPLOMA ---
  if (step.type === 'diploma') {
    const diploma = document.createElement('div');
    diploma.className = 'diploma';

    const header = document.createElement('div');
    header.className = 'diploma-header';
    header.textContent = step.header;

    const body = document.createElement('div');
    body.className = 'diploma-body';
    body.textContent = step.body;

    // Player name input — handwritten on the diploma
    const nameRow = document.createElement('div');
    nameRow.className = 'diploma-name-row';
    const nameInput = document.createElement('input');
    nameInput.type = 'text';
    nameInput.className = 'diploma-name-input';
    nameInput.placeholder = 'Your name';
    nameInput.maxLength = 24;
    nameInput.id = 'diploma-name';
    nameRow.appendChild(nameInput);
    
    const detail = document.createElement('div');
    detail.className = 'diploma-detail';
    detail.textContent = step.detail;

    // 70s university stamp
    const stamp = document.createElement('div');
    stamp.className = 'diploma-stamp';
    stamp.innerHTML = '<div class="diploma-stamp-ring"><div class="diploma-stamp-inner">STOCKHOLMS<br>UNIVERSITET<br><span class="diploma-stamp-year">1974</span></div></div>';

    const footer = document.createElement('div');
    footer.className = 'diploma-footer';
    footer.textContent = step.footer;

    diploma.appendChild(header);
    diploma.appendChild(body);
    diploma.appendChild(nameRow);
    diploma.appendChild(detail);
    diploma.appendChild(stamp);
    diploma.appendChild(footer);
    wrapper.appendChild(diploma);
  }

  // --- JOB AD ---
  if (step.type === 'job-ad') {
    const ad = document.createElement('div');
    ad.className = `job-ad ${step.style}`;

    const header = document.createElement('div');
    header.className = 'job-ad-header';
    header.textContent = step.header;

    if (step.tagline) {
      const tagline = document.createElement('div');
      tagline.className = 'job-ad-tagline';
      tagline.textContent = step.tagline;
      ad.appendChild(header);
      ad.appendChild(tagline);
    } else {
      ad.appendChild(header);
    }

    const body = document.createElement('div');
    body.className = 'job-ad-body';
    body.textContent = step.body;

    const salary = document.createElement('div');
    salary.className = 'job-ad-salary';
    salary.textContent = step.salary;

    ad.appendChild(body);
    ad.appendChild(salary);
    wrapper.appendChild(ad);
  }

  // --- REJECTION ---
  if (step.type === 'rejection') {
    const letter = document.createElement('div');
    letter.className = 'rejection-letter';

    const header = document.createElement('div');
    header.className = 'rejection-header';
    header.textContent = step.header;

    const stamp = document.createElement('div');
    stamp.className = 'rejection-stamp';
    stamp.textContent = 'REJECTED';
    SFX.play('reject');

    const body = document.createElement('div');
    body.className = 'rejection-body';
    body.textContent = step.body;

    const sender = document.createElement('div');
    sender.className = 'rejection-sender';
    sender.textContent = step.sender;

    letter.appendChild(header);
    letter.appendChild(stamp);
    letter.appendChild(body);
    letter.appendChild(sender);
    wrapper.appendChild(letter);
  }

  // --- ACCEPTANCE ---
  if (step.type === 'acceptance') {
    const letter = document.createElement('div');
    letter.className = 'acceptance-letter';

    SFX.play('relief');

    const header = document.createElement('div');
    header.className = 'acceptance-header';
    header.textContent = step.header;

    const body = document.createElement('div');
    body.className = 'acceptance-body';
    body.textContent = step.body;

    const sender = document.createElement('div');
    sender.className = 'acceptance-sender';
    sender.textContent = step.sender;

    letter.appendChild(header);
    letter.appendChild(body);
    letter.appendChild(sender);
    wrapper.appendChild(letter);
  }

  // --- BOSS ---
  if (step.type === 'boss') {
    // Persist the boss frame (portrait + name) across boss steps;
    // only animate the speech bubble in/out.
    let bossEl = container.querySelector('.onboarding-boss');
    let speechZone = container.querySelector('.boss-speech-zone');

    if (!bossEl) {
      // First boss step — build the persistent frame
      bossEl = document.createElement('div');
      bossEl.className = 'onboarding-boss';

      const portrait = document.createElement('div');
      portrait.className = 'boss-portrait';
      const placeholder = document.createElement('div');
      placeholder.className = 'pixel-placeholder';
      placeholder.dataset.initials = 'GE';
      portrait.appendChild(placeholder);

      const nameTag = document.createElement('div');
      nameTag.className = 'boss-name-tag';
      nameTag.textContent = step.name;

      const leftCol = document.createElement('div');
      leftCol.className = 'boss-left-col';
      leftCol.appendChild(portrait);
      leftCol.appendChild(nameTag);

      speechZone = document.createElement('div');
      speechZone.className = 'boss-speech-zone';

      bossEl.appendChild(leftCol);
      bossEl.appendChild(speechZone);

      // Insert boss frame directly in container (not in wrapper)
      // so it persists between steps
      wrapper.appendChild(bossEl);
    }

    // Clear previous bubble
    speechZone.innerHTML = '';

    // New speech bubble
    const bubble = document.createElement('div');
    bubble.className = `boss-bubble boss-bubble-${step.mood || 'warm'}`;
    bubble.textContent = step.speech.replace(/\{name\}/g, enteredName || 'kid');
    speechZone.appendChild(bubble);
  }

  // --- TITLE CARD ---
  if (step.type === 'title-card') {
    wrapper.className = 'onboarding-container title-card-container';

    const titleEl = document.createElement('div');
    titleEl.className = 'title-card';

    // Word-by-word reveal: PRESS → or → PERISH!
    const words = ['PRESS', 'or', 'PERISH'];
    words.forEach((w, i) => {
      const span = document.createElement('span');
      span.className = 'title-word';
      span.dataset.index = i;
      span.textContent = w;
      if (i === 1) span.classList.add('title-word-or');
      titleEl.appendChild(span);
      if (i < words.length - 1) titleEl.appendChild(document.createTextNode(' '));
    });

    wrapper.appendChild(titleEl);
  }

  // Continue button (auto-advance for title card)
  if (step.type === 'title-card') {
    // Staggered word slam: 0.6s apart
    const wordEls = wrapper.querySelectorAll('.title-word');
    wordEls.forEach((el, i) => {
      setTimeout(() => {
        el.classList.add('visible');
        SFX.play('slam');
      }, 400 + i * 600);
    });

    // After all words shown (400 + 3*600 = 2200), hold 1.5s, then fade out
    const totalRevealTime = 400 + 3 * 600;
    setTimeout(() => {
      const titleEl = wrapper.querySelector('.title-card');
      if (titleEl) titleEl.classList.add('fade-out');
      setTimeout(() => {
        currentStep++;
        showStep(container);
      }, 2000);
    }, totalRevealTime + 1500);
  } else {
    const btn = document.createElement('button');
    btn.className = 'btn-paper onboarding-continue';

    if (step.type === 'diploma') {
      btn.textContent = 'Time to find a job →';
      btn.disabled = true;
      btn.style.opacity = '0.35';
      btn.style.pointerEvents = 'none';
      // Enable only when name is entered
      const nameInput = wrapper.querySelector('#diploma-name');
      nameInput.addEventListener('input', () => {
        const hasName = nameInput.value.trim().length > 0;
        btn.disabled = !hasName;
        btn.style.opacity = hasName ? '' : '0.35';
        btn.style.pointerEvents = hasName ? '' : 'none';
      });
      // Focus the input
      setTimeout(() => nameInput.focus(), 700);
    } else if (step.type === 'job-ad') {
      btn.textContent = step.style === 'shabby' ? '...I guess I\'ll take it' : 'Apply! →';
    } else if (step.type === 'rejection') {
      btn.textContent = 'Next...';
    } else if (step.type === 'acceptance') {
      btn.textContent = 'Report for duty →';
    } else if (step.type === 'boss' && step.mood === 'intense') {
      btn.textContent = 'I understand.';
    } else if (step.type === 'boss') {
      btn.textContent = 'Continue →';
    } else {
      btn.textContent = 'Continue →';
    }

    btn.addEventListener('click', () => {
      SFX.play('click');
      // Save name if on diploma step
      if (step.type === 'diploma') {
        const nameInput = wrapper.querySelector('#diploma-name');
        enteredName = nameInput ? nameInput.value.trim() : '';
      }
      currentStep++;
      showStep(container);
    });
    wrapper.appendChild(btn);
  }

  // Only append wrapper if it's fresh (not a persistent boss frame)
  if (!wrapper.parentNode) {
    container.appendChild(wrapper);
  }
}
