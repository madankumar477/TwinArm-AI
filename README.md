# TwinArm-AI

TwinArm-AI is a robotics portfolio project demonstrating the Physical AI concept: one Dobot Magician arm (follower) mirrors the real-time motion of a second Dobot (leader).

## Project overview

- Leader endpoint captures pose from `/dev/ttyACM0`.
- Follower endpoint receives commands on `/dev/ttyACM1`.
- Y offset is applied to follower pose for safe workspace separation.
- Rotation is fixed to prevent twist instability.

## Features

- Real-time leader-to-follower mirroring with `pydobot`.
- Safe offsets and fixed rotation control.
- Simple core logic in `mirror_dobot.py`.
- Extensible for PID, smoothing, and multi-axis adaptation.

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/TwinArm-AI.git
cd TwinArm-AI
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Hardware setup

1. Place two Dobot Magician arms in non-colliding working zones.
2. Connect leader to USB `/dev/ttyACM0`.
3. Connect follower to USB `/dev/ttyACM1`.
4. Power on both units and make sure they are homed in a safe pose.

## Calibration

- Measure and adjust `Y_OFFSET` in `mirror_dobot.py` until safe separation is achieved.
- Make small moves and verify follower tracks leader before full-speed operation.
- Use `DobotStudio` or manufacturer tools to zero encoders and verify coordinates.

## Serial port configuration

- Leader: `/dev/ttyACM0` (or `COM3` on Windows)
- Follower: `/dev/ttyACM1` (or `COM4` on Windows)
- `pydobot` supports direct serial connection through `Dobot(port, baudrate=115200)`.

## Usage

```bash
python mirror_dobot.py
```

- The program loops indefinitely; stop with `Ctrl+C`.
- Adjust `Y_OFFSET` and `FIXED_R` in the script as needed.

## System architecture

- Single script, leader reading and follower command path.
- Low-latency 50ms control loop in the baseline implementation.
- Ideal extension: state smoothing and safety limit checks.

## Demo video / GIF (placeholder)

Add demo materials here:

- `![Demo](docs/demo.gif)`
- `https://youtu.be/YOUR_VIDEO_LINK`

---

## License

MIT
