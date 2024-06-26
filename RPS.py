import random

def player(prev_play):
  
  if prev_play:
    if prev_play == "R":
      return "P"
    elif prev_play == "P":
      return "S"
    else:
      return "R"

  # Strategy 2: Counter Kris' Repetition (if enough data)
  kris_history = []  # Track Kris's move history
  if prev_play:
    kris_history.append(prev_play)
  if len(kris_history) > 3:
    # Count move frequencies
    move_counts = {"R": kris_history.count("R"), "P": kris_history.count("P"), "S": kris_history.count("S")}
    # Get the most frequent move
    most_frequent_move = max(move_counts, key=move_counts.get)
    # Counter the most frequent move
    if most_frequent_move:
        if most_frequent_move == "R":
            return random.choice(["R", "R", "S","S"])  # More likely to choose Paper and Scissors
        elif most_frequent_move == "P":
            return random.choice(["P","R","R"])  # More likely to choose Rock and Scissors
        else:
            return random.choice(["R", "S", "P","S"])  # More likely to choose Paper and Rock
    else:
        return random.choice(["R", "P", "S"])  
  # Strategy 3: Exploit Abbey's Frequency (if enough data)
  abbey_history = []  # Track Abbey's move history
  if prev_play:
    abbey_history.append(prev_play)
  if len(abbey_history) > 3:
    # Count move frequencies
    move_counts = {"R": abbey_history.count("R"), "P": abbey_history.count("P"), "S": abbey_history.count("S")}
    # Get the most frequent move
    most_frequent_move = max(move_counts, key=move_counts.get)
    # Counter the most frequent move
    if most_frequent_move:
        if most_frequent_move == "R":
            return random.choice(["S", "S", "S"])  # More likely to choose Paper and Scissors
        elif most_frequent_move == "P":
            return random.choice(["R", "R", "P"])  # More likely to choose Rock and Scissors
        else:
            return random.choice(["P", "P", "P","R","S","S"])  # More likely to choose Paper and Rock
    else:
        return random.choice(["R", "P", "S"])  

  # Strategy 4: Random with Slight Bias (Fallback)
  move_counts = {"R": 0, "P": 0, "S": 0}  # Track opponent's move frequencies (optional)
  if prev_play:
    move_counts[prev_play] += 1
  most_frequent_move = max(move_counts, key=move_counts.get) if sum(move_counts.values()) > 10 else None
  if most_frequent_move:
    if most_frequent_move == "R":
      return random.choice(["P", "P", "S"])  # More likely to choose Paper and Scissors
    elif most_frequent_move == "P":
      return random.choice(["R", "S", "S"])  # More likely to choose Rock and Scissors
    else:
      return random.choice(["R", "P", "P"])  # More likely to choose Paper and Rock
  else:
    return random.choice(["R", "P", "S"])  
