# BARL - Bayesian Approximate Reinforcement Learning
This package should serve as a collection of tools to do RL in general and in particular bayesian RL.

## The Main Features(Jul 2019):
1. estimators
2. agents
3. environments
4. simulations & visualisation

## Installation:

### PIP:
```bash
pip3 install barl
```

### Github:
```bash
git clone https://github.com/ai-nikolai/barl
cd barl
pip3 install -e .
```

## Usage:

### Testing
```bash
cd barl
pytest
```

### Experiments:
```bash
cd barl
cd experiments
python3 experiments_mab.py
```

### Scripts:
```python
import barl

env = barl.environments.MultiArmedBandit(arms=4)

agent1 = barl.agents.baselines.RandomActionsSampler(numActions=4)

total, arlist, _ = barl.simulations.run_state_less_agent_and_env( environment=env, agent=agent1, N=100)

barl.utils.plotting.plot_reward_over_time_from_ar(arlist)
```



## Copyright (C) - Nikolai Rozanov 2019-Present
