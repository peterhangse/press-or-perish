/**
 * ACHIEVEMENTS ENGINE — Pure logic, no DOM
 * Press or Perish · Achievement definitions + check logic
 *
 * All achievements stored in localStorage as pop_achievements (JSON array of unlocked IDs).
 * Each achievement has a check(ctx) function that receives the current game context.
 */

// ── Achievement Definitions ──

const ACHIEVEMENTS = [

  // ═══════════════════════════════════
  //  MILESTONES (6)
  // ═══════════════════════════════════

  {
    id: 'first_byline',
    name: 'First Byline',
    description: 'Complete Day 1',
    category: 'milestones',
    trigger: 'day_end',
    check: (ctx) => ctx.day === 1,
  },
  {
    id: 'no_skill',
    name: 'No Skill',
    description: 'Publish a Tier 0 story',
    category: 'milestones',
    trigger: 'day_end',
    check: (ctx) => ctx.tier === 0,
  },
  {
    id: 'breakthrough',
    name: 'Breakthrough',
    description: 'Reach Tier 3',
    category: 'milestones',
    trigger: 'day_end',
    check: (ctx) => ctx.tier === 3,
  },
  {
    id: 'beat_the_clock',
    name: 'Beat the Clock',
    description: 'Win a day by 5+ points',
    category: 'milestones',
    trigger: 'day_end',
    check: (ctx) => (ctx.points - ctx.competitorScore) >= 5,
  },
  {
    id: 'survived',
    name: 'Survived',
    description: 'Reach Friday evening',
    category: 'milestones',
    trigger: 'game_over',
    check: (ctx) => ctx.survived === true,
  },
  {
    id: 'press_master',
    name: 'Press Master',
    description: 'Max news value + interview (14 pts)',
    category: 'milestones',
    trigger: 'day_end',
    check: (ctx) => ctx.baseValue === 8 && ctx.tier === 3,
  },

  // ═══════════════════════════════════
  //  INTERVIEW MASTERY (5)
  // ═══════════════════════════════════

  {
    id: 'soft_touch',
    name: 'Soft Touch',
    description: 'Reach Tier 3 using Friendly',
    category: 'interview',
    trigger: 'day_end',
    check: (ctx) => ctx.tier === 3 && ctx.q1Archetype === 'friendly',
  },
  {
    id: 'silent_treatment',
    name: 'Silent Treatment',
    description: 'Reach Tier 3 using Silence',
    category: 'interview',
    trigger: 'day_end',
    check: (ctx) => ctx.tier === 3 && ctx.q1Archetype === 'silence',
  },
  {
    id: 'full_arsenal',
    name: 'Full Arsenal',
    description: 'Use all 4 archetypes in one week',
    category: 'interview',
    trigger: 'game_over',
    check: (ctx) => {
      const archetypes = new Set(ctx.dayHistory.map(d => d.q1Archetype).filter(Boolean));
      return archetypes.size >= 4;
    },
  },
  {
    id: 'pattern_master',
    name: 'Pattern Master',
    description: 'Tier 3 on 3 consecutive days',
    category: 'interview',
    trigger: 'day_end',
    check: (ctx) => {
      const history = ctx.dayHistory;
      if (history.length < 3) return false;
      const last3 = history.slice(-3);
      return last3.every(d => d.tier === 3);
    },
  },
  {
    id: 'hidden_gem',
    name: 'Hidden Gem',
    description: 'Find gold in a low-value story',
    category: 'interview',
    trigger: 'day_end',
    check: (ctx) => ctx.tier >= 2 && ctx.baseValue <= 3,
  },

  // ═══════════════════════════════════
  //  SURVIVAL (5)
  // ═══════════════════════════════════

  {
    id: 'clean_sweep',
    name: 'Clean Sweep',
    description: 'Win all 5 days',
    category: 'survival',
    trigger: 'game_over',
    check: (ctx) => {
      return ctx.survived && ctx.dayHistory.length >= 5 &&
        ctx.dayHistory.every(d => d.points > d.competitorScore);
    },
  },
  {
    id: 'comeback_king',
    name: 'Comeback King',
    description: 'Survive after being at -8 or worse',
    category: 'survival',
    trigger: 'game_over',
    check: (ctx) => {
      return ctx.survived && ctx.dayHistory.some(d => d.deficit <= -8);
    },
  },
  {
    id: 'perfect_week',
    name: 'Perfect Week',
    description: 'All 5 stories at Tier 3',
    category: 'survival',
    trigger: 'game_over',
    check: (ctx) => {
      return ctx.survived && ctx.dayHistory.length >= 5 &&
        ctx.dayHistory.every(d => d.tier === 3);
    },
  },
  {
    id: 'high_scorer',
    name: 'High Scorer',
    description: 'Score 60+ total in one week',
    category: 'survival',
    trigger: 'game_over',
    check: (ctx) => ctx.totalPoints >= 60,
  },
  {
    id: 'veteran',
    name: 'Survivor',
    description: 'Win 10 weeks',
    category: 'survival',
    trigger: 'game_over',
    check: (ctx) => {
      if (!ctx.survived) return false;
      const highscores = JSON.parse(localStorage.getItem('pop_highscores') || '[]');
      // Count survived runs (including this one, which is already saved)
      const survivedCount = highscores.filter(h => h.survived).length;
      return survivedCount >= 10;
    },
  },

  // ═══════════════════════════════════
  //  STORIES — Specific legendary moments (9)
  // ═══════════════════════════════════

  {
    id: 'journalism_at_its_best',
    name: 'Journalism at Its Best',
    description: 'Use silence to learn what the police couldn\'t',
    category: 'stories',
    trigger: 'day_end',
    check: (ctx) => ctx.storyId === 'missing_girl' && ctx.q1Archetype === 'silence' && ctx.q2Index === 2 && ctx.tier === 3,
  },
  {
    id: 'its_my_fault',
    name: '"It\'s My Fault"',
    description: 'Hear the mother\'s confession',
    category: 'stories',
    trigger: 'day_end',
    check: (ctx) => ctx.storyId === 'missing_girl' && ctx.q1Archetype === 'pressure' && ctx.q2Index === 2 && ctx.tier === 3,
  },
  {
    id: 's_is_doing_it_again',
    name: '"S Is Doing It Again"',
    description: 'Find the diary under the mattress',
    category: 'stories',
    trigger: 'day_end',
    check: (ctx) => ctx.storyId === 'missing_girl' && ctx.q1Archetype === 'direct' && ctx.q2Index === 2 && ctx.tier === 3,
  },
  {
    id: 'i_recorded_it',
    name: '"I Recorded It"',
    description: 'The fire chief made a terrible mistake',
    category: 'stories',
    trigger: 'day_end',
    check: (ctx) => ctx.storyId === 'brandkårsutryckning' && ctx.q1Archetype === 'silence' && ctx.q2Index === 2 && ctx.tier === 3,
  },
  {
    id: 'twenty_minutes',
    name: 'Twenty Minutes',
    description: 'Discover the falsified emergency logs',
    category: 'stories',
    trigger: 'day_end',
    check: (ctx) => ctx.storyId === 'brandkårsutryckning' && ctx.q1Archetype === 'pressure' && ctx.q2Index === 0 && ctx.tier === 3,
  },
  {
    id: 'three_years_of_silence',
    name: 'Three Years of Silence',
    description: 'A whistleblower hands you everything',
    category: 'stories',
    trigger: 'day_end',
    check: (ctx) => ctx.storyId === 'sjukskrivningarna' && ctx.q1Archetype === 'silence' && ctx.q2Index === 2 && ctx.tier === 3,
  },
  {
    id: 'print_that_if_you_dare',
    name: 'Print That If You Dare',
    description: 'Get your own boss to dare you',
    category: 'stories',
    trigger: 'day_end',
    check: (ctx) => ctx.storyId === 'vargjakten' && ctx.q1Archetype === 'direct' && ctx.q2Index === 0 && ctx.tier === 3,
  },
  {
    id: 'eighty_five_vs_twenty_seven',
    name: '85 vs 27',
    description: 'Expose the obscene budget contrast',
    category: 'stories',
    trigger: 'day_end',
    check: (ctx) => ctx.storyId === 'äldreboende_svält' && ctx.q1Archetype === 'pressure' && ctx.q2Index === 1 && ctx.tier === 3,
  },
  {
    id: 'fourteen_and_crying',
    name: 'Fourteen and Crying',
    description: 'Find the human behind a petty crime',
    category: 'stories',
    trigger: 'day_end',
    check: (ctx) => ctx.storyId === 'stöld_på_ica' && ctx.tier >= 1,
  },

  // ═══════════════════════════════════
  //  ROOKIE MISTAKES (5)
  // ═══════════════════════════════════

  {
    id: 'get_back_to_your_desk',
    name: 'Get Back to Your Desk',
    description: 'Moralize your own boss',
    category: 'rookie',
    trigger: 'day_end',
    check: (ctx) => ctx.storyId === 'vargjakten' && ctx.q1Archetype === 'pressure' && ctx.q2Index === 0 && ctx.tier === 0,
  },
  {
    id: 'ive_never_met_you',
    name: '"I\'ve Never Met You"',
    description: 'Scare away a terrified whistleblower',
    category: 'rookie',
    trigger: 'day_end',
    check: (ctx) => ctx.storyId === 'sjukskrivningarna' && ctx.q1Archetype === 'pressure' && ctx.q2Index === 1 && ctx.tier === 0,
  },
  {
    id: 'you_sound_like_the_police',
    name: 'You Sound Like the Police',
    description: 'Lose a traumatized witness',
    category: 'rookie',
    trigger: 'day_end',
    check: (ctx) => ctx.storyId === 'trafikolyckan' && ctx.q1Archetype === 'pressure' && ctx.q2Index === 1 && ctx.tier === 0,
  },
  {
    id: 'we_are_done_here',
    name: '"We\'re Done Here"',
    description: 'Threaten an injured worker',
    category: 'rookie',
    trigger: 'day_end',
    check: (ctx) => ctx.storyId === 'mill_accident' && ctx.q1Archetype === 'pressure' && ctx.q2Index === 1 && ctx.tier === 0,
  },
  {
    id: 'five_zeroes',
    name: 'Five Zeroes',
    description: 'Tier 0 on all 5 days',
    category: 'rookie',
    trigger: 'game_over',
    check: (ctx) => {
      return ctx.dayHistory.length >= 5 && ctx.dayHistory.every(d => d.tier === 0);
    },
  },
];

// ── Category labels in display order ──

export const CATEGORIES = [
  { id: 'milestones', name: 'MILESTONES' },
  { id: 'interview', name: 'INTERVIEW MASTERY' },
  { id: 'survival', name: 'SURVIVAL' },
  { id: 'stories', name: 'STORIES' },
  { id: 'rookie', name: 'ROOKIE MISTAKES' },
];

// ── Public API ──

/**
 * Get all achievement definitions
 */
export function getAll() {
  return ACHIEVEMENTS;
}

/**
 * Get total count
 */
export function getTotal() {
  return ACHIEVEMENTS.length;
}

/**
 * Load unlocked achievement IDs from localStorage
 * @returns {Set<string>}
 */
export function loadUnlocked() {
  try {
    const data = JSON.parse(localStorage.getItem('pop_achievements') || '[]');
    return new Set(data);
  } catch {
    return new Set();
  }
}

/**
 * Save an achievement as unlocked
 * @param {string} id
 */
export function saveUnlocked(id) {
  const unlocked = loadUnlocked();
  unlocked.add(id);
  localStorage.setItem('pop_achievements', JSON.stringify([...unlocked]));
}

/**
 * Check all achievements against current context.
 * Returns array of newly unlocked achievement objects.
 *
 * @param {string} trigger - 'day_end' or 'game_over'
 * @param {Object} ctx - Game context:
 *   { day, storyId, q1Archetype, q2Index, tier, points, baseValue,
 *     competitorScore, deficit, dayHistory, survived, totalPoints }
 * @returns {Array<Object>} - Newly unlocked achievements
 */
export function checkAchievements(trigger, ctx) {
  const unlocked = loadUnlocked();
  const newlyUnlocked = [];

  for (const achievement of ACHIEVEMENTS) {
    // Skip already unlocked
    if (unlocked.has(achievement.id)) continue;
    // Skip wrong trigger
    if (achievement.trigger !== trigger) continue;
    // Check condition
    try {
      if (achievement.check(ctx)) {
        newlyUnlocked.push(achievement);
        saveUnlocked(achievement.id);
      }
    } catch (e) {
      console.warn(`Achievement check failed: ${achievement.id}`, e);
    }
  }

  return newlyUnlocked;
}
