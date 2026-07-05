import random
import math
import time

# ==============================
# CONFIGURATION
# ==============================
NUM_ROBOTS = 20
NUM_TASKS = 8
PLANT_SIZE = 120
MAX_SPEED = 1.8
SAFE_DIST = 3.0

FAILURE_PROB = 0.04
LOW_ENERGY_THRESHOLD = 25

CYCLE_DELAY = 3.0
STEP_DELAY = 1.5

# ==============================
# ROBOT
# ==============================
class Robot:
    def __init__(self, rid):
        self.id = rid
        self.x = random.uniform(0, PLANT_SIZE)
        self.y = random.uniform(0, PLANT_SIZE)
        self.vx = 0
        self.vy = 0
        self.task = None
        self.load = 0
        self.energy = random.randint(40, 100)
        self.failed = False
        self.leader = False

    def dist(self, x, y):
        return math.hypot(self.x - x, self.y - y)

# ==============================
# TASK
# ==============================
class Task:
    def __init__(self, tid):
        self.id = tid
        self.x = random.uniform(10, PLANT_SIZE - 10)
        self.y = random.uniform(10, PLANT_SIZE - 10)
        self.priority = random.randint(1, 5)
        self.owner = None
        self.done = False

# ==============================
# CONSENSUS VOTING
# ==============================
def consensus_vote(task, robots):
    print("\n🗳️  Consensus voting initiated for Task", task.id)
    time.sleep(STEP_DELAY)

    votes = []
    for r in robots:
        if r.failed or r.task is not None:
            continue
        score = r.dist(task.x, task.y) + (100 - r.energy)
        votes.append((score, r))
        print(f"   Robot {r.id:02d} voted with score {score:.1f}")
        time.sleep(0.5)

    if not votes:
        print("❌ No eligible robots for consensus")
        return None

    winner = min(votes, key=lambda x: x[0])[1]
    print(f"🏆 Consensus winner: Robot {winner.id:02d}")
    time.sleep(STEP_DELAY)
    return winner

# ==============================
# TEMPORARY LEADER EMERGENCE
# ==============================
def elect_temporary_leader(robots):
    candidates = [r for r in robots if not r.failed]
    leader = max(candidates, key=lambda r: r.energy)
    leader.leader = True

    print(f"\n⭐ Temporary leader emerged: Robot {leader.id:02d}")
    time.sleep(STEP_DELAY)
    return leader

# ==============================
# ENERGY-AWARE TASK CLAIM
# ==============================
def attempt_task_claim(robot, tasks):
    if robot.failed or robot.task is not None:
        return

    if robot.energy < LOW_ENERGY_THRESHOLD:
        print(f"🔋 Robot {robot.id:02d} refused task due to low energy ({robot.energy}%)")
        time.sleep(0.7)
        return

    free_tasks = [t for t in tasks if not t.done and t.owner is None]
    if not free_tasks:
        return

    chosen = min(
        free_tasks,
        key=lambda t: robot.dist(t.x, t.y) - t.priority * 2
    )

    chosen.owner = robot.id
    robot.task = chosen
    robot.load += chosen.priority

    print(f"🤖 Robot {robot.id:02d} autonomously selected Task {chosen.id}")
    time.sleep(STEP_DELAY)

# ==============================
# FAILURE & COLLABORATIVE RECOVERY
# ==============================
def induce_failure(robot):
    if robot.failed or robot.task is None:
        return False
    if random.random() < FAILURE_PROB:
        robot.failed = True
        return True
    return False

def collaborative_recovery(failed_robot, robots):
    lost_task = failed_robot.task
    print(f"\n⚠️  FAILURE DETECTED")
    print(f"❌ Robot {failed_robot.id:02d} failed during Task {lost_task.id}")
    time.sleep(STEP_DELAY)

    leader = elect_temporary_leader(robots)

    helper = consensus_vote(lost_task, robots)

    if helper:
        helper.task = lost_task
        helper.load += lost_task.priority
        lost_task.owner = helper.id
        print(f"🤝 Task {lost_task.id} reassigned to Robot {helper.id:02d}")
        time.sleep(STEP_DELAY)

    leader.leader = False
    failed_robot.task = None

# ==============================
# MOTION & EXECUTION
# ==============================
def execute(robot):
    if robot.failed or robot.task is None:
        return

    dx = robot.task.x - robot.x
    dy = robot.task.y - robot.y

    robot.vx += dx * 0.025
    robot.vy += dy * 0.025

    speed = math.hypot(robot.vx, robot.vy)
    if speed > MAX_SPEED:
        robot.vx = (robot.vx / speed) * MAX_SPEED
        robot.vy = (robot.vy / speed) * MAX_SPEED

    robot.x += robot.vx
    robot.y += robot.vy

    robot.energy -= 0.3

    if math.hypot(dx, dy) < 2:
        print(f"✅ Robot {robot.id:02d} completed Task {robot.task.id}")
        robot.task.done = True
        robot.task = None
        time.sleep(STEP_DELAY)

# ==============================
# DASHBOARD
# ==============================
def dashboard(step, robots):
    print(f"\n🏭 COLLABORATIVE DECISION CYCLE {step}")
    print("-" * 80)
    for r in robots:
        if r.failed:
            state = "FAILED"
        elif r.task:
            state = f"TASK-{r.task.id}"
        else:
            state = "IDLE"

        print(f"Robot {r.id:02d} | Pos({r.x:6.1f},{r.y:6.1f}) | "
              f"Energy {r.energy:3.0f}% | Load {r.load:2d} | {state}")

# ==============================
# MAIN LOOP
# ==============================
robots = [Robot(i) for i in range(NUM_ROBOTS)]
tasks = [Task(i) for i in range(NUM_TASKS)]

for step in range(40):
    dashboard(step, robots)
    time.sleep(CYCLE_DELAY)

    for r in robots:
        attempt_task_claim(r, tasks)

    for r in robots:
        if induce_failure(r):
            collaborative_recovery(r, robots)

    for r in robots:
        execute(r)
