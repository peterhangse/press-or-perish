/**
 * INTERVIEW SCREEN — Q1 → Q2 → Result flow with lookup table
 */

import * as InterviewEngine from '../engine/interview-engine.js';
import * as ScreenManager from './screen-manager.js';
import { renderSprite } from './npc-sprites.js';
import * as SFX from '../engine/sfx-engine.js';

let currentStory = null;
let currentNPC = null;
let onComplete = null;
let disabledQ1 = [];  // archetypes to gray out (Day Zero tutorial)

/**
 * Start an interview
 * @param {Object} story - Story data from stories.json
 * @param {Object} npc - NPC data from npcs.json
 * @param {Function} callback - Called with { tier, points, headlineOptions } when done
 * @param {Object} [options] - Optional settings
 * @param {Array}  [options.disabledArchetypes] - Q1 archetypes to gray out
 */
export function start(story, npc, callback, options = {}) {
  currentStory = story;
  currentNPC = npc;
  onComplete = callback;
  disabledQ1 = options.disabledArchetypes || [];

  const container = document.getElementById('screen-interview');
  container.innerHTML = '';

  // Build layout
  const layout = document.createElement('div');
  layout.className = 'interview-layout';

  // Left panel — NPC
  const left = buildLeftPanel(npc);
  layout.appendChild(left);

  // Right panel — dialogue + questions
  const right = document.createElement('div');
  right.className = 'interview-right';

  // Story header
  const header = document.createElement('div');
  header.className = 'interview-story-header';
  const title = document.createElement('div');
  title.className = 'interview-story-title';
  title.textContent = story.title;
  const desc = document.createElement('div');
  desc.className = 'interview-story-desc';
  desc.textContent = story.description;
  header.appendChild(title);
  header.appendChild(desc);
  right.appendChild(header);

  // Dialogue area
  const dialogue = document.createElement('div');
  dialogue.className = 'interview-dialogue';
  dialogue.id = 'interview-dialogue';

  // NPC opening line — typewriter word-by-word (1s delay for screen to settle)
  setTimeout(() => {
    typewriteDialogue(dialogue, npc.name, story.interview.opening_line, 'npc', () => {
      // After typewriter finishes, show "Start Interview" button
      const questions = document.getElementById('interview-questions');
      const startBtn = document.createElement('button');
      startBtn.className = 'btn-paper';
      startBtn.textContent = 'Start Interview';
      startBtn.style.alignSelf = 'center';
      startBtn.addEventListener('click', () => {
        SFX.play('click');
        showQ1Options();
      });
      questions.appendChild(startBtn);
    });
  }, 1000);
  right.appendChild(dialogue);

  // Questions area
  const questions = document.createElement('div');
  questions.className = 'interview-questions';
  questions.id = 'interview-questions';
  right.appendChild(questions);

  layout.appendChild(right);
  container.appendChild(layout);
}

/**
 * Build the left NPC panel
 */
function buildLeftPanel(npc) {
  const left = document.createElement('div');
  left.className = 'interview-left';

  const portrait = document.createElement('div');
  portrait.className = 'npc-portrait';

  // Render pixel art sprite (falls back to procedural portrait)
  renderSprite(npc.id, portrait);

  left.appendChild(portrait);

  const name = document.createElement('div');
  name.className = 'npc-name';
  name.textContent = npc.name;

  const title = document.createElement('div');
  title.className = 'npc-title';
  title.textContent = npc.title || npc.role || '';

  const hint = document.createElement('div');
  hint.className = 'npc-expression-hint';
  hint.id = 'npc-expression-hint';
  hint.textContent = npc.initial_demeanor || 'Seems guarded';

  left.appendChild(name);
  left.appendChild(title);
  left.appendChild(hint);

  // Notesheet — bullet points appear as you gather info
  const notesheet = document.createElement('div');
  notesheet.className = 'interview-notesheet';
  notesheet.id = 'interview-notesheet';
  const noteHeader = document.createElement('div');
  noteHeader.className = 'notesheet-header';
  noteHeader.textContent = 'NOTES';
  notesheet.appendChild(noteHeader);
  left.appendChild(notesheet);

  return left;
}

/**
 * Show Q1 archetype choices
 */
function showQ1Options() {
  const questions = document.getElementById('interview-questions');
  questions.innerHTML = '';

  const label = document.createElement('div');
  label.className = 'interview-phase-label';
  label.textContent = 'Opening Question';
  questions.appendChild(label);

  const q1Options = InterviewEngine.getQ1Options(currentStory);

  q1Options.forEach(option => {
    const btn = document.createElement('button');
    btn.className = 'question-btn';

    const isDisabled = disabledQ1.includes(option.archetype);
    if (isDisabled) {
      btn.classList.add('disabled');
      btn.disabled = true;
    }

    const dot = document.createElement('span');
    dot.className = `question-dot ${option.archetype}`;

    const textWrap = document.createElement('div');

    const text = document.createElement('div');
    text.className = 'question-text';
    text.textContent = option.text;

    const arch = document.createElement('div');
    arch.className = 'question-archetype';
    arch.textContent = getArchetypeLabel(option.archetype);

    textWrap.appendChild(text);
    textWrap.appendChild(arch);
    btn.appendChild(dot);
    btn.appendChild(textWrap);

    if (!isDisabled) {
      btn.addEventListener('click', () => handleQ1(option.archetype, option.text));
    }
    questions.appendChild(btn);
  });
}

/**
 * Handle Q1 selection
 */
function handleQ1(archetype, questionText) {
  SFX.play('click');
  const dialogue = document.getElementById('interview-dialogue');
  const questions = document.getElementById('interview-questions');

  // Hide Q1 options while NPC responds
  questions.innerHTML = '';

  // Show player's question
  addDialogueLine(dialogue, 'You', questionText, 'player');

  // Get Q1 response from story data
  const branch = currentStory.interview.branches[archetype];

  // Compute Q1 bonus at pick time
  const q1Bonus = InterviewEngine.computeQ1Bonus(currentStory, archetype);

  // Typewrite NPC response, then continue (1s pause to let the question land)
  setTimeout(() => {
    typewriteDialogue(dialogue, currentNPC.name, branch.q1_response, 'npc', () => {
      // ── Q1 bonus badge on NPC response ──
      const npcLines = dialogue.querySelectorAll('.dialogue-line.npc');
      const lastNPC = npcLines[npcLines.length - 1];
      if (lastNPC) {
        if (q1Bonus > 0) {
          lastNPC.classList.add('tier-2');
          const badge = document.createElement('span');
          badge.className = 'points-badge positive';
          badge.textContent = `+${q1Bonus}`;
          lastNPC.appendChild(badge);
        } else {
          lastNPC.classList.add('tier-0');
          const badge = document.createElement('span');
          badge.className = 'points-badge fail';
          badge.textContent = '\u2717';
          lastNPC.appendChild(badge);
        }
      }

      // Add note from Q1 answer (with bonus)
      addNote(branch.q1_note || summarizeResponse(branch.q1_response), undefined, q1Bonus);

      // Update expression hint
      const hint = document.getElementById('npc-expression-hint');
      hint.textContent = branch.expression_hint || '';

      // Show Q2 options
      showQ2Options(archetype);
    });
  }, 1000);
}

/**
 * Show Q2 follow-up choices
 */
function showQ2Options(q1Archetype) {
  const questions = document.getElementById('interview-questions');
  questions.innerHTML = '';

  const label = document.createElement('div');
  label.className = 'interview-phase-label';
  label.textContent = 'Follow-up Question';
  questions.appendChild(label);

  const q2Options = InterviewEngine.getQ2Options(currentStory, q1Archetype);

  q2Options.forEach((option, index) => {
    const btn = document.createElement('button');
    btn.className = 'question-btn';

    const dot = document.createElement('span');
    dot.className = `question-dot ${option.archetype || q1Archetype}`;

    const textWrap = document.createElement('div');

    const text = document.createElement('div');
    text.className = 'question-text';
    text.textContent = option.text;

    textWrap.appendChild(text);
    btn.appendChild(dot);
    btn.appendChild(textWrap);

    btn.addEventListener('click', () => handleQ2(q1Archetype, index, option.text));
    questions.appendChild(btn);
  });
}

/**
 * Handle Q2 selection — resolves interview
 */
function handleQ2(q1Archetype, q2Index, questionText) {
  SFX.play('click');
  const dialogue = document.getElementById('interview-dialogue');
  const questions = document.getElementById('interview-questions');

  // Hide Q2 options while NPC responds
  questions.innerHTML = '';

  // Remove opening line only — keep Q1 exchange visible
  const openingLine = dialogue.querySelector('.dialogue-line.npc');
  if (openingLine) openingLine.remove();

  // Show player's follow-up
  addDialogueLine(dialogue, 'You', questionText, 'player');

  // Resolve the interview via lookup table
  const result = InterviewEngine.resolveInterview(currentStory, q1Archetype, q2Index);

  // Typewrite NPC response, then show result (1s pause to let the question land)
  setTimeout(() => {
    typewriteDialogue(dialogue, currentNPC.name, result.response, 'npc', () => {
      // ── Feedback: tier-colored border on NPC response ──
      const npcLines = dialogue.querySelectorAll('.dialogue-line.npc');
      const lastNPC = npcLines[npcLines.length - 1];
      if (lastNPC) lastNPC.classList.add(`tier-${result.tier}`);

      // ── Feedback: Q2 bonus badge ──
      if (lastNPC) {
        if (result.q2Bonus > 0) {
          const badge = document.createElement('span');
          badge.className = 'points-badge positive';
          badge.textContent = `+${result.q2Bonus}`;
          lastNPC.appendChild(badge);
        } else {
          const badge = document.createElement('span');
          badge.className = 'points-badge fail';
          badge.textContent = '\u2717';
          lastNPC.appendChild(badge);
        }
      }

      // Add note from Q2 answer (with tier and bonus)
      addNote(result.note || summarizeResponse(result.response), result.tier, result.q2Bonus);

      // Update expression
      const hint = document.getElementById('npc-expression-hint');
      hint.textContent = getExpressionText(result.expression);

      // ── Feedback: portrait tint + body animation ──
      applyExpressionTint(result.expression);
      applyBodyAnimation(result.expression);

      // ── Feedback: one-line verdict below NPC response ──
      if (result.feedback) {
        const fbLine = document.createElement('div');
        fbLine.className = `feedback-line tier-${result.tier}`;
        fbLine.textContent = result.feedback;
        dialogue.appendChild(fbLine);
      }

      // Auto-scroll to bottom after Q2 response
      dialogue.scrollTop = dialogue.scrollHeight;

      // Continue button
      const continueBtn = document.createElement('button');
      continueBtn.className = 'btn-paper';
      continueBtn.textContent = 'Write article →';
      continueBtn.style.marginTop = '6px';
      continueBtn.addEventListener('click', () => {
        if (onComplete) {
          SFX.play('stamp');
          // Rubber stamp flash
          const container = document.getElementById('screen-interview');
          const stamp = document.createElement('div');
          stamp.className = 'stamp-flash green';
          stamp.textContent = 'FILED';
          container.appendChild(stamp);
        
          setTimeout(() => {
            const headlines = InterviewEngine.getHeadlines(currentStory, result.tier);
            onComplete({
              tier: result.tier,
              points: result.points,
              q1Bonus: result.q1Bonus,
              q2Bonus: result.q2Bonus,
              headlines,
              q1Archetype,
              q2Index,
            });
          }, 350);
        }
      });
      questions.appendChild(continueBtn);
    });
  }, 1000);
}

/**
 * Add a dialogue line to the log
 */
function addDialogueLine(container, speaker, text, type) {
  const line = document.createElement('div');
  line.className = `dialogue-line ${type}`;

  const speakerEl = document.createElement('span');
  speakerEl.className = 'speaker';
  speakerEl.textContent = speaker;

  const textEl = document.createElement('span');
  textEl.textContent = text;

  line.appendChild(speakerEl);
  line.appendChild(textEl);
  container.appendChild(line);

  // Auto-scroll
  container.scrollTop = container.scrollHeight;
}

/**
 * Typewrite a dialogue line word-by-word, then call onDone
 */
function typewriteDialogue(container, speaker, text, type, onDone) {
  const line = document.createElement('div');
  line.className = `dialogue-line ${type}`;

  const speakerEl = document.createElement('span');
  speakerEl.className = 'speaker';
  speakerEl.textContent = speaker;

  const textEl = document.createElement('span');
  textEl.className = 'typewriter-cursor';
  textEl.textContent = '';

  line.appendChild(speakerEl);
  line.appendChild(textEl);
  container.appendChild(line);

  const words = text.split(' ');
  let i = 0;

  function nextWord() {
    if (i < words.length) {
      textEl.textContent += (i > 0 ? ' ' : '') + words[i];
      i++;
      SFX.play('tick');
      container.scrollTop = container.scrollHeight;
      setTimeout(nextWord, 100 + Math.random() * 60);
    } else {
      // Remove cursor
      textEl.classList.remove('typewriter-cursor');
      if (onDone) onDone();
    }
  }
  nextWord();
}

/**
 * Get archetype label
 */
function getArchetypeLabel(archetype) {
  switch (archetype) {
    case 'friendly': return 'Trust Builder';
    case 'direct':   return 'Direct';
    case 'pressure': return 'Pressure';
    case 'silence':  return 'Silence';
    default:         return archetype;
  }
}

/**
 * Get expression text description
 */
function getExpressionText(expression) {
  switch (expression) {
    case 'open':     return 'Looks relieved, opening up';
    case 'guarded':  return 'Arms crossed, skeptical';
    case 'hostile':  return 'Angry, wants to end the conversation';
    case 'neutral':  return 'Hard to read';
    case 'grateful': return 'Seems grateful';
    case 'nervous':  return 'Uneasy, looking around';
    case 'defiant':  return 'Defiant, chin raised';
    default:         return expression || '';
  }
}

/**
 * Get tier label
 */
function getTierLabel(tier) {
  switch (tier) {
    case 0: return 'Basic facts only';
    case 1: return 'Good information';
    case 2: return 'Strong story';
    case 3: return 'Full investigation';
    default: return '';
  }
}

/**
 * Get initials from name
 */
function getInitials(name) {
  return name.split(' ').map(w => w[0]).join('').toUpperCase().slice(0, 2);
}

/**
 * Add a note bullet to the notesheet
 * @param {string} text - Note text
 * @param {number} [tier] - Interview tier (0-3) for colored feedback
 * @param {number} [bonus] - Bonus points this note contributed
 */
function addNote(text, tier, bonus) {
  SFX.play('note');
  const notesheet = document.getElementById('interview-notesheet');
  if (!notesheet) return;

  const note = document.createElement('div');
  note.className = 'notesheet-item';
  if (tier !== undefined && tier >= 2) note.classList.add('note-underline');

  const dot = document.createElement('span');
  dot.className = tier !== undefined ? `notesheet-dot tier-${tier}` : 'notesheet-dot';
  dot.textContent = tier !== undefined && tier >= 2 ? '★' : '•';

  const content = document.createElement('span');
  content.className = 'notesheet-text';
  content.textContent = text;

  note.appendChild(dot);
  note.appendChild(content);

  // Per-note bonus indicator
  if (bonus !== undefined) {
    const bonusEl = document.createElement('span');
    if (bonus > 0) {
      bonusEl.className = 'notesheet-bonus positive';
      bonusEl.textContent = `+${bonus}`;
    } else {
      bonusEl.className = 'notesheet-bonus fail';
      bonusEl.textContent = '✗';
    }
    note.appendChild(bonusEl);
  }

  notesheet.appendChild(note);

  // Trigger animation
  requestAnimationFrame(() => note.classList.add('visible'));
}

/**
 * Apply a color tint overlay on the portrait based on expression
 */
function applyExpressionTint(expression) {
  const portrait = document.querySelector('.npc-portrait');
  if (!portrait) return;

  // Remove any existing tint
  portrait.querySelectorAll('.portrait-tint').forEach(el => el.remove());

  let tintClass = '';
  switch (expression) {
    case 'open':     case 'grateful': tintClass = 'tint-warm'; break;
    case 'guarded':  case 'nervous':  tintClass = 'tint-cold'; break;
    case 'hostile':  case 'defiant':  tintClass = 'tint-hostile'; break;
    default: return; // neutral — no tint
  }

  const overlay = document.createElement('div');
  overlay.className = `portrait-tint ${tintClass}`;
  portrait.appendChild(overlay);
}

/**
 * Apply a body animation to the sprite based on expression
 */
function applyBodyAnimation(expression) {
  const body = document.querySelector('.npc-portrait .sprite-body');
  if (!body) return;

  // Remove previous expression animations
  body.classList.remove('anim-nervous', 'anim-hostile', 'anim-open');

  switch (expression) {
    case 'nervous':  body.classList.add('anim-nervous'); break;
    case 'hostile':  case 'defiant': body.classList.add('anim-hostile'); break;
    case 'open':     case 'grateful': body.classList.add('anim-open'); break;
    // neutral/guarded: keep default idle sway
  }
}

/**
 * Summarize a response into a short note (first sentence, max ~60 chars)
 */
function summarizeResponse(text) {
  if (!text) return '...';
  // Strip stage directions (*action text*)
  let clean = text.replace(/\*[^*]+\*\s*/g, '').trim();
  if (!clean) clean = text;
  // Take first sentence
  const firstSentence = clean.split(/[.!?]/)[0].trim();
  if (firstSentence.length <= 60) return firstSentence;
  return firstSentence.substring(0, 57) + '...';
}
