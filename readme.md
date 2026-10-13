# Tic-Tac-Toe with Alpha-Beta Pruning
### Rule-Based vs. Search-Based Game AI

## Project Overview

This project implements an intelligent Tic-Tac-Toe game using **Minimax Algorithm, Alpha-Beta Pruning, Rule-Based Reasoning, and Constraint Satisfaction Problems (CSP)**.

The main objective is to compare rule-based decision-making with search-based game AI and evaluate their performance in terms of winning results, execution time, explainability, and search efficiency.

The project also includes a puzzle-generation system that creates valid Tic-Tac-Toe board positions using backtracking and constraint propagation.

## Objectives

- Implement the Minimax algorithm for optimal Tic-Tac-Toe gameplay.
- Improve search efficiency using Alpha-Beta Pruning.
- Compare the number of nodes explored by Minimax and Alpha-Beta on identical board positions.
- Demonstrate which branches are pruned and explain why the optimal result remains unchanged.
- Develop a rule-based AI player using an ordered set of strategic rules.
- Generate valid Tic-Tac-Toe puzzles using Constraint Satisfaction Problems.
- Explain AI decisions in human-readable language.
- Evaluate rule-based and alpha-beta players over 100 or more games.

## Key Features

### 1. Minimax Algorithm

Minimax explores possible future game states to select the best move.

- Maximizes the AI's winning outcome.
- Minimizes the opponent's winning opportunities.
- Evaluates possible game outcomes using a scoring function.

### 2. Alpha-Beta Pruning

Alpha-Beta Pruning optimizes Minimax by eliminating branches that cannot improve the final decision.

**Features:**
- Tracks alpha and beta values.
- Identifies and records pruned branches.
- Counts explored and pruned nodes.
- Compares search efficiency against plain Minimax.
- Verifies that both algorithms return the same optimal outcome when configured with the same evaluation rules.

### 3. Rule-Based AI

The rule-based player follows an ordered set of strategies:

1. Win if possible.
2. Block the opponent's winning move.
3. Create a fork.
4. Block the opponent's fork.
5. Take the centre.
6. Take the opposite corner.
7. Take an empty corner.
8. Take an empty side.

The system selects the first applicable rule and explains its decision.

**Example:** "Blocked O's row 2 to prevent an immediate win."

### 4. CSP-Based Puzzle Generator

The puzzle generator creates board positions that satisfy specified constraints using backtracking and constraint propagation.

**Constraints include:**
- Legal X and O piece counts.
- No existing winner in the starting position.
- X is the next player to move.
- X can force a win in exactly `n` moves, according to the selected puzzle definition.
- Every generated board must represent a valid game state.

The generator validates each candidate board and rejects positions that violate the constraints.

### 5. Propositional Logic and Reasoning

The project uses logical rules to verify game-state properties.

Example property:

A valid Tic-Tac-Toe board cannot have both X and O as winners.

Let:
- `WX` = X has a winning line.
- `WO` = O has a winning line.

The property can be expressed as:

`¬(WX ∧ WO)`

This means that X and O cannot both have winning lines in a valid game state.

### 6. Explainable and Responsible AI

Each AI move includes a human-readable explanation of the selected action.

Examples:
- "Won by completing row 1."
- "Blocked O's winning column."
- "Selected the centre because no immediate win or block was available."

The project compares the transparency of rule-based decisions with the search-based decisions of Alpha-Beta AI.

## Performance Evaluation

The project evaluates the two AI approaches over **100 or more games**.

The evaluation records:

| Metric | Description |
|---|---|
| Wins | Number of games won by each AI |
| Draws | Number of games ending in a draw |
| Losses | Number of games lost |
| Time per move | Average time taken to select a move |
| Nodes explored | Number of game-tree nodes evaluated |
| Nodes pruned | Number of branches eliminated by Alpha-Beta |
| Puzzle generation | Number of valid puzzles generated for each constraint set |
| Explainability | Human-readable reason provided for each move |

Both algorithms are evaluated on identical starting positions wherever applicable to ensure a fair comparison.

Actual performance results will be recorded after running the experiments.

## Technologies Used

- **Programming Language:** Python
- **Algorithms:** Minimax and Alpha-Beta Pruning
- **AI Techniques:** Rule-Based Systems and Constraint Satisfaction Problems
- **Search Technique:** Backtracking with Constraint Propagation
- **Logic:** Propositional Logic
- **Evaluation:** Game Simulation and Performance Metrics
- **Version Control:** Git and GitHub

## Expected Outcomes

- A working Tic-Tac-Toe game with intelligent AI players.
- A measurable comparison between Minimax and Alpha-Beta Pruning.
- Evidence of branch pruning without changing the optimal search result.
- A rule-based player that provides explanations for its moves.
- A CSP-based puzzle generator that produces valid board positions.
- Logical validation of important game-state properties.
- Performance statistics from 100 or more simulated games.

## Project Structure

```text
tic-tac-toe-alpha-beta/
├── README.md
├── main.py
├── minimax.py
├── alpha_beta.py
├── rule_based_ai.py
├── csp_puzzle_generator.py
├── game_simulator.py
├── evaluation.py
├── logic_validation.py
├── tests/
│   └── test_game.py
└── results/
    ├── pruning_stats.csv
    ├── game_results.csv
    └── puzzle_results.csv
```

*Note: This is a suggested project structure. Update the filenames to match the actual files in your repository.*

## How to Run

1. Clone the repository.
2. Open the project folder.
3. Run the main Python program.
4. Select a game mode or puzzle mode.
5. Run the evaluation module to compare the AI players.

Example:

```bash
git clone <your-github-repository-url>
cd tic-tac-toe-alpha-beta
python main.py
```

Run the appropriate evaluation script to generate performance statistics.

## Conclusion

This project demonstrates how search-based AI and rule-based reasoning can solve the same game using different decision-making approaches. Alpha-Beta Pruning reduces unnecessary search, while rule-based AI provides clear explanations for its decisions. The CSP puzzle generator and logical validation layer extend the project into a broader study of artificial intelligence, reasoning, and responsible AI.

The final evaluation will use experimental results to compare both approaches objectively.

