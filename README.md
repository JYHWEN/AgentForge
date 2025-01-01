# AgentForge
A lightweight, open‑source framework for building and running simple agent‑based simulations in Python.

## Description
AgentForge provides the core building blocks—`Agent` and `Environment`—to model entities that move, interact, and evolve on a grid. It's designed for educational purposes, rapid prototyping, and hobby projects.

## Features
- Grid‑based world with wrap‑around edges  
- Pluggable `Agent` behaviors via the `act` method  
- Simple health system and damage handling  
- Minimal dependencies (only the Python standard library)  
- Easy to extend with custom agents and rules  

## Installation
```bash
git clone https://github.com/yourname/AgentForge.git
cd AgentForge
python -m pip install -r requirements.txt   # (empty, only stdlib)
```

## Usage
Run the demo simulation:
```bash
python agentforge.py
```
Create your own agents by subclassing `Agent` and overriding `act`. Add them to an `Environment` instance and call `tick()` each step.

## License
MIT © 2024 AgentForge contributors