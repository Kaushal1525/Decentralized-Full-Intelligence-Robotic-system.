
# Decentralized Multi-Robot Collaborative Decision-Making System

## Overview

This project presents a decentralized multi-robot collaborative decision-making simulation developed using Python. The system demonstrates how a fleet of autonomous robots can independently select tasks, coordinate through consensus-based decision making, recover from failures, and dynamically reassign unfinished work without relying on a permanent central controller.

The simulation incorporates concepts from swarm robotics, distributed artificial intelligence, autonomous systems, and multi-agent coordination. Robots continuously monitor their energy levels, select tasks based on priority and proximity, elect temporary leaders during failures, and collaboratively recover from unexpected robot breakdowns.

The project serves as a research-oriented simulation of decentralized robotic coordination suitable for autonomous warehouse systems, industrial automation, and collaborative robotics.

---

## Features

- Decentralized task allocation
- Autonomous task selection
- Energy-aware decision making
- Consensus-based task reassignment
- Temporary leader election
- Robot failure simulation
- Collaborative recovery mechanism
- Dynamic workload distribution
- Motion simulation
- Multi-agent coordination
- Real-time decision cycles
- Distributed robot management

---

## Technologies Used

- Python 3
- Math
- Random
- Time

---

## Project Structure

```text
Decentralized-Multi-Robot-System/
│
├── decentralized_collaboration.py
├── README.md
└── requirements.txt
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Kaushal1525/Decentralized-Multi-Robot-System.git
```

### Navigate to the project

```bash
cd Decentralized-Multi-Robot-System
```

### Run the simulation

```bash
python decentralized_collaboration.py
```

No external libraries are required.

---

## Working Principle

The simulation operates through repeated collaborative decision cycles.

During each cycle:

1. The status of every robot is displayed.
2. Idle robots autonomously select suitable tasks.
3. Robot energy levels are evaluated before accepting work.
4. Robot failures are randomly simulated.
5. A temporary leader is elected whenever a failure occurs.
6. Available robots participate in consensus voting.
7. The failed robot's unfinished task is reassigned.
8. Robots continue moving toward assigned tasks.
9. Completed tasks are removed from the task queue.
10. The process repeats until all cycles are completed.

---

## System Architecture

### Robot Model

Each robot maintains:

- Robot ID
- Current position
- Velocity
- Energy level
- Current workload
- Assigned task
- Failure status
- Temporary leadership status

---

### Task Model

Each task contains:

- Task ID
- Target location
- Priority level
- Assigned robot
- Completion status

---

### Autonomous Task Selection

Robots independently evaluate available tasks.

Task selection considers:

- Distance to the task
- Robot energy level
- Task priority
- Current workload
- Task availability

Robots with insufficient battery levels remain idle until conditions improve.

---

### Consensus-Based Coordination

When a robot fails during task execution:

1. A temporary leader is elected.
2. Available robots evaluate the unfinished task.
3. Each robot computes a suitability score based on distance and remaining energy.
4. The robot with the best score is selected.
5. The task is reassigned automatically.

This decentralized process eliminates dependence on a permanent controller.

---

### Temporary Leader Election

During collaborative recovery:

- The operational robot with the highest remaining energy is elected as the temporary leader.
- The leader coordinates task recovery only during the failure event.
- Leadership is released immediately after recovery.

---

### Failure Recovery

The simulation includes random robot failures.

Recovery includes:

- Failure detection
- Leader election
- Consensus voting
- Task reassignment
- Mission continuation

This enables uninterrupted system operation despite robot failures.

---

### Motion Simulation

Each robot moves toward its assigned task using a simple velocity-based motion model.

Movement includes:

- Velocity updates
- Speed limiting
- Position updates
- Energy consumption
- Task completion detection

---

## Decision Cycle Workflow

```text
Initialize Robots and Tasks
            │
            ▼
Display Robot Status
            │
            ▼
Autonomous Task Selection
            │
            ▼
Energy Verification
            │
            ▼
Robot Failure Detection
            │
            ▼
Temporary Leader Election
            │
            ▼
Consensus Voting
            │
            ▼
Collaborative Task Recovery
            │
            ▼
Robot Motion
            │
            ▼
Task Completion
            │
            ▼
Next Decision Cycle
```

---

## Algorithms and Concepts Demonstrated

- Distributed Decision Making
- Consensus Voting
- Temporary Leadership
- Autonomous Task Allocation
- Energy-Aware Scheduling
- Failure Recovery
- Multi-Agent Coordination
- Swarm Robotics Principles
- Dynamic Task Reallocation
- Motion Planning
- Cooperative Robotics

---

## Future Enhancements

- Conflict-Based Search (CBS)
- Time-Expanded A*
- Adaptive Swarm Intelligence
- Multi-Robot Path Planning
- Dynamic Obstacle Avoidance
- Inter-Robot Communication
- ROS 2 Integration
- Gazebo Simulation
- Warehouse Digital Twin
- Reinforcement Learning
- Task Deadline Optimization
- Battery Charging Stations
- SLAM Integration
- Fleet Visualization Dashboard
- Real Robot Deployment

---

## Applications

- Warehouse Automation
- Industrial Robotics
- Autonomous Mobile Robots
- Swarm Robotics
- Smart Manufacturing
- Logistics Automation
- Search and Rescue Robotics
- Autonomous Fleet Coordination
- Multi-Agent Artificial Intelligence
- Robotics Research
- Intelligent Factory Systems
- Autonomous Systems Education

---

## Requirements

- Python 3.8 or later

---

## Dependencies

This project uses only Python's built-in standard library modules.

- math
- random
- time

---

## Author

Kaushal Jammula

Graduate | Former Vice President @Aprameya | Entrepreneur | Focused - Automotive Systems Specialist | Space Tech Enthusiast | Researcher | Emerging Tech Innovator| Engineering Beyond Limits

GitHub: https://github.com/Kaushal1525
````
