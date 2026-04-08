# ============================================================
#   NUMBER GUESSING GAME - Single File Program
#   Built-in functions + Exception Handling + Flask Web App
# ============================================================

import random
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# ─────────────────────────────────────────────
#  SECTION 1: GAME LOGIC (built-in functions)
# ─────────────────────────────────────────────

def generate_secret_number(start=1, end=100):
    """Generate random number using built-in random.randint()"""
    try:
        if start >= end:
            raise ValueError("Start must be less than end!")
        return random.randint(start, end)       # built-in: random.randint
    except ValueError as e:
        print(f"Error: {e}")
        return random.randint(1, 100)


def validate_guess(guess_str, start=1, end=100):
    """Validate guess using built-in int() and range()"""
    try:
        guess = int(guess_str)                  # built-in: int()
        if guess not in range(start, end + 1):  # built-in: range()
            raise ValueError(f"Enter a number between {start} and {end}!")
        return guess, None
    except ValueError as e:
        return None, str(e)                     # built-in: str()


def check_guess(guess, secret):
    """Check guess and return result using built-in abs()"""
    try:
        if not isinstance(guess, int) or not isinstance(secret, int):
            raise TypeError("Values must be integers!")

        difference = abs(guess - secret)        # built-in: abs()

        if guess == secret:
            return "correct", "exact"

        hint = "too_low" if guess < secret else "too_high"

        # Closeness hint
        if difference <= 5:
            closeness = "very_close"
        elif difference <= 15:
            closeness = "close"
        else:
            closeness = "far"

        return hint, closeness

    except TypeError as e:
        return "error", str(e)


def calculate_score(attempts):
    """Calculate score using built-in max() and min()"""
    try:
        if attempts <= 0:
            raise ValueError("Attempts must be positive!")
        score = max(0, 1000 - attempts * 80)    # built-in: max()
        score = min(score, 1000)                # built-in: min()
        return score
    except ValueError as e:
        print(f"Score error: {e}")
        return 0


def get_attempts_left(attempts_used, max_attempts=10):
    """Return remaining attempts using built-in max()"""
    return max(0, max_attempts - attempts_used) # built-in: max()


def get_result_message(score):
    """Return result message using built-in next()"""
    messages = [
        (900, "🏆 Genius! Unbelievable!"),
        (700, "🌟 Excellent! Very impressive!"),
        (500, "😊 Good job! Well played!"),
        (200, "😅 Not bad! Keep practicing!"),
        (0,   "😬 Better luck next time!"),
    ]
    return next((m for s, m in messages if score >= s), "😬 Try again!")  # built-in: next()


# ─────────────────────────────────────────────
#  SECTION 2: GAME STATE
# ─────────────────────────────────────────────

game_state = {
    "secret":      None,
    "attempts":    0,
    "max_attempts": 10,
    "game_over":   False,
    "won":         False,
    "history":     []
}

# ─────────────────────────────────────────────
#  SECTION 3: HTML PAGE (runs in browser)
# ─────────────────────────────────────────────

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>🎯 Number Guessing Game</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka+One&family=Nunito:wght@400;600;800&display=swap');

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      min-height: 100vh;
      background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
      display: flex; align-items: center; justify-content: center;
      font-family: 'Nunito', sans-serif;
      color: #fff;
    }

    .card {
      background: rgba(255,255,255,0.07);
      border: 1px solid rgba(255,255,255,0.15);
      border-radius: 24px;
      padding: 40px 36px;
      width: 430px;
      text-align: center;
      backdrop-filter: blur(12px);
      box-shadow: 0 20px 60px rgba(0,0,0,0.5);
    }

    h1 {
      font-family: 'Fredoka One', cursive;
      font-size: 2.4rem;
      color: #f7c948;
      text-shadow: 0 0 20px rgba(247,201,72,0.5);
      margin-bottom: 4px;
    }

    .subtitle { color: #a0aec0; font-size: 0.95rem; margin-bottom: 26px; }

    .stats {
      display: flex; justify-content: space-between;
      background: rgba(0,0,0,0.25);
      border-radius: 14px;
      padding: 14px 20px;
      margin-bottom: 22px;
    }

    .stat label { color: #a0aec0; display: block; font-size: 0.75rem; }
    .stat span  { font-weight: 800; font-size: 1.2rem; color: #f7c948; }

    #message-box {
      min-height: 52px;
      background: rgba(0,0,0,0.3);
      border-radius: 12px;
      padding: 12px 16px;
      margin-bottom: 20px;
      font-size: 1rem;
      font-weight: 600;
      color: #e2e8f0;
      display: flex; align-items: center; justify-content: center;
      transition: all 0.3s;
    }

    .history {
      max-height: 130px;
      overflow-y: auto;
      margin-bottom: 18px;
      display: flex; flex-direction: column; gap: 6px;
    }

    .history-item {
      display: flex; justify-content: space-between; align-items: center;
      background: rgba(255,255,255,0.06);
      border-radius: 8px;
      padding: 6px 14px;
      font-size: 0.88rem;
      animation: slideIn 0.3s ease;
    }

    @keyframes slideIn {
      from { transform: translateX(-20px); opacity: 0; }
      to   { transform: translateX(0);     opacity: 1; }
    }

    .tag { padding: 2px 10px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; }
    .tag.high { background: #fc8181; color: #1a1a1a; }
    .tag.low  { background: #68d391; color: #1a1a1a; }
    .tag.win  { background: #f7c948; color: #1a1a1a; }

    .input-row { display: flex; gap: 10px; margin-bottom: 14px; }

    input[type=number] {
      flex: 1;
      padding: 14px 16px;
      border-radius: 12px;
      border: 2px solid rgba(255,255,255,0.15);
      background: rgba(255,255,255,0.08);
      color: #fff;
      font-size: 1.1rem;
      font-family: 'Nunito', sans-serif;
      outline: none;
      transition: border-color 0.2s;
    }

    input[type=number]:focus { border-color: #f7c948; }
    input[type=number]::-webkit-inner-spin-button { -webkit-appearance: none; }

    button {
      padding: 14px 22px;
      border-radius: 12px;
      border: none;
      cursor: pointer;
      font-family: 'Fredoka One', cursive;
      font-size: 1rem;
      transition: all 0.2s;
    }

    #guess-btn {
      background: linear-gradient(135deg, #f7c948, #f6ad55);
      color: #1a1a1a;
    }

    #guess-btn:hover  { transform: scale(1.05); box-shadow: 0 4px 20px rgba(247,201,72,0.4); }
    #guess-btn:active { transform: scale(0.97); }

    #new-btn {
      width: 100%;
      background: rgba(255,255,255,0.1);
      color: #fff;
      font-size: 0.95rem;
      border: 1px solid rgba(255,255,255,0.2);
    }

    #new-btn:hover { background: rgba(255,255,255,0.18); }

    .win-msg  { color: #f7c948 !important; text-shadow: 0 0 12px rgba(247,201,72,0.6); }
    .lose-msg { color: #fc8181 !important; }
  </style>
</head>
<body>
<div class="card">
  <h1>🎯 Guess the Number</h1>
  <p class="subtitle">Pick a number between <strong>1</strong> and <strong>100</strong></p>

  <div class="stats">
    <div class="stat">
      <label>Attempts</label>
      <span id="attempts">0</span> / <span>10</span>
    </div>
    <div class="stat">
      <label>Remaining</label>
      <span id="remaining">10</span>
    </div>
    <div class="stat">
      <label>Score</label>
      <span id="score">—</span>
    </div>
  </div>

  <div id="message-box">Make your first guess! 🤔</div>

  <div class="history" id="history"></div>

  <div class="input-row">
    <input type="number" id="guess-input" placeholder="Enter 1–100..." min="1" max="100"/>
    <button id="guess-btn" onclick="makeGuess()">Guess!</button>
  </div>

  <button id="new-btn" onclick="newGame()">🔄 New Game</button>
</div>

<script>
  async function newGame() {
    const res  = await fetch('/new_game', { method: 'POST' });
    const data = await res.json();
    document.getElementById('attempts').textContent  = 0;
    document.getElementById('remaining').textContent = data.max_attempts;
    document.getElementById('score').textContent     = '—';
    document.getElementById('message-box').textContent = '🎮 New game! Make your guess!';
    document.getElementById('message-box').className   = '';
    document.getElementById('history').innerHTML        = '';
    document.getElementById('guess-input').value        = '';
    document.getElementById('guess-input').disabled     = false;
    document.getElementById('guess-btn').disabled       = false;
  }

  async function makeGuess() {
    const input = document.getElementById('guess-input');
    const val   = input.value.trim();
    if (!val) return;

    const res  = await fetch('/guess', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ guess: val })
    });
    const data = await res.json();

    document.getElementById('attempts').textContent  = data.attempts;
    document.getElementById('remaining').textContent = data.attempts_left;

    const msgBox = document.getElementById('message-box');
    msgBox.className = '';

    if (data.error) {
      msgBox.textContent = '⚠️ ' + data.error;
      input.value = '';
      return;
    }

    // Add history row
    const hist = document.getElementById('history');
    const item = document.createElement('div');
    item.className = 'history-item';
    const tagClass = data.result === 'too_high' ? 'high' : data.result === 'too_low' ? 'low' : 'win';
    const tagLabel = data.result === 'too_high' ? '▲ Too High' : data.result === 'too_low' ? '▼ Too Low' : '✓ Correct!';
    item.innerHTML = `<span>Guess: <strong>${val}</strong></span><span class="tag ${tagClass}">${tagLabel}</span>`;
    hist.prepend(item);

    if (data.game_over) {
      if (data.won) {
        msgBox.textContent = data.message + ' | Score: ' + data.score;
        msgBox.classList.add('win-msg');
        document.getElementById('score').textContent = data.score;
      } else {
        msgBox.textContent = '😢 Game Over! The number was ' + data.secret;
        msgBox.classList.add('lose-msg');
      }
      document.getElementById('guess-input').disabled = true;
      document.getElementById('guess-btn').disabled   = true;
    } else {
      const hints = {
        too_high_very_close: '🔥 Too High — VERY close!',
        too_high_close:      '📉 Too High — getting closer!',
        too_high_far:        '⬇️ Too High! Go lower.',
        too_low_very_close:  '🔥 Too Low — VERY close!',
        too_low_close:       '📈 Too Low — getting closer!',
        too_low_far:         '⬆️ Too Low! Go higher.',
      };
      msgBox.textContent = hints[data.result + '_' + data.closeness] || 'Keep guessing!';
    }

    input.value = '';
    input.focus();
  }

  document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('guess-input').addEventListener('keydown', e => {
      if (e.key === 'Enter') makeGuess();
    });
    newGame();
  });
</script>
</body>
</html>
"""

# ─────────────────────────────────────────────
#  SECTION 4: FLASK ROUTES (web endpoints)
# ─────────────────────────────────────────────

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)


@app.route("/new_game", methods=["POST"])
def new_game():
    try:
        game_state["secret"]     = generate_secret_number(1, 100)
        game_state["attempts"]   = 0
        game_state["game_over"]  = False
        game_state["won"]        = False
        game_state["history"]    = []
        return jsonify({"status": "started", "max_attempts": game_state["max_attempts"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/guess", methods=["POST"])
def guess():
    try:
        if game_state["secret"] is None:
            raise RuntimeError("Game not started! Click New Game first.")

        if game_state["game_over"]:
            raise RuntimeError("Game is over. Click New Game!")

        data      = request.get_json()
        guess_str = data.get("guess", "")

        # Validate using our function
        guess_num, error = validate_guess(guess_str, 1, 100)
        if error:
            return jsonify({"error": error})

        game_state["attempts"] += 1

        # Check using our function
        result, closeness = check_guess(guess_num, game_state["secret"])

        attempts_left = get_attempts_left(game_state["attempts"], game_state["max_attempts"])

        response = {
            "result":        result,
            "closeness":     closeness,
            "attempts":      game_state["attempts"],
            "attempts_left": attempts_left,
            "game_over":     False,
            "won":           False,
        }

        if result == "correct":
            score   = calculate_score(game_state["attempts"])
            message = get_result_message(score)
            game_state["game_over"] = True
            game_state["won"]       = True
            response.update({"game_over": True, "won": True, "score": score, "message": message})

        elif attempts_left == 0:
            game_state["game_over"] = True
            response.update({"game_over": True, "won": False, "secret": game_state["secret"]})

        game_state["history"].append(guess_num)
        return jsonify(response)

    except (RuntimeError, KeyError) as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Unexpected error: " + str(e)}), 500


# ─────────────────────────────────────────────
#  SECTION 5: RUN THE APP
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 45)
    print("   🎯 NUMBER GUESSING GAME")
    print("=" * 45)
    print("  Open browser at: http://localhost:5000")
    print("  Press Ctrl+C to stop the server")
    print("=" * 45)
    app.run(debug=True)